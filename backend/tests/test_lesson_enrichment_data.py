"""Checks on the real, built enrichment file for Master's Year 1 and 2."""
import json
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
DATA = json.loads((BACKEND / "data" / "lesson_enrichment" / "enrichment.json").read_text(encoding="utf-8"))


def lesson_ids(level):
    data = json.loads((BACKEND / "syllabus" / f"level_{level}.json").read_text(encoding="utf-8"))
    return {l["id"]: subject for subject, c in data["subjects"].items() for l in c["lessons"]}


@pytest.mark.parametrize("level", ["m1", "m2"])
def test_every_lesson_is_covered_and_has_a_complete_subject_pack(level):
    for lid, subject in lesson_ids(level).items():
        entry = DATA["lessons"][lid]
        assert entry["s"] == subject and entry["q"]
        pack = DATA["packs"][subject]
        assert len(pack["formulas"]) >= 2 and pack["tables"] and len(pack["cases"]) >= 2


def test_packs_are_well_formed():
    for subject, pack in DATA["packs"].items():
        for f in pack["formulas"]:
            assert f["label"] and f["expr"], subject
        for t in pack["tables"]:
            assert t["headers"] and t["rows"], subject
            assert all(len(r) == len(t["headers"]) for r in t["rows"]), (subject, t["title"])
        for c in pack["cases"]:
            assert all(c[k] for k in ("title", "when", "summary", "takeaway", "wiki")), (subject, c["title"])


def test_topic_rules_are_well_formed_and_used():
    used = {rid for e in DATA["lessons"].values() for rid in e.get("r", [])}
    assert used == set(DATA["rules"])
    for rid, rule in DATA["rules"].items():
        assert rule.get("formulas") or rule.get("tables") or rule.get("cases"), rid
        for t in rule.get("tables", []):
            assert all(len(r) == len(t["headers"]) for r in t["rows"]), (rid, t["title"])


def test_topic_rules_do_not_fire_on_look_alike_words():
    by_title = {}
    for level in ("m1", "m2"):
        data = json.loads((BACKEND / "syllabus" / f"level_{level}.json").read_text(encoding="utf-8"))
        for c in data["subjects"].values():
            for l in c["lessons"]:
                by_title[l["id"]] = l["title"]
    def rules_for(fragment):
        return {rid for lid, e in DATA["lessons"].items() if fragment in by_title[lid] for rid in e.get("r", [])}
    assert "nuclear" not in rules_for("Nuclear Magnetic Resonance")
    assert "quantumcomp" not in rules_for("Expected Shortfall")
    assert "energy" not in rules_for("Rate Limiting")
    assert "ozone" not in rules_for("Eurozone Sovereign")
