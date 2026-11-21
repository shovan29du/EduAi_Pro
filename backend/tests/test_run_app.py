import os
import sys
from pathlib import Path

import pytest

import run_app

ROOT = Path(__file__).resolve().parents[2]


import socket
import types


def test_is_listening_is_a_plain_socket_check():
    server = socket.socket()
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]
    try:
        assert run_app.is_listening(port) is True
    finally:
        server.close()
    assert run_app.is_listening(port) is False


class _Response:
    def __init__(self, status): self.status = status
    def __enter__(self): return self
    def __exit__(self, *a): return False


class _Opener:
    def __init__(self, status): self.status = status
    def open(self, url, timeout=0):
        assert url.endswith("/api/levels")
        return _Response(self.status)


def test_is_ours_ignores_system_proxies_and_checks_the_api(monkeypatch):
    handlers = []

    def build_opener(*h):
        handlers.extend(h)
        return _Opener(200)

    monkeypatch.setattr(run_app.urllib.request, "build_opener", build_opener)
    assert run_app.is_ours(8080) is True
    assert any(isinstance(h, run_app.urllib.request.ProxyHandler) and h.proxies == {} for h in handlers)

    monkeypatch.setattr(run_app.urllib.request, "build_opener", lambda *h: _Opener(404))
    assert run_app.is_ours(8080) is False

    def refused(*h):
        raise OSError("refused")

    monkeypatch.setattr(run_app.urllib.request, "build_opener", refused)
    assert run_app.is_ours(8080) is False


def test_windows_launches_edge_directly_when_it_is_installed(monkeypatch):
    monkeypatch.delenv("EDUAI_NO_BROWSER", raising=False)
    monkeypatch.setattr(run_app.sys, "platform", "win32")
    monkeypatch.setattr(run_app, "find_edge", lambda: r"C:\Edge\msedge.exe")
    launched = []
    monkeypatch.setattr(run_app.subprocess, "Popen", lambda cmd: launched.append(cmd))
    assert run_app.open_browser("http://localhost:8080") == "Microsoft Edge"
    assert launched == [[r"C:\Edge\msedge.exe", "http://localhost:8080"]]


def test_windows_falls_back_to_the_default_browser_then_to_webbrowser(monkeypatch):
    monkeypatch.delenv("EDUAI_NO_BROWSER", raising=False)
    monkeypatch.setattr(run_app.sys, "platform", "win32")
    monkeypatch.setattr(run_app, "find_edge", lambda: None)
    started, fallback = [], []
    monkeypatch.setattr(run_app.os, "startfile", lambda target: started.append(target), raising=False)
    monkeypatch.setattr(run_app.webbrowser, "open", lambda url: fallback.append(url) or True)
    assert run_app.open_browser("http://localhost:8080") == "your default browser"
    assert started == ["http://localhost:8080"] and fallback == []

    def broken(target):
        raise OSError("no handler")

    monkeypatch.setattr(run_app.os, "startfile", broken, raising=False)
    assert run_app.open_browser("http://localhost:8080") == "your default browser"
    assert fallback == ["http://localhost:8080"]

    def edge_fails(cmd):
        raise OSError("cannot start")

    monkeypatch.setattr(run_app, "find_edge", lambda: "msedge.exe")
    monkeypatch.setattr(run_app.subprocess, "Popen", edge_fails)
    started.clear()
    monkeypatch.setattr(run_app.os, "startfile", lambda target: started.append(target), raising=False)
    assert run_app.open_browser("http://localhost:8080") == "your default browser" and started


def test_other_platforms_use_webbrowser_and_the_opt_out_works(monkeypatch):
    monkeypatch.delenv("EDUAI_NO_BROWSER", raising=False)
    monkeypatch.setattr(run_app.sys, "platform", "linux")
    seen = []
    monkeypatch.setattr(run_app.webbrowser, "open", lambda url: seen.append(url) or True)
    assert run_app.open_browser("http://localhost:8080") == "your default browser"
    monkeypatch.setenv("EDUAI_NO_BROWSER", "1")
    assert run_app.open_browser("http://localhost:8080") == "disabled"
    assert seen == ["http://localhost:8080"]
    monkeypatch.delenv("EDUAI_NO_BROWSER")
    monkeypatch.setattr(run_app.webbrowser, "open", lambda url: False)
    assert run_app.open_browser("http://localhost:8080") is None


def test_find_edge_looks_in_the_standard_install_folders(monkeypatch, tmp_path):
    exe = tmp_path / "Microsoft" / "Edge" / "Application" / "msedge.exe"
    exe.parent.mkdir(parents=True)
    exe.write_text("x")
    for variable in ("ProgramFiles(x86)", "ProgramFiles", "LocalAppData"):
        monkeypatch.delenv(variable, raising=False)
    monkeypatch.setattr(run_app.shutil, "which", lambda name: None)
    assert run_app.find_edge() is None
    monkeypatch.setenv("ProgramFiles", str(tmp_path))
    assert run_app.find_edge() == str(exe)


