import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.ai_tutor import _parse_grammar_mistake_response
from app.main import app

client = TestClient(app)

FAKE_RESPONSE = """PASSAGE: Yesterday, me and my friend goes to the park. We seen a dog running fast.
MISTAKE: me and my friend goes => my friend and I went :: Subject pronoun and subject-verb agreement.
MISTAKE: We seen => We saw :: Use simple past tense, not the past participle, without an auxiliary verb.
"""


def test_parse_grammar_mistake_response_extracts_passage_and_mistakes():
    result = _parse_grammar_mistake_response(FAKE_RESPONSE)
    assert result["passage"] == (
        "Yesterday, me and my friend goes to the park. We seen a dog running fast."
    )
    assert len(result["mistakes"]) == 2
    assert result["mistakes"][0] == {
        "wrong": "me and my friend goes",
        "correct": "my friend and I went",
        "explanation": "Subject pronoun and subject-verb agreement.",
    }
    assert result["mistakes"][1]["wrong"] == "We seen"


def test_parse_grammar_mistake_response_handles_no_mistakes():
    result = _parse_grammar_mistake_response("PASSAGE: A perfectly correct sentence.")
    assert result["passage"] == "A perfectly correct sentence."
    assert result["mistakes"] == []


def test_parse_grammar_mistake_response_handles_garbage_input():
    result = _parse_grammar_mistake_response("not formatted at all")
    assert result["passage"] == ""
    assert result["mistakes"] == []


@pytest.fixture
def mock_ai_grammar(monkeypatch):
    monkeypatch.setattr(
        ai_tutor, "generate_grammar_mistake_exercise",
        lambda *a, **k: _parse_grammar_mistake_response(FAKE_RESPONSE),
    )


def test_mistake_hunt_endpoint_returns_passage_and_mistakes(mock_ai_grammar):
    resp = client.post("/api/grammar/mistake-hunt", json={
        "topic": "a trip to the park", "language": "English", "mistake_count": 2, "level": "5",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "park" in data["passage"]
    assert len(data["mistakes"]) == 2


def test_mistake_hunt_endpoint_defaults_when_body_is_empty(mock_ai_grammar):
    resp = client.post("/api/grammar/mistake-hunt", json={})
    assert resp.status_code == 200
    data = resp.json()
    assert "passage" in data
    assert "mistakes" in data


def test_mistake_hunt_caps_mistake_count(monkeypatch):
    captured = {}

    def fake_generate(topic, grade=1, level=None, language="English", mistake_count=8):
        captured["mistake_count"] = mistake_count
        return {"passage": "", "mistakes": []}

    monkeypatch.setattr(ai_tutor, "generate_grammar_mistake_exercise", fake_generate)
    resp = client.post("/api/grammar/mistake-hunt", json={"mistake_count": 999})
    assert resp.status_code == 200
    assert captured["mistake_count"] == 20
