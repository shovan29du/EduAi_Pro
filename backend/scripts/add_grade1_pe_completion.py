#!/usr/bin/env python3
"""Depth pass, Grade 1 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 17 Grade 1 PE lessons not covered
by the earlier breadth-first batch. Brings Grade 1 PE to full 20/20
coverage.

Content covers standard early-childhood motor-skill and safety concepts
with concrete examples -- nothing fabricated or presented as fact when
it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_pe_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "pe-g1-l1": {
        "data_table": table(["Body Movement", "Example"], [
            ["Locomotor movement", "Walking, running, jumping"],
            ["Non-locomotor movement", "Bending, twisting, stretching in place"],
        ]),
    },
    "physical-education-self-defense-g1-l2": {
        "data_table": table(["Skill", "Focus"], [
            ["Running", "Speed and arm movement"], ["Jumping", "Bending knees and landing softly"],
        ]),
    },
    "physical-education-self-defense-g1-l3": {
        "data_table": table(["Skill", "Technique"], [
            ["Throwing", "Step forward, aim, release"], ["Catching", "Watch the ball, use both hands"],
        ]),
    },
    "physical-education-self-defense-g1-l4": {
        "data_table": table(["Activity", "Skill Developed"], [
            ["Standing on one foot", "Balance"], ["Walking on a line", "Coordination"],
        ]),
    },
    "physical-education-self-defense-g1-l6": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Teamwork", "Working together to win"], ["Communication", "Telling teammates what to do"],
        ]),
    },
    "physical-education-self-defense-g1-l7": {
        "data_table": table(["Rule Type", "Example"], [
            ["Safety rule", "No pushing"], ["Fairness rule", "Taking turns"],
        ]),
    },
    "physical-education-self-defense-g1-l9": {
        "data_table": table(["Movement", "Description"], [
            ["Hop", "Jump on one foot"], ["Skip", "Step and hop, alternating feet"],
            ["Gallop", "Slide one foot forward, then the other follows"],
        ]),
    },
    "physical-education-self-defense-g1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Personal space", "The area around your body that you keep clear"],
            ["Safe distance", "Enough room to move without bumping into others"],
        ]),
    },
    "physical-education-self-defense-g1-l11": {
        "data_table": table(["Rule", "Why"], [
            ["Don't go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if a stranger approaches", "Helps adults protect you"],
        ]),
    },
    "physical-education-self-defense-g1-l12": {
        "data_table": table(["Step", "Action"], [
            ["1", "Say 'No' firmly"], ["2", "Walk or run away"], ["3", "Tell a trusted adult right away"],
        ]),
    },
    "physical-education-self-defense-g1-l13": {
        "data_table": table(["Situation", "Safe Response"], [
            ["Someone grabs your arm", "Pull away and yell for help"],
            ["Feeling unsafe", "Run to a trusted adult"],
        ]),
    },
    "physical-education-self-defense-g1-l14": {
        "data_table": table(["Rule", "Where"], [
            ["Look both ways", "Road"], ["Use equipment properly", "Playground"],
        ]),
    },
    "physical-education-self-defense-g1-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can help if needed"],
            ["Only swim where a lifeguard is present", "Extra safety"],
        ]),
    },
    "physical-education-self-defense-g1-l16": {
        "data_table": table(["Habit", "Benefit"], [
            ["Daily active play", "Keeps the body strong"], ["Stretching before activity", "Prevents injury"],
        ]),
    },
    "physical-education-self-defense-g1-l17": {
        "data_table": table(["Skill", "Example"], [
            ["Turn-taking", "Waiting for your turn on the slide"],
            ["Cooperation", "Working together to build a fort"],
        ]),
    },
    "physical-education-self-defense-g1-l19": {
        "data_table": table(["Movement Type", "Example"], [
            ["Rhythmic movement", "Clapping and stepping to a beat"],
            ["Free dance", "Moving however the music feels"],
        ]),
    },
    "physical-education-self-defense-g1-l20": {
        "data_table": table(["Fair Play Value", "Example"], [
            ["Honesty", "Admitting when you're out in a game"],
            ["Respect", "Congratulating the other team"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json PE: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 PE lessons (completing 20/20).")


if __name__ == "__main__":
    main()
