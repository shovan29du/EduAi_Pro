"""Shared pytest fixtures.

The app ships with zero default child profiles (see app/storage.py --
Aliza and Saifan were removed as shipped defaults). Tests that exercise
child-scoped endpoints need *some* valid child profile to call, so this
fixture provisions two ephemeral test profiles once per test session,
the same way a parent would via POST /api/users.
"""
from app.storage import add_user

TEST_CHILD_1 = "TestChildOne"
TEST_CHILD_2 = "TestChildTwo"


def _ensure_test_children() -> None:
    for name in (TEST_CHILD_1, TEST_CHILD_2):
        try:
            add_user(name, "child")
        except ValueError:
            pass  # already exists from a previous test run


_ensure_test_children()
