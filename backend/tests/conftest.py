"""Shared pytest fixtures.

The app ships with zero default child profiles (see app/storage.py --
Aliza and Saifan were removed as shipped defaults). Tests that exercise
child-scoped endpoints need *some* valid child profile to call, so this
fixture provisions two ephemeral test profiles once per test session,
the same way a parent would via POST /api/users.
"""
from app.database import create_schema
from app.storage import add_user

TEST_CHILD_1 = "TestChildOne"
TEST_CHILD_2 = "TestChildTwo"


def _ensure_test_children() -> None:
    # A fresh checkout has no database file yet -- app/main.py normally
    # creates the schema via its FastAPI lifespan handler, but this module
    # seeds test users before any TestClient is ever instantiated, so it
    # needs to bootstrap the schema itself first.
    create_schema()
    for name in (TEST_CHILD_1, TEST_CHILD_2):
        try:
            add_user(name, "child")
        except ValueError:
            pass  # already exists from a previous test run


_ensure_test_children()


import pytest  # noqa: E402


@pytest.fixture
def museum_db(tmp_path, monkeypatch):
    """A throwaway database for the museum's stored pictures and deleted objects."""
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from app import database, museum_store
    from app import models  # noqa: F401  (registers the tables)

    engine = create_engine(f"sqlite:///{(tmp_path / 'museum.db').as_posix()}", connect_args={"check_same_thread": False})
    database.Base.metadata.create_all(bind=engine)
    monkeypatch.setattr(database, "SessionLocal", sessionmaker(bind=engine, autoflush=False, expire_on_commit=False))
    museum_store.invalidate()
    yield engine
    museum_store.invalidate()
    engine.dispose()
