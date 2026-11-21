#!/usr/bin/env python3
"""Depth pass, Grade 4 Survival Skills: fill in real, hand-checked
data_table content for the 28 Grade 4 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 4 Survival
Skills to full 30/30 coverage.

Content covers standard, uncontroversial safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g4-l1": {
        "data_table": table(["Rule", "Why"], [
            ["Stop, Drop, and Roll", "Puts out fire on clothing"],
            ["Know two ways out of every room", "Ensures an escape route if one is blocked"],
        ]),
    },
    "survival-skills-g4-l3": {
        "data_table": table(["Shelter Type", "Material"], [
            ["Lean-to", "Branches leaned against a support"], ["Debris hut", "Leaves and branches for insulation"],
        ]),
    },
    "survival-skills-g4-l4": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Never swim without adult supervision", "Adults can respond to emergencies"],
        ]),
    },
    "survival-skills-g4-l5": {
        "data_table": table(["Water Source", "Safe to Drink?"], [
            ["Tap water (treated)", "Yes"], ["Untreated stream water", "No, without purification"],
        ]),
    },
    "survival-skills-g4-l6": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of equal thickness"], ["Bowline", "Creates a secure loop"],
        ]),
    },
    "survival-skills-g4-l7": {
        "data_table": table(["Weather Sign", "Meaning"], [
            ["Dark clouds", "Possible storm approaching"], ["Sudden temperature drop", "Weather change coming"],
        ]),
    },
    "survival-skills-g4-l8": {
        "data_table": table(["Rule", "Why"], [
            ["Stay in one place", "Makes it easier for searchers to find you"],
            ["Make noise or use a signal", "Helps others locate you"],
        ]),
    },
    "survival-skills-g4-l9": {
        "data_table": table(["Rule", "Why"], [
            ["Never go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if approached", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g4-l10": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three whistle blasts", "Universal distress signal"], ["Waving both arms overhead", "Signals for help"],
        ]),
    },
    "survival-skills-g4-l11": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Checks for oncoming traffic"],
            ["Cross at a crosswalk", "Safest place for drivers to see you"],
        ]),
    },
    "survival-skills-g4-l12": {
        "data_table": table(["Hazard", "Prevention"], [
            ["Loose rugs", "Secure them to prevent trips"], ["Exposed wires", "Keep them covered and tidy"],
        ]),
    },
    "survival-skills-g4-l13": {
        "data_table": table(["Drill Step", "Action"], [
            ["Drop", "Get down on hands and knees"], ["Cover", "Protect head and neck under sturdy furniture"],
            ["Hold on", "Hold onto shelter until shaking stops"],
        ]),
    },
    "survival-skills-g4-l14": {
        "data_table": table(["Weather Emergency", "Safe Action"], [
            ["Thunderstorm", "Go indoors, avoid open areas"], ["Flood", "Move to higher ground"],
        ]),
    },
    "survival-skills-g4-l16": {
        "data_table": table(["Hazard", "Rule"], [
            ["Poison ivy", "Leaves of three, let it be"], ["Unknown wild animals", "Keep a safe distance"],
        ]),
    },
    "survival-skills-g4-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Stay on marked trails", "Reduces risk of getting lost"],
            ["Tell someone your plans", "Helps others find you if needed"],
        ]),
    },
    "survival-skills-g4-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Tell a trusted adult about anything unsafe", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g4-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Reach or throw, don't go", "Avoid entering the water yourself to help someone"],
        ]),
    },
    "survival-skills-g4-l20": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Following the plan", "Reduces panic in an emergency"],
        ]),
    },
    "survival-skills-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Home fire drill", "Practicing the escape plan with family"],
        ]),
    },
    "survival-skills-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Hiking trip", "Using a compass to stay on course"],
        ]),
    },
    "survival-skills-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Camping trip", "Building a simple shelter for the night"],
        ]),
    },
    "survival-skills-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Pool day", "Swimming only with a buddy"],
        ]),
    },
    "survival-skills-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Camping", "Boiling stream water before drinking it"],
        ]),
    },
    "survival-skills-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Setting up a tent", "Using knots to secure guy lines"],
        ]),
    },
    "survival-skills-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Outdoor trip planning", "Checking the forecast before leaving"],
        ]),
    },
    "survival-skills-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Family hike", "Agreeing on a meeting point if separated"],
        ]),
    },
    "survival-skills-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Walking home from school", "Only speaking to trusted adults"],
        ]),
    },
    "survival-skills-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Lost hiker", "Using a whistle to signal for help"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Survival Skills lessons (completing 30/30).")


if __name__ == "__main__":
    main()
