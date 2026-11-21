"""Pictures for lessons (Survival Skills, Practical Skills and subject lessons).

A lesson shows the closest Wikipedia picture by default (see lesson_enrichment).
The owner can replace it: *Download* saves a picture found on the web, *Upload*
saves one from their computer. Both are stored in the database
(``lesson_pictures``) and then shown instead of the automatic one.

A lesson is identified by a key such as ``survival/personal_safety/Stranger
Awareness``, ``practical/cooking/Baking Cookies`` or ``subject/UG1/math-ug1-l3``.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from urllib.parse import quote, unquote

from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, Field

from app import database, image_credit, lesson_enrichment, museum_pictures, museum_store
from app.models import LessonPicture

router = APIRouter(prefix="/api/lesson-picture", tags=["lessons"])
KINDS = ("survival", "practical", "subject")


def valid_key(key: str) -> str:
    key = (key or "").strip()
    kind, _, rest = key.partition("/")
    if kind not in KINDS or not rest or len(key) > 400:
        raise HTTPException(status_code=400, detail="Not a valid lesson key.")
    return key


def stored_response(key: str) -> dict | None:
    """The lesson's stored picture in the same shape as a Wikipedia article, or None."""
    try:
        with database.session_scope() as db:
            row = db.get(LessonPicture, key)
            if not row:
                return None
            credit = row.credit or {}
            version = int(row.updated_at.timestamp()) if row.updated_at else 0
            source, source_url = row.source, row.source_url
    except Exception:
        return None
    return {
        "available": True, "stored": True, "source": source,
        "title": credit.get("title") or ("Your uploaded picture" if source == "upload" else "Downloaded picture"),
        "description": "", "extract": "",
        "thumbnail_url": f"/api/lesson-picture?key={quote(key, safe='')}&v={version}",
        "page_url": credit.get("page_url") or "",
        "credit": credit if credit.get("line") else None,
    }


def save(key: str, data: bytes, *, source: str, source_url: str = "", filename: str = "", credit: dict | None = None) -> dict:
    if not data or len(data) < museum_store.MIN_BYTES:
        raise ValueError("That file is empty or too small to be a picture.")
    if len(data) > museum_store.MAX_BYTES:
        raise ValueError(f"That picture is too large (limit {museum_store.MAX_BYTES // (1024 * 1024)} MB).")
    content_type = museum_store.sniff(data)
    if not content_type:
        raise ValueError("Only JPEG, PNG, WebP and GIF pictures can be used.")
    fields = dict(kind=key.partition("/")[0], content_type=content_type, data=data, size=len(data),
                  sha1=hashlib.sha1(data).hexdigest(), source=source, source_url=source_url or None,
                  filename=(filename or "")[:300] or None, credit=credit or {}, updated_at=datetime.now(timezone.utc))
    with database.session_scope() as db:
        row = db.get(LessonPicture, key)
        if row:
            for name, value in fields.items():
                setattr(row, name, value)
        else:
            db.add(LessonPicture(key=key, **fields))
    return stored_response(key)


@router.get("")
def get_picture(key: str, request: Request):
    key = valid_key(key)
    try:
        with database.session_scope() as db:
            row = db.get(LessonPicture, key)
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
    """Upload a picture for a lesson: the request body is the image file itself."""
    key = valid_key(key)
    declared = request.headers.get("content-length")
    if declared and declared.isdigit() and int(declared) > museum_store.MAX_BYTES + 1024:
        raise HTTPException(status_code=413, detail="That picture is too large (limit 8 MB).")
    data = await request.body()
    try:
        return save(key, data, source="upload", filename=unquote(request.headers.get("x-filename", "")),
                    credit={"title": "Your uploaded picture", "credit": "Uploaded by the owner",
                            "line": "Picture uploaded by the owner of this app"})
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


class DownloadIn(BaseModel):
    key: str
    title: str = Field(default="", max_length=300)
    context: str = Field(default="", max_length=100)
    wiki_title: str = Field(default="", max_length=200)


@router.post("/download")
def download_picture(body: DownloadIn):
    """Find a picture for the lesson on the web (the closest Wikipedia article with a free picture) and save it."""
    key = valid_key(body.key)
    if not (body.title.strip() or body.wiki_title.strip()):
        raise HTTPException(status_code=400, detail="title is required")
    try:
        article = lesson_enrichment.find_article(body.wiki_title.strip(), body.title.strip(), body.context.strip())
    except Exception:
        raise HTTPException(status_code=502, detail="Could not reach the picture sources. Check the Internet connection and try again.")
    if not article or not article.get("thumbnail_url"):
        raise HTTPException(status_code=404, detail="No picture was found for this lesson. You can upload one instead.")
    url = article["thumbnail_url"]
    try:
        data, _ = museum_pictures._fetch_image(url)
    except Exception:
        raise HTTPException(status_code=502, detail="Found a picture but could not download it. Check the Internet connection and try again.")
    try:
        record = image_credit.credit_for(url) or {}
    except Exception:
        record = {}
    credit = {"title": article["title"], "page_url": article.get("page_url", ""), "credit": record.get("artist") or record.get("credit"),
              "license": record.get("license"), "license_url": record.get("license_url"), "source_url": record.get("source_url"),
              "line": image_credit.credit_line(record) if record else "Picture from Wikipedia"}
    try:
        return save(key, data, source="download", source_url=url, credit=credit)
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
