#!/usr/bin/env python3
"""Depth pass, Grade 10 Physical Education & Self-Defense: fill in
real, hand-checked data_table content for the Grade 10 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 10 PE to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g10-l1": {
        "data_table": table(["Skill", "Benefit"], [
            ["Clear communication", "Improves team coordination"],
        ]),
    },
    "physical-education-self-defense-g10-l2": {
        "data_table": table(["Component", "Example"], [
            ["Cardiovascular endurance", "Running"], ["Muscular strength", "Weightlifting"],
        ]),
    },
    "physical-education-self-defense-g10-l3": {
        "data_table": table(["Component", "Example"], [
            ["Flexibility", "Stretching"], ["Body composition", "Ratio of fat to lean mass"],
        ]),
    },
    "physical-education-self-defense-g10-l4": {
        "data_table": table(["Phase", "Purpose"], [
            ["Warm-up", "Prepares muscles and raises heart rate gradually"], ["Cool-down", "Gradually lowers heart rate and aids recovery"],
        ]),
    },
    "physical-education-self-defense-g10-l5": {
        "data_table": table(["Principle", "Meaning"], [
            ["Progressive overload", "Gradually increasing resistance to build strength"],
        ]),
    },
    "physical-education-self-defense-g10-l6": {
        "data_table": table(["Activity", "Benefit"], [
            ["Running", "Improves heart and lung capacity"],
        ]),
    },
    "physical-education-self-defense-g10-l7": {
        "data_table": table(["Type", "Example"], [
            ["Static stretching", "Holding a stretch position"], ["Dynamic stretching", "Moving stretches, like leg swings"],
        ]),
    },
    "physical-education-self-defense-g10-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"], ["Free throw", "Unopposed shot worth one point"],
        ]),
    },
    "physical-education-self-defense-g10-l9": {
        "data_table": table(["Skill", "Description"], [
            ["Passing", "Moving the ball to a teammate"], ["Offside rule", "Restricts attacking positioning without the ball"],
        ]),
    },
    "physical-education-self-defense-g10-l10": {
        "data_table": table(["Skill", "Description"], [
            ["Serve", "Puts the ball in play"], ["Bump/pass", "Directs the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g10-l12": {
        "data_table": table(["Skill", "Description"], [
            ["Forehand", "Basic offensive shot"], ["Serve", "Starts the point"],
        ]),
    },
    "physical-education-self-defense-g10-l13": {
        "data_table": table(["Event Type", "Example"], [
            ["Track event", "100m sprint"], ["Field event", "Long jump"],
        ]),
    },
    "physical-education-self-defense-g10-l14": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Fastest competitive stroke"], ["Breaststroke", "Frog-kick stroke"],
        ]),
    },
    "physical-education-self-defense-g10-l15": {
        "data_table": table(["Event", "Description"], [
            ["Floor exercise", "Tumbling routine on a mat"], ["Balance beam", "Routine on a narrow beam"],
        ]),
    },
    "physical-education-self-defense-g10-l16": {
        "data_table": table(["Pose", "Benefit"], [
            ["Downward dog", "Stretches hamstrings and shoulders"],
        ]),
    },
    "physical-education-self-defense-g10-l17": {
        "data_table": table(["Skill", "Benefit"], [
            ["Cooperative play", "Builds trust and coordination among teammates"],
        ]),
    },
    "physical-education-self-defense-g10-l18": {
        "data_table": table(["Principle", "Meaning"], [
            ["SMART goals", "Specific, Measurable, Achievable, Relevant, Time-bound"],
        ]),
    },
    "physical-education-self-defense-g10-l20": {
        "data_table": table(["Practice", "Reason"], [
            ["Drinking water before, during, after exercise", "Prevents dehydration"],
        ]),
    },
    "physical-education-self-defense-g10-l21": {
        "data_table": table(["Practice", "Reason"], [
            ["Proper warm-up", "Reduces the risk of muscle strain"],
        ]),
    },
    "physical-education-self-defense-g10-l22": {
        "data_table": table(["Method", "Use"], [
            ["RICE (Rest, Ice, Compression, Elevation)", "Initial treatment for sprains and strains"],
        ]),
    },
    "physical-education-self-defense-g10-l23": {
        "data_table": table(["Bone", "Location"], [
            ["Femur", "Thigh, the longest bone in the body"],
        ]),
    },
    "physical-education-self-defense-g10-l24": {
        "data_table": table(["Muscle", "Movement"], [
            ["Biceps", "Bends the elbow"], ["Quadriceps", "Extends the knee"],
        ]),
    },
    "physical-education-self-defense-g10-l25": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness first", "Avoiding danger is safer than confronting it"],
        ]),
    },
    "physical-education-self-defense-g10-l26": {
        "data_table": table(["Stance", "Purpose"], [
            ["Fighting stance", "Balanced posture for quick defensive movement"],
        ]),
    },
    "physical-education-self-defense-g10-l27": {
        "data_table": table(["Principle", "Meaning"], [
            ["Situational awareness", "Continuously observing your environment for risk"],
        ]),
    },
    "physical-education-self-defense-g10-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Calm, non-confrontational tone", "Helps defuse escalating conflict"],
        ]),
    },
    "physical-education-self-defense-g10-l29": {
        "data_table": table(["Style", "Origin"], [
            ["Karate", "Japan"], ["Taekwondo", "Korea"], ["Judo", "Japan"],
        ]),
    },
    "physical-education-self-defense-g10-l30": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wrist escape", "Breaks free from a wrist grab"],
        ]),
    },
    "physical-education-self-defense-g10-l31": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wrist escape", "Breaks free from a wrist grab"],
        ]),
    },
    "physical-education-self-defense-g10-l32": {
        "data_table": table(["Principle", "Meaning"], [
            ["Reasonable force", "Self-defense response should match the level of threat"],
        ]),
    },
    "physical-education-self-defense-g10-l33": {
        "data_table": table(["Benefit", "Detail"], [
            ["Physical training", "Builds discipline and self-assurance"],
        ]),
    },
    "physical-education-self-defense-g10-l34": {
        "data_table": table(["Test", "Measures"], [
            ["Beep test", "Cardiovascular fitness"], ["Push-up test", "Muscular endurance"],
        ]),
    },
    "physical-education-self-defense-g10-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Assess current fitness", "Establishes a baseline for a personal plan"],
        ]),
    },
    "physical-education-self-defense-g10-l36": {
        "data_table": table(["Effect", "Detail"], [
            ["Regular exercise", "Strengthens the heart and improves circulation"],
        ]),
    },
    "physical-education-self-defense-g10-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Exercise", "Releases endorphins that reduce stress"],
        ]),
    },
    "physical-education-self-defense-g10-l38": {
        "data_table": table(["Value", "Meaning"], [
            ["Sportsmanship", "Treating opponents and officials with respect"],
        ]),
    },
    "physical-education-self-defense-g10-l39": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces the rules of the game"],
        ]),
    },
    "physical-education-self-defense-g10-l40": {
        "data_table": table(["Principle", "Meaning"], [
            ["Positive reinforcement", "Effective coaching technique for building skill and confidence"],
        ]),
    },
    "physical-education-self-defense-g10-l41": {
        "data_table": table(["Activity", "Benefit"], [
            ["Hiking", "Builds endurance and connects with nature"],
        ]),
    },
    "physical-education-self-defense-g10-l42": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reading trail markers", "Prevents getting lost while hiking"],
        ]),
    },
    "physical-education-self-defense-g10-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["Dance", "Improves cardiovascular fitness and coordination"],
        ]),
    },
    "physical-education-self-defense-g10-l44": {
        "data_table": table(["Practice", "Reason"], [
            ["Wear a helmet", "Reduces head injury risk while cycling"],
        ]),
    },
    "physical-education-self-defense-g10-l45": {
        "data_table": table(["Risk", "Detail"], [
            ["Performance-enhancing substances", "Carry serious health risks and are banned in most competitive sport"],
        ]),
    },
    "physical-education-self-defense-g10-l46": {
        "data_table": table(["Concept", "Reason"], [
            ["Rest days", "Allow muscles to repair and prevent overtraining"],
        ]),
    },
    "physical-education-self-defense-g10-l47": {
        "data_table": table(["Element", "Purpose"], [
            ["Specific, measurable goal", "Makes athletic goals achievable"],
        ]),
    },
    "physical-education-self-defense-g10-l48": {
        "data_table": table(["Skill", "Benefit"], [
            ["Communication", "Coordinates team strategy"],
        ]),
    },
    "physical-education-self-defense-g10-l49": {
        "data_table": table(["Fact", "Detail"], [
            ["Modern Olympics began", "1896, Athens"],
        ]),
    },
    "physical-education-self-defense-g10-l50": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular physical activity", "Supports lifelong health and wellbeing"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 PE lessons (completing 50/50).")


if __name__ == "__main__":
    main()
