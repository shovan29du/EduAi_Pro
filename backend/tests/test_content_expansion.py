from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_museum_world_collections_gallery_has_1000_objects():
    resp = client.get("/api/museum/world_collections")
    assert resp.status_code == 200
    assert len(resp.json()["objects"]) >= 1000


def test_museum_total_grew_past_original():
    resp = client.get("/api/museum")
    assert resp.status_code == 200
    assert resp.json()["total_objects"] >= 2500


def test_movies_library_grew_by_at_least_100():
    resp = client.get("/api/movies?per_page=1000")
    assert resp.status_code == 200
    assert resp.json()["total"] >= 445


def test_songs_library_grew_by_at_least_400():
    resp = client.get("/api/songs")
    assert resp.status_code == 200
    # Deduplication (removing repeat entries for the same song/artist added
    # by earlier expansion passes) later brought the raw total down from a
    # higher, duplicate-inflated count -- this floor reflects the current
    # deduplicated library, still comfortably above the pre-expansion baseline.
    assert resp.json()["total"] >= 1200


def test_world_literature_adult_section_has_300_plus_books():
    resp = client.get("/api/world-literature/world_classics_adult")
    assert resp.status_code == 200
    assert len(resp.json()["books"]) >= 300


def test_nonfiction_adult_section_has_200_plus_books():
    resp = client.get("/api/nonfiction/adult_advanced_nonfiction")
    assert resp.status_code == 200
    assert len(resp.json()["books"]) >= 200


def test_new_languages_registered():
    resp = client.get("/api/languages")
    assert resp.status_code == 200
    codes = {l["code"] for l in resp.json()["languages"]}
    for code in ("bn", "hi", "ur", "sw"):
        assert code in codes


def test_new_languages_have_vocab_including_slang():
    for code in ("bn", "hi", "ur", "sw"):
        resp = client.get(f"/api/languages/{code}")
        assert resp.status_code == 200
        categories = {w["category"] for w in resp.json()["vocabulary"]}
        assert "slang" in categories


def test_new_languages_have_grammar():
    for code in ("bn", "hi", "ur", "sw"):
        resp = client.get(f"/api/grammar/language/{code}")
        assert resp.status_code == 200
        assert set(resp.json()["levels"].keys()) == {"beginner", "elementary", "intermediate", "advanced"}


def test_self_defense_pathway_exists_and_is_adult_oriented():
    resp = client.get("/api/practical-skills/self_defense_adult")
    assert resp.status_code == 200
    data = resp.json()
    assert data["skills"]
    assert all(s["grade_range"] == "Adult" for s in data["skills"])


def test_adult_life_skills_pathway_exists():
    resp = client.get("/api/practical-skills/adult_life_skills")
    assert resp.status_code == 200
    assert resp.json()["skills"]


def test_adult_personal_safety_survival_category_exists():
    resp = client.get("/api/survival-skills/adult_personal_safety")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["skills"]) >= 4
    assert all(not s["adult_supervision_required"] for s in data["skills"])


def test_assessment_covers_up_to_age_60():
    resp = client.get("/api/assessment/age-groups")
    assert resp.status_code == 200
    ids = {g["id"] for g in resp.json()["age_groups"]}
    for expected in ("17-25", "26-40", "41-60"):
        assert expected in ids


def test_assessment_41_60_has_sections():
    resp = client.get("/api/assessment/41-60")
    assert resp.status_code == 200
    assert resp.json()["sections"]
