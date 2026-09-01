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


def test_grade1_to_4_all_subjects_have_real_charts():
    """Breadth-first pass extending beyond Math: every subject (not just
    Math) in Grade 1 through Grade 4 should have a handful of lessons with
    a genuine data_table of real, verifiable facts."""
    for level in ["grade1", "grade2", "grade3", "grade4"]:
        data = json.loads((SYLLABUS_DIR / f"{level}.json").read_text(encoding="utf-8"))
        non_math_enriched = 0
        for subject_name, subject in data["subjects"].items():
            if subject_name == "Math":
                continue
            enriched = [l for l in subject["lessons"] if l.get("data_table")]
            for lesson in enriched:
                assert lesson["data_table"]["headers"]
                assert lesson["data_table"]["rows"]
                for row in lesson["data_table"]["rows"]:
                    assert len(row) == len(lesson["data_table"]["headers"])
            non_math_enriched += len(enriched)
        assert non_math_enriched >= 25, f"{level} has too few non-Math lessons with real chart/table content"

    # Spot-check a few real, independently-verifiable facts.
    g1 = json.loads((SYLLABUS_DIR / "grade1.json").read_text(encoding="utf-8"))
    continents = {l["id"]: l for l in g1["subjects"]["Geography"]["lessons"]}["geography-g1-l8"]
    assert ["Asia", "1 (largest)"] in continents["data_table"]["rows"]

    g2 = json.loads((SYLLABUS_DIR / "grade2.json").read_text(encoding="utf-8"))
    pillars = {l["id"]: l for l in g2["subjects"]["Islamic Studies"]["lessons"]}["is-g2-l1"]
    assert ["Hajj", "Pilgrimage to Mecca"] in pillars["data_table"]["rows"]

    g4 = json.loads((SYLLABUS_DIR / "grade4.json").read_text(encoding="utf-8"))
    bones = {l["id"]: l for l in g4["subjects"]["Science"]["lessons"]}["science-g4-l13"]
    assert ["Number of bones in the adult human body", "206"] in bones["data_table"]["rows"]


def test_grade5_non_math_subjects_have_real_charts():
    """Grade 5 Math already has full pilot coverage; this checks every
    OTHER subject at Grade 5 also has a batch of real chart/table content."""
    data = json.loads((SYLLABUS_DIR / "grade5.json").read_text(encoding="utf-8"))
    non_math_enriched = 0
    for subject_name, subject in data["subjects"].items():
        if subject_name == "Math":
            continue
        enriched = [l for l in subject["lessons"] if l.get("data_table")]
        for lesson in enriched:
            assert lesson["data_table"]["headers"]
            assert lesson["data_table"]["rows"]
        non_math_enriched += len(enriched)
    assert non_math_enriched >= 25

    articles = {l["id"]: l for l in data["subjects"]["Islamic Studies"]["lessons"]}["islamic-studies-g5-l2"]
    assert ["1", "Allah (God)"] in articles["data_table"]["rows"]

    rivers = {l["id"]: l for l in data["subjects"]["General Knowledge"]["lessons"]}["general-knowledge-g5-l4"]
    assert ["Nile", "~6,650 km", "Africa"] in rivers["data_table"]["rows"]


def test_grade6_and_7_all_subjects_have_real_charts():
    """Breadth-first pass: every subject in Grade 6 and Grade 7 should have
    a handful of lessons with a genuine data_table of real, verifiable
    facts, beyond the Math-only breadth batch."""
    for level in ["grade6", "grade7"]:
        data = json.loads((SYLLABUS_DIR / f"{level}.json").read_text(encoding="utf-8"))
        non_math_enriched = 0
        for subject_name, subject in data["subjects"].items():
            if subject_name == "Math":
                continue
            enriched = [l for l in subject["lessons"] if l.get("data_table")]
            for lesson in enriched:
                assert lesson["data_table"]["headers"]
                assert lesson["data_table"]["rows"]
                for row in lesson["data_table"]["rows"]:
                    assert len(row) == len(lesson["data_table"]["headers"])
            non_math_enriched += len(enriched)
        assert non_math_enriched >= 25, f"{level} has too few non-Math lessons with real chart/table content"

    g6 = json.loads((SYLLABUS_DIR / "grade6.json").read_text(encoding="utf-8"))
    newton = {l["id"]: l for l in g6["subjects"]["Science"]["lessons"]}["science-g6-l13"]
    assert "F = m x a" in newton["formulae"][0]

    g7 = json.loads((SYLLABUS_DIR / "grade7.json").read_text(encoding="utf-8"))
    wonders = {l["id"]: l for l in g7["subjects"]["General Knowledge"]["lessons"]}["general-knowledge-g7-l4"]
    assert ["Taj Mahal", "India"] in wonders["data_table"]["rows"]


