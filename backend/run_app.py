#!/usr/bin/env python3
"""Start EduAi_Pro and open it in the browser once the server is ready.

The desktop shortcut runs this after building the frontend. The server is
started first and the browser is opened only when it answers, so the browser
never lands on "This site can't be reached" while Python is still starting.
On Windows it opens Microsoft Edge (falling back to the default browser).

    python backend/run_app.py            # port 8080
    EDUAI_PORT=9000 python backend/run_app.py
    EDUAI_NO_BROWSER=1 python backend/run_app.py
"""
from __future__ import annotations

import os
import sys
import threading
import time
import urllib.request
import webbrowser
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
PORT = int(os.environ.get("EDUAI_PORT", "8080"))
URL = f"http://localhost:{PORT}"
READY_TIMEOUT_SECONDS = 180


def is_up(port: int = PORT) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/levels", timeout=2) as response:
            return response.status == 200
    except Exception:
        return False


def open_browser(url: str = URL) -> None:
    if os.environ.get("EDUAI_NO_BROWSER"):
        return
    if sys.platform == "win32":
        try:
            # Edge's own URL scheme: opens Edge even when another browser is the default.
            os.startfile(f"microsoft-edge:{url}")  # noqa: S606
            return
        except OSError:
            pass
    webbrowser.open(url)


def open_when_ready(timeout: float = READY_TIMEOUT_SECONDS, interval: float = 0.5) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if is_up():
            open_browser()
            return True
        time.sleep(interval)
    return False


def main() -> int:
    if is_up():
        print(f"EduAi_Pro is already running at {URL} - opening it.")
        open_browser()
        return 0
    os.chdir(BACKEND_DIR)
    sys.path.insert(0, str(BACKEND_DIR))
    threading.Thread(target=open_when_ready, daemon=True).start()
    print(f"Starting EduAi_Pro at {URL} ... (the browser opens by itself when it is ready)")
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=PORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
