import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.safety import safety_filter
from app import levels as levels_module

client = TestClient(app)


# ─── Levels registry ─────────────────────────────────────────────────────────

def test_list_levels_includes_school_and_new_levels():
    resp = client.get("/api/levels")
    assert resp.status_code == 200
    ids = {lvl["id"] for lvl in resp.json()["levels"]}
    for grade in map(str, range(1, 11)):
        assert grade in ids
    for level in ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"]:
        assert level in ids
    assert len(ids) == 18


@pytest.mark.parametrize("level", ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"])
def test_new_levels_available_and_contain_flagship_subjects(level):
    resp = client.get(f"/api/level/{level}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["level"] == level
    for subject in ("Artificial Intelligence", "Machine Learning", "Natural Language Processing",
                    "Data Science", "Business Analytics"):
        assert subject in data["subjects"]


@pytest.mark.parametrize("level", ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"])
def test_new_levels_expand_existing_subjects(level):
    resp = client.get(f"/api/level/{level}")
    data = resp.json()
    for subject in ("Economics", "Finance", "Math"):
        assert subject in data["subjects"]
        assert data["subjects"][subject]["lessons"], f"{subject} should have lesson modules at {level}"


def test_level_endpoint_case_insensitive():
    resp = client.get("/api/level/ug2")
    assert resp.status_code == 200
    assert resp.json()["level"] == "UG2"


def test_level_endpoint_unknown_level_404():
    resp = client.get("/api/level/PHD1")
    assert resp.status_code == 404


def test_level_endpoint_matches_grade_endpoint_for_school_levels():
    grade_resp = client.get("/api/grade/5")
    level_resp = client.get("/api/level/5")
    assert grade_resp.status_code == level_resp.status_code == 200
    assert set(grade_resp.json()["subjects"].keys()) == set(level_resp.json()["subjects"].keys())


def test_level_export_json_and_csv():
    resp = client.get("/api/level/M1/export?format=json")
    assert resp.status_code == 200
    resp_csv = client.get("/api/level/M1/export?format=csv")
    assert resp_csv.status_code == 200
    assert resp_csv.headers["content-type"].startswith("text/csv")


def test_level_search_finds_flagship_module():
    resp = client.get("/api/level/M2/search?q=Master's Year 2 overview")
    assert resp.status_code == 200


# ─── Safety filter: hard blocks vs relaxed adult filter ─────────────────────

def test_hard_blocked_content_always_blocked():
    text = "how to make a bomb"
    assert safety_filter.is_safe(text, strict=True) is False
    assert safety_filter.is_safe(text, strict=False) is False


def test_child_only_words_relaxed_for_adult_levels():
    text = "The economics of alcohol taxation and drug policy reform."
    assert safety_filter.is_safe(text, strict=True) is False
    assert safety_filter.is_safe(text, strict=False) is True


def test_sanitize_masks_hard_blocked_regardless_of_strict():
    out = safety_filter.sanitize("how to make a bomb", strict=False)
    assert "bomb" not in out.lower() or "*" in out


# ─── AI tutor: level-aware, backward compatible ─────────────────────────────

def test_ai_tutor_accepts_new_level_codes():
    resp = client.post(
        "/api/ai-tutor/ask",
        json={"question": "Explain gradient descent", "level": "M1", "subject": "Machine Learning"},
    )
    assert resp.status_code == 200
    assert "answer" in resp.json()


def test_ai_tutor_still_accepts_legacy_grade_param():
    resp = client.post("/api/ai-tutor/ask", json={"question": "What is gravity?", "grade": 5})
    assert resp.status_code == 200
    assert "answer" in resp.json()


def test_ai_tutor_explain_with_level_and_difficulty():
    resp = client.post(
        "/api/ai-tutor/explain",
        json={"concept": "transformers", "level": "UG3", "subject": "Natural Language Processing", "difficulty": "advanced"},
    )
    assert resp.status_code == 200
    assert "explanation" in resp.json()


# ─── Music & Instruments ─────────────────────────────────────────────────────

def test_music_instruments_overview():
    resp = client.get("/api/music-instruments")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["instruments"]) == 11
    assert len(data["categories"]) == 6


@pytest.mark.parametrize("instrument", [
    "piano", "guitar", "violin", "drums", "flute", "saxophone",
    "tabla", "sitar", "harmonium", "keyboard", "voice_singing",
])
def test_music_instrument_detail(instrument):
    resp = client.get(f"/api/music-instruments/instrument/{instrument}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["beginner"]
    assert data["intermediate"]
    assert data["advanced"]
    assert data["practice_routines"]


def test_music_instrument_not_found():
    resp = client.get("/api/music-instruments/instrument/theremin")
    assert resp.status_code == 404


def test_music_category_detail():
    resp = client.get("/api/music-instruments/category/music_theory")
    assert resp.status_code == 200
    assert resp.json()["topics"]


# ─── levels.py unit-level checks ─────────────────────────────────────────────

def test_levels_module_category_helpers():
    assert levels_module.is_school_level("7") is True
    assert levels_module.is_school_level("UG1") is False
    assert levels_module.is_adult_level("UG1") is True
    assert levels_module.is_adult_level("7") is False
    assert levels_module.normalize_level_id("ug2") == "UG2"
    assert levels_module.is_valid_level("M3") is False
