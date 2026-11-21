"""Real-world examples for curriculum lessons: vetted store, review queue, quiz.

The syllabus holds ~48,000 lessons whose reading text only *asks* students to
find a real-world example. Examples reach a student in this order:

1. **Vetted** -- drafts a person has approved (optionally edited) in the
   review queue. Stored per level in data/lesson_examples_vetted/ and
   committed to the repo, so every install serves the same reviewed text.
2. **On demand** -- written by the AI tutor the first time a lesson asks,
   cached, and dropped into the review queue so it can be vetted later.

Drafts can also be produced in bulk (POST /pregenerate here, or
backend/scripts/lesson_examples_cli.py for large batches).
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from threading import Lock

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app import ai_tutor
from app import levels as levels_module

router = APIRouter(prefix="/api/lesson-example", tags=["lessons"])

_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SYLLABUS_DIR = Path(__file__).resolve().parent.parent / "syllabus"
CACHE_DIR = _DATA_DIR / "lesson_examples"
VETTED_DIR = _DATA_DIR / "lesson_examples_vetted"
PENDING_DIR = _DATA_DIR / "lesson_examples_pending"
MAX_PREGENERATE = 25
_lock = Lock()


# ── storage helpers ───────────────────────────────────────────────────────────
def level_key(level) -> str:
    key = re.sub(r"[^a-z0-9_]", "", levels_module.normalize_level_id(level).lower())
    return key or "general"


def _read(directory: Path, level) -> dict:
    path = directory / f"{level_key(level)}.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _write(directory: Path, level, records: dict) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{level_key(level)}.json"
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def get_vetted(level, lesson_id: str) -> dict | None:
    return _read(VETTED_DIR, level).get(lesson_id) if lesson_id else None


def add_pending(level, lesson_id: str, title: str, subject: str, example: str, cache_file: str = "") -> bool:
    """Queue a draft for review. Returns False if it is already vetted/queued."""
    if not lesson_id:
        return False
    with _lock:
        if lesson_id in _read(VETTED_DIR, level):
            return False
        pending = _read(PENDING_DIR, level)
        if lesson_id in pending:
            return False
        pending[lesson_id] = {"example": example, "title": title, "subject": subject, "created_at": time.time()}
        if cache_file:
            pending[lesson_id]["cache_file"] = cache_file
        _write(PENDING_DIR, level, pending)
    return True


def review_flags(example: str) -> list[str]:
    """Automatic hints telling a reviewer what to look at; never auto-rejects."""
    flags = []
    if len(example) < 120:
        flags.append("very short")
    if len(example) > 900:
        flags.append("very long")
    if re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", example):
        flags.append("contains a year - check it")
    if re.search(r"\d+(\.\d+)?\s?(%|per cent|percent|million|billion)", example):
        flags.append("contains a statistic - check it")
    return flags


def _cache_path(lesson_id: str, title: str, subject: str, level: str) -> Path:
    key = "|".join((lesson_id, title, subject, level)).lower()
    return CACHE_DIR / f"{hashlib.sha1(key.encode('utf-8')).hexdigest()}.json"


def iter_lessons(level, subject: str = ""):
    """Yield (subject_name, lesson) for a level's syllabus file."""
    path = SYLLABUS_DIR / levels_module.syllabus_filename(str(level))
    if not path.exists():
        raise FileNotFoundError(path.name)
    data = json.loads(path.read_text(encoding="utf-8"))
    for subject_name, content in data.get("subjects", {}).items():
        if subject and subject_name.lower() != subject.lower():
            continue
        for lesson in content.get("lessons") or []:
            if lesson.get("id") and lesson.get("title"):
                yield subject_name, lesson


def pregenerate(level, subject: str = "", limit: int = MAX_PREGENERATE, on_progress=None) -> dict:
    """Draft examples for lessons with nothing vetted or queued. Stops at the
    first AI failure so a missing key doesn't burn through the whole list."""
    vetted, pending = _read(VETTED_DIR, level), _read(PENDING_DIR, level)
    created, remaining, unavailable = 0, 0, False
    for subject_name, lesson in iter_lessons(level, subject):
        if lesson["id"] in vetted or lesson["id"] in pending:
            continue
        if created >= limit or unavailable:
            remaining += 1
            continue
        example = ai_tutor.generate_real_world_example(
            lesson["title"], subject_name, level=str(level),
            key_concepts=lesson.get("key_concepts") or [],
            summary=(lesson.get("reading_material") or "").split("\n\n")[0],
        )
        if not example:
            unavailable = True
            remaining += 1
            continue
        add_pending(level, lesson["id"], lesson["title"], subject_name, example)
        created += 1
        if on_progress:
            on_progress(created, lesson)
    return {"created": created, "remaining": remaining, "unavailable": unavailable}


