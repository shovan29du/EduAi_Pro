from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_biographies_overview():
    resp = client.get("/api/biographies")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_people"] >= 250
    assert len(data["sections"]) >= 10
    section_ids = {s["id"] for s in data["sections"]}
    assert "bengali_notable_people" in section_ids
    assert "science_innovation" in section_ids


def test_bengali_notable_people_has_at_least_30():
    resp = client.get("/api/biographies/bengali_notable_people")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["people"]) >= 30


def test_all_biography_summaries_are_1000_to_3000_words():
    overview = client.get("/api/biographies").json()
    for section in overview["sections"]:
        detail = client.get(f"/api/biographies/{section['id']}").json()
        for person in detail["people"]:
            word_count = len(person["summary"].split())
            assert 1000 <= word_count <= 3000, f"{person['name']} has {word_count} words"
            assert person["links"]["wikipedia"].startswith("https://en.wikipedia.org/wiki/")
            assert person["links"]["video"]
            assert person["wiki_title"]
            assert len(person["key_facts"]) >= 6


def test_biography_no_duplicate_ids_within_a_section():
    overview = client.get("/api/biographies").json()
    for section in overview["sections"]:
        detail = client.get(f"/api/biographies/{section['id']}").json()
        ids = [p["id"] for p in detail["people"]]
        assert len(ids) == len(set(ids)), f"duplicate ids in {section['id']}"


def test_biography_person_detail():
    resp = client.get("/api/biographies/science_innovation/marie_curie")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Marie Curie"
    assert "Nobel" in data["summary"]


def test_biography_person_not_found():
    resp = client.get("/api/biographies/science_innovation/not_a_real_person")
    assert resp.status_code == 404


def test_biography_section_not_found():
    resp = client.get("/api/biographies/not_a_real_section")
    assert resp.status_code == 404


def test_biography_search():
    resp = client.get("/api/biographies/search", params={"q": "Curie"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_matches"] >= 1
    assert any(r["name"] == "Marie Curie" for r in data["results"])


def test_biography_search_short_query_returns_empty():
    resp = client.get("/api/biographies/search", params={"q": "a"})
    assert resp.status_code == 200
    assert resp.json()["results"] == []
