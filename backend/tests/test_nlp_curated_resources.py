import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

LEVELS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"]


@pytest.mark.parametrize("level", LEVELS)
def test_nlp_has_curated_library_book_and_course_resources(level):
    data = client.get(f"/api/level/{level}").json()
    subject = data["subjects"]["Natural Language Processing"]

    text_titles = {r["title"] for r in subject["text_resources"]}
    assert "spaCy (library)" in text_titles
    assert "Hugging Face Transformers (library)" in text_titles

    book_titles = {b["title"] for b in subject["books"]}
    assert "Speech and Language Processing" in book_titles

    course_titles = {c["title"] for c in subject["external_courses"]}
    assert "CS224N: Deep Learning for Natural Language Processing" in course_titles
    assert "Hugging Face NLP Course" in course_titles


@pytest.mark.parametrize("level", LEVELS)
def test_nlp_curated_resources_are_all_marked_safe(level):
    data = client.get(f"/api/level/{level}").json()
    subject = data["subjects"]["Natural Language Processing"]
    for resource in subject["text_resources"] + subject["books"] + subject["external_courses"]:
        assert resource.get("safe") is True
