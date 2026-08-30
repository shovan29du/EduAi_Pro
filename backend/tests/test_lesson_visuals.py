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


def test_every_math_level_from_grade1_to_masters_year2_has_real_charts():
    """Breadth-first pass: every level from Grade 1 through Masters Year 2
    should have at least a handful of Math lessons with a genuine
    data_table/graph/formulae (Grade 5 is covered by the pilot test above)."""
    levels = [
        "grade1", "grade2", "grade3", "grade4", "grade6", "grade7", "grade8",
        "grade9", "grade10", "level_c1", "level_c2", "level_m1", "level_m2",
        "level_ug1", "level_ug2", "level_ug3", "level_ug4",
    ]
    total_enriched = 0
    for level in levels:
        data = json.loads((SYLLABUS_DIR / f"{level}.json").read_text(encoding="utf-8"))
        lessons = data["subjects"]["Math"]["lessons"]
        enriched = [l for l in lessons if l.get("data_table") or l.get("graph") or l.get("formulae")]
        assert enriched, f"{level} has no Math lessons with real chart/table/graph content"
        for lesson in enriched:
            if lesson.get("data_table"):
                assert lesson["data_table"]["headers"]
                assert lesson["data_table"]["rows"]
            if lesson.get("graph"):
                assert lesson["graph"]["points"]
                assert all(p >= 0 for p in lesson["graph"]["points"])
            if lesson.get("formulae"):
                assert all(isinstance(f, str) and f for f in lesson["formulae"])
        total_enriched += len(enriched)
    assert total_enriched >= 80

    # Spot-check a few real, independently-verifiable facts.
    g1 = json.loads((SYLLABUS_DIR / "grade1.json").read_text(encoding="utf-8"))
    money = {l["id"]: l for l in g1["subjects"]["Math"]["lessons"]}["math-g1-l20"]
    assert ["Quarter", "25 cents"] in money["data_table"]["rows"]

    g8 = json.loads((SYLLABUS_DIR / "grade8.json").read_text(encoding="utf-8"))
    pythag = {l["id"]: l for l in g8["subjects"]["Math"]["lessons"]}["math-g8-l27"]
    assert ["13 ft", "5 ft", "12 ft"] in pythag["data_table"]["rows"]

    m1 = json.loads((SYLLABUS_DIR / "level_m1.json").read_text(encoding="utf-8"))
    zeta = {l["id"]: l for l in m1["subjects"]["Math"]["lessons"]}["math-m1-l28"]
    assert ["2", "1.6449"] in zeta["data_table"]["rows"]

    ug4 = json.loads((SYLLABUS_DIR / "level_ug4.json").read_text(encoding="utf-8"))
    pnt = {l["id"]: l for l in ug4["subjects"]["Math"]["lessons"]}["math-ug4-l25"]
    assert ["100", "25", "21.7"] in pnt["data_table"]["rows"]