def test_browser_opens_only_after_the_server_is_listening_and_says_so(monkeypatch, capsys):
    answers = iter([False, False, True])
    opened = []
    monkeypatch.setattr(run_app, "is_listening", lambda *a: next(answers))
    monkeypatch.setattr(run_app, "open_browser", lambda *a: opened.append(1) or "Microsoft Edge")
    assert run_app.open_when_ready(timeout=5, interval=0) is True
    out = capsys.readouterr().out
    assert opened == [1] and "Server is ready" in out and "Opened http://localhost:" in out and "Microsoft Edge" in out


def test_gives_up_with_a_message_if_the_server_never_starts(monkeypatch, capsys):
    monkeypatch.setattr(run_app, "is_listening", lambda *a: False)
    monkeypatch.setattr(run_app, "open_browser", lambda *a: pytest.fail("must not open a dead server"))
    assert run_app.open_when_ready(timeout=0.05, interval=0.01) is False
    assert "did not become ready" in capsys.readouterr().out


def test_tells_the_user_when_no_browser_could_be_opened(monkeypatch, capsys):
    monkeypatch.setattr(run_app, "open_browser", lambda *a: None)
    run_app._announce_open("http://localhost:8080")
    assert "Open http://localhost:8080 yourself" in capsys.readouterr().out


def test_main_opens_an_already_running_app_instead_of_starting_twice(monkeypatch):
    opened = []
    monkeypatch.setattr(run_app, "is_listening", lambda *a: True)
    monkeypatch.setattr(run_app, "is_ours", lambda *a: True)
    monkeypatch.setattr(run_app, "running_stamp", lambda *a: run_app.code_stamp())  # same code as on disk
    monkeypatch.setattr(run_app, "open_browser", lambda *a: opened.append(1) or "Microsoft Edge")
    monkeypatch.setitem(sys.modules, "uvicorn", None)  # importing it would raise
    assert run_app.main() == 0 and opened == [1]


@pytest.mark.parametrize("running", [None, 1])  # no /api/health at all (an old server), or older code
def test_main_replaces_a_server_that_still_runs_old_code(monkeypatch, tmp_path, capsys, running):
    state = {"up": True, "stopped": []}
    monkeypatch.setattr(run_app, "is_listening", lambda *a: state["up"])
    monkeypatch.setattr(run_app, "is_ours", lambda *a: True)
    monkeypatch.setattr(run_app, "running_stamp", lambda *a: running)
    monkeypatch.setattr(run_app, "find_listening_pid", lambda *a: 4242)
    monkeypatch.setattr(run_app, "stop_process", lambda pid: (state["stopped"].append(pid), state.update(up=False)))
    monkeypatch.setattr(run_app, "build_frontend", lambda *a: True)
    monkeypatch.setattr(run_app, "open_when_ready", lambda *a, **k: None)
    started = {}
    monkeypatch.setitem(sys.modules, "uvicorn", types.SimpleNamespace(run=lambda app, **kw: started.update(app=app)))
    cwd = Path.cwd()
    try:
        assert run_app.main() == 0
    finally:
        os.chdir(cwd)
    assert state["stopped"] == [4242] and started["app"] == "app.main:app"
    assert "older copy" in capsys.readouterr().out


def test_main_says_so_when_the_old_server_cannot_be_closed(monkeypatch, capsys):
    monkeypatch.setattr(run_app, "is_listening", lambda *a: True)
    monkeypatch.setattr(run_app, "is_ours", lambda *a: True)
    monkeypatch.setattr(run_app, "running_stamp", lambda *a: None)
    monkeypatch.setattr(run_app, "find_listening_pid", lambda *a: None)
    monkeypatch.setitem(sys.modules, "uvicorn", None)
    assert run_app.main() == 1
    assert "Could not close the older copy" in capsys.readouterr().out


def test_find_listening_pid_reads_windows_netstat(monkeypatch):
    out = ("  Proto  Local Address          Foreign Address        State           PID\n"
           "  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       10\n"
           "  TCP    127.0.0.1:8080         0.0.0.0:0              LISTENING       4242\n"
           "  TCP    127.0.0.1:50000        127.0.0.1:8080         ESTABLISHED     99\n")
    monkeypatch.setattr(run_app.sys, "platform", "win32")
    monkeypatch.setattr(run_app.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout=out))
    assert run_app.find_listening_pid(8080) == 4242
    assert run_app.find_listening_pid(9999) is None


def test_the_health_endpoint_reports_the_code_stamp():
    from fastapi.testclient import TestClient
    from app.main import app
    body = TestClient(app).get("/api/health").json()
    assert body["app"] == "EduAi_Pro" and isinstance(body["code_stamp"], int) and body["code_stamp"] > 0


def test_main_refuses_when_another_program_owns_the_port(monkeypatch, capsys):
    monkeypatch.setattr(run_app, "is_listening", lambda *a: True)
    monkeypatch.setattr(run_app, "is_ours", lambda *a: False)
    monkeypatch.setitem(sys.modules, "uvicorn", None)
    assert run_app.main() == 1
    assert "used by another program" in capsys.readouterr().out


