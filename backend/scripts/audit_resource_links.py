"""Audit every curriculum URL structurally and sample endpoints live.

Structural checks cover every occurrence.  Live checks are deliberately
bounded per host so the audit does not send tens of thousands of near-
duplicate search requests to Wikipedia, YouTube, or course providers.
"""

from __future__ import annotations

import argparse
import json
import ssl
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SYLLABUS_DIR = ROOT / "syllabus"
MOVIES_PATH = ROOT / "data" / "movies.json"
REPORT_PATH = ROOT / "data" / "resource_link_audit.json"


def collect_strings(value, output: list[str]) -> None:
    if isinstance(value, dict):
        for child in value.values():
            collect_strings(child, output)
    elif isinstance(value, list):
        for child in value:
            collect_strings(child, output)
    elif isinstance(value, str) and value.startswith(("http://", "https://")):
        output.append(value)


def valid_url(url: str) -> bool:
    parsed = urlsplit(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc) and " " not in url


def live_check(url: str) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": "EduAI-Pro-Link-Audit/1.0 (+educational catalogue)",
            "Range": "bytes=0-1024",
        },
    )
    try:
        with urlopen(request, timeout=15, context=ssl.create_default_context()) as response:
            return {"url": url, "status": response.status, "reachable": response.status < 500}
    except HTTPError as exc:
        # 401/403/429 confirm that the host/path exists but rejects automation.
        return {"url": url, "status": exc.code, "reachable": exc.code in {401, 403, 405, 429}}
    except (URLError, TimeoutError, OSError) as exc:
        # A transient network failure is inconclusive, not proof of a dead link.
        return {"url": url, "status": None, "reachable": None, "error": str(exc)[:240]}


def representative_urls(urls: set[str], per_host: int) -> list[str]:
    hosts: dict[str, list[str]] = defaultdict(list)
    for url in sorted(urls):
        hosts[urlsplit(url).netloc.lower()].append(url)
    selected = []
    for host_urls in hosts.values():
        if len(host_urls) <= per_host:
            selected.extend(host_urls)
            continue
        step = len(host_urls) / per_host
        selected.extend(host_urls[min(int(index * step), len(host_urls) - 1)] for index in range(per_host))
    return sorted(set(selected))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--per-host", type=int, default=5)
    parser.add_argument("--workers", type=int, default=24)
    args = parser.parse_args()

    occurrences: list[str] = []
    files = sorted(SYLLABUS_DIR.glob("*.json"))
    for path in files:
        collect_strings(json.loads(path.read_text(encoding="utf-8")), occurrences)
    unique_urls = set(occurrences)
    malformed = sorted(url for url in unique_urls if not valid_url(url))
    hosts = Counter(urlsplit(url).netloc.lower() for url in unique_urls if valid_url(url))

    movies = json.loads(MOVIES_PATH.read_text(encoding="utf-8"))["movies"]
    top_movies = [movie for movie in movies if movie.get("source_batch") == "bfi_sight_sound_2022_top_200"]
    thumbnail_issues = []
    for movie in top_movies:
        thumbnail = str(movie.get("thumbnail_url") or "")
        if not thumbnail.startswith("/movie-thumbnails/"):
            thumbnail_issues.append({"title": movie.get("title"), "issue": "missing local thumbnail URL"})
            continue
        local_path = ROOT / "data" / "movie_thumbnails" / Path(thumbnail).name
        if not local_path.is_file() or local_path.stat().st_size < 500:
            thumbnail_issues.append({"title": movie.get("title"), "issue": "thumbnail file missing or empty"})

    checks = []
    if args.live:
        sample = representative_urls({url for url in unique_urls if valid_url(url)}, max(1, args.per_host))
        # Check all original BFI preview URLs as well as the bounded curriculum sample.
        sample.extend(
            movie["preview_image"]
            for movie in top_movies
            if valid_url(str(movie.get("preview_image") or ""))
        )
        sample = sorted(set(sample))
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {executor.submit(live_check, url): url for url in sample}
            for future in as_completed(futures):
                checks.append(future.result())

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "syllabus_files": len(files),
        "url_occurrences_checked": len(occurrences),
        "unique_urls_checked": len(unique_urls),
        "unique_hosts": len(hosts),
        "malformed_urls": malformed,
        "top_hosts": hosts.most_common(30),
        "live_urls_checked": len(checks),
        "live_reachable": sum(item["reachable"] is True for item in checks),
        "live_unreachable": [item for item in checks if item["reachable"] is False],
        "live_inconclusive": [item for item in checks if item["reachable"] is None],
        "movie_top_200_count": len(top_movies),
        "movie_thumbnail_issues": thumbnail_issues,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key not in {"top_hosts", "live_unreachable"}}, indent=2))
    print(f"live_unreachable_count={len(report['live_unreachable'])}")
    if malformed or thumbnail_issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
