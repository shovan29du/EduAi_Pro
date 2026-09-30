from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_famous_masterpieces_gallery_exists():
    resp = client.get("/api/museum/famous_masterpieces")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["objects"]) >= 400


def test_famous_objects_include_well_known_real_works():
    resp = client.get("/api/museum/famous_masterpieces")
    names = {o["name"] for o in resp.json()["objects"]}
    for expected in ("Mona Lisa", "The Starry Night", "David", "Rosetta Stone", "The Great Pyramid of Giza"):
        assert expected in names


def test_famous_objects_have_no_duplicate_wiki_titles():
    resp = client.get("/api/museum/famous_masterpieces")
    titles = [o["wiki_title"] for o in resp.json()["objects"]]
    assert len(titles) == len(set(titles))


def test_famous_objects_all_have_wiki_title_for_live_thumbnail():
    resp = client.get("/api/museum/famous_masterpieces")
    for obj in resp.json()["objects"]:
        assert obj.get("wiki_title"), f"{obj.get('name')} missing wiki_title"
        assert obj["links"]["wikipedia"].startswith("https://en.wikipedia.org/wiki/")


def test_museum_overview_reflects_growth():
    resp = client.get("/api/museum")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_objects"] >= 3100
    assert len(data["galleries"]) >= 15


def test_world_heritage_treasures_objects_have_wiki_title():
    # world_heritage_treasures is the real-curated-object successor to the
    # old single "world_collections" gallery; the newer wc_-prefixed themed
    # galleries (world_visual_arts etc.) are generic study cards without a
    # single identifiable real-world source, so they don't carry a wiki_title.
    resp = client.get("/api/museum/world_heritage_treasures")
    objects = resp.json()["objects"]
    assert len(objects) >= 1000
    assert all(o.get("wiki_title") for o in objects)


def test_famous_object_detail_lookup():
    resp = client.get("/api/museum/famous_masterpieces/fm_0001")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Mona Lisa"
