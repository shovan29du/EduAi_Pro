#!/usr/bin/env python3
"""Depth pass, Grade 3 Coding: fill in real, hand-checked data_table
content for the 18 Grade 3 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Coding to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g3-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Scratch", "A block-based visual programming language"], ["Sprite", "A character or object in Scratch"],
        ]),
    },
    "coding-g3-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Program", "A set of instructions for a computer"], ["Code", "The instructions written in a program"],
        ]),
    },
    "coding-g3-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sequencing", "Running steps in a specific order"],
        ]),
    },
    "coding-g3-l5": {
        "data_table": table(["Concept", "Example"], [
            ["If-then", "If it rains, then take an umbrella"],
        ]),
    },
    "coding-g3-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Event", "Something that triggers an action"], ["Example event", "Clicking the green flag"],
        ]),
    },
    "coding-g3-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Sprite", "A character that can move and act"], ["Backdrop", "The background of the stage"],
        ]),
    },
    "coding-g3-l8": {
        "data_table": table(["Block Type", "Effect"], [
            ["Move block", "Moves the sprite a number of steps"], ["Glide block", "Moves smoothly over time"],
        ]),
    },
    "coding-g3-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Variable", "A named container that stores a value"],
        ]),
    },
    "coding-g3-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g3-l11": {
        "data_table": table(["Step", "Purpose"], [
            ["Plan the motion", "Decide what should move and how"], ["Add blocks", "Build the animation sequence"],
        ]),
    },
    "coding-g3-l12": {
        "data_table": table(["Step", "Purpose"], [
            ["Add dialogue", "Characters speak using say blocks"], ["Add choices", "Let the user pick an option"],
        ]),
    },
    "coding-g3-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g3-l14": {
        "data_table": table(["Activity", "Skill Practiced"], [
            ["Following a recipe", "Sequencing steps"], ["Giving directions", "Precise instructions"],
        ]),
    },
    "coding-g3-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Block-based coding", "Building programs by snapping together visual blocks"],
        ]),
    },
    "coding-g3-l16": {
        "data_table": table(["Game Element", "Example"], [
            ["Goal", "Reach the finish line"], ["Score", "Points earned during play"],
        ]),
    },
    "coding-g3-l17": {
        "data_table": table(["Block Type", "Effect"], [
            ["Play sound block", "Plays an audio clip"], ["Change tempo block", "Speeds up or slows down music"],
        ]),
    },
    "coding-g3-l18": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "coding-g3-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Tell a trusted adult about anything unsafe", "Helps adults protect you"],
        ]),
    },
    "coding-g3-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Explain the project", "Helps others understand what you made"],
            ["Demonstrate it", "Shows the project in action"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Coding lessons (completing 20/20).")


if __name__ == "__main__":
    main()
