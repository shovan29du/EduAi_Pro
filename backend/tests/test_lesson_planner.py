import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app
from app.lesson_planner import _schedule_dates
from datetime import date

client = TestClient(app)

FAKE_LESSONS = [
    {"title": "Introduction", "objectives": ["Define key terms", "Set expectations"], "content": "Overview of the topic."},
    {"title": "Core concepts", "objectives": ["Explain the core idea"], "content": "Deep dive into fundamentals."},
    {"title": "Applications", "objectives": ["Apply concepts to examples"], "content": "Worked examples."},
    {"title": "Review", "objectives": ["Consolidate learning"], "content": "Recap and practice questions."},
]


@pytest.fixture
def mock_ai_lesson_plan(monkeypatch):
    monkeypatch.setattr(ai_tutor, "generate_lesson_plan", lambda *a, **k: FAKE_LESSONS)


@pytest.fixture
def generated_plan(mock_ai_lesson_plan):
    resp = client.post("/api/lesson-planner/generate", json={
        "owner_id": "owner1",
        "subject": "Algebra",
        "term_name": "Term 1",
        "start_date": "2026-08-03",  # a Monday
        "lesson_count": 4,
        "lessons_per_week": 2,
        "level": "C1",
    })
    assert resp.status_code == 200
    plan = resp.json()
    yield plan
    client.delete(f"/api/lesson-planner/{plan['id']}")


def test_schedule_dates_respects_lessons_per_week_and_weekdays_only():
    monday = date(2026, 8, 3)
    dates = _schedule_dates(monday, 4, 2)
    assert dates == ["2026-08-03", "2026-08-04", "2026-08-10", "2026-08-11"]
    for d in dates:
        assert date.fromisoformat(d).weekday() < 5


def test_generate_requires_all_fields():
    resp = client.post("/api/lesson-planner/generate", json={
        "owner_id": "", "subject": "", "term_name": "", "start_date": "",
    })
    assert resp.status_code == 400


def test_generate_rejects_bad_date_format():
    resp = client.post("/api/lesson-planner/generate", json={
        "owner_id": "owner1", "subject": "Algebra", "term_name": "Term 1", "start_date": "not-a-date",
    })
    assert resp.status_code == 400


def test_generate_creates_plan_with_scheduled_lessons(generated_plan):
    assert generated_plan["subject"] == "Algebra"
    assert generated_plan["term_name"] == "Term 1"
    assert generated_plan["level"] == "C1"
    lessons = generated_plan["lessons"]
    assert len(lessons) == 4
    assert [l["title"] for l in lessons] == ["Introduction", "Core concepts", "Applications", "Review"]
    assert lessons[0]["objectives"] == ["Define key terms", "Set expectations"]
    dates = [l["date"] for l in lessons]
    assert dates == ["2026-08-03", "2026-08-04", "2026-08-10", "2026-08-11"]
    assert len({l["id"] for l in lessons}) == 4


def test_list_scoped_by_owner(generated_plan):
    mine = client.get("/api/lesson-planner", params={"owner_id": "owner1"}).json()
    assert any(p["id"] == generated_plan["id"] for p in mine)

    other = client.get("/api/lesson-planner", params={"owner_id": "someone_else"}).json()
    assert not any(p["id"] == generated_plan["id"] for p in other)


def test_get_plan(generated_plan):
    resp = client.get(f"/api/lesson-planner/{generated_plan['id']}")
    assert resp.status_code == 200
    assert resp.json()["id"] == generated_plan["id"]


def test_get_unknown_plan_404():
    resp = client.get("/api/lesson-planner/not-a-real-id")
    assert resp.status_code == 404


def test_delete_unknown_plan_404():
    resp = client.delete("/api/lesson-planner/not-a-real-id")
    assert resp.status_code == 404


def test_reschedule_lesson_updates_date(generated_plan):
    lesson_id = generated_plan["lessons"][0]["id"]
    resp = client.patch(
        f"/api/lesson-planner/{generated_plan['id']}/lessons/{lesson_id}",
        json={"date": "2026-09-01"},
    )
    assert resp.status_code == 200
    updated = next(l for l in resp.json()["lessons"] if l["id"] == lesson_id)
    assert updated["date"] == "2026-09-01"


def test_reschedule_requires_date(generated_plan):
    lesson_id = generated_plan["lessons"][0]["id"]
    resp = client.patch(f"/api/lesson-planner/{generated_plan['id']}/lessons/{lesson_id}", json={})
    assert resp.status_code == 400


def test_reschedule_rejects_bad_date_format(generated_plan):
    lesson_id = generated_plan["lessons"][0]["id"]
    resp = client.patch(
        f"/api/lesson-planner/{generated_plan['id']}/lessons/{lesson_id}",
        json={"date": "not-a-date"},
    )
    assert resp.status_code == 400


def test_reschedule_unknown_lesson_400(generated_plan):
    resp = client.patch(
        f"/api/lesson-planner/{generated_plan['id']}/lessons/not-a-real-lesson",
        json={"date": "2026-09-01"},
    )
    assert resp.status_code == 400


def test_reschedule_unknown_plan_404():
    resp = client.patch(
        "/api/lesson-planner/not-a-real-plan/lessons/not-a-real-lesson",
        json={"date": "2026-09-01"},
    )
    assert resp.status_code == 404


def test_delete_plan(generated_plan):
    resp = client.delete(f"/api/lesson-planner/{generated_plan['id']}")
    assert resp.status_code == 200
    assert client.get(f"/api/lesson-planner/{generated_plan['id']}").status_code == 404
