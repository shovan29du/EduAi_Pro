"""Checks on the real, built enrichment file for Undergraduate Years 1-4 and Master's Years 1-2."""
import json
import re
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
DATA = json.loads((BACKEND / "data" / "lesson_enrichment" / "enrichment.json").read_text(encoding="utf-8"))
LEVELS = ["ug1", "ug2", "ug3", "ug4", "m1", "m2"]


def syllabus(level):
    return json.loads((BACKEND / "syllabus" / f"level_{level}.json").read_text(encoding="utf-8"))["subjects"]


@pytest.mark.parametrize("level", LEVELS)
def test_every_lesson_is_covered_and_has_a_complete_subject_pack(level):
    for subject, content in syllabus(level).items():
        pack = DATA["packs"][subject]
        assert pack["tables"] and len(pack["cases"]) >= 2
        for lesson in content["lessons"]:
            entry = DATA["lessons"][lesson["id"]]
            assert entry["s"] == subject and entry["q"]


def test_subject_packs_carry_no_equations():
    # Equations are shown only on lessons about a quantitative topic.
    assert all("formulas" not in pack for pack in DATA["packs"].values())


def test_packs_are_well_formed():
    for subject, pack in DATA["packs"].items():
        for t in pack["tables"]:
            assert t["headers"] and t["rows"], subject
            assert all(len(r) == len(t["headers"]) for r in t["rows"]), (subject, t["title"])
        for c in pack["cases"]:
            assert all(c[k] for k in ("title", "when", "summary", "takeaway", "wiki")), (subject, c["title"])


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
    assert len(charts) >= 25
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


def test_rules_respect_their_level_limits():
    titles = {}
    for level in LEVELS:
        for subject, content in syllabus(level).items():
            for lesson in content["lessons"]:
                titles[lesson["id"]] = (level, lesson["title"])
    for lid, entry in DATA["lessons"].items():
        level, _ = titles[lid]
        if level.startswith("ug1") or level.startswith("ug2"):
            assert not ({"stochastic", "topology", "riemann", "options", "econometrics"} & set(entry.get("r", []))), lid


def test_topic_rules_do_not_fire_on_look_alike_words():
    by_title = {}
    for level in LEVELS:
        for content in syllabus(level).values():
            for lesson in content["lessons"]:
                by_title[lesson["id"]] = lesson["title"]

    def rules_for(fragment):
        return {rid for lid, e in DATA["lessons"].items() if fragment in by_title[lid] for rid in e.get("r", [])}

    assert "nuclear" not in rules_for("Nuclear Magnetic Resonance")
    assert "quantumcomp" not in rules_for("Expected Shortfall")
    assert "energy" not in rules_for("Rate Limiting")
    assert "ozone" not in rules_for("Eurozone Sovereign")
    assert "h_ww1" not in rules_for("World War II")
    assert "h_wto" not in rules_for("Newton's Laws")
    assert "c_thermochem" not in rules_for("Chess")
    assert "h_byzantine" not in rules_for("Byzantine Fault")
