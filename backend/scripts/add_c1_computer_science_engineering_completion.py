#!/usr/bin/env python3
"""Depth pass, C1 Computer Science Engineering: fill in real,
hand-checked data_table content for the 69 C1 Computer Science
Engineering lessons not covered by the earlier breadth-first batch.
Brings C1 Computer Science Engineering to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_computer_science_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "computer-science-engineering-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer science engineering", "Combines computing theory, hardware, and software design"],
        ]),
    },
    "computer-science-engineering-c1-l2": {
        "data_table": table(["Structure", "Use"], [
            ["Array", "Ordered, indexed collection"], ["Linked list", "Sequence of nodes pointing to the next"],
        ]),
    },
    "computer-science-engineering-c1-l4": {
        "data_table": table(["Operator", "Meaning"], [
            ["AND", "True only if both are true"], ["OR", "True if either is true"], ["NOT", "Reverses the value"],
        ]),
    },
    "computer-science-engineering-c1-l5": {
        "data_table": table(["Gate", "Output"], [
            ["AND gate", "1 only if both inputs are 1"], ["OR gate", "1 if either input is 1"],
        ]),
    },
    "computer-science-engineering-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Combinational circuit", "Output depends only on current inputs, no memory"],
        ]),
    },
    "computer-science-engineering-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Sequential circuit", "Output depends on current inputs and stored state"], ["Flip-flop", "A basic memory element storing one bit"],
        ]),
    },
    "computer-science-engineering-c1-l8": {
        "data_table": table(["Paradigm", "Example"], [
            ["Procedural", "C"], ["Object-oriented", "Java"], ["Functional", "Haskell"],
        ]),
    },
    "computer-science-engineering-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Pseudocode", "Informal, structured description of an algorithm's logic"],
        ]),
    },
    "computer-science-engineering-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Assembly language", "A low-level language closely tied to machine instructions"],
        ]),
    },
    "computer-science-engineering-c1-l11": {
        "data_table": table(["Stage", "Purpose"], [
            ["Fetch", "Retrieves the next instruction"], ["Decode", "Interprets the instruction"], ["Execute", "Performs the operation"],
        ]),
    },
    "computer-science-engineering-c1-l12": {
        "data_table": table(["Level", "Speed"], [
            ["Registers", "Fastest, smallest"], ["Cache", "Fast"], ["RAM", "Moderate"], ["Disk", "Slowest, largest"],
        ]),
    },
    "computer-science-engineering-c1-l13": {
        "data_table": table(["Component", "Role"], [
            ["CPU", "Executes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "computer-science-engineering-c1-l14": {
        "data_table": table(["Function", "Purpose"], [
            ["Process management", "Schedules and coordinates running programs"], ["Memory management", "Allocates and tracks memory usage"],
        ]),
    },
    "computer-science-engineering-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["File system", "The method an OS uses to organize and store files"],
        ]),
    },
    "computer-science-engineering-c1-l16": {
        "data_table": table(["Command", "Purpose"], [
            ["ls", "Lists files"], ["cd", "Changes directory"],
        ]),
    },
    "computer-science-engineering-c1-l17": {
        "data_table": table(["Command", "Purpose"], [
            ["git commit", "Saves a snapshot of changes"], ["git push", "Uploads commits to a remote repository"],
        ]),
        "formulae": ["git add .", "git commit -m \"message\""],
    },
    "computer-science-engineering-c1-l18": {
        "data_table": table(["Phase", "Purpose"], [
            ["Requirements", "Defines what the software should do"], ["Testing", "Verifies the software works correctly"],
        ]),
    },
    "computer-science-engineering-c1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Decomposition", "Breaks a problem into smaller parts"], ["Abstraction", "Focuses on essential details, ignoring irrelevant ones"],
        ]),
    },
    "computer-science-engineering-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "computer-science-engineering-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer network", "Interconnected devices that share resources and data"],
        ]),
    },
    "computer-science-engineering-c1-l22": {
        "data_table": table(["Layer", "Function"], [
            ["Physical", "Transmits raw bits"], ["Application", "Interfaces with software applications"],
        ]),
    },
    "computer-science-engineering-c1-l23": {
        "data_table": table(["Protocol", "Function"], [
            ["TCP", "Reliable, ordered delivery of data"], ["IP", "Addresses and routes packets"],
        ]),
    },
    "computer-science-engineering-c1-l24": {
        "data_table": table(["Topology", "Feature"], [
            ["Star", "All devices connect to a central hub"], ["Mesh", "Devices connect to multiple others directly"],
        ]),
    },
    "computer-science-engineering-c1-l25": {
        "data_table": table(["Device", "Function"], [
            ["Router", "Directs data between networks"], ["Switch", "Connects devices within a local network"],
        ]),
    },
    "computer-science-engineering-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["DAC", "Digital-to-Analog Converter, converts digital signals to analog"],
        ]),
    },
    "computer-science-engineering-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Microprocessor", "An integrated circuit that performs the functions of a CPU"],
        ]),
    },
    "computer-science-engineering-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Microcontroller", "A compact chip with a processor, memory, and I/O for embedded tasks"],
        ]),
    },
    "computer-science-engineering-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Embedded system", "A specialized computer system built into a larger device"],
        ]),
    },
    "computer-science-engineering-c1-l30": {
        "data_table": table(["Device Type", "Example"], [
            ["Input", "Keyboard, mouse"], ["Output", "Monitor, printer"],
        ]),
    },
    "computer-science-engineering-c1-l31": {
        "data_table": table(["State", "Meaning"], [
            ["Running", "Currently executing"], ["Waiting", "Waiting for a resource or event"],
        ]),
    },
    "computer-science-engineering-c1-l32": {
        "data_table": table(["Technique", "Purpose"], [
            ["Paging", "Divides memory into fixed-size blocks"],
        ]),
    },
    "computer-science-engineering-c1-l33": {
        "data_table": table(["Algorithm", "Approach"], [
            ["First-Come-First-Served", "Processes run in arrival order"], ["Round Robin", "Each process gets a fixed time slice"],
        ]),
    },
    "computer-science-engineering-c1-l34": {
        "data_table": table(["Condition", "Meaning"], [
            ["Deadlock", "Two or more processes wait indefinitely for each other's resources"],
        ]),
    },
    "computer-science-engineering-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtual memory", "Uses disk space to extend available RAM"],
        ]),
    },
    "computer-science-engineering-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Interrupt", "A signal that pauses normal execution to handle an urgent event"],
        ]),
    },
    "computer-science-engineering-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Compiler", "Translates source code into machine code all at once"], ["Interpreter", "Executes source code line by line"],
        ]),
    },
    "computer-science-engineering-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Lexical analysis", "Breaks source code into tokens for further processing"],
        ]),
    },
    "computer-science-engineering-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Parsing", "Analyzes tokens against grammar rules to build a syntax tree"],
        ]),
    },
    "computer-science-engineering-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Relational database", "Organizes data into tables with rows and columns"],
        ]),
    },
    "computer-science-engineering-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["ER model", "Represents entities and their relationships in a database design"],
        ]),
    },
    "computer-science-engineering-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Normalization", "Organizing database tables to reduce redundancy"],
        ]),
    },
    "computer-science-engineering-c1-l43": {
        "data_table": table(["Property", "Meaning"], [
            ["Atomicity", "A transaction fully completes or fully fails"], ["Consistency", "A transaction leaves the database in a valid state"],
        ]),
    },
    "computer-science-engineering-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Requirements engineering", "Gathering and documenting what a software system must do"],
        ]),
    },
    "computer-science-engineering-c1-l45": {
        "data_table": table(["Test Type", "Focus"], [
            ["Unit testing", "Tests individual components"], ["Integration testing", "Tests components working together"],
        ]),
    },
    "computer-science-engineering-c1-l46": {
        "data_table": table(["Diagram", "Purpose"], [
            ["Class diagram", "Shows classes and their relationships"], ["Sequence diagram", "Shows the order of interactions between objects"],
        ]),
    },
    "computer-science-engineering-c1-l47": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"], ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "computer-science-engineering-c1-l48": {
        "data_table": table(["Tool", "Purpose"], [
            ["Karnaugh map", "Visually simplifies Boolean expressions"],
        ]),
    },
    "computer-science-engineering-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Multiplexer", "Selects one of several inputs to output"], ["Demultiplexer", "Routes one input to one of several outputs"],
        ]),
    },
    "computer-science-engineering-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Register", "A small, fast storage location within the CPU"], ["Counter", "A circuit that counts occurrences of events"],
        ]),
    },
    "computer-science-engineering-c1-l51": {
        "data_table": table(["Signal Type", "Feature"], [
            ["Analog", "Continuous values"], ["Digital", "Discrete values, usually binary"],
        ]),
    },
    "computer-science-engineering-c1-l52": {
        "data_table": table(["Concept", "Meaning"], [
            ["Rasterization", "Converting vector graphics into pixels for display"],
        ]),
    },
    "computer-science-engineering-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Human-computer interaction", "The study of how people interact with computer systems"],
        ]),
    },
    "computer-science-engineering-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Parallel computing", "Performing multiple computations simultaneously"],
        ]),
    },
    "computer-science-engineering-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed system", "A system of independent computers that work together as one"],
        ]),
    },
    "computer-science-engineering-c1-l56": {
        "data_table": table(["Technology", "Example"], [
            ["Wi-Fi", "Wireless local networking"], ["Bluetooth", "Short-range wireless connection"],
        ]),
    },
    "computer-science-engineering-c1-l57": {
        "data_table": table(["Scheme", "Use"], [
            ["ASCII", "Encodes text characters as numbers"], ["Unicode", "Encodes text across all writing systems"],
        ]),
    },
    "computer-science-engineering-c1-l58": {
        "data_table": table(["Method", "Purpose"], [
            ["Parity bit", "Detects single-bit errors"], ["Checksum", "Detects errors across a block of data"],
        ]),
    },
    "computer-science-engineering-c1-l59": {
        "data_table": table(["Metric", "Meaning"], [
            ["Throughput", "Amount of work completed per unit time"], ["Latency", "Time delay before a response"],
        ]),
    },
    "computer-science-engineering-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Software engineer", "Designs and builds software systems"], ["Hardware engineer", "Designs computer hardware components"],
        ]),
    },
    "computer-science-engineering-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a computing field", "Matching a career interest to CS engineering subfields"],
        ]),
    },
    "computer-science-engineering-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a data structure", "Deciding between an array and a linked list for a task"],
        ]),
    },
    "computer-science-engineering-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Converting number systems", "Converting a decimal number to binary and hexadecimal"],
        ]),
        "formulae": ["decimal 13 = binary 1101 = hex D"],
    },
    "computer-science-engineering-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Simplifying a Boolean expression", "Applying De Morgan's laws to a sample expression"],
        ]),
    },
    "computer-science-engineering-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Building a truth table", "Constructing the truth table for an AND-OR combination"],
        ]),
    },
    "computer-science-engineering-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Designing a circuit", "Building a half-adder from basic logic gates"],
        ]),
    },
    "computer-science-engineering-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a flip-flop", "Following a D flip-flop's state across several clock cycles"],
        ]),
    },
    "computer-science-engineering-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing paradigms", "Writing the same task in a procedural and an object-oriented style"],
        ]),
    },
    "computer-science-engineering-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Writing pseudocode", "Drafting the logic for finding the largest number in a list"],
        ]),
    },
    "computer-science-engineering-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Reading assembly", "Tracing what a short sequence of assembly instructions computes"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Computer Science Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Computer Science Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Computer Science Engineering lessons (completing 70/70).")


if __name__ == "__main__":
    main()
