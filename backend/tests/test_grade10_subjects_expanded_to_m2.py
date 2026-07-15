import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

LEVELS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"]

NEW_FLAGSHIP_SUBJECTS = [
    "Art History", "Python", "R", "JavaScript", "Prompt Engineering",
    "Computer Science Engineering", "Big Data", "MBA", "Operations Management", "AI Tools",
]

PROMOTED_TO_FLAGSHIP = ["Economics", "Finance", "Philosophy"]


def test_all_grade10_subjects_present_through_m2():
    grade10 = client.get("/api/grade/10").json()["subjects"].keys()
    for level in LEVELS:
        level_subjects = client.get(f"/api/level/{level}").json()["subjects"]
        for subject in grade10:
            assert subject in level_subjects, f"{subject} (Grade 10) missing at {level}"


@pytest.mark.parametrize("subject", NEW_FLAGSHIP_SUBJECTS)
def test_new_subjects_present_and_progress_through_levels(subject):
    seen_titles = set()
    for level in LEVELS:
        data = client.get(f"/api/level/{level}").json()
        assert subject in data["subjects"], f"{subject} missing at {level}"
        lessons = data["subjects"][subject]["lessons"]
        assert lessons, f"{subject} has no lessons at {level}"
        for lesson in lessons:
            seen_titles.add(lesson["title"])
    # Across 8 levels x 2 modules/level, expect the full 16-module ladder with no repeats.
    assert len(seen_titles) == 16, f"{subject} should have 16 distinct modules across levels, got {len(seen_titles)}"


@pytest.mark.parametrize("subject", PROMOTED_TO_FLAGSHIP)
def test_promoted_subjects_have_bespoke_capstone_at_m2(subject):
    data = client.get("/api/level/M2").json()
    lessons = data["subjects"][subject]["lessons"]
    titles = [l["title"] for l in lessons]
    assert any("Capstone" in t for t in titles), f"{subject} should reach a Capstone module by M2"


def test_python_r_javascript_use_real_official_docs():
    m1 = client.get("/api/level/M1").json()["subjects"]
    assert m1["Python"]["books"][0]["link"] == "https://docs.python.org/3/"
    assert m1["R"]["books"][0]["link"] == "https://www.r-project.org/"
    assert "developer.mozilla.org" in m1["JavaScript"]["books"][0]["link"]


def test_total_subject_count_grew_to_52():
    data = client.get("/api/level/M2").json()
    assert len(data["subjects"]) == 52
