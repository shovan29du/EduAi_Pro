#!/usr/bin/env python3
"""Depth pass, Grade 3 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 18 Grade 3 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 3 PE to full
20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g3-l1": {
        "data_table": table(["Sportsmanship Trait", "Example"], [
            ["Fair play", "Following the rules"], ["Encouragement", "Cheering on teammates"],
        ]),
    },
    "physical-education-self-defense-g3-l2": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g3-l3": {
        "data_table": table(["Activity", "Benefit"], [
            ["Jogging", "Builds endurance"], ["Sprinting", "Builds speed"],
        ]),
    },
    "physical-education-self-defense-g3-l4": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Bending knees on landing", "Absorbs impact and prevents injury"],
        ]),
    },
    "physical-education-self-defense-g3-l5": {
        "data_table": table(["Skill", "Key Point"], [
            ["Throwing", "Step forward with the opposite foot"], ["Catching", "Keep eyes on the ball"],
        ]),
    },
    "physical-education-self-defense-g3-l6": {
        "data_table": table(["Skill", "Key Point"], [
            ["Dribbling", "Use control taps, not hard kicks"], ["Kicking", "Strike with the inside of the foot for accuracy"],
        ]),
    },
    "physical-education-self-defense-g3-l7": {
        "data_table": table(["Skill", "Example Activity"], [
            ["Balance", "Standing on one foot"], ["Coordination", "Bouncing and catching a ball"],
        ]),
    },
    "physical-education-self-defense-g3-l9": {
        "data_table": table(["Skill", "Benefit"], [
            ["Jump rope", "Builds coordination and cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g3-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Awareness", "Noticing your surroundings"], ["Confidence", "Standing tall and speaking firmly"],
        ]),
    },
    "physical-education-self-defense-g3-l11": {
        "data_table": table(["Concept", "Meaning"], [
            ["Personal boundary", "A limit on what you're comfortable with"],
            ["Saying no", "A clear way to protect your boundary"],
        ]),
    },
    "physical-education-self-defense-g3-l12": {
        "data_table": table(["Fitness Component", "Example"], [
            ["Endurance", "Running for a longer time without stopping"],
            ["Strength", "Doing push-ups"],
        ]),
    },
    "physical-education-self-defense-g3-l13": {
        "data_table": table(["Activity", "Skill Built"], [
            ["Human knot", "Problem-solving and communication"], ["Trust walk", "Trust and cooperation"],
        ]),
    },
    "physical-education-self-defense-g3-l14": {
        "data_table": table(["Movement", "Skill"], [
            ["Forward roll", "Balance and coordination"], ["Cartwheel", "Balance and body control"],
        ]),
    },
    "physical-education-self-defense-g3-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Never swim without supervision", "Adults can respond to emergencies"],
        ]),
    },
    "physical-education-self-defense-g3-l16": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"], ["Good sportsmanship", "Congratulating the winner"],
        ]),
    },
    "physical-education-self-defense-g3-l18": {
        "data_table": table(["Playground Rule", "Why"], [
            ["Wait your turn on equipment", "Prevents crowding and injury"],
            ["No pushing", "Prevents falls"],
        ]),
    },
    "physical-education-self-defense-g3-l19": {
        "data_table": table(["Skill", "Purpose"], [
            ["Baton pass", "Smoothly transfers to the next runner"], ["Teamwork", "Coordinates the whole relay team"],
        ]),
    },
    "physical-education-self-defense-g3-l20": {
        "data_table": table(["Cool-Down Step", "Purpose"], [
            ["Slow walking", "Gradually lowers heart rate"], ["Stretching", "Reduces muscle soreness"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 PE lessons (completing 20/20).")


if __name__ == "__main__":
    main()
