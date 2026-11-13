from fastapi.testclient import TestClient

from app import ai_tutor, lesson_examples
from app.main import app

client = TestClient(app)


def test_example_is_generated_once_then_served_from_cache(monkeypatch, tmp_path):
    monkeypatch.setattr(lesson_examples, "CACHE_DIR", tmp_path)
    calls = []

    def fake(title, subject, grade=1, level=None, key_concepts=None, summary=""):
        calls.append((title, subject, tuple(key_concepts or [])))
        return "A baker doubles a recipe, which is multiplying fractions."

    monkeypatch.setattr(ai_tutor, "generate_real_world_example", fake)
    params = {"title": "Multiplying Fractions", "subject": "Math", "lesson_id": "math-g5-l9", "concepts": "fraction, product"}
    first = client.get("/api/lesson-example", params=params).json()
    second = client.get("/api/lesson-example", params=params).json()
    assert first == {"example": "A baker doubles a recipe, which is multiplying fractions.", "cached": False}
    assert second["cached"] is True and second["example"] == first["example"]
    assert calls == [("Multiplying Fractions", "Math", ("fraction", "product"))]


def test_unavailable_ai_is_reported_and_not_cached(monkeypatch, tmp_path):
    monkeypatch.setattr(lesson_examples, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(ai_tutor, "generate_real_world_example", lambda *a, **k: None)
    body = client.get("/api/lesson-example", params={"title": "The Solar System", "subject": "Science"}).json()
    assert body["example"] is None and body["unavailable"] is True
    assert list(tmp_path.glob("*.json")) == []


def test_title_is_required():
    assert client.get("/api/lesson-example", params={"title": " "}).status_code == 400


def test_generate_real_world_example_ignores_offline_message(monkeypatch):
    monkeypatch.setattr(ai_tutor, "_call", lambda *a, **k: "Ark AI is offline. Please ask your teacher.")
    assert ai_tutor.generate_real_world_example("Fractions", "Math", grade=5) is None
    monkeypatch.setattr(ai_tutor, "_call", lambda *a, **k: "Sharing a pizza into 8 slices shows fractions.")
    assert "pizza" in ai_tutor.generate_real_world_example("Fractions", "Math", grade=5)
