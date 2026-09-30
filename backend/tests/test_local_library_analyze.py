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

    nonfiction_path = tmp_path / "nonfiction.json"
    nonfiction_path.write_text(json.dumps({
        "title": "Non-Fiction Library", "description": "test",
        "categories": {
            "science": {
                "label": "Science & Nature", "emoji": "🔬",
                "books": [{
                    "id": "sapiens", "title": "Sapiens", "author": "Yuval Noah Harari",
                    "summary": "Old summary.",
                    "links": {"read_online": "https://openlibrary.org/works/OL1234"},
                }],
            },
        },
    }))
    monkeypatch.setattr(book_link_sync, "NONFICTION_PATH", nonfiction_path)

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
    # No ANTHROPIC_API_KEY in this sandbox, so the real (unmocked) Ark AI
    # lesson-extraction call returns the offline fallback text, which can't
    # parse into any snippets -- confirms nothing gets written unexpectedly.
    assert body["topic_links"] == []

    new_path = Path(body["file"]["path"])
    assert new_path.exists()
    assert new_path.parent.name == "Mathematics"
    assert new_path.parent.parent.name == "Reference"


def test_analyze_endpoint_links_textbook_content_to_matching_lessons(tmp_folder, monkeypatch):
    import app.main as main_module

    file_id = index_one_book(tmp_folder, filename="algebra.txt", content="Equations and variables. " * 30)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "textbook", "title": "Algebra Basics", "author": "", "subject": "Mathematics", "synopsis": ""}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    def fake_analyse_text(text, limit=12):
        return {
            "summary": "", "extracted_chars": len(text),
            "matched_topics": [
                {"level": "5", "subject": "Math", "topic": "Equations", "score": 3.0},
                {"level": "5", "subject": "Math", "topic": "Variables", "score": 2.5},
                {"level": "C1", "subject": "Mathematics", "topic": "Linear Algebra", "score": 1.0},
                {"level": "UG1", "subject": "Mathematics", "topic": "Calculus", "score": 0.5},
            ],
        }
    monkeypatch.setattr(local_library, "analyse_text", fake_analyse_text)

    captured_calls = []

    def fake_curate_book_topics(level_id, subject, title, text, source="Parent-uploaded book"):
        captured_calls.append((level_id, subject, source))
        if (level_id, subject) == ("5", "Math"):
            return ["Solving Equations"]
        return []
    monkeypatch.setattr(main_module, "curate_book_topics", fake_curate_book_topics)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    body = resp.json()

    assert body["topic_links"] == [{"level": "5", "subject": "Math", "lesson": "Solving Equations"}]
    # Unique (level, subject) pairs only, best-scoring first, capped at 3 groups.
    assert captured_calls == [
        ("5", "Math", "Scanned local library book"),
        ("C1", "Mathematics", "Scanned local library book"),
        ("UG1", "Mathematics", "Scanned local library book"),
    ]


def test_analyze_endpoint_skips_topic_linking_for_literature(tmp_folder, monkeypatch):
    import app.main as main_module

    file_id = index_one_book(tmp_folder)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "literature", "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "subject": "", "synopsis": ""}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    called = []
    monkeypatch.setattr(local_library, "analyse_text", lambda *a, **k: called.append(1))
    monkeypatch.setattr(main_module, "curate_book_topics", lambda *a, **k: called.append(1))

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    assert resp.json()["topic_links"] == []
    assert called == []


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


def test_analyze_endpoint_moves_nonfiction_into_az_author_folder_and_syncs_nonfiction_library(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder, filename="sapiens.txt", content="A brief history of humankind. " * 30)
    long_synopsis = "Word " * 900  # stand-in for an 800-1500 word synopsis

    def fake_analyze(filename, text_excerpt):
        return {
            "classification": "non-fiction", "title": "Sapiens",
            "author": "Yuval Noah Harari", "subject": "", "synopsis": long_synopsis,
        }
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    assert resp.status_code == 200
    body = resp.json()

    assert body["analysis"]["classification"] == "non-fiction"
    assert body["world_literature"] is None
    assert body["nonfiction"] == {"category": "science", "book_id": "sapiens", "title": "Sapiens", "created": False}
    assert body["lesson_matches"] == []

    # Non-fiction files the same way as literature -- A-Z-by-author, not Reference/subject.
    new_path = Path(body["file"]["path"])
    assert new_path.exists()
    assert new_path.parent.name == "Yuval Noah Harari"
    assert new_path.parent.parent.name == "Y"
    assert body["file"]["classification"] == "non-fiction"
    assert body["file"]["synopsis"] == long_synopsis


def test_analyze_endpoint_creates_new_nonfiction_entry_when_no_match(tmp_folder, monkeypatch):
    file_id = index_one_book(tmp_folder, filename="memoir.txt", content="My life story. " * 30)

    def fake_analyze(filename, text_excerpt):
        return {"classification": "non-fiction", "title": "My Local Memoir", "author": "New Author", "subject": "", "synopsis": "A synopsis."}
    monkeypatch.setattr(ai_tutor, "analyze_book_for_library", fake_analyze)

    resp = client.post(f"/api/local-library/files/{file_id}/analyze")
    body = resp.json()
    assert body["nonfiction"]["created"] is True
    assert body["nonfiction"]["category"] == "local"
    assert body["world_literature"] is None
