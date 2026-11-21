import json

import pytest
from fastapi.testclient import TestClient

from app import image_credit
from app import museum_pictures as mp
from app import museum_store
from app.main import app

client = TestClient(app)

JPEG = b"\xff\xd8\xff" + b"0" * 5000


@pytest.fixture(autouse=True)
def isolated(tmp_path, monkeypatch, museum_db):
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


def test_download_pictures_saves_to_the_database_with_credits_and_resumes(monkeypatch):
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
    stored = museum_store.stored_pictures()
    assert set(stored) == {"met_9", "cma-1", "w_1"}
    assert stored["met_9"]["credit"]["license"].startswith("CC0") and museum_store.get_picture("met_9")[0] == JPEG
    assert stored["w_1"]["credit"]["credit"] == "A. Photographer" and stored["w_1"]["credit"]["line"].startswith("A. Photographer")
    assert not mp.IMAGES_DIR.exists() or not list(mp.IMAGES_DIR.iterdir())  # nothing written as a loose file
    assert lookups[0] == ("Wiki thing", "")  # its own article first; Met and Cleveland objects never search by name

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
    assert not museum_store.has_picture("met_5")
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


# ── using the links an object already has ─────────────────────────────────────
def test_wikipedia_article_links_give_the_article_title_but_search_pages_do_not():
    assert mp.wikipedia_title("https://en.wikipedia.org/wiki/Rosetta_Stone") == "Rosetta Stone"
    assert mp.wikipedia_title("https://en.wikipedia.org/wiki/Mona_Lisa_(painting)") == "Mona Lisa (painting)"
    assert mp.wikipedia_title("https://en.wikipedia.org/wiki/Caf%C3%A9_Terrace_at_Night") == "Café Terrace at Night"
    assert mp.wikipedia_title("https://en.wikipedia.org/w/index.php?search=Basket") is None
    assert mp.wikipedia_title("https://example.org/wiki/X") is None


def test_candidate_sources_try_the_objects_own_links_first_and_search_by_name_last():
    obj = {"id": "x", "name": "Rosetta Stone", "origin": "Egypt", "wiki_title": "Rosetta Stone (artifact)",
           "links": {"wikipedia": "https://en.wikipedia.org/wiki/Rosetta_Stone", "wikidata": "https://www.wikidata.org/wiki/Q48584",
                     "museum_object": "https://www.britishmuseum.org/collection/object/Y_EA24"}}
    kinds = [k for k, _ in mp.candidate_sources(obj)]
    assert kinds == ["museum_page", "wikipedia_article", "wikidata_item", "wikipedia_article", "name_search"]
    values = dict((k, v) for k, v in mp.candidate_sources(obj) if k in ("museum_page", "wikidata_item", "name_search"))
    assert values == {"museum_page": "https://www.britishmuseum.org/collection/object/Y_EA24", "wikidata_item": "Q48584", "name_search": "Rosetta Stone Egypt"}


def test_met_and_cleveland_links_use_their_open_access_sources_not_the_page():
    met = {"id": "met_1", "met_id": 1, "name": "N", "links": {"museum_object": "https://www.metmuseum.org/art/collection/search/1"}}
    assert [k for k, _ in mp.candidate_sources(met)][0] == "met_api" and "museum_page" not in [k for k, _ in mp.candidate_sources(met)]
    cma = {"id": "cma-1915.534", "name": "N", "links": {"museum_object": "https://clevelandart.org/art/1915.534"}}
    assert list(mp.candidate_sources(cma))[0] == ("image_url", "https://openaccess-cdn.clevelandart.org/1915.534/1915.534_web.jpg")


def test_page_image_url_reads_og_image_in_either_attribute_order_and_resolves_relative_links():
    page = '<head><meta property="og:image" content="/img/object.jpg"><meta name="x" content="y"></head>'
    assert mp.page_image_url("https://museum.example/object/1", page) == "https://museum.example/img/object.jpg"
    assert mp.page_image_url("https://m.example/o", '<meta content="https://cdn.example/a.png" name="twitter:image">') == "https://cdn.example/a.png"
    assert mp.page_image_url("https://m.example/o", "<html>no picture</html>") is None


def test_a_source_that_fails_is_skipped_and_the_next_link_is_tried(monkeypatch):
    obj = {"id": "w", "name": "Thing", "wiki_title": "Thing", "links": {"wikipedia": "https://en.wikipedia.org/wiki/Thing",
                                                                          "wikidata": "https://www.wikidata.org/wiki/Q1"}}

    def broken_wikidata(qid):
        raise OSError("404")

    monkeypatch.setattr(mp, "wikidata_image_url", broken_wikidata)
    monkeypatch.setattr(mp.image_credit, "credit_for", lambda url: None)
    asked = []

    def wiki(title, q):
        asked.append((title, q))
        return None if title == "Thing" else "https://upload.wikimedia.org/found.jpg"

    tried = []
    url, credit, how = mp.find_picture_url(obj, wiki, tried)
    assert (url, how) == ("https://upload.wikimedia.org/found.jpg", "name_search")
    assert asked == [("Thing", ""), ("", "Thing")] and any("wikidata_item" in t for t in tried)


def test_wikidata_image_becomes_a_commons_url(monkeypatch):
    monkeypatch.setattr(mp, "_get_json", lambda url: {"entities": {"Q9": {"claims": {"P18": [{"mainsnak": {"datavalue": {"value": "Mona Lisa, by Leonardo da Vinci.jpg"}}}]}}}})
    url = mp.wikidata_image_url("Q9")
    assert url.startswith("https://commons.wikimedia.org/wiki/Special:FilePath/Mona_Lisa%2C_by_Leonardo_da_Vinci.jpg")
    assert image_credit.commons_filename(url).replace("_", " ") == "Mona Lisa, by Leonardo da Vinci.jpg"  # so its credit can be looked up
    monkeypatch.setattr(mp, "_get_json", lambda url: {"entities": {"Q9": {"claims": {}}}})
    assert mp.wikidata_image_url("Q9") is None


