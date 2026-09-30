#!/usr/bin/env python3
"""Depth pass, Grade 8 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 38 Grade 8 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 8 PE to full
40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g8-l1": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness", "Noticing your surroundings"], ["Avoidance", "Staying away from risky situations"],
        ]),
    },
    "physical-education-self-defense-g8-l2": {
        "data_table": table(["Activity", "Benefit"], [
            ["Jogging", "Builds endurance"], ["Swimming", "Builds cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g8-l3": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Push-ups", "Chest and arms"], ["Squats", "Legs and glutes"],
        ]),
    },
    "physical-education-self-defense-g8-l4": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g8-l5": {
        "data_table": table(["Step", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"], ["Cool-down", "Gradually lowers heart rate"],
        ]),
    },
    "physical-education-self-defense-g8-l6": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"], ["Free throw", "Shooting from the foul line"],
        ]),
    },
    "physical-education-self-defense-g8-l7": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Moving the ball with the feet"], ["Passing", "Kicking the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g8-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Bump", "Passing the ball with forearms"], ["Serve", "Starting play by hitting the ball over the net"],
        ]),
    },
    "physical-education-self-defense-g8-l9": {
        "data_table": table(["Event", "Skill"], [
            ["Sprint", "Speed"], ["Long jump", "Power and technique"],
        ]),
    },
    "physical-education-self-defense-g8-l11": {
        "data_table": table(["Skill", "Description"], [
            ["Serve", "Starts play by hitting the ball into the opponent's area"],
        ]),
    },
    "physical-education-self-defense-g8-l12": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Alternating arm strokes with a flutter kick"], ["Backstroke", "Swum on the back"],
        ]),
    },
    "physical-education-self-defense-g8-l13": {
        "data_table": table(["Skill", "Purpose"], [
            ["Communication", "Coordinates the whole team"], ["Cooperation", "Builds trust between teammates"],
        ]),
    },
    "physical-education-self-defense-g8-l14": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"],
        ]),
    },
    "physical-education-self-defense-g8-l15": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces the rules during play"],
        ]),
    },
    "physical-education-self-defense-g8-l16": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Run a mile without stopping this month"], ["Long-term", "Complete a 5K race this year"],
        ]),
    },
    "physical-education-self-defense-g8-l18": {
        "data_table": table(["Prevention Tip", "Why"], [
            ["Warm up before activity", "Prepares muscles and reduces injury risk"],
        ]),
    },
    "physical-education-self-defense-g8-l19": {
        "data_table": table(["RICE Step", "Meaning"], [
            ["Rest", "Avoid using the injured area"], ["Ice", "Reduces swelling"],
        ]),
    },
    "physical-education-self-defense-g8-l20": {
        "data_table": table(["Skill", "Example Activity"], [
            ["Balance", "Standing on one foot"], ["Coordination", "Bouncing and catching a ball"],
        ]),
    },
    "physical-education-self-defense-g8-l21": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Plank", "Core"], ["Wall sit", "Legs"],
        ]),
    },
    "physical-education-self-defense-g8-l22": {
        "data_table": table(["Stance", "Purpose"], [
            ["Ready stance", "Balanced position for quick response"],
        ]),
    },
    "physical-education-self-defense-g8-l23": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "physical-education-self-defense-g8-l24": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Staying calm", "Reduces escalation"], ["Walking away", "Avoids confrontation"],
        ]),
    },
    "physical-education-self-defense-g8-l25": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wrist escape", "Breaks free from a wrist grab"],
        ]),
    },
    "physical-education-self-defense-g8-l26": {
        "data_table": table(["Concept", "Meaning"], [
            ["Personal boundary", "A limit on what you're comfortable with"], ["Saying no", "A clear way to protect your boundary"],
        ]),
    },
    "physical-education-self-defense-g8-l27": {
        "data_table": table(["Step", "Action"], [
            ["Tell a trusted adult", "Reports the behavior"],
        ]),
    },
    "physical-education-self-defense-g8-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Basic block", "Protects the body from a strike"],
        ]),
    },
    "physical-education-self-defense-g8-l29": {
        "data_table": table(["Technique", "Purpose"], [
            ["Breakfall", "Reduces injury when falling by spreading impact"],
        ]),
    },
    "physical-education-self-defense-g8-l30": {
        "data_table": table(["Pose", "Focus"], [
            ["Tree pose", "Balance"], ["Child's pose", "Relaxation and stretching"],
        ]),
    },
    "physical-education-self-defense-g8-l31": {
        "data_table": table(["Dance Element", "Example"], [
            ["Rhythm", "Moving in time with the music"],
        ]),
    },
    "physical-education-self-defense-g8-l32": {
        "data_table": table(["Fitness Test", "Measures"], [
            ["Beep test", "Cardiovascular endurance"], ["Sit and reach", "Flexibility"],
        ]),
    },
    "physical-education-self-defense-g8-l33": {
        "data_table": table(["Nutrient", "Function"], [
            ["Carbohydrates", "Provides energy"], ["Protein", "Builds and repairs muscle"],
        ]),
    },
    "physical-education-self-defense-g8-l34": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "physical-education-self-defense-g8-l35": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Goal setting", "Defines what to work toward"], ["Weekly schedule", "Structures the training routine"],
        ]),
    },
    "physical-education-self-defense-g8-l36": {
        "data_table": table(["Rule", "Why"], [
            ["Stay on marked trails", "Reduces risk of getting lost"],
        ]),
    },
    "physical-education-self-defense-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Disc golf", "A sport thrown at targets using a flying disc"],
        ]),
    },
    "physical-education-self-defense-g8-l38": {
        "data_table": table(["Movement", "Skill"], [
            ["Forward roll", "Balance and coordination"],
        ]),
    },
    "physical-education-self-defense-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Doping", "Using banned substances to gain an unfair advantage"],
            ["Fair competition", "Competing without illegal performance enhancement"],
        ]),
    },
    "physical-education-self-defense-g8-l40": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular exercise", "Improves long-term health"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 PE lessons (completing 40/40).")


if __name__ == "__main__":
    main()
