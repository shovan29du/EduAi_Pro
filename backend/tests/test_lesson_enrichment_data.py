"""Checks on the real, built enrichment file for school Grades 6-10, College 1-2,
Undergraduate 1-4 and Master's 1-2."""
import json
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
DATA = json.loads((BACKEND / "data" / "lesson_enrichment" / "enrichment.json").read_text(encoding="utf-8"))
FILES = {"6": "grade6", "7": "grade7", "8": "grade8", "9": "grade9", "10": "grade10", "c1": "level_c1", "c2": "level_c2",
         "ug1": "level_ug1", "ug2": "level_ug2", "ug3": "level_ug3", "ug4": "level_ug4", "m1": "level_m1", "m2": "level_m2"}
SCHOOL = ["6", "7", "8", "9", "10"]


def syllabus(level):
    return json.loads((BACKEND / "syllabus" / f"{FILES[level]}.json").read_text(encoding="utf-8"))["subjects"]


def pack_for(entry):
    return DATA["packs"][entry.get("p") or entry["s"]]


@pytest.mark.parametrize("level", list(FILES))
def test_every_lesson_is_covered_and_has_a_complete_subject_pack(level):
    for subject, content in syllabus(level).items():
        for lesson in content["lessons"]:
            entry = DATA["lessons"][lesson["id"]]
            assert entry["s"] == subject and entry["q"]
            assert (entry.get("p") == "school:" + subject) == (level in SCHOOL)
            pack = pack_for(entry)
            assert pack["tables"] and len(pack["cases"]) >= 2


def test_subject_packs_carry_no_equations():
    # Equations are shown only on lessons about a quantitative topic.
    assert all("formulas" not in pack for pack in DATA["packs"].values())


def test_packs_are_well_formed():
    for name, pack in DATA["packs"].items():
        for t in pack["tables"]:
            assert t["headers"] and t["rows"], name
            assert all(len(r) == len(t["headers"]) for r in t["rows"]), (name, t["title"])
        for c in pack["cases"]:
            assert all(c[k] for k in ("title", "when", "summary", "takeaway", "wiki")), (name, c["title"])


def test_topic_rules_are_well_formed_and_used():
    used = {rid for e in DATA["lessons"].values() for rid in e.get("r", [])}
    assert used == set(DATA["rules"])
    for rid, rule in DATA["rules"].items():
        assert rule.get("formulas") or rule.get("charts") or rule.get("tables") or rule.get("cases"), rid
        for f in rule.get("formulas", []):
            assert f["label"] and f["expr"], rid
        for t in rule.get("tables", []):
            assert all(len(r) == len(t["headers"]) for r in t["rows"]), (rid, t["title"])
        for c in rule.get("cases", []):
            assert all(c[k] for k in ("title", "when", "summary", "takeaway")), (rid, c["title"])  # wiki is optional


def test_charts_are_consistent_with_their_data():
    charts = [c for r in DATA["rules"].values() for c in r.get("charts", [])]
    assert len(charts) >= 30
    for chart in charts:
        assert chart["kind"] in ("line", "bar", "scatter") and chart["title"] and chart["x_label"] and chart["y_label"]
        keys = {k for row in chart["data"] for k in row}
        assert "x" in keys
        for name in chart["series"] + chart.get("lines", []):
            assert name in keys, (chart["title"], name)
        if chart["log"]:
            assert all(row[s] > 0 for row in chart["data"] for s in chart["series"] if s in row)


def test_equations_appear_only_on_topic_rules_that_need_them():
    with_formulas = {rid for rid, r in DATA["rules"].items() if r.get("formulas")}
    lessons_with = sum(1 for e in DATA["lessons"].values() if with_formulas & set(e.get("r", [])))
    assert 0 < lessons_with < len(DATA["lessons"]) * 0.2


def lesson_levels():
    out = {}
    for level in FILES:
        for content in syllabus(level).values():
            for lesson in content["lessons"]:
                out[lesson["id"]] = (level, lesson["title"])
    return out


def test_advanced_rules_never_reach_school_or_early_undergraduate_lessons():
    advanced = {"stochastic", "topology", "riemann", "particle", "condensed", "compchem", "neuro", "options", "var", "mm", "econometrics", "linalg"}
    levels = lesson_levels()
    for lid, entry in DATA["lessons"].items():
        level = levels[lid][0]
        if level in SCHOOL + ["c1", "c2", "ug1", "ug2"]:
            assert not (advanced & set(entry.get("r", []))), (lid, level)


def test_school_lessons_only_get_rules_written_for_them():
    levels = lesson_levels()
    school_ok_tech = {"t_http", "t_net", "t_turing", "t_deepblue"}
    college_only = {rid for rid in DATA["rules"] if rid.startswith(("t_", "e_minwage", "e_central", "e_info", "e_monopoly"))} - school_ok_tech
    for lid, entry in DATA["lessons"].items():
        if levels[lid][0] in SCHOOL:
            assert not (college_only & set(entry.get("r", []))), lid
    # early grades get only the plain-language school rules and a few simple charts
    for lid, entry in DATA["lessons"].items():
        if levels[lid][0] in ("6", "7"):
            for rid in entry.get("r", []):
                assert rid.startswith(("k_", "ch_")) or rid in ("climate", "ecology", "nutrition", "silkroad", "egypt", "americas"), (lid, rid)


def test_topic_rules_do_not_fire_on_look_alike_words():
    by_title = {lid: title for lid, (_, title) in lesson_levels().items()}

    def rules_for(fragment):
        return {rid for lid, e in DATA["lessons"].items() if fragment in by_title[lid] for rid in e.get("r", [])}

    assert "nuclear" not in rules_for("Nuclear Magnetic Resonance")
    assert "quantumcomp" not in rules_for("Expected Shortfall")
    assert "energy" not in rules_for("Rate Limiting")
    assert "energy" not in rules_for("The Solar System")
    assert "ozone" not in rules_for("Eurozone Sovereign")
    assert "h_ww1" not in rules_for("World War II")
    assert "h_wto" not in rules_for("Newton's Laws")
    assert "c_thermochem" not in rules_for("Chess")
    assert "h_byzantine" not in rules_for("Byzantine Fault")
    assert "americas" not in rules_for("Ramayana")
    assert "k_alphabet" not in rules_for("Descriptive Writing")
    assert "ottoman" not in rules_for("The Rise of Islam and Early Caliphates")