# ── API ───────────────────────────────────────────────────────────────────────
@router.get("")
def lesson_example(
    title: str,
    subject: str = "",
    lesson_id: str = "",
    level: str = "",
    grade: int = 1,
    summary: str = "",
    concepts: str = "",
    vetted_only: bool = False,
):
    title, subject, level = title.strip()[:200], subject.strip()[:100], level.strip()[:20]
    lesson_id = lesson_id.strip()[:100]
    if len(title) < 2:
        raise HTTPException(status_code=400, detail="title is required")

    vetted = get_vetted(level, lesson_id)
    if vetted:
        return {"example": vetted["example"], "vetted": True, "cached": True}
    if vetted_only:
        return {"example": None, "vetted": False, "cached": False}

    path = _cache_path(lesson_id, title, subject, level)
    if path.exists():
        try:
            return {"example": json.loads(path.read_text(encoding="utf-8"))["example"], "vetted": False, "cached": True}
        except (OSError, ValueError, KeyError):
            pass
    key_concepts = [c.strip() for c in concepts.split(",") if c.strip()][:8]
    example = ai_tutor.generate_real_world_example(
        title, subject, grade=grade, level=level or None, key_concepts=key_concepts, summary=summary,
    )
    if not example:
        return {"example": None, "vetted": False, "cached": False, "unavailable": True}
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"example": example, "created_at": time.time()}), encoding="utf-8")
    except OSError:
        pass
    add_pending(level, lesson_id, title, subject, example, cache_file=path.name)
    return {"example": example, "vetted": False, "cached": False}


@router.get("/pending")
def pending_examples(level: str, limit: int = 20):
    pending = _read(PENDING_DIR, level)
    items = sorted(pending.items(), key=lambda kv: kv[1].get("created_at", 0))[: max(1, min(limit, 100))]
    return {
        "level": level_key(level),
        "pending_count": len(pending),
        "vetted_count": len(_read(VETTED_DIR, level)),
        "items": [
            {"lesson_id": lid, "title": rec.get("title", ""), "subject": rec.get("subject", ""),
             "example": rec["example"], "flags": review_flags(rec["example"])}
            for lid, rec in items
        ],
    }


class ReviewIn(BaseModel):
    level: str
    lesson_id: str = Field(min_length=1, max_length=100)
    action: str
    example: str = Field(default="", max_length=2000)


@router.post("/review")
def review_example(body: ReviewIn):
    if body.action not in ("approve", "reject"):
        raise HTTPException(status_code=422, detail="action must be 'approve' or 'reject'")
    with _lock:
        pending = _read(PENDING_DIR, body.level)
        draft = pending.pop(body.lesson_id, None)
        if draft is None:
            raise HTTPException(status_code=404, detail="No pending example for that lesson")
        if body.action == "approve":
            text = body.example.strip() or draft["example"]
            if len(text) < 40:
                raise HTTPException(status_code=422, detail="Example is too short to approve")
            vetted = _read(VETTED_DIR, body.level)
            vetted[body.lesson_id] = {
                "example": text, "title": draft.get("title", ""), "subject": draft.get("subject", ""),
                "edited": text != draft["example"], "approved_at": time.strftime("%Y-%m-%d"),
            }
            _write(VETTED_DIR, body.level, vetted)
        elif draft.get("cache_file"):
            # A rejected draft must not keep being served from the on-demand cache.
            (CACHE_DIR / Path(draft["cache_file"]).name).unlink(missing_ok=True)
        _write(PENDING_DIR, body.level, pending)
    return {"status": "approved" if body.action == "approve" else "rejected", "pending_count": len(pending)}


class PregenerateIn(BaseModel):
    level: str
    subject: str = ""
    limit: int = Field(default=10, ge=1, le=MAX_PREGENERATE)


@router.post("/pregenerate")
def pregenerate_examples(body: PregenerateIn):
    try:
        return pregenerate(body.level, body.subject.strip(), body.limit)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No syllabus for that level") from None


class QuizIn(BaseModel):
    example: str = Field(min_length=40, max_length=2000)
    title: str = Field(default="", max_length=200)
    subject: str = Field(default="", max_length=100)
    level: str = Field(default="", max_length=20)


@router.post("/quiz")
def example_quiz(body: QuizIn):
    """Two multiple-choice questions about one example, cached by its text."""
    digest = hashlib.sha1(body.example.strip().encode("utf-8")).hexdigest()
    path = CACHE_DIR / f"quiz_{digest}.json"
    if path.exists():
        try:
            return {"questions": json.loads(path.read_text(encoding="utf-8"))["questions"], "cached": True}
        except (OSError, ValueError, KeyError):
            pass
    text = f"Lesson: {body.title}\n\nReal-world example: {body.example.strip()}"
    raw = ai_tutor.generate_quiz_from_text(text, subject=body.subject, count=2, level=body.level or None)
    questions = [
        q for q in raw
        if q.get("answer") in q.get("options", {}) and len(q["options"]) >= 3
    ][:2]
    if not questions:
        return {"questions": [], "cached": False, "unavailable": True}
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"questions": questions}), encoding="utf-8")
    except OSError:
        pass
    return {"questions": questions, "cached": False}
