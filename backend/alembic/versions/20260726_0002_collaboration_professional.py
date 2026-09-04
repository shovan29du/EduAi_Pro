"""Collaboration, attendance, portfolio and CPD records.

Revision ID: 20260726_0002
Revises: 20260726_0001
"""

from alembic import op

from app.database import Base
from app import models  # noqa: F401

revision = "20260726_0002"
down_revision = "20260726_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    Base.metadata.create_all(bind=op.get_bind())


def downgrade() -> None:
    for table_name in ("cpd_records", "portfolio_items", "discussion_posts", "attendance_records"):
        op.drop_table(table_name)
