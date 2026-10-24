import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.ai_tutor import _parse_graded_answer_response, _parse_study_questions_response
from app.main import app
from app.study_coach import _quality_from_result, _sm2_update

client = TestClient(app)

SAMPLE_RAW = """TYPE: MCQ
Q: What is the powerhouse of the cell?
A) Nucleus
B) Mitochondria
C) Ribosome
D) Golgi apparatus
ANSWER: B
EXPLANATION: Mitochondria produce ATP through cellular respiration.
TYPE: OPEN
Q: Why do cells need energy?
KEY_POINTS: growth; repair; active transport; maintaining homeostasis
EXPLANATION: Cells use energy to power all life processes.
"""

FAKE_QUESTIONS = [
    {"type": "mcq", "question": "What is 2+2?", "options": {"A": "3", "B": "4", "C": "5", "D": "6"}, "answer": "B", "explanation": "2+2=4"},
    {"type": "open", "question": "Explain photosynthesis.", "key_points": ["light energy", "chlorophyll", "produces glucose"], "explanation": "Plants convert light into chemical energy."},
]


def test_parse_study_questions_response_extracts_mcq_and_open():
    parsed = _parse_study_questions_response(SAMPLE_RAW)
    assert len(parsed) == 2
    assert parsed[0] == {
        "type": "mcq",
        "question": "What is the powerhouse of the cell?",
        "options": {"A": "Nucleus", "B": "Mitochondria", "C": "Ribosome", "D": "Golgi apparatus"},
        "answer": "B",
        "explanation": "Mitochondria produce ATP through cellular respiration.",
    }
    assert parsed[1]["type"] == "open"
    assert parsed[1]["key_points"] == ["growth", "repair", "active transport", "maintaining homeostasis"]


def test_parse_study_questions_response_handles_garbage():
    assert _parse_study_questions_response("nothing structured here") == []


def test_parse_graded_answer_response_extracts_score_and_feedback():
    result = _parse_graded_answer_response("SCORE: 72\nFEEDBACK: Good understanding, but missing detail.")
    assert result == {"score": 72, "feedback": "Good understanding, but missing detail."}


def test_parse_graded_answer_response_clamps_score_and_falls_back():
    result = _parse_graded_answer_response("SCORE: 150\nFEEDBACK: Overshoot test.")
    assert result["score"] == 100
    result2 = _parse_graded_answer_response("no structure at all")
    assert result2["score"] == 0
    assert result2["feedback"] == "no structure at all"


@pytest.mark.parametrize("correct,confidence,expected", [
    (True, 5, 5),
    (True, 1, 3),
    (False, 5, 2),
    (False, 1, 0),
])
def test_quality_from_result(correct, confidence, expected):
    assert _quality_from_result(correct, confidence) == expected


def test_sm2_update_grows_interval_on_repeated_success():
    record = {"ease": 2.5, "interval_days": 0, "review_count": 0}
    _sm2_update(record, quality=5)
    assert record["interval_days"] == 1
    assert record["review_count"] == 1
    _sm2_update(record, quality=5)
    assert record["interval_days"] == 6
    assert record["review_count"] == 2
    _sm2_update(record, quality=5)
    assert record["interval_days"] > 6
    assert record["review_count"] == 3


def test_sm2_update_resets_on_failure():
    record = {"ease": 2.5, "interval_days": 15, "review_count": 3}
    _sm2_update(record, quality=1)
    assert record["interval_days"] == 1
    assert record["review_count"] == 0


@pytest.fixture
def mock_ai_study(monkeypatch):
    monkeypatch.setattr(ai_tutor, "generate_study_questions", lambda *a, **k: FAKE_QUESTIONS)


@pytest.fixture
def generated_questions(mock_ai_study):
    resp = client.post("/api/study-coach/generate", json={
        "child": "TestChild", "topic": "basic math", "level": "5", "count": 2,
    })
    assert resp.status_code == 200
    questions = resp.json()["questions"]
    yield questions
    client.delete("/api/study-coach/topics/basic math", params={"child": "TestChild"})


def test_generate_requires_child_and_topic():
    resp = client.post("/api/study-coach/generate", json={"child": "", "topic": ""})
    assert resp.status_code == 400


def test_generate_creates_mcq_and_open_questions(generated_questions):
    types = {q["type"] for q in generated_questions}
    assert types == {"mcq", "open"}
    for q in generated_questions:
        assert q["due_date"]
        assert q["ease"] == 2.5
        assert q["review_count"] == 0


def test_due_questions_scoped_to_child(generated_questions):
    mine = client.get("/api/study-coach/due", params={"child": "TestChild"}).json()["questions"]
    assert len(mine) == 2

    other = client.get("/api/study-coach/due", params={"child": "SomeoneElse"}).json()["questions"]
    assert other == []


def test_due_requires_child():
    resp = client.get("/api/study-coach/due")
    assert resp.status_code == 422  # missing required query param


def test_answer_mcq_correct_advances_schedule(generated_questions):
    mcq = next(q for q in generated_questions if q["type"] == "mcq")
    resp = client.post(f"/api/study-coach/{mcq['id']}/answer", json={
        "child": "TestChild", "answer": "B", "confidence": 5,
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["correct"] is True
    assert data["score"] == 100
    assert data["interval_days"] >= 1


def test_answer_mcq_incorrect_resets_schedule(generated_questions):
    mcq = next(q for q in generated_questions if q["type"] == "mcq")
    resp = client.post(f"/api/study-coach/{mcq['id']}/answer", json={
        "child": "TestChild", "answer": "A", "confidence": 4,
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["correct"] is False
    assert data["score"] == 0


def test_answer_open_question_uses_ai_grading(generated_questions, monkeypatch):
    monkeypatch.setattr(ai_tutor, "grade_open_answer", lambda *a, **k: {"score": 85, "feedback": "Great job!"})
    open_q = next(q for q in generated_questions if q["type"] == "open")
    resp = client.post(f"/api/study-coach/{open_q['id']}/answer", json={
        "child": "TestChild", "answer": "Plants convert light into sugar.", "confidence": 4,
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["correct"] is True
    assert data["score"] == 85
    assert data["feedback"] == "Great job!"


def test_answer_unknown_question_404():
    resp = client.post("/api/study-coach/not-a-real-id/answer", json={"child": "TestChild", "answer": "x"})
    assert resp.status_code == 404


def test_answer_requires_child(generated_questions):
    mcq = next(q for q in generated_questions if q["type"] == "mcq")
    resp = client.post(f"/api/study-coach/{mcq['id']}/answer", json={"answer": "B"})
    assert resp.status_code == 400


def test_stats_reflect_generated_and_answered_questions(generated_questions):
    mcq = next(q for q in generated_questions if q["type"] == "mcq")
    client.post(f"/api/study-coach/{mcq['id']}/answer", json={"child": "TestChild", "answer": "B", "confidence": 5})

    stats = client.get("/api/study-coach/stats", params={"child": "TestChild"}).json()
    assert stats["total_questions"] == 2
    assert stats["topics"] == ["basic math"]


def test_delete_topic_removes_its_questions(mock_ai_study):
    client.post("/api/study-coach/generate", json={"child": "TestChild", "topic": "delete-me", "count": 2})
    resp = client.delete("/api/study-coach/topics/delete-me", params={"child": "TestChild"})
    assert resp.status_code == 200
    assert resp.json()["deleted"] == 2

    stats = client.get("/api/study-coach/stats", params={"child": "TestChild"}).json()
    assert "delete-me" not in stats["topics"]
