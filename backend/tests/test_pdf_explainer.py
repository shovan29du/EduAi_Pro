import io

import pytest
from fastapi.testclient import TestClient
from reportlab.pdfgen import canvas

from app.main import app

client = TestClient(app)


def _make_pdf_bytes(lines):
    buf = io.BytesIO()
    c = canvas.Canvas(buf)
    y = 750
    for line in lines:
        c.drawString(100, y, line)
        y -= 20
    c.save()
    return buf.getvalue()


@pytest.fixture
def uploaded_doc():
    pdf_bytes = _make_pdf_bytes([
        "The mitochondria is the powerhouse of the cell.",
        "Photosynthesis converts sunlight into chemical energy.",
    ])
    resp = client.post(
        "/api/pdf-explainer/upload",
        files={"file": ("bio.pdf", pdf_bytes, "application/pdf")},
        data={"child": "TestChild"},
    )
    assert resp.status_code == 200
    doc = resp.json()
    yield doc
    client.delete(f"/api/pdf-explainer/{doc['id']}")


def test_upload_rejects_non_pdf_extension():
    resp = client.post(
        "/api/pdf-explainer/upload",
        files={"file": ("notes.txt", b"hello world", "text/plain")},
    )
    assert resp.status_code == 400
    assert "PDF" in resp.json()["detail"]


def test_upload_rejects_bad_pdf_signature():
    resp = client.post(
        "/api/pdf-explainer/upload",
        files={"file": ("fake.pdf", b"this is not really a pdf", "application/pdf")},
    )
    assert resp.status_code == 400
    assert "valid PDF" in resp.json()["detail"]


def test_upload_rejects_oversize_pdf():
    from app import pdf_explainer

    original_max = pdf_explainer.MAX_PDF_BYTES
    pdf_explainer.MAX_PDF_BYTES = 10
    try:
        pdf_bytes = _make_pdf_bytes(["Some content that exceeds the tiny test limit."])
        resp = client.post(
            "/api/pdf-explainer/upload",
            files={"file": ("big.pdf", pdf_bytes, "application/pdf")},
        )
        assert resp.status_code == 400
        assert "too large" in resp.json()["detail"]
    finally:
        pdf_explainer.MAX_PDF_BYTES = original_max


def test_upload_and_list_and_get(uploaded_doc):
    doc_id = uploaded_doc["id"]
    assert uploaded_doc["filename"] == "bio.pdf"
    assert uploaded_doc["page_count"] == 1
    assert "text" not in uploaded_doc

    listed = client.get("/api/pdf-explainer", params={"child": "TestChild"}).json()
    assert any(d["id"] == doc_id for d in listed)

    got = client.get(f"/api/pdf-explainer/{doc_id}")
    assert got.status_code == 200
    assert got.json()["id"] == doc_id


def test_get_unknown_document_404():
    resp = client.get("/api/pdf-explainer/not-a-real-id")
    assert resp.status_code == 404


def test_delete_unknown_document_404():
    resp = client.delete("/api/pdf-explainer/not-a-real-id")
    assert resp.status_code == 404


def test_explain_document_returns_text(uploaded_doc):
    resp = client.post(f"/api/pdf-explainer/{uploaded_doc['id']}/explain", json={"level": "C1"})
    assert resp.status_code == 200
    assert isinstance(resp.json()["explanation"], str)
    assert resp.json()["explanation"]


def test_explain_unknown_document_404():
    resp = client.post("/api/pdf-explainer/not-a-real-id/explain", json={"level": "C1"})
    assert resp.status_code == 404


def test_ask_requires_question(uploaded_doc):
    resp = client.post(f"/api/pdf-explainer/{uploaded_doc['id']}/ask", json={"level": "C1", "question": ""})
    assert resp.status_code == 400


def test_ask_returns_answer(uploaded_doc):
    resp = client.post(
        f"/api/pdf-explainer/{uploaded_doc['id']}/ask",
        json={"level": "C1", "question": "What is mitochondria?"},
    )
    assert resp.status_code == 200
    assert isinstance(resp.json()["answer"], str)
    assert resp.json()["answer"]


def test_quiz_returns_list(uploaded_doc):
    resp = client.post(f"/api/pdf-explainer/{uploaded_doc['id']}/quiz", json={"level": "C1", "count": 3})
    assert resp.status_code == 200
    assert isinstance(resp.json()["quiz"], list)


def test_notes_add_list_delete(uploaded_doc):
    doc_id = uploaded_doc["id"]

    add_resp = client.post(f"/api/pdf-explainer/{doc_id}/notes", json={"text": "remember this", "child": "TestChild"})
    assert add_resp.status_code == 200
    note = add_resp.json()
    assert note["text"] == "remember this"

    list_resp = client.get(f"/api/pdf-explainer/{doc_id}/notes", params={"child": "TestChild"})
    assert list_resp.status_code == 200
    assert any(n["id"] == note["id"] for n in list_resp.json())

    del_resp = client.delete(f"/api/pdf-explainer/notes/{note['id']}")
    assert del_resp.status_code == 200

    list_resp2 = client.get(f"/api/pdf-explainer/{doc_id}/notes", params={"child": "TestChild"})
    assert not any(n["id"] == note["id"] for n in list_resp2.json())


def test_notes_add_requires_text(uploaded_doc):
    resp = client.post(f"/api/pdf-explainer/{uploaded_doc['id']}/notes", json={"text": "", "child": "TestChild"})
    assert resp.status_code == 400


def test_notes_add_unknown_document_404():
    resp = client.post("/api/pdf-explainer/not-a-real-id/notes", json={"text": "hi"})
    assert resp.status_code == 404


def test_delete_unknown_note_404():
    resp = client.delete("/api/pdf-explainer/notes/not-a-real-id")
    assert resp.status_code == 404


def test_delete_document_removes_it_and_its_notes(uploaded_doc):
    doc_id = uploaded_doc["id"]
    client.post(f"/api/pdf-explainer/{doc_id}/notes", json={"text": "note before delete"})

    del_resp = client.delete(f"/api/pdf-explainer/{doc_id}")
    assert del_resp.status_code == 200

    assert client.get(f"/api/pdf-explainer/{doc_id}").status_code == 404
    assert client.get(f"/api/pdf-explainer/{doc_id}/notes").status_code == 404
