import json

import pytest
from fastapi.testclient import TestClient

from app import image_credit
from app import museum_pictures as mp
from app.main import app

client = TestClient(app)

JPEG = b"\xff\xd8\xff" + b"0" * 5000


@pytest.fixture(autouse=True)
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(mp, "IMAGES_DIR", tmp_path / "images")
    monkeypatch.setattr(mp, "MANIFEST_PATH", tmp_path / "pictures.json")
    monkeypatch.setattr(mp, "CACHE_DIR", tmp_path / "cache")


def test_met_thumbnail_returns_only_public_domain_pictures(monkeypatch):
    monkeypatch.setattr(mp, "_get_json", lambda url: {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/a/web-large/x.jpg", "primaryImage": "https://images.metmuseum.org/a/original/x.jpg"})
    assert mp.met_thumbnail(436532)["thumbnail_url"] == "https://images.metmuseum.org/a/web-large/x.jpg"
    monkeypatch.setattr(mp, "_get_json", lambda url: {"isPublicDomain": False, "primaryImageSmall": "https://images.metmuseum.org/b.jpg"})
    assert mp.met_thumbnail(2)["thumbnail_url"] is None


def test_met_thumbnail_is_cached_but_a_network_failure_is_not(monkeypatch):
    calls = []

    def ok(url):
        calls.append(url)
        return {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/c.jpg"}

    monkeypatch.setattr(mp, "_get_json", ok)
    mp.met_thumbnail(7)
    assert mp.met_thumbnail(7)["cached"] is True and len(calls) == 1

    def down(url):
        raise OSError("offline")

    monkeypatch.setattr(mp, "_get_json", down)
    assert mp.met_thumbnail(8) == {"thumbnail_url": None, "cached": False}
    monkeypatch.setattr(mp, "_get_json", ok)
    assert mp.met_thumbnail(8)["thumbnail_url"].endswith("c.jpg")  # not remembered as 'no picture'


def test_thumbnail_endpoint_accepts_a_met_id(monkeypatch):
    monkeypatch.setattr(mp, "_get_json", lambda url: {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/d.jpg"})
    body = client.get("/api/museum/thumbnail", params={"met_id": 11}).json()
    assert body["thumbnail_url"] == "https://images.metmuseum.org/d.jpg" and body["met_id"] == 11


def test_met_images_are_credited_as_cc0():
    record = image_credit.credit_for("https://images.metmuseum.org/CRDImages/ep/web-large/DT1567.jpg")
    assert record["license"].startswith("CC0") and "Metropolitan" in record["credit"]


def test_overlay_points_an_object_at_its_downloaded_picture(tmp_path):
    (tmp_path / "images").mkdir()
    (tmp_path / "images" / "met_1.jpg").write_bytes(JPEG)
    (tmp_path / "pictures.json").write_text(json.dumps({"met_1": {"file": "met_1.jpg", "credit": "The Met", "license": "CC0 1.0", "license_url": "u", "source_url": "s", "line": "The Met · CC0 1.0"}}))
    obj = {"id": "met_1", "name": "X", "thumbnail_local": "/museum-resource/thumbnails/met_1.svg"}
    shown = mp.overlay(obj)
    assert shown["thumbnail_local"] == "/museum-resource/images/met_1.jpg"
    assert shown["image_credit"]["line"] == "The Met · CC0 1.0"
    assert obj["thumbnail_local"].endswith(".svg")  # the stored object is untouched
    assert mp.overlay({"id": "other"}) == {"id": "other"}
    (tmp_path / "images" / "met_1.jpg").unlink()  # a missing file means no overlay
    assert mp.overlay(obj) is obj


def _network(monkeypatch, images):
    monkeypatch.setattr(mp, "_fetch_image", lambda url: images[url])
    monkeypatch.setattr(mp, "_get_json", lambda url: {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/m.jpg"})
    monkeypatch.setattr(mp.image_credit, "credit_for", lambda url: {"artist": "A. Photographer", "credit": "A. Photographer", "license": "CC BY-SA 4.0", "license_url": "l", "source_url": "s"})


def test_download_pictures_saves_files_credits_and_resumes(monkeypatch):
    _network(monkeypatch, {"https://images.metmuseum.org/m.jpg": (JPEG, ".jpg"), "https://cdn.example/cma.jpg": (JPEG, ".jpg"), "https://upload.wikimedia.org/w.jpg": (JPEG, ".jpg")})
    objects = [
        {"id": "met_9", "met_id": 9, "name": "Met thing"},
        {"id": "cma-1", "name": "Cleveland thing", "thumbnail_local": "https://cdn.example/cma.jpg"},
        {"id": "w_1", "name": "Wiki thing", "wiki_title": "Wiki thing"},
        {"id": "w_2", "name": "Nothing found"},
    ]
    lookups = []

    def wiki(title, q):
        lookups.append((title, q))
        return "https://upload.wikimedia.org/w.jpg" if title else None

    stats = mp.download_pictures(objects, wiki, sleep=0, log=lambda *_: None)
    assert stats == {"downloaded": 3, "no_picture": 1, "failed": 0, "skipped": 0}
    manifest = json.loads(mp.MANIFEST_PATH.read_text())
    assert set(manifest) == {"met_9", "cma-1", "w_1"}
    assert manifest["met_9"]["license"].startswith("CC0") and (mp.IMAGES_DIR / manifest["met_9"]["file"]).read_bytes() == JPEG
    assert manifest["w_1"]["credit"] == "A. Photographer" and manifest["w_1"]["line"].startswith("A. Photographer")
    assert lookups[0] == ("Wiki thing", "Wiki thing")  # the Met and Cleveland objects never use name search

    again = mp.download_pictures(objects, wiki, sleep=0, log=lambda *_: None)  # resumable: only the unfinished one is retried
    assert again["skipped"] == 3 and again["downloaded"] == 0


def test_download_pictures_counts_failures_and_retries_them_later(monkeypatch):
    state = {"down": True}

    def fetch(url):
        if state["down"]:
            raise OSError("rate limited")
        return JPEG, ".jpg"

    monkeypatch.setattr(mp, "_fetch_image", fetch)
    monkeypatch.setattr(mp, "_get_json", lambda url: {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/m.jpg"})
    objects = [{"id": "met_5", "met_id": 5, "name": "X"}]
    assert mp.download_pictures(objects, lambda *a: None, sleep=0, log=lambda *_: None)["failed"] == 1
    assert not mp.MANIFEST_PATH.exists() or "met_5" not in json.loads(mp.MANIFEST_PATH.read_text())
    state["down"] = False
    assert mp.download_pictures(objects, lambda *a: None, sleep=0, log=lambda *_: None)["downloaded"] == 1


def test_non_image_responses_are_rejected(monkeypatch):
    class Resp:
        headers = {"Content-Type": "text/html"}

        def read(self):
            return b"<html>" + b"x" * 5000

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    monkeypatch.setattr(mp, "urlopen", lambda *a, **k: Resp())
    with pytest.raises(ValueError):
        mp._fetch_image("https://example.org/page")


def test_the_limit_stops_the_run(monkeypatch):
    _network(monkeypatch, {"https://images.metmuseum.org/m.jpg": (JPEG, ".jpg")})
    objects = [{"id": f"met_{i}", "met_id": i, "name": "X"} for i in range(1, 6)]
    stats = mp.download_pictures(objects, lambda *a: None, limit=2, sleep=0, log=lambda *_: None)
    assert stats["downloaded"] == 2
