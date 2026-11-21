#!/usr/bin/env python3
"""Breadth-first pass, Level UG3 (third undergraduate-tier level): add
genuine, hand-checked data_table content to one real, verifiable lesson
per subject across all 52 non-Math subjects in level_ug3.json (Math
already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real BERT facts,
real bond types, real HTTP methods, real quantum numbers, real prevailing
wind belts, etc.) -- nothing fabricated or presented as fact when it's
actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_ug3_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_ug3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Agent", "The learner/decision-maker in reinforcement learning"],
            ["Reward signal", "Feedback indicating how good an action was"],
        ]),
    },
    "machine-learning-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["GRU", "A recurrent neural network unit with gating mechanisms to manage memory"],
            ["Gate", "A learned mechanism controlling what information to keep or discard"],
        ]),
    },
    "natural-language-processing-ug3-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["BERT stands for", "Bidirectional Encoder Representations from Transformers"],
            ["Released by", "Google, 2018"], ["Key feature", "Reads text in both directions simultaneously"],
        ]),
    },
    "data-science-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Control group", "Receives the existing/unchanged experience"],
            ["Treatment group", "Receives the new variant being tested"],
        ]),
    },
    "business-analytics-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Attrition rate", "Percentage of employees who leave in a given period"],
            ["Headcount forecasting", "Predicting future staffing needs"],
        ]),
    },
    "web-development-ug3-l3": {
        "data_table": table(["PWA Feature", "Purpose"], [
            ["Service worker", "Enables offline functionality and caching"],
            ["Web app manifest", "Defines how the app appears when installed"],
        ]),
    },
    "cybersecurity-ug3-l3": {
        "data_table": table(["Zero Trust Principle", "Meaning"], [
            ["Never trust, always verify", "No user/device is trusted by default, even inside the network"],
            ["Least privilege access", "Grant only the minimum access needed"],
        ]),
    },
    "cloud-computing-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Pay-as-you-go", "Pricing model where you pay only for resources used"],
            ["Reserved instances", "Discounted pricing for committing to usage over time"],
        ]),
    },
    "digital-marketing-ug3-l3": {
        "data_table": table(["Brand Identity Element", "Purpose"], [
            ["Logo", "Visual symbol representing the brand"],
            ["Color palette", "Consistent colors reinforcing brand recognition"],
            ["Typography", "Consistent fonts used across brand materials"],
        ]),
    },
    "ui/ux-design-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Design system", "A collection of reusable components and guidelines"],
            ["Component library", "The coded implementation of design system components"],
        ]),
    },
    "project-management-ug3-l3": {
        "data_table": table(["Power-Interest Quadrant", "Strategy"], [
            ["High power, high interest", "Manage closely"], ["High power, low interest", "Keep satisfied"],
            ["Low power, high interest", "Keep informed"], ["Low power, low interest", "Monitor"],
        ]),
    },
    "economics-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Adverse selection", "Information asymmetry before a transaction (e.g. only risky people buy insurance)"],
            ["Moral hazard", "Behavior changes after a transaction because risk is now shared"],
        ]),
    },
    "finance-ug3-l3": {
        "data_table": table(["Bond Type", "Issued By"], [
            ["Government (Treasury)", "National government"], ["Corporate", "Companies"],
            ["Municipal", "Local/state governments"],
        ]),
    },
    "philosophy-ug3-l3": {
        "data_table": table(["Position", "Core Claim"], [
            ["Internalism", "Justification depends only on factors internal to the believer's mind"],
            ["Externalism", "Justification can depend on factors external to the believer (e.g. reliability of the process)"],
        ]),
    },
    "art-history-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Literati painting", "Art by scholar-officials, valuing expression over technical skill"],
            ["Shan shui", "'Mountain-water' - the traditional Chinese landscape painting genre"],
        ]),
    },
    "python-ug3-l3": {
        "data_table": table(["NumPy Concept", "Meaning"], [
            ["ndarray", "NumPy's core N-dimensional array object"],
            ["Broadcasting", "Automatically expanding array shapes for element-wise operations"],
        ]),
    },
    "r-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["CRAN", "The Comprehensive R Archive Network - the main repository for R packages"],
            ["install.packages()", "The R function used to install a CRAN package"],
        ]),
    },
    "javascript-ug3-l3": {
        "data_table": table(["HTTP Method", "Typical Use"], [
            ["GET", "Retrieve data"], ["POST", "Create data"], ["PUT", "Update data"], ["DELETE", "Remove data"],
        ]),
    },
    "prompt-engineering-ug3-l3": {
        "data_table": table(["RAG Step", "Purpose"], [
            ["Retrieval", "Finds relevant documents/passages from a knowledge source"],
            ["Augmentation", "Adds retrieved content to the prompt"],
            ["Generation", "The model produces a response using that context"],
        ]),
    },
    "computer-science-engineering-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Finite automaton", "An abstract machine with a finite number of states"],
            ["Regular language", "A language that can be recognized by a finite automaton"],
        ]),
    },
    "big-data-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Presto/Trino", "A distributed SQL query engine for querying large datasets"],
            ["Distributed query engine", "Splits queries across many machines for parallel processing"],
        ]),
    },
    "mba-ug3-l3": {
        "data_table": table(["Strategy Type", "Focus"], [
            ["Red ocean", "Competing in existing markets"], ["Blue ocean", "Creating new, uncontested market space"],
        ]),
    },
    "operations-management-ug3-l3": {
        "data_table": table(["ARIMA Component", "Meaning"], [
            ["AR (AutoRegressive)", "Uses past values to predict future values"],
            ["I (Integrated)", "Differencing to make data stationary"],
            ["MA (Moving Average)", "Uses past forecast errors"],
        ]),
    },
    "ai-tools-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Agentic workflow", "An AI system that plans and takes multiple actions toward a goal"],
            ["Tool use", "An AI model calling external functions/APIs to get information or act"],
        ]),
    },
    "english-ug3-l3": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeal to credibility/character"], ["Pathos", "Appeal to emotion"],
            ["Logos", "Appeal to logic/reason"],
        ]),
    },
    "science-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Factorial design", "Tests multiple factors simultaneously to see their combined effects"],
            ["Interaction effect", "When the effect of one factor depends on the level of another"],
        ]),
    },
    "geography-ug3-l3": {
        "data_table": table(["Wind Belt", "Approx. Latitude"], [
            ["Trade winds", "0-30 degrees"], ["Westerlies", "30-60 degrees"], ["Polar easterlies", "60-90 degrees"],
        ]),
    },
    "world-history-ug3-l3": {
        "data_table": table(["Empire", "Traditional Fall Date"], [
            ["Western Roman Empire", "476 CE"], ["Han Dynasty China", "220 CE"],
        ]),
    },
    "islamic-studies-ug3-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Surah number", "49"], ["Meaning of name", "The Chambers"],
            ["Common themes", "Social conduct, avoiding suspicion and mockery"],
        ]),
    },
    "coding-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Space complexity", "The amount of memory an algorithm uses relative to input size"],
            ["Time-space trade-off", "Using more memory to reduce runtime, or vice versa"],
        ]),
    },
    "world-literature-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Eurocentrism", "Framing European culture/history as the norm or standard"],
            ["Critique", "Argues for including non-Western literary traditions on equal footing"],
        ]),
    },
    "art-ug3-l3": {
        "data_table": table(["Approach", "Focus"], [
            ["Observational drawing", "Depicting what is actually seen"],
            ["Abstraction", "Simplifying or distorting forms to emphasize essential qualities"],
        ]),
    },
    "music-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Fugue", "A contrapuntal piece where a theme is introduced and imitated across multiple voices"],
            ["Subject", "The main theme of a fugue"],
        ]),
    },
    "survival-skills-ug3-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-ug3-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-ug3-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-ug3-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-ug3-l3": {
        "data_table": table(["Sociological Perspective", "Core Idea"], [
            ["Functionalism", "Society is a system of interdependent parts working together"],
            ["Conflict theory", "Society is shaped by competition over scarce resources"],
            ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
        ]),
    },
    "physical-education-and-self-defense-ug3-l3": {
        "data_table": table(["Adaptation", "Effect of Aerobic Training"], [
            ["VO2 max", "Increases (greater oxygen uptake capacity)"],
            ["Resting heart rate", "Decreases"], ["Stroke volume", "Increases (more blood pumped per beat)"],
        ]),
    },
    "first-aid-ug3-l3": {
        "data_table": table(["Wound Healing Phase", "What Happens"], [
            ["Hemostasis", "Blood clotting stops bleeding"], ["Inflammation", "Immune cells clean the wound"],
            ["Proliferation", "New tissue forms"], ["Remodeling", "Scar tissue strengthens"],
        ]),
    },
    "physics-ug3-l3": {
        "formulae": ["v = u + at", "s = ut + 1/2at^2"],
        "data_table": table(["Symbol", "Meaning"], [
            ["u", "Initial velocity"], ["v", "Final velocity"], ["a", "Acceleration"],
            ["t", "Time"], ["s", "Displacement"],
        ]),
    },
    "chemistry-ug3-l3": {
        "data_table": table(["Quantum Number", "What It Describes"], [
            ["Principal (n)", "Energy level/shell"], ["Angular momentum (l)", "Orbital shape (s, p, d, f)"],
            ["Magnetic (ml)", "Orbital orientation"],
        ]),
    },
    "biology-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Recombinant DNA", "DNA formed by combining genetic material from different sources"],
            ["Restriction enzyme", "A protein that cuts DNA at specific sequences"],
        ]),
    },
    "critical-thinking-ug3-l3": {
        "data_table": table(["Bloom's Taxonomy Level", "Focus"], [
            ["Remember", "Recall facts"], ["Understand", "Explain ideas"],
            ["Analyze", "Break down and examine"], ["Evaluate", "Judge and critique"],
        ]),
    },
    "health-education-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Needs assessment", "Identifying a population's health needs before designing a program"],
            ["Program evaluation", "Assessing whether a health program achieved its goals"],
        ]),
    },
    "ict-and-computer-science-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["SDN", "Software-Defined Networking - separates network control from the physical infrastructure"],
            ["Control plane", "Makes decisions about how traffic should flow"],
        ]),
    },
    "business-studies-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-ug3-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-ug3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-ug3-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-ug3-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-ug3-l1": {
        "data_table": table(["Artistic Influence (Hindu Mythology)", "Example"], [
            ["Temple sculpture", "Depictions of deities like Vishnu, Shiva, and Durga"],
            ["Dance", "Bharatanatyam and other classical dances draw on mythological stories"],
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
        raise SystemExit(f"Lesson ids not found in level_ug3.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level UG3 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
