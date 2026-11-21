from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# A minimal valid 1x1 transparent PNG, base64-encoded.
TINY_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
    "+A8AAQUBAScY42YAAAAASUVORK5CYII="
)
TINY_PNG_DATA_URL = f"data:image/png;base64,{TINY_PNG_B64}"


def test_paintings_save_list_download_and_delete():
    # Fresh gallery is empty
    resp = client.get("/api/paintings/TestChildOne")
    assert resp.status_code == 200
    before_ids = {p["id"] for p in resp.json()["paintings"]}

    saved = client.post(
        "/api/paintings/TestChildOne",
        json={"title": "Sunset", "image": TINY_PNG_DATA_URL},
    )
    assert saved.status_code == 200
    record = saved.json()
    assert record["title"] == "Sunset"
    assert "id" in record

    listed = client.get("/api/paintings/TestChildOne")
    assert listed.status_code == 200
    ids = {p["id"] for p in listed.json()["paintings"]}
    assert record["id"] in ids
    assert ids - before_ids  # something new was added

    image = client.get(f"/api/paintings/TestChildOne/{record['id']}/image")
    assert image.status_code == 200
    assert image.headers["content-type"] == "image/png"
    assert len(image.content) > 0

    deleted = client.delete(f"/api/paintings/TestChildOne/{record['id']}")
    assert deleted.status_code == 200

    missing = client.get(f"/api/paintings/TestChildOne/{record['id']}/image")
    assert missing.status_code == 404


def test_paintings_update_existing_by_id_reuses_the_same_record():
    saved = client.post(
        "/api/paintings/TestChildOne",
        json={"title": "Draft", "image": TINY_PNG_DATA_URL},
    )
    record = saved.json()

    updated = client.post(
        "/api/paintings/TestChildOne",
        json={"id": record["id"], "title": "Finished piece", "image": TINY_PNG_DATA_URL},
    )
    assert updated.status_code == 200
    updated_record = updated.json()
    assert updated_record["id"] == record["id"]
    assert updated_record["title"] == "Finished piece"

    listed = client.get("/api/paintings/TestChildOne").json()["paintings"]
    matching = [p for p in listed if p["id"] == record["id"]]
    assert len(matching) == 1  # not duplicated

    client.delete(f"/api/paintings/TestChildOne/{record['id']}")


def test_paintings_rejects_invalid_image_data():
    resp = client.post(
        "/api/paintings/TestChildOne",
        json={"title": "Bad", "image": "not-a-real-image"},
    )
    assert resp.status_code == 400


def test_paintings_unknown_child_rejected():
    resp = client.get("/api/paintings/Unknown")
    assert resp.status_code == 404

    resp = client.post(
        "/api/paintings/Unknown",
        json={"title": "X", "image": TINY_PNG_DATA_URL},
    )
    assert resp.status_code == 404


def test_paintings_delete_missing_returns_404():
    resp = client.delete("/api/paintings/TestChildOne/does-not-exist")
    assert resp.status_code == 404
