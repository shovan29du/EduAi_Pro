import json
import shutil
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import ai_tutor, local_library
from app.main import app

client = TestClient(app)


@pytest.fixture
def tmp_folder():
    tmp = Path(tempfile.mkdtemp())
    yield tmp
    shutil.rmtree(tmp, ignore_errors=True)


@pytest.fixture(autouse=True)
def isolated_db(monkeypatch, tmp_path):
    db_path = tmp_path / "local_library_test.sqlite3"
    monkeypatch.setattr(local_library, "DB_PATH", db_path)
    yield


def fake_analyse_local_media(filename, category, text_excerpt=""):
    if category == "books":
        return {"kind": "", "genre": "Science", "title": "", "ai_summary": "A summary about photosynthesis."}
    kind = "Lecture recording" if category == "videos" else "Music track"
    return {"kind": kind, "genre": "Biology", "title": "Cleaned Title", "ai_summary": ""}


def test_parse_local_media_analysis_for_books():
    raw = "GENRE: Fantasy\nSUMMARY: A tale of dragons and knights."
    result = ai_tutor._parse_local_media_analysis(raw, "books")
    assert result == {"kind": "", "genre": "Fantasy", "title": "", "ai_summary": "A tale of dragons and knights."}


def test_parse_local_media_analysis_for_video():
    raw = "KIND: Lecture recording\nGENRE: Biology\nTITLE: Photosynthesis Lecture"
    result = ai_tutor._parse_local_media_analysis(raw, "videos")
    assert result == {"kind": "Lecture recording", "genre": "Biology", "title": "Photosynthesis Lecture", "ai_summary": ""}


def test_analyse_local_media_falls_back_gracefully_when_offline():
    # No ANTHROPIC_API_KEY is set in this sandbox, so _call returns the
    # "Ark AI is offline" fallback text, which shouldn't match any field.
    result = ai_tutor.analyse_local_media("some_video.mp4", "videos")
    assert result == {"kind": "", "genre": "", "title": "", "ai_summary": ""}


def test_scan_folder_categorises_by_extension_and_calls_ai(tmp_folder, monkeypatch):
    monkeypatch.setattr(ai_tutor, "analyse_local_media", fake_analyse_local_media)
    (tmp_folder / "book1.txt").write_text("Photosynthesis converts sunlight into energy. " * 20)
    (tmp_folder / "lecture.mp4").write_bytes(b"fake video")
    (tmp_folder / "track.mp3").write_bytes(b"fake audio")
    (tmp_folder / "photo.png").write_bytes(b"fake image")

    result = local_library.scan_folder(str(tmp_folder), analyse_books=True, max_files=100, max_ai_calls=10)

    assert result["indexed"] == 4
    assert result["books_analysed"] == 1
    assert result["ai_analysed"] == 3  # book, video, audio -- not the picture
    assert result["truncated_ai"] is False

    by_name = {f["filename"]: f for f in result["files"]}
    assert by_name["book1.txt"]["category"] == "books"
    assert by_name["book1.txt"]["ai_genre"] == "Science"
    assert by_name["book1.txt"]["summary"] == "A summary about photosynthesis."
    assert by_name["lecture.mp4"]["category"] == "videos"
    assert by_name["lecture.mp4"]["ai_kind"] == "Lecture recording"
    assert by_name["lecture.mp4"]["ai_title"] == "Cleaned Title"
    assert by_name["track.mp3"]["category"] == "audio"
    assert by_name["track.mp3"]["ai_kind"] == "Music track"
    assert by_name["photo.png"]["category"] == "pictures"
    assert by_name["photo.png"]["ai_kind"] == ""


def test_scan_folder_reuses_analysis_for_unchanged_files(tmp_folder, monkeypatch):
    calls = []

    def counting_fake(filename, category, text_excerpt=""):
        calls.append(filename)
        return fake_analyse_local_media(filename, category, text_excerpt)

    monkeypatch.setattr(ai_tutor, "analyse_local_media", counting_fake)
    (tmp_folder / "book1.txt").write_text("Photosynthesis converts sunlight into energy. " * 20)

    local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=10)
    assert calls == ["book1.txt"]

    calls.clear()
    result = local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=10)
    assert calls == []
    assert result["ai_analysed"] == 0
    assert result["indexed"] == 1
    assert result["files"][0]["ai_genre"] == "Science"


def test_scan_folder_prunes_removed_files_and_analyses_new_ones(tmp_folder, monkeypatch):
    monkeypatch.setattr(ai_tutor, "analyse_local_media", fake_analyse_local_media)
    (tmp_folder / "keep.mp3").write_bytes(b"keep me")
    (tmp_folder / "remove.mp3").write_bytes(b"remove me")

    local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=10)

    (tmp_folder / "remove.mp3").unlink()
    (tmp_folder / "added.mp3").write_bytes(b"new file")
    result = local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=10)

    filenames = {f["filename"] for f in result["files"]}
    assert filenames == {"keep.mp3", "added.mp3"}


def test_scan_folder_respects_max_ai_calls_cap(tmp_folder, monkeypatch):
    calls = []

    def counting_fake(filename, category, text_excerpt=""):
        calls.append(filename)
        return fake_analyse_local_media(filename, category, text_excerpt)

    monkeypatch.setattr(ai_tutor, "analyse_local_media", counting_fake)
    for i in range(5):
        (tmp_folder / f"track{i}.mp3").write_bytes(b"audio")

    result = local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=2)
    assert len(calls) == 2
    assert result["ai_analysed"] == 2
    assert result["truncated_ai"] is True
    assert result["indexed"] == 5


def test_scan_folder_does_not_ai_analyse_when_analyse_books_is_false(tmp_folder, monkeypatch):
    calls = []
    monkeypatch.setattr(ai_tutor, "analyse_local_media", lambda *a, **k: calls.append(1) or fake_analyse_local_media(*a, **k))
    (tmp_folder / "track.mp3").write_bytes(b"audio")

    result = local_library.scan_folder(str(tmp_folder), analyse_books=False, max_files=100, max_ai_calls=10)
    assert calls == []
    assert result["ai_analysed"] == 0


def test_local_library_open_serves_file_from_disk(tmp_folder, monkeypatch):
    monkeypatch.setattr(ai_tutor, "analyse_local_media", fake_analyse_local_media)
    (tmp_folder / "book.txt").write_text("hello world content")
    local_library.scan_folder(str(tmp_folder), max_files=100, max_ai_calls=10)
    files = local_library.list_files(root_path=str(tmp_folder.resolve()))
    assert len(files) == 1
    file_id = files[0]["id"]

    resp = client.get(f"/api/local-library/files/{file_id}")
    assert resp.status_code == 200
    assert resp.content == b"hello world content"


def test_local_library_scan_endpoint(tmp_folder, monkeypatch):
    monkeypatch.setattr(ai_tutor, "analyse_local_media", fake_analyse_local_media)
    (tmp_folder / "notes.txt").write_text("Photosynthesis is important. " * 10)

    resp = client.post("/api/local-library/scan", json={"folder": str(tmp_folder), "max_ai_calls": 10})
    assert resp.status_code == 200
    data = resp.json()
    assert data["indexed"] == 1
    assert data["ai_analysed"] == 1
