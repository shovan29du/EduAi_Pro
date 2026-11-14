import json
import re
from datetime import date, timedelta
from pathlib import Path
from threading import Lock

from sqlalchemy import select

from app.database import session_scope
from app.models import AuditEvent, LearningItem, User

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# EduAI_Pro is a single-owner adult-learning installation.
_DEFAULT_CHILDREN = []
_DEFAULT_PARENTS  = ["Shovan"]
PROTECTED_PARENT  = "Shovan"   # the installation owner cannot be deleted or renamed

# Legacy constants kept for import compatibility
ALLOWED_CHILDREN = set(_DEFAULT_CHILDREN)
PARENT_PROFILE   = "Parent"
PARENT_PROFILES  = set(_DEFAULT_PARENTS)
ALL_PROFILES     = (*sorted(ALLOWED_CHILDREN), *sorted(PARENT_PROFILES))

_lock = Lock()
_users_path = DATA_DIR / "users.json"


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "profile"


def _profile_email(name: str) -> str:
    return f"{_slug(name)}@legacy.local"


def _user_for_name(session, name: str, role: str = "learner") -> User:
    user = session.scalar(select(User).where(User.display_name == name))
    if not user:
        user = User(
            email=_profile_email(name),
            display_name=name,
            role=role,
            settings={"profile_role": "child" if role == "learner" else "parent"},
        )
        session.add(user)
        session.flush()
    elif user.deleted_at is not None or not user.active:
        user.deleted_at = None
        user.active = True
        user.role = role
    return user


def _audit(session, actor_id, action: str, entity_type: str, entity_id: str | None, before=None, after=None):
    session.add(
        AuditEvent(
            actor_id=actor_id,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            before=before,
            after=after,
            metadata_json={"source": "legacy_compatibility_api"},
        )
    )


def _legacy_override(path: Path) -> bool:
    """Tests and explicit callers may redirect a legacy path to a temp folder."""
    return path.parent.resolve() != DATA_DIR.resolve()


def _load_users() -> dict:
    with session_scope() as session:
        users = list(session.scalars(select(User).where(User.deleted_at.is_(None), User.active.is_(True))))
        if not users:
            _user_for_name(session, "Shovan", "admin")
            session.flush()
            users = list(session.scalars(select(User).where(User.deleted_at.is_(None), User.active.is_(True))))
        children = sorted(
            user.display_name
            for user in users
            if user.settings.get("profile_role") == "child"
            or (user.settings.get("legacy_import") and user.role == "learner")
        )
        parents = sorted(
            user.display_name
            for user in users
            if user.settings.get("profile_role") == "parent"
            or (user.settings.get("legacy_import") and user.role != "learner")
        )
        return {"children": children, "parents": parents}


def _save_users(data: dict) -> None:
    # Kept as a compatibility hook; all profile mutations now use transactions.
    return None


def get_children() -> list[str]:
    return _load_users()["children"]


def get_all_parent_profiles() -> list[str]:
    return _load_users()["parents"]


def get_all_profiles() -> list[str]:
    u = _load_users()
    return sorted(u["children"]) + sorted(u["parents"])


def add_user(name: str, role: str) -> dict:
    """role: 'child' or 'parent'. Returns updated users dict."""
    with _lock:
        with session_scope() as session:
            existing = session.scalar(select(User).where(User.display_name == name, User.deleted_at.is_(None)))
            if existing:
                raise ValueError(f"User '{name}' already exists")
            user = _user_for_name(session, name, "learner" if role == "child" else "admin")
            user.settings = {**(user.settings or {}), "profile_role": role}
            _audit(session, user.id, "profile_created", "user", user.id, after={"name": name, "role": role})
        return _load_users()


