#!/usr/bin/env python3
"""Depth pass, Grade 5 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 28 Grade 5 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 5 PE to full
30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g5-l1": {
        "data_table": table(["Fitness Component", "Example"], [
            ["Endurance", "Running for a longer time without stopping"], ["Strength", "Doing push-ups"],
        ]),
    },
    "physical-education-self-defense-g5-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"], ["Cool-down", "Gradually lowers heart rate"],
        ]),
    },
    "physical-education-self-defense-g5-l3": {
        "data_table": table(["Activity", "Benefit"], [
            ["Jogging", "Builds endurance"], ["Swimming", "Builds cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g5-l4": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Push-ups", "Chest and arms"], ["Sit-ups", "Core"],
        ]),
    },
    "physical-education-self-defense-g5-l5": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g5-l6": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"], ["Good sportsmanship", "Congratulating the winner"],
        ]),
    },
    "physical-education-self-defense-g5-l7": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Moving the ball with the feet"], ["Passing", "Kicking the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g5-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"], ["Free throw", "Shooting from the foul line"],
        ]),
    },
    "physical-education-self-defense-g5-l10": {
        "data_table": table(["Event", "Skill"], [
            ["Sprint", "Speed"], ["Long jump", "Power and technique"],
        ]),
    },
    "physical-education-self-defense-g5-l11": {
        "data_table": table(["Rule Type", "Example"], [
            ["Scoring rule", "How points are earned"], ["Foul rule", "What counts as a violation"],
        ]),
    },
    "physical-education-self-defense-g5-l12": {
        "data_table": table(["Skill", "Example Activity"], [
            ["Balance", "Standing on one foot"], ["Coordination", "Bouncing and catching a ball"],
        ]),
    },
    "physical-education-self-defense-g5-l13": {
        "data_table": table(["Skill", "Benefit"], [
            ["Jump rope", "Builds coordination and cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g5-l14": {
        "data_table": table(["Pose", "Focus"], [
            ["Tree pose", "Balance"], ["Child's pose", "Relaxation and stretching"],
        ]),
    },
    "physical-education-self-defense-g5-l15": {
        "data_table": table(["Stance", "Purpose"], [
            ["Ready stance", "Balanced position for quick response"],
        ]),
    },
    "physical-education-self-defense-g5-l16": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "physical-education-self-defense-g5-l17": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Staying calm", "Reduces escalation"], ["Walking away", "Avoids confrontation"],
        ]),
    },
    "physical-education-self-defense-g5-l18": {
        "data_table": table(["Technique", "Purpose"], [
            ["Basic block", "Protects the body from a strike"],
        ]),
    },
    "physical-education-self-defense-g5-l19": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Run a mile without stopping this month"], ["Long-term", "Complete a 5K race this year"],
        ]),
    },
    "physical-education-self-defense-g5-l21": {
        "data_table": table(["Prevention Tip", "Why"], [
            ["Warm up before activity", "Prepares muscles and reduces injury risk"],
            ["Use proper form", "Avoids strain"],
        ]),
    },
    "physical-education-self-defense-g5-l22": {
        "data_table": table(["Activity", "Skill Built"], [
            ["Human knot", "Problem-solving and communication"], ["Trust walk", "Trust and cooperation"],
        ]),
    },
    "physical-education-self-defense-g5-l23": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Alternating arm strokes with a flutter kick"], ["Backstroke", "Swum on the back"],
        ]),
    },
    "physical-education-self-defense-g5-l24": {
        "data_table": table(["Dance Element", "Example"], [
            ["Rhythm", "Moving in time with the music"], ["Coordination", "Combining multiple movements smoothly"],
        ]),
    },
    "physical-education-self-defense-g5-l25": {
        "data_table": table(["Concept", "Meaning"], [
            ["Body awareness", "Understanding where your body is in space"],
        ]),
    },
    "physical-education-self-defense-g5-l26": {
        "data_table": table(["Concept", "Meaning"], [
            ["Personal boundary", "A limit on what you're comfortable with"],
            ["Saying no", "A clear way to protect your boundary"],
        ]),
    },
    "physical-education-self-defense-g5-l27": {
        "data_table": table(["Value", "Meaning"], [
            ["Discipline", "Following rules and respecting others"], ["Respect", "Honoring instructors and training partners"],
        ]),
    },
    "physical-education-self-defense-g5-l28": {
        "data_table": table(["Rule", "Why"], [
            ["Wait your turn on equipment", "Prevents crowding and injury"], ["No pushing", "Prevents falls"],
        ]),
    },
    "physical-education-self-defense-g5-l29": {
        "data_table": table(["Interval Type", "Example"], [
            ["Work interval", "30 seconds of fast running"], ["Rest interval", "30 seconds of walking"],
        ]),
    },
    "physical-education-self-defense-g5-l30": {
        "data_table": table(["Goal-Setting Step", "Purpose"], [
            ["Set a clear team goal", "Gives the team a shared target"], ["Track progress", "Shows how close the team is"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 PE lessons (completing 30/30).")


if __name__ == "__main__":
    main()
