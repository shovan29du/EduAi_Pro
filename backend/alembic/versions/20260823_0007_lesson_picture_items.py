"""Several pictures per lesson.

Revision ID: 20260823_0007
Revises: 20260822_0006
"""

import sqlalchemy as sa
from alembic import op

revision = "20260823_0007"
down_revision = "20260822_0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    if "lesson_picture_items" in sa.inspect(op.get_bind()).get_table_names():  # the start-up bootstrap may have made it
        return
    op.create_table(
        "lesson_picture_items",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("key", sa.String(400), nullable=False),
        sa.Column("position", sa.Integer, nullable=False, server_default="0"),
        sa.Column("content_type", sa.String(50), nullable=False),
        sa.Column("data", sa.LargeBinary, nullable=False),
        sa.Column("size", sa.Integer, nullable=False, server_default="0"),
        sa.Column("sha1", sa.String(40), nullable=False, server_default=""),
        sa.Column("source", sa.String(20), nullable=False, server_default="download"),
        sa.Column("source_url", sa.Text),
        sa.Column("filename", sa.String(300)),
        sa.Column("title", sa.String(300), nullable=False, server_default=""),
        sa.Column("credit", sa.JSON, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_lesson_picture_items_key", "lesson_picture_items", ["key"])


def downgrade() -> None:
    op.drop_index("ix_lesson_picture_items_key", table_name="lesson_picture_items")
    op.drop_table("lesson_picture_items")
