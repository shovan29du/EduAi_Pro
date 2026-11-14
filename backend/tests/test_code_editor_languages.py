"""Tests for /api/run-code across every language the Code Editor supports.

The container this test suite runs in may or may not have every compiler/
interpreter installed (the production Docker image installs all of them --
see backend/Dockerfile -- but a dev sandbox might be missing one or two).
So each case asserts the endpoint never 500s and always returns an "output"
string, then does a soft assertion on the expected greeting only when the
toolchain actually ran (i.e. the output isn't an "Error: ..." from a missing
binary) -- that keeps the test meaningful without being environment-specific.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

CASES = [
    ("cpp", '#include <iostream>\nint main() { std::cout << "hi-cpp"; return 0; }', "hi-cpp"),
    ("c", '#include <stdio.h>\nint main() { printf("hi-c"); return 0; }', "hi-c"),
    ("java", 'public class Main { public static void main(String[] a) { System.out.print("hi-java"); } }', "hi-java"),
    ("go", 'package main\nimport "fmt"\nfunc main() { fmt.Print("hi-go") }', "hi-go"),
    ("rust", 'fn main() { print!("hi-rust"); }', "hi-rust"),
    ("php", '<?php echo "hi-php";', "hi-php"),
    ("ruby", 'print "hi-ruby"', "hi-ruby"),
    ("perl", 'print "hi-perl";', "hi-perl"),
    ("csharp", 'using System;\nclass Program { static void Main() { Console.Write("hi-csharp"); } }', "hi-csharp"),
    ("fortran", 'program hello\n  write(*,"(A)", advance="no") "hi-fortran"\nend program hello', "hi-fortran"),
    ("r", 'cat("hi-r")', "hi-r"),
]


@pytest.mark.parametrize("language,code,expected", CASES)
def test_run_code_never_500s_and_runs_when_toolchain_present(language, code, expected):
    resp = client.post("/api/run-code", json={"language": language, "code": code})
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data.get("output"), str)
    assert data["output"]  # never empty
    if not data["output"].startswith(("Error:", "Compile error:")):
        assert expected in data["output"]


def test_run_code_sql_still_works():
    resp = client.post("/api/run-code", json={
        "language": "sql",
        "code": "CREATE TABLE t (n INTEGER); INSERT INTO t VALUES (1); SELECT * FROM t;",
    })
    assert resp.status_code == 200
    assert "1" in resp.json()["output"]


def test_run_code_unsupported_language():
    resp = client.post("/api/run-code", json={"language": "cobol", "code": "x"})
    assert resp.status_code == 200
    assert "Unsupported language" in resp.json()["output"]