def rename_user(old_name: str, new_name: str) -> dict:
    with _lock:
        if old_name == PROTECTED_PARENT:
            raise ValueError("Cannot rename the Parent account")
        with session_scope() as session:
            user = session.scalar(select(User).where(User.display_name == old_name, User.deleted_at.is_(None)))
            if not user:
                raise ValueError(f"User '{old_name}' not found")
            duplicate = session.scalar(select(User).where(User.display_name == new_name, User.deleted_at.is_(None)))
            if duplicate:
                raise ValueError(f"Name '{new_name}' already taken")
            before = {"display_name": user.display_name}
            user.display_name = new_name
            _audit(session, user.id, "profile_renamed", "user", user.id, before=before, after={"display_name": new_name})
        return _load_users()


def delete_user(name: str) -> dict:
    with _lock:
        if name == PROTECTED_PARENT:
            raise ValueError("Cannot delete the Parent account")
        with session_scope() as session:
            user = session.scalar(select(User).where(User.display_name == name, User.deleted_at.is_(None)))
            if not user:
                raise ValueError(f"User '{name}' not found")
            from datetime import datetime, timezone
            user.deleted_at = datetime.now(timezone.utc)
            user.active = False
            _audit(session, user.id, "profile_soft_deleted", "user", user.id, before={"name": name})
        return _load_users()

STREAK_BADGE_MILESTONES = (3, 7, 14, 30)


def _today() -> date:
    return date.today()


def _current_streak(lesson_dates: list) -> int:
    days = sorted({date.fromisoformat(d) for d in lesson_dates}, reverse=True)
    if not days:
        return 0
    today = _today()
    if days[0] not in (today, today - timedelta(days=1)):
        return 0
    streak = 1
    for i in range(1, len(days)):
        if days[i - 1] - days[i] == timedelta(days=1):
            streak += 1
        else:
            break
    return streak


def _progress_path(child: str) -> Path:
    return DATA_DIR / f"progress_{child}.json"


def _activity_path(child: str) -> Path:
    return DATA_DIR / f"activity_{child}.json"


def _get_learning_content(child: str, kind: str, default):
    with session_scope() as session:
        user = _user_for_name(session, child)
        item = session.scalar(
            select(LearningItem).where(
                LearningItem.user_id == user.id,
                LearningItem.kind == kind,
                LearningItem.title == kind,
                LearningItem.deleted_at.is_(None),
            )
        )
        return item.content if item else default


def _save_learning_content(child: str, kind: str, content):
    with session_scope() as session:
        user = _user_for_name(session, child)
        item = session.scalar(
            select(LearningItem).where(
                LearningItem.user_id == user.id,
                LearningItem.kind == kind,
                LearningItem.title == kind,
                LearningItem.deleted_at.is_(None),
            )
        )
        before = item.content if item else None
        if item:
            item.content = content
        else:
            item = LearningItem(user_id=user.id, kind=kind, title=kind, content=content)
            session.add(item)
            session.flush()
        _audit(session, user.id, f"{kind}_updated", "learning_item", item.id, before=before, after=content)
    return content


def get_progress(child: str) -> dict:
    path = _progress_path(child)
    default = {
        "scores": {},
        "badges": [],
        "mastery": {},
        "snippets": {},
        "completed_lessons": {},
        "lesson_streak_dates": [],
        "lesson_streak": 0,
    }
    if _legacy_override(path):
        if not path.exists():
            return default
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = _get_learning_content(child, "progress", None)
        if data is None:
            # One-time compatibility read; all subsequent writes go to SQL.
            if path.exists():
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                _save_learning_content(child, "progress", data)
            else:
                data = default
    data.setdefault("completed_lessons", {})
    data.setdefault("lesson_streak_dates", [])
    data["lesson_streak"] = _current_streak(data["lesson_streak_dates"])
    return data


