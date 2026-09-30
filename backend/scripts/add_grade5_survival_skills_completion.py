#!/usr/bin/env python3
"""Depth pass, Grade 5 Survival Skills: fill in real, hand-checked
data_table content for the 28 Grade 5 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 5 Survival
Skills to full 30/30 coverage.

Content covers standard, uncontroversial safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g5-l1": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Reach or throw, don't go", "Avoid entering the water yourself to help someone"],
        ]),
    },
    "survival-skills-g5-l2": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Flashlight", "Provides light during a power outage"], ["Water", "Prevents dehydration"],
        ]),
    },
    "survival-skills-g5-l4": {
        "data_table": table(["Map Element", "Meaning"], [
            ["Legend", "Explains map symbols"], ["Scale", "Converts map distance to real distance"],
        ]),
    },
    "survival-skills-g5-l5": {
        "data_table": table(["Warning Type", "Meaning"], [
            ["Watch", "Conditions are possible"], ["Warning", "Conditions are occurring or imminent"],
        ]),
    },
    "survival-skills-g5-l6": {
        "data_table": table(["Drill Step", "Action"], [
            ["Drop", "Get down on hands and knees"], ["Cover", "Protect head and neck"], ["Hold on", "Stay sheltered until shaking stops"],
        ]),
    },
    "survival-skills-g5-l7": {
        "data_table": table(["Rule", "Why"], [
            ["Know two ways out of every room", "Ensures an escape route if one is blocked"],
            ["Have a meeting point outside", "Confirms everyone got out safely"],
        ]),
    },
    "survival-skills-g5-l8": {
        "data_table": table(["Step", "Action"], [
            ["1", "Clean the wound with water"], ["2", "Cover with a clean bandage"],
        ]),
    },
    "survival-skills-g5-l9": {
        "data_table": table(["Burn Degree", "First Aid"], [
            ["Minor (first-degree)", "Cool water, then cover loosely"],
        ]),
    },
    "survival-skills-g5-l10": {
        "data_table": table(["Step", "Detail"], [
            ["Stay calm", "Speak clearly to the operator"], ["Give your location", "Helps responders find you"],
        ]),
    },
    "survival-skills-g5-l11": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of equal thickness"], ["Bowline", "Creates a secure loop"],
        ]),
    },
    "survival-skills-g5-l13": {
        "data_table": table(["Shelter Type", "Material"], [
            ["Lean-to", "Branches leaned against a support"], ["Debris hut", "Leaves and branches for insulation"],
        ]),
    },
    "survival-skills-g5-l14": {
        "data_table": table(["Rule", "Why"], [
            ["Clear the area around the fire", "Prevents spreading"], ["Fully extinguish before leaving", "Prevents reignition"],
        ]),
    },
    "survival-skills-g5-l15": {
        "data_table": table(["Plant", "Rule"], [
            ["Poison ivy", "Leaves of three, let it be"],
        ]),
    },
    "survival-skills-g5-l16": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three whistle blasts", "Universal distress signal"], ["Mirror flash", "Can be seen from far away"],
        ]),
    },
    "survival-skills-g5-l17": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Deep breathing", "Calms the body"], ["Following a plan", "Reduces panic"],
        ]),
    },
    "survival-skills-g5-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Checks for oncoming traffic"],
            ["Cross at a crosswalk", "Safest place for drivers to see you"],
        ]),
    },
    "survival-skills-g5-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Wear a helmet", "Protects your head in a fall"], ["Follow traffic signals", "Keeps you safe around vehicles"],
        ]),
    },
    "survival-skills-g5-l20": {
        "data_table": table(["Rule", "Why"], [
            ["Never go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if approached", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g5-l21": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Tell a trusted adult about anything unsafe", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g5-l22": {
        "data_table": table(["Cold Weather Rule", "Why"], [
            ["Dress in layers", "Traps warm air"], ["Cover exposed skin", "Prevents frostbite"],
        ]),
    },
    "survival-skills-g5-l23": {
        "data_table": table(["Heat Safety Rule", "Why"], [
            ["Drink water regularly", "Prevents dehydration"], ["Rest in the shade", "Prevents heat exhaustion"],
        ]),
    },
    "survival-skills-g5-l24": {
        "data_table": table(["Sign of Choking", "Response"], [
            ["Can't speak or cough", "Get help from an adult immediately"],
        ]),
    },
    "survival-skills-g5-l25": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Meeting point", "Where family reunites if separated"], ["Emergency contact", "Someone to call for updates"],
        ]),
    },
    "survival-skills-g5-l26": {
        "data_table": table(["Rule", "Why"], [
            ["Move to higher ground", "Floodwater rises quickly"], ["Avoid walking through moving water", "Water can sweep you away"],
        ]),
    },
    "survival-skills-g5-l27": {
        "data_table": table(["Rule", "Why"], [
            ["Keep a safe distance from wild animals", "Prevents provoking them"],
            ["Never feed wild animals", "Keeps them from relying on humans"],
        ]),
    },
    "survival-skills-g5-l28": {
        "data_table": table(["Navigation Method", "How It Works"], [
            ["Sun position", "Rises in the east, sets in the west"], ["Moss on trees", "Often grows more on the shaded side"],
        ]),
    },
    "survival-skills-g5-l29": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Emergency kit", "Supplies ready in advance"], ["Practice drills", "Ensures everyone knows what to do"],
        ]),
    },
    "survival-skills-g5-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Staying put", "Makes it easier for searchers to find a lost person"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Survival Skills lessons (completing 30/30).")


if __name__ == "__main__":
    main()
