"""One-time/maintenance command for the single-owner EduAI_Pro installation."""

from datetime import datetime, timezone

from sqlalchemy import select

from app.database import session_scope
from app.models import User


def main() -> None:
    removed = []
    retained = False
    with session_scope() as session:
        users = list(session.scalars(select(User)))
        now = datetime.now(timezone.utc)
        for user in users:
            if user.display_name == "Shovan" and not retained:
                retained = True
                user.active = True
                user.deleted_at = None
                user.role = "admin"
                user.settings = {**(user.settings or {}), "profile_role": "parent"}
            else:
                removed.append(user.display_name)
                user.active = False
                user.deleted_at = now
    print(f"Retained Shovan; deactivated {len(removed)} other accounts.")


if __name__ == "__main__":
    main()
