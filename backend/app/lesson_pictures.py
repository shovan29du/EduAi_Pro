"""Pictures for lessons (Survival Skills, Practical Skills and subject lessons).

A lesson shows the closest Wikipedia picture by default (see lesson_enrichment).
The owner can give it pictures of their own, as many as they like:

* *Download* searches many free image collections (see image_search), shows the
  pictures found, each marked with how well it fits the lesson's topic and
  description, and saves the ones the owner picks.
* *Upload* saves pictures from the owner's computer.

Saved pictures live in the database (``lesson_picture_items``) and are shown
instead of the automatic one.

A lesson is identified by a key such as ``survival/personal_safety/Stranger
Awareness``, ``practical/cooking/Baking Cookies`` or ``subject/UG1/math-ug1-l3``.
"""
from __future__ import annotations

import hashlib
import hmac
import ipaddress
import secrets
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from urllib.parse import quote, unquote, urlparse

from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, Field
from sqlalchemy import delete, func, select

from app import database, image_credit, image_search, lesson_enrichment, museum_pictures, museum_store
from app.models import LessonPicture, LessonPictureItem

router = APIRouter(prefix="/api/lesson-picture", tags=["lessons"])
KINDS = ("survival", "practical", "subject")
MAX_PER_LESSON = 12
MAX_CANDIDATES = 18
# Only pictures this server found can be saved: each carries a signature made with a secret
# that exists only in this running process, so the save call cannot be used to fetch arbitrary addresses.
_SECRET = secrets.token_bytes(32)


def sign(url: str) -> str:
    return hmac.new(_SECRET, (url or "").encode("utf-8"), hashlib.sha256).hexdigest()[:32]


def public_url(url: str) -> bool:
    parsed = urlparse(url or "")
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in ("http", "https") or not host or host == "localhost" or host.endswith(".local"):
        return False
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return True
    return not (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved)


def valid_key(key: str) -> str:
    key = (key or "").strip()
    kind, _, rest = key.partition("/")
    if kind not in KINDS or not rest or len(key) > 400:
        raise HTTPException(status_code=400, detail="Not a valid lesson key.")
    return key


# ── what is stored ────────────────────────────────────────────────────────────
def _describe(row) -> dict:
    credit = row.credit or {}
    version = int(row.updated_at.timestamp()) if row.updated_at else 0
    return {
        "id": row.id, "url": f"/api/lesson-picture/{row.id}/image?v={version}", "source": row.source,
        "title": row.title or ("Your uploaded picture" if row.source == "upload" else "Downloaded picture"),
        "source_name": credit.get("source_name") or "", "page_url": credit.get("page_url") or "",
        "credit": credit if credit.get("line") else None, "filename": row.filename or "",
    }


def pictures(key: str) -> list[dict]:
    try:
        with database.session_scope() as db:
            rows = db.execute(select(LessonPictureItem).where(LessonPictureItem.key == key)
                              .order_by(LessonPictureItem.position, LessonPictureItem.created_at)).scalars().all()
            return [_describe(r) for r in rows]
    except Exception:
        return []


def stored_response(key: str) -> dict | None:
    """The lesson's saved pictures in the shape of a Wikipedia article (first picture) plus the full list, or None."""
    items = pictures(key)
    if not items:
        return None
    first = items[0]
    return {"available": True, "stored": True, "source": first["source"], "title": first["title"], "description": "",
            "extract": "", "thumbnail_url": first["url"], "page_url": first["page_url"], "source_name": first["source_name"],
            "credit": first["credit"], "pictures": items}


def add_picture(key: str, data: bytes, *, source: str, source_url: str = "", filename: str = "", title: str = "",
                credit: dict | None = None) -> dict | None:
    """Add a picture to a lesson. Returns it, or None when the lesson already has exactly this picture.
    Raises ValueError for anything that is not a usable picture or when the lesson is full."""
    if not data or len(data) < museum_store.MIN_BYTES:
        raise ValueError("That file is empty or too small to be a picture.")
    if len(data) > museum_store.MAX_BYTES:
        raise ValueError(f"That picture is too large (limit {museum_store.MAX_BYTES // (1024 * 1024)} MB).")
    content_type = museum_store.sniff(data)
    if not content_type:
        raise ValueError("Only JPEG, PNG, WebP and GIF pictures can be used.")
    sha1 = hashlib.sha1(data).hexdigest()
    with database.session_scope() as db:
        existing = db.execute(select(LessonPictureItem.sha1).where(LessonPictureItem.key == key)).scalars().all()
        if sha1 in existing:
            return None
        if len(existing) >= MAX_PER_LESSON:
            raise ValueError(f"A lesson can have up to {MAX_PER_LESSON} pictures. Remove one first.")
        row = LessonPictureItem(key=key, position=len(existing), content_type=content_type, data=data, size=len(data),
                                sha1=sha1, source=source, source_url=source_url or None,
                                filename=(filename or "")[:300] or None, title=(title or "")[:300], credit=credit or {},
                                updated_at=datetime.now(timezone.utc))
        db.add(row)
        db.flush()
        return _describe(row)


