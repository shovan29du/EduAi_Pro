#!/usr/bin/env python3
"""Depth pass, Grade 10 ICT & Computer Science: fill in real,
hand-checked data_table content for the Grade 10 ICT lessons not
covered by the earlier breadth-first batch. Brings Grade 10 ICT &
Computer Science to full 50/50 coverage.

Examples use real, runnable Python/HTML/CSS/SQL syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g10-l2": {
        "data_table": table(["Component", "Role"], [
            ["CPU", "Executes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "ict-computer-science-g10-l3": {
        "data_table": table(["Type", "Example"], [
            ["System software", "Operating system"], ["Application software", "Word processor"],
        ]),
    },
    "ict-computer-science-g10-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting billions of devices"],
        ]),
    },
    "ict-computer-science-g10-l5": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network"], ["WAN", "Wide Area Network"],
        ]),
    },
    "ict-computer-science-g10-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["IP address", "A numerical label identifying a device on a network"], ["Domain name", "A human-readable website address"],
        ]),
    },
    "ict-computer-science-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "ict-computer-science-g10-l8": {
        "data_table": table(["Malware Type", "Behavior"], [
            ["Virus", "Attaches to files and spreads when executed"], ["Worm", "Spreads independently across networks"],
        ]),
    },
    "ict-computer-science-g10-l9": {
        "data_table": table(["Practice", "Reason"], [
            ["Use unique, long passwords", "Makes accounts harder to guess or crack"],
        ]),
    },
    "ict-computer-science-g10-l10": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "A named storage location for data"], ["Loop", "Repeats a block of code"],
        ]),
    },
    "ict-computer-science-g10-l11": {
        "data_table": table(["Data Type", "Example"], [
            ["Integer", "5"], ["String", "'hello'"], ["Boolean", "True/False"],
        ]),
    },
    "ict-computer-science-g10-l12": {
        "data_table": table(["Structure", "Example"], [
            ["Loop", "for i in range(5): print(i)"], ["Conditional", "if x > 0: print('positive')"],
        ]),
        "formulae": ["for i in range(5):", "    if i % 2 == 0:", "        print(i)"],
    },
    "ict-computer-science-g10-l13": {
        "data_table": table(["Concept", "Meaning"], [
            ["Function", "A reusable block of code that performs a task"], ["Modular programming", "Breaking a program into independent, reusable modules"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "ict-computer-science-g10-l14": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "ict-computer-science-g10-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step procedure for solving a problem"],
        ]),
    },
    "ict-computer-science-g10-l16": {
        "data_table": table(["Tool", "Purpose"], [
            ["Flowchart", "Visual diagram of a process"], ["Pseudocode", "Plain-language description of an algorithm"],
        ]),
    },
    "ict-computer-science-g10-l17": {
        "data_table": table(["Structure", "Description"], [
            ["Array", "An ordered, indexed collection of items"],
        ]),
        "formulae": ["numbers = [1, 2, 3, 4]"],
    },
    "ict-computer-science-g10-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of structured data"],
        ]),
    },
    "ict-computer-science-g10-l20": {
        "data_table": table(["Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "ict-computer-science-g10-l21": {
        "data_table": table(["Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "ict-computer-science-g10-l22": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() { return 'Hi'; }"],
        ]),
        "formulae": ["function greet() {", "    return \"Hi\";", "}"],
    },
    "ict-computer-science-g10-l23": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["4", "100"],
        ]),
    },
    "ict-computer-science-g10-l24": {
        "data_table": table(["Unit", "Size"], [
            ["Byte", "8 bits"], ["Kilobyte", "1024 bytes"],
        ]),
    },
    "ict-computer-science-g10-l25": {
        "data_table": table(["OS", "Example"], [
            ["Desktop", "Windows, macOS, Linux"], ["Mobile", "Android, iOS"],
        ]),
    },
    "ict-computer-science-g10-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["File system", "The method an OS uses to organize and store files"],
        ]),
    },
    "ict-computer-science-g10-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud computing", "Delivering computing services over the internet"],
        ]),
    },
    "ict-computer-science-g10-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems performing tasks requiring human-like intelligence"],
        ]),
    },
    "ict-computer-science-g10-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "A subset of AI where systems learn patterns from data"],
        ]),
    },
    "ict-computer-science-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Big data", "Extremely large datasets analyzed to reveal patterns and trends"],
        ]),
    },
    "ict-computer-science-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Robotics", "The design and use of machines that can sense and act in the physical world"],
        ]),
    },
    "ict-computer-science-g10-l32": {
        "data_table": table(["Principle", "Meaning"], [
            ["Digital ethics", "Using technology responsibly and respecting others"],
        ]),
    },
    "ict-computer-science-g10-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Software license", "Legal terms governing how software may be used or distributed"],
        ]),
    },
    "ict-computer-science-g10-l34": {
        "data_table": table(["Phase", "Purpose"], [
            ["Requirements", "Defines what the software should do"], ["Testing", "Verifies the software works correctly"],
        ]),
    },
    "ict-computer-science-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Debugging", "Finding and fixing errors in code"],
        ]),
    },
    "ict-computer-science-g10-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks and manages changes to code over time"],
        ]),
        "formulae": ["git commit -m \"Add feature\"", "git push origin main"],
    },
    "ict-computer-science-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Spreadsheet", "A grid of rows and columns for organizing and calculating data"],
        ]),
    },
    "ict-computer-science-g10-l38": {
        "data_table": table(["Chart Type", "Best For"], [
            ["Bar chart", "Comparing categories"], ["Line chart", "Trends over time"],
        ]),
    },
    "ict-computer-science-g10-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer graphics", "The creation and manipulation of images using computers"],
        ]),
    },
    "ict-computer-science-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "Software that ranks and selects content shown to social media users"],
        ]),
    },
    "ict-computer-science-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data a person leaves from their online activity"],
        ]),
    },
    "ict-computer-science-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["E-commerce", "Buying and selling goods or services over the internet"],
        ]),
    },
    "ict-computer-science-g10-l43": {
        "data_table": table(["Element", "Purpose"], [
            ["Game loop", "Continuously updates the game state"],
        ]),
    },
    "ict-computer-science-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Human-computer interaction", "The study of how people interact with computer systems"],
        ]),
    },
    "ict-computer-science-g10-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer vision", "AI that interprets and understands visual information"],
        ]),
    },
    "ict-computer-science-g10-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A defined way for programs to communicate with each other"],
        ]),
    },
    "ict-computer-science-g10-l47": {
        "data_table": table(["Technology", "Use"], [
            ["Bluetooth", "Short-range wireless connection between devices"],
        ]),
    },
    "ict-computer-science-g10-l48": {
        "data_table": table(["Era", "Milestone"], [
            ["1940s", "First electronic computers"], ["1990s", "Rise of the World Wide Web"],
        ]),
    },
    "ict-computer-science-g10-l49": {
        "data_table": table(["Technology", "Example"], [
            ["Quantum computing", "Uses quantum bits to process information"],
        ]),
    },
    "ict-computer-science-g10-l50": {
        "data_table": table(["Career", "Focus"], [
            ["Software developer", "Writes and maintains programs"], ["Network administrator", "Manages an organization's networks"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 ICT & Computer Science lessons (completing 50/50).")


if __name__ == "__main__":
    main()
