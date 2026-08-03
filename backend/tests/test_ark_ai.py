import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app

client = TestClient(app)


def fake_chat(message, history=None, agent="teacher", level=None, grade=1, context=""):
    ctx = f" ctx={context!r}" if context else ""
    return f"[{agent}] reply to: {message} (history_len={len(history or [])}){ctx}"


def test_chat_requires_message():
    resp = client.post("/api/ark-ai/chat", json={"message": ""})
    assert resp.status_code == 400


def test_chat_requires_history_to_be_a_list():
    resp = client.post("/api/ark-ai/chat", json={"message": "hi", "history": "nope"})
    assert resp.status_code == 400


def test_chat_returns_reply(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={"message": "Hello!", "agent": "teacher"})
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[teacher] reply to: Hello! (history_len=0)"}


def test_chat_passes_history_and_instructor_agent(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={
        "message": "Explain photosynthesis",
        "agent": "instructor",
        "history": [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "hello"}],
        "level": "5",
    })
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[instructor] reply to: Explain photosynthesis (history_len=2)"}


def test_chat_helper_agent(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={"message": "hi", "agent": "helper"})
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[helper] reply to: hi (history_len=0)"}


def test_chat_falls_back_to_teacher_agent_for_unknown_agent(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={"message": "hi", "agent": "bogus"})
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[teacher] reply to: hi (history_len=0)"}


def test_chat_partner_agent_with_context(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={
        "message": "Hola",
        "agent": "partner",
        "context": "Learner practicing Spanish.",
    })
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[partner] reply to: Hola (history_len=0) ctx='Learner practicing Spanish.'"}


def test_chat_singing_partner_agent_with_context(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={
        "message": "here we go!",
        "agent": "singing_partner",
        "context": 'Song: "Amazing Grace"',
    })
    assert resp.status_code == 200
    assert resp.json() == {
        "reply": "[singing_partner] reply to: here we go! (history_len=0) ctx='Song: \"Amazing Grace\"'"
    }


def test_ark_ai_chat_folds_history_into_prompt(monkeypatch):
    captured = {}

    class FakeMessage:
        content = [type("C", (), {"text": "Sure, here's an answer."})()]

    class FakeMessages:
        def create(self, **kwargs):
            captured.update(kwargs)
            return FakeMessage()

    class FakeClient:
        messages = FakeMessages()

    monkeypatch.setattr(ai_tutor, "_get_client", lambda: FakeClient())

    reply = ai_tutor.ark_ai_chat(
        "What's next?",
        history=[{"role": "user", "content": "Tell me about Mars"}, {"role": "assistant", "content": "Mars is red."}],
        agent="instructor",
        level="5",
    )
    assert reply == "Sure, here's an answer."
    assert "Tell me about Mars" in captured["messages"][0]["content"]
    assert "Mars is red." in captured["messages"][0]["content"]
    assert "What's next?" in captured["messages"][0]["content"]
    assert "Instructor" in captured["system"]


def test_ark_ai_chat_uses_distinct_prompts_per_agent(monkeypatch):
    captured = {}

    class FakeMessage:
        content = [type("C", (), {"text": "ok"})()]

    class FakeMessages:
        def create(self, **kwargs):
            captured["system"] = kwargs["system"]
            return FakeMessage()

    class FakeClient:
        messages = FakeMessages()

    monkeypatch.setattr(ai_tutor, "_get_client", lambda: FakeClient())

    ai_tutor.ark_ai_chat("hi", agent="teacher")
    teacher_system = captured["system"]
    ai_tutor.ark_ai_chat("hi", agent="instructor")
    instructor_system = captured["system"]
    ai_tutor.ark_ai_chat("hi", agent="helper")
    helper_system = captured["system"]

    assert teacher_system != instructor_system != helper_system
    assert "Teacher" in teacher_system
    assert "Instructor" in instructor_system
    assert "Helper" in helper_system


def test_ark_ai_chat_folds_context_into_system_prompt(monkeypatch):
    captured = {}

    class FakeMessage:
        content = [type("C", (), {"text": "ok"})()]

    class FakeMessages:
        def create(self, **kwargs):
            captured["system"] = kwargs["system"]
            return FakeMessage()

    class FakeClient:
        messages = FakeMessages()

    monkeypatch.setattr(ai_tutor, "_get_client", lambda: FakeClient())

    ai_tutor.ark_ai_chat("Hola", agent="partner", context="Learner practicing Spanish.")
    assert "Conversation Partner" in captured["system"]
    assert "Learner practicing Spanish." in captured["system"]

    ai_tutor.ark_ai_chat("hi", agent="singing_partner", context='Song: "Amazing Grace"')
    assert "Singing Partner" in captured["system"]
    assert 'Song: "Amazing Grace"' in captured["system"]

    ai_tutor.ark_ai_chat("hi", agent="teacher")
    assert "Context for this conversation" not in captured["system"]
