#!/usr/bin/env python3
"""Depth pass, Grade 9 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 48 Grade 9 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 9 PE to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Exercise physiology", "The study of how the body responds to physical activity"],
        ]),
    },
    "physical-education-self-defense-g9-l2": {
        "data_table": table(["Component", "Example"], [
            ["Cardiovascular endurance", "Running"], ["Muscular strength", "Weightlifting"], ["Flexibility", "Stretching"],
        ]),
    },
    "physical-education-self-defense-g9-l3": {
        "data_table": table(["Phase", "Purpose"], [
            ["Warm-up", "Prepares muscles and raises heart rate gradually"], ["Cool-down", "Gradually lowers heart rate and aids recovery"],
        ]),
    },
    "physical-education-self-defense-g9-l4": {
        "data_table": table(["Activity", "Benefit"], [
            ["Running", "Improves heart and lung capacity"],
        ]),
    },
    "physical-education-self-defense-g9-l5": {
        "data_table": table(["Principle", "Meaning"], [
            ["Progressive overload", "Gradually increasing resistance to build strength"],
        ]),
    },
    "physical-education-self-defense-g9-l6": {
        "data_table": table(["Type", "Example"], [
            ["Static stretching", "Holding a stretch position"], ["Dynamic stretching", "Moving stretches, like leg swings"],
        ]),
    },
    "physical-education-self-defense-g9-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"], ["Free throw", "Unopposed shot worth one point"],
        ]),
    },
    "physical-education-self-defense-g9-l9": {
        "data_table": table(["Skill", "Description"], [
            ["Passing", "Moving the ball to a teammate"], ["Dribbling", "Controlling the ball with the feet"],
        ]),
    },
    "physical-education-self-defense-g9-l10": {
        "data_table": table(["Skill", "Description"], [
            ["Serve", "Puts the ball in play"], ["Bump/pass", "Directs the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g9-l11": {
        "data_table": table(["Event Type", "Example"], [
            ["Track event", "100m sprint"], ["Field event", "Long jump"],
        ]),
    },
    "physical-education-self-defense-g9-l12": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Fastest competitive stroke"], ["Breaststroke", "Frog-kick stroke"],
        ]),
    },
    "physical-education-self-defense-g9-l13": {
        "data_table": table(["Event", "Description"], [
            ["Floor exercise", "Tumbling routine on a mat"], ["Balance beam", "Routine on a narrow beam"],
        ]),
    },
    "physical-education-self-defense-g9-l15": {
        "data_table": table(["Skill", "Description"], [
            ["Forehand", "Basic offensive shot"], ["Serve", "Starts the point"],
        ]),
    },
    "physical-education-self-defense-g9-l16": {
        "data_table": table(["Pose", "Benefit"], [
            ["Downward dog", "Stretches hamstrings and shoulders"],
        ]),
    },
    "physical-education-self-defense-g9-l17": {
        "data_table": table(["Skill", "Benefit"], [
            ["Communication", "Coordinates team strategy"],
        ]),
    },
    "physical-education-self-defense-g9-l18": {
        "data_table": table(["Value", "Meaning"], [
            ["Sportsmanship", "Treating opponents and officials with respect"],
        ]),
    },
    "physical-education-self-defense-g9-l19": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces the rules of the game"],
        ]),
    },
    "physical-education-self-defense-g9-l20": {
        "data_table": table(["Practice", "Reason"], [
            ["Proper warm-up", "Reduces the risk of muscle strain"],
        ]),
    },
    "physical-education-self-defense-g9-l21": {
        "data_table": table(["Method", "Use"], [
            ["RICE (Rest, Ice, Compression, Elevation)", "Initial treatment for sprains and strains"],
        ]),
    },
    "physical-education-self-defense-g9-l22": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness first", "Avoiding danger is safer than confronting it"],
        ]),
    },
    "physical-education-self-defense-g9-l23": {
        "data_table": table(["Principle", "Meaning"], [
            ["Avoidance", "The best self-defense is avoiding dangerous situations"],
        ]),
    },
    "physical-education-self-defense-g9-l24": {
        "data_table": table(["Technique", "Purpose"], [
            ["Blocking", "Deflects an incoming strike"],
        ]),
    },
    "physical-education-self-defense-g9-l25": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wrist escape", "Breaks free from a wrist grab"],
        ]),
    },
    "physical-education-self-defense-g9-l26": {
        "data_table": table(["Style", "Origin"], [
            ["Karate", "Japan"], ["Taekwondo", "Korea"], ["Judo", "Japan"],
        ]),
    },
    "physical-education-self-defense-g9-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Judo", "Japanese martial art emphasizing throws and grappling"],
        ]),
    },
    "physical-education-self-defense-g9-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Karate", "Japanese striking martial art using punches and kicks"],
        ]),
    },
    "physical-education-self-defense-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Taekwondo", "Korean martial art known for kicking techniques"],
        ]),
    },
    "physical-education-self-defense-g9-l30": {
        "data_table": table(["Safety Rule", "Reason"], [
            ["Wear headgear and gloves", "Reduces injury risk"],
        ]),
    },
    "physical-education-self-defense-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Takedown", "Bringing an opponent to the ground"],
        ]),
    },
    "physical-education-self-defense-g9-l32": {
        "data_table": table(["Principle", "Meaning"], [
            ["Personal boundaries", "The limits a person sets for physical and emotional space"],
        ]),
    },
    "physical-education-self-defense-g9-l33": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Tell a trusted adult", "Gets support in stopping bullying"],
        ]),
    },
    "physical-education-self-defense-g9-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Exercise", "Releases endorphins that reduce stress"],
        ]),
    },
    "physical-education-self-defense-g9-l35": {
        "data_table": table(["Principle", "Meaning"], [
            ["SMART goals", "Specific, Measurable, Achievable, Relevant, Time-bound"],
        ]),
    },
    "physical-education-self-defense-g9-l36": {
        "data_table": table(["Zone", "Purpose"], [
            ["Target heart rate zone", "Range for effective cardio training"],
        ]),
    },
    "physical-education-self-defense-g9-l37": {
        "data_table": table(["Muscle", "Movement"], [
            ["Biceps", "Bends the elbow"], ["Quadriceps", "Extends the knee"],
        ]),
    },
    "physical-education-self-defense-g9-l38": {
        "data_table": table(["Bone", "Location"], [
            ["Femur", "Thigh, the longest bone in the body"],
        ]),
    },
    "physical-education-self-defense-g9-l39": {
        "data_table": table(["Practice", "Reason"], [
            ["Good posture", "Reduces strain on the spine"],
        ]),
    },
    "physical-education-self-defense-g9-l40": {
        "data_table": table(["Practice", "Reason"], [
            ["Drinking water before, during, after exercise", "Prevents dehydration"],
        ]),
    },
    "physical-education-self-defense-g9-l41": {
        "data_table": table(["Condition", "Precaution"], [
            ["Extreme heat", "Increase hydration, avoid peak sun hours"],
        ]),
    },
    "physical-education-self-defense-g9-l42": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sports psychology", "Study of the mental factors affecting performance"],
        ]),
    },
    "physical-education-self-defense-g9-l43": {
        "data_table": table(["Skill", "Benefit"], [
            ["Clear communication", "Improves team coordination"],
        ]),
    },
    "physical-education-self-defense-g9-l44": {
        "data_table": table(["Activity", "Benefit"], [
            ["Hiking", "Builds endurance and connects with nature"],
        ]),
    },
    "physical-education-self-defense-g9-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Dance", "Improves cardiovascular fitness and coordination"],
        ]),
    },
    "physical-education-self-defense-g9-l46": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reading trail markers", "Prevents getting lost"],
        ]),
    },
    "physical-education-self-defense-g9-l47": {
        "data_table": table(["Practice", "Reason"], [
            ["Wear a helmet", "Reduces head injury risk while cycling"],
        ]),
    },
    "physical-education-self-defense-g9-l48": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reach-throw-row-go", "Order of priority for helping someone in water, safest first"],
        ]),
    },
    "physical-education-self-defense-g9-l49": {
        "data_table": table(["Step", "Purpose"], [
            ["Set goals", "Provides direction for a fitness plan"],
        ]),
    },
    "physical-education-self-defense-g9-l50": {
        "data_table": table(["Value", "Meaning"], [
            ["Inclusion", "Welcoming participants of all backgrounds and abilities in sports"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 PE lessons (completing 50/50).")


if __name__ == "__main__":
    main()
