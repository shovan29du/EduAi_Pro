"""Persistent personalized-learning concept mastery.

Revision ID: 20260727_0003
Revises: 20260726_0002
"""

from alembic import op

from app.database import Base
from app import models  # noqa: F401

revision = "20260727_0003"
down_revision = "20260726_0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    Base.metadata.create_all(bind=op.get_bind())


def downgrade() -> None:
    op.drop_table("concept_mastery")
