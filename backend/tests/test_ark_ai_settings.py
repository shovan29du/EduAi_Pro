import pytest
from fastapi.testclient import TestClient

from app import ai_tutor, settings_store
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def isolated_settings(monkeypatch, tmp_path):
    monkeypatch.setattr(settings_store, "SETTINGS_PATH", tmp_path / "app_settings.json")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    yield


def test_mask_key_short_and_long():
    assert settings_store.mask_key("short") == "*****"
    assert settings_store.mask_key("sk-ant-abcdefghijklmnop") == "sk-ant...mnop"


def test_set_get_clear_round_trip():
    assert settings_store.get_anthropic_api_key() == ""
    settings_store.set_anthropic_api_key("sk-ant-my-real-key-12345")
    assert settings_store.get_anthropic_api_key() == "sk-ant-my-real-key-12345"
    settings_store.clear_anthropic_api_key()
    assert settings_store.get_anthropic_api_key() == ""


def test_set_anthropic_api_key_rejects_blank():
    with pytest.raises(ValueError):
        settings_store.set_anthropic_api_key("   ")


def test_get_status_endpoint_reports_none_when_unconfigured():
    resp = client.get("/api/settings/anthropic-key")
    assert resp.status_code == 200
    assert resp.json() == {"configured": False, "source": "none", "masked": ""}


def test_post_and_get_status_endpoint_reports_settings_source():
    resp = client.post("/api/settings/anthropic-key", json={"api_key": "sk-ant-abcdefghijklmnop"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["configured"] is True
    assert body["source"] == "settings"
    assert body["masked"] == "sk-ant...mnop"
    assert "sk-ant-abcdefghijklmnop" not in resp.text

    status = client.get("/api/settings/anthropic-key")
    assert status.json()["source"] == "settings"


def test_post_rejects_empty_key():
    resp = client.post("/api/settings/anthropic-key", json={"api_key": ""})
    assert resp.status_code == 400


def test_delete_clears_saved_key_and_falls_back_to_env(monkeypatch):
    client.post("/api/settings/anthropic-key", json={"api_key": "sk-ant-abcdefghijklmnop"})
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-env-fallback-key-999")

    resp = client.delete("/api/settings/anthropic-key")
    assert resp.status_code == 200
    body = resp.json()
    assert body["configured"] is True
    assert body["source"] == "env"


def test_ai_tutor_prefers_settings_store_key_over_env(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-env-should-be-overridden")
    settings_store.set_anthropic_api_key("sk-ant-from-settings-ui")

    captured = {}

    class FakeAnthropic:
        def __init__(self, api_key):
            captured["api_key"] = api_key

    import sys
    import types
    fake_module = types.ModuleType("anthropic")
    fake_module.Anthropic = FakeAnthropic
    monkeypatch.setitem(sys.modules, "anthropic", fake_module)

    client_obj = ai_tutor._get_client()
    assert client_obj is not None
    assert captured["api_key"] == "sk-ant-from-settings-ui"


def test_ai_tutor_falls_back_to_env_when_no_settings_key(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-env-only-key")

    captured = {}

    class FakeAnthropic:
        def __init__(self, api_key):
            captured["api_key"] = api_key

    import sys
    import types
    fake_module = types.ModuleType("anthropic")
    fake_module.Anthropic = FakeAnthropic
    monkeypatch.setitem(sys.modules, "anthropic", fake_module)

    client_obj = ai_tutor._get_client()
    assert client_obj is not None
    assert captured["api_key"] == "sk-env-only-key"


def test_ai_tutor_returns_none_when_no_key_anywhere():
    assert ai_tutor._get_client() is None
