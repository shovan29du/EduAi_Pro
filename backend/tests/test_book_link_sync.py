import json

import pytest

from app import book_link_sync


@pytest.fixture(autouse=True)
def isolated_paths(monkeypatch, tmp_path):
    wlit_path = tmp_path / "library.json"
    wlit_path.write_text(json.dumps({
        "title": "World Literature Library",
        "description": "test",
        "sections": {
            "childrens_classics": {
                "label": "Children's Classics",
                "emoji": "📖",
                "age_range": "5-12",
                "books": [
                    {
                        "id": "alice_wonderland",
                        "title": "Alice's Adventures in Wonderland",
                        "author": "Lewis Carroll",
                        "summary": "Old summary.",
                        "links": {"read_online": "https://www.gutenberg.org/ebooks/11", "wikipedia": "https://en.wikipedia.org/wiki/Alice"},
                    },
                ],
            },
        },
    }))
    monkeypatch.setattr(book_link_sync, "WLIT_PATH", wlit_path)

    syllabus_dir = tmp_path / "syllabus"
    syllabus_dir.mkdir()
    (syllabus_dir / "grade5.json").write_text(json.dumps({
        "subjects": {
            "English": {
                "books": [
                    {"id": "b1", "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "link": "https://www.gutenberg.org/ebooks/11"},
                    {"id": "b2", "title": "Unrelated Book", "author": "Someone Else", "link": "https://example.com/unrelated"},
                ],
                "textbooks": [
                    {"id": "t1", "title": "A Study Guide", "author": "Jane Q. Smith", "link": "https://example.com/guide"},
                ],
            },
        },
    }))
    (syllabus_dir / "grade6.json").write_text(json.dumps({
        "subjects": {"Math": {"books": []}},
    }))
    monkeypatch.setattr(book_link_sync, "SYLLABUS_DIR", syllabus_dir)
    yield wlit_path, syllabus_dir


def test_sync_world_literature_replaces_link_and_summary_on_match(isolated_paths):
    wlit_path, _ = isolated_paths
    result = book_link_sync.sync_world_literature(
        "Alice's Adventures in Wonderland", "Lewis Carroll", "/api/local-library/files/abc123", "New AI synopsis."
    )
    assert result == {"section": "childrens_classics", "book_id": "alice_wonderland", "title": "Alice's Adventures in Wonderland", "created": False}

    data = json.loads(wlit_path.read_text())
    book = data["sections"]["childrens_classics"]["books"][0]
    assert book["links"]["read_online"] == "/api/local-library/files/abc123"
    assert book["links"]["local_copy"] is True
    assert book["links"]["wikipedia"] == "https://en.wikipedia.org/wiki/Alice"  # untouched
    assert book["summary"] == "New AI synopsis."


def test_sync_world_literature_matches_by_last_name_despite_middle_name(isolated_paths):
    result = book_link_sync.sync_world_literature(
        "Alice's Adventures in Wonderland", "Lewis  Carroll Jr", "/api/local-library/files/x", ""
    )
    assert result["created"] is False
    assert result["book_id"] == "alice_wonderland"


def test_sync_world_literature_creates_new_local_entry_when_no_match(isolated_paths):
    wlit_path, _ = isolated_paths
    result = book_link_sync.sync_world_literature(
        "My Unpublished Novel", "Some Author", "/api/local-library/files/y", "A synopsis."
    )
    assert result["created"] is True
    assert result["section"] == "local"

    data = json.loads(wlit_path.read_text())
    local_books = data["sections"]["local"]["books"]
    assert len(local_books) == 1
    assert local_books[0]["title"] == "My Unpublished Novel"
    assert local_books[0]["links"]["read_online"] == "/api/local-library/files/y"
    assert local_books[0]["summary"] == "A synopsis."


def test_sync_world_literature_does_not_match_same_title_different_author(isolated_paths):
    result = book_link_sync.sync_world_literature(
        "Alice's Adventures in Wonderland", "Someone Unrelated", "/api/local-library/files/z", ""
    )
    assert result["created"] is True  # no author match -> treated as a new book


def test_sync_syllabus_books_replaces_matching_book_and_textbook_links(isolated_paths):
    _, syllabus_dir = isolated_paths
    updated = book_link_sync.sync_syllabus_books(
        "Alice's Adventures in Wonderland", "Lewis Carroll", "/api/local-library/files/abc123"
    )
    assert updated == [{"file": "grade5.json", "subject": "English", "title": "Alice's Adventures in Wonderland"}]

    data = json.loads((syllabus_dir / "grade5.json").read_text())
    books = data["subjects"]["English"]["books"]
    assert books[0]["link"] == "/api/local-library/files/abc123"
    assert books[0]["local_copy"] is True
    assert books[1]["link"] == "https://example.com/unrelated"  # unrelated book untouched


def test_sync_syllabus_books_matches_textbooks_resource_too(isolated_paths):
    _, syllabus_dir = isolated_paths
    updated = book_link_sync.sync_syllabus_books("A Study Guide", "Jane Smith", "/api/local-library/files/t1")
    assert updated == [{"file": "grade5.json", "subject": "English", "title": "A Study Guide"}]

    data = json.loads((syllabus_dir / "grade5.json").read_text())
    assert data["subjects"]["English"]["textbooks"][0]["link"] == "/api/local-library/files/t1"


def test_sync_syllabus_books_no_match_leaves_files_unwritten(isolated_paths):
    _, syllabus_dir = isolated_paths
    before = (syllabus_dir / "grade6.json").stat().st_mtime
    updated = book_link_sync.sync_syllabus_books("Nothing Like This", "Nobody", "/api/local-library/files/n")
    assert updated == []
    after = (syllabus_dir / "grade6.json").stat().st_mtime
    assert before == after
