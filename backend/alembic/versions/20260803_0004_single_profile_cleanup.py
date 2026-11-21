"""Data cleanup: keep only the Shovan profile.

EduAI_Pro is configured for the single administrator Shovan (see
app/storage.py PROTECTED_PARENT and the /api/users POST lockdown). This
soft-deletes any other profile (Parent, Bely, test/legacy profiles, etc.)
left over from before that lockdown, on any database that still has them.

Revision ID: 20260803_0004
Revises: 20260727_0003
"""

from datetime import datetime, timezone

import sqlalchemy as sa
from alembic import op

revision = "20260803_0004"
down_revision = "20260727_0003"
branch_labels = None
depends_on = None

users = sa.table(
    "users",
    sa.column("display_name", sa.String),
    sa.column("deleted_at", sa.DateTime(timezone=True)),
    sa.column("active", sa.Boolean),
)


def upgrade() -> None:
    op.execute(
        users.update()
        .where(users.c.display_name != "Shovan")
        .where(users.c.deleted_at.is_(None))
        .values(deleted_at=datetime.now(timezone.utc), active=False)
    )


def downgrade() -> None:
    # The specific set of profiles that existed before this cleanup isn't
    # recoverable from this migration alone.
    pass
