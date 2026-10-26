#!/usr/bin/env python3
"""Depth pass, C1 ICT & Computer Science: fill in real, hand-checked
data_table/formulae content for the 69 C1 ICT & Computer Science lessons
not covered by the earlier breadth-first batch. Brings the subject to
full 70/70 coverage.

Note: lesson ids l1-l60 use the prefix "ict-and-computer-science-c1-",
while l61-l70 use "ict-computer-science-c1-" (no "and-"). Both forms
are preserved exactly as they exist in level_c1.json.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_ict_computer_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-and-computer-science-c1-l1": {
        "data_table": table(["Component", "Function"], [
            ["CPU", "Executes instructions and performs calculations"], ["RAM", "Temporary working memory for active processes"],
        ]),
    },
    "ict-and-computer-science-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of structured data"], ["Network", "A system of interconnected computers sharing resources"],
        ]),
    },
    "ict-and-computer-science-c1-l4": {
        "data_table": table(["Level", "Example"], [
            ["Data", "Raw numbers, e.g. 72"], ["Information", "Data with context, e.g. 72°F outside"],
        ]),
    },
    "ict-and-computer-science-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Table", "A structured collection of related data organized in rows and columns"], ["Record", "A single row representing one entity in a table"],
        ]),
    },
    "ict-and-computer-science-c1-l6": {
        "data_table": table(["Clause", "Purpose"], [
            ["SELECT", "Chooses which columns to return"], ["WHERE", "Filters rows by condition"],
        ]),
        "formulae": ["SELECT name FROM students WHERE grade = 'A';"],
    },
    "ict-and-computer-science-c1-l7": {
        "data_table": table(["Type", "Scope"], [
            ["LAN", "Local Area Network, confined to a small area like an office"], ["WAN", "Wide Area Network, spans large geographic distances"],
        ]),
    },
    "ict-and-computer-science-c1-l8": {
        "data_table": table(["Layer", "Function"], [
            ["Physical layer", "Transmits raw bits over a medium"], ["Application layer", "Provides network services directly to end users"],
        ]),
    },
    "ict-and-computer-science-c1-l9": {
        "data_table": table(["Protocol", "Role"], [
            ["TCP", "Ensures reliable, ordered delivery of data"], ["IP", "Handles addressing and routing of packets"],
        ]),
    },
    "ict-and-computer-science-c1-l10": {
        "data_table": table(["Threat", "Description"], [
            ["Phishing", "Deceptive messages tricking users into revealing information"], ["Malware", "Software designed to damage or exploit a system"],
        ]),
    },
    "ict-and-computer-science-c1-l11": {
        "data_table": table(["Practice", "Benefit"], [
            ["Multi-factor authentication", "Adds a second verification layer beyond a password"],
        ]),
    },
    "ict-and-computer-science-c1-l12": {
        "data_table": table(["Step", "Purpose"], [
            ["Stakeholder interviews", "Gathers real user needs before designing a system"],
        ]),
    },
    "ict-and-computer-science-c1-l13": {
        "data_table": table(["Model Type", "Purpose"], [
            ["Data flow diagram", "Shows how data moves through a system"],
        ]),
    },
    "ict-and-computer-science-c1-l14": {
        "data_table": table(["Constraint", "Detail"], [
            ["Scope", "Defines what the project will and won't deliver"], ["Timeline", "Sets milestones and deadlines"],
        ]),
    },
    "ict-and-computer-science-c1-l15": {
        "data_table": table(["Model", "Feature"], [
            ["IaaS", "Provides virtualized computing infrastructure"], ["SaaS", "Delivers software over the internet"],
        ]),
    },
    "ict-and-computer-science-c1-l16": {
        "data_table": table(["Feature", "Detail"], [
            ["Mobile computing", "Enables computing tasks on portable, wireless-connected devices"],
        ]),
    },
    "ict-and-computer-science-c1-l17": {
        "data_table": table(["Principle", "Meaning"], [
            ["Usability", "How easily users can accomplish tasks with a system"],
        ]),
    },
    "ict-and-computer-science-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["ITSM", "IT Service Management, structured processes for delivering IT services"],
        ]),
    },
    "ict-and-computer-science-c1-l19": {
        "data_table": table(["Practice", "Reason"], [
            ["Thinking before posting", "Reduces harm from impulsive or harmful online content"],
        ]),
    },
    "ict-and-computer-science-c1-l20": {
        "data_table": table(["Principle", "Meaning"], [
            ["Acceptable use policy", "Defines appropriate use of an organization's IT resources"],
        ]),
    },
    "ict-and-computer-science-c1-l21": {
        "data_table": table(["Component", "Role"], [
            ["CPU", "Executes instructions"], ["RAM", "Volatile working memory"], ["Storage", "Non-volatile long-term data storage"],
        ]),
    },
    "ict-and-computer-science-c1-l22": {
        "data_table": table(["Decimal", "Binary"], [
            ["5", "101"], ["10", "1010"],
        ]),
        "formulae": ["10 in binary is 1010"],
    },
    "ict-and-computer-science-c1-l23": {
        "data_table": table(["Gate", "Output Rule"], [
            ["AND", "True only if both inputs are true"], ["OR", "True if at least one input is true"],
        ]),
    },
    "ict-and-computer-science-c1-l24": {
        "data_table": table(["Type", "Example"], [
            ["Single-user OS", "Windows on a personal laptop"], ["Multi-user OS", "Linux server supporting many concurrent users"],
        ]),
    },
    "ict-and-computer-science-c1-l25": {
        "data_table": table(["Concept", "Meaning"], [
            ["File path", "The location of a file within a directory structure"],
        ]),
    },
    "ict-and-computer-science-c1-l26": {
        "data_table": table(["Structure", "Example"], [
            ["Variable", "x = 5"], ["If statement", "if x > 0: print('positive')"],
        ]),
        "formulae": ["x = 5\nif x > 0:\n    print('positive')"],
    },
    "ict-and-computer-science-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Pseudocode", "Plain-language description of an algorithm's logic before coding"],
        ]),
        "formulae": ["BEGIN\n  READ n\n  IF n > 0 THEN PRINT \"positive\"\nEND"],
    },
    "ict-and-computer-science-c1-l28": {
        "data_table": table(["Structure", "Feature"], [
            ["Array", "Fixed-size, indexed collection of same-type elements"], ["List", "Dynamic, resizable ordered collection"],
        ]),
    },
    "ict-and-computer-science-c1-l29": {
        "data_table": table(["Phase", "Focus"], [
            ["Requirements", "Defines what the software must do"], ["Testing", "Verifies the software behaves correctly"],
        ]),
    },
    "ict-and-computer-science-c1-l30": {
        "data_table": table(["Command", "Purpose"], [
            ["git commit", "Saves a snapshot of staged changes"], ["git push", "Uploads local commits to a remote repository"],
        ]),
        "formulae": ["git add .\ngit commit -m \"message\"\ngit push"],
    },
    "ict-and-computer-science-c1-l31": {
        "data_table": table(["Tag", "Purpose"], [
            ["<h1>", "Defines a top-level heading"], ["<p>", "Defines a paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>\n<p>Content</p>"],
    },
    "ict-and-computer-science-c1-l32": {
        "data_table": table(["Role", "Function"], [
            ["Client", "Requests services or resources"], ["Server", "Provides services or resources in response"],
        ]),
    },
    "ict-and-computer-science-c1-l33": {
        "data_table": table(["Type", "Feature"], [
            ["Document store", "Stores flexible, semi-structured records, e.g. MongoDB"], ["Key-value store", "Stores simple key-value pairs, e.g. Redis"],
        ]),
    },
    "ict-and-computer-science-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Data warehouse", "A centralized repository optimized for analysis and reporting"],
        ]),
    },
    "ict-and-computer-science-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Business intelligence", "Tools and processes that turn data into actionable business insight"],
        ]),
    },
    "ict-and-computer-science-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtualization", "Running multiple virtual machines on a single physical server"],
        ]),
    },
    "ict-and-computer-science-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Container", "A lightweight, portable package bundling an application with its dependencies"],
        ]),
    },
    "ict-and-computer-science-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["IoT", "Internet of Things, physical devices connected and exchanging data online"],
        ]),
    },
    "ict-and-computer-science-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Embedded system", "A specialized computer system built into a larger device"],
        ]),
    },
    "ict-and-computer-science-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Raster graphics", "Images made of a grid of pixels"], ["Vector graphics", "Images made of scalable mathematical paths"],
        ]),
    },
    "ict-and-computer-science-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Encryption", "Converting data into a coded form to prevent unauthorized access"],
        ]),
    },
    "ict-and-computer-science-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital forensics", "Recovering and investigating material found in digital devices"],
        ]),
    },
    "ict-and-computer-science-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["IT governance", "The framework ensuring IT investments align with business goals and rules"],
        ]),
    },
    "ict-and-computer-science-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Enterprise architecture", "A blueprint aligning an organization's IT systems with its strategy"],
        ]),
    },
    "ict-and-computer-science-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems integration", "Connecting different subsystems into one functioning whole"],
        ]),
    },
    "ict-and-computer-science-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Disaster recovery plan", "A documented process for restoring IT systems after a disruption"],
        ]),
    },
    "ict-and-computer-science-c1-l47": {
        "data_table": table(["Strategy", "Detail"], [
            ["3-2-1 backup rule", "3 copies of data, on 2 different media, 1 offsite"],
        ]),
    },
    "ict-and-computer-science-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["E-governance", "Using digital technology to deliver government services"],
        ]),
    },
    "ict-and-computer-science-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["GIS", "Geographic Information System, captures and analyzes spatially referenced data"],
        ]),
    },
    "ict-and-computer-science-c1-l50": {
        "data_table": table(["Type", "Feature"], [
            ["Compiler", "Translates entire source code into machine code before execution"], ["Interpreter", "Executes source code line by line"],
        ]),
    },
    "ict-and-computer-science-c1-l51": {
        "data_table": table(["State", "Meaning"], [
            ["Running", "Actively executing on the CPU"], ["Waiting", "Paused until a resource becomes available"],
        ]),
    },
    "ict-and-computer-science-c1-l52": {
        "data_table": table(["Technique", "Purpose"], [
            ["Paging", "Divides memory into fixed-size blocks for allocation"],
        ]),
    },
    "ict-and-computer-science-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Concurrency", "Multiple tasks making progress during overlapping time periods"], ["Multithreading", "Running multiple threads within a single process"],
        ]),
    },
    "ict-and-computer-science-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed system", "Multiple independent computers that appear to users as one coherent system"],
        ]),
    },
    "ict-and-computer-science-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Blockchain", "A distributed, tamper-resistant ledger of transactions"],
        ]),
    },
    "ict-and-computer-science-c1-l56": {
        "data_table": table(["Standard", "Use"], [
            ["Wi-Fi", "Wireless local area networking"], ["4G/5G", "Wide-area mobile cellular networking"],
        ]),
    },
    "ict-and-computer-science-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Cyber law", "Legal rules governing digital conduct and online activity"],
        ]),
    },
    "ict-and-computer-science-c1-l58": {
        "data_table": table(["Type", "Focus"], [
            ["Unit testing", "Tests individual components in isolation"], ["Integration testing", "Tests how components work together"],
        ]),
    },
    "ict-and-computer-science-c1-l59": {
        "data_table": table(["Principle", "Meaning"], [
            ["Iterative development", "Delivers working software in short, repeated cycles called sprints"],
        ]),
    },
    "ict-and-computer-science-c1-l60": {
        "data_table": table(["Diagram Type", "Purpose"], [
            ["Class diagram", "Models the structure of a system's classes and relationships"], ["Use case diagram", "Models how users interact with a system"],
        ]),
    },
    "ict-computer-science-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a real system's components", "Identifying input, processing, and output for a workflow"],
        ]),
    },
    "ict-computer-science-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Designing a simple schema", "Linking a students table and a courses table"],
        ]),
    },
    "ict-computer-science-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a real system", "Identifying the components of an online ordering system"],
        ]),
    },
    "ict-computer-science-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Turning raw data into insight", "Converting sales numbers into a trend summary"],
        ]),
    },
    "ict-computer-science-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Designing a table structure", "Choosing appropriate columns for a customer record"],
        ]),
    },
    "ict-computer-science-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Writing a basic query", "Retrieving records matching a specific condition"],
        ]),
        "formulae": ["SELECT * FROM orders WHERE total > 100;"],
    },
    "ict-computer-science-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a network type", "Deciding between LAN and WAN for a given scenario"],
        ]),
    },
    "ict-computer-science-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Tracing data through layers", "Following a request from application to physical layer"],
        ]),
    },
    "ict-computer-science-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Explaining packet delivery", "Describing how TCP/IP ensures data arrives intact"],
        ]),
    },
    "ict-computer-science-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a security risk", "Recognizing a phishing attempt in a sample email"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 ICT & Computer Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
