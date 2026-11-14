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
import shutil
import socket
import subprocess
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


def is_listening(port: int = PORT) -> bool:
    """True once something accepts connections on the port.

    uvicorn only opens its port after the app has finished starting, so this
    means "ready". It is a plain socket check on purpose: an HTTP check can be
    blocked or rerouted by a Windows proxy or security software.
    """
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            return True
    except OSError:
        return False


def is_ours(port: int = PORT) -> bool:
    """True if the thing on the port is EduAi_Pro (bypassing any system proxy)."""
    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f"http://127.0.0.1:{port}/api/levels", timeout=3) as response:
            return response.status == 200
    except Exception:
        return False


def find_edge() -> str | None:
    for variable in ("ProgramFiles(x86)", "ProgramFiles", "LocalAppData"):
        base = os.environ.get(variable)
        if base:
            candidate = Path(base) / "Microsoft" / "Edge" / "Application" / "msedge.exe"
            if candidate.is_file():
                return str(candidate)
    return shutil.which("msedge")


def open_browser(url: str = URL) -> str | None:
    """Open the app. Returns the name of what was used, or None if nothing worked."""
    if os.environ.get("EDUAI_NO_BROWSER"):
        return "disabled"
    if sys.platform == "win32":
        edge = find_edge()
        if edge:
            try:
                subprocess.Popen([edge, url])
                return "Microsoft Edge"
            except OSError:
                pass
        try:
            os.startfile(url)  # noqa: S606 - default browser, like `start <url>`
            return "your default browser"
        except OSError:
            pass
    return "your default browser" if webbrowser.open(url) else None


def _announce_open(url: str = URL) -> None:
    used = open_browser(url)
    if used is None:
        print(f"Could not open a browser automatically. Open {url} yourself.", flush=True)
    elif used != "disabled":
        print(f"Opened {url} in {used}. If you do not see it, open {url} yourself.", flush=True)


def open_when_ready(timeout: float = READY_TIMEOUT_SECONDS, interval: float = 0.5) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if is_listening():
            print("Server is ready.", flush=True)
            _announce_open()
            return True
        time.sleep(interval)
    print(f"The server did not become ready in {int(timeout)} seconds. Check the messages above.", flush=True)
    return False


def main() -> int:
    if is_listening():
        if is_ours():
            print(f"EduAi_Pro is already running at {URL} - opening it.")
            _announce_open()
            return 0
        print(f"Port {PORT} is being used by another program, so EduAi_Pro cannot start.")
        print("Close that program (or restart the PC) and try again.")
        return 1
    os.chdir(BACKEND_DIR)
    sys.path.insert(0, str(BACKEND_DIR))
    threading.Thread(target=open_when_ready, daemon=True).start()
    print(f"Starting EduAi_Pro at {URL} ... (the browser opens by itself when it is ready)", flush=True)
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=PORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
