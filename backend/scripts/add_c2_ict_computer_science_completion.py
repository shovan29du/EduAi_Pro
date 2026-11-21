#!/usr/bin/env python3
"""Depth pass, C2 ICT & Computer Science: fill in real, hand-checked
data_table content for the 69 C2 ICT & Computer Science lessons not
covered by the earlier breadth-first batch. Brings C2 ICT & Computer
Science to full 70/70 coverage.

Lesson ID quirk (matches the C1 subject): l1-l63 use the prefix
"ict-and-computer-science-c2-", while l64-l70 use the shorter
"ict-computer-science-c2-" (no "and"). l61-l63 are "Foundations 2"
lessons revisiting l22, l26, and l53; l64-l70 are "Worked Analysis"
companions to l1-l7. l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_ict_computer_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-and-computer-science-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Networks & databases foundations", "Connects data storage design with the infrastructure that moves it"],
        ]),
    },
    "ict-and-computer-science-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Computer science theory foundations", "Covers algorithmic and computational concepts underlying software"],
        ]),
    },
    "ict-and-computer-science-c2-l4": {
        "data_table": table(["Element", "Detail"], [
            ["Entity-relationship model", "Represents entities, attributes, and relationships in a database design"],
        ]),
    },
    "ict-and-computer-science-c2-l5": {
        "data_table": table(["Join Type", "Result"], [
            ["INNER JOIN", "Returns only matching rows from both tables"],
            ["LEFT JOIN", "Returns all rows from the left table plus matches from the right"],
        ]),
    },
    "ict-and-computer-science-c2-l6": {
        "data_table": table(["Property", "Meaning"], [
            ["Atomicity", "A transaction completes fully or not at all"],
            ["Durability", "Committed changes persist even after a system failure"],
        ]),
    },
    "ict-and-computer-science-c2-l7": {
        "data_table": table(["Protocol", "Purpose"], [
            ["HTTP", "Transfers web page content between client and server"],
            ["DNS", "Translates domain names into IP addresses"],
        ]),
    },
    "ict-and-computer-science-c2-l8": {
        "data_table": table(["Tool", "Purpose"], [
            ["Firewall", "Filters network traffic based on defined security rules"],
            ["Encryption", "Protects data confidentiality in transit or at rest"],
        ]),
    },
    "ict-and-computer-science-c2-l9": {
        "data_table": table(["Standard", "Feature"], [
            ["WPA3", "Current wireless security standard offering stronger encryption than predecessors"],
        ]),
    },
    "ict-and-computer-science-c2-l10": {
        "data_table": table(["Element", "Purpose"], [
            ["Data flow diagram", "Visualizes how data moves through a system's processes"],
        ]),
    },
    "ict-and-computer-science-c2-l11": {
        "data_table": table(["Element", "Purpose"], [
            ["Use case diagram", "Shows how actors interact with system functions"],
        ]),
    },
    "ict-and-computer-science-c2-l12": {
        "data_table": table(["Approach", "Feature"], [
            ["Structured (waterfall)", "Sequential phases completed in order before the next begins"],
            ["Agile", "Iterative cycles adapting to changing requirements"],
        ]),
    },
    "ict-and-computer-science-c2-l13": {
        "data_table": table(["Element", "Purpose"], [
            ["BPMN diagram", "Standardizes notation for modeling business processes"],
        ]),
    },
    "ict-and-computer-science-c2-l14": {
        "data_table": table(["Framework", "Focus"], [
            ["COBIT", "IT governance framework focused on control and risk management"],
        ]),
    },
    "ict-and-computer-science-c2-l15": {
        "data_table": table(["Model", "Feature"], [
            ["IaaS", "Provides virtualized computing infrastructure"],
            ["SaaS", "Delivers ready-to-use software over the internet"],
        ]),
    },
    "ict-and-computer-science-c2-l16": {
        "data_table": table(["Approach", "Trade-off"], [
            ["Native app", "Best performance but requires separate codebases per platform"],
            ["Cross-platform app", "Shared codebase but potential performance trade-offs"],
        ]),
    },
    "ict-and-computer-science-c2-l17": {
        "data_table": table(["Method", "Purpose"], [
            ["Usability testing", "Observes real users to identify interface friction points"],
        ]),
    },
    "ict-and-computer-science-c2-l18": {
        "data_table": table(["Process", "Focus"], [
            ["Incident management", "Restores normal service as quickly as possible"],
            ["Problem management", "Identifies and eliminates the underlying root cause"],
        ]),
    },
    "ict-and-computer-science-c2-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital divide", "Unequal access to technology and connectivity across populations"],
        ]),
    },
    "ict-and-computer-science-c2-l20": {
        "data_table": table(["License Type", "Feature"], [
            ["Open-source license", "Permits viewing, modifying, and redistributing source code"],
            ["Proprietary license", "Restricts use and redistribution of the software"],
        ]),
    },
    "ict-and-computer-science-c2-l21": {
        "data_table": table(["Architecture", "Feature"], [
            ["Von Neumann", "Shares one memory for instructions and data"],
            ["Harvard", "Uses separate memory for instructions and data"],
        ]),
    },
    "ict-and-computer-science-c2-l22": {
        "data_table": table(["Algorithm", "Feature"], [
            ["Round robin", "Gives each process a fixed time slice in rotation"],
            ["Shortest job first", "Prioritizes the process with the smallest execution time"],
        ]),
    },
    "ict-and-computer-science-c2-l23": {
        "data_table": table(["Condition", "Purpose"], [
            ["Mutual exclusion", "One of four necessary conditions for a deadlock to occur"],
        ]),
    },
    "ict-and-computer-science-c2-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Paging", "Divides memory into fixed-size blocks to support virtual memory"],
        ]),
    },
    "ict-and-computer-science-c2-l25": {
        "data_table": table(["Structure", "Use Case"], [
            ["Tree", "Represents hierarchical relationships"],
            ["Graph", "Represents arbitrary connections between nodes"],
        ]),
    },
    "ict-and-computer-science-c2-l26": {
        "data_table": table(["Notation", "Meaning"], [
            ["O(1)", "Constant time regardless of input size"],
            ["O(n log n)", "Time grows proportionally to n times log n"],
        ]),
    },
    "ict-and-computer-science-c2-l27": {
        "data_table": table(["Algorithm", "Complexity"], [
            ["Binary search", "O(log n), requires sorted data"],
            ["Linear search", "O(n), works on unsorted data"],
        ]),
    },
    "ict-and-computer-science-c2-l28": {
        "data_table": table(["Principle", "Detail"], [
            ["Inheritance", "A class derives shared behavior from a parent class"],
            ["Polymorphism", "Objects of different types respond to the same interface differently"],
        ]),
    },
    "ict-and-computer-science-c2-l29": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Singleton", "Ensures a class has only one shared instance"],
        ]),
    },
    "ict-and-computer-science-c2-l30": {
        "data_table": table(["Test Level", "Scope"], [
            ["Unit test", "Verifies a single function or component in isolation"],
            ["System test", "Verifies the complete integrated system"],
        ]),
    },
    "ict-and-computer-science-c2-l31": {
        "data_table": table(["Concept", "Purpose"], [
            ["CI/CD pipeline", "Automates building, testing, and deploying code changes"],
        ]),
    },
    "ict-and-computer-science-c2-l32": {
        "data_table": table(["Principle", "Detail"], [
            ["RESTful API design", "Resources are addressed by URLs and manipulated via standard HTTP methods"],
        ]),
    },
    "ict-and-computer-science-c2-l33": {
        "data_table": table(["Technology", "Role"], [
            ["JavaScript framework", "Structures reusable, dynamic front-end web components"],
        ]),
    },
    "ict-and-computer-science-c2-l34": {
        "data_table": table(["Model", "Feature"], [
            ["Document store", "Stores flexible, schema-less JSON-like documents"],
            ["Graph database", "Optimized for querying densely connected relationships"],
        ]),
    },
    "ict-and-computer-science-c2-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Extract, Transform, Load", "Moves and reshapes data from source systems into a data warehouse"],
        ]),
    },
    "ict-and-computer-science-c2-l36": {
        "data_table": table(["Element", "Purpose"], [
            ["Business intelligence dashboard", "Visualizes key metrics for rapid, data-driven decision-making"],
        ]),
    },
    "ict-and-computer-science-c2-l37": {
        "data_table": table(["Component", "Role"], [
            ["Hypervisor", "Allows multiple virtual machines to run on shared physical hardware"],
        ]),
    },
    "ict-and-computer-science-c2-l38": {
        "data_table": table(["Concept", "Purpose"], [
            ["Kubernetes orchestration", "Automates deployment, scaling, and management of containerized applications"],
        ]),
    },
    "ict-and-computer-science-c2-l39": {
        "data_table": table(["Layer", "Function"], [
            ["Device layer", "Sensors and actuators collect and act on physical-world data"],
            ["Network layer", "Transmits IoT data between devices and cloud systems"],
        ]),
    },
    "ict-and-computer-science-c2-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Embedded system", "A dedicated computer built into a larger device for a specific function"],
        ]),
    },
    "ict-and-computer-science-c2-l41": {
        "data_table": table(["Stage", "Purpose"], [
            ["Rendering pipeline", "Converts 3D scene data into a 2D displayed image"],
        ]),
    },
    "ict-and-computer-science-c2-l42": {
        "data_table": table(["Key Type", "Use"], [
            ["Public key", "Shared openly, used to encrypt or verify"],
            ["Private key", "Kept secret, used to decrypt or sign"],
        ]),
    },
    "ict-and-computer-science-c2-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Chain of custody", "Documents evidence handling to preserve its integrity for legal use"],
        ]),
    },
    "ict-and-computer-science-c2-l44": {
        "data_table": table(["Framework", "Focus"], [
            ["GDPR", "EU regulation governing personal data protection and privacy rights"],
        ]),
    },
    "ict-and-computer-science-c2-l45": {
        "data_table": table(["Framework", "Purpose"], [
            ["TOGAF", "Structures how an organization plans and governs its IT architecture"],
        ]),
    },
    "ict-and-computer-science-c2-l46": {
        "data_table": table(["Component", "Role"], [
            ["Middleware", "Connects and mediates communication between separate software systems"],
        ]),
    },
    "ict-and-computer-science-c2-l47": {
        "data_table": table(["Metric", "Meaning"], [
            ["RTO", "Maximum acceptable time to restore a system after a disruption"],
            ["RPO", "Maximum acceptable amount of data loss measured in time"],
        ]),
    },
    "ict-and-computer-science-c2-l48": {
        "data_table": table(["Type", "Feature"], [
            ["Full backup", "Copies all data every time, slowest but simplest to restore"],
            ["Incremental backup", "Copies only data changed since the last backup"],
        ]),
    },
    "ict-and-computer-science-c2-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["E-governance", "Delivers government services digitally to improve access and efficiency"],
        ]),
    },
    "ict-and-computer-science-c2-l50": {
        "data_table": table(["Technique", "Purpose"], [
            ["Spatial analysis", "Examines patterns and relationships in geographically referenced data"],
        ]),
    },
    "ict-and-computer-science-c2-l51": {
        "data_table": table(["Stage", "Purpose"], [
            ["Lexical analysis", "Breaks source code into tokens before parsing"],
            ["Parsing", "Builds a syntax tree from the token stream"],
        ]),
    },
    "ict-and-computer-science-c2-l52": {
        "data_table": table(["Property", "Trade-off"], [
            ["CAP theorem", "A distributed system can guarantee at most two of consistency, availability, partition tolerance"],
        ]),
    },
    "ict-and-computer-science-c2-l53": {
        "data_table": table(["Application", "Detail"], [
            ["Blockchain beyond cryptocurrency", "Supply chain tracking and verifiable digital records are common use cases"],
        ]),
    },
    "ict-and-computer-science-c2-l54": {
        "data_table": table(["Feature", "Detail"], [
            ["5G networks", "Offer higher bandwidth and lower latency than prior cellular generations"],
        ]),
    },
    "ict-and-computer-science-c2-l55": {
        "data_table": table(["Topic", "Detail"], [
            ["Digital IP law", "Governs how creative and technical works are protected online"],
        ]),
    },
    "ict-and-computer-science-c2-l56": {
        "data_table": table(["Metric", "Purpose"], [
            ["Defect density", "Measures the number of confirmed defects relative to code size"],
        ]),
    },
    "ict-and-computer-science-c2-l57": {
        "data_table": table(["Element", "Purpose"], [
            ["Sprint planning", "Selects and estimates the work for an upcoming Scrum iteration"],
        ]),
    },
    "ict-and-computer-science-c2-l58": {
        "data_table": table(["Diagram", "Purpose"], [
            ["Class diagram", "Shows a system's classes, attributes, and relationships"],
            ["Sequence diagram", "Shows the order of interactions between objects over time"],
        ]),
    },
    "ict-and-computer-science-c2-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Edge computing", "Processes data closer to its source to reduce latency"],
        ]),
    },
    "ict-and-computer-science-c2-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Qubit", "Basic unit of quantum information that can exist in superposition"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Normal Form", "Purpose"], [
    ["1NF", "Eliminate repeating groups; atomic values"],
    ["2NF", "Remove partial dependencies"],
    ["3NF", "Remove transitive dependencies"],
])

# l61-l63 "Foundations 2" lessons revisit l22, l26, and l53.
FOUNDATIONS_2_MAP = {61: 22, 62: 26, 63: 53}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"ict-and-computer-science-c2-l{base_n}"
    CHARTS[f"ict-and-computer-science-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l64-l70 use the shorter prefix and are "Worked Analysis" companions to l1-l7.
WORKED_ANALYSIS_MAP = {64: 1, 65: 2, 66: 3, 67: 4, 68: 5, 69: 6, 70: 7}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"ict-and-computer-science-c2-l{base_n}"
    worked_key = f"ict-computer-science-c2-l{worked_n}"
    if base_key in CHARTS:
        CHARTS[worked_key] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[worked_key] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 ICT & Computer Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
