"""Download / Upload / Delete on each Virtual Museum object, with pictures kept in the database."""
import pytest
from fastapi.testclient import TestClient

from app import main, museum_pictures as mp, museum_store
from app.main import app

client = TestClient(app)
JPEG = b"\xff\xd8\xff" + b"0" * 5000
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 5000

DATA = {"title": "t", "description": "d", "galleries": {
    "g1": {"label": "One", "emoji": "x", "objects": [
        {"id": "a", "name": "Alpha", "wiki_title": "Alpha"}, {"id": "shared", "name": "Shared"}]},
    "g2": {"label": "Two", "emoji": "y", "objects": [{"id": "shared", "name": "Shared too"}, {"id": "b", "name": "Beta"}]},
}}


@pytest.fixture(autouse=True)
def museum(museum_db, tmp_path, monkeypatch):
    monkeypatch.setattr(main, "_load_museum_cached", lambda mtime: DATA)
    main._without_deleted.cache_clear()

    path = tmp_path / "museum.json"
    path.write_text("{}")
    monkeypatch.setattr(main, "_MUSEUM_PATH", path)
    monkeypatch.setattr(mp, "IMAGES_DIR", tmp_path / "images")
    monkeypatch.setattr(mp, "MANIFEST_PATH", tmp_path / "pictures.json")
    yield
    main._without_deleted.cache_clear()


def _objects(gallery):
    return client.get(f"/api/museum/{gallery}").json()["objects"]


def test_upload_stores_the_picture_in_the_database_and_shows_it():
    r = client.put("/api/museum/g1/a/picture", content=JPEG, headers={"X-Filename": "my%20photo.jpg"})
    assert r.status_code == 200
    body = r.json()
    assert body["thumbnail_local"].startswith("/api/museum/picture/a?v=") and body["picture_source"] == "upload"
    assert "uploaded by the owner" in body["image_credit"]["line"].lower()
    got = client.get("/api/museum/picture/a")
    assert got.status_code == 200 and got.content == JPEG and got.headers["content-type"] == "image/jpeg"
    assert museum_store.get_picture("a")[0] == JPEG
    # the gallery list now shows it too
    assert next(o for o in _objects("g1") if o["id"] == "a")["thumbnail_local"].startswith("/api/museum/picture/a")
    # sending the same picture again is answered "not modified"
    again = client.get("/api/museum/picture/a", headers={"If-None-Match": got.headers["etag"]})
    assert again.status_code == 304


def test_a_second_upload_replaces_the_first():
    client.put("/api/museum/g1/a/picture", content=JPEG)
    client.put("/api/museum/g1/a/picture", content=PNG)
    assert client.get("/api/museum/picture/a").headers["content-type"] == "image/png"


@pytest.mark.parametrize("payload,fragment", [
    (b"", "empty"), (b"<svg xmlns='http://www.w3.org/2000/svg'>" + b"x" * 500, "JPEG, PNG"),
    (b"not an image at all " * 50, "JPEG, PNG"), (JPEG + b"0" * (8 * 1024 * 1024), "too large")])
def test_bad_uploads_are_refused_and_nothing_is_stored(payload, fragment):
    r = client.put("/api/museum/g1/a/picture", content=payload)
    assert r.status_code in (400, 413) and fragment in r.json()["detail"]
    assert not museum_store.has_picture("a")


def test_upload_to_an_unknown_object_is_404():
    assert client.put("/api/museum/g1/nope/picture", content=JPEG).status_code == 404
    assert client.put("/api/museum/zzz/a/picture", content=JPEG).status_code == 404


def test_download_finds_the_picture_on_the_web_and_saves_it_in_the_database(monkeypatch):
    monkeypatch.setattr(mp, "_fetch_image", lambda url: (JPEG, ".jpg"))
    monkeypatch.setattr(main, "museum_thumbnail", lambda wiki_title="", q="", met_id=0: {"thumbnail_url": "https://upload.wikimedia.org/a.jpg"})
    monkeypatch.setattr(mp.image_credit, "credit_for", lambda url: {"artist": "A. Photographer", "credit": "A. Photographer", "license": "CC BY-SA 4.0", "license_url": "l", "source_url": "s"})
    r = client.post("/api/museum/g1/a/picture/download")
    assert r.status_code == 200 and r.json()["picture_source"] == "download"
    assert r.json()["image_credit"]["credit"] == "A. Photographer"
    assert museum_store.get_picture("a")[0] == JPEG


def test_download_says_so_when_nothing_is_found_or_the_network_is_down(monkeypatch):
    monkeypatch.setattr(main, "museum_thumbnail", lambda **k: {"thumbnail_url": None})
    r = client.post("/api/museum/g1/a/picture/download")
    assert r.status_code == 404 and "upload one" in r.json()["detail"]

    def down(**k):
        raise OSError("<urlopen error [Errno -3] Temporary failure>")

    monkeypatch.setattr(mp, "find_picture_url", lambda obj, wl, tried=None: (tried.append("name_search: <urlopen error x>") or (None, None, None)))
    assert client.post("/api/museum/g1/a/picture/download").status_code == 502
    assert not museum_store.has_picture("a")


def test_delete_needs_confirmation_then_removes_the_object_and_its_picture():
    client.put("/api/museum/g1/a/picture", content=JPEG)
    assert client.delete("/api/museum/g1/a").status_code == 400  # no confirmation: nothing happens
    assert any(o["id"] == "a" for o in _objects("g1")) and museum_store.has_picture("a")

    r = client.delete("/api/museum/g1/a", params={"confirm": "true"})
    assert r.status_code == 200 and r.json()["deleted"] is True
    assert [o["id"] for o in _objects("g1")] == ["shared"]
    assert client.get("/api/museum/g1/a").status_code == 404
    assert client.get("/api/museum/picture/a").status_code == 404
    assert client.get("/api/museum").json()["total_objects"] == 3
    assert [g["object_count"] for g in client.get("/api/museum").json()["galleries"]] == [1, 2]
    assert ("g1", "a") in museum_store.deleted_objects()
    assert not any(o["id"] == "a" for o in client.get("/api/museum/search", params={"q": "alpha"}).json()["results"])


def test_deleting_one_copy_keeps_the_picture_while_another_gallery_still_shows_it():
    client.put("/api/museum/g1/shared/picture", content=JPEG)
    client.delete("/api/museum/g1/shared", params={"confirm": "true"})
    assert museum_store.has_picture("shared")  # g2 still has "shared"
    client.delete("/api/museum/g2/shared", params={"confirm": "true"})
    assert not museum_store.has_picture("shared")


def test_deleting_something_that_is_not_there_is_404():
    assert client.delete("/api/museum/g1/nope", params={"confirm": "true"}).status_code == 404


def test_pictures_saved_as_files_by_the_old_downloader_move_into_the_database(tmp_path):
    images = tmp_path / "old"
    images.mkdir()
    (images / "b.jpg").write_bytes(JPEG)
    manifest = tmp_path / "pictures.json"
    manifest.write_text('{"b": {"file": "b.jpg", "credit": "Someone", "license": "CC0", "line": "Someone · CC0", "image_url": "https://x/b.jpg"}, "gone": {"file": "missing.jpg"}}')
    assert museum_store.import_legacy_files(images, manifest) == 1
    assert museum_store.get_picture("b")[0] == JPEG
    assert museum_store.stored_pictures()["b"]["credit"]["license"] == "CC0"
    assert museum_store.import_legacy_files(images, manifest) == 0  # once each
