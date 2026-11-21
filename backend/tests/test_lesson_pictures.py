"""Download / Upload of lesson pictures (Survival, Practical, subject lessons), stored in the database."""
import pytest
from fastapi.testclient import TestClient

from app import image_search, lesson_enrichment as le, lesson_pictures as lp, museum_pictures
from app.main import app

client = TestClient(app)
JPEG = b"\xff\xd8\xff" + b"0" * 5000
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 5000
KEY = "survival/personal_safety/Stranger Awareness"


@pytest.fixture(autouse=True)
def isolated(museum_db, tmp_path, monkeypatch):
    monkeypatch.setattr(le, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(image_search, "search", lambda *a, **k: [])  # no live network in tests


ARTICLE = {"title": "Stranger danger", "description": "", "extract": "x", "page_url": "https://en.wikipedia.org/wiki/Stranger_danger",
           "thumbnail_url": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Sd.jpg"}


def test_upload_is_saved_in_the_database_and_served_back():
    r = client.put("/api/lesson-picture", params={"key": KEY}, content=JPEG, headers={"X-Filename": "mine.jpg"})
    assert r.status_code == 200
    body = r.json()
    assert body["stored"] is True and body["source"] == "upload" and body["title"] == "Your uploaded picture"
    assert body["thumbnail_url"].startswith("/api/lesson-picture?key=survival%2Fpersonal_safety%2FStranger%20Awareness&v=")
    got = client.get("/api/lesson-picture", params={"key": KEY})
    assert got.content == JPEG and got.headers["content-type"] == "image/jpeg"
    assert client.get("/api/lesson-picture", params={"key": KEY}, headers={"If-None-Match": got.headers["etag"]}).status_code == 304
    client.put("/api/lesson-picture", params={"key": KEY}, content=PNG)  # replaces
    assert client.get("/api/lesson-picture", params={"key": KEY}).headers["content-type"] == "image/png"


@pytest.mark.parametrize("payload,fragment", [(b"", "empty"), (b"<svg>" + b"x" * 500, "JPEG, PNG"), (JPEG + b"0" * (8 * 1024 * 1024), "too large")])
def test_bad_uploads_are_refused(payload, fragment):
    r = client.put("/api/lesson-picture", params={"key": KEY}, content=payload)
    assert r.status_code in (400, 413) and fragment in r.json()["detail"]
    assert client.get("/api/lesson-picture", params={"key": KEY}).status_code == 404


@pytest.mark.parametrize("key", ["", "nothing", "other/x/y", "survival/", "survival/" + "x" * 500])
def test_only_lesson_keys_are_accepted(key):
    assert client.put("/api/lesson-picture", params={"key": key}, content=JPEG).status_code == 400
    assert client.post("/api/lesson-picture/download", json={"key": key, "title": "t"}).status_code == 400


def test_the_lesson_lookup_returns_the_stored_picture_instead_of_wikipedia(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda *a, **k: ARTICLE)
    plain = client.get("/api/lesson-enrichment/wiki", params={"q": "Stranger Awareness", "key": KEY}).json()
    assert plain["title"] == "Stranger danger" and "stored" not in plain  # nothing saved yet: automatic picture
    client.put("/api/lesson-picture", params={"key": KEY}, content=JPEG)
    after = client.get("/api/lesson-enrichment/wiki", params={"q": "Stranger Awareness", "key": KEY}).json()
    assert after["stored"] is True and after["thumbnail_url"].startswith("/api/lesson-picture?key=")
    # even a lesson with no title to search for shows its stored picture
    assert client.get("/api/lesson-enrichment/wiki", params={"key": KEY}).json()["stored"] is True


def test_download_saves_the_web_picture_with_its_credit(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda title, q, ctx: {**ARTICLE, "_args": (title, q, ctx)})
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: (JPEG, ".jpg"))
    monkeypatch.setattr(lp.image_credit, "credit_for", lambda url: {"artist": "A. Photographer", "credit": "A. Photographer", "license": "CC BY-SA 4.0", "license_url": "l", "source_url": "s"})
    r = client.post("/api/lesson-picture/download", json={"key": KEY, "title": "Stranger Awareness", "context": "Personal Safety", "wiki_title": ""})
    assert r.status_code == 200
    body = r.json()
    assert body["source"] == "download" and body["title"] == "Stranger danger" and body["credit"]["line"].startswith("A. Photographer")
    assert body["page_url"] == "https://en.wikipedia.org/wiki/Stranger_danger"
    assert client.get("/api/lesson-picture", params={"key": KEY}).content == JPEG


def test_download_says_why_when_it_cannot(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda *a: None)
    r = client.post("/api/lesson-picture/download", json={"key": KEY, "title": "x"})
    assert r.status_code == 404 and "upload one" in r.json()["detail"]

    def down(*a):
        raise OSError("offline")

    monkeypatch.setattr(le, "find_article", down)
    monkeypatch.setattr(image_search, "search", lambda q, *a, log=None, **k: (log or []).extend(f"{n}: offline" for n in image_search.SOURCES) or [])
    assert client.post("/api/lesson-picture/download", json={"key": KEY, "title": "x"}).status_code == 502
    monkeypatch.setattr(le, "find_article", lambda *a: ARTICLE)
    monkeypatch.setattr(museum_pictures, "_fetch_image", down)
    assert client.post("/api/lesson-picture/download", json={"key": KEY, "title": "x"}).status_code == 502
    assert client.post("/api/lesson-picture/download", json={"key": KEY}).status_code == 400
    assert client.get("/api/lesson-picture", params={"key": KEY}).status_code == 404


def _hit(n, source="Openverse (flickr)", **extra):
    return {"source": source, "url": f"https://img.example/{n}.jpg", "fallback_url": "", "title": f"Photo {n}",
            "credit": {"credit": f"Person {n}", "license": "CC BY 2.0", "license_url": "l", "source_url": f"https://page.example/{n}", "line": f"Person {n} · CC BY 2.0"}, **extra}


def test_download_searches_beyond_wikipedia_and_credits_the_source(monkeypatch):
    queries = []
    monkeypatch.setattr(le, "find_article", lambda *a: None)  # Wikipedia has nothing
    monkeypatch.setattr(image_search, "search", lambda q, *a, **k: queries.append(q) or [_hit(1)])
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: (JPEG, ".jpg"))
    r = client.post("/api/lesson-picture/download", json={"key": KEY, "title": "Stranger Awareness", "context": "Personal Safety"})
    assert r.status_code == 200
    body = r.json()
    assert body["source_name"] == "Openverse (flickr)" and body["title"] == "Photo 1"
    assert body["credit"]["line"] == "Person 1 · CC BY 2.0" and body["page_url"] == "https://page.example/1"
    assert queries[0] == "Stranger Awareness"


def test_pressing_download_again_gives_the_next_picture_then_starts_over(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda *a: ARTICLE)
    monkeypatch.setattr(image_search, "search", lambda q, *a, **k: [_hit(1), _hit(2)])
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: (JPEG, ".jpg"))
    monkeypatch.setattr(lp.image_credit, "credit_for", lambda url: {})
    seen = [client.post("/api/lesson-picture/download", json={"key": KEY, "title": "x"}).json()["title"] for _ in range(4)]
    assert seen == ["Stranger danger", "Photo 1", "Photo 2", "Stranger danger"]


def test_a_picture_that_cannot_be_fetched_is_skipped_for_the_next_one(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda *a: None)
    monkeypatch.setattr(image_search, "search", lambda q, *a, **k: [_hit(1), {**_hit(2), "fallback_url": "https://img.example/2-full.jpg"}, _hit(3)])

    def fetch(url):
        if url in ("https://img.example/1.jpg", "https://img.example/2.jpg"):
            raise OSError("403")
        return JPEG, ".jpg"

    monkeypatch.setattr(museum_pictures, "_fetch_image", fetch)
    assert client.post("/api/lesson-picture/download", json={"key": KEY, "title": "x"}).json()["title"] == "Photo 2"  # via its fallback url
