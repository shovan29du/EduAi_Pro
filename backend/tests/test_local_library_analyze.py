import json
import shutil
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import ai_tutor, book_link_sync, local_library
from app.main import app

client = TestClient(app)


@pytest.fixture
def tmp_folder():
    tmp = Path(tempfile.mkdtemp())
    yield tmp
    shutil.rmtree(tmp, ignore_errors=True)


@pytest.fixture(autouse=True)
def isolated_state(monkeypatch, tmp_path):
    monkeypatch.setattr(local_library, "DB_PATH", tmp_path / "local_library_test.sqlite3")

    wlit_path = tmp_path / "library.json"
    wlit_path.write_text(json.dumps({
        "title": "World Literature Library", "description": "test",
        "sections": {
            "childrens_classics": {
                "label": "Children's Classics", "emoji": "📖", "age_range": "5-12",
                "books": [{
                    "id": "alice_wonderland", "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll",
                    "summary": "Old summary.",
                    "links": {"read_online": "https://www.gutenberg.org/ebooks/11"},
                }],
            },
        },
    }))
    monkeypatch.setattr(book_link_sync, "WLIT_PATH", wlit_path)

    syllabus_dir = tmp_path / "syllabus"
    syllabus_dir.mkdir()
    monkeypatch.setattr(book_link_sync, "SYLLABUS_DIR", syllabus_dir)
    yield


def index_one_book(tmp_folder, filename="alice.txt", content="Alice fell down a rabbit hole. " * 30):
    (tmp_folder / filename).write_text(content)
    result = local_library.scan_folder(str(tmp_folder), analyse_books=False)
    return result["files"][0]["id"]


def test_parse_book_library_analysis_literature():
    raw = (
        "CLASSIFICATION: literature\nTITLE: Alice's Adventures in Wonderland\nAUTHOR: Lewis Carroll\n"
        "SUBJECT: \nSYNOPSIS: A girl falls into a fantastical underground world."
    )
    result = ai_tutor._parse_book_library_analysis(raw)
    assert result == {
        "classification": "literature", "title": "Alice's Adventures in Wonderland",
        "author": "Lewis Carroll", "subject": "", "synopsis": "A girl falls into a fantastical underground world.",
    }


def test_parse_book_library_analysis_textbook_with_unknown_author():
    raw = "CLASSIFICATION: textbook\nTITLE: Intro to Algebra\nAUTHOR: Unknown\nSUBJECT: Mathematics\nSYNOPSIS: "
    result = ai_tutor._parse_book_library_analysis(raw)
    assert result["classification"] == "textbook"
    assert result["author"] == ""
    assert result["subject"] == "Mathematics"


def test_parse_book_library_analysis_rejects_unrecognized_classification():
    raw = "CLASSIFICATION: poetry collection\nTITLE: X\nAUTHOR: Y\nSUBJECT: \nSYNOPSIS: "
    result = ai_tutor._parse_book_library_analysis(raw)
    assert result["classification"] == ""


def test_analyze_endpoint_rejects_non_book_category(tmp_folder):
    (tmp_folder / "video.mp4").write_bytes(b"fake video")
    result = local_library.scan_folder(str(tmp_folder), analyse_books=False)
    file_id = result["files"][0]["id"]

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 400


def test_analyze_endpoint_404_for_unknown_file():
    resp = client.post("/api/local-library/files/doesnotexist/analyze")
    assert resp.status_code == 404


def test_analyze_endpoint_moves_literature_and_syncs_world_literature(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder)

    def fake_analyze(filename, text_excerpt):
        return {
            "classification": "literature", "title": "Alice's Adventures in Wonderland",
            "author": "Lewis Carroll", "subject": "", "synopsis": "A short new synopsis.",
        }
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    body = resp.json()

    assert body["analysis"]["classification"] == "literature"
    assert body["world_literature"]["created"] is False
    assert body["world_literature"]["book_id"] == "alice_wonderland"
    assert body["lesson_matches"] == []

    new_path = Path(body["file"]["path"])
    assert new_path.exists()
    assert new_path.parent.name == "Lewis Carroll"
    assert new_path.parent.parent.name == "L"
    assert body["file"]["author"] == "Lewis Carroll"
    assert body["file"]["classification"] == "literature"
    assert body["file"]["synopsis"] == "A short new synopsis."

    # get_file() must still resolve the moved file under the same root.
    get_resp = client.get(f"/api/local-library/files/{file_id}")
    assert get_resp.status_code == 200


def test_analyze_endpoint_moves_textbook_into_reference_subject_folder(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder, filename="algebra.txt", content="Chapters on equations. " * 30)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "textbook", "title": "Algebra Basics", "author": "", "subject": "Mathematics", "synopsis": ""}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    body = resp.json()
    assert body["world_literature"] is None
    assert body["lesson_matches"] == []

    new_path = Path(body["file"]["path"])
    assert new_path.exists()
    assert new_path.parent.name == "Mathematics"
    assert new_path.parent.parent.name == "Reference"


def test_analyze_endpoint_creates_new_world_lit_entry_when_no_match(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder, filename="mynovel.txt", content="Once upon a time. " * 30)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "literature", "title": "My Unpublished Novel", "author": "New Author", "subject": "", "synopsis": "A tale."}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    body = resp.json()
    assert body["world_literature"]["created"] is True
    assert body["world_literature"]["section"] == "local"


def test_analyze_endpoint_skips_world_lit_sync_when_author_unknown(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "literature", "title": "Something", "author": "", "subject": "", "synopsis": ""}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    body = resp.json()
    assert body["world_literature"] is None
    # Still filed under the catch-all "#" author-initial folder.
    new_path = Path(body["file"]["path"])
    assert new_path.parent.parent.name == "#"


def test_analyze_endpoint_422_when_ai_cannot_classify(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder)
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", lambda *a, **k: {
        "classification": "", "title": "", "author": "", "subject": "", "synopsis": "",
    })
    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 422
