#!/usr/bin/env python3
"""Depth pass, Grade 7 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 38 Grade 7 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 7 PE to full
40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g7-l1": {
        "data_table": table(["Fitness Test", "Measures"], [
            ["Beep test", "Cardiovascular endurance"], ["Sit and reach", "Flexibility"],
        ]),
    },
    "physical-education-self-defense-g7-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"], ["Cool-down", "Gradually lowers heart rate"],
        ]),
    },
    "physical-education-self-defense-g7-l3": {
        "data_table": table(["Activity", "Benefit"], [
            ["Jogging", "Builds endurance"], ["Swimming", "Builds cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g7-l4": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Push-ups", "Chest and arms"], ["Squats", "Legs and glutes"],
        ]),
    },
    "physical-education-self-defense-g7-l5": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g7-l6": {
        "data_table": table(["Exercise", "Muscle Group"], [
            ["Plank", "Core"], ["Wall sit", "Legs"],
        ]),
    },
    "physical-education-self-defense-g7-l7": {
        "data_table": table(["Skill", "Example Activity"], [
            ["Balance", "Standing on one foot"], ["Coordination", "Bouncing and catching a ball"],
        ]),
    },
    "physical-education-self-defense-g7-l8": {
        "data_table": table(["Drill", "Skill Built"], [
            ["Shuttle run", "Speed and agility"], ["Cone weave", "Coordination"],
        ]),
    },
    "physical-education-self-defense-g7-l10": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Moving the ball with the feet"], ["Passing", "Kicking the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g7-l11": {
        "data_table": table(["Skill", "Description"], [
            ["Bump", "Passing the ball with forearms"], ["Serve", "Starting play by hitting the ball over the net"],
        ]),
    },
    "physical-education-self-defense-g7-l13": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Alternating arm strokes with a flutter kick"], ["Backstroke", "Swum on the back"],
        ]),
    },
    "physical-education-self-defense-g7-l14": {
        "data_table": table(["Movement", "Skill"], [
            ["Forward roll", "Balance and coordination"], ["Cartwheel", "Balance and body control"],
        ]),
    },
    "physical-education-self-defense-g7-l15": {
        "data_table": table(["Dance Element", "Example"], [
            ["Rhythm", "Moving in time with the music"], ["Coordination", "Combining multiple movements smoothly"],
        ]),
    },
    "physical-education-self-defense-g7-l16": {
        "data_table": table(["Pose", "Focus"], [
            ["Tree pose", "Balance"], ["Child's pose", "Relaxation and stretching"],
        ]),
    },
    "physical-education-self-defense-g7-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Wear a helmet", "Protects your head in a fall"], ["Follow traffic signals", "Keeps you safe around vehicles"],
        ]),
    },
    "physical-education-self-defense-g7-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Stay on marked trails", "Reduces risk of getting lost"], ["Wear appropriate footwear", "Prevents injury"],
        ]),
    },
    "physical-education-self-defense-g7-l19": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"], ["Good sportsmanship", "Congratulating the winner"],
        ]),
    },
    "physical-education-self-defense-g7-l20": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces the rules during play"], ["Player", "Follows the rules and plays fairly"],
        ]),
    },
    "physical-education-self-defense-g7-l21": {
        "data_table": table(["Leadership Trait", "Example"], [
            ["Communication", "Directing teammates clearly"], ["Encouragement", "Motivating others"],
        ]),
    },
    "physical-education-self-defense-g7-l22": {
        "data_table": table(["Prevention Tip", "Why"], [
            ["Warm up before activity", "Prepares muscles and reduces injury risk"],
            ["Use proper form", "Avoids strain"],
        ]),
    },
    "physical-education-self-defense-g7-l23": {
        "data_table": table(["RICE Step", "Meaning"], [
            ["Rest", "Avoid using the injured area"], ["Ice", "Reduces swelling"],
            ["Compression", "Wraps to reduce swelling"], ["Elevation", "Raises the area to reduce swelling"],
        ]),
    },
    "physical-education-self-defense-g7-l24": {
        "data_table": table(["Nutrient", "Function"], [
            ["Carbohydrates", "Provides energy"], ["Protein", "Builds and repairs muscle"],
        ]),
    },
    "physical-education-self-defense-g7-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
            ["General guidance", "Drink water throughout the day, more when active"],
        ]),
    },
    "physical-education-self-defense-g7-l26": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "physical-education-self-defense-g7-l27": {
        "data_table": table(["Body Mechanic", "Purpose"], [
            ["Good posture", "Reduces strain on the spine"], ["Proper lifting form", "Prevents back injury"],
        ]),
    },
    "physical-education-self-defense-g7-l28": {
        "data_table": table(["Body System", "Exercise Effect"], [
            ["Cardiovascular system", "Heart pumps more efficiently"], ["Muscular system", "Muscles grow stronger"],
        ]),
    },
    "physical-education-self-defense-g7-l29": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sports psychology", "The study of how mental factors affect athletic performance"],
        ]),
    },
    "physical-education-self-defense-g7-l30": {
        "data_table": table(["Benefit", "Detail"], [
            ["Exercise and mood", "Regular activity can reduce stress and anxiety"],
        ]),
    },
    "physical-education-self-defense-g7-l31": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness", "Noticing your surroundings"], ["Avoidance", "Staying away from risky situations"],
        ]),
    },
    "physical-education-self-defense-g7-l32": {
        "data_table": table(["Concept", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings and potential risks"],
        ]),
    },
    "physical-education-self-defense-g7-l33": {
        "data_table": table(["Martial Art", "Origin"], [
            ["Karate", "Japan"], ["Taekwondo", "Korea"],
        ]),
    },
    "physical-education-self-defense-g7-l34": {
        "data_table": table(["Concept", "Meaning"], [
            ["Personal boundary", "A limit on what you're comfortable with"], ["Saying no", "A clear way to protect your boundary"],
        ]),
    },
    "physical-education-self-defense-g7-l35": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Staying calm", "Reduces escalation"], ["Walking away", "Avoids confrontation"],
        ]),
    },
    "physical-education-self-defense-g7-l36": {
        "data_table": table(["Step", "Action"], [
            ["Tell a trusted adult", "Reports the behavior"], ["Support the person being bullied", "Reduces isolation"],
        ]),
    },
    "physical-education-self-defense-g7-l37": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Positive self-talk", "Improves focus under pressure"],
        ]),
    },
    "physical-education-self-defense-g7-l38": {
        "data_table": table(["Trait", "Meaning"], [
            ["Resilience", "Bouncing back from setbacks"], ["Healthy competition", "Striving to improve without harming others"],
        ]),
    },
    "physical-education-self-defense-g7-l39": {
        "data_table": table(["Skill", "Purpose"], [
            ["Communication", "Coordinates the whole team"], ["Cooperation", "Builds trust between teammates"],
        ]),
    },
    "physical-education-self-defense-g7-l40": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Goal setting", "Defines what to work toward"], ["Weekly schedule", "Structures the training routine"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 PE lessons (completing 40/40).")


if __name__ == "__main__":
    main()
