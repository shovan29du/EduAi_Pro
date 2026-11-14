import sys
from pathlib import Path

import pytest

import run_app

ROOT = Path(__file__).resolve().parents[2]


def test_is_up_reflects_whether_the_server_answers(monkeypatch):
    class Ok:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *a): return False

    monkeypatch.setattr(run_app.urllib.request, "urlopen", lambda *a, **k: Ok())
    assert run_app.is_up(8080) is True

    def refused(*a, **k):
        raise ConnectionRefusedError()

    monkeypatch.setattr(run_app.urllib.request, "urlopen", refused)
    assert run_app.is_up(8080) is False


def test_windows_opens_edge_first_and_falls_back_to_the_default_browser(monkeypatch):
    monkeypatch.delenv("EDUAI_NO_BROWSER", raising=False)
    monkeypatch.setattr(run_app.sys, "platform", "win32")
    opened, fallback = [], []
    monkeypatch.setattr(run_app.os, "startfile", lambda target: opened.append(target), raising=False)
    monkeypatch.setattr(run_app.webbrowser, "open", lambda url: fallback.append(url))
    run_app.open_browser("http://localhost:8080")
    assert opened == ["microsoft-edge:http://localhost:8080"] and fallback == []

    def no_edge(target):
        raise OSError("no handler")

    monkeypatch.setattr(run_app.os, "startfile", no_edge, raising=False)
    run_app.open_browser("http://localhost:8080")
    assert fallback == ["http://localhost:8080"]


def test_other_platforms_use_the_default_browser_and_the_opt_out_works(monkeypatch):
    monkeypatch.delenv("EDUAI_NO_BROWSER", raising=False)
    monkeypatch.setattr(run_app.sys, "platform", "linux")
    seen = []
    monkeypatch.setattr(run_app.webbrowser, "open", lambda url: seen.append(url))
    run_app.open_browser("http://localhost:8080")
    monkeypatch.setenv("EDUAI_NO_BROWSER", "1")
    run_app.open_browser("http://localhost:8080")
    assert seen == ["http://localhost:8080"]


def test_browser_opens_only_after_the_server_answers(monkeypatch):
    answers = iter([False, False, True])
    opened = []
    monkeypatch.setattr(run_app, "is_up", lambda *a: next(answers))
    monkeypatch.setattr(run_app, "open_browser", lambda *a: opened.append(1))
    assert run_app.open_when_ready(timeout=5, interval=0) is True
    assert opened == [1]


def test_gives_up_quietly_if_the_server_never_starts(monkeypatch):
    monkeypatch.setattr(run_app, "is_up", lambda *a: False)
    monkeypatch.setattr(run_app, "open_browser", lambda *a: pytest.fail("must not open a dead server"))
    assert run_app.open_when_ready(timeout=0.05, interval=0.01) is False


def test_an_already_running_app_is_opened_not_started_twice(monkeypatch):
    opened = []
    monkeypatch.setattr(run_app, "is_up", lambda *a: True)
    monkeypatch.setattr(run_app, "open_browser", lambda *a: opened.append(1))
    monkeypatch.setitem(sys.modules, "uvicorn", None)  # importing it would raise
    assert run_app.main() == 0 and opened == [1]


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
