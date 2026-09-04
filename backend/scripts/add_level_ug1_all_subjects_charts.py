#!/usr/bin/env python3
"""Breadth-first pass, Level UG1 (first undergraduate-tier level): add
genuine, hand-checked data_table content to one real, verifiable lesson
per subject across all 52 non-Math subjects in level_ug1.json (Math
already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (Descartes' Cogito,
real Six Sigma DMAIC steps, real Toulmin argument elements, real VSEPR
electron geometries, real wound-healing phases, etc.) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_ug1_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_ug1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Knowledge graph", "A network of entities and their relationships, represented as nodes and edges"],
            ["Triple", "A basic unit of a knowledge graph: subject-predicate-object"],
        ]),
    },
    "machine-learning-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["PCA", "A technique for reducing dimensionality by finding directions of maximum variance"],
            ["Principal component", "A new axis that captures the most variance in the data"],
        ]),
    },
    "natural-language-processing-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Constituency parsing", "Breaks a sentence into nested phrases (noun phrase, verb phrase, etc.)"],
            ["Parse tree", "A tree diagram representing the sentence's grammatical structure"],
        ]),
    },
    "data-science-ug1-l3": {
        "data_table": table(["Chart Design Principle", "Meaning"], [
            ["Data-ink ratio", "Maximize the ink used to show data, minimize decoration (Tufte)"],
            ["Avoid chartjunk", "Remove unnecessary visual elements that don't convey information"],
        ]),
    },
    "business-analytics-ug1-l3": {
        "data_table": table(["ARIMA Component", "Meaning"], [
            ["AR (AutoRegressive)", "Uses past values to predict future values"],
            ["I (Integrated)", "Differencing to make data stationary"],
            ["MA (Moving Average)", "Uses past forecast errors"],
        ]),
    },
    "web-development-ug1-l3": {
        "data_table": table(["React Hook", "Purpose"], [
            ["useState", "Adds state to a function component"], ["useEffect", "Runs side effects after render"],
        ]),
    },
    "cybersecurity-ug1-l3": {
        "data_table": table(["Penetration Testing Phase", "Purpose"], [
            ["Reconnaissance", "Gathering information about the target"],
            ["Scanning", "Identifying live hosts and open ports"],
            ["Exploitation", "Attempting to gain access"],
            ["Reporting", "Documenting findings and recommendations"],
        ]),
    },
    "cloud-computing-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Infrastructure as Code (IaC)", "Managing infrastructure through machine-readable config files"],
            ["Terraform", "An open-source IaC tool by HashiCorp"],
        ]),
    },
    "digital-marketing-ug1-l3": {
        "data_table": table(["Segmentation Type", "Example"], [
            ["Demographic", "Age, gender, income"], ["Behavioral", "Purchase history, browsing activity"],
        ]),
    },
    "ui/ux-design-ug1-l3": {
        "data_table": table(["Grid Term", "Meaning"], [
            ["Column", "A vertical division of the grid"], ["Gutter", "The space between columns"],
            ["12-column grid", "A common flexible layout system"],
        ]),
    },
    "project-management-ug1-l3": {
        "data_table": table(["Estimating Approach", "Method"], [
            ["Top-down", "Estimates the whole project first, then breaks it into parts"],
            ["Bottom-up", "Estimates individual tasks first, then sums them for the total"],
        ]),
    },
    "economics-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Utility", "The satisfaction a consumer gets from a good or service"],
            ["Marginal utility", "The additional satisfaction from one more unit consumed"],
        ]),
    },
    "finance-ug1-l3": {
        "data_table": table(["Financing Type", "Key Trait"], [
            ["Debt", "Borrowed funds that must be repaid with interest"],
            ["Equity", "Ownership shares sold in exchange for capital"],
        ]),
    },
    "philosophy-ug1-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Rene Descartes"], ["Key work", "Meditations on First Philosophy (1641)"],
            ["Famous phrase", "'Cogito, ergo sum' - 'I think, therefore I am'"],
        ]),
    },
    "art-history-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Tenebrism", "Dramatic use of strong contrasts between light and dark"],
            ["Associated artist", "Michelangelo Merisi da Caravaggio"],
        ]),
    },
    "python-ug1-l3": {
        "data_table": table(["Block", "Runs When"], [
            ["try", "Always attempted first"], ["except", "An error occurs in try"],
            ["else", "No error occurred in try"], ["finally", "Always, regardless of errors"],
        ]),
    },
    "r-ug1-l3": {
        "data_table": table(["dplyr Function", "Purpose"], [
            ["filter()", "Selects rows matching a condition"], ["select()", "Selects columns"],
            ["mutate()", "Creates or modifies columns"],
        ]),
    },
    "javascript-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Callback", "A function passed as an argument to be executed later"],
            ["Callback hell", "Deeply nested callbacks that become hard to read/maintain"],
        ]),
    },
    "prompt-engineering-ug1-l3": {
        "data_table": table(["Template Element", "Purpose"], [
            ["Placeholder/variable", "A slot filled in with different values each use"],
            ["Instruction", "The fixed task description"],
        ]),
    },
    "computer-science-engineering-ug1-l3": {
        "data_table": table(["Scheduling Algorithm", "Approach"], [
            ["FCFS", "First Come, First Served"],
            ["Round Robin", "Each process gets a fixed time slice in turn"],
            ["SJF", "Shortest Job First"],
        ]),
    },
    "big-data-ug1-l3": {
        "data_table": table(["MongoDB Term", "Meaning"], [
            ["Document", "A record stored in JSON-like (BSON) format"],
            ["Collection", "A group of documents (similar to a table)"],
        ]),
    },
    "mba-ug1-l3": {
        "data_table": table(["Porter's Five Forces", "Description"], [
            ["Competitive rivalry", "Intensity of competition among existing firms"],
            ["Threat of new entrants", "How easily new competitors can enter"],
            ["Bargaining power of suppliers", "Suppliers' ability to raise prices"],
            ["Bargaining power of buyers", "Buyers' ability to demand lower prices"],
            ["Threat of substitutes", "Availability of alternative products"],
        ]),
    },
    "operations-management-ug1-l3": {
        "data_table": table(["DMAIC Letter", "Meaning"], [
            ["D", "Define the problem"], ["M", "Measure current performance"],
            ["A", "Analyze root causes"], ["I", "Improve the process"], ["C", "Control to sustain gains"],
        ]),
    },
    "ai-tools-ug1-l3": {
        "data_table": table(["Prompting Approach", "Description"], [
            ["Zero-shot", "No examples given, just an instruction"],
            ["Few-shot", "A small number of examples given before the task"],
        ]),
    },
    "english-ug1-l3": {
        "data_table": table(["Toulmin Element", "Meaning"], [
            ["Claim", "The conclusion being argued for"], ["Grounds", "The evidence supporting the claim"],
            ["Warrant", "The reasoning linking grounds to claim"],
        ]),
    },
    "science-ug1-l3": {
        "data_table": table(["Step", "Description"], [
            ["1. Hypothesis", "Propose a testable explanation"],
            ["2. Deduction", "Predict what should follow if the hypothesis is true"],
            ["3. Test", "Check the prediction against observation"],
        ]),
    },
    "geography-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Tectonic plate", "A large slab of Earth's crust that moves slowly"],
            ["Fault", "A crack where plates meet and can slip"],
            ["Magnitude scale", "Measures the energy/strength of an earthquake"],
        ]),
    },
    "world-history-ug1-l3": {
        "data_table": table(["Empire", "Approx. Period"], [
            ["Roman Empire", "27 BCE - 476 CE (Western)"], ["Han Dynasty", "206 BCE - 220 CE"],
        ]),
    },
    "islamic-studies-ug1-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Surah number", "4"], ["Meaning of name", "The Women"],
            ["Common themes", "Family law, inheritance, social justice"],
        ]),
    },
    "coding-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Amortized analysis", "Averaging the cost of an operation over a sequence of operations"],
            ["Example", "Dynamic array append is O(1) amortized despite occasional O(n) resizing"],
        ]),
    },
    "world-literature-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Comparative literature", "The study of literature across different languages/cultures"],
            ["Focus", "Themes, forms, and influences that cross borders"],
        ]),
    },
    "art-ug1-l3": {
        "data_table": table(["Drawing Technique", "Description"], [
            ["Cross-hatching", "Layered intersecting lines to build shading"],
            ["Stippling", "Using dots to create tone and texture"],
        ]),
    },
    "music-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Counterpoint", "The relationship between independent musical voices that are harmonically interdependent"],
            ["Species counterpoint", "A pedagogical method developed by Johann Joseph Fux"],
        ]),
    },
    "survival-skills-ug1-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-ug1-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-ug1-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-ug1-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-ug1-l3": {
        "data_table": table(["Sociological Perspective", "Core Idea"], [
            ["Functionalism", "Society is a system of interdependent parts working together"],
            ["Conflict theory", "Society is shaped by competition over scarce resources"],
            ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
        ]),
    },
    "physical-education-and-self-defense-ug1-l3": {
        "data_table": table(["Adaptation", "Effect of Aerobic Training"], [
            ["VO2 max", "Increases (greater oxygen uptake capacity)"],
            ["Resting heart rate", "Decreases"], ["Stroke volume", "Increases (more blood pumped per beat)"],
        ]),
    },
    "first-aid-ug1-l3": {
        "data_table": table(["Wound Healing Phase", "What Happens"], [
            ["Hemostasis", "Blood clotting stops bleeding"], ["Inflammation", "Immune cells clean the wound"],
            ["Proliferation", "New tissue forms"], ["Remodeling", "Scar tissue strengthens"],
        ]),
    },
    "physics-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Center of mass", "The average position of a system's mass, weighted by mass distribution"],
            ["Conservation of momentum", "Total momentum of a closed system stays constant"],
        ]),
    },
    "chemistry-ug1-l3": {
        "data_table": table(["Electron Groups", "Example Shape (VSEPR)"], [
            ["2", "Linear"], ["3", "Trigonal planar"], ["4", "Tetrahedral"],
        ]),
    },
    "biology-ug1-l3": {
        "data_table": table(["Innate Immune Component", "Role"], [
            ["Skin", "Physical barrier"], ["White blood cells (phagocytes)", "Engulf pathogens"],
            ["Inflammation", "Increases blood flow to fight infection"],
        ]),
    },
    "critical-thinking-ug1-l3": {
        "data_table": table(["Legal Reasoning Type", "Description"], [
            ["Precedent-based reasoning", "Applying past court decisions to new cases"],
            ["Statutory interpretation", "Determining the meaning of written law"],
        ]),
    },
    "health-education-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Epidemiology", "The study of disease patterns and causes in populations"],
            ["Incidence", "Number of new cases in a time period"],
            ["Prevalence", "Total existing cases at a given time"],
        ]),
    },
    "ict-and-computer-science-ug1-l3": {
        "data_table": table(["Normal Form", "Purpose"], [
            ["1NF", "Eliminate repeating groups; atomic values"],
            ["2NF", "Remove partial dependencies"], ["3NF", "Remove transitive dependencies"],
        ]),
    },
    "business-studies-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-ug1-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-ug1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-ug1-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-ug1-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-ug1-l1": {
        "data_table": table(["Hero / Legend", "Story"], [
            ["Rama", "Hero of the Ramayana; ideal king and warrior"],
            ["Arjuna", "Hero of the Mahabharata; receives the Bhagavad Gita's teachings"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    by_id: dict[str, dict] = {}
    for subject in data["subjects"].values():
        for lesson in subject.get("lessons", []):
            by_id[lesson["id"]] = lesson

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_ug1.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level UG1 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
