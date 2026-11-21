import json

import pytest
from fastapi.testclient import TestClient

from app import image_credit
from app.main import app

client = TestClient(app)


class _Resp:
    def __init__(self, payload):
        self._b = json.dumps(payload).encode()

    def read(self):
        return self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


COMMONS_META = {"query": {"pages": {"123": {"imageinfo": [{"extmetadata": {
    "Artist": {"value": '<a href="//commons.wikimedia.org/wiki/User:Foo">Jane &amp; Co</a>'},
    "Credit": {"value": "Own work"},
    "LicenseShortName": {"value": "CC BY-SA 4.0"},
    "LicenseUrl": {"value": "https://creativecommons.org/licenses/by-sa/4.0"},
    "AttributionRequired": {"value": "true"},
}}]}}}}


@pytest.fixture(autouse=True)
def _tmp_cache(monkeypatch, tmp_path):
    monkeypatch.setattr(image_credit, "CACHE_DIR", tmp_path)


@pytest.mark.parametrize("url,expected", [
    ("https://commons.wikimedia.org/wiki/Special:FilePath/Rosetta_Stone.JPG", "Rosetta_Stone.JPG"),
    ("https://commons.wikimedia.org/wiki/Special:FilePath/K%C3%B6nigsthron_Bamum.jpg", "Königsthron_Bamum.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Rosetta_Stone.JPG/320px-Rosetta_Stone.JPG", "Rosetta_Stone.JPG"),
    ("https://upload.wikimedia.org/wikipedia/commons/a/a9/Rosetta_Stone.JPG", "Rosetta_Stone.JPG"),
    ("https://upload.wikimedia.org/wikipedia/en/a/a9/Fair_use.jpg", None),
    ("https://example.org/pic.jpg", None),
])
def test_commons_filename_parsing(url, expected):
    assert image_credit.commons_filename(url) == expected


def test_commons_credit_reads_licence_and_strips_html(monkeypatch):
    calls = []
    monkeypatch.setattr(image_credit, "urlopen", lambda req, timeout=5: calls.append(req.full_url) or _Resp(COMMONS_META))
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Rosetta_Stone.JPG/320px-Rosetta_Stone.JPG"
    body = client.get("/api/museum/credit", params={"image": url}).json()
    assert body["known"] is True
    assert body["artist"] == "Jane & Co"
    assert body["license"] == "CC BY-SA 4.0"
    assert body["license_url"] == "https://creativecommons.org/licenses/by-sa/4.0"
    assert body["line"] == "Jane & Co · CC BY-SA 4.0"
    assert body["source_url"] == "https://commons.wikimedia.org/wiki/File:Rosetta_Stone.JPG"
    assert "titles=File:Rosetta_Stone.JPG" in calls[0]
    again = client.get("/api/museum/credit", params={"image": url}).json()
    assert again == body and len(calls) == 1  # served from the disk cache


def test_cleveland_images_are_cc0_without_a_network_call(monkeypatch):
    monkeypatch.setattr(image_credit, "urlopen", lambda *a, **k: pytest.fail("no network call expected"))
    body = client.get("/api/museum/credit", params={"image": "https://openaccess-cdn.clevelandart.org/1915.534/1915.534_web.jpg"}).json()
    assert body["line"] == "Cleveland Museum of Art · CC0 1.0 (Open Access)"
    assert body["source_url"] == "https://clevelandart.org/art/1915.534"
    assert body["license_url"].startswith("https://creativecommons.org/publicdomain/zero")


def test_unknown_sources_and_placeholders_are_not_known(monkeypatch):
    monkeypatch.setattr(image_credit, "urlopen", lambda *a, **k: pytest.fail("no network call expected"))
    for image in ("", "/museum-resource/thumbnails/rosetta_stone.svg", "https://example.org/pic.jpg"):
        body = client.get("/api/museum/credit", params={"image": image}).json()
        assert body["known"] is False and body["line"] == ""


def test_network_failure_is_not_cached(monkeypatch, tmp_path):
    def boom(*a, **k):
        raise OSError("offline")

    monkeypatch.setattr(image_credit, "urlopen", boom)
    url = "https://commons.wikimedia.org/wiki/Special:FilePath/Rosetta_Stone.JPG"
    assert client.get("/api/museum/credit", params={"image": url}).json()["known"] is False
    assert list(tmp_path.glob("*.json")) == []
    monkeypatch.setattr(image_credit, "urlopen", lambda req, timeout=5: _Resp(COMMONS_META))
    assert client.get("/api/museum/credit", params={"image": url}).json()["known"] is True


def test_missing_metadata_still_links_to_the_source_page(monkeypatch):
    monkeypatch.setattr(image_credit, "urlopen", lambda req, timeout=5: _Resp({"query": {"pages": {"-1": {"missing": ""}}}}))
    body = client.get("/api/museum/credit", params={"image": "https://commons.wikimedia.org/wiki/Special:FilePath/Gone.jpg"}).json()
    assert body["known"] is True and body["line"] == ""
    assert body["source_url"] == "https://commons.wikimedia.org/wiki/File:Gone.jpg"
