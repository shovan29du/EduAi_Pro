"""Real pictures for Virtual Museum objects.

Three pieces work together:

* ``met_thumbnail`` finds the picture of a Metropolitan Museum object through the
  Met's open-access API (public-domain images only, CC0), cached on disk.
* A *manifest* (data/museum_resource/pictures.json) lists pictures that have been
  downloaded to data/museum_resource/images/. ``overlay`` points an object at its
  local file, so the museum works offline and loads fast.
* ``download_pictures`` fills the manifest. It is run by
  backend/scripts/museum_download_pictures.py on a computer with Internet access.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from functools import lru_cache
from pathlib import Path
from urllib.request import Request, urlopen

from app import image_credit

DATA = Path(__file__).resolve().parent.parent / "data"
IMAGES_DIR = DATA / "museum_resource" / "images"
MANIFEST_PATH = DATA / "museum_resource" / "pictures.json"
CACHE_DIR = DATA / "museum_thumbnail_cache"
MET_API = "https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
MET_OPEN_ACCESS = "https://www.metmuseum.org/about-the-met/policies-and-documents/open-access"
CACHE_TTL = 5 * 24 * 3600
HEADERS = {"User-Agent": "EduAI/1.0 (educational; contact@eduai.app)", "Accept": "application/json,image/*"}
EXTENSIONS = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}


# ── Met open-access pictures ──────────────────────────────────────────────────
def _get_json(url: str) -> dict:
    with urlopen(Request(url, headers=HEADERS), timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def met_credit(object_id: int | str | None = None) -> dict:
    return {"artist": None, "credit": "The Metropolitan Museum of Art", "license": "CC0 1.0 (Open Access)",
            "license_url": image_credit.CC0_URL, "attribution_required": False,
            "source_url": f"https://www.metmuseum.org/art/collection/search/{object_id}" if object_id else MET_OPEN_ACCESS}


def met_thumbnail(object_id: int | str) -> dict:
    """{'thumbnail_url': str | None, 'available': bool}. Only public-domain pictures are returned.
    A failed lookup (network down) raises nothing and is *not* cached."""
    oid = str(int(object_id))
    path = CACHE_DIR / f"met_{oid}.json"
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if time.time() - cached["fetched_at"] < CACHE_TTL:
            return {"thumbnail_url": cached["thumbnail_url"], "cached": True}
    except (OSError, ValueError, KeyError):
        pass
    try:
        record = _get_json(MET_API.format(id=oid))
    except Exception:
        return {"thumbnail_url": None, "cached": False}
    url = None
    if record.get("isPublicDomain"):
        url = record.get("primaryImageSmall") or record.get("primaryImage") or None
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"fetched_at": time.time(), "thumbnail_url": url}), encoding="utf-8")
    except OSError:
        pass
    return {"thumbnail_url": url, "cached": False}


# ── local pictures (the manifest) ─────────────────────────────────────────────
@lru_cache(maxsize=2)
def _manifest(mtime: float) -> dict:
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def manifest() -> dict:
    try:
        return _manifest(MANIFEST_PATH.stat().st_mtime)
    except OSError:
        return {}


def overlay(obj: dict) -> dict:
    """The object with its downloaded picture (and credit) attached, if there is one."""
    entry = manifest().get(obj.get("id"))
    if not entry or not (IMAGES_DIR / entry["file"]).exists():
        return obj
    return {**obj, "thumbnail_local": f"/museum-resource/images/{entry['file']}",
            "image_credit": {k: entry.get(k) for k in ("credit", "license", "license_url", "source_url", "line")}}


# ── downloading ───────────────────────────────────────────────────────────────
def find_picture_url(obj: dict, wiki_lookup) -> tuple[str | None, dict | None]:
    """(image url, credit record) for an object, trying its most precise source first.

    `wiki_lookup(wiki_title, q)` returns a Wikipedia/Commons thumbnail URL or None."""
    if obj.get("met_id"):
        url = met_thumbnail(obj["met_id"])["thumbnail_url"]
        return (url, met_credit(obj["met_id"])) if url else (None, None)
    local = obj.get("thumbnail_local") or ""
    if re.match(r"https?://", local):
        try:
            return local, image_credit.credit_for(local)
        except Exception:
            return local, None
    url = wiki_lookup(obj.get("wiki_title") or "", " ".join(x for x in (obj.get("name"), obj.get("origin")) if x))
    if not url:
        return None, None
    try:
        return url, image_credit.credit_for(url)
    except Exception:
        return url, None


def _fetch_image(url: str) -> tuple[bytes, str]:
    with urlopen(Request(url, headers=HEADERS), timeout=30) as resp:
        data = resp.read()
        kind = (resp.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    if kind not in EXTENSIONS or len(data) < 2000:
        raise ValueError(f"not an image ({kind or 'unknown type'}, {len(data)} bytes)")
    return data, EXTENSIONS[kind]


def download_pictures(objects, wiki_lookup, limit: int = 0, sleep: float = 0.2, log=print, save_every: int = 25) -> dict:
    """Download a picture for every object without one. Resumable: finished objects are skipped,
    failures are retried on the next run. Returns counts."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    done = dict(manifest())
    stats = {"downloaded": 0, "no_picture": 0, "failed": 0, "skipped": 0}

    def save():
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        tmp = MANIFEST_PATH.with_suffix(".tmp")
        tmp.write_text(json.dumps(done, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(MANIFEST_PATH)

    attempted = 0
    for obj in objects:
        oid = obj.get("id")
        if oid in done and (IMAGES_DIR / done[oid]["file"]).exists():
            stats["skipped"] += 1
            continue
        if limit and attempted >= limit:
            break
        attempted += 1
        try:
            url, credit = find_picture_url(obj, wiki_lookup)
            if not url:
                stats["no_picture"] += 1
                continue
            data, ext = _fetch_image(url)
            name = re.sub(r"[^A-Za-z0-9_.-]", "_", oid) + ext
            (IMAGES_DIR / name).write_bytes(data)
            credit = credit or {}
            done[oid] = {"file": name, "source_url": credit.get("source_url") or url, "image_url": url,
                         "credit": credit.get("artist") or credit.get("credit"), "license": credit.get("license"),
                         "license_url": credit.get("license_url"), "line": image_credit.credit_line(credit) if credit else "",
                         "sha1": hashlib.sha1(data).hexdigest(), "fetched_at": int(time.time())}
            stats["downloaded"] += 1
        except Exception as exc:  # network error, rate limit, bad image: retry on the next run
            stats["failed"] += 1
            log(f"  {oid}: {exc}")
        if attempted % save_every == 0:
            save()
            log(f"  {attempted} tried — {stats}")
        time.sleep(sleep)
    save()
    return stats
