"""Tests for the Quine Museum: /api/quines plus round-trip verification that
each quine actually reproduces its own source through this app's real
execution paths (the /api/run-code sandbox for compiled/interpreted
languages, exec() for Python, and a Node harness mirroring the Code
Editor's browser JS sandbox for JavaScript/TypeScript).

Some toolchains (csharp, r, fortran) may not be installed in every
environment this suite runs in (see test_code_editor_languages.py for the
same caveat) -- production installs all of them, but a dev sandbox might
not. So those checks only assert an exact match when the toolchain
actually ran, mirroring the established pattern in that file.
"""
import contextlib
import io
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

QUINES_PATH = Path(__file__).resolve().parent.parent / "data" / "quines" / "quines.json"

EXPECTED_LANGUAGES = {
    "javascript", "typescript", "python", "java", "c", "cpp",
    "csharp", "go", "php", "ruby", "perl", "r", "fortran",
}

BACKEND_RUN_LANGUAGES = ["java", "c", "cpp", "go", "php", "ruby", "perl", "csharp", "r", "fortran"]


def _quines_by_language():
    with open(QUINES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {q["language"]: q for q in data["quines"]}


def test_list_quines():
    resp = client.get("/api/quines")
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Quine Museum"
    languages = {q["language"] for q in data["quines"]}
    assert languages == EXPECTED_LANGUAGES
    assert "sql" not in languages


def test_every_quine_has_required_fields():
    data = client.get("/api/quines").json()
    for q in data["quines"]:
        assert q["label"]
        assert q["source"].strip()
        assert isinstance(q["verified"], bool)


def test_get_single_quine():
    resp = client.get("/api/quines/python")
    assert resp.status_code == 200
    data = resp.json()
    assert data["language"] == "python"
    assert data["verified"] is True
    assert "print" in data["source"]


def test_get_unknown_language_404():
    resp = client.get("/api/quines/klingon")
    assert resp.status_code == 404


def test_python_quine_reproduces_itself_exactly():
    source = _quines_by_language()["python"]["source"]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(source, {})
    output = buf.getvalue()
    if output.endswith("\n"):
        output = output[:-1]
    assert output == source


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed in this environment")
@pytest.mark.parametrize("language", ["javascript", "typescript"])
def test_js_family_quine_reproduces_itself_through_app_sandbox_semantics(language):
    """Mirrors the Code Editor's browser sandbox exactly: it captures each
    console.log call's joined arguments into an array and joins that array
    with '\\n' -- for a quine that logs exactly once, this reproduces the
    logged string with no extra trailing newline (unlike raw Node stdout,
    which always appends one)."""
    source = _quines_by_language()[language]["source"]
    harness = (
        "const log = [];\n"
        "console.log = (...args) => { log.push(args.join(' ')); };\n"
        f"eval({json.dumps(source)});\n"
        "process.stdout.write(log.join('\\n'));\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(harness)
        harness_path = f.name
    result = subprocess.run(["node", harness_path], capture_output=True, text=True, timeout=10)
    assert result.stdout == source


@pytest.mark.parametrize("language", BACKEND_RUN_LANGUAGES)
def test_backend_quine_reproduces_itself_when_toolchain_present(language):
    q = _quines_by_language()[language]
    resp = client.post("/api/run-code", json={"language": language, "code": q["source"]})
    assert resp.status_code == 200
    output = resp.json()["output"]
    if output.startswith(("Error:", "Compile error:")):
        pytest.skip(f"{language} toolchain not available in this environment")
    # This sandbox's `java` prints a "Picked up JAVA_TOOL_OPTIONS" notice to
    # stderr (merged into output) only when a proxy-related env var is set on
    # the host -- strip it before comparing, since it isn't part of the quine.
    if language == "java":
        output = "\n".join(
            line for line in output.split("\n") if not line.startswith("Picked up JAVA_TOOL_OPTIONS")
        )
    assert output == q["source"]
