#!/usr/bin/env python3
"""Breadth-first pass, Level M1 (first graduate-tier level): add genuine,
hand-checked data_table content to one real, verifiable lesson per subject
across all 52 non-Math subjects in level_m1.json (Math already covered by
add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (Popper vs. Kuhn on
the philosophy of science, real P/NP complexity classes, real epigenetics
terminology, real Jest testing functions, etc.) -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_m1_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["AI Alignment", "Ensuring AI systems act according to human intentions and values"],
            ["Reward hacking", "When an AI optimizes for a proxy reward in an unintended way"],
        ]),
    },
    "machine-learning-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Hyperparameter", "A setting configured before training (e.g. learning rate)"],
            ["Bayesian optimization", "Uses a probabilistic model to efficiently search hyperparameter space"],
        ]),
    },
    "natural-language-processing-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["ASR (Automatic Speech Recognition)", "Converting spoken audio into text"],
            ["Phoneme", "The smallest unit of sound in speech"],
        ]),
    },
    "data-science-m1-l3": {
        "data_table": table(["MLOps Stage", "Purpose"], [
            ["Model training", "Building the model from data"],
            ["Model deployment", "Putting the model into production"],
            ["Model monitoring", "Tracking performance over time"],
        ]),
    },
    "business-analytics-m1-l3": {
        "formulae": ["P(A|B) = P(B|A) x P(A) / P(B)"],
        "data_table": table(["Term", "Meaning"], [
            ["Prior", "Belief before new data"], ["Posterior", "Updated belief after new data"],
        ]),
    },
    "web-development-m1-l3": {
        "data_table": table(["React Hook/Tool", "Purpose"], [
            ["useMemo", "Memoizes a computed value"], ["useCallback", "Memoizes a function reference"],
            ["React.memo", "Prevents re-render if props are unchanged"],
        ]),
    },
    "cybersecurity-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Zero-knowledge proof", "Proving a statement is true without revealing the underlying information"],
            ["Prover", "The party proving a claim"], ["Verifier", "The party checking the proof"],
        ]),
    },
    "cloud-computing-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Edge computing", "Processing data near its source rather than in a centralized cloud"],
            ["Latency benefit", "Reduced delay by avoiding round trips to distant servers"],
        ]),
    },
    "digital-marketing-m1-l3": {
        "data_table": table(["Platform", "Common Video Aspect Ratio"], [
            ["Instagram Stories/Reels", "9:16 (vertical)"], ["YouTube", "16:9 (horizontal)"],
            ["Instagram Feed", "1:1 (square) or 4:5"],
        ]),
    },
    "ui/ux-design-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Voice", "A brand's consistent personality in writing"],
            ["Tone", "How that voice adapts to context (e.g. error vs. success message)"],
        ]),
    },
    "project-management-m1-l3": {
        "data_table": table(["Prioritization Framework", "Basis for Prioritization"], [
            ["MoSCoW", "Must have, Should have, Could have, Won't have"],
            ["Weighted scoring", "Numeric scores across weighted criteria"],
        ]),
    },
    "economics-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["General equilibrium", "A state where supply equals demand in all markets simultaneously"],
            ["Partial equilibrium", "Analyzing one market in isolation"],
        ]),
    },
    "finance-m1-l3": {
        "formulae": ["DCF = sum of [CFt / (1+r)^t]"],
        "data_table": table(["Term", "Meaning"], [
            ["CF", "Cash flow in a given period"], ["r", "Discount rate"], ["t", "Time period"],
        ]),
    },
    "philosophy-m1-l3": {
        "data_table": table(["Modal Operator", "Meaning"], [
            ["Necessarily (Box)", "True in all possible worlds"],
            ["Possibly (Diamond)", "True in at least one possible world"],
        ]),
    },
    "art-history-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Connoisseurship", "Expert judgment of an artwork's authenticity/quality from close visual study"],
            ["Provenance", "An artwork's documented history of ownership"],
        ]),
    },
    "python-m1-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Class", "A blueprint for creating objects"],
            ["Metaclass", "A 'class of a class' - defines how classes themselves behave (default: type)"],
        ]),
    },
    "r-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Environment", "A structure holding variable bindings in R"],
            ["Closure", "A function paired with the environment it was created in"],
        ]),
    },
    "javascript-m1-l3": {
        "data_table": table(["Jest Function", "Purpose"], [
            ["test()", "Defines a single test case"], ["expect()", "Makes an assertion"],
            ["describe()", "Groups related tests"],
        ]),
    },
    "prompt-engineering-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Agentic workflow", "An AI system that plans and takes multiple actions toward a goal"],
            ["Tool use", "An AI model calling external functions/APIs to get information or act"],
        ]),
    },
    "computer-science-engineering-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Symmetric encryption", "Same key used to encrypt and decrypt"],
            ["Asymmetric encryption", "Different keys (public/private) for encrypt and decrypt"],
        ]),
    },
    "big-data-m1-l3": {
        "data_table": table(["Security Layer", "Purpose"], [
            ["Data encryption", "Protects data at rest and in transit"],
            ["Access control", "Restricts who can view/modify data"],
        ]),
    },
    "mba-m1-l3": {
        "data_table": table(["Porter's Five Forces", "Description"], [
            ["Competitive rivalry", "Intensity of competition among existing firms"],
            ["Threat of new entrants", "How easily new competitors can enter"],
            ["Bargaining power of suppliers", "Suppliers' ability to raise prices"],
            ["Bargaining power of buyers", "Buyers' ability to demand lower prices"],
            ["Threat of substitutes", "Availability of alternative products"],
        ]),
    },
    "operations-management-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Node", "A point in a network (e.g. a location)"],
            ["Edge", "A connection between two nodes"],
            ["Shortest path problem", "Finding the minimum-cost route between two nodes"],
        ]),
    },
    "ai-tools-m1-l3": {
        "data_table": table(["Component", "Role"], [
            ["Planner", "Decides the sequence of actions to take"],
            ["Executor", "Carries out the chosen actions/tool calls"],
            ["Memory", "Stores context across steps"],
        ]),
    },
    "english-m1-l3": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeal to credibility/character"], ["Pathos", "Appeal to emotion"],
            ["Logos", "Appeal to logic/reason"],
        ]),
    },
    "science-m1-l3": {
        "data_table": table(["Philosopher", "Key Idea about Science"], [
            ["Karl Popper", "Science advances by falsification, not verification"],
            ["Thomas Kuhn", "Science progresses through 'paradigm shifts'"],
        ]),
    },
    "geography-m1-l3": {
        "data_table": table(["Earth System", "Examples"], [
            ["Atmosphere", "Air, weather, climate"], ["Hydrosphere", "Oceans, rivers, ice"],
            ["Lithosphere", "Crust, rocks, tectonic plates"], ["Biosphere", "All living organisms"],
        ]),
    },
    "world-history-m1-l3": {
        "data_table": table(["Civilization", "River"], [
            ["Mesopotamia", "Tigris and Euphrates"], ["Egypt", "Nile"], ["Indus Valley", "Indus"],
            ["Ancient China (Shang)", "Yellow River (Huang He)"],
        ]),
    },
    "islamic-studies-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Tafsir", "Interpretation and explanation of the Quran"],
            ["Asbab al-nuzul", "The historical context/occasions of revelation for specific verses"],
        ]),
    },
    "coding-m1-l3": {
        "data_table": table(["Complexity Class", "Meaning"], [
            ["P", "Problems solvable in polynomial time"],
            ["NP", "Problems whose solutions can be verified in polynomial time"],
            ["NP-complete", "The hardest problems in NP"],
        ]),
    },
    "world-literature-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["World Literature", "Literature that circulates beyond its original culture/language"],
            ["Coined by", "Johann Wolfgang von Goethe (Weltliteratur, 1827)"],
        ]),
    },
    "art-m1-l3": {
        "data_table": table(["Element of Drawing", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D enclosed area"],
            ["Value", "The lightness or darkness of a tone"],
        ]),
    },
    "music-m1-l3": {
        "data_table": table(["Roman Numeral", "Chord Function"], [
            ["I", "Tonic"], ["IV", "Subdominant"], ["V", "Dominant"],
        ]),
    },
    "survival-skills-m1-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-m1-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-m1-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-m1-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-m1-l3": {
        "data_table": table(["Sociological Perspective", "Core Idea"], [
            ["Functionalism", "Society is a system of interdependent parts working together"],
            ["Conflict theory", "Society is shaped by competition over scarce resources"],
            ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
        ]),
    },
    "physical-education-and-self-defense-m1-l3": {
        "data_table": table(["Energy System", "Duration Used"], [
            ["ATP-PCr (Phosphagen)", "0-10 seconds, high intensity"],
            ["Anaerobic glycolysis", "10 seconds-2 minutes"], ["Aerobic system", "2+ minutes, endurance"],
        ]),
    },
    "first-aid-m1-l3": {
        "data_table": table(["Wound Care Step", "Action"], [
            ["1", "Clean hands and wear gloves if available"],
            ["2", "Stop the bleeding with direct pressure"],
            ["3", "Clean the wound with water"], ["4", "Cover with a sterile dressing"],
        ]),
    },
    "physics-m1-l3": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    "chemistry-m1-l3": {
        "data_table": table(["Orbital Type", "Effect"], [
            ["Bonding orbital", "Lower energy, stabilizes the molecule"],
            ["Antibonding orbital", "Higher energy, destabilizes the molecule"],
        ]),
    },
    "biology-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Chromatin", "The complex of DNA and proteins (histones) that packages DNA"],
            ["Epigenetics", "Heritable changes in gene expression that don't alter the DNA sequence"],
        ]),
    },
    "critical-thinking-m1-l3": {
        "data_table": table(["Modal Operator", "Meaning"], [
            ["Necessarily (Box)", "True in all possible worlds"],
            ["Possibly (Diamond)", "True in at least one possible world"],
        ]),
    },
    "health-education-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Incidence", "Number of new cases in a population over a time period"],
            ["Prevalence", "Total number of existing cases at a given time"],
        ]),
    },
    "ict-and-computer-science-m1-l3": {
        "data_table": table(["Information System Component", "Role"], [
            ["Hardware", "Physical devices"], ["Software", "Programs and applications"],
            ["Data", "Information processed"], ["People", "Users and IT staff"],
            ["Processes", "Procedures for using the system"],
        ]),
    },
    "business-studies-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-m1-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-m1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-m1-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-m1-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-m1-l1": {
        "data_table": table(["Concept", "Meaning"], [
            ["Trimurti", "The three-fold Hindu concept of Brahma (creator), Vishnu (preserver), Shiva (destroyer)"],
            ["Yuga", "A cosmic age/era in Hindu cosmology"],
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
        raise SystemExit(f"Lesson ids not found in level_m1.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level M1 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