def save_progress(child: str, update: dict) -> dict:
    with _lock:
        current = get_progress(child)
        for key in ("scores", "mastery", "snippets"):
            if key in update:
                current.setdefault(key, {}).update(update[key])
        if "badges" in update:
            current.setdefault("badges", [])
            for badge in update["badges"]:
                if badge not in current["badges"]:
                    current["badges"].append(badge)
        if "completed_lessons" in update:
            current.setdefault("completed_lessons", {})
            gained_lesson = False
            for subject, lesson_ids in update["completed_lessons"].items():
                existing = current["completed_lessons"].setdefault(subject, [])
                for lesson_id in lesson_ids:
                    if lesson_id not in existing:
                        existing.append(lesson_id)
                        gained_lesson = True
            if gained_lesson:
                dates = current.setdefault("lesson_streak_dates", [])
                today_str = _today().isoformat()
                if today_str not in dates:
                    dates.append(today_str)
                streak = _current_streak(dates)
                current["lesson_streak"] = streak
                badges = current.setdefault("badges", [])
                for milestone in STREAK_BADGE_MILESTONES:
                    if streak >= milestone:
                        badge = f"lesson-streak-{milestone}"
                        if badge not in badges:
                            badges.append(badge)
        path = _progress_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(current, f, indent=2)
        else:
            _save_learning_content(child, "progress", current)
        return current


def delete_snippet(child: str, snippet_id: str) -> dict:
    """Remove one saved Code Editor snippet by id. save_progress() only ever
    adds/updates snippets (a shallow dict.update merge), so a real delete
    needs its own path that rewrites the progress file directly."""
    with _lock:
        current = get_progress(child)
        current.setdefault("snippets", {}).pop(snippet_id, None)
        path = _progress_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(current, f, indent=2)
        else:
            _save_learning_content(child, "progress", current)
        return current


def get_activity_log(child: str) -> list:
    path = _activity_path(child)
    if _legacy_override(path):
        if not path.exists():
            return []
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _get_learning_content(child, "activity_log", [])


def append_activity(child: str, entry: dict) -> list:
    with _lock:
        log = get_activity_log(child)
        log.append(entry)
        log = log[-50:]
        path = _activity_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(log, f, indent=2)
        else:
            _save_learning_content(child, "activity_log", log)
        return log


# ── Homework ──────────────────────────────────────────────────────────────────

def _homework_path(child: str) -> Path:
    return DATA_DIR / f"homework_{child}.json"


def get_homework(child: str) -> list:
    path = _homework_path(child)
    if _legacy_override(path):
        if not path.exists():
            return []
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _get_learning_content(child, "homework", [])


def save_homework(child: str, items: list) -> list:
    with _lock:
        path = _homework_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(items, f, indent=2)
        else:
            _save_learning_content(child, "homework", items)
        return items


# ── Reading Log ───────────────────────────────────────────────────────────────

def _reading_log_path(child: str) -> Path:
    return DATA_DIR / f"reading_log_{child}.json"


def get_reading_log(child: str) -> list:
    path = _reading_log_path(child)
    if _legacy_override(path):
        if not path.exists():
            return []
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _get_learning_content(child, "reading_log", [])


def append_reading_entry(child: str, entry: dict) -> list:
    with _lock:
        log = get_reading_log(child)
        log.append(entry)
        path = _reading_log_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(log, f, indent=2)
        else:
            _save_learning_content(child, "reading_log", log)
        return log


# ── Screen Time ───────────────────────────────────────────────────────────────

def _screen_time_path(child: str) -> Path:
    return DATA_DIR / f"screen_time_{child}.json"


def get_screen_time(child: str) -> dict:
    path = _screen_time_path(child)
    if _legacy_override(path):
        if not path.exists():
            return {}
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _get_learning_content(child, "screen_time", {})


def add_screen_time(child: str, minutes: int, date_str: str | None = None) -> dict:
    with _lock:
        data = get_screen_time(child)
        key = date_str or _today().isoformat()
        data[key] = data.get(key, 0) + minutes
        path = _screen_time_path(child)
        if _legacy_override(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        else:
            _save_learning_content(child, "screen_time", data)
        return data


def get_attendance(child: str) -> list:
    return _get_learning_content(child, "attendance", [])


def save_attendance(child: str, records: list) -> list:
    with _lock:
        return _save_learning_content(child, "attendance", records)
