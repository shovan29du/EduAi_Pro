#!/usr/bin/env python3
"""Depth pass, Grade 8 Survival Skills: fill in real, hand-checked
data_table content for the 38 Grade 8 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Survival
Skills to full 40/40 coverage.

Content covers standard, uncontroversial safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g8-l1": {
        "data_table": table(["Shelter Type", "Material"], [
            ["Lean-to", "Branches leaned against a support"], ["Debris hut", "Leaves and branches for insulation"],
        ]),
    },
    "survival-skills-g8-l2": {
        "data_table": table(["Tool", "Use"], [
            ["Compass", "Points to magnetic north"], ["Topographic map", "Shows elevation and terrain"],
        ]),
    },
    "survival-skills-g8-l3": {
        "data_table": table(["Navigation Method", "How It Works"], [
            ["Sun position", "Rises in the east, sets in the west"], ["Moss on trees", "Often grows more on the shaded side"],
        ]),
    },
    "survival-skills-g8-l5": {
        "data_table": table(["Method", "How It Works"], [
            ["Friction fire", "Rubbing wood to generate heat"], ["Fire starter/flint", "Sparks ignite tinder"],
        ]),
    },
    "survival-skills-g8-l6": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of equal thickness"], ["Bowline", "Creates a secure loop"],
        ]),
    },
    "survival-skills-g8-l7": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Small cut", "Clean it and cover with a bandage"], ["Sprain", "Rest, ice, compression, elevation"],
        ]),
    },
    "survival-skills-g8-l8": {
        "data_table": table(["Plant", "Rule"], [
            ["Poison ivy", "Leaves of three, let it be"],
        ]),
    },
    "survival-skills-g8-l9": {
        "data_table": table(["Rule", "Why"], [
            ["Never eat unfamiliar plants", "Prevents accidental poisoning"],
        ]),
    },
    "survival-skills-g8-l10": {
        "data_table": table(["Method", "Description"], [
            ["Hand line fishing", "A simple line with a hook and bait"],
        ]),
    },
    "survival-skills-g8-l11": {
        "data_table": table(["Sign", "Possible Meaning"], [
            ["Dark, towering clouds", "Possible thunderstorm"],
        ]),
    },
    "survival-skills-g8-l12": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Flashlight", "Provides light during a power outage"], ["Water", "Prevents dehydration"],
        ]),
    },
    "survival-skills-g8-l13": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three whistle blasts", "Universal distress signal"], ["Mirror flash", "Can be seen from far away"],
        ]),
    },
    "survival-skills-g8-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Keep a safe distance from wild animals", "Prevents provoking them"],
        ]),
    },
    "survival-skills-g8-l16": {
        "data_table": table(["Leave No Trace Principle", "Meaning"], [
            ["Pack it in, pack it out", "Take your trash with you"],
        ]),
    },
    "survival-skills-g8-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Use tools only for their intended purpose", "Reduces injury risk"],
        ]),
    },
    "survival-skills-g8-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Clear the area around the fire", "Prevents spreading"], ["Fully extinguish before leaving", "Prevents reignition"],
        ]),
    },
    "survival-skills-g8-l19": {
        "data_table": table(["Preparedness Item", "Purpose"], [
            ["First aid kit", "Treats minor injuries"], ["Emergency contact list", "Quick access in a crisis"],
        ]),
    },
    "survival-skills-g8-l20": {
        "data_table": table(["Drill Step", "Action"], [
            ["Drop", "Get down on hands and knees"], ["Cover", "Protect head and neck"],
        ]),
    },
    "survival-skills-g8-l21": {
        "data_table": table(["Rule", "Why"], [
            ["Move to higher ground", "Floodwater rises quickly"],
        ]),
    },
    "survival-skills-g8-l22": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes"], ["Clove hitch", "Securing a rope to a post"],
        ]),
    },
    "survival-skills-g8-l23": {
        "data_table": table(["Step", "Action"], [
            ["1", "Clean the wound with water"], ["2", "Apply pressure to stop bleeding"],
        ]),
    },
    "survival-skills-g8-l24": {
        "data_table": table(["Burn Degree", "First Aid"], [
            ["Minor (first-degree)", "Cool water, then cover loosely"],
        ]),
    },
    "survival-skills-g8-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["CPR", "Used when a person is unresponsive and not breathing normally"],
            ["When to call for help first", "Before starting CPR, call emergency services"],
        ]),
    },
    "survival-skills-g8-l26": {
        "data_table": table(["Situation", "Response"], [
            ["Insect sting", "Remove the stinger, clean the area"], ["Snake bite", "Keep calm, seek medical help immediately"],
        ]),
    },
    "survival-skills-g8-l27": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Deep breathing", "Calms the body"], ["Following a plan", "Reduces panic"],
        ]),
    },
    "survival-skills-g8-l28": {
        "data_table": table(["Rule", "Why"], [
            ["Know your surroundings", "Helps identify safe locations"],
        ]),
    },
    "survival-skills-g8-l29": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Checks for oncoming traffic"],
        ]),
    },
    "survival-skills-g8-l30": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"], ["Reach or throw, don't go", "Avoid entering the water yourself"],
        ]),
    },
    "survival-skills-g8-l31": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Contour line", "Connects points of equal elevation"],
        ]),
    },
    "survival-skills-g8-l32": {
        "data_table": table(["Climate", "Shelter Consideration"], [
            ["Cold climate", "Insulation is the priority"], ["Hot climate", "Shade and ventilation are the priority"],
        ]),
    },
    "survival-skills-g8-l33": {
        "data_table": table(["Preservation Method", "Purpose"], [
            ["Drying", "Removes moisture to prevent spoilage"], ["Salting", "Draws out moisture, inhibits bacteria"],
        ]),
    },
    "survival-skills-g8-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Staying put", "Makes it easier for searchers to find a lost person"],
        ]),
    },
    "survival-skills-g8-l35": {
        "data_table": table(["Method", "Use"], [
            ["Signal fire", "Visible smoke can attract attention"], ["Whistle", "Carries sound over long distances"],
        ]),
    },
    "survival-skills-g8-l36": {
        "data_table": table(["Skill", "Use"], [
            ["Basic stitch", "Repairing a small tear in fabric or gear"],
        ]),
    },
    "survival-skills-g8-l37": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "survival-skills-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Disaster risk reduction", "Planning ahead to reduce harm from disasters"],
        ]),
    },
    "survival-skills-g8-l39": {
        "data_table": table(["Star/Constellation", "Use"], [
            ["North Star (Polaris)", "Indicates true north in the Northern Hemisphere"],
        ]),
    },
    "survival-skills-g8-l40": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Working together", "Combines skills and resources"], ["Clear communication", "Reduces confusion in emergencies"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Survival Skills lessons (completing 40/40).")


if __name__ == "__main__":
    main()
