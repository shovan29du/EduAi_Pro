"""Lesson pictures: several per lesson, found across many collections, checked against the topic, kept in the database."""
import pytest
from fastapi.testclient import TestClient

from app import image_search, lesson_enrichment as le, lesson_pictures as lp, museum_pictures
from app.main import app

client = TestClient(app)
JPEG = b"\xff\xd8\xff" + b"0" * 5000
JPEG2 = b"\xff\xd8\xff" + b"1" * 5000
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 5000
KEY = "survival/personal_safety/Stranger Awareness"


@pytest.fixture(autouse=True)
def isolated(museum_db, tmp_path, monkeypatch):
    monkeypatch.setattr(le, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(le, "find_article", lambda *a: None)
    monkeypatch.setattr(image_search, "search", lambda *a, **k: [])  # no live network in tests


def put(data, key=KEY, name="mine.jpg"):
    return client.put("/api/lesson-picture", params={"key": key}, content=data, headers={"X-Filename": name})


# ── uploads ───────────────────────────────────────────────────────────────────
def test_uploads_are_added_not_replaced_and_served_from_the_database():
    first = put(JPEG, name="one.jpg").json()
    second = put(PNG, name="two.png").json()
    assert first["added"] is True and len(first["pictures"]) == 1
    assert [p["title"] for p in second["pictures"]] == ["one", "two"] and second["stored"] is True
    image = client.get(second["pictures"][1]["url"])
    assert image.content == PNG and image.headers["content-type"] == "image/png"
    assert client.get(second["pictures"][0]["url"]).content == JPEG
    assert client.get(second["pictures"][0]["url"], headers={"If-None-Match": image.headers["etag"]}).status_code in (200, 304)
    assert client.get(f"/api/lesson-picture/list", params={"key": KEY}).json()["pictures"][0]["source"] == "upload"


def test_uploading_the_same_picture_twice_is_noticed():
    put(JPEG)
    again = put(JPEG).json()
    assert again["duplicate"] is True and len(again["pictures"]) == 1


def test_a_lesson_can_hold_twelve_pictures():
    for n in range(lp.MAX_PER_LESSON):
        assert put(b"\xff\xd8\xff" + bytes([n]) * 5000).status_code == 200
    r = put(JPEG2)
    assert r.status_code == 400 and "up to 12" in r.json()["detail"]


@pytest.mark.parametrize("payload,fragment", [(b"", "empty"), (b"<svg>" + b"x" * 500, "JPEG, PNG"), (JPEG + b"0" * (8 * 1024 * 1024), "too large")])
def test_bad_uploads_are_refused(payload, fragment):
    r = put(payload)
    assert r.status_code in (400, 413) and fragment in r.json()["detail"]
    assert client.get("/api/lesson-picture/list", params={"key": KEY}).json()["pictures"] == []


@pytest.mark.parametrize("key", ["", "nothing", "other/x/y", "survival/", "survival/" + "x" * 500])
def test_only_lesson_keys_are_accepted(key):
    assert put(JPEG, key=key).status_code == 400
    assert client.post("/api/lesson-picture/search", json={"key": key, "title": "t"}).status_code == 400
    assert client.post("/api/lesson-picture/save", json={"key": key, "pictures": [{"url": "https://x/y.jpg", "token": "t"}]}).status_code == 400


def test_a_picture_can_be_removed():
    put(JPEG)
    ids = [p["id"] for p in put(PNG).json()["pictures"]]
    gone = client.delete(f"/api/lesson-picture/{ids[0]}").json()
    assert gone["removed"] is True and [p["id"] for p in gone["pictures"]] == [ids[1]]
    assert client.get(f"/api/lesson-picture/{ids[0]}/image").status_code == 404
    last = client.delete(f"/api/lesson-picture/{ids[1]}").json()
    assert last["pictures"] == [] and client.delete(f"/api/lesson-picture/{ids[1]}").status_code == 404


def test_the_lesson_lookup_returns_saved_pictures_instead_of_wikipedia(monkeypatch):
    article = {"title": "Stranger danger", "description": "", "extract": "x", "page_url": "https://en.wikipedia.org/wiki/Stranger_danger",
               "thumbnail_url": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Sd.jpg"}
    monkeypatch.setattr(le, "find_article", lambda *a, **k: article)
    plain = client.get("/api/lesson-enrichment/wiki", params={"q": "Stranger Awareness", "key": KEY}).json()
    assert plain["title"] == "Stranger danger" and "stored" not in plain  # nothing saved yet: the automatic picture
    put(JPEG)
    put(PNG, name="b.png")
    after = client.get("/api/lesson-enrichment/wiki", params={"q": "Stranger Awareness", "key": KEY}).json()
    assert after["stored"] is True and len(after["pictures"]) == 2 and after["thumbnail_url"] == after["pictures"][0]["url"]
    assert client.get("/api/lesson-enrichment/wiki", params={"key": KEY}).json()["stored"] is True


def test_pictures_from_the_one_picture_version_move_across(museum_db):
    from app import database
    from app.models import LessonPicture
    with database.session_scope() as db:
        db.add(LessonPicture(key=KEY, kind="survival", content_type="image/jpeg", data=JPEG, size=len(JPEG), sha1="a" * 40,
                             source="upload", credit={"title": "Mine", "line": "Picture uploaded by the owner of this app"}))
    assert lp.import_legacy_single_pictures() == 1
    assert lp.import_legacy_single_pictures() == 0
    items = client.get("/api/lesson-picture/list", params={"key": KEY}).json()["pictures"]
    assert len(items) == 1 and items[0]["title"] == "Mine"


# ── searching: many sources, ranked by fit ────────────────────────────────────
def hit(n, title, text="", source="Openverse (flickr)", **extra):
    return {"source": source, "url": f"https://img.example/{n}.jpg", "fallback_url": "", "title": title, "text": text,
            "credit": {"credit": f"Person {n}", "license": "CC BY 2.0", "license_url": "l", "source_url": f"https://page.example/{n}",
                       "line": f"Person {n} · CC BY 2.0"}, **extra}


def fake_search(monkeypatch, hits, queries=None):
    def search(q, order=None, per_source=3, log=None, topic=None):
        if queries is not None:
            queries.append(q)
        out = [dict(h) for h in hits]
        for h in out:
            h["score"] = image_search.relevance(h, topic["title"], topic["description"], topic["context"])
            h["match"] = image_search.match_label(h["score"])
        return sorted(out, key=lambda h: -h["score"])

    monkeypatch.setattr(image_search, "search", search)


def test_search_returns_signed_candidates_best_fit_first_and_labelled(monkeypatch):
    queries = []
    fake_search(monkeypatch, [hit(1, "Sunset over the sea"), hit(2, "Teaching children about stranger awareness", "safe adult circle")], queries)
    body = client.post("/api/lesson-picture/search", json={
        "key": KEY, "title": "Stranger Awareness", "context": "Personal Safety",
        "description": "Identify safe adults and know what to do if approached"}).json()
    cands = body["candidates"]
    assert [c["title"] for c in cands][0] == "Teaching children about stranger awareness"
    assert cands[0]["match"] == "Good match" and cands[-1]["match"] == "Weak match" and cands[0]["score"] > cands[-1]["score"]
    assert all(c["token"] == lp.sign(c["url"]) for c in cands)
    assert "Stranger Awareness" in queries and any("Personal Safety" in q for q in queries)
    assert body["max"] == 12 and body["saved"] == 0


def test_search_leaves_out_pictures_already_shown(monkeypatch):
    fake_search(monkeypatch, [hit(1, "Stranger awareness"), hit(2, "Stranger awareness poster")])
    r = client.post("/api/lesson-picture/search", json={"key": KEY, "title": "Stranger Awareness", "exclude": ["https://img.example/1.jpg"]}).json()
    assert [c["url"] for c in r["candidates"]] == ["https://img.example/2.jpg"]


def test_the_wikipedia_picture_is_a_candidate_too(monkeypatch):
    monkeypatch.setattr(le, "find_article", lambda *a: {"title": "Stranger danger", "description": "Child safety campaign", "extract": "Stranger awareness teaches children",
                                                         "page_url": "https://en.wikipedia.org/wiki/Stranger_danger", "thumbnail_url": "https://upload.wikimedia.org/a.jpg"})
    monkeypatch.setattr(lp.image_credit, "credit_for", lambda url: {"artist": "A", "license": "CC BY-SA 4.0"})
    r = client.post("/api/lesson-picture/search", json={"key": KEY, "title": "Stranger Awareness"}).json()
    assert r["candidates"][0]["source"] == "Wikipedia" and r["candidates"][0]["match"] == "Good match"


def test_search_says_when_nothing_is_found_or_the_connection_is_down(monkeypatch):
    assert client.post("/api/lesson-picture/search", json={"key": KEY, "title": "x"}).json()["candidates"] == []
    monkeypatch.setattr(image_search, "search", lambda q, *a, log=None, **k: log.extend(f"{n}: offline" for n in image_search.SOURCES) or [])
    assert client.post("/api/lesson-picture/search", json={"key": KEY, "title": "x"}).status_code == 502
    assert client.post("/api/lesson-picture/search", json={"key": KEY}).status_code == 400


# ── saving the ones picked ────────────────────────────────────────────────────
def pick(n, **extra):
    h = hit(n, f"Photo {n}")
    return {"url": h["url"], "token": lp.sign(h["url"]), "title": h["title"], "source": h["source"], "credit": h["credit"],
            "page_url": h["credit"]["source_url"], **extra}


def test_saving_several_picked_pictures_adds_them_all_with_credits(monkeypatch):
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: ((JPEG if url.endswith("1.jpg") else JPEG2), ".jpg"))
    r = client.post("/api/lesson-picture/save", json={"key": KEY, "pictures": [pick(1), pick(2)]}).json()
    assert r["saved"] == 2 and r["failed"] == [] and len(r["pictures"]) == 2
    assert r["pictures"][0]["title"] == "Photo 1" and r["pictures"][0]["source_name"] == "Openverse (flickr)"
    assert r["pictures"][1]["credit"]["line"] == "Person 2 · CC BY 2.0" and r["pictures"][1]["page_url"] == "https://page.example/2"
    again = client.post("/api/lesson-picture/save", json={"key": KEY, "pictures": [pick(1)]}).json()
    assert again["saved"] == 0 and again["already_saved"] == 1 and len(again["pictures"]) == 2


def test_a_picture_that_cannot_be_downloaded_is_reported_but_the_others_are_kept(monkeypatch):
    def fetch(url):
        if url.endswith("1.jpg"):
            raise OSError("403")
        return JPEG2, ".jpg"

    monkeypatch.setattr(museum_pictures, "_fetch_image", fetch)
    r = client.post("/api/lesson-picture/save", json={"key": KEY, "pictures": [pick(1), pick(2)]}).json()
    assert r["saved"] == 1 and r["failed"][0]["title"] == "Photo 1"
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: (_ for _ in ()).throw(OSError("down")))
    assert client.post("/api/lesson-picture/save", json={"key": "survival/a/b", "pictures": [pick(3)]}).status_code == 502


