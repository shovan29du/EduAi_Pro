"""Lesson pictures (Survival Skills, Practical Skills, subject lessons).

Revision ID: 20260822_0006
Revises: 20260821_0005
"""

import sqlalchemy as sa
from alembic import op

revision = "20260822_0006"
down_revision = "20260821_0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    if "lesson_pictures" in sa.inspect(op.get_bind()).get_table_names():  # the start-up bootstrap may have made it
        return
    op.create_table(
        "lesson_pictures",
        sa.Column("key", sa.String(400), primary_key=True),
        sa.Column("kind", sa.String(20), nullable=False),
        sa.Column("content_type", sa.String(50), nullable=False),
        sa.Column("data", sa.LargeBinary, nullable=False),
        sa.Column("size", sa.Integer, nullable=False, server_default="0"),
        sa.Column("sha1", sa.String(40), nullable=False, server_default=""),
        sa.Column("source", sa.String(20), nullable=False, server_default="download"),
        sa.Column("source_url", sa.Text),
        sa.Column("filename", sa.String(300)),
        sa.Column("credit", sa.JSON, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_lesson_pictures_kind", "lesson_pictures", ["kind"])


def downgrade() -> None:
    op.drop_index("ix_lesson_pictures_kind", table_name="lesson_pictures")
    op.drop_table("lesson_pictures")
