import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

NEW_SUBJECTS = [
    "Web Development", "Cybersecurity", "Cloud Computing",
    "Digital Marketing", "UI/UX Design", "Project Management",
]

LEVELS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"]


@pytest.mark.parametrize("level", LEVELS)
def test_new_subjects_present_at_every_level(level):
    resp = client.get(f"/api/level/{level}")
    assert resp.status_code == 200
    subjects = resp.json()["subjects"]
    for subject in NEW_SUBJECTS:
        assert subject in subjects, f"{subject} missing at {level}"


@pytest.mark.parametrize("level", ["C1", "M2"])
def test_every_subject_has_external_course_links(level):
    resp = client.get(f"/api/level/{level}")
    data = resp.json()
    for name, subject in data["subjects"].items():
        courses = subject.get("external_courses")
        assert courses, f"{name} at {level} has no external_courses"
        sources = {c["source"] for c in courses}
        for expected in ("Udemy", "Coursera", "edX", "MIT OpenCourseWare", "Harvard Online Learning", "Pinterest"):
            assert expected in sources, f"{name} at {level} missing {expected} link"
        for course in courses:
            assert course["url"].startswith("https://")
            assert course.get("safe") is True


def test_movies_have_streaming_search_link():
    resp = client.get("/api/movies?per_page=1000")
    movies = resp.json()["movies"]
    assert movies
    for m in movies[:20]:
        assert m.get("streaming_search", "").startswith("https://www.justwatch.com/")


def test_music_instruments_have_pinterest_link():
    resp = client.get("/api/music-instruments/instrument/piano")
    assert resp.status_code == 200
    assert resp.json()["pinterest_search"].startswith("https://www.pinterest.com/")


def test_music_categories_have_pinterest_resource():
    resp = client.get("/api/music-instruments/category/music_theory")
    assert resp.status_code == 200
    sources = [r["title"] for r in resp.json()["resources"]]
    assert any("Pinterest" in t for t in sources)


@pytest.mark.parametrize("grade,subject", [
    (1, "Math"), (5, "Math"), (10, "Math"),
    (1, "Science"), (8, "Physics"), (9, "Chemistry"), (10, "Biology"),
])
def test_k12_math_and_science_have_benchmark_curricula_links(grade, subject):
    """Math cites Singapore MOE and MIT OpenCourseWare; the sciences cite
    IB, AP, and Khan Academy -- the specific benchmark curricula
    requested for gap comparison, reusing the existing external_courses
    field and "More Courses" tab."""
    resp = client.get(f"/api/level/{grade}")
    assert resp.status_code == 200
    subjects = resp.json()["subjects"]
    courses = subjects[subject].get("external_courses")
    assert courses, f"{subject} at grade {grade} has no external_courses"
    sources = {c["source"] for c in courses}
    if subject == "Math":
        for expected in ("Singapore MOE", "MIT OpenCourseWare", "Khan Academy"):
            assert expected in sources, f"Math at grade {grade} missing {expected} link"
    else:
        for expected in ("IB", "AP", "Khan Academy"):
            assert expected in sources, f"{subject} at grade {grade} missing {expected} link"
    for course in courses:
        assert course["url"].startswith("https://")
        assert course.get("safe") is True


@pytest.mark.parametrize("level", LEVELS)
def test_college_levels_have_ivy_league_benchmark_links(level):
    """Every subject at C1/C2/UG1-4/M1/M2 gets curated Ivy League and
    top-program links (Stanford, Yale, Wharton, Princeton) appended
    alongside the existing generic course-search sources."""
    resp = client.get(f"/api/level/{level}")
    assert resp.status_code == 200
    subjects = resp.json()["subjects"]
    for name, subject in subjects.items():
        courses = subject.get("external_courses")
        assert courses, f"{name} at {level} has no external_courses"
        sources = {c["source"] for c in courses}
        for expected in ("Stanford Online", "Open Yale Courses", "Wharton School", "Princeton University"):
            assert expected in sources, f"{name} at {level} missing {expected} link"
        for course in courses:
            assert course["url"].startswith("https://")
            assert course.get("safe") is True
