"""Real pictures for Virtual Museum objects.

Three pieces work together:

* ``met_thumbnail`` finds the picture of a Metropolitan Museum object through the
  Met's open-access API (public-domain images only, CC0), cached on disk.
* A *manifest* (data/museum_resource/pictures.json) lists pictures that have been
  downloaded to data/museum_resource/images/. ``overlay`` points an object at its
  local file, so the museum works offline and loads fast.
* ``download_pictures`` fills the manifest. It is run by
  backend/scripts/museum_download_pictures.py on a computer with Internet access.
  It works from the links an object already has (its museum page, its Wikipedia
  article, its Wikidata item) before searching by name, handles objects with no
  picture first, and ``check_links`` reports which of those links are broken.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import time
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse
from urllib.request import Request, urlopen

from app import image_credit, image_search, museum_store

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
    """The object with its stored picture (and credit) attached, if there is one.

    A picture in the database wins; older pictures saved as files are still shown.
    """
    stored = museum_store.stored_pictures().get(obj.get("id"))
    if stored:
        credit = stored.get("credit") or {}
        return {**obj, "thumbnail_local": f"/api/museum/picture/{quote(obj['id'], safe='')}?v={stored['v']}",
                "picture_source": stored.get("source"),
                "image_credit": {k: credit.get(k) for k in ("credit", "license", "license_url", "source_url", "line")}}
    entry = manifest().get(obj.get("id"))
    if not entry or not (IMAGES_DIR / entry["file"]).exists():
        return obj
    return {**obj, "thumbnail_local": f"/museum-resource/images/{entry['file']}",
            "image_credit": {k: entry.get(k) for k in ("credit", "license", "license_url", "source_url", "line")}}


# ── finding a picture from the links an object already has ────────────────────
IMAGE_URL = re.compile(r"\.(jpe?g|png|webp|gif)(\?|$)", re.I)
_META = re.compile(r"<meta\b[^>]*>", re.I)
_ATTR = re.compile(r"""([a-zA-Z:_-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""")


def _fetch_text(url: str, limit: int = 1_000_000) -> str:
    with urlopen(Request(url, headers={**HEADERS, "Accept": "text/html,*/*"}), timeout=15) as resp:
        return resp.read(limit).decode("utf-8", "replace")


def page_image_url(page_url: str, page_html: str | None = None) -> str | None:
    """The picture a web page advertises (og:image / twitter:image), as an absolute URL."""
    page_html = page_html if page_html is not None else _fetch_text(page_url)
    for tag in _META.findall(page_html):
        attrs = {m[0].lower(): html.unescape(m[1] or m[2]) for m in _ATTR.findall(tag)}
        if (attrs.get("property") or attrs.get("name") or "").lower() in ("og:image", "og:image:url", "twitter:image") and attrs.get("content"):
            return urljoin(page_url, attrs["content"].strip())
    return None


def wikipedia_title(url: str) -> str | None:
    """'https://en.wikipedia.org/wiki/Rosetta_Stone' -> 'Rosetta Stone' (None for search pages and other sites)."""
    parsed = urlparse(url or "")
    if not parsed.netloc.endswith("wikipedia.org") or not parsed.path.startswith("/wiki/"):
        return None
    return unquote(parsed.path[len("/wiki/"):]).replace("_", " ").strip() or None


def wikidata_image_url(qid: str) -> str | None:
    """The picture (property P18) of a Wikidata item, as a Wikimedia Commons URL."""
    record = _get_json(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
    claims = (record.get("entities", {}).get(qid, {}).get("claims", {})).get("P18") or []
    name = claims and claims[0].get("mainsnak", {}).get("datavalue", {}).get("value")
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(name.replace(' ', '_'))}?width=900" if name else None


def candidate_sources(obj: dict):
    """Places to look for an object's picture, most precise first: (kind, value)."""
    links = obj.get("links") or {}
    for key in ("thumbnail_local", "image", "image_url"):
        if re.match(r"https?://", obj.get(key) or ""):
            yield "image_url", obj[key]
    if links.get("image") and IMAGE_URL.search(links["image"]):
        yield "image_url", links["image"]
    if obj.get("met_id"):
        yield "met_api", obj["met_id"]
    page = links.get("museum_object") or ""
    cma = re.match(r"https?://(?:www\.)?clevelandart\.org/art/([\w.-]+)", page)
    if cma:
        yield "image_url", f"https://openaccess-cdn.clevelandart.org/{cma.group(1)}/{cma.group(1)}_web.jpg"
    elif page and not obj.get("met_id") and "metmuseum.org" not in page:
        yield "museum_page", page
    title = wikipedia_title(links.get("wikipedia") or "")
    if title:
        yield "wikipedia_article", title
    qid = re.search(r"(Q\d+)", links.get("wikidata") or "")
    if qid:
        yield "wikidata_item", qid.group(1)
    if obj.get("wiki_title") and obj["wiki_title"] != title:
        yield "wikipedia_article", obj["wiki_title"]
    yield "name_search", " ".join(x for x in (obj.get("name"), obj.get("origin")) if x)
    yield "web_search", obj.get("name") or ""  # every free image collection, not only Wikipedia


def _credit_for(url: str):
    try:
        return image_credit.credit_for(url)
    except Exception:
        return None


def _resolve(kind: str, value, obj: dict, wiki_lookup) -> tuple[str | None, dict | None]:
    if kind == "image_url":
        return value, _credit_for(value)
    if kind == "met_api":
        url = met_thumbnail(value)["thumbnail_url"]
        return (url, met_credit(value)) if url else (None, None)
    if kind == "museum_page":
        url = page_image_url(value)
        host = urlparse(value).netloc
        # The page does not state a licence we can read, so say so: the credit points back to the page.
        return (url, {"credit": host, "license": None, "source_url": value,
                      "line": f"Image from {host}: check its terms before reuse"}) if url else (None, None)
    if kind == "wikipedia_article":
        url = wiki_lookup(value, "")
    elif kind == "wikidata_item":
        url = wikidata_image_url(value)
    else:  # name_search
        url = wiki_lookup("", value)
    return (url, _credit_for(url)) if url else (None, None)


def find_picture_url(obj: dict, wiki_lookup, tried: list | None = None, skip=()) -> tuple[str | None, dict | None, str | None]:
    """(image url, credit, how it was found). A source that fails or has no picture is skipped, not fatal;
    `tried` collects what was attempted, for the 'still missing' report. Pictures whose URL is in `skip`
    (ones already used or that would not download) are passed over."""
    for kind, value in candidate_sources(obj):
        try:
            if kind == "web_search":
                problems: list = []
                topic = {"title": obj.get("name") or "", "description": (obj.get("description") or "")[:400],
                         "context": obj.get("origin") or ""}
                # Only pictures whose own words fit the object (name and description); ones that do not are left out.
                hits = [h for h in image_search.search(value, order=image_search.ARTWORKS, log=problems, topic=topic)
                        if h["url"] not in skip and h.get("score", 1.0) >= image_search.POSSIBLE]
                if problems and tried is not None:
                    tried.extend(f"web_search {p}" for p in problems)
                if hits:
                    return hits[0]["url"], {**hits[0]["credit"], "found_in": hits[0]["source"]}, kind
                if tried is not None:
                    tried.append("web_search: no picture")
                continue
            url, credit = _resolve(kind, value, obj, wiki_lookup)
        except Exception as exc:
            if tried is not None:
                tried.append(f"{kind}: {exc}")
            continue
        if url and url not in skip:
            return url, credit, kind
        if tried is not None:
            tried.append(f"{kind}: no picture")
    return None, None, None


def has_picture(obj: dict) -> bool:
    """True if the object already shows a real picture (a web URL or a downloaded copy)."""
    if museum_store.has_picture(obj.get("id")):
        return True
    entry = manifest().get(obj.get("id"))
    if entry and (IMAGES_DIR / entry["file"]).exists():
        return True
    return bool(re.match(r"https?://", obj.get("thumbnail_local") or ""))


def prioritise(objects) -> list[dict]:
    """Objects with no picture at all first, then Met objects (found by ID), then those that only need
    their existing picture downloaded."""
    def tier(obj):
        if has_picture(obj):
            return 2
        return 1 if obj.get("met_id") else 0
    return sorted(objects, key=tier)  # stable: the museum's own order is kept within a tier


# ── checking links ────────────────────────────────────────────────────────────
CHECKED_LINKS = ("museum_object", "wikipedia", "wikidata", "podcast", "museum_channel")


def checkable_links(obj: dict) -> dict:
    """The links worth checking: those pointing at a specific page (search pages always answer 200)."""
    out = {}
    for key in CHECKED_LINKS:
        url = (obj.get("links") or {}).get(key)
        parsed = urlparse(url or "")
        is_search = ("search" in parsed.query or "q=" in parsed.query or parsed.path.rstrip("/").endswith("/search")
                     or "/results" in parsed.path)
        if url and not is_search:
            out[key] = url
    return out


def check_link(url: str) -> dict:
    """{'status': int | None, 'ok': bool, 'error': str | None}. Tries HEAD, then GET when HEAD is refused."""
    last = None
    for method in ("HEAD", "GET"):
        try:
            req = Request(url, headers={**HEADERS, "Accept": "*/*"}, method=method)
            with urlopen(req, timeout=15) as resp:
                return {"status": resp.status, "ok": 200 <= resp.status < 400, "error": None}
        except Exception as exc:
            code = getattr(exc, "code", None)
            last = {"status": code, "ok": False, "error": f"{type(exc).__name__}: {exc}"}
            if code in (404, 410):
                return last
    return last


def check_links(objects, sleep: float = 0.2, log=print) -> dict:
    """Check every object's own links. Returns {object id: {link: result}} and writes the report next to the manifest."""
    report_path = MANIFEST_PATH.with_name("link_report.json")
    report: dict = {}
    for n, obj in enumerate(objects, 1):
        for key, url in checkable_links(obj).items():
            result = {**check_link(url), "url": url, "checked_at": int(time.time())}
            report.setdefault(obj["id"], {})[key] = result
            if not result["ok"]:
                log(f"  broken {key}: {obj['id']} {url} ({result['status'] or result['error']})")
            time.sleep(sleep)
        if n % 100 == 0:
            log(f"  {n} objects checked")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


# ── downloading ───────────────────────────────────────────────────────────────
def _fetch_image(url: str) -> tuple[bytes, str]:
    with urlopen(Request(url, headers=HEADERS), timeout=30) as resp:
        data = resp.read()
        kind = (resp.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    if kind not in EXTENSIONS or len(data) < 2000:
        raise ValueError(f"not an image ({kind or 'unknown type'}, {len(data)} bytes)")
    return data, EXTENSIONS[kind]


class NoPicture(Exception):
    """None of the places searched had a picture for the object."""

    def __init__(self, tried: list):
        super().__init__("no picture found")
        self.tried = tried


def download_for(obj: dict, wiki_lookup, gallery: str = "") -> dict:
    """Find a picture for one object anywhere on the web's free image collections and store it in the database.

    The object's own links are tried first (see ``candidate_sources``), then Wikipedia and Commons by name,
    then every other collection (Openverse, museum collections, NASA, Library of Congress). Calling it again
    for an object that already has a downloaded picture gives the next different picture. Raises NoPicture
    (with what was tried) or the error that stopped the download.
    """
    tried: list = []
    previous = (museum_store.stored_pictures().get(obj["id"]) or {}).get("credit") or {}
    skip = list(previous.get("tried") or [])
    for _ in range(8):  # a picture that will not download is skipped for the next one
        url, credit, how = find_picture_url(obj, wiki_lookup, tried, skip)
        if not url and skip:
            skip = []  # seen them all: start over
            url, credit, how = find_picture_url(obj, wiki_lookup, tried, skip)
        if not url:
            raise NoPicture(tried)
        try:
            data, _ = _fetch_image(url)
            break
        except Exception as exc:
            tried.append(f"download: {exc}")
            skip.append(url)
    else:
        raise NoPicture(tried)
    credit = credit or {}
    stored_credit = {"credit": credit.get("artist") or credit.get("credit"), "license": credit.get("license"),
                     "license_url": credit.get("license_url"), "source_url": credit.get("source_url") or url,
                     "line": credit.get("line") or (image_credit.credit_line(credit) if credit else ""),
                     "found_via": how, "found_in": credit.get("found_in"), "tried": (skip + [url])[-30:]}
    museum_store.save_picture(obj["id"], gallery, data, source="download", source_url=url, credit=stored_credit)
    return {"found_via": how, "image_url": url, "credit": stored_credit}


def download_pictures(objects, wiki_lookup, limit: int = 0, sleep: float = 0.2, log=print, save_every: int = 25,
                      only_missing: bool = False) -> dict:
    """Download a picture for every object without one, starting with the objects that have none at all.

    Pictures go into the database. Each object's own links are tried first (see ``candidate_sources``).
    Resumable: finished objects are skipped and failures are retried on the next run. ``only_missing``
    skips objects that already show a picture from a web URL. Objects that still have no picture are
    listed, with what was tried, in pictures_missing.json. Returns counts."""
    stats = {"downloaded": 0, "no_picture": 0, "failed": 0, "skipped": 0}
    missing: dict = {}
    attempted = 0
    for obj in prioritise(objects):
        oid = obj.get("id")
        if museum_store.has_picture(oid) or (oid in manifest() and (IMAGES_DIR / manifest()[oid]["file"]).exists()):
            stats["skipped"] += 1
            continue
        if only_missing and has_picture(obj):
            stats["skipped"] += 1
            continue
        if limit and attempted >= limit:
            break
        attempted += 1
        try:
            download_for(obj, wiki_lookup, obj.get("gallery", ""))
            stats["downloaded"] += 1
        except NoPicture as exc:
            failed_download = any(t.startswith("download:") for t in exc.tried)
            stats["failed" if failed_download else "no_picture"] += 1
            missing[oid] = {"name": obj.get("name"), "tried": exc.tried}
            if failed_download:
                log(f"  {oid}: {exc.tried[-1]}")
        except Exception as exc:  # database or other unexpected problem: retry on the next run
            stats["failed"] += 1
            missing[oid] = {"name": obj.get("name"), "tried": [f"error: {exc}"]}
            log(f"  {oid}: {exc}")
        if attempted % save_every == 0:
            log(f"  {attempted} tried — {stats}")
        time.sleep(sleep)
    report = MANIFEST_PATH.with_name("pictures_missing.json")
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")
    return stats
