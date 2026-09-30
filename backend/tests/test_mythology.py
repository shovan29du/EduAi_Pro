from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

MYTHOLOGY_LEVELS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1"]

EXPECTED_TRADITIONS = {
    "Hindu", "Greek", "Egyptian", "Norse", "Celtic", "Mayan", "Aztec", "Inca",
    "Roman", "Mesopotamian", "Chinese", "Japanese", "Korean", "Pacific", "African",
    "Other World Mythologies",
}


def test_mythology_subject_present_at_every_level_c1_through_m1():
    for level in MYTHOLOGY_LEVELS:
        resp = client.get(f"/api/level/{level}")
        assert resp.status_code == 200
        assert "Mythology" in resp.json()["subjects"], f"Mythology missing at {level}"


def test_mythology_not_present_at_m2():
    resp = client.get("/api/level/M2")
    assert resp.status_code == 200
    assert "Mythology" not in resp.json()["subjects"]


def test_mythology_has_16_lessons_covering_all_traditions_at_each_level():
    for level in MYTHOLOGY_LEVELS:
        resp = client.get(f"/api/level/{level}/subjects/Mythology")
        assert resp.status_code == 200
        lessons = resp.json()["subject"]["lessons"]
        assert len(lessons) == 16, f"{level} has {len(lessons)} lessons"
        titles = " | ".join(lesson["title"] for lesson in lessons)
        for tradition in EXPECTED_TRADITIONS:
            assert tradition in titles, f"{tradition} missing from {level} lesson titles"


def test_mythology_reading_material_has_substantial_real_content():
    for level in MYTHOLOGY_LEVELS:
        resp = client.get(f"/api/level/{level}/subjects/Mythology")
        lessons = resp.json()["subject"]["lessons"]
        for lesson in lessons:
            word_count = len(lesson["reading_material"].split())
            assert word_count >= 400, f"{level} '{lesson['title']}' has only {word_count} words"


def test_mythology_depth_increases_from_c1_to_m1():
    def avg_words(level):
        lessons = client.get(f"/api/level/{level}/subjects/Mythology").json()["subject"]["lessons"]
        counts = [len(l["reading_material"].split()) for l in lessons]
        return sum(counts) / len(counts)

    assert avg_words("M1") > avg_words("C1")
