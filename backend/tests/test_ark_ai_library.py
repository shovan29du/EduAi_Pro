from fastapi.testclient import TestClient

from app import ark_ai_library
from app.main import app

client = TestClient(app)


def test_library_loaded_with_expected_scale():
    # Sanity check that the full library made it into the app, not a stub.
    assert len(ark_ai_library.list_prompts(limit=10_000)) > 300
    assert len(ark_ai_library.list_models()) > 40
    assert len(ark_ai_library.list_tools(limit=10_000)) > 40


def test_prompts_endpoint_returns_prompts_and_tags():
    resp = client.get("/api/ark-ai/prompts")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["prompts"]) == 50  # default limit
    assert "tags" in data and len(data["tags"]) > 5
    for p in data["prompts"]:
        assert set(p.keys()) == {"id", "name", "tag", "prompt"}


def test_prompts_endpoint_filters_by_query():
    resp = client.get("/api/ark-ai/prompts", params={"q": "research"})
    assert resp.status_code == 200
    prompts = resp.json()["prompts"]
    assert len(prompts) > 0
    for p in prompts:
        assert "research" in p["name"].lower() or "research" in p["prompt"].lower()


def test_prompts_endpoint_filters_by_tag():
    resp = client.get("/api/ark-ai/prompts", params={"tag": "code"})
    assert resp.status_code == 200
    prompts = resp.json()["prompts"]
    assert len(prompts) > 0
    assert all(p["tag"] == "code" for p in prompts)


def test_prompt_detail_endpoint():
    listing = client.get("/api/ark-ai/prompts").json()["prompts"]
    prompt_id = listing[0]["id"]
    resp = client.get(f"/api/ark-ai/prompts/{prompt_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == prompt_id


def test_prompt_detail_404_for_unknown_id():
    resp = client.get("/api/ark-ai/prompts/not-a-real-id")
    assert resp.status_code == 404


def test_models_endpoint():
    resp = client.get("/api/ark-ai/models")
    assert resp.status_code == 200
    models = resp.json()["models"]
    assert len(models) > 40
    providers = {m["provider"] for m in models}
    assert "Claude" in providers
    for m in models:
        assert set(m.keys()) == {"id", "name", "provider", "raw"}


def test_tools_endpoint_with_kind_filter():
    resp = client.get("/api/ark-ai/tools", params={"kind": "plugin"})
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["tools"]) > 0
    assert all(t["kind"] == "plugin" for t in data["tools"])
    assert "categories" in data and "kinds" in data


def test_tools_endpoint_filters_by_query_and_category():
    resp = client.get("/api/ark-ai/tools", params={"q": "code", "category": "Coding"})
    assert resp.status_code == 200
    tools = resp.json()["tools"]
    assert len(tools) > 0
    for t in tools:
        assert t["category"] == "Coding"
        assert "code" in t["name"].lower() or "code" in t["note"].lower()
