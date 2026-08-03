import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app

client = TestClient(app)


def fake_chat(message, history=None, mode="chat", level=None, grade=1):
    return f"[{mode}] reply to: {message} (history_len={len(history or [])})"


def test_chat_requires_message():
    resp = client.post("/api/ark-ai/chat", json={"message": ""})
    assert resp.status_code == 400


def test_chat_requires_history_to_be_a_list():
    resp = client.post("/api/ark-ai/chat", json={"message": "hi", "history": "nope"})
    assert resp.status_code == 400


def test_chat_returns_reply(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={"message": "Hello!", "mode": "chat"})
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[chat] reply to: Hello! (history_len=0)"}


def test_chat_passes_history_and_learn_mode(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={
        "message": "Explain photosynthesis",
        "mode": "learn",
        "history": [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "hello"}],
        "level": "5",
    })
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[learn] reply to: Explain photosynthesis (history_len=2)"}


def test_chat_falls_back_to_chat_mode_for_unknown_mode(monkeypatch):
    monkeypatch.setattr(ai_tutor, "ark_ai_chat", fake_chat)
    resp = client.post("/api/ark-ai/chat", json={"message": "hi", "mode": "bogus"})
    assert resp.status_code == 200
    assert resp.json() == {"reply": "[chat] reply to: hi (history_len=0)"}


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
        mode="learn",
        level="5",
    )
    assert reply == "Sure, here's an answer."
    assert "Tell me about Mars" in captured["messages"][0]["content"]
    assert "Mars is red." in captured["messages"][0]["content"]
    assert "What's next?" in captured["messages"][0]["content"]
    assert "Learn" in captured["system"]
