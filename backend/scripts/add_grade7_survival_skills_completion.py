#!/usr/bin/env python3
"""Depth pass, Grade 7 Survival Skills: fill in real, hand-checked
data_table content for the 38 Grade 7 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Survival
Skills to full 40/40 coverage.

Content covers standard, uncontroversial safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g7-l1": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Small cut", "Clean it and cover with a bandage"], ["Sprain", "Rest, ice, compression, elevation"],
        ]),
    },
    "survival-skills-g7-l3": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of equal thickness"], ["Bowline", "Creates a secure loop"],
        ]),
    },
    "survival-skills-g7-l4": {
        "data_table": table(["Rule", "Why"], [
            ["Clear the area around the fire", "Prevents spreading"], ["Fully extinguish before leaving", "Prevents reignition"],
        ]),
    },
    "survival-skills-g7-l5": {
        "data_table": table(["Shelter Type", "Material"], [
            ["Lean-to", "Branches leaned against a support"], ["Debris hut", "Leaves and branches for insulation"],
        ]),
    },
    "survival-skills-g7-l6": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Kills most pathogens after a full rolling boil"], ["Filtration", "Removes particles and some microbes"],
        ]),
    },
    "survival-skills-g7-l7": {
        "data_table": table(["Rule", "Why"], [
            ["Keep food sealed", "Prevents contamination and attracting wildlife"],
            ["Cook food thoroughly", "Kills harmful bacteria"],
        ]),
    },
    "survival-skills-g7-l8": {
        "data_table": table(["Plant", "Rule"], [
            ["Poison ivy", "Leaves of three, let it be"],
        ]),
    },
    "survival-skills-g7-l9": {
        "data_table": table(["Sign", "Possible Meaning"], [
            ["Dark, towering clouds", "Possible thunderstorm"], ["Sudden calm and stillness", "Storm may be approaching"],
        ]),
    },
    "survival-skills-g7-l10": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Flashlight", "Provides light during a power outage"], ["Water", "Prevents dehydration"],
        ]),
    },
    "survival-skills-g7-l11": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three whistle blasts", "Universal distress signal"], ["Mirror flash", "Can be seen from far away"],
        ]),
    },
    "survival-skills-g7-l12": {
        "data_table": table(["Rule", "Why"], [
            ["Stay on marked trails", "Reduces risk of getting lost"], ["Tell someone your plans", "Helps others find you if needed"],
        ]),
    },
    "survival-skills-g7-l13": {
        "data_table": table(["Leave No Trace Principle", "Meaning"], [
            ["Pack it in, pack it out", "Take your trash with you"],
        ]),
    },
    "survival-skills-g7-l14": {
        "data_table": table(["Rule", "Why"], [
            ["Keep a safe distance from wild animals", "Prevents provoking them"],
            ["Never feed wild animals", "Keeps them from relying on humans"],
        ]),
    },
    "survival-skills-g7-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Cook food fully before eating", "Kills harmful bacteria"],
            ["Keep a safe distance from the fire", "Prevents burns"],
        ]),
    },
    "survival-skills-g7-l16": {
        "data_table": table(["Sign", "Meaning"], [
            ["Difficulty breathing", "Possible serious medical emergency"], ["Unresponsiveness", "Requires immediate emergency care"],
        ]),
    },
    "survival-skills-g7-l18": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Minor burn", "Cool water, then cover loosely"], ["Cut", "Clean and apply pressure to stop bleeding"],
        ]),
    },
    "survival-skills-g7-l19": {
        "data_table": table(["Sign of Choking", "Response"], [
            ["Can't speak or cough", "Get help from an adult immediately"],
        ]),
    },
    "survival-skills-g7-l20": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Checks for oncoming traffic"],
            ["Cross at a crosswalk", "Safest place for drivers to see you"],
        ]),
    },
    "survival-skills-g7-l21": {
        "data_table": table(["Rule", "Why"], [
            ["Know two ways out of every room", "Ensures an escape route if one is blocked"],
            ["Have a meeting point outside", "Confirms everyone got out safely"],
        ]),
    },
    "survival-skills-g7-l22": {
        "data_table": table(["Drill Step", "Action"], [
            ["Drop", "Get down on hands and knees"], ["Cover", "Protect head and neck"],
        ]),
    },
    "survival-skills-g7-l23": {
        "data_table": table(["Rule", "Why"], [
            ["Move to higher ground", "Floodwater rises quickly"], ["Avoid walking through moving water", "Water can sweep you away"],
        ]),
    },
    "survival-skills-g7-l24": {
        "data_table": table(["Hazard", "Safety Rule"], [
            ["Lightning", "Avoid open areas and tall isolated objects"], ["Thunder heard", "Go indoors immediately"],
        ]),
    },
    "survival-skills-g7-l25": {
        "data_table": table(["Sun Safety Tip", "Why"], [
            ["Wear sunscreen", "Protects skin from UV rays"], ["Drink water regularly", "Prevents heat illness"],
        ]),
    },
    "survival-skills-g7-l26": {
        "data_table": table(["Cold Weather Rule", "Why"], [
            ["Dress in layers", "Traps warm air"], ["Cover exposed skin", "Prevents frostbite"],
        ]),
    },
    "survival-skills-g7-l27": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"], ["Reach or throw, don't go", "Avoid entering the water yourself"],
        ]),
    },
    "survival-skills-g7-l28": {
        "data_table": table(["Rule", "Why"], [
            ["Never go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if approached", "Helps adults protect you"],
        ]),
    },
    "survival-skills-g7-l29": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
        ]),
    },
    "survival-skills-g7-l30": {
        "data_table": table(["Skill", "Use"], [
            ["Basic stitch", "Repairing a small tear in fabric or gear"],
        ]),
    },
    "survival-skills-g7-l31": {
        "data_table": table(["Habit", "Why"], [
            ["Regular handwashing", "Reduces illness even outdoors"],
        ]),
    },
    "survival-skills-g7-l32": {
        "data_table": table(["Tool", "Use"], [
            ["Compass", "Points to magnetic north"], ["Topographic map", "Shows elevation and terrain"],
        ]),
    },
    "survival-skills-g7-l33": {
        "data_table": table(["Rule", "Why"], [
            ["Use tools only for their intended purpose", "Reduces injury risk"],
        ]),
    },
    "survival-skills-g7-l34": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["First aid supplies", "Treats minor injuries"], ["Water and food", "Sustains basic needs"],
        ]),
    },
    "survival-skills-g7-l35": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Meeting point", "Where family reunites if separated"], ["Emergency contact", "Someone to call for updates"],
        ]),
    },
    "survival-skills-g7-l36": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Working together", "Combines skills and resources"], ["Clear communication", "Reduces confusion in emergencies"],
        ]),
    },
    "survival-skills-g7-l37": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Deep breathing", "Calms the body"], ["Positive self-talk", "Helps maintain focus under stress"],
        ]),
    },
    "survival-skills-g7-l38": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "survival-skills-g7-l39": {
        "data_table": table(["Technique", "Purpose"], [
            ["Staying calm", "Improves decision-making in danger"],
        ]),
    },
    "survival-skills-g7-l40": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Emergency kit", "Supplies ready in advance"], ["Practice drills", "Ensures everyone knows what to do"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Survival Skills lessons (completing 40/40).")


if __name__ == "__main__":
    main()
