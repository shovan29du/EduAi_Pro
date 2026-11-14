#!/usr/bin/env python3
"""Depth pass, Grade 9 ICT & Computer Science: fill in real, hand-checked
data_table content for the 48 Grade 9 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 9 ICT & Computer Science to
full 50/50 coverage.

Examples use real, runnable Python/HTML/CSS syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Web development", "Building and maintaining websites"],
        ]),
    },
    "ict-computer-science-g9-l2": {
        "data_table": table(["Component", "Role"], [
            ["Hardware", "Physical parts of a computer"], ["Software", "Programs that run on hardware"],
        ]),
    },
    "ict-computer-science-g9-l3": {
        "data_table": table(["Type", "Example"], [
            ["Hardware", "Keyboard, monitor, CPU"], ["Software", "Operating system, apps"],
        ]),
    },
    "ict-computer-science-g9-l4": {
        "data_table": table(["Device Type", "Example"], [
            ["Input", "Keyboard, mouse"], ["Output", "Monitor, printer"],
        ]),
    },
    "ict-computer-science-g9-l5": {
        "data_table": table(["Storage Type", "Example"], [
            ["Volatile (RAM)", "Loses data when powered off"], ["Non-volatile (SSD/HDD)", "Retains data when powered off"],
        ]),
    },
    "ict-computer-science-g9-l7": {
        "data_table": table(["Concept", "Meaning"], [
            ["Variable", "A named storage location for data"], ["Loop", "Repeats a block of code"],
        ]),
    },
    "ict-computer-science-g9-l8": {
        "data_table": table(["Data Type", "Example"], [
            ["Integer", "5"], ["String", "'hello'"], ["Boolean", "True/False"],
        ]),
    },
    "ict-computer-science-g9-l9": {
        "data_table": table(["Loop Type", "Example"], [
            ["for loop", "for i in range(5):"], ["while loop", "while x < 10:"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "ict-computer-science-g9-l10": {
        "data_table": table(["Statement", "Purpose"], [
            ["if", "Runs code when a condition is true"], ["else", "Runs code when the condition is false"],
        ]),
        "formulae": ["if age >= 18:", "    print(\"Adult\")", "else:", "    print(\"Minor\")"],
    },
    "ict-computer-science-g9-l11": {
        "data_table": table(["Concept", "Example"], [
            ["Function", "def greet(name): return f'Hello {name}'"],
        ]),
        "formulae": ["def greet(name):", "    return f\"Hello {name}\""],
    },
    "ict-computer-science-g9-l12": {
        "data_table": table(["Concept", "Example"], [
            ["Print statement", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "ict-computer-science-g9-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step procedure for solving a problem"],
        ]),
    },
    "ict-computer-science-g9-l14": {
        "data_table": table(["Tool", "Purpose"], [
            ["Flowchart", "Visual diagram of a process"], ["Pseudocode", "Plain-language description of an algorithm"],
        ]),
    },
    "ict-computer-science-g9-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Debugging", "Finding and fixing errors in code"],
        ]),
    },
    "ict-computer-science-g9-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of structured data"],
        ]),
    },
    "ict-computer-science-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Spreadsheet", "A grid of rows and columns for organizing and calculating data"],
        ]),
    },
    "ict-computer-science-g9-l18": {
        "data_table": table(["Encoding", "Use"], [
            ["ASCII", "Represents text characters as numbers"],
        ]),
    },
    "ict-computer-science-g9-l19": {
        "data_table": table(["Format", "Use"], [
            ["JPEG", "Compressed image format"], ["MP3", "Compressed audio format"],
        ]),
    },
    "ict-computer-science-g9-l20": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network, small area"], ["WAN", "Wide Area Network, large area"],
        ]),
    },
    "ict-computer-science-g9-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting billions of devices"],
        ]),
    },
    "ict-computer-science-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["World Wide Web", "A system of linked documents accessed via the internet"],
        ]),
    },
    "ict-computer-science-g9-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["IP address", "A numerical label identifying a device on a network"], ["Domain name", "A human-readable website address"],
        ]),
    },
    "ict-computer-science-g9-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting systems and data from digital attacks"],
        ]),
    },
    "ict-computer-science-g9-l25": {
        "data_table": table(["Malware Type", "Behavior"], [
            ["Virus", "Attaches to files and spreads when executed"], ["Worm", "Spreads independently across networks"],
        ]),
    },
    "ict-computer-science-g9-l26": {
        "data_table": table(["Practice", "Reason"], [
            ["Use unique, long passwords", "Makes accounts harder to guess or crack"],
        ]),
    },
    "ict-computer-science-g9-l27": {
        "data_table": table(["Practice", "Reason"], [
            ["Limit shared personal information", "Reduces online privacy risk"],
        ]),
    },
    "ict-computer-science-g9-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data a person leaves from their online activity"],
        ]),
    },
    "ict-computer-science-g9-l29": {
        "data_table": table(["Practice", "Reason"], [
            ["Report and block", "Recommended response to cyberbullying"],
        ]),
    },
    "ict-computer-science-g9-l30": {
        "data_table": table(["Principle", "Meaning"], [
            ["Digital ethics", "Using technology responsibly and respecting others"],
        ]),
    },
    "ict-computer-science-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks requiring human-like intelligence"],
        ]),
    },
    "ict-computer-science-g9-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "A subset of AI where systems learn patterns from data"],
        ]),
    },
    "ict-computer-science-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Robotics", "The design and use of machines that can sense and act in the physical world"],
        ]),
    },
    "ict-computer-science-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer vision", "AI that interprets and understands visual information"],
        ]),
    },
    "ict-computer-science-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud computing", "Delivering computing services over the internet"],
        ]),
    },
    "ict-computer-science-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["File system", "The method an OS uses to organize and store files"],
        ]),
    },
    "ict-computer-science-g9-l37": {
        "data_table": table(["OS", "Example"], [
            ["Desktop", "Windows, macOS, Linux"], ["Mobile", "Android, iOS"],
        ]),
    },
    "ict-computer-science-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks and manages changes to code over time"],
        ]),
        "formulae": ["git commit -m \"Add feature\"", "git push origin main"],
    },
    "ict-computer-science-g9-l39": {
        "data_table": table(["Phase", "Purpose"], [
            ["Design", "Plans the software's structure"], ["Testing", "Verifies the software works correctly"],
        ]),
    },
    "ict-computer-science-g9-l40": {
        "data_table": table(["Concept", "Example"], [
            ["Class", "class Car:"], ["Object", "my_car = Car()"],
        ]),
        "formulae": ["class Car:", "    def drive(self):", "        print(\"Vroom\")"],
    },
    "ict-computer-science-g9-l41": {
        "data_table": table(["Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<a>", "Hyperlink"],
        ]),
        "formulae": ["<h1>Welcome</h1>", "<a href=\"https://example.com\">Link</a>"],
    },
    "ict-computer-science-g9-l42": {
        "data_table": table(["Property", "Effect"], [
            ["background-color", "Sets the background color"], ["margin", "Sets space outside an element"],
        ]),
        "formulae": ["body { background-color: white; margin: 0; }"],
    },
    "ict-computer-science-g9-l43": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "let score = 0;"], ["Function", "function add(a, b) { return a + b; }"],
        ]),
        "formulae": ["function add(a, b) {", "    return a + b;", "}"],
    },
    "ict-computer-science-g9-l44": {
        "data_table": table(["Platform", "Language Example"], [
            ["Android", "Kotlin or Java"], ["iOS", "Swift"],
        ]),
    },
    "ict-computer-science-g9-l45": {
        "data_table": table(["Element", "Purpose"], [
            ["Game loop", "Continuously updates the game state"], ["Sprite", "A 2D image used in the game"],
        ]),
    },
    "ict-computer-science-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptography", "The practice of securing information using codes"],
        ]),
    },
    "ict-computer-science-g9-l47": {
        "data_table": table(["Structure", "Description"], [
            ["Array", "An ordered, indexed collection of items"],
        ]),
        "formulae": ["numbers = [1, 2, 3, 4]"],
    },
    "ict-computer-science-g9-l48": {
        "data_table": table(["Algorithm", "Approach"], [
            ["Binary search", "Repeatedly halves a sorted list to find a target"], ["Bubble sort", "Repeatedly swaps adjacent out-of-order elements"],
        ]),
    },
    "ict-computer-science-g9-l49": {
        "data_table": table(["Skill", "Meaning"], [
            ["Computational thinking", "Breaking problems into smaller, solvable steps"],
        ]),
    },
    "ict-computer-science-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital citizenship", "Responsible and ethical use of technology"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 ICT & Computer Science lessons (completing 50/50).")


if __name__ == "__main__":
    main()
