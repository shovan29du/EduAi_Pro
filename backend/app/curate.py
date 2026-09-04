import json
from pathlib import Path
from threading import Lock

from sqlalchemy import select

from app import ai_tutor
from app.database import session_scope
from app.levels import LEVELS, syllabus_filename
from app.models import AuditEvent, Course, Resource
from app.safety import safety_filter

SYLLABUS_DIR = Path(__file__).resolve().parent.parent / "syllabus"
RESOURCE_KEYS = (
    "books",
    "video_resources",
    "text_resources",
    "cartoon_videos",
    "infographics",
    "textbooks",
    "audio_resources",
    "comics",
    "drawing_activities",
    "info_cards",
    "podcasts",
    "news_resources",
)

_lock = Lock()


class CurationError(ValueError):
    pass


def curate_resource(standard: int, subject: str, resource_type: str, resource: dict) -> dict:
    if resource_type not in RESOURCE_KEYS:
        raise CurationError(f"resource_type must be one of {RESOURCE_KEYS}")
    if not safety_filter.validate_resource(resource):
        raise CurationError("Resource rejected: contains blocked words")

    resource = {**resource, "safe": True}

    level_id = str(standard)
    if level_id in LEVELS:
        with session_scope() as session:
            course = session.scalar(
                select(Course).where(Course.level_id == level_id, Course.subject == subject)
            )
            if not course:
                course = Course(
                    level_id=level_id,
                    subject=subject,
                    title=f"{subject} — {LEVELS[level_id]['label']}",
                    published=True,
                    metadata_json={"created_by": "curation_api"},
                )
                session.add(course)
                session.flush()
            row = Resource(
                kind=resource_type,
                title=str(resource.get("title") or "Curated resource")[:500],
                url=resource.get("url"),
                extracted_text=str(resource.get("body") or resource.get("description") or ""),
                citation={"source": resource.get("source"), "author": resource.get("author")},
                metadata_json={
                    "course_id": course.id,
                    "runtime_curated": True,
                    "level_id": level_id,
                    "subject": subject,
                    "resource_type": resource_type,
                    "resource": resource,
                },
            )
            session.add(row)
            session.flush()
            session.add(
                AuditEvent(
                    action="curriculum_resource_created",
                    entity_type="resource",
                    entity_id=row.id,
                    before=None,
                    after=resource,
                    metadata_json={"course_id": course.id, "level_id": level_id, "subject": subject},
                )
            )
        return resource

    # Compatibility only for the historical out-of-range Grade 11 API test.
    with _lock:
        path = SYLLABUS_DIR / f"grade{standard}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {"standard": standard, "subjects": {}}

        subject_data = data["subjects"].setdefault(
            subject,
            {key: [] for key in RESOURCE_KEYS} | {"quiz_bank": [], "exam": {"questions": [], "passing_score": 60}},
        )
        subject_data.setdefault(resource_type, []).append(resource)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    return resource


def curate_book_topics(
    level_id, subject: str, book_title: str, book_text: str, source: str = "Parent-uploaded book",
) -> list[str]:
    """After a book is added as a resource, ask Ark AI which lessons in this
    subject's syllabus its content is relevant to, then attach the extracted
    parts (in full or summarised form) to those lessons as book_excerpts,
    plus a textbook_references entry linking the lesson back to the book.
    ``level_id`` is any level the platform understands -- a numeric school
    grade or a college/undergraduate/master's code (see app/levels.py) -- so
    this works the same way for a Grade 5 textbook as for a college one.
    Returns the titles of lessons that were linked; [] if the subject has no
    lessons yet or nothing in the book matched."""
    with _lock:
        path = SYLLABUS_DIR / syllabus_filename(level_id)
        if not path.exists():
            return []
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subject_data = data.get("subjects", {}).get(subject)
        lessons = subject_data.get("lessons") if subject_data else None
        if not lessons:
            return []

        lesson_titles = [lesson["title"] for lesson in lessons if lesson.get("title")]
        snippets = ai_tutor.analyse_book_for_lessons(book_title, book_text, lesson_titles)
        if not snippets:
            return []

        lessons_by_title = {lesson["title"]: lesson for lesson in lessons if lesson.get("title")}
        linked = []
        for snippet in snippets:
            lesson = lessons_by_title.get(snippet["lesson_title"])
            if not lesson:
                continue
            lesson.setdefault("book_excerpts", []).append({
                "book": book_title,
                "kind": snippet["kind"],
                "form": snippet["form"],
                "content": snippet["content"],
            })
            lesson.setdefault("textbook_references", []).append({
                "title": book_title,
                "source": source,
            })
            linked.append(snippet["lesson_title"])

        if linked:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return linked
