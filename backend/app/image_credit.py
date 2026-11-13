"""Credit and licence information for museum photos.

Photos come from Wikimedia Commons (reusable under per-file licences that
usually require attribution) and the Cleveland Museum of Art Open Access
programme (CC0). Commons licence data is read from the file's `extmetadata`
and cached on disk, like the museum thumbnails.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import time
from pathlib import Path
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen

from fastapi import APIRouter

router = APIRouter(prefix="/api/museum", tags=["museum"])

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "museum_credit_cache"
CACHE_TTL_SECONDS = 30 * 24 * 3600
HEADERS = {
    "Api-User-Agent": "EduAI/1.0 (educational; contact@eduai.app)",
    "User-Agent": "EduAI/1.0 (educational; contact@eduai.app)",
}
CC0_URL = "https://creativecommons.org/publicdomain/zero/1.0/"


def commons_filename(image_url: str) -> str | None:
    """File name on Commons for a Special:FilePath or upload.wikimedia.org URL."""
    parsed = urlparse(image_url)
    path = parsed.path
    if parsed.netloc == "commons.wikimedia.org" and "/Special:FilePath/" in path:
        return unquote(path.split("/Special:FilePath/", 1)[1]) or None
    if parsed.netloc == "upload.wikimedia.org" and path.startswith("/wikipedia/commons/"):
        parts = [unquote(p) for p in path.split("/")[3:]]  # after /wikipedia/commons/
        if parts and parts[0] == "thumb":
            parts = parts[1:]
            return parts[2] if len(parts) >= 3 else None
        return parts[2] if len(parts) >= 3 else None
    return None


def _clean(value: str | None) -> str | None:
    if not value:
        return None
    text = re.sub(r"<[^>]+>", "", value)
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return text or None


def _commons_credit(filename: str) -> dict:
    title = quote("File:" + filename.replace(" ", "_"), safe=":_(),'!-.")
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata"
        f"&format=json&titles={title}"
    )
    with urlopen(Request(url, headers=HEADERS), timeout=5) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    pages = (payload.get("query") or {}).get("pages") or {}
    meta = {}
    for page in pages.values():
        meta = ((page.get("imageinfo") or [{}])[0]).get("extmetadata") or {}
    value = lambda key: _clean((meta.get(key) or {}).get("value"))  # noqa: E731
    return {
        "artist": value("Artist"),
        "credit": value("Credit"),
        "license": value("LicenseShortName"),
        "license_url": value("LicenseUrl"),
        "attribution_required": (value("AttributionRequired") or "").lower() == "true",
        "source_url": "https://commons.wikimedia.org/wiki/File:" + quote(filename.replace(" ", "_"), safe="_(),'!-."),
    }


def _cma_credit(image_url: str) -> dict:
    accession = urlparse(image_url).path.strip("/").split("/")[0]
    return {
        "artist": None,
        "credit": "Cleveland Museum of Art",
        "license": "CC0 1.0 (Open Access)",
        "license_url": CC0_URL,
        "attribution_required": False,
        "source_url": f"https://clevelandart.org/art/{accession}" if accession else "https://clevelandart.org/open-access",
    }


def credit_for(image_url: str) -> dict | None:
    """Credit record for an image URL, or None when the source is unknown.
    Raises on network failure so callers don't cache a blank result."""
    host = urlparse(image_url).netloc
    if host.endswith("clevelandart.org"):
        return _cma_credit(image_url)
    filename = commons_filename(image_url)
    if filename:
        return _commons_credit(filename)
    return None


def credit_line(record: dict) -> str:
    who = record.get("artist") or record.get("credit")
    parts = [p for p in (who, record.get("license")) if p]
    return " · ".join(parts)


@router.get("/credit")
def museum_image_credit(image: str = ""):
    image = image.strip()
    empty = {"image": image, "known": False, "line": "", "artist": None, "license": None, "license_url": None, "source_url": None}
    if not image.startswith("http"):
        return empty
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / (hashlib.sha1(image.encode("utf-8")).hexdigest() + ".json")
    if cache_path.exists():
        try:
            record = json.loads(cache_path.read_text(encoding="utf-8"))
            if time.time() - record.get("fetched_at", 0) < CACHE_TTL_SECONDS:
                return record["response"]
        except (OSError, ValueError, KeyError):
            pass
    try:
        record = credit_for(image)
    except Exception:
        return empty  # transient failure: don't cache
    if record is None:
        response = empty
    else:
        response = {
            "image": image, "known": True, "line": credit_line(record),
            "artist": record.get("artist"), "license": record.get("license"),
            "license_url": record.get("license_url"), "source_url": record.get("source_url"),
            "attribution_required": record.get("attribution_required", False),
        }
    try:
        cache_path.write_text(json.dumps({"fetched_at": time.time(), "response": response}), encoding="utf-8")
    except OSError:
        pass
    return response
