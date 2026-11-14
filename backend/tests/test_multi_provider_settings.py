import pytest
from fastapi.testclient import TestClient

from app import ai_tutor, ark_ai_library, llm_providers, settings_store
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def isolated_settings(monkeypatch, tmp_path):
    monkeypatch.setattr(settings_store, "SETTINGS_PATH", tmp_path / "app_settings.json")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    yield


# ─── settings_store: generic multi-provider key storage ──────────────────────

def test_all_eleven_providers_listed():
    assert len(settings_store.PROVIDERS) == 11
    assert "anthropic" in settings_store.PROVIDERS
    assert "openai" in settings_store.PROVIDERS
    assert "openrouter" in settings_store.PROVIDERS


def test_set_get_clear_api_key_per_provider():
    assert settings_store.get_api_key("openai") == ""
    settings_store.set_api_key("openai", "sk-openai-key")
    assert settings_store.get_api_key("openai") == "sk-openai-key"
    # A different provider's key is unaffected.
    assert settings_store.get_api_key("gemini") == ""
    settings_store.clear_api_key("openai")
    assert settings_store.get_api_key("openai") == ""


def test_anthropic_wrappers_delegate_to_generic_store():
    settings_store.set_anthropic_api_key("sk-ant-abc")
    assert settings_store.get_api_key("anthropic") == "sk-ant-abc"
    assert settings_store.get_anthropic_api_key() == "sk-ant-abc"


def test_preferred_model_round_trip():
    assert settings_store.get_preferred_model() == ""
    settings_store.set_preferred_model("openai:gpt-5.1")
    assert settings_store.get_preferred_model() == "openai:gpt-5.1"
    settings_store.clear_preferred_model()
    assert settings_store.get_preferred_model() == ""


# ─── ark_ai_library: model lookup + provider slug mapping ────────────────────

def test_get_model_returns_known_model():
    model = ark_ai_library.get_model("openai:gpt-5.1")
    assert model is not None
    assert model["provider"] == "Openai"
    assert model["raw"] == "gpt-5.1"


def test_get_model_returns_none_for_unknown_id():
    assert ark_ai_library.get_model("not-a-real-model-id") is None


def test_provider_slugs_cover_every_provider_in_models_json():
    providers_in_data = {m["provider"] for m in ark_ai_library.list_models()}
    assert providers_in_data <= set(ark_ai_library.PROVIDER_SLUGS)


# ─── /api/settings/api-keys endpoints ─────────────────────────────────────────

def test_list_api_key_status_reports_all_providers_unconfigured():
    resp = client.get("/api/settings/api-keys")
    assert resp.status_code == 200
    providers = {p["provider"]: p for p in resp.json()["providers"]}
    assert set(providers) == set(settings_store.PROVIDERS)
    assert all(p["configured"] is False for p in providers.values())


def test_set_provider_key_endpoint():
    resp = client.post("/api/settings/api-keys/openai", json={"api_key": "sk-openai-abcdefgh"})
    assert resp.status_code == 200
    body = resp.json()
    assert body == {"provider": "openai", "label": "OpenAI", "configured": True, "source": "settings", "masked": "sk-ope...efgh"}
    assert "sk-openai-abcdefgh" not in resp.text


def test_set_provider_key_rejects_unknown_provider():
    resp = client.post("/api/settings/api-keys/not-a-provider", json={"api_key": "x"})
    assert resp.status_code == 404


def test_set_provider_key_rejects_empty_key():
    resp = client.post("/api/settings/api-keys/openai", json={"api_key": ""})
    assert resp.status_code == 400


def test_delete_provider_key_endpoint():
    client.post("/api/settings/api-keys/groq", json={"api_key": "gsk-abc"})
    resp = client.delete("/api/settings/api-keys/groq")
    assert resp.status_code == 200
    assert resp.json()["configured"] is False


# ─── /api/settings/preferred-model endpoints ──────────────────────────────────

def test_set_preferred_model_requires_key_for_non_claude_provider():
    resp = client.post("/api/settings/preferred-model", json={"model_id": "openai:gpt-5.1"})
    assert resp.status_code == 400
    assert "OpenAI" in resp.json()["detail"]


def test_set_preferred_model_succeeds_once_key_is_present():
    client.post("/api/settings/api-keys/openai", json={"api_key": "sk-openai-abcdefgh"})
    resp = client.post("/api/settings/preferred-model", json={"model_id": "openai:gpt-5.1"})
    assert resp.status_code == 200
    assert resp.json()["model_id"] == "openai:gpt-5.1"

    status = client.get("/api/settings/preferred-model")
    assert status.json()["model_id"] == "openai:gpt-5.1"
    assert status.json()["model"]["raw"] == "gpt-5.1"


def test_set_preferred_model_rejects_unknown_model_id():
    resp = client.post("/api/settings/preferred-model", json={"model_id": "not-a-real-model"})
    assert resp.status_code == 404


def test_set_preferred_model_with_blank_id_clears_it():
    client.post("/api/settings/api-keys/openai", json={"api_key": "sk-openai-abcdefgh"})
    client.post("/api/settings/preferred-model", json={"model_id": "openai:gpt-5.1"})
    resp = client.post("/api/settings/preferred-model", json={"model_id": ""})
    assert resp.status_code == 200
    assert resp.json()["model_id"] == ""
    assert settings_store.get_preferred_model() == ""


# ─── ai_tutor._call routing + fallback behaviour ──────────────────────────────

def test_call_uses_claude_default_when_no_preferred_model_set():
    # No preferred model, no anthropic key either -- offline fallback text,
    # confirming behaviour is completely unchanged from before this feature.
    result = ai_tutor._call("system", "hello")
    assert result.startswith("Ark AI is offline")


def test_call_routes_to_preferred_model_when_configured(monkeypatch):
    settings_store.set_api_key("openai", "sk-openai-abcdefgh")
    settings_store.set_preferred_model("openai:gpt-5.1")

    captured = {}

    def fake_call_chat(provider, model, api_key, system, user, max_tokens=512):
        captured.update(provider=provider, model=model, api_key=api_key)
        return "Hello from the alternate model!"

    monkeypatch.setattr(llm_providers, "call_chat", fake_call_chat)
    result = ai_tutor._call("system prompt", "hello", strict=False)

    assert result == "Hello from the alternate model!"
    assert captured == {"provider": "openai", "model": "gpt-5.1", "api_key": "sk-openai-abcdefgh"}


def test_call_falls_back_to_claude_when_preferred_model_call_fails(monkeypatch):
    settings_store.set_api_key("openai", "sk-openai-abcdefgh")
    settings_store.set_preferred_model("openai:gpt-5.1")

    def failing_call_chat(*args, **kwargs):
        raise llm_providers.ProviderCallError("boom")

    monkeypatch.setattr(llm_providers, "call_chat", failing_call_chat)
    # No anthropic key configured either, so it falls through all the way to
    # the offline message rather than raising.
    result = ai_tutor._call("system", "hello")
    assert result.startswith("Ark AI is offline")


def test_call_ignores_preferred_model_pointing_at_claude(monkeypatch):
    # If a Claude model were ever set as "preferred", it should just use the
    # normal default Claude path rather than routing through llm_providers.
    settings_store.set_preferred_model("claude:claude-opus-4-8")

    called = []
    monkeypatch.setattr(llm_providers, "call_chat", lambda *a, **k: called.append(1))
    result = ai_tutor._call("system", "hello")

    assert called == []
    assert result.startswith("Ark AI is offline")
