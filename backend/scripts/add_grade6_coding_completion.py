#!/usr/bin/env python3
"""Depth pass, Grade 6 Coding: fill in real, hand-checked data_table
content for the 28 Grade 6 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Coding to full 30/30 coverage.

Examples use real, runnable Python/HTML/CSS syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g6-l1": {
        "data_table": table(["Concept", "Example"], [
            ["for loop", "for i in range(5): print(i)"], ["List", "fruits = ['apple', 'banana']"],
        ]),
        "formulae": ["fruits = [\"apple\", \"banana\"]", "for fruit in fruits:", "    print(fruit)"],
    },
    "coding-g6-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Program", "A set of instructions for a computer"], ["Syntax", "The rules of a programming language"],
        ]),
    },
    "coding-g6-l3": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["float", "3.14"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g6-l4": {
        "data_table": table(["String Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".split()", "Breaks a string into a list"],
        ]),
    },
    "coding-g6-l5": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs if a condition is true"], ["elif", "Checks another condition"], ["else", "Runs if none are true"],
        ]),
        "formulae": ["if score >= 90:", "    print(\"A\")", "elif score >= 80:", "    print(\"B\")", "else:", "    print(\"C\")"],
    },
    "coding-g6-l6": {
        "data_table": table(["Concept", "Example"], [
            ["Function definition", "def add(a, b): return a + b"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "coding-g6-l7": {
        "data_table": table(["Concept", "Example"], [
            ["Dictionary", "student = {'name': 'Sam', 'age': 12}"],
        ]),
        "formulae": ["student = {\"name\": \"Sam\", \"age\": 12}"],
    },
    "coding-g6-l8": {
        "data_table": table(["Structure", "Example"], [
            ["Tuple", "point = (3, 5)"], ["Set", "colors = {'red', 'blue'}"],
        ]),
    },
    "coding-g6-l9": {
        "data_table": table(["Error Type", "Meaning"], [
            ["SyntaxError", "Code doesn't follow the language's rules"], ["NameError", "A variable isn't defined"],
        ]),
    },
    "coding-g6-l10": {
        "data_table": table(["Function", "Purpose"], [
            ["print()", "Displays output"], ["input()", "Gets typed text from the user"],
        ]),
    },
    "coding-g6-l11": {
        "data_table": table(["Command", "Effect"], [
            ["forward(100)", "Moves the turtle forward 100 units"], ["right(90)", "Turns the turtle right 90 degrees"],
        ]),
    },
    "coding-g6-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g6-l13": {
        "data_table": table(["Tool", "Purpose"], [
            ["Flowchart", "Visualizes steps and decisions"], ["Pseudocode", "Plain-language outline of code logic"],
        ]),
    },
    "coding-g6-l15": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Linear search", "Checks each item one at a time"],
        ]),
    },
    "coding-g6-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Scratch", "A block-based visual programming language"], ["Sprite", "A character or object in Scratch"],
        ]),
    },
    "coding-g6-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Event", "Something that triggers an action"], ["Event handler", "Code that responds to an event"],
        ]),
    },
    "coding-g6-l18": {
        "data_table": table(["Game Element", "Purpose"], [
            ["Score variable", "Tracks the player's points"], ["Win condition", "Determines when the player wins"],
        ]),
    },
    "coding-g6-l20": {
        "data_table": table(["CSS Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "coding-g6-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "coding-g6-l22": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"],
        ]),
    },
    "coding-g6-l23": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "coding-g6-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks changes to code over time"], ["Commit", "Saves a snapshot of changes"],
        ]),
    },
    "coding-g6-l25": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comments (#)", "Explains what code does"], ["Clear variable names", "Makes code easier to read"],
        ]),
    },
    "coding-g6-l26": {
        "data_table": table(["Concept", "Example"], [
            ["Nested loop", "A loop inside another loop"],
        ]),
        "formulae": ["for i in range(3):", "    for j in range(2):", "        print(i, j)"],
    },
    "coding-g6-l27": {
        "data_table": table(["Concept", "Example"], [
            ["List comprehension", "squares = [x*x for x in range(5)]"],
        ]),
        "formulae": ["squares = [x * x for x in range(5)]"],
    },
    "coding-g6-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursion", "A function that calls itself to solve a smaller version of the problem"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "coding-g6-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A way for programs to communicate with each other"],
        ]),
    },
    "coding-g6-l30": {
        "data_table": table(["Concept", "Meaning"], [
            ["Decomposition", "Breaking a big problem into smaller parts"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Coding lessons (completing 30/30).")


if __name__ == "__main__":
    main()
