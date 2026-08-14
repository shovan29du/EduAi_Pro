from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _lessons(level: str, subject: str):
    resp = client.get(f"/api/level/{level}/subjects/{subject}")
    assert resp.status_code == 200
    return resp.json()["subject"]["lessons"]


def test_different_lessons_in_the_same_subject_get_different_graphs():
    lessons = _lessons("5", "Science")
    assert len(lessons) >= 2
    points_seen = {tuple(l["graph"]["points"]) for l in lessons[:5]}
    assert len(points_seen) > 1, "every lesson's graph has identical points"


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


def test_graph_axis_labels_are_domain_appropriate():
    math_graph = _lessons("5", "Math")[0]["graph"]
    history_graph = _lessons("5", "World History")[0]["graph"]
    assert math_graph["x_axis"] != history_graph["x_axis"]
