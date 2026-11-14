import json
from urllib.error import HTTPError, URLError

import pytest

from app import llm_providers


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def test_call_chat_openai_compatible_success(monkeypatch):
    captured = {}

    def fake_urlopen(req, timeout=None):
        captured["url"] = req.full_url
        captured["headers"] = dict(req.header_items())
        captured["body"] = json.loads(req.data.decode("utf-8"))
        return FakeResponse({"choices": [{"message": {"content": "Hello from OpenAI!"}}]})

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    result = llm_providers.call_chat("openai", "gpt-5.1", "sk-test", "system prompt", "user question", max_tokens=200)

    assert result == "Hello from OpenAI!"
    assert captured["url"] == "https://api.openai.com/v1/chat/completions"
    assert captured["headers"]["Authorization"] == "Bearer sk-test"
    assert captured["body"]["model"] == "gpt-5.1"
    assert captured["body"]["max_tokens"] == 200
    assert captured["body"]["messages"] == [
        {"role": "system", "content": "system prompt"},
        {"role": "user", "content": "user question"},
    ]


@pytest.mark.parametrize("provider,url", [
    ("mistral", "https://api.mistral.ai/v1/chat/completions"),
    ("grok", "https://api.x.ai/v1/chat/completions"),
    ("groq", "https://api.groq.com/openai/v1/chat/completions"),
    ("together", "https://api.together.xyz/v1/chat/completions"),
    ("perplexity", "https://api.perplexity.ai/chat/completions"),
    ("fireworks", "https://api.fireworks.ai/inference/v1/chat/completions"),
    ("deepseek", "https://api.deepseek.com/v1/chat/completions"),
    ("openrouter", "https://openrouter.ai/api/v1/chat/completions"),
])
def test_call_chat_every_openai_compatible_provider_hits_its_own_url(monkeypatch, provider, url):
    captured = {}

    def fake_urlopen(req, timeout=None):
        captured["url"] = req.full_url
        return FakeResponse({"choices": [{"message": {"content": "ok"}}]})

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    result = llm_providers.call_chat(provider, "some-model", "key", "sys", "user")
    assert result == "ok"
    assert captured["url"] == url


def test_call_chat_gemini_success(monkeypatch):
    captured = {}

    def fake_urlopen(req, timeout=None):
        captured["url"] = req.full_url
        captured["body"] = json.loads(req.data.decode("utf-8"))
        return FakeResponse({"candidates": [{"content": {"parts": [{"text": "Hello from Gemini!"}]}}]})

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    result = llm_providers.call_chat("gemini", "gemini-2.5-pro", "gk-test", "system prompt", "user question")

    assert result == "Hello from Gemini!"
    assert "gemini-2.5-pro:generateContent" in captured["url"]
    assert "key=gk-test" in captured["url"]
    assert captured["body"]["system_instruction"]["parts"][0]["text"] == "system prompt"
    assert captured["body"]["contents"][0]["parts"][0]["text"] == "user question"


def test_call_chat_unknown_provider_raises():
    with pytest.raises(llm_providers.ProviderCallError):
        llm_providers.call_chat("not-a-real-provider", "model", "key", "sys", "user")


def test_call_chat_raises_on_http_error(monkeypatch):
    def fake_urlopen(req, timeout=None):
        raise HTTPError(req.full_url, 401, "Unauthorized", hdrs=None, fp=None)

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    with pytest.raises(llm_providers.ProviderCallError):
        llm_providers.call_chat("openai", "gpt-5.1", "bad-key", "sys", "user")


def test_call_chat_raises_on_network_error(monkeypatch):
    def fake_urlopen(req, timeout=None):
        raise URLError("no route to host")

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    with pytest.raises(llm_providers.ProviderCallError):
        llm_providers.call_chat("groq", "llama-3.3-70b-versatile", "key", "sys", "user")


def test_call_chat_raises_on_unexpected_response_shape(monkeypatch):
    def fake_urlopen(req, timeout=None):
        return FakeResponse({"unexpected": "shape"})

    monkeypatch.setattr(llm_providers, "urlopen", fake_urlopen)
    with pytest.raises(llm_providers.ProviderCallError):
        llm_providers.call_chat("openai", "gpt-5.1", "key", "sys", "user")
