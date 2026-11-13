import json

import pytest
from fastapi.testclient import TestClient

from app import ai_tutor, lesson_examples
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def _tmp_stores(monkeypatch, tmp_path):
    monkeypatch.setattr(lesson_examples, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(lesson_examples, "VETTED_DIR", tmp_path / "vetted")
    monkeypatch.setattr(lesson_examples, "PENDING_DIR", tmp_path / "pending")
    monkeypatch.setattr(lesson_examples, "SYLLABUS_DIR", tmp_path / "syllabus")
    (tmp_path / "syllabus").mkdir()
    return tmp_path


BAKER = "A baker doubles a recipe that needs three quarters of a cup of sugar, which is multiplying a fraction by two."
PARAMS = {"title": "Multiplying Fractions", "subject": "Math", "lesson_id": "math-g5-l9", "level": "5", "concepts": "fraction, product"}


def _fake_ai(monkeypatch, text=BAKER):
    calls = []

    def fake(title, subject, grade=1, level=None, key_concepts=None, summary=""):
        calls.append((title, subject, tuple(key_concepts or [])))
        return text

    monkeypatch.setattr(ai_tutor, "generate_real_world_example", fake)
    return calls


def test_example_is_generated_once_then_served_from_cache(monkeypatch):
    calls = _fake_ai(monkeypatch)
    first = client.get("/api/lesson-example", params=PARAMS).json()
    second = client.get("/api/lesson-example", params=PARAMS).json()
    assert first == {"example": BAKER, "vetted": False, "cached": False}
    assert second["cached"] is True and second["example"] == BAKER
    assert calls == [("Multiplying Fractions", "Math", ("fraction", "product"))]


def test_unavailable_ai_is_reported_and_not_cached(monkeypatch, _tmp_stores):
    monkeypatch.setattr(ai_tutor, "generate_real_world_example", lambda *a, **k: None)
    body = client.get("/api/lesson-example", params={"title": "The Solar System", "subject": "Science"}).json()
    assert body["example"] is None and body["unavailable"] is True
    assert not (_tmp_stores / "cache").exists()


def test_title_is_required():
    assert client.get("/api/lesson-example", params={"title": " "}).status_code == 400


def test_generate_real_world_example_ignores_offline_message(monkeypatch):
    monkeypatch.setattr(ai_tutor, "_call", lambda *a, **k: "Ark AI is offline. Please ask your teacher.")
    assert ai_tutor.generate_real_world_example("Fractions", "Math", grade=5) is None
    monkeypatch.setattr(ai_tutor, "_call", lambda *a, **k: "Sharing a pizza into 8 slices shows fractions.")
    assert "pizza" in ai_tutor.generate_real_world_example("Fractions", "Math", grade=5)


def test_on_demand_example_enters_review_queue_and_approval_makes_it_vetted(monkeypatch):
    calls = _fake_ai(monkeypatch)
    client.get("/api/lesson-example", params=PARAMS)
    queue = client.get("/api/lesson-example/pending", params={"level": "5"}).json()
    assert queue["pending_count"] == 1 and queue["vetted_count"] == 0
    assert queue["items"][0]["lesson_id"] == "math-g5-l9" and queue["items"][0]["title"] == "Multiplying Fractions"

    edited = BAKER + " She needs one and a half cups."
    resp = client.post("/api/lesson-example/review", json={"level": "5", "lesson_id": "math-g5-l9", "action": "approve", "example": edited})
    assert resp.json() == {"status": "approved", "pending_count": 0}

    served = client.get("/api/lesson-example", params={**PARAMS, "vetted_only": "true"}).json()
    assert served == {"example": edited, "vetted": True, "cached": True}
    assert len(calls) == 1  # vetted text is served without another AI call


def test_vetted_only_never_calls_the_ai(monkeypatch):
    calls = _fake_ai(monkeypatch)
    body = client.get("/api/lesson-example", params={**PARAMS, "vetted_only": "true"}).json()
    assert body == {"example": None, "vetted": False, "cached": False}
    assert calls == []


def test_rejected_draft_is_not_served_again(monkeypatch):
    calls = _fake_ai(monkeypatch, "A wrong example that the reviewer does not like at all, for testing purposes only.")
    client.get("/api/lesson-example", params=PARAMS)
    resp = client.post("/api/lesson-example/review", json={"level": "5", "lesson_id": "math-g5-l9", "action": "reject"})
    assert resp.json()["status"] == "rejected"
    monkeypatch.setattr(ai_tutor, "generate_real_world_example", lambda *a, **k: BAKER)
    assert client.get("/api/lesson-example", params=PARAMS).json()["example"] == BAKER
    assert len(calls) == 1


def test_review_validation():
    assert client.post("/api/lesson-example/review", json={"level": "5", "lesson_id": "nope", "action": "approve"}).status_code == 404
    assert client.post("/api/lesson-example/review", json={"level": "5", "lesson_id": "x", "action": "maybe"}).status_code == 422


def test_review_flags_point_at_facts_to_check():
    flags = lesson_examples.review_flags("In 1969 about 20 per cent of people watched. " + "x" * 120)
    assert "contains a year - check it" in flags and "contains a statistic - check it" in flags
    assert lesson_examples.review_flags("short") == ["very short"]


def _write_syllabus(tmp_path, lessons):
    (tmp_path / "syllabus" / "grade5.json").write_text(
        json.dumps({"standard": 5, "subjects": {"Math": {"lessons": lessons}, "Art": {"lessons": [{"id": "art-1", "title": "Colour"}]}}}),
        encoding="utf-8",
    )


def test_pregenerate_drafts_only_missing_lessons_and_respects_limit(monkeypatch, _tmp_stores):
    _write_syllabus(_tmp_stores, [{"id": f"m{i}", "title": f"Topic {i}", "key_concepts": ["a"]} for i in range(4)])
    calls = _fake_ai(monkeypatch)
    out = client.post("/api/lesson-example/pregenerate", json={"level": "5", "subject": "Math", "limit": 3}).json()
    assert out == {"created": 3, "remaining": 1, "unavailable": False}
    out = client.post("/api/lesson-example/pregenerate", json={"level": "5", "subject": "Math", "limit": 3}).json()
    assert out == {"created": 1, "remaining": 0, "unavailable": False}
    assert [c[0] for c in calls] == ["Topic 0", "Topic 1", "Topic 2", "Topic 3"]  # Art untouched
    assert client.get("/api/lesson-example/pending", params={"level": "5"}).json()["pending_count"] == 4


def test_pregenerate_stops_at_first_ai_failure(monkeypatch, _tmp_stores):
    _write_syllabus(_tmp_stores, [{"id": f"m{i}", "title": f"Topic {i}"} for i in range(3)])
    calls = []
    monkeypatch.setattr(ai_tutor, "generate_real_world_example", lambda *a, **k: calls.append(1))
    out = client.post("/api/lesson-example/pregenerate", json={"level": "5", "subject": "Math"}).json()
    assert out == {"created": 0, "remaining": 3, "unavailable": True}
    assert len(calls) == 1


def test_pregenerate_unknown_level_and_limit_bounds():
    assert client.post("/api/lesson-example/pregenerate", json={"level": "9"}).status_code == 404
    assert client.post("/api/lesson-example/pregenerate", json={"level": "5", "limit": 500}).status_code == 422


QUESTION = {"question": "What does the baker double?", "options": {"A": "Sugar", "B": "Salt", "C": "Flour", "D": "Eggs"}, "answer": "A", "explanation": "The recipe."}


def test_quiz_is_generated_from_the_example_and_cached(monkeypatch):
    calls = []

    def fake_quiz(text, grade=1, subject="", count=5, level=None):
        calls.append((text, count))
        return [QUESTION, {"question": "bad", "options": {"A": "x", "B": "y"}, "answer": "C"}]

    monkeypatch.setattr(ai_tutor, "generate_quiz_from_text", fake_quiz)
    body = {"example": BAKER, "title": "Multiplying Fractions", "subject": "Math", "level": "5"}
    first = client.post("/api/lesson-example/quiz", json=body).json()
    second = client.post("/api/lesson-example/quiz", json=body).json()
    assert first == {"questions": [QUESTION], "cached": False}  # malformed question dropped
    assert second == {"questions": [QUESTION], "cached": True}
    assert len(calls) == 1 and BAKER in calls[0][0] and calls[0][1] == 2


def test_quiz_unavailable_is_not_cached(monkeypatch, _tmp_stores):
    monkeypatch.setattr(ai_tutor, "generate_quiz_from_text", lambda *a, **k: [])
    out = client.post("/api/lesson-example/quiz", json={"example": BAKER}).json()
    assert out == {"questions": [], "cached": False, "unavailable": True}
    assert not list((_tmp_stores).glob("cache/quiz_*.json"))
    assert client.post("/api/lesson-example/quiz", json={"example": "too short"}).status_code == 422