def import_legacy_single_pictures() -> int:
    """Move pictures saved by the earlier one-picture-per-lesson version into the new table (once each)."""
    moved = 0
    try:
        with database.session_scope() as db:
            old = db.execute(select(LessonPicture)).scalars().all()
            have = set(db.execute(select(LessonPictureItem.key).distinct()).scalars().all())
            for row in old:
                if row.key in have:
                    continue
                credit = row.credit or {}
                db.add(LessonPictureItem(key=row.key, position=0, content_type=row.content_type, data=row.data, size=row.size,
                                         sha1=row.sha1, source=row.source, source_url=row.source_url, filename=row.filename,
                                         title=credit.get("title") or "", credit=credit))
                moved += 1
    except Exception:
        return 0
    return moved


# ── serving, uploading, removing ──────────────────────────────────────────────
@router.get("/list")
def list_pictures(key: str):
    return {"key": valid_key(key), "pictures": pictures(valid_key(key)), "max": MAX_PER_LESSON}


@router.get("/{item_id}/image")
def get_image(item_id: str, request: Request):
    try:
        with database.session_scope() as db:
            row = db.get(LessonPictureItem, item_id)
            found = (row.data, row.content_type, row.sha1) if row else None
    except Exception:
        found = None
    if not found:
        raise HTTPException(status_code=404, detail="No stored picture")
    data, content_type, sha1 = found
    headers = {"ETag": f'"{sha1}"', "Cache-Control": "public, max-age=86400", "X-Content-Type-Options": "nosniff"}
    if request.headers.get("if-none-match") == headers["ETag"]:
        return Response(status_code=304, headers=headers)
    return Response(content=data, media_type=content_type, headers=headers)


@router.put("")
async def upload_picture(key: str, request: Request):
    """Upload a picture for a lesson (added to the ones it has): the request body is the image file itself."""
    key = valid_key(key)
    declared = request.headers.get("content-length")
    if declared and declared.isdigit() and int(declared) > museum_store.MAX_BYTES + 1024:
        raise HTTPException(status_code=413, detail="That picture is too large (limit 8 MB).")
    data = await request.body()
    filename = unquote(request.headers.get("x-filename", ""))
    try:
        added = add_picture(key, data, source="upload", filename=filename, title=filename.rsplit(".", 1)[0] or "Your uploaded picture",
                            credit={"credit": "Uploaded by the owner", "line": "Picture uploaded by the owner of this app"})
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"added": added is not None, "duplicate": added is None, **(stored_response(key) or {})}


@router.delete("/{item_id}")
def remove_picture(item_id: str):
    try:
        with database.session_scope() as db:
            row = db.get(LessonPictureItem, item_id)
            if not row:
                raise HTTPException(status_code=404, detail="No such picture")
            key = row.key
            db.execute(delete(LessonPictureItem).where(LessonPictureItem.id == item_id))
    except HTTPException:
        raise
    return {"removed": True, **(stored_response(key) or {"stored": False, "pictures": []}), "key": key}


# ── finding pictures on the web, then saving the ones the owner picks ─────────
class SearchIn(BaseModel):
    key: str
    title: str = Field(default="", max_length=300)
    context: str = Field(default="", max_length=100)
    wiki_title: str = Field(default="", max_length=200)
    description: str = Field(default="", max_length=800)
    exclude: list[str] = Field(default_factory=list, max_length=100)


def _queries(body: SearchIn) -> list[str]:
    title = body.title.strip() or body.wiki_title.strip()
    queries = [title]
    if body.context.strip():
        queries.append(f"{title} {body.context.strip()}")
    extra = sorted(image_search.tokens(body.description) - image_search.tokens(title))[:2]
    if extra:
        queries.append(f"{title} {' '.join(extra)}")
    return list(dict.fromkeys(queries))


