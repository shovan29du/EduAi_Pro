#!/usr/bin/env python3
"""Live link check that writes a report a person can act on.

Used by .github/workflows/link-check.yml (weekly) but runnable by hand:

    python3 backend/scripts/link_check_report.py --out-dir link-report

What it checks
  * a bounded sample of URLs per host from the syllabus and data files
    (same sampling as audit_resource_links.py); each failure is retried
    before it is called broken, and the data files that contain it are listed;
  * every Wikipedia article the museum links to (batched MediaWiki API calls,
    50 titles per request) and every Wikimedia Commons image file it uses.

Outputs link_report.md and link_report.json in --out-dir. Exit status is 1
when broken links are found, so a scheduled run can open an issue; network
trouble is reported as "inconclusive" and never fails the run.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_resource_links as audit  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MUSEUM_PATH = DATA_DIR / "virtual_museum" / "museum.json"
SKIP_DATA = {"resource_link_audit.json", "eduai_pro.db"}
API_HEADERS = {"User-Agent": "EduAI-Pro-Link-Audit/1.0 (+educational catalogue)"}
BATCH = 50


# ── collecting ────────────────────────────────────────────────────────────────
def json_files() -> list[Path]:
    files = sorted(audit.SYLLABUS_DIR.glob("*.json"))
    for path in sorted(DATA_DIR.rglob("*.json")):
        rel = path.relative_to(DATA_DIR)
        if path.name in SKIP_DATA or rel.parts[0] in {"museum_thumbnail_cache", "museum_credit_cache", "news_cache", "lesson_examples", "problem_reports"}:
            continue
        files.append(path)
    return files


def collect_sources(files: list[Path]) -> dict[str, list[str]]:
    """url -> up to three data files containing it."""
    sources: dict[str, list[str]] = defaultdict(list)
    for path in files:
        urls: list[str] = []
        audit.collect_strings(json.loads(path.read_text(encoding="utf-8")), urls)
        name = str(path.relative_to(ROOT))
        for url in set(urls):
            if len(sources[url]) < 3:
                sources[url].append(name)
    return sources


def museum_titles() -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """(wikipedia titles, commons file names) -> ids of up to three objects using them."""
    wiki: dict[str, list[str]] = defaultdict(list)
    commons: dict[str, list[str]] = defaultdict(list)

    def add(bucket, key, object_id):
        if key and len(bucket[key]) < 3 and object_id not in bucket[key]:
            bucket[key].append(object_id)

    data = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    for gallery in data["galleries"].values():
        for obj in gallery["objects"]:
            add(wiki, (obj.get("wiki_title") or "").replace("_", " ").strip(), obj["id"])
            article = (obj.get("links") or {}).get("wikipedia") or ""
            if "/wiki/" in article:
                add(wiki, unquote(article.split("/wiki/", 1)[1]).replace("_", " ").split("#")[0], obj["id"])
            thumb = obj.get("thumbnail_local") or ""
            if "/Special:FilePath/" in thumb:
                add(commons, unquote(thumb.split("/Special:FilePath/", 1)[1]).replace("_", " "), obj["id"])
    return wiki, commons


# ── checking ──────────────────────────────────────────────────────────────────
def check_with_retry(url: str, checker=audit.live_check, retries: int = 1, delay: float = 2.0) -> dict:
    result = checker(url)
    attempt = 0
    while result["reachable"] is not True and attempt < retries:
        time.sleep(delay)
        result = checker(url)
        attempt += 1
    return result


DEAD_STATUSES = {404, 410}
NO_SUCH_HOST = ("name or service not known", "nodename nor servname", "getaddrinfo failed", "no address associated")


def classify(result: dict) -> dict:
    """Decide whether a failed check is really a broken link.

    Only "gone" (404/410) and "domain does not exist" count as broken. Other
    4xx codes (bots are often answered with 400/406/418/999) and 5xx errors are
    inconclusive, so the weekly report doesn't cry wolf.
    """
    if result["reachable"] is True:
        return result
    status, error = result.get("status"), str(result.get("error", "")).lower()
    if status in DEAD_STATUSES:
        return {**result, "reachable": False, "reason": f"HTTP {status}"}
    if status is None and any(marker in error for marker in NO_SUCH_HOST):
        return {**result, "reachable": False, "reason": "domain does not exist"}
    detail = f"HTTP {status}" if status is not None else result.get("error", "unreachable")
    return {**result, "reachable": None, "error": f"{detail} (not treated as broken)"}


def check_urls(urls: list[str], workers: int, checker=audit.live_check, delay: float = 2.0) -> list[dict]:
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        results = [classify(r) for r in pool.map(lambda u: check_with_retry(u, checker, delay=delay), urls)]
    # If many hosts "don't exist" the runner's DNS is the problem, not the links.
    dns_failures = [r for r in results if r.get("reason") == "domain does not exist"]
    if len(dns_failures) > max(5, len(results) // 4):
        results = [
            {**r, "reachable": None, "error": "DNS failures on many hosts - likely a runner network problem"}
            if r.get("reason") == "domain does not exist" else r
            for r in results
        ]
    return results


def _fetch_json(url: str) -> dict:
    with urlopen(Request(url, headers=API_HEADERS), timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def find_missing_titles(api: str, titles: list[str], prefix: str = "", fetch=_fetch_json) -> tuple[list[str], list[str]]:
    """Titles with no page on a MediaWiki site, plus titles that could not be checked."""
    missing, unchecked = [], []
    ordered = sorted(titles)
    for start in range(0, len(ordered), BATCH):
        chunk = ordered[start:start + BATCH]
        query = "|".join(prefix + t for t in chunk)
        url = f"{api}?action=query&redirects=1&format=json&titles={quote(query, safe='')}"
        try:
            payload = fetch(url).get("query", {})
        except Exception:
            unchecked.extend(chunk)
            continue
        alias = {}
        for entry in payload.get("normalized", []):
            alias[entry["from"]] = entry["to"]
        for entry in payload.get("redirects", []):
            alias[entry["from"]] = entry["to"]
        gone = {page["title"] for page in payload.get("pages", {}).values() if "missing" in page}
        for title in chunk:
            name = prefix + title
            for _ in range(3):  # normalised name, then redirect target
                name = alias.get(name, name)
            if name in gone:
                missing.append(title)
    return missing, unchecked


# ── reporting ─────────────────────────────────────────────────────────────────
def build_report(checks, sources, wiki_missing, wiki_unchecked, commons_missing, commons_unchecked, wiki, commons, totals) -> dict:
    broken = [
        {**c, "found_in": sources.get(c["url"], [])}
        for c in checks if c["reachable"] is False
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **totals,
        "urls_checked": len(checks),
        "urls_ok": sum(c["reachable"] is True for c in checks),
        "broken": sorted(broken, key=lambda b: b["url"]),
        "inconclusive": sorted(
            ({"url": c["url"], "error": c.get("error", "")} for c in checks if c["reachable"] is None),
            key=lambda i: i["url"],
        ),
        "wikipedia_missing": [{"title": t, "objects": wiki.get(t, [])} for t in sorted(wiki_missing)],
        "wikipedia_unchecked": len(wiki_unchecked),
        "commons_missing": [{"file": t, "objects": commons.get(t, [])} for t in sorted(commons_missing)],
        "commons_unchecked": len(commons_unchecked),
    }


def has_problems(report: dict) -> bool:
    return bool(report["broken"] or report["wikipedia_missing"] or report["commons_missing"])


def render_markdown(report: dict, limit: int = 200) -> str:
    lines = [
        "# Link check report",
        "",
        f"Generated {report['generated_at']}.",
        "",
        "| Check | Result |",
        "|---|---|",
        f"| Sampled external URLs | {report['urls_checked']} checked, {report['urls_ok']} reachable, "
        f"{len(report['broken'])} broken, {len(report['inconclusive'])} inconclusive |",
        f"| Museum Wikipedia articles | {report['wikipedia_titles']} checked, {len(report['wikipedia_missing'])} missing"
        f"{', ' + str(report['wikipedia_unchecked']) + ' not checked' if report['wikipedia_unchecked'] else ''} |",
        f"| Museum Commons images | {report['commons_files']} checked, {len(report['commons_missing'])} missing"
        f"{', ' + str(report['commons_unchecked']) + ' not checked' if report['commons_unchecked'] else ''} |",
        "",
    ]
    incomplete = (
        len(report["inconclusive"]) * 2 > max(1, report["urls_checked"])
        or report["wikipedia_unchecked"] or report["commons_unchecked"]
    )
    if not has_problems(report):
        lines += ["No broken links found." + (" :white_check_mark:" if not incomplete else ""), ""]
    if incomplete:
        lines += [
            "> **Incomplete check:** many links could not be reached from the machine that ran this report "
            "(network trouble, blocked hosts or timeouts). Absence of broken links above does not mean the "
            "unchecked ones are fine - see the inconclusive list and re-run.",
            "",
        ]

    def clipped(items):
        return items[:limit], max(0, len(items) - limit)

    if report["broken"]:
        shown, more = clipped(report["broken"])
        lines += ["## Broken links", "", "| URL | Status | Found in |", "|---|---|---|"]
        lines += [f"| {b['url']} | {b.get('reason') or b['status']} | {', '.join(b['found_in']) or '-'} |" for b in shown]
        lines += [f"| ...and {more} more | | |"] if more else []
        lines.append("")
    if report["wikipedia_missing"]:
        shown, more = clipped(report["wikipedia_missing"])
        lines += ["## Museum: Wikipedia articles that no longer exist", "", "| Title | Museum objects |", "|---|---|"]
        lines += [f"| {m['title']} | {', '.join(m['objects'])} |" for m in shown]
        lines += [f"| ...and {more} more | |"] if more else []
        lines.append("")
    if report["commons_missing"]:
        shown, more = clipped(report["commons_missing"])
        lines += ["## Museum: Commons images that no longer exist", "", "| File | Museum objects |", "|---|---|"]
        lines += [f"| {m['file']} | {', '.join(m['objects'])} |" for m in shown]
        lines += [f"| ...and {more} more | |"] if more else []
        lines.append("")
    if report["inconclusive"]:
        lines += [
            f"<details><summary>{len(report['inconclusive'])} inconclusive (timeouts or network errors; not counted as broken)</summary>",
            "",
        ]
        lines += [f"- {i['url']} - {i['error']}" for i in report["inconclusive"][:50]]
        lines += ["", "</details>", ""]
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", default="link-report")
    parser.add_argument("--per-host", type=int, default=5)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--skip-museum", action="store_true")
    args = parser.parse_args(argv)

    files = json_files()
    sources = collect_sources(files)
    valid = {u for u in sources if audit.valid_url(u)}
    malformed = sorted(u for u in sources if not audit.valid_url(u))
    sample = audit.representative_urls(valid, max(1, args.per_host))
    print(f"{len(files)} data files, {len(sources)} unique URLs, checking a sample of {len(sample)}", flush=True)
    checks = check_urls(sample, args.workers)

    wiki, commons = ({}, {}) if args.skip_museum else museum_titles()
    wiki_missing, wiki_unchecked = find_missing_titles("https://en.wikipedia.org/w/api.php", list(wiki)) if wiki else ([], [])
    commons_missing, commons_unchecked = (
        find_missing_titles("https://commons.wikimedia.org/w/api.php", list(commons), prefix="File:") if commons else ([], [])
    )
    totals = {
        "data_files": len(files), "unique_urls": len(sources), "malformed_urls": malformed,
        "wikipedia_titles": len(wiki), "commons_files": len(commons),
    }
    report = build_report(checks, sources, wiki_missing, wiki_unchecked, commons_missing, commons_unchecked, wiki, commons, totals)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "link_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown = render_markdown(report)
    (out / "link_report.md").write_text(markdown + "\n", encoding="utf-8")
    print(markdown)
    return 1 if (has_problems(report) or malformed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