def test_grade8_to_10_all_subjects_have_real_charts():
    """Breadth-first pass: every subject in Grade 8 through Grade 10
    (including the new Economics/Finance/First Aid/Physics/Chemistry/
    Biology/Philosophy subjects introduced at Grade 8) should have a
    handful of lessons with a genuine data_table of real, verifiable
    facts, beyond the Math-only breadth batch."""
    for level in ["grade8", "grade9", "grade10"]:
        data = json.loads((SYLLABUS_DIR / f"{level}.json").read_text(encoding="utf-8"))
        non_math_enriched = 0
        for subject_name, subject in data["subjects"].items():
            if subject_name == "Math":
                continue
            enriched = [l for l in subject["lessons"] if l.get("data_table")]
            for lesson in enriched:
                assert lesson["data_table"]["headers"]
                assert lesson["data_table"]["rows"]
                for row in lesson["data_table"]["rows"]:
                    assert len(row) == len(lesson["data_table"]["headers"])
            non_math_enriched += len(enriched)
        assert non_math_enriched >= 40, f"{level} has too few non-Math lessons with real chart/table content"

    g8 = json.loads((SYLLABUS_DIR / "grade8.json").read_text(encoding="utf-8"))
    caliphs = {l["id"]: l for l in g8["subjects"]["Islamic Studies"]["lessons"]}["islamic-studies-g8-l7"]
    assert ["Abu Bakr", "1st"] in caliphs["data_table"]["rows"]

    g9 = json.loads((SYLLABUS_DIR / "grade9.json").read_text(encoding="utf-8"))
    interest = {l["id"]: l for l in g9["subjects"]["Finance"]["lessons"]}["finance-g9-l8"]
    assert ["Compound (annual)", "$1,157.63"] in interest["data_table"]["rows"]

    g10 = json.loads((SYLLABUS_DIR / "grade10.json").read_text(encoding="utf-8"))
    dna = {l["id"]: l for l in g10["subjects"]["Biology"]["lessons"]}["biology-g10-l8"]
    assert ["Adenine (A)", "Thymine (T)"] in dna["data_table"]["rows"]


def test_level_c1_and_c2_all_52_subjects_have_a_real_chart():
    """College-tier levels carry ~52 subjects each (AI, Machine Learning,
    Data Science, several programming languages, Business Studies, World
    Religions, Mythology, etc.) -- every one should have at least one real,
    verifiable data_table lesson."""
    for level in ["level_c1", "level_c2"]:
        data = json.loads((SYLLABUS_DIR / f"{level}.json").read_text(encoding="utf-8"))
        subjects = [s for s in data["subjects"] if s != "Math"]
        assert len(subjects) >= 50, f"{level} unexpectedly has few subjects: {len(subjects)}"
        missing_subjects = []
        for subject_name in subjects:
            lessons = data["subjects"][subject_name]["lessons"]
            enriched = [l for l in lessons if l.get("data_table")]
            if not enriched:
                missing_subjects.append(subject_name)
            for lesson in enriched:
                assert lesson["data_table"]["headers"]
                assert lesson["data_table"]["rows"]
                for row in lesson["data_table"]["rows"]:
                    assert len(row) == len(lesson["data_table"]["headers"])
        assert not missing_subjects, f"{level} subjects missing any real chart: {missing_subjects}"

    c1 = json.loads((SYLLABUS_DIR / "level_c1.json").read_text(encoding="utf-8"))
    cia = {l["id"]: l for l in c1["subjects"]["Cybersecurity"]["lessons"]}["cybersecurity-c1-l3"]
    assert ["Confidentiality", "Preventing unauthorized access to data"] in cia["data_table"]["rows"]

    c2 = json.loads((SYLLABUS_DIR / "level_c2.json").read_text(encoding="utf-8"))
    forces = {l["id"]: l for l in c2["subjects"]["MBA"]["lessons"]}["mba-c2-l3"]
    assert any("Threat of new entrants" in row[0] for row in forces["data_table"]["rows"])
