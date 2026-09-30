"""Idempotently import legacy EduAI_Pro JSON into the SQLAlchemy domain.

Run after ``alembic upgrade head``. Source JSON is read-only and remains as a
rollback/export source until the database-backed API cutover is complete.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from sqlalchemy import select

from app.curate import RESOURCE_KEYS
from app.database import session_scope
from app.levels import LEVELS, syllabus_filename
from app.models import AuditEvent, Course, LearningItem, Module, Resource, User

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SYLLABUS_DIR = BASE_DIR / "syllabus"


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result or "legacy-user"


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def upsert_user(session, name: str, role: str) -> User:
    email = f"{slug(name)}@legacy.local"
    user = session.scalar(select(User).where(User.email == email))
    if not user:
        user = User(email=email, display_name=name, role=role, settings={"legacy_import": True})
        session.add(user)
        session.flush()
    return user


def iter_resources(subject: dict):
    # Only the curated external-resource lists (books, videos, articles, etc.) --
    # not "lessons" or "quiz_bank", which are curriculum content served straight
    # from the syllabus JSON and were never meant to be duplicated as Resource rows.
    for resource_type in RESOURCE_KEYS:
        values = subject.get(resource_type)
        if not isinstance(values, list):
            continue
        for value in values:
            if not isinstance(value, dict):
                continue
            title = value.get("title") or value.get("name") or value.get("label")
            url = value.get("url") or value.get("link") or value.get("resource_link")
            body = value.get("body") or value.get("description") or value.get("summary") or ""
            if title or url or body:
                yield resource_type, str(title or url or "Untitled resource"), url, body, value


def _load_existing_resource_keys(session) -> dict:
    """Map course_id -> set of (title, kind, url) already imported.

    Loaded once up front instead of re-querying the (ever-growing) resources
    table with an unindexed JSON-path filter for every subject -- that
    per-subject query was the dominant cost on a re-run against a
    populated database.
    """
    existing_by_course: dict = {}
    for item in session.scalars(select(Resource)):
        course_id = (item.metadata_json or {}).get("course_id")
        existing_by_course.setdefault(course_id, set()).add((item.title, item.kind, item.url))
    return existing_by_course


def migrate(dry_run: bool = False) -> dict:
    stats = {"users": 0, "courses": 0, "resources": 0, "progress_records": 0}
    with session_scope() as session:
        users = load_json(DATA_DIR / "users.json", {"children": [], "parents": []})
        imported_users = {}
        for name in users.get("children", []):
            imported_users[name] = upsert_user(session, name, "learner")
            stats["users"] += 1
        for name in users.get("parents", []):
            imported_users[name] = upsert_user(session, name, "admin")
            stats["users"] += 1

        existing_by_course = _load_existing_resource_keys(session)

        for level_id in LEVELS:
            path = SYLLABUS_DIR / syllabus_filename(level_id)
            data = load_json(path, {})
            if not data:
                continue
            print(f"Importing {level_id}...")
            for subject_name, subject in data.get("subjects", {}).items():
                if not isinstance(subject, dict):
                    continue
                course = session.scalar(
                    select(Course).where(Course.level_id == level_id, Course.subject == subject_name)
                )
                if not course:
                    course = Course(
                        level_id=level_id,
                        subject=subject_name,
                        title=f"{subject_name} — {level_id}",
                        description=subject.get("description", ""),
                        published=True,
                        metadata_json={"legacy_source": str(path.relative_to(BASE_DIR))},
                    )
                    session.add(course)
                    session.flush()
                    module = Module(course_id=course.id, title="Imported curriculum", position=0)
                    session.add(module)
                    session.flush()
                    stats["courses"] += 1
                existing = existing_by_course.setdefault(course.id, set())
                for kind, title, url, body, raw in iter_resources(subject):
                    key = (title, kind, url)
                    if key in existing:
                        continue
                    existing.add(key)
                    session.add(
                        Resource(
                            kind=kind,
                            title=title[:500],
                            url=url,
                            extracted_text=str(body),
                            citation={"source": raw.get("source"), "author": raw.get("author")},
                            metadata_json={"course_id": course.id, "legacy": raw},
                        )
                    )
                    stats["resources"] += 1

        for path in DATA_DIR.glob("progress_*.json"):
            name = path.stem.removeprefix("progress_")
            user = imported_users.get(name) or upsert_user(session, name, "learner")
            content = load_json(path, {})
            existing = session.scalar(
                select(LearningItem).where(
                    LearningItem.user_id == user.id,
                    LearningItem.kind == "legacy_progress",
                    LearningItem.title == "Imported progress",
                )
            )
            if existing:
                existing.content = content
            else:
                session.add(
                    LearningItem(
                        user_id=user.id,
                        kind="legacy_progress",
                        title="Imported progress",
                        content=content,
                    )
                )
            stats["progress_records"] += 1

        session.add(
            AuditEvent(
                action="legacy_json_import",
                entity_type="system",
                after=stats,
                metadata_json={"dry_run": dry_run},
            )
        )
        if dry_run:
            session.rollback()
    return stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(json.dumps(migrate(dry_run=args.dry_run), indent=2))