def test_the_fallback_address_is_used_when_the_first_will_not_download(monkeypatch):
    fb = "https://img.example/full.jpg"
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: (_ for _ in ()).throw(OSError("x")) if url.endswith("1.jpg") else (JPEG, ".jpg"))
    r = client.post("/api/lesson-picture/save", json={"key": KEY, "pictures": [pick(1, fallback_url=fb, fallback_token=lp.sign(fb))]}).json()
    assert r["saved"] == 1


def test_only_addresses_this_server_found_can_be_saved(monkeypatch):
    fetched = []
    monkeypatch.setattr(museum_pictures, "_fetch_image", lambda url: fetched.append(url) or (JPEG, ".jpg"))
    forged = {**pick(1), "token": "0" * 32}
    local = {"url": "http://127.0.0.1:8080/api/levels", "token": lp.sign("http://127.0.0.1:8080/api/levels"), "title": "x"}
    private = {"url": "http://192.168.1.1/a.jpg", "token": lp.sign("http://192.168.1.1/a.jpg"), "title": "y"}
    r = client.post("/api/lesson-picture/save", json={"key": KEY, "pictures": [forged, local, private, pick(2)]}).json()
    assert r["saved"] == 1 and len(r["failed"]) == 3 and fetched == ["https://img.example/2.jpg"]
