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
    monkeypatch.setattr(run_app, "open_browser", lambda *a: opened.append(1) or "Microsoft Edge")
    monkeypatch.setitem(sys.modules, "uvicorn", None)  # importing it would raise
    assert run_app.main() == 0 and opened == [1]


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
    launcher = full_install.write_launcher()
    text = launcher.read_text()
    assert "run_app.py" in text and "start http" not in text and "timeout /t" not in text
    assert text.index("npm") < text.index("run_app.py")
    backend_only = (backend / "run_backend.bat").read_text()
    assert "set EDUAI_PORT=8080" in backend_only and "run_app.py" in backend_only and "-m uvicorn" not in backend_only
