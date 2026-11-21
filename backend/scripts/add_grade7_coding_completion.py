#!/usr/bin/env python3
"""Depth pass, Grade 7 Coding: fill in real, hand-checked data_table
content for the 38 Grade 7 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Coding to full 40/40 coverage.

Examples use real, runnable Python/HTML/CSS syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g7-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Function", "def greet(): return 'Hi'"], ["Module", "import math"],
        ]),
        "formulae": ["def greet():", "    return \"Hi\"", "import math", "print(math.sqrt(16))"],
    },
    "coding-g7-l2": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["float", "3.14"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g7-l3": {
        "data_table": table(["Function", "Purpose"], [
            ["print()", "Displays output"], ["input()", "Gets typed text from the user"],
        ]),
    },
    "coding-g7-l4": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs if a condition is true"], ["elif", "Checks another condition"], ["else", "Runs if none are true"],
        ]),
        "formulae": ["if score >= 90:", "    print(\"A\")", "elif score >= 80:", "    print(\"B\")", "else:", "    print(\"C\")"],
    },
    "coding-g7-l5": {
        "data_table": table(["Operator", "Meaning"], [
            ["==", "Equal to"], ["and", "Both conditions true"], ["or", "Either condition true"],
        ]),
    },
    "coding-g7-l6": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "coding-g7-l7": {
        "data_table": table(["Loop", "Example"], [
            ["while", "while count < 5: count += 1"],
        ]),
        "formulae": ["count = 0", "while count < 5:", "    count += 1"],
    },
    "coding-g7-l8": {
        "data_table": table(["Concept", "Example"], [
            ["Nested loop", "A loop inside another loop"],
        ]),
        "formulae": ["for i in range(3):", "    for j in range(2):", "        print(i, j)"],
    },
    "coding-g7-l9": {
        "data_table": table(["Method", "Effect"], [
            [".append()", "Adds an item to the end"], [".sort()", "Sorts the list"],
        ]),
    },
    "coding-g7-l10": {
        "data_table": table(["Concept", "Example"], [
            ["Dictionary", "student = {'name': 'Sam', 'age': 12}"],
        ]),
        "formulae": ["student = {\"name\": \"Sam\", \"age\": 12}"],
    },
    "coding-g7-l11": {
        "data_table": table(["Structure", "Example"], [
            ["Tuple", "point = (3, 5)"], ["Set", "colors = {'red', 'blue'}"],
        ]),
    },
    "coding-g7-l12": {
        "data_table": table(["Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".format()", "Inserts values into a string"],
        ]),
    },
    "coding-g7-l13": {
        "data_table": table(["Validation", "Purpose"], [
            ["Type checking", "Ensures input is the expected data type"],
        ]),
    },
    "coding-g7-l14": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "coding-g7-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g7-l17": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Bubble sort", "Repeatedly swaps adjacent out-of-order items"],
            ["Selection sort", "Repeatedly selects the smallest remaining item"],
        ]),
    },
    "coding-g7-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursion", "A function that calls itself to solve a smaller version of the problem"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "coding-g7-l19": {
        "data_table": table(["Error Type", "Meaning"], [
            ["SyntaxError", "Code doesn't follow the language's rules"], ["NameError", "A variable isn't defined"],
        ]),
    },
    "coding-g7-l21": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comments (#)", "Explains what code does"], ["Docstrings", "Documents a function's purpose"],
        ]),
    },
    "coding-g7-l22": {
        "data_table": table(["Concept", "Example"], [
            ["Class", "class Dog:"], ["Object", "my_dog = Dog()"],
        ]),
        "formulae": ["class Dog:", "    def bark(self):", "        print(\"Woof\")", "my_dog = Dog()", "my_dog.bark()"],
    },
    "coding-g7-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks changes to code over time"], ["Commit", "Saves a snapshot of changes"],
        ]),
    },
    "coding-g7-l24": {
        "data_table": table(["Function", "Purpose"], [
            ["open()", "Opens a file"], ["write()", "Writes text to a file"],
        ]),
        "formulae": ["with open(\"notes.txt\", \"w\") as f:", "    f.write(\"Hello\")"],
    },
    "coding-g7-l25": {
        "data_table": table(["Command", "Effect"], [
            ["forward(100)", "Moves the turtle forward 100 units"], ["right(90)", "Turns the turtle right 90 degrees"],
        ]),
    },
    "coding-g7-l26": {
        "data_table": table(["Game Element", "Purpose"], [
            ["input()", "Gets the player's typed response"], ["if/else", "Decides what happens based on the answer"],
        ]),
    },
    "coding-g7-l27": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "coding-g7-l28": {
        "data_table": table(["CSS Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "coding-g7-l29": {
        "data_table": table(["JavaScript Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() { return 'Hi'; }"],
        ]),
    },
    "coding-g7-l30": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["4", "100"],
        ]),
    },
    "coding-g7-l31": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "coding-g7-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "coding-g7-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A way for programs to communicate with each other"],
        ]),
    },
    "coding-g7-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Record", "One entry in a database"],
        ]),
    },
    "coding-g7-l35": {
        "data_table": table(["Concept", "Meaning"], [
            ["Decomposition", "Breaking a big problem into smaller parts"],
        ]),
    },
    "coding-g7-l36": {
        "data_table": table(["GUI Element", "Purpose"], [
            ["Button", "Triggers an action when clicked"], ["Text field", "Accepts typed input"],
        ]),
    },
    "coding-g7-l37": {
        "data_table": table(["Game Design Concept", "Meaning"], [
            ["Win condition", "The requirement for the player to win"],
            ["Game loop", "The repeating cycle that updates the game"],
        ]),
    },
    "coding-g7-l38": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"],
            ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "coding-g7-l39": {
        "data_table": table(["Planning Step", "Purpose"], [
            ["Define requirements", "Know what the software should do"],
            ["Sketch the design", "Plan the structure before coding"],
        ]),
    },
    "coding-g7-l40": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
            ["Strong password", "Hard for others to guess"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Coding lessons (completing 40/40).")


if __name__ == "__main__":
    main()
