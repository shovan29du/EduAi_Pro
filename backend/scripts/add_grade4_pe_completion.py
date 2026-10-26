#!/usr/bin/env python3
"""Depth pass, Grade 4 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 28 Grade 4 PE lessons not
covered by the earlier breadth-first batch. Brings Grade 4 PE to full
30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g4-l1": {
        "data_table": table(["Sportsmanship Trait", "Example"], [
            ["Fair play", "Following the rules"], ["Teamwork", "Passing to teammates"],
        ]),
    },
    "physical-education-self-defense-g4-l2": {
        "data_table": table(["Stretch", "Muscle Group"], [
            ["Toe touch", "Hamstrings"], ["Arm circles", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g4-l3": {
        "data_table": table(["Drill", "Skill Built"], [
            ["Shuttle run", "Speed and agility"], ["Cone weave", "Coordination"],
        ]),
    },
    "physical-education-self-defense-g4-l4": {
        "data_table": table(["Skill", "Key Point"], [
            ["Throwing", "Step forward with the opposite foot"], ["Catching", "Keep eyes on the ball"],
        ]),
    },
    "physical-education-self-defense-g4-l5": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Bending knees on landing", "Absorbs impact and prevents injury"], ["Balance", "Steadying the body"],
        ]),
    },
    "physical-education-self-defense-g4-l6": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"], ["Free throw", "Shooting from the foul line"],
        ]),
    },
    "physical-education-self-defense-g4-l7": {
        "data_table": table(["Skill", "Description"], [
            ["Dribbling", "Moving the ball with the feet"], ["Passing", "Kicking the ball to a teammate"],
        ]),
    },
    "physical-education-self-defense-g4-l8": {
        "data_table": table(["Skill", "Description"], [
            ["Bump", "Passing the ball with forearms"], ["Serve", "Starting play by hitting the ball over the net"],
        ]),
    },
    "physical-education-self-defense-g4-l9": {
        "data_table": table(["Movement", "Skill"], [
            ["Forward roll", "Balance and coordination"], ["Cartwheel", "Balance and body control"],
        ]),
    },
    "physical-education-self-defense-g4-l10": {
        "data_table": table(["Pose", "Focus"], [
            ["Tree pose", "Balance"], ["Child's pose", "Relaxation and stretching"],
        ]),
    },
    "physical-education-self-defense-g4-l11": {
        "data_table": table(["Stroke", "Description"], [
            ["Freestyle", "Alternating arm strokes with a flutter kick"], ["Backstroke", "Swum on the back"],
        ]),
    },
    "physical-education-self-defense-g4-l12": {
        "data_table": table(["Concept", "Meaning"], [
            ["Awareness", "Noticing your surroundings"], ["Avoidance", "Staying away from risky situations"],
        ]),
    },
    "physical-education-self-defense-g4-l13": {
        "data_table": table(["Concept", "Meaning"], [
            ["Safe distancing", "Keeping physical space from a threat"], ["Saying no", "A clear way to protect a boundary"],
        ]),
    },
    "physical-education-self-defense-g4-l14": {
        "data_table": table(["Activity", "Skill Built"], [
            ["Human knot", "Problem-solving and communication"], ["Trust walk", "Trust and cooperation"],
        ]),
    },
    "physical-education-self-defense-g4-l15": {
        "data_table": table(["Event", "Skill"], [
            ["Sprint", "Speed"], ["Long jump", "Power and technique"],
        ]),
    },
    "physical-education-self-defense-g4-l16": {
        "data_table": table(["Skill", "Benefit"], [
            ["Jump rope", "Builds coordination and cardiovascular fitness"],
        ]),
    },
    "physical-education-self-defense-g4-l17": {
        "data_table": table(["Value", "Example"], [
            ["Fair play", "Following the rules even when it's hard"], ["Good sportsmanship", "Congratulating the winner"],
        ]),
    },
    "physical-education-self-defense-g4-l18": {
        "data_table": table(["Stance", "Purpose"], [
            ["Ready stance", "Balanced position for quick response"], ["Discipline", "Following rules and respecting others"],
        ]),
    },
    "physical-education-self-defense-g4-l19": {
        "data_table": table(["Fitness Component", "Example"], [
            ["Endurance", "Running for a longer time without stopping"], ["Strength", "Doing push-ups"],
        ]),
    },
    "physical-education-self-defense-g4-l20": {
        "data_table": table(["Etiquette Rule", "Why"], [
            ["Shake hands after a game", "Shows respect for opponents"], ["Follow the referee's calls", "Maintains fair play"],
        ]),
    },
    "physical-education-self-defense-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Team sports", "Applying fair play in a weekend match"],
        ]),
    },
    "physical-education-self-defense-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Before exercise", "Stretching to prevent injury"],
        ]),
    },
    "physical-education-self-defense-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Running a race", "Using agility drills to improve speed"],
        ]),
    },
    "physical-education-self-defense-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Playing catch", "Using proper throwing form"],
        ]),
    },
    "physical-education-self-defense-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Playground play", "Landing safely after jumping"],
        ]),
    },
    "physical-education-self-defense-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Pickup basketball game", "Applying dribbling skills"],
        ]),
    },
    "physical-education-self-defense-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Backyard soccer", "Applying passing and dribbling skills"],
        ]),
    },
    "physical-education-self-defense-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Beach volleyball", "Applying bump and serve skills"],
        ]),
    },
    "physical-education-self-defense-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Gymnastics class", "Practicing forward rolls safely"],
        ]),
    },
    "physical-education-self-defense-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Morning routine", "Practicing yoga poses for calm and balance"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 PE lessons (completing 30/30).")


if __name__ == "__main__":
    main()
