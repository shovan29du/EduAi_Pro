#!/usr/bin/env python3
"""Depth pass, Grade 10 Coding: fill in real, hand-checked data_table
content for the Grade 10 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Coding to full 50/50 coverage.

Examples use real, runnable Python/HTML/CSS/SQL syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g10-l1": {
        "data_table": table(["Structure", "Use"], [
            ["Array", "Ordered, indexed collection"], ["Linked list", "Sequence of nodes pointing to the next"],
        ]),
    },
    "coding-g10-l2": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g10-l3": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs code if a condition is true"], ["elif", "Checks another condition"],
        ]),
        "formulae": ["if x > 0:", "    print(\"positive\")", "elif x == 0:", "    print(\"zero\")", "else:", "    print(\"negative\")"],
    },
    "coding-g10-l4": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"], ["while", "while count < 5: count += 1"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "coding-g10-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Scope", "The region of code where a variable is accessible"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "coding-g10-l6": {
        "data_table": table(["Structure", "Example"], [
            ["Array/List", "fruits = ['apple', 'banana']"],
        ]),
    },
    "coding-g10-l7": {
        "data_table": table(["Structure", "Example"], [
            ["Dictionary", "student = {'name': 'Sam', 'age': 15}"],
        ]),
        "formulae": ["student = {\"name\": \"Sam\", \"age\": 15}"],
    },
    "coding-g10-l8": {
        "data_table": table(["Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".split()", "Breaks a string into a list"],
        ]),
    },
    "coding-g10-l9": {
        "data_table": table(["Concept", "Meaning"], [
            ["OOP", "Organizes code around objects that bundle data and behavior"],
        ]),
    },
    "coding-g10-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Class", "A blueprint for creating objects"], ["Object", "An instance of a class"],
        ]),
        "formulae": ["class Dog:", "    def bark(self):", "        print(\"Woof\")"],
    },
    "coding-g10-l11": {
        "data_table": table(["Concept", "Meaning"], [
            ["Inheritance", "A class derives properties from a parent class"], ["Polymorphism", "Objects of different classes respond to the same method call"],
        ]),
    },
    "coding-g10-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursion", "A function that calls itself to solve a smaller subproblem"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "coding-g10-l13": {
        "data_table": table(["Algorithm", "Approach"], [
            ["Bubble sort", "Repeatedly swaps adjacent out-of-order items"], ["Merge sort", "Divides and merges sorted sublists"],
        ]),
    },
    "coding-g10-l14": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Linear search", "Checks each item one at a time"], ["Binary search", "Repeatedly halves a sorted list"],
        ]),
    },
    "coding-g10-l17": {
        "data_table": table(["Structure", "Description"], [
            ["Linked list", "A sequence of nodes, each pointing to the next"],
        ]),
    },
    "coding-g10-l18": {
        "data_table": table(["Structure", "Description"], [
            ["Binary tree", "A tree where each node has at most two children"], ["BST", "A binary tree ordered so search is efficient"],
        ]),
    },
    "coding-g10-l19": {
        "data_table": table(["Traversal", "Order"], [
            ["Breadth-first search", "Explores neighbors level by level"], ["Depth-first search", "Explores as far as possible along each branch"],
        ]),
    },
    "coding-g10-l20": {
        "data_table": table(["Command", "Purpose"], [
            ["git commit", "Saves a snapshot of changes"], ["git push", "Uploads commits to a remote repository"],
        ]),
        "formulae": ["git add .", "git commit -m \"message\"", "git push origin main"],
    },
    "coding-g10-l21": {
        "data_table": table(["Technique", "Purpose"], [
            ["Print debugging", "Inserts print statements to trace values"], ["Breakpoints", "Pause execution to inspect state"],
        ]),
    },
    "coding-g10-l22": {
        "data_table": table(["Practice", "Benefit"], [
            ["Meaningful variable names", "Makes code easier to understand"], ["Comments", "Explains non-obvious logic"],
        ]),
    },
    "coding-g10-l23": {
        "data_table": table(["Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "coding-g10-l24": {
        "data_table": table(["Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "coding-g10-l25": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() { return 'Hi'; }"],
        ]),
        "formulae": ["function greet() {", "    return \"Hi\";", "}"],
    },
    "coding-g10-l26": {
        "data_table": table(["Event", "Trigger"], [
            ["onclick", "User clicks an element"],
        ]),
        "formulae": ["document.getElementById(\"btn\").onclick = function() { alert(\"Clicked!\"); };"],
    },
    "coding-g10-l27": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "coding-g10-l28": {
        "data_table": table(["Function", "Purpose"], [
            ["open()", "Opens a file"], ["write()", "Writes text to a file"],
        ]),
        "formulae": ["with open(\"notes.txt\", \"w\") as f:", "    f.write(\"Hello\")"],
    },
    "coding-g10-l29": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might raise an error"], ["except", "Handles the error if raised"],
        ]),
        "formulae": ["try:", "    x = 1 / 0", "except ZeroDivisionError:", "    print(\"Can't divide by zero\")"],
    },
    "coding-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A defined way for programs to communicate with each other"],
        ]),
    },
    "coding-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of structured data"],
        ]),
    },
    "coding-g10-l32": {
        "data_table": table(["SQL Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["WHERE", "Filters results"],
        ]),
        "formulae": ["SELECT name FROM students WHERE grade = 10;"],
    },
    "coding-g10-l33": {
        "data_table": table(["App Type", "Example"], [
            ["Mobile app", "Runs on smartphones"], ["Web app", "Runs in a browser"],
        ]),
    },
    "coding-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Event-driven programming", "Code executes in response to events like clicks or key presses"],
        ]),
    },
    "coding-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Divide and conquer", "Breaks a problem into smaller subproblems, solves them, and combines results"],
        ]),
    },
    "coding-g10-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Dynamic programming", "Solves problems by storing results of subproblems to avoid recomputation"],
        ]),
    },
    "coding-g10-l37": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "coding-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Encryption", "Encoding data so only authorized parties can read it"],
        ]),
    },
    "coding-g10-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems performing tasks that normally require human intelligence"],
        ]),
    },
    "coding-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "A subset of AI where systems learn patterns from data"],
        ]),
    },
    "coding-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Computational thinking", "Breaking problems into smaller, solvable steps"],
        ]),
    },
    "coding-g10-l42": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["4", "100"],
        ]),
    },
    "coding-g10-l43": {
        "data_table": table(["Component", "Role"], [
            ["CPU", "Executes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "coding-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["IP address", "A numerical label identifying a device on a network"],
        ]),
    },
    "coding-g10-l45": {
        "data_table": table(["Phase", "Purpose"], [
            ["Requirements", "Defines what the software should do"], ["Testing", "Verifies the software works correctly"],
        ]),
    },
    "coding-g10-l46": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Unit testing", "Tests individual components in isolation"],
        ]),
    },
    "coding-g10-l47": {
        "data_table": table(["Element", "Purpose"], [
            ["Game loop", "Continuously updates the game state"],
        ]),
    },
    "coding-g10-l48": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"], ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "coding-g10-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Open source", "Software whose source code is publicly available to use and modify"],
        ]),
    },
    "coding-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Robotics programming", "Writing code that controls sensors and motors on a physical robot"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Coding lessons (completing 50/50).")


if __name__ == "__main__":
    main()
