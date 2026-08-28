"""Every lesson across all syllabus files should carry at least a
lesson-specific concept-flow figure or wiki_title for a real photo lookup
(SubjectLessons.jsx already renders both), and the Grade 5 Math pilot
lessons should carry genuinely correct data_table / graph / formulae
content.
"""
import glob
import json

from app.main import SYLLABUS_DIR

STOPWORDS = {"with", "and", "the", "of", "for", "a", "an", "in", "on", "to", "at", "or", "but", "is", "as"}


def _all_lessons():
    lessons = []
    for path in glob.glob(str(SYLLABUS_DIR / "*.json")):
        data = json.loads(open(path, encoding="utf-8").read())
        for subject in data.get("subjects", {}).values():
            lessons.extend(subject.get("lessons", []))
    return lessons


def test_every_lesson_has_a_wiki_title_for_real_photo_lookup():
    lessons = _all_lessons()
    assert len(lessons) >= 40000
    missing = [l["id"] for l in lessons if not l.get("wiki_title")]
    assert not missing, f"{len(missing)} lessons missing wiki_title, e.g. {missing[:5]}"


def test_most_lessons_have_a_quality_concept_figure():
    lessons = _all_lessons()
    with_figure = [l for l in lessons if l.get("figure")]
    assert len(with_figure) / len(lessons) >= 0.85
    for lesson in with_figure:
        figure = lesson["figure"]
        assert figure.get("caption")
        nodes = figure.get("nodes") or []
        assert len(nodes) >= 3
        for node in nodes:
            assert node.lower() not in STOPWORDS
            assert len(node) >= 3


def test_grade5_math_pilot_lessons_have_real_charts():
    data = json.loads((SYLLABUS_DIR / "grade5.json").read_text(encoding="utf-8"))
    lessons = {l["id"]: l for l in data["subjects"]["Math"]["lessons"]}

    percentages = lessons["math-g5-l1"]
    assert percentages["data_table"]["headers"] == ["Fraction", "Decimal", "Percent"]
    assert ["1/2", "0.5", "50%"] in percentages["data_table"]["rows"]
    assert any("Percent = (Part" in f for f in percentages["formulae"])

    line_graphs = lessons["math-g5-l19"]
    assert line_graphs["graph"]["points"] == [2, 4, 7, 9, 13, 15]
    assert line_graphs["graph"]["x_axis"] and line_graphs["graph"]["y_axis"]

    prime_factorization = lessons["math-g5-l30"]
    rows = {row[0]: row[1] for row in prime_factorization["data_table"]["rows"]}
    assert rows["12"] == "2 × 2 × 3"
    assert rows["30"] == "2 × 3 × 5"

    # At least half of the 30-lesson pilot batch got a chart/table/formula.
    enriched = sum(1 for l in lessons.values() if l.get("data_table") or l.get("graph") or l.get("formulae"))
    assert enriched >= 15
