import json

from fastapi.testclient import TestClient

from app import main
from app.main import app

client = TestClient(app)


class _FakeResponse:
    """Minimal stand-in for the object returned by urllib's urlopen."""

    def __init__(self, payload):
        self._payload = json.dumps(payload).encode("utf-8")

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def test_museum_thumbnail_requires_wiki_title():
    resp = client.get("/api/museum/thumbnail")
    assert resp.status_code == 400


def test_museum_thumbnail_fetches_and_caches_to_disk(monkeypatch, tmp_path):
    monkeypatch.setattr(main, "_MUSEUM_THUMB_CACHE_DIR", tmp_path)
    calls = []

    def fake_urlopen(req, timeout=5):
        calls.append(req.full_url)
        return _FakeResponse({"thumbnail": {"source": "https://example.org/thumb.jpg"}})

    monkeypatch.setattr(main, "urlopen", fake_urlopen)

    resp = client.get("/api/museum/thumbnail", params={"wiki_title": "Mona Lisa"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["thumbnail_url"] == "https://example.org/thumb.jpg"
    assert body["cached"] is False
    assert len(calls) == 1

    cache_files = list(tmp_path.glob("*.json"))
    assert len(cache_files) == 1
    on_disk = json.loads(cache_files[0].read_text(encoding="utf-8"))
    assert on_disk["thumbnail_url"] == "https://example.org/thumb.jpg"
    assert "fetched_at" in on_disk

    # A second request for the same title should be served from the disk
    # cache instead of calling out to Wikipedia again.
    resp2 = client.get("/api/museum/thumbnail", params={"wiki_title": "Mona Lisa"})
    assert resp2.status_code == 200
    body2 = resp2.json()
    assert body2["thumbnail_url"] == "https://example.org/thumb.jpg"
    assert body2["cached"] is True
    assert len(calls) == 1


def test_museum_thumbnail_falls_back_to_stale_cache_on_fetch_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(main, "_MUSEUM_THUMB_CACHE_DIR", tmp_path)

    cache_path = main._museum_thumb_cache_path("Old Painting")
    cache_path.write_text(
        json.dumps({
            "wiki_title": "Old Painting",
            "thumbnail_url": "https://example.org/stale.jpg",
            "fetched_at": 0,
        }),
        encoding="utf-8",
    )

    def fake_urlopen(req, timeout=5):
        raise OSError("network unavailable")

    monkeypatch.setattr(main, "urlopen", fake_urlopen)

    resp = client.get("/api/museum/thumbnail", params={"wiki_title": "Old Painting"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["thumbnail_url"] == "https://example.org/stale.jpg"
    assert body.get("stale") is True
