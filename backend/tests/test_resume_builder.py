import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app

client = TestClient(app)


def fake_generate_resume_content(profile):
    return {
        "summary": f"Resume summary for {profile['name'] or 'candidate'}.",
        "skills": profile["skills"],
        "experience": [f"Achieved: {item}" for item in profile["experience"]],
    }


def test_parse_resume_content_reads_structured_response():
    raw = (
        "SUMMARY: Results-driven analyst with a track record of shipping dashboards.\n"
        "SKILLS: Python, SQL, Data Visualization\n"
        "EXPERIENCE:\n"
        "- Built a sales dashboard that cut reporting time by 40%\n"
        "- Automated a nightly data pipeline\n"
    )
    result = ai_tutor._parse_resume_content(raw, fallback_skills=["x"], fallback_experience=["y"])
    assert result["summary"] == "Results-driven analyst with a track record of shipping dashboards."
    assert result["skills"] == ["Python", "SQL", "Data Visualization"]
    assert result["experience"] == [
        "Built a sales dashboard that cut reporting time by 40%",
        "Automated a nightly data pipeline",
    ]


def test_parse_resume_content_falls_back_on_unstructured_response():
    raw = "EduBot is offline. Please ask your teacher, tutor, or a trusted adult for help with this question."
    result = ai_tutor._parse_resume_content(raw, fallback_skills=["Python"], fallback_experience=["Did a thing"])
    assert result["summary"] == raw
    assert result["skills"] == ["Python"]
    assert result["experience"] == ["Did a thing"]


def test_draft_resume_requires_skills_or_experience():
    resp = client.post("/api/pro/resume/draft", json={"skills": [], "experience": []})
    assert resp.status_code == 400


def test_draft_resume_returns_generated_content(monkeypatch):
    monkeypatch.setattr(ai_tutor, "generate_resume_content", fake_generate_resume_content)
    resp = client.post("/api/pro/resume/draft", json={
        "name": "Shovan",
        "target_role": "Data Analyst",
        "skills": ["Python", "SQL"],
        "experience": ["Built a sales dashboard"],
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["summary"] == "Resume summary for Shovan."
    assert data["skills"] == ["Python", "SQL"]
    assert data["experience"] == ["Achieved: Built a sales dashboard"]


def test_export_resume_requires_content():
    resp = client.post("/api/pro/resume/export", json={"format": "pdf"})
    assert resp.status_code == 400


def test_export_resume_rejects_unknown_format():
    resp = client.post("/api/pro/resume/export", json={"summary": "x", "format": "bogus"})
    assert resp.status_code == 422


def test_export_resume_as_pdf():
    resp = client.post("/api/pro/resume/export", json={
        "name": "Shovan Test",
        "target_role": "Data Analyst",
        "contact": "shovan@example.com",
        "education": "BSc Computer Science",
        "summary": "Experienced analyst.",
        "skills": ["Python", "SQL"],
        "experience": ["Delivered a dashboard"],
        "format": "pdf",
    })
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "application/pdf"
    assert resp.content.startswith(b"%PDF")
    assert 'filename="shovan-test.pdf"' in resp.headers["content-disposition"]


def test_export_resume_as_docx():
    resp = client.post("/api/pro/resume/export", json={
        "name": "Shovan Test",
        "summary": "Experienced analyst.",
        "format": "docx",
    })
    assert resp.status_code == 200
    assert resp.headers["content-type"] == (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    assert len(resp.content) > 0


def test_export_resume_sanitizes_filename():
    resp = client.post("/api/pro/resume/export", json={
        "name": "  Weird / Name!! ",
        "summary": "x",
        "format": "pdf",
    })
    assert resp.status_code == 200
    assert 'filename="weird-name.pdf"' in resp.headers["content-disposition"]
