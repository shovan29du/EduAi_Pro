"""Database storage for Virtual Museum pictures and deleted objects.

Pictures (downloaded from the web, or uploaded by the owner) live in the
``museum_pictures`` table, so they are backed up and moved with the rest of the
database. Deleted objects live in ``museum_deleted_objects`` rather than in
museum.json, so a deletion survives an app update that replaces the catalogue.

Everything here fails soft for *reading* (a database problem means "no stored
picture", never a broken museum page); writes raise so the caller can say why.
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, select

from app import database
from app.models import MuseumDeletedObject, MuseumPicture

MAX_BYTES = 8 * 1024 * 1024
MIN_BYTES = 200
EXTENSIONS = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}
_INDEX_TTL = 30.0
_lock = threading.Lock()
_index: dict = {"at": 0.0, "pictures": {}, "deleted": set()}


def sniff(data: bytes) -> str | None:
    """The image type from the file's own first bytes (never from a name or header)."""
    if data[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def invalidate() -> None:
    with _lock:
        _index["at"] = 0.0


def _refresh() -> dict:
    with _lock:
        if time.time() - _index["at"] < _INDEX_TTL:
            return _index
    try:
        with database.session_scope() as db:
            pictures = {
                row.object_id: {"v": int(row.updated_at.timestamp()) if row.updated_at else 0,
                                "source": row.source, "credit": row.credit or {}, "gallery": row.gallery}
                for row in db.execute(select(MuseumPicture.object_id, MuseumPicture.updated_at, MuseumPicture.source,
                                             MuseumPicture.credit, MuseumPicture.gallery))
            }
            deleted = {(row.gallery, row.object_id) for row in db.execute(
                select(MuseumDeletedObject.gallery, MuseumDeletedObject.object_id))}
    except Exception:
        return _index  # keep the last good copy; try again next time
    with _lock:
        _index.update(at=time.time(), pictures=pictures, deleted=deleted)
        return _index


def stored_pictures() -> dict:
    """{object_id: {v, source, credit, gallery}} for every stored picture."""
    return _refresh()["pictures"]


def deleted_objects() -> set:
    """{(gallery, object_id)} the owner has deleted."""
    return _refresh()["deleted"]


def has_picture(object_id: str) -> bool:
    return object_id in stored_pictures()


def get_picture(object_id: str):
    """(bytes, content_type, sha1) or None."""
    try:
        with database.session_scope() as db:
            row = db.get(MuseumPicture, object_id)
            return (row.data, row.content_type, row.sha1) if row else None
    except Exception:
        return None


def save_picture(object_id: str, gallery: str, data: bytes, *, source: str, source_url: str = "",
                 filename: str = "", credit: dict | None = None) -> dict:
    """Store (or replace) an object's picture. Raises ValueError for anything that is not a usable picture."""
    if not data or len(data) < MIN_BYTES:
        raise ValueError("That file is empty or too small to be a picture.")
    if len(data) > MAX_BYTES:
        raise ValueError(f"That picture is too large (limit {MAX_BYTES // (1024 * 1024)} MB).")
    content_type = sniff(data)
    if not content_type:
        raise ValueError("Only JPEG, PNG, WebP and GIF pictures can be used.")
    fields = dict(gallery=gallery or "", content_type=content_type, data=data, size=len(data),
                  sha1=hashlib.sha1(data).hexdigest(), source=source, source_url=source_url or None,
                  filename=(filename or "")[:300] or None, credit=credit or {},
                  updated_at=datetime.now(timezone.utc))
    with database.session_scope() as db:
        row = db.get(MuseumPicture, object_id)
        if row:
            for key, value in fields.items():
                setattr(row, key, value)
        else:
            db.add(MuseumPicture(object_id=object_id, **fields))
    invalidate()
    return {"object_id": object_id, "content_type": content_type, "size": len(data), "source": source}


def delete_picture(object_id: str) -> bool:
    with database.session_scope() as db:
        removed = db.execute(delete(MuseumPicture).where(MuseumPicture.object_id == object_id)).rowcount
    invalidate()
    return bool(removed)


def mark_deleted(gallery: str, object_id: str, name: str = "") -> None:
    with database.session_scope() as db:
        if not db.get(MuseumDeletedObject, (gallery, object_id)):
            db.add(MuseumDeletedObject(gallery=gallery, object_id=object_id, name=(name or "")[:300]))
    invalidate()


def import_legacy_files(images_dir: Path, manifest_path: Path) -> int:
    """Move pictures saved as files by the older downloader into the database (once each).

    The files are left where they are; a picture already in the database is not touched.
    """
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return 0
    have = set(stored_pictures())
    added = 0
    for object_id, entry in manifest.items():
        if object_id in have:
            continue
        try:
            data = (images_dir / entry["file"]).read_bytes()
            credit = {k: entry.get(k) for k in ("credit", "license", "license_url", "source_url", "line")}
            save_picture(object_id, "", data, source="download", source_url=entry.get("image_url") or "",
                         filename=entry["file"], credit=credit)
            added += 1
        except (OSError, KeyError, ValueError):
            continue
    return added
