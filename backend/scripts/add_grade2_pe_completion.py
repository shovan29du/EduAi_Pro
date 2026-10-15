#!/usr/bin/env python3
"""Depth pass, Grade 2 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 18 Grade 2 PE lessons not covered
by the earlier breadth-first batch. Brings Grade 2 PE to full 20/20
coverage.

Content covers standard early-childhood motor-skill and safety concepts
with concrete examples -- nothing fabricated or presented as fact when
it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g2-l1": {
        "data_table": table(["Body Movement", "Example"], [
            ["Locomotor movement", "Walking, running, jumping"],
            ["Non-locomotor movement", "Bending, twisting, stretching in place"],
        ]),
    },
    "physical-education-self-defense-g2-l2": {
        "data_table": table(["Movement", "Description"], [
            ["Hop", "Jump on one foot"], ["Skip", "Step and hop, alternating feet"],
            ["Gallop", "Slide one foot forward, then the other follows"],
        ]),
    },
    "physical-education-self-defense-g2-l3": {
        "data_table": table(["Activity", "Skill Developed"], [
            ["Standing on one foot", "Balance"], ["Walking on a line", "Coordination"],
        ]),
    },
    "physical-education-self-defense-g2-l4": {
        "data_table": table(["Skill", "Technique"], [
            ["Throwing", "Step forward, aim, release"], ["Catching", "Watch the ball, use both hands"],
        ]),
    },
    "physical-education-self-defense-g2-l5": {
        "data_table": table(["Skill", "Technique"], [
            ["Kicking", "Use the inside of your foot for control"],
            ["Striking", "Watch the ball and follow through"],
        ]),
    },
    "physical-education-self-defense-g2-l6": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Teamwork", "Working together to win"], ["Communication", "Telling teammates what to do"],
        ]),
    },
    "physical-education-self-defense-g2-l8": {
        "data_table": table(["Phase", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"],
            ["Cool-down", "Lowers heart rate gradually and helps prevent injury"],
        ]),
    },
    "physical-education-self-defense-g2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Personal space", "The area around your body that you keep clear"],
            ["Safe distance", "Enough room to move without bumping into others"],
        ]),
    },
    "physical-education-self-defense-g2-l10": {
        "data_table": table(["Stance", "Purpose"], [
            ["Ready stance", "Feet shoulder-width apart, knees slightly bent"],
            ["Balanced stance", "Keeps you stable and ready to react"],
        ]),
    },
    "physical-education-self-defense-g2-l11": {
        "data_table": table(["Step", "Action"], [
            ["1", "Say 'No' firmly"], ["2", "Walk or run away"], ["3", "Tell a trusted adult right away"],
        ]),
    },
    "physical-education-self-defense-g2-l12": {
        "data_table": table(["Rule", "Why"], [
            ["Don't go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if a stranger approaches", "Helps adults protect you"],
        ]),
    },
    "physical-education-self-defense-g2-l13": {
        "data_table": table(["Technique", "Purpose"], [
            ["Tucking your chin", "Protects your head"], ["Rolling with the fall", "Spreads out the impact"],
        ]),
    },
    "physical-education-self-defense-g2-l14": {
        "data_table": table(["Skill Practiced", "Example"], [
            ["Agility", "Changing direction quickly"], ["Speed", "Running fast to avoid being tagged"],
        ]),
    },
    "physical-education-self-defense-g2-l15": {
        "data_table": table(["Skill", "Description"], [
            ["Basic jump", "Jumping with both feet together"],
            ["Timing", "Jumping as the rope passes under your feet"],
        ]),
    },
    "physical-education-self-defense-g2-l17": {
        "data_table": table(["Activity", "Endurance Benefit"], [
            ["Running games", "Builds cardiovascular stamina"], ["Obstacle courses", "Builds overall endurance"],
        ]),
    },
    "physical-education-self-defense-g2-l18": {
        "data_table": table(["Rule Type", "Example"], [
            ["Safety rule", "No pushing"], ["Fairness rule", "Taking turns"],
        ]),
    },
    "physical-education-self-defense-g2-l19": {
        "data_table": table(["Fair Play Value", "Example"], [
            ["Honesty", "Admitting when you're out in a game"],
            ["Respect", "Congratulating the other team"],
        ]),
    },
    "physical-education-self-defense-g2-l20": {
        "data_table": table(["Block Type", "Purpose"], [
            ["Arm block", "Deflects an incoming strike"], ["Step back and block", "Creates distance and defends"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 PE lessons (completing 20/20).")


if __name__ == "__main__":
    main()
