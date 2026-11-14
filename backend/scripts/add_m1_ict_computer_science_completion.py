#!/usr/bin/env python3
"""Depth pass, M1 ICT & Computer Science: fill in real, hand-checked
data_table content for the 99 M1 ICT & Computer Science lessons not
covered by the earlier breadth-first batch. Brings M1 ICT & Computer
Science to full 120/120 coverage.

Lesson ID quirk (matches the C1/C2 subject): l1-l100 use the prefix
"ict-and-computer-science-m1-", while l101-l120 use the shorter
"ict-computer-science-m1-" (no "and"). l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_ict_computer_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-and-computer-science-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Computer science theory", "Covers algorithmic and computational concepts underlying software"],
        ]),
    },
    "ict-and-computer-science-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Advanced computing research", "Explores emerging computational paradigms at the research frontier"],
        ]),
    },
    "ict-and-computer-science-m1-l4": {
        "data_table": table(["System", "Feature"], [
            ["NewSQL", "Combines relational guarantees with horizontal scalability"],
        ]),
    },
    "ict-and-computer-science-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Network function virtualization", "Replaces dedicated hardware appliances with software-defined network functions"],
        ]),
    },
    "ict-and-computer-science-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Threat intelligence", "Systematically collects and analyzes information about potential adversaries"],
        ]),
    },
    "ict-and-computer-science-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Governance, risk, and compliance", "Aligns security posture with regulatory and organizational requirements"],
        ]),
    },
    "ict-and-computer-science-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Model-driven architecture", "Generates system implementation from abstract, platform-independent models"],
        ]),
    },
    "ict-and-computer-science-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["IT portfolio management", "Prioritizes and balances investment across a collection of IT projects"],
        ]),
    },
    "ict-and-computer-science-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["ERP customization strategy", "Balances configuration flexibility against upgrade complexity"],
        ]),
    },
    "ict-and-computer-science-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Process mining", "Analyzes event log data to reconstruct and improve actual business processes"],
        ]),
    },
    "ict-and-computer-science-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Enterprise risk framework", "Systematically identifies and manages risk across an organization's IT operations"],
        ]),
    },
    "ict-and-computer-science-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Cloud-native architecture", "Designs applications specifically to exploit cloud elasticity and scalability"],
        ]),
    },
    "ict-and-computer-science-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["AI-IoT convergence", "Combines edge sensing devices with intelligent on-device processing"],
        ]),
    },
    "ict-and-computer-science-m1-l15": {
        "data_table": table(["Model", "Feature"], [
            ["Blockchain governance", "Determines how a decentralized network makes and enforces protocol decisions"],
        ]),
    },
    "ict-and-computer-science-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["ICT for development policy", "Shapes how technology access and regulation affect development outcomes"],
        ]),
    },
    "ict-and-computer-science-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Data mesh", "Decentralizes data ownership to domain teams rather than a single central platform"],
        ]),
    },
    "ict-and-computer-science-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Hybrid infrastructure", "Combines on-premises and cloud resources into a unified operational design"],
        ]),
    },
    "ict-and-computer-science-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Responsible innovation", "Balances technological advancement with ethical and societal consideration"],
        ]),
    },
    "ict-and-computer-science-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone systems project", "Defends an original ICT systems research contribution and its recommendations"],
        ]),
    },
    "ict-and-computer-science-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed protocol verification", "Formally proves a protocol behaves correctly under all possible message orderings"],
        ]),
    },
    "ict-and-computer-science-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Byzantine fault tolerance", "Keeps a distributed system correct even when some nodes behave arbitrarily or maliciously"],
        ]),
    },
    "ict-and-computer-science-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["CRDT", "A data structure that merges concurrent updates deterministically without conflict"],
        ]),
    },
    "ict-and-computer-science-m1-l24": {
        "data_table": table(["Pattern", "Detail"], [
            ["Event sourcing", "Persists state as a sequence of events rather than a mutable snapshot"],
            ["CQRS", "Separates read and write models to optimize each independently"],
        ]),
    },
    "ict-and-computer-science-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Service mesh", "A dedicated infrastructure layer managing service-to-service communication"],
        ]),
    },
    "ict-and-computer-science-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Container orchestration", "Automates deployment, scaling, and management of containerized applications"],
        ]),
    },
    "ict-and-computer-science-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Serverless computing", "Runs code without managing underlying server infrastructure, scaling automatically"],
        ]),
    },
    "ict-and-computer-science-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Infrastructure as code", "Manages infrastructure through versioned, declarative configuration files"],
        ]),
    },
    "ict-and-computer-science-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Chaos engineering", "Deliberately injects failure to test and improve system resilience"],
        ]),
    },
    "ict-and-computer-science-m1-l30": {
        "data_table": table(["Pillar", "Purpose"], [
            ["Traces", "Follows a single request's path across distributed services"],
            ["Metrics", "Aggregates numeric system performance indicators over time"],
        ]),
    },
    "ict-and-computer-science-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Master data management", "Establishes a single authoritative source for critical shared business data"],
        ]),
    },
    "ict-and-computer-science-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Stream processing", "Continuously processes data as it arrives rather than in periodic batches"],
        ]),
    },
    "ict-and-computer-science-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Columnar storage", "Stores data by column rather than row, accelerating analytical queries"],
        ]),
    },
    "ict-and-computer-science-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Graph query optimization", "Improves traversal efficiency across densely connected relationship data"],
        ]),
    },
    "ict-and-computer-science-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Time-series database", "Optimized to store and query data indexed by timestamp at high ingestion rates"],
        ]),
    },
    "ict-and-computer-science-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["In-memory computing", "Keeps data in RAM rather than disk to dramatically reduce access latency"],
        ]),
    },
    "ict-and-computer-science-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["RISC-V", "An open, royalty-free instruction set architecture enabling flexible hardware design"],
        ]),
    },
    "ict-and-computer-science-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Hardware-software co-design", "Jointly optimizes hardware and software to meet performance goals"],
        ]),
    },
    "ict-and-computer-science-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["FPGA acceleration", "Reconfigurable hardware customizes circuits for a specific computational task"],
        ]),
    },
    "ict-and-computer-science-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Real-time operating system", "Guarantees deterministic response times for time-critical embedded tasks"],
        ]),
    },
    "ict-and-computer-science-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Autonomous systems safety verification", "Formally validates that automated systems behave safely across scenarios"],
        ]),
    },
    "ict-and-computer-science-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Explainable AI", "Makes model decisions interpretable for enterprise accountability and trust"],
        ]),
    },
    "ict-and-computer-science-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["AI governance framework", "Establishes organizational policy for responsible AI deployment and oversight"],
        ]),
    },
    "ict-and-computer-science-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["ITIL service management", "Standardizes IT service delivery processes at enterprise scale"],
        ]),
    },
    "ict-and-computer-science-m1-l45": {
        "data_table": table(["Framework", "Purpose"], [
            ["TOGAF", "Structures how an organization plans and governs its IT architecture"],
        ]),
    },
    "ict-and-computer-science-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster recovery planning", "Prepares organizations to restore IT operations after a major disruption"],
        ]),
    },
    "ict-and-computer-science-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Sustainable computing", "Reduces the energy and environmental footprint of IT infrastructure"],
        ]),
    },
    "ict-and-computer-science-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Forensics readiness", "Prepares an organization in advance to preserve digital evidence effectively"],
        ]),
    },
    "ict-and-computer-science-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Threat hunting", "Proactively searches for hidden adversaries rather than waiting for alerts"],
        ]),
    },
    "ict-and-computer-science-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Security operations center", "Centralizes monitoring, detection, and response to security incidents"],
        ]),
    },
    "ict-and-computer-science-m1-l51": {
        "data_table": table(["Principle", "Detail"], [
            ["Zero trust", "Never implicitly trusts any user or device, verifying continuously regardless of network location"],
        ]),
    },
    "ict-and-computer-science-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Identity and access management at scale", "Centralizes authentication and authorization across large, complex organizations"],
        ]),
    },
    "ict-and-computer-science-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Blockchain interoperability", "Enables communication and value transfer between separate blockchain networks"],
        ]),
    },
    "ict-and-computer-science-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Smart contract verification", "Applies formal methods to catch costly bugs before contract deployment"],
        ]),
    },
    "ict-and-computer-science-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Decentralized identity", "Gives individuals direct control over their own digital identity credentials"],
        ]),
    },
    "ict-and-computer-science-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum networking", "Uses quantum properties like entanglement to enable novel secure communication"],
        ]),
    },
    "ict-and-computer-science-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Post-quantum cryptography", "Develops encryption resistant to attacks from future quantum computers"],
        ]),
    },
    "ict-and-computer-science-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Software-defined networking", "Separates network control logic from the underlying forwarding hardware"],
        ]),
    },
    "ict-and-computer-science-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["5G core network", "A cloud-native architecture enabling network slicing and low-latency service"],
        ]),
    },
    "ict-and-computer-science-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Edge computing orchestration", "Coordinates distributed compute resources close to the data source"],
        ]),
    },
    "ict-and-computer-science-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational complexity advances", "Refines understanding of problem classes' inherent computational difficulty"],
        ]),
    },
    "ict-and-computer-science-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Automata theory", "Studies abstract machines and the languages they can recognize"],
        ]),
    },
    "ict-and-computer-science-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Program synthesis", "Automatically generates code satisfying a given formal specification"],
        ]),
    },
    "ict-and-computer-science-m1-l64": {
        "data_table": table(["Type", "Detail"], [
            ["Static analysis", "Examines code without executing it to catch potential defects"],
            ["Dynamic analysis", "Examines program behavior during actual execution"],
        ]),
    },
    "ict-and-computer-science-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Malware reverse engineering", "Disassembles malicious code to understand its behavior and origin"],
        ]),
    },
    "ict-and-computer-science-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Penetration testing", "Authorized simulated attacks reveal exploitable security vulnerabilities"],
        ]),
    },
    "ict-and-computer-science-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Secure coding for critical systems", "Applies rigorous defensive practice where failure carries severe consequences"],
        ]),
    },
    "ict-and-computer-science-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Differential privacy", "Adds calibrated noise to data analysis to protect individual privacy statistically"],
        ]),
    },
    "ict-and-computer-science-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Federated learning", "Trains a shared model across decentralized data without centralizing raw data"],
        ]),
    },
    "ict-and-computer-science-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["TinyML", "Runs compact machine learning models directly on resource-constrained edge devices"],
        ]),
    },
    "ict-and-computer-science-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Neuromorphic computing", "Hardware architecture modeled on the structure and efficiency of biological neurons"],
        ]),
    },
    "ict-and-computer-science-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational geometry", "Designs algorithms for solving problems involving geometric shapes and spaces"],
        ]),
    },
    "ict-and-computer-science-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Algorithmic game theory", "Analyzes computational systems where participants act strategically"],
        ]),
    },
    "ict-and-computer-science-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Social graph analysis", "Applies network science to understand structure and influence in social systems"],
        ]),
    },
    "ict-and-computer-science-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Recommender system at scale", "Balances relevance, diversity, and computational cost for millions of users"],
        ]),
    },
    "ict-and-computer-science-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Search engine ranking", "Combines relevance signals to order results by likely usefulness to the query"],
        ]),
    },
    "ict-and-computer-science-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed consensus algorithm", "Enables multiple nodes to agree on a single value despite failures"],
        ]),
    },
    "ict-and-computer-science-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital twin", "A virtual model mirrors a physical system's real-time state for simulation"],
        ]),
    },
    "ict-and-computer-science-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Knowledge graph", "Represents entities and their relationships to enable structured semantic queries"],
        ]),
    },
    "ict-and-computer-science-m1-l80": {
        "data_table": table(["Metric", "Purpose"], [
            ["Precision/recall", "Evaluates how well an information retrieval system returns relevant results"],
        ]),
    },
    "ict-and-computer-science-m1-l81": {
        "data_table": table(["Method", "Purpose"], [
            ["Usability testing", "Observes real users to identify interface friction points"],
        ]),
    },
    "ict-and-computer-science-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Accessibility engineering", "Designs software usable by people with a wide range of abilities"],
        ]),
    },
    "ict-and-computer-science-m1-l83": {
        "data_table": table(["Strategy", "Detail"], [
            ["Advanced testing strategy", "Combines multiple testing levels to maximize defect detection efficiently"],
        ]),
    },
    "ict-and-computer-science-m1-l84": {
        "data_table": table(["Tool", "Purpose"], [
            ["TLA+", "A formal specification language for modeling and verifying concurrent system designs"],
        ]),
    },
    "ict-and-computer-science-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Model checking", "Exhaustively verifies a finite-state system against a formal specification"],
        ]),
    },
    "ict-and-computer-science-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["GPU computing", "Exploits massively parallel architecture for data-intensive computation"],
        ]),
    },
    "ict-and-computer-science-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["High-performance computing", "Coordinates many processors to solve computationally intensive problems"],
        ]),
    },
    "ict-and-computer-science-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Robotic perception", "Uses computer vision to interpret sensor data for autonomous decision-making"],
        ]),
    },
    "ict-and-computer-science-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital signal processing", "Manipulates discretized signals mathematically for filtering and analysis"],
        ]),
    },
    "ict-and-computer-science-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Conversational AI design", "Combines language understanding with dialogue management for natural interaction"],
        ]),
    },
    "ict-and-computer-science-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Type theory", "Provides the formal foundation for safe, expressive programming language design"],
        ]),
    },
    "ict-and-computer-science-m1-l92": {
        "data_table": table(["Technique", "Purpose"], [
            ["Loop unrolling", "Reduces loop overhead by replicating the loop body"],
        ]),
    },
    "ict-and-computer-science-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Virtualization internals", "Manages hardware abstraction to run multiple isolated operating system instances"],
        ]),
    },
    "ict-and-computer-science-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Wireless sensor network protocol", "Balances energy efficiency with reliable data delivery across sensor nodes"],
        ]),
    },
    "ict-and-computer-science-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Mesh networking", "Nodes relay traffic for each other, providing resilient decentralized connectivity"],
        ]),
    },
    "ict-and-computer-science-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Non-terrestrial network", "Satellite constellations extend connectivity beyond traditional ground infrastructure"],
        ]),
    },
    "ict-and-computer-science-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Data warehousing for analytics", "Structures historical data for efficient large-scale business intelligence queries"],
        ]),
    },
    "ict-and-computer-science-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Bioinformatics computing infrastructure", "Supports the massive storage and processing demands of genomic data analysis"],
        ]),
    },
    "ict-and-computer-science-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum algorithm design", "Exploits superposition and entanglement for computational advantage over classical methods"],
        ]),
    },
    "ict-and-computer-science-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Site reliability engineering", "Applies software engineering discipline to operational reliability and uptime"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Information System Component", "Role"], [
        ["Hardware", "Physical devices"],
        ["Software", "Programs and applications"],
        ["Data", "Information processed"],
        ["People", "Users and IT staff"],
        ["Processes", "Procedures for using the system"],
    ]),
}

# l101-l120 use the shorter prefix and are "Worked Analysis" companions to l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"ict-and-computer-science-m1-l{base_n}"
    worked_key = f"ict-computer-science-m1-l{worked_n}"
    if base_key in CHARTS:
        CHARTS[worked_key] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[worked_key] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 ICT & Computer Science lessons (completing 120/120).")


if __name__ == "__main__":
    main()