def test_page_pictures_are_downloaded_with_an_honest_credit(monkeypatch):
    monkeypatch.setattr(mp, "page_image_url", lambda url, page_html=None: "https://museum.example/o1.jpg")
    monkeypatch.setattr(mp, "_fetch_image", lambda url: (JPEG, ".jpg"))
    obj = {"id": "o1", "name": "Object", "links": {"museum_object": "https://museum.example/object/1"}}
    stats = mp.download_pictures([obj], lambda *a: None, sleep=0, log=lambda *_: None)
    entry = museum_store.stored_pictures()["o1"]["credit"]
    assert stats["downloaded"] == 1 and entry["found_via"] == "museum_page" and entry["license"] is None
    assert "check its terms" in entry["line"] and entry["source_url"] == "https://museum.example/object/1"


def test_objects_with_no_picture_come_first(monkeypatch):
    objs = [{"id": "cma-1", "name": "has url", "thumbnail_local": "https://cdn.example/1.jpg"}, {"id": "met_2", "met_id": 2, "name": "met"},
            {"id": "none", "name": "no picture", "thumbnail_local": "/museum-resource/thumbnails/none.svg"}]
    assert [o["id"] for o in mp.prioritise(objs)] == ["none", "met_2", "cma-1"]


def test_only_missing_skips_objects_that_already_show_a_picture(monkeypatch):
    _network(monkeypatch, {"https://cdn.example/1.jpg": (JPEG, ".jpg"), "https://upload.wikimedia.org/w.jpg": (JPEG, ".jpg")})
    objs = [{"id": "cma-1", "name": "has url", "thumbnail_local": "https://cdn.example/1.jpg"}, {"id": "w", "name": "wiki", "wiki_title": "wiki"}]
    stats = mp.download_pictures(objs, lambda t, q: "https://upload.wikimedia.org/w.jpg", sleep=0, log=lambda *_: None, only_missing=True)
    assert stats["downloaded"] == 1 and stats["skipped"] == 1
    assert set(museum_store.stored_pictures()) == {"w"}


def test_still_missing_objects_are_reported_with_what_was_tried(monkeypatch):
    monkeypatch.setattr(mp.image_credit, "credit_for", lambda url: None)
    obj = {"id": "m", "name": "Mystery", "links": {"wikipedia": "https://en.wikipedia.org/wiki/Mystery"}}
    stats = mp.download_pictures([obj], lambda t, q: None, sleep=0, log=lambda *_: None)
    report = json.loads(mp.MANIFEST_PATH.with_name("pictures_missing.json").read_text())
    assert stats["no_picture"] == 1 and report["m"]["name"] == "Mystery"
    assert any("wikipedia_article" in t for t in report["m"]["tried"]) and any("name_search" in t for t in report["m"]["tried"])


# ── checking links ────────────────────────────────────────────────────────────
def test_only_links_to_specific_pages_are_checked():
    obj = {"links": {"museum_object": "https://www.metmuseum.org/art/collection/search/1", "wikipedia": "https://en.wikipedia.org/w/index.php?search=X",
                     "wikidata": "https://www.wikidata.org/wiki/Q1", "video": "https://www.youtube.com/results?search_query=x", "image_search": "https://commons.wikimedia.org/w/index.php?search=x"}}
    assert set(mp.checkable_links(obj)) == {"museum_object", "wikidata"}


class _Resp:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def test_check_link_reports_status_and_falls_back_from_head_to_get(monkeypatch):
    import urllib.error
    methods = []

    def fake(req, timeout=0):
        methods.append(req.get_method())
        if req.get_method() == "HEAD":
            raise urllib.error.HTTPError(req.full_url, 405, "Method Not Allowed", {}, None)
        return _Resp(200)

    monkeypatch.setattr(mp, "urlopen", fake)
    assert mp.check_link("https://a.example/x") == {"status": 200, "ok": True, "error": None}
    assert methods == ["HEAD", "GET"]

    def gone(req, timeout=0):
        raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, None)

    monkeypatch.setattr(mp, "urlopen", gone)
    result = mp.check_link("https://a.example/missing")
    assert result["ok"] is False and result["status"] == 404

    def offline(req, timeout=0):
        raise OSError("no network")

    monkeypatch.setattr(mp, "urlopen", offline)
    assert mp.check_link("https://a.example/x")["ok"] is False


def test_check_links_writes_a_report_of_broken_links(monkeypatch):
    monkeypatch.setattr(mp, "check_link", lambda url: {"status": 404, "ok": False, "error": "x"} if "bad" in url else {"status": 200, "ok": True, "error": None})
    objects = [{"id": "a", "links": {"museum_object": "https://m.example/good"}}, {"id": "b", "links": {"museum_object": "https://m.example/bad", "wikidata": "https://www.wikidata.org/wiki/Q2"}}]
    logged = []
    report = mp.check_links(objects, sleep=0, log=logged.append)
    assert report["a"]["museum_object"]["ok"] and not report["b"]["museum_object"]["ok"] and report["b"]["wikidata"]["ok"]
    assert any("broken museum_object: b" in line for line in logged)
    assert json.loads(mp.MANIFEST_PATH.with_name("link_report.json").read_text()) == report
