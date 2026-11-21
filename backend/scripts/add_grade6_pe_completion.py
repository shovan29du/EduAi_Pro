#!/usr/bin/env python3
"""Depth pass, Grade 6 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 28 Grade 6 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 6 PE to full
30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g6-l1": {
        "data_table": table(["Event", "Skill"], [
            ["Sprint", "Speed"], ["Relay", "Teamwork and speed"],
        ]),
    },
    "physical-education-self-defense-g6-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"], ["Stretch", "Improves flexibility, reduces injury risk"],
        ]),
    },
    "physical-education-self-defense-g6-l3": {
        "data_table": table(["Activity", "Benefit"], [
            ["Jogging", "Builds endurance"], ["Swimming", "Builds cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g6-l4": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Push-ups", "Chest and arms"], ["Sit-ups", "Core"],
        ]),
    },
    "physical-education-self-defense-g6-l5": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g6-l7": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Moving the ball with the feet"], ["Passing", "Kicking the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g6-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Bump", "Passing the ball with forearms"], ["Serve", "Starting play by hitting the ball over the net"],
        ]),
    },
    "physical-education-self-defense-g6-l9": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Alternating arm strokes with a flutter kick"], ["Backstroke", "Swum on the back"],
        ]),
    },
    "physical-education-self-defense-g6-l10": {
        "data_table": table(["Movement", "Skill"], [
            ["Forward roll", "Balance and coordination"], ["Cartwheel", "Balance and body control"],
        ]),
    },
    "physical-education-self-defense-g6-l12": {
        "data_table": table(["Event", "Skill"], [
            ["Shot put", "Power and technique"], ["Discus throw", "Rotational power"],
        ]),
    },
    "physical-education-self-defense-g6-l13": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness", "Noticing your surroundings"], ["Avoidance", "Staying away from risky situations"],
        ]),
    },
    "physical-education-self-defense-g6-l14": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "physical-education-self-defense-g6-l15": {
        "data_table": table(["Technique", "Purpose"], [
            ["Basic block", "Protects the body from a strike"], ["Evasion", "Moving out of the way of a threat"],
        ]),
    },
    "physical-education-self-defense-g6-l16": {
        "data_table": table(["Skill", "Example Activity"], [
            ["Balance", "Standing on one foot"], ["Core stability", "Plank exercises"],
        ]),
    },
    "physical-education-self-defense-g6-l17": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"], ["Good sportsmanship", "Congratulating the winner"],
        ]),
    },
    "physical-education-self-defense-g6-l18": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces the rules during play"], ["Player", "Follows the rules and plays fairly"],
        ]),
    },
    "physical-education-self-defense-g6-l19": {
        "data_table": table(["Prevention Tip", "Why"], [
            ["Warm up before activity", "Prepares muscles and reduces injury risk"],
            ["Use proper form", "Avoids strain"],
        ]),
    },
    "physical-education-self-defense-g6-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Slow walking", "Gradually lowers heart rate"], ["Stretching", "Reduces muscle soreness"],
        ]),
    },
    "physical-education-self-defense-g6-l21": {
        "data_table": table(["Nutrient", "Function"], [
            ["Carbohydrates", "Provides energy"], ["Protein", "Builds and repairs muscle"],
        ]),
    },
    "physical-education-self-defense-g6-l22": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Run a mile without stopping this month"], ["Long-term", "Complete a 5K race this year"],
        ]),
    },
    "physical-education-self-defense-g6-l23": {
        "data_table": table(["Pose", "Focus"], [
            ["Tree pose", "Balance"], ["Child's pose", "Relaxation and stretching"],
        ]),
    },
    "physical-education-self-defense-g6-l24": {
        "data_table": table(["Martial Art", "Origin"], [
            ["Karate", "Japan"], ["Taekwondo", "Korea"], ["Judo", "Japan"],
        ]),
    },
    "physical-education-self-defense-g6-l25": {
        "data_table": table(["Safety Rule", "Why"], [
            ["Only practice with a trained coach", "Reduces injury risk"], ["Stop when told", "Prevents accidents"],
        ]),
    },
    "physical-education-self-defense-g6-l26": {
        "data_table": table(["Dance Element", "Example"], [
            ["Rhythm", "Moving in time with the music"], ["Coordination", "Combining multiple movements smoothly"],
        ]),
    },
    "physical-education-self-defense-g6-l27": {
        "data_table": table(["Activity", "Skill Built"], [
            ["Human knot", "Problem-solving and communication"], ["Trust walk", "Trust and cooperation"],
        ]),
    },
    "physical-education-self-defense-g6-l28": {
        "data_table": table(["Step", "Action"], [
            ["Tell a trusted adult", "Reports the behavior"], ["Support the person being bullied", "Reduces isolation"],
        ]),
    },
    "physical-education-self-defense-g6-l29": {
        "data_table": table(["Body Mechanic", "Purpose"], [
            ["Good posture", "Reduces strain on the spine"], ["Proper lifting form", "Prevents back injury"],
        ]),
    },
    "physical-education-self-defense-g6-l30": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular exercise", "Improves long-term health"], ["Consistent sleep", "Supports recovery and growth"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 PE lessons (completing 30/30).")


if __name__ == "__main__":
    main()
