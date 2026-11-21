"""A fingerprint of the backend code, so the launcher can tell a running server is out of date.

After an update the app's files change, but a copy of the server that was already
running keeps the *old* code in memory: new buttons then fail with errors such as
"Method Not Allowed". The server reports this fingerprint at /api/health and the
launcher compares it with the files on disk.
"""
from __future__ import annotations

from pathlib import Path

APP_DIR = Path(__file__).resolve().parent


def code_stamp(app_dir: Path = APP_DIR) -> int:
    """The newest modification time (whole seconds) of any Python file in the app."""
    newest = 0
    for path in app_dir.rglob("*.py"):
        try:
            newest = max(newest, int(path.stat().st_mtime))
        except OSError:
            pass
    return newest
