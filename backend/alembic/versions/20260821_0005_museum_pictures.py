"""Virtual Museum pictures and deleted objects.

Revision ID: 20260821_0005
Revises: 20260803_0004
"""

import sqlalchemy as sa
from alembic import op

revision = "20260821_0005"
down_revision = "20260803_0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    existing = set(sa.inspect(bind).get_table_names())
    if "museum_pictures" not in existing:  # the app's start-up bootstrap may have made it already
        op.create_table(
            "museum_pictures",
            sa.Column("object_id", sa.String(200), primary_key=True),
            sa.Column("gallery", sa.String(100), nullable=False, server_default=""),
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
    if "museum_deleted_objects" not in existing:
        op.create_table(
            "museum_deleted_objects",
            sa.Column("gallery", sa.String(100), primary_key=True),
            sa.Column("object_id", sa.String(200), primary_key=True),
            sa.Column("name", sa.String(300), nullable=False, server_default=""),
            sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=False),
        )


def downgrade() -> None:
    op.drop_table("museum_deleted_objects")
    op.drop_table("museum_pictures")
