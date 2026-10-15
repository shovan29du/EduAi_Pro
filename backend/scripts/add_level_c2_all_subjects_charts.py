#!/usr/bin/env python3
"""Breadth-first pass, Level C2 (second college-tier level): add genuine,
hand-checked data_table content to one real, verifiable lesson per subject
across all 52 non-Math subjects in level_c2.json (Math already covered by
add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (Porter's Five
Forces, the SMART goal mnemonic, real database normal forms, real DNA
replication enzymes, real truth tables, etc.) -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_c2_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-c2-l3": {
        "data_table": table(["Algorithm", "Purpose"], [
            ["Minimax", "Chooses the move that minimizes the opponent's best possible outcome"],
            ["Alpha-Beta Pruning", "Skips branches that won't affect the final decision, speeding up minimax"],
        ]),
    },
    "machine-learning-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Hyperplane", "The decision boundary separating classes"],
            ["Support vectors", "The data points closest to the hyperplane"],
            ["Margin", "The distance between the hyperplane and the nearest points"],
        ]),
    },
    "natural-language-processing-c2-l3": {
        "data_table": table(["N-gram", "Example (from 'the cat sat')"], [
            ["Unigram (n=1)", "'the', 'cat', 'sat'"], ["Bigram (n=2)", "'the cat', 'cat sat'"],
            ["Trigram (n=3)", "'the cat sat'"],
        ]),
    },
    "data-science-c2-l3": {
        "data_table": table(["Correlation Coefficient (r)", "Interpretation"], [
            ["+1", "Perfect positive correlation"], ["0", "No linear correlation"],
            ["-1", "Perfect negative correlation"],
        ]),
    },
    "business-analytics-c2-l3": {
        "formulae": ["y = b0 + b1x1 + b2x2 + ... + bnxn"],
        "data_table": table(["Term", "Meaning"], [
            ["Dependent variable (y)", "The outcome being predicted"],
            ["Independent variables (x)", "The predictors"],
        ]),
    },
    "web-development-c2-l3": {
        "data_table": table(["Declaration", "Reassignable?"], [
            ["var", "Yes (function-scoped)"], ["let", "Yes (block-scoped)"], ["const", "No (block-scoped)"],
        ]),
    },
    "cybersecurity-c2-l3": {
        "data_table": table(["System", "Function"], [
            ["IDS (Intrusion Detection System)", "Monitors and alerts on suspicious activity"],
            ["IPS (Intrusion Prevention System)", "Monitors and actively blocks suspicious activity"],
        ]),
    },
    "cloud-computing-c2-l3": {
        "data_table": table(["Docker Term", "Meaning"], [
            ["Image", "A read-only template used to create containers"],
            ["Container", "A running instance of an image"],
            ["Dockerfile", "A script defining how to build an image"],
        ]),
    },
    "digital-marketing-c2-l3": {
        "data_table": table(["Content Calendar Element", "Purpose"], [
            ["Publish date", "When content goes live"],
            ["Channel", "Where content is published (blog, social, email)"],
            ["Topic/theme", "The subject of the content"],
        ]),
    },
    "ui/ux-design-c2-l3": {
        "data_table": table(["Card Sort Type", "Description"], [
            ["Open card sort", "Participants create and label their own categories"],
            ["Closed card sort", "Participants sort cards into predefined categories"],
        ]),
    },
    "project-management-c2-l3": {
        "data_table": table(["Requirements Gathering Technique", "Description"], [
            ["Interviews", "One-on-one discussions with stakeholders"],
            ["Surveys", "Written questions to a group of stakeholders"],
            ["Workshops", "Facilitated group sessions"],
        ]),
    },
    "economics-c2-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Budget constraint", "The combinations of goods a consumer can afford"],
            ["Indifference curve", "Combinations of goods giving equal satisfaction"],
        ]),
    },
    "finance-c2-l3": {
        "formulae": ["FV = PV(1+r)^n", "PV = FV/(1+r)^n"],
        "data_table": table(["Variable", "Meaning"], [
            ["PV", "Present Value"], ["FV", "Future Value"], ["r", "Interest rate"], ["n", "Number of periods"],
        ]),
    },
    "philosophy-c2-l3": {
        "data_table": table(["p", "q", "p AND q"], [
            ["T", "T", "T"], ["T", "F", "F"], ["F", "T", "F"], ["F", "F", "F"],
        ]),
    },
    "art-history-c2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Roman catacombs (underground burial chambers)"],
            ["Approx. period", "3rd-4th century CE"],
            ["Common subject", "Symbols like the fish (ichthys) and Good Shepherd"],
        ]),
    },
    "python-c2-l3": {
        "data_table": table(["List Comprehension", "Result"], [
            ["[x for x in range(5)]", "[0, 1, 2, 3, 4]"], ["[x*2 for x in range(3)]", "[0, 2, 4]"],
        ]),
    },
    "r-c2-l3": {
        "data_table": table(["Tidy Data Rule", "Meaning"], [
            ["Each variable", "Forms a column"], ["Each observation", "Forms a row"],
            ["Each value", "Has its own cell"],
        ]),
    },
    "javascript-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Closure", "A function that remembers variables from its outer scope even after that scope has closed"],
        ]),
    },
    "prompt-engineering-c2-l3": {
        "data_table": table(["Prompting Approach", "Description"], [
            ["Zero-shot", "No examples given, just an instruction"],
            ["Few-shot", "A small number of examples given before the task"],
        ]),
    },
    "computer-science-engineering-c2-l3": {
        "data_table": table(["Structure", "Order"], [
            ["Stack", "LIFO (Last In, First Out)"], ["Queue", "FIFO (First In, First Out)"],
        ]),
    },
    "big-data-c2-l3": {
        "data_table": table(["HDFS Component", "Role"], [
            ["NameNode", "Manages filesystem metadata (the 'master')"],
            ["DataNode", "Stores the actual data blocks (the 'workers')"],
        ]),
    },
    "mba-c2-l3": {
        "data_table": table(["Porter's Five Forces", "Description"], [
            ["Competitive rivalry", "Intensity of competition among existing firms"],
            ["Threat of new entrants", "How easily new competitors can enter"],
            ["Bargaining power of suppliers", "Suppliers' ability to raise prices"],
            ["Bargaining power of buyers", "Buyers' ability to demand lower prices"],
            ["Threat of substitutes", "Availability of alternative products"],
        ]),
    },
    "operations-management-c2-l3": {
        "data_table": table(["Process Map Symbol", "Meaning"], [
            ["Rectangle", "A process step"], ["Diamond", "A decision point"], ["Arrow", "Flow direction"],
        ]),
    },
    "ai-tools-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["LLM", "A model trained on large text data to understand/generate language"],
            ["Prompt", "The input text given to an AI model"],
        ]),
    },
    "english-c2-l3": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeal to credibility/character"], ["Pathos", "Appeal to emotion"],
            ["Logos", "Appeal to logic/reason"],
        ]),
    },
    "science-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Hypothesis", "A testable, falsifiable proposed explanation"],
            ["Independent variable", "The variable you change"],
            ["Dependent variable", "The variable you measure"],
        ]),
    },
    "geography-c2-l3": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot year-round, high rainfall"],
            ["Temperate", "Moderate temperatures, four seasons"],
            ["Polar", "Very cold year-round"],
        ]),
    },
    "world-history-c2-l3": {
        "data_table": table(["Civilization", "River"], [
            ["Mesopotamia", "Tigris and Euphrates"], ["Egypt", "Nile"], ["Indus Valley", "Indus"],
            ["Ancient China (Shang)", "Yellow River (Huang He)"],
        ]),
    },
    "islamic-studies-c2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Surah number", "18"], ["Meaning of name", "The Cave"], ["Traditionally recited on", "Fridays"],
        ]),
    },
    "coding-c2-l3": {
        "data_table": table(["Case", "Meaning"], [
            ["Best case", "Minimum time/steps needed"], ["Worst case", "Maximum time/steps needed"],
            ["Average case", "Expected time/steps over typical input"],
        ]),
    },
    "world-literature-c2-l3": {
        "data_table": table(["Comparative Approach", "Focus"], [
            ["Thematic comparison", "Shared themes across texts"],
            ["Formal comparison", "Shared structures/techniques across texts"],
        ]),
    },
    "art-c2-l3": {
        "data_table": table(["Principle of Composition", "Meaning"], [
            ["Balance", "Even visual weight distribution"],
            ["Contrast", "Difference between elements to create interest"],
            ["Emphasis", "A focal point that draws the eye"],
        ]),
    },
    "music-c2-l3": {
        "data_table": table(["Roman Numeral", "Chord Function"], [
            ["I", "Tonic"], ["IV", "Subdominant"], ["V", "Dominant"],
        ]),
    },
    "survival-skills-c2-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-c2-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-c2-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-c2-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-c2-l3": {
        "data_table": table(["Sociological Perspective", "Core Idea"], [
            ["Functionalism", "Society is a system of interdependent parts working together"],
            ["Conflict theory", "Society is shaped by competition over scarce resources"],
            ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
        ]),
    },
    "physical-education-and-self-defense-c2-l3": {
        "data_table": table(["Energy System", "Duration Used"], [
            ["ATP-PCr (Phosphagen)", "0-10 seconds, high intensity"],
            ["Anaerobic glycolysis", "10 seconds-2 minutes"],
            ["Aerobic system", "2+ minutes, endurance"],
        ]),
    },
    "first-aid-c2-l3": {
        "data_table": table(["Wound Care Step", "Action"], [
            ["1", "Clean hands and wear gloves if available"],
            ["2", "Stop the bleeding with direct pressure"],
            ["3", "Clean the wound with water"],
            ["4", "Cover with a sterile dressing"],
        ]),
    },
    "physics-c2-l3": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    "chemistry-c2-l3": {
        "data_table": table(["Orbital Type", "Effect"], [
            ["Bonding orbital", "Lower energy, stabilizes the molecule"],
            ["Antibonding orbital", "Higher energy, destabilizes the molecule"],
        ]),
    },
    "biology-c2-l3": {
        "data_table": table(["Enzyme", "Role in DNA Replication"], [
            ["DNA polymerase", "Adds new nucleotides to the growing strand"],
            ["Helicase", "Unwinds the DNA double helix"],
            ["Ligase", "Joins DNA fragments together"],
        ]),
    },
    "critical-thinking-c2-l3": {
        "data_table": table(["Syllogism Part", "Example"], [
            ["Major premise", "All mammals are warm-blooded"],
            ["Minor premise", "A dog is a mammal"],
            ["Conclusion", "Therefore, a dog is warm-blooded"],
        ]),
    },
    "health-education-c2-l3": {
        "data_table": table(["SMART Goal Letter", "Meaning"], [
            ["S", "Specific"], ["M", "Measurable"], ["A", "Achievable"], ["R", "Relevant"], ["T", "Time-bound"],
        ]),
    },
    "ict-and-computer-science-c2-l3": {
        "data_table": table(["Normal Form", "Purpose"], [
            ["1NF", "Eliminate repeating groups; atomic values"],
            ["2NF", "Remove partial dependencies"],
            ["3NF", "Remove transitive dependencies"],
        ]),
    },
    "business-studies-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-c2-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-c2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-c2-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-c2-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-c2-l1": {
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
        raise SystemExit(f"Lesson ids not found in level_c2.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level C2 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
