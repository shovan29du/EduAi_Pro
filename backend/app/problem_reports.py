"""'Report a problem' store for lessons, museum objects and other content.

Local JSON index storage (same convention as lesson_planner.py). Reports are
written by learners and read by the app owner in the Users tab.
"""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.safety import safety_filter

router = APIRouter(prefix="/api/reports", tags=["reports"])

REPORTS_DIR = Path(__file__).resolve().parent.parent / "data" / "problem_reports"
MAX_REPORTS = 2000
KINDS = ("lesson", "museum_object", "stem_experiment", "other")
CATEGORIES = ("wrong_information", "broken_link", "wrong_or_missing_image", "typo", "inappropriate", "other")
_lock = Lock()


class ReportIn(BaseModel):
    kind: str
    item_id: str = Field(min_length=1, max_length=200)
    title: str = Field(default="", max_length=300)
    context: str = Field(default="", max_length=300)
    category: str = "other"
    message: str = Field(default="", max_length=2000)
    reporter: str = Field(default="", max_length=80)


class ReportStatusIn(BaseModel):
    status: str


def _index_path() -> Path:
    return REPORTS_DIR / "index.json"


def _load() -> list[dict]:
    path = _index_path()
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


def _save(records: list[dict]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    _index_path().write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")


@router.post("")
def create_report(body: ReportIn):
    if body.kind not in KINDS:
        raise HTTPException(status_code=422, detail=f"kind must be one of {KINDS}")
    if body.category not in CATEGORIES:
        raise HTTPException(status_code=422, detail=f"category must be one of {CATEGORIES}")
    message = body.message.strip()
    if body.category == "other" and len(message) < 3:
        raise HTTPException(status_code=422, detail="Please describe the problem.")
    record = {
        "id": uuid.uuid4().hex[:12],
        "kind": body.kind,
        "item_id": body.item_id.strip(),
        "title": body.title.strip(),
        "context": body.context.strip(),
        "category": body.category,
        "message": safety_filter.sanitize(message, strict=True) if message else "",
        "reporter": body.reporter.strip(),
        "status": "open",
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with _lock:
        records = _load()
        records.append(record)
        # Keep the newest reports; resolved ones are dropped first when full.
        if len(records) > MAX_REPORTS:
            overflow = len(records) - MAX_REPORTS
            resolved = [r for r in records if r["status"] == "resolved"][:overflow]
            drop = {r["id"] for r in resolved}
            records = [r for r in records if r["id"] not in drop][-MAX_REPORTS:]
        _save(records)
    return record


@router.get("")
def list_reports(status: str = ""):
    records = _load()
    if status:
        records = [r for r in records if r["status"] == status]
    records.sort(key=lambda r: r["created_at"], reverse=True)
    return {"reports": records, "open_count": sum(1 for r in _load() if r["status"] == "open")}


@router.patch("/{report_id}")
def update_report(report_id: str, body: ReportStatusIn):
    if body.status not in ("open", "resolved"):
        raise HTTPException(status_code=422, detail="status must be 'open' or 'resolved'")
    with _lock:
        records = _load()
        for record in records:
            if record["id"] == report_id:
                record["status"] = body.status
                _save(records)
                return record
    raise HTTPException(status_code=404, detail="Report not found")
