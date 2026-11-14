import pytest
from fastapi.testclient import TestClient

from app import problem_reports
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def _tmp_store(monkeypatch, tmp_path):
    monkeypatch.setattr(problem_reports, "REPORTS_DIR", tmp_path)


def _post(**overrides):
    body = {"kind": "lesson", "item_id": "math-g5-l1", "title": "Percentages", "category": "typo", "message": "Typo in line 2"}
    body.update(overrides)
    return client.post("/api/reports", json=body)


def test_create_list_and_resolve_report():
    created = _post().json()
    assert created["status"] == "open" and created["id"]
    listing = client.get("/api/reports").json()
    assert listing["open_count"] == 1
    assert listing["reports"][0]["title"] == "Percentages"

    resolved = client.patch(f"/api/reports/{created['id']}", json={"status": "resolved"})
    assert resolved.status_code == 200
    assert client.get("/api/reports").json()["open_count"] == 0
    assert client.get("/api/reports", params={"status": "open"}).json()["reports"] == []


def test_rejects_unknown_kind_category_and_empty_other():
    assert _post(kind="nonsense").status_code == 422
    assert _post(category="nonsense").status_code == 422
    assert _post(category="other", message=" ").status_code == 422
    assert _post(item_id="").status_code == 422
    assert _post(message="x" * 2001).status_code == 422


def test_category_alone_is_enough_for_specific_problems():
    assert _post(kind="museum_object", item_id="wc_0076", category="wrong_or_missing_image", message="").status_code == 200


def test_unknown_report_id_is_404():
    assert client.patch("/api/reports/doesnotexist", json={"status": "resolved"}).status_code == 404
    created = _post().json()
    assert client.patch(f"/api/reports/{created['id']}", json={"status": "deleted"}).status_code == 422


def test_store_is_capped(monkeypatch):
    monkeypatch.setattr(problem_reports, "MAX_REPORTS", 3)
    ids = [_post(message=f"problem {i}").json()["id"] for i in range(5)]
    kept = [r["id"] for r in client.get("/api/reports").json()["reports"]]
    assert len(kept) == 3 and ids[-1] in kept and ids[0] not in kept
