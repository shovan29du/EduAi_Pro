from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _lessons(level: str, subject: str):
    resp = client.get(f"/api/level/{level}/subjects/{subject}")
    assert resp.status_code == 200
    return resp.json()["subject"]["lessons"]


def test_lessons_never_include_a_graph_field():
    for level, subject in (("1", "Math"), ("5", "Science"), ("M2", "Philosophy")):
        lessons = _lessons(level, subject)
        assert lessons, f"no lessons returned for {level}/{subject}"
        assert all("graph" not in l for l in lessons), f"graph field leaked into {level}/{subject}"


def test_different_lessons_get_different_table_rows():
    lessons = _lessons("5", "Science")
    rows_seen = {tuple(l["data_table"]["rows"][0]) for l in lessons[:5]}
    assert len(rows_seen) > 1, "every lesson's table row is identical"


def test_figure_nodes_use_the_lesson_s_own_key_concepts():
    lessons = _lessons("5", "Science")
    lesson = next(l for l in lessons if l.get("key_concepts"))
    assert lesson["figure"]["nodes"][0] == lesson["key_concepts"][0]


def test_subject_domains_get_distinct_table_headers():
    math_headers = _lessons("5", "Math")[0]["data_table"]["headers"]
    science_headers = _lessons("5", "Science")[0]["data_table"]["headers"]
    history_headers = _lessons("5", "World History")[0]["data_table"]["headers"]
    assert math_headers != science_headers
    assert science_headers != history_headers
    assert math_headers != history_headers


