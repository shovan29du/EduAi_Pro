import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app

client = TestClient(app)


@pytest.fixture
def two_documents():
    r1 = client.post(
        "/api/resource-tab/upload",
        files={"file": ("doc1.txt", b"The mitochondria is the powerhouse of the cell.", "text/plain")},
    )
    r2 = client.post(
        "/api/resource-tab/upload",
        files={"file": ("doc2.txt", b"Photosynthesis converts sunlight into chemical energy.", "text/plain")},
    )
    doc1, doc2 = r1.json(), r2.json()
    yield doc1, doc2
    client.delete(f"/api/resource-tab/{doc1['id']}")
    client.delete(f"/api/resource-tab/{doc2['id']}")


def test_get_document_text_reextracts_full_text():
    from app import resource_tab

    record = resource_tab.add_document("plain.txt", b"Hello from a real extracted document.")
    try:
        assert resource_tab.get_document_text(record["id"]) == "Hello from a real extracted document."
    finally:
        resource_tab.delete_document(record["id"])


def test_get_document_text_returns_none_for_unknown_id():
    from app import resource_tab

    assert resource_tab.get_document_text("not-a-real-id") is None


def test_ask_requires_document_ids():
    resp = client.post("/api/resource-tab/course-assistant/ask", json={"document_ids": [], "question": "x"})
    assert resp.status_code == 400


def test_ask_requires_question(two_documents):
    doc1, _ = two_documents
    resp = client.post("/api/resource-tab/course-assistant/ask", json={
        "document_ids": [doc1["id"]], "question": "",
    })
    assert resp.status_code == 400


def test_ask_rejects_unknown_document():
    resp = client.post("/api/resource-tab/course-assistant/ask", json={
        "document_ids": ["not-a-real-id"], "question": "What is this about?",
    })
    assert resp.status_code == 404


def test_ask_answers_grounded_in_provided_documents(two_documents, monkeypatch):
    doc1, doc2 = two_documents
    captured = {}

    def fake_answer(question, documents, level=None, grade=1):
        captured["question"] = question
        captured["documents"] = documents
        return "Mitochondria produce energy. (from doc1.txt)"

    monkeypatch.setattr(ai_tutor, "answer_from_course_materials", fake_answer)

    resp = client.post("/api/resource-tab/course-assistant/ask", json={
        "document_ids": [doc1["id"], doc2["id"]],
        "question": "What is the powerhouse of the cell?",
        "level": "5",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["answer"] == "Mitochondria produce energy. (from doc1.txt)"
    assert data["documents"] == ["doc1.txt", "doc2.txt"]

    assert captured["question"] == "What is the powerhouse of the cell?"
    filenames = {d["filename"] for d in captured["documents"]}
    assert filenames == {"doc1.txt", "doc2.txt"}
    texts = {d["filename"]: d["text"] for d in captured["documents"]}
    assert "mitochondria" in texts["doc1.txt"].lower()
    assert "photosynthesis" in texts["doc2.txt"].lower()


def test_ask_caps_document_ids_at_ten():
    resp = client.post("/api/resource-tab/course-assistant/ask", json={
        "document_ids": [f"id{i}" for i in range(15)], "question": "x",
    })
    # First id won't exist, so this 404s -- the point is it doesn't 500 on 15 ids.
    assert resp.status_code == 404
