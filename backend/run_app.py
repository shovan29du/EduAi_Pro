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

import json
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
sys.path.insert(0, str(BACKEND_DIR))
from app.version import code_stamp  # noqa: E402
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


def running_stamp(port: int = PORT):
    """The code fingerprint the running server reports, or None (an older server has no /api/health)."""
    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f"http://127.0.0.1:{port}/api/health", timeout=3) as response:
            return json.loads(response.read().decode("utf-8")).get("code_stamp")
    except Exception:
        return None


def find_listening_pid(port: int = PORT):
    """The process id of whatever is listening on the port (None if it cannot be found)."""
    try:
        if sys.platform == "win32":
            out = subprocess.run(["netstat", "-ano", "-p", "tcp"], capture_output=True, text=True, timeout=15).stdout
            for line in out.splitlines():
                parts = line.split()
                if len(parts) >= 5 and parts[3].upper() == "LISTENING" and parts[1].rsplit(":", 1)[-1] == str(port):
                    return int(parts[4])
        else:
            out = subprocess.run(["lsof", "-ti", f"tcp:{port}", "-sTCP:LISTEN"], capture_output=True, text=True, timeout=15).stdout
            return int(out.split()[0]) if out.split() else None
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return None


def stop_process(pid: int) -> None:
    if sys.platform == "win32":
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True, timeout=30)
    else:
        os.kill(pid, 15)


def replace_stale_server(port: int = PORT, wait: float = 15.0) -> bool:
    """Stop an out-of-date copy of EduAi_Pro that is still running. True once the port is free."""
    pid = find_listening_pid(port)
    if pid is None or pid == os.getpid():
        return False
    try:
        stop_process(pid)
    except (OSError, subprocess.SubprocessError):
        return False
    deadline = time.time() + wait
    while time.time() < deadline:
        if not is_listening(port):
            return True
        time.sleep(0.3)
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


FRONTEND_DIR = BACKEND_DIR.parent / "frontend"
_SOURCE_NAMES = ("src", "public", "index.html", "package.json", "vite.config.js", "vite.config.mjs", "vite.config.ts")


def _newest_mtime(path: Path) -> float:
    if path.is_file():
        return path.stat().st_mtime
    newest = 0.0
    for folder, _dirs, files in os.walk(path):
        for name in files:
            try:
                newest = max(newest, (Path(folder) / name).stat().st_mtime)
            except OSError:
                pass
    return newest


def frontend_needs_build(frontend: Path = FRONTEND_DIR) -> bool:
    """True when there is no build yet, or a source file is newer than it."""
    built = frontend / "dist" / "index.html"
    if not built.is_file():
        return True
    built_at = built.stat().st_mtime
    return any(
        _newest_mtime(frontend / name) > built_at
        for name in _SOURCE_NAMES
        if (frontend / name).exists()
    )


def build_frontend(frontend: Path = FRONTEND_DIR) -> bool:
    """Build the web pages when they are missing or out of date.

    This used to be a line in the .bat launcher: `npm run build`. npm is a .cmd
    file, and a batch file that runs another .cmd without `call` never comes
    back -- so the launcher stopped after the build and the server never
    started, which looked like "the shortcut does not work". Doing it here has
    no such trap, and it skips the (slow) build when nothing changed.

    Returns True when a usable build exists afterwards.
    """
    if not frontend_needs_build(frontend):
        return True
    have_old_build = (frontend / "dist" / "index.html").is_file()
    npm = shutil.which("npm.cmd") or shutil.which("npm")
    if not npm:
        print("Node.js (npm) was not found, so the pages cannot be rebuilt.", flush=True)
        if not have_old_build:
            print("Install Node.js from https://nodejs.org and run: python full_install.py", flush=True)
        return have_old_build
    try:
        if not (frontend / "node_modules").is_dir():
            print("Installing the frontend packages (first run only) ...", flush=True)
            subprocess.run([npm, "install"], cwd=frontend, check=True)
        print("Building the pages (about a minute) ...", flush=True)
        subprocess.run([npm, "run", "build"], cwd=frontend, check=True)
        return True
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"The page build failed ({exc}).", flush=True)
        if have_old_build:
            print("Starting with the previous build instead.", flush=True)
        return have_old_build


def main() -> int:
    if is_listening():
        if not is_ours():
            print(f"Port {PORT} is being used by another program, so EduAi_Pro cannot start.")
            print("Close that program (or restart the PC) and try again.")
            return 1
        if running_stamp() == code_stamp():
            print(f"EduAi_Pro is already running at {URL} - opening it.")
            _announce_open()
            return 0
        # It was started before the last update, so it still has the old code in memory
        # (new buttons then fail with "Method Not Allowed"). Close it and start fresh.
        print("An older copy of EduAi_Pro is still running. Closing it so the updated version starts ...", flush=True)
        if not replace_stale_server():
            print("Could not close the older copy. Close its black window (or restart the PC) and try again.")
            return 1
    if not build_frontend():
        print("There is no built copy of the pages, so the app cannot open. See the messages above.")
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