def find_candidates(body: SearchIn, problems: list) -> list[dict]:
    topic = {"title": body.title.strip() or body.wiki_title.strip(), "description": body.description, "context": body.context}
    out = []
    try:
        article = lesson_enrichment.find_article(body.wiki_title.strip(), body.title.strip(), body.context.strip())
    except Exception as exc:
        article = None
        problems.append(f"wikipedia: {exc}")
    if article and article.get("thumbnail_url"):
        try:
            record = image_credit.credit_for(article["thumbnail_url"]) or {}
        except Exception:
            record = {}
        hit = {"source": "Wikipedia", "url": article["thumbnail_url"], "fallback_url": "", "title": article["title"],
               "text": f"{article.get('description', '')} {article.get('extract', '')}",
               "credit": {"credit": record.get("artist") or record.get("credit"), "license": record.get("license"),
                          "license_url": record.get("license_url"), "source_url": article.get("page_url") or record.get("source_url"),
                          "line": image_credit.credit_line(record) if record else "Picture from Wikipedia"}}
        hit["score"] = image_search.relevance(hit, topic["title"], topic["description"], topic["context"])
        hit["match"] = image_search.match_label(hit["score"])
        out.append(hit)
    queries = _queries(body)
    with ThreadPoolExecutor(max_workers=len(queries)) as pool:
        found = list(pool.map(lambda q: image_search.search(q, topic=topic, log=problems), queries))
    seen = {h["url"] for h in out}
    for hits in found:
        for hit in hits:
            if hit["url"] not in seen:
                seen.add(hit["url"])
                out.append(hit)
    skip = set(body.exclude)
    out = [h for h in out if h["url"] not in skip]
    out.sort(key=lambda h: -h["score"])
    return out[:MAX_CANDIDATES]


def _candidate(hit: dict) -> dict:
    return {"url": hit["url"], "token": sign(hit["url"]), "fallback_url": hit.get("fallback_url") or "",
            "fallback_token": sign(hit["fallback_url"]) if hit.get("fallback_url") else "",
            "title": hit["title"], "source": hit["source"], "score": hit.get("score", 0), "match": hit.get("match", ""),
            "credit": hit["credit"], "page_url": hit["credit"].get("source_url") or ""}


@router.post("/search")
def search_pictures(body: SearchIn):
    """Pictures for the lesson from every free collection, best fit first. Nothing is saved yet."""
    valid_key(body.key)
    if not (body.title.strip() or body.wiki_title.strip()):
        raise HTTPException(status_code=400, detail="title is required")
    problems: list = []
    found = find_candidates(body, problems)
    if not found and len({p.split(":")[0] for p in problems}) >= 4:  # nearly every source failed: it is the connection
        raise HTTPException(status_code=502, detail="Could not reach the picture sources. Check the Internet connection and try again.")
    return {"candidates": [_candidate(h) for h in found], "max": MAX_PER_LESSON, "saved": len(pictures(body.key))}


class PickedIn(BaseModel):
    url: str
    token: str
    fallback_url: str = ""
    fallback_token: str = ""
    title: str = Field(default="", max_length=300)
    source: str = Field(default="", max_length=100)
    credit: dict = Field(default_factory=dict)
    page_url: str = Field(default="", max_length=1000)


class SaveIn(BaseModel):
    key: str
    pictures: list[PickedIn] = Field(min_length=1, max_length=MAX_PER_LESSON)


@router.post("/save")
def save_pictures(body: SaveIn):
    """Download the pictures the owner picked and add them to the lesson."""
    key = valid_key(body.key)
    saved, skipped, failed = 0, 0, []
    for pick in body.pictures:
        urls = [u for u, t in ((pick.url, pick.token), (pick.fallback_url, pick.fallback_token))
                if u and hmac.compare_digest(sign(u), t or "") and public_url(u)]
        if not urls:
            failed.append({"title": pick.title, "reason": "This picture was not found by a search (search again)."})
            continue
        data, used = None, ""
        for url in urls:
            try:
                data, _ = museum_pictures._fetch_image(url)
                used = url
                break
            except Exception:
                continue
        if data is None:
            failed.append({"title": pick.title, "reason": "Could not download it."})
            continue
        credit = {k: pick.credit.get(k) for k in ("credit", "license", "license_url", "source_url", "line")}
        credit.update(title=pick.title, page_url=pick.page_url or credit.get("source_url") or "", source_name=pick.source)
        try:
            added = add_picture(key, data, source="download", source_url=used, title=pick.title, credit=credit)
        except ValueError as exc:
            failed.append({"title": pick.title, "reason": str(exc)})
            continue
        saved, skipped = (saved + 1, skipped) if added else (saved, skipped + 1)
    if not saved and not skipped:
        raise HTTPException(status_code=502, detail="Could not download the picked pictures: " + "; ".join(f["reason"] for f in failed))
    return {"saved": saved, "already_saved": skipped, "failed": failed, **(stored_response(key) or {})}
