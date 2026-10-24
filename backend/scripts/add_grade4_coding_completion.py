#!/usr/bin/env python3
"""Depth pass, Grade 4 Coding: fill in real, hand-checked data_table
content for the 28 Grade 4 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 4 Coding to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g4-l1": {
        "data_table": table(["Concept", "Example"], [
            ["If-then", "If it rains, then take an umbrella"],
        ]),
    },
    "coding-g4-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sequencing", "Running steps in a specific order"],
        ]),
    },
    "coding-g4-l3": {
        "data_table": table(["Concept", "Example"], [
            ["Loop", "Repeat 10 times: move forward"],
        ]),
    },
    "coding-g4-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Event", "Something that triggers an action"], ["Trigger", "The signal that starts the event"],
        ]),
    },
    "coding-g4-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g4-l7": {
        "data_table": table(["Step", "Purpose"], [
            ["Plan the motion", "Decide what should move and how"], ["Add blocks", "Build the sequence"],
        ]),
    },
    "coding-g4-l8": {
        "data_table": table(["Quiz Element", "Purpose"], [
            ["Question", "Prompts the player"], ["Score tracker", "Counts correct answers"],
        ]),
    },
    "coding-g4-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g4-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Broadcast", "Sends a message that other sprites can respond to"],
        ]),
    },
    "coding-g4-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Costume", "A sprite's different appearances"], ["Sprite movement", "Changing a sprite's position"],
        ]),
    },
    "coding-g4-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Custom block", "A reusable set of instructions you create"],
        ]),
    },
    "coding-g4-l14": {
        "data_table": table(["Term", "Use"], [
            ["Random number block", "Generates unpredictable outcomes, like dice rolls"],
        ]),
    },
    "coding-g4-l15": {
        "data_table": table(["Maze Element", "Purpose"], [
            ["Walls", "Block the player's path"], ["Goal", "The finish point"],
        ]),
    },
    "coding-g4-l16": {
        "data_table": table(["Concept", "Meaning"], [
            ["Text-based coding", "Writing code as typed text instead of blocks"],
        ]),
    },
    "coding-g4-l17": {
        "data_table": table(["Concept", "Meaning"], [
            ["Decomposition", "Breaking a big problem into smaller parts"],
        ]),
    },
    "coding-g4-l18": {
        "data_table": table(["Block Type", "Effect"], [
            ["Play sound block", "Plays an audio clip"], ["Change tempo block", "Speeds up or slows down music"],
        ]),
    },
    "coding-g4-l19": {
        "data_table": table(["Element", "Purpose"], [
            ["Say block", "Shows dialogue"], ["Scene change", "Moves the story forward"],
        ]),
    },
    "coding-g4-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Explain the project", "Helps others understand what you made"],
            ["Demonstrate it", "Shows the project in action"],
        ]),
    },
    "coding-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Traffic lights", "If red, then stop"],
        ]),
    },
    "coding-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Morning routine", "Wake up, then brush teeth, then eat breakfast"],
        ]),
    },
    "coding-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Washing machine", "Repeats a wash cycle a set number of times"],
        ]),
    },
    "coding-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Score tracker", "Stores the current score in a variable"],
        ]),
    },
    "coding-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Doorbell", "Pressing the button triggers a sound"],
        ]),
    },
    "coding-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Troubleshooting", "Checking each step to find where something went wrong"],
        ]),
    },
    "coding-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Flipbook animation", "Frames shown quickly to create motion"],
        ]),
    },
    "coding-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Trivia app", "Presents questions and checks answers"],
        ]),
    },
    "coding-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Recipe steps", "A recipe is an everyday algorithm"],
        ]),
    },
    "coding-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Group game", "One sprite's action tells another sprite to respond"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Coding lessons (completing 30/30).")


if __name__ == "__main__":
    main()