def test_main_starts_the_server_and_the_ready_watcher(monkeypatch, tmp_path):
    monkeypatch.setattr(run_app, "is_listening", lambda *a: False)
    started = {}
    monkeypatch.setattr(run_app, "open_when_ready", lambda *a, **k: started.setdefault("watcher", True))
    monkeypatch.setitem(sys.modules, "uvicorn", types.SimpleNamespace(run=lambda app, **kw: started.update(app=app, **kw)))
    cwd = Path.cwd()
    try:
        assert run_app.main() == 0
    finally:
        import os
        os.chdir(cwd)
    assert started["app"] == "app.main:app" and started["port"] == run_app.PORT and started["host"] == "127.0.0.1"


def test_generated_windows_launchers_start_the_server_before_opening_the_browser(monkeypatch, tmp_path):
    sys.path.insert(0, str(ROOT))
    import full_install

    monkeypatch.setattr(full_install, "IS_WINDOWS", True)
    monkeypatch.setattr(full_install, "REPO_ROOT", tmp_path)
    backend = tmp_path / "backend"
    backend.mkdir()
    monkeypatch.setattr(full_install, "BACKEND_DIR", backend)
    monkeypatch.setattr(full_install, "FRONTEND_DIR", tmp_path / "frontend")
    monkeypatch.setattr(full_install, "venv_python", lambda: tmp_path / "py.exe")
    stale = backend / "run_backend.bat"
    stale.write_text("old")
    launcher = full_install.write_launcher()
    raw = launcher.read_bytes().decode()
    assert launcher.name == "start_EduAi_Pro.bat" and "\r\n" in raw
    assert "run_app.py" in raw and "start http" not in raw and "timeout /t" not in raw
    assert "EDUAI_PORT=8080" in raw
    # `npm run build` without `call` ends a batch file before the server line,
    # so the launcher must not run npm at all (run_app.py builds the pages).
    assert "npm" not in raw
    # relative to the .bat, so moving the folder keeps the shortcut working
    assert str(tmp_path) not in raw and "%~dp0" in raw
    assert not stale.exists()


# ---- building the pages -------------------------------------------------

def _frontend(tmp_path, built=True):
    front = tmp_path / "frontend"
    (front / "src").mkdir(parents=True)
    (front / "src" / "App.jsx").write_text("x")
    (front / "package.json").write_text("{}")
    if built:
        (front / "dist").mkdir()
        (front / "dist" / "index.html").write_text("<html>")
        # sources older than the build
        old = (front / "dist" / "index.html").stat().st_mtime - 100
        for name in ("src/App.jsx", "package.json"):
            os.utime(front / name, (old, old))
    return front


def test_build_needed_when_no_build_or_source_is_newer(tmp_path):
    assert run_app.frontend_needs_build(_frontend(tmp_path / "a", built=False)) is True
    fresh = _frontend(tmp_path / "b")
    assert run_app.frontend_needs_build(fresh) is False
    newer = (fresh / "dist" / "index.html").stat().st_mtime + 50
    os.utime(fresh / "src" / "App.jsx", (newer, newer))
    assert run_app.frontend_needs_build(fresh) is True


def test_build_skipped_when_up_to_date(tmp_path, monkeypatch):
    front = _frontend(tmp_path)
    calls = []
    monkeypatch.setattr(run_app.subprocess, "run", lambda *a, **k: calls.append(a))
    assert run_app.build_frontend(front) is True
    assert calls == []


def test_build_runs_npm_and_reports_success(tmp_path, monkeypatch):
    front = _frontend(tmp_path, built=False)
    (front / "node_modules").mkdir()
    calls = []
    monkeypatch.setattr(run_app.shutil, "which", lambda name: "C:/node/npm.cmd")
    monkeypatch.setattr(run_app.subprocess, "run", lambda cmd, **k: calls.append(cmd))
    assert run_app.build_frontend(front) is True
    assert calls == [["C:/node/npm.cmd", "run", "build"]]


def test_failed_build_falls_back_to_the_old_build(tmp_path, monkeypatch):
    front = _frontend(tmp_path)
    newer = (front / "dist" / "index.html").stat().st_mtime + 50
    os.utime(front / "src" / "App.jsx", (newer, newer))
    (front / "node_modules").mkdir()

    def boom(cmd, **k):
        raise run_app.subprocess.CalledProcessError(1, cmd)

    monkeypatch.setattr(run_app.shutil, "which", lambda name: "npm")
    monkeypatch.setattr(run_app.subprocess, "run", boom)
    assert run_app.build_frontend(front) is True  # old build still usable
    (front / "dist" / "index.html").unlink()
    assert run_app.build_frontend(front) is False  # nothing to serve


def test_no_npm_and_no_build_is_a_clear_failure(tmp_path, monkeypatch):
    front = _frontend(tmp_path, built=False)
    monkeypatch.setattr(run_app.shutil, "which", lambda name: None)
    assert run_app.build_frontend(front) is False
