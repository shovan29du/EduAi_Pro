#!/usr/bin/env python3
"""Depth pass, Grade 3 Survival Skills: fill in real, hand-checked
data_table content for the 18 Grade 3 Survival Skills lessons not covered
by the earlier breadth-first batch. Brings Grade 3 Survival Skills to
full 20/20 coverage.

Content covers standard, uncontroversial safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g3-l1": {
        "data_table": table(["Rule", "Why"], [
            ["Know your address and phone number", "Helps adults or emergency workers help you"],
        ]),
    },
    "survival-skills-g3-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Never go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if approached", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g3-l3": {
        "data_table": table(["Step", "Action"], [
            ["1", "Clean the cut with water"], ["2", "Cover with a clean bandage"],
        ]),
    },
    "survival-skills-g3-l5": {
        "data_table": table(["Rule", "Why"], [
            ["Stop, Drop, and Roll", "Puts out fire on clothing"],
            ["Know two ways out of every room", "Ensures an escape route if one is blocked"],
        ]),
    },
    "survival-skills-g3-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Checks for oncoming traffic"],
            ["Cross at a crosswalk", "Safest place for drivers to see you"],
        ]),
    },
    "survival-skills-g3-l7": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Never swim without adult supervision", "Adults can respond to emergencies"],
        ]),
    },
    "survival-skills-g3-l8": {
        "data_table": table(["Map Feature", "Safety Use"], [
            ["Compass rose", "Shows direction to avoid getting lost"],
            ["Landmark symbols", "Helps identify your location"],
        ]),
    },
    "survival-skills-g3-l9": {
        "data_table": table(["Weather Emergency", "Safe Action"], [
            ["Thunderstorm", "Go indoors, avoid open areas"], ["Tornado", "Go to a basement or interior room"],
        ]),
    },
    "survival-skills-g3-l11": {
        "data_table": table(["Rule", "Why"], [
            ["Stay with a group", "Reduces risk of getting lost"],
            ["Wear appropriate clothing", "Protects from weather conditions"],
        ]),
    },
    "survival-skills-g3-l12": {
        "data_table": table(["Situation", "Emergency Number (US Example)"], [
            ["Fire, medical, police emergency", "911"],
        ]),
    },
    "survival-skills-g3-l13": {
        "data_table": table(["Checklist Item", "Why"], [
            ["Smoke detectors working", "Warns of fire early"],
            ["Emergency contacts posted", "Quick access in a crisis"],
        ]),
    },
    "survival-skills-g3-l14": {
        "data_table": table(["First Aid Kit Item", "Use"], [
            ["Bandages", "Cover small cuts"], ["Antiseptic wipes", "Clean a wound"],
        ]),
    },
    "survival-skills-g3-l15": {
        "data_table": table(["Safe Adult Example", "Why"], [
            ["Parent or guardian", "Responsible for your care"],
            ["Teacher or police officer", "Trained to help in emergencies"],
        ]),
    },
    "survival-skills-g3-l16": {
        "data_table": table(["Wilderness Rule", "Why"], [
            ["Stay on marked trails", "Reduces risk of getting lost"],
            ["Tell someone your plans", "Helps others find you if needed"],
        ]),
    },
    "survival-skills-g3-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Wear a helmet", "Protects your head in a fall"],
            ["Follow traffic signals", "Keeps you safe around vehicles"],
        ]),
    },
    "survival-skills-g3-l18": {
        "data_table": table(["Drill", "Purpose"], [
            ["Tornado drill", "Practices moving to a safe interior space"],
            ["Fire drill", "Practices exiting the building safely"],
        ]),
    },
    "survival-skills-g3-l19": {
        "data_table": table(["Sun Safety Tip", "Why"], [
            ["Wear sunscreen", "Protects skin from UV rays"], ["Wear a hat", "Shades face and head"],
        ]),
    },
    "survival-skills-g3-l20": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body during stress"],
            ["Talking to a trusted adult", "Helps process difficult feelings"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Survival Skills lessons (completing 20/20).")


if __name__ == "__main__":
    main()
