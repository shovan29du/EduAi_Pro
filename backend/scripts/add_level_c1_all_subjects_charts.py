#!/usr/bin/env python3
"""Breadth-first pass, Level C1 (first college-tier level): add genuine,
hand-checked data_table content to one real, verifiable lesson per subject
across all 52 non-Math subjects in level_c1.json (Math already covered by
add_math_charts_all_levels.py). This level introduces a much larger
subject list than K-12 (AI, Machine Learning, Data Science, several
programming languages, Business Studies, World Religions, Mythology,
etc.), so coverage here is one well-verified lesson per subject rather
than a larger batch -- still real, breadth-first coverage across every
subject.

Every fact here is real and independently verifiable (Bayes' Theorem,
the CIA security triad, the "Rule of 3s" survival priority order, Robert
Hooke's 1665 discovery of cells, kinematics equations, etc.) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_c1_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-c1-l3": {
        "data_table": table(["Connective", "Symbol", "Meaning"], [
            ["AND", "AND", "Both true"], ["OR", "OR", "At least one true"],
            ["NOT", "NOT", "Negation"], ["IMPLIES", "IF...THEN", "If...then"],
        ]),
    },
    "machine-learning-c1-l3": {
        "formulae": ["P(A|B) = P(B|A) x P(A) / P(B)  (Bayes' Theorem)"],
        "data_table": table(["Term", "Meaning"], [
            ["Prior", "P(A) - belief before evidence"],
            ["Likelihood", "P(B|A) - probability of evidence given the hypothesis"],
            ["Posterior", "P(A|B) - updated belief after evidence"],
        ]),
    },
    "natural-language-processing-c1-l3": {
        "data_table": table(["Technique", "Example"], [
            ["Lowercasing", "'Hello' -> 'hello'"], ["Stemming", "'running' -> 'run'"],
            ["Lemmatization", "'better' -> 'good'"],
        ]),
    },
    "data-science-c1-l3": {
        "data_table": table(["Issue", "Technique"], [
            ["Missing values", "Imputation (mean/median) or removal"],
            ["Duplicates", "De-duplication"],
            ["Outliers", "Statistical detection (e.g. IQR method) and review"],
        ]),
    },
    "business-analytics-c1-l3": {
        "data_table": table(["Spreadsheet Function", "Purpose"], [
            ["SUM", "Adds a range of values"], ["AVERAGE", "Calculates the mean"],
            ["VLOOKUP", "Looks up a value in a table"],
        ]),
    },
    "web-development-c1-l3": {
        "data_table": table(["HTML5 Tag", "Purpose"], [
            ["<header>", "Introductory content"], ["<nav>", "Navigation links"],
            ["<main>", "Main content"], ["<footer>", "Footer content"],
        ]),
    },
    "cybersecurity-c1-l3": {
        "data_table": table(["CIA Triad", "Meaning"], [
            ["Confidentiality", "Preventing unauthorized access to data"],
            ["Integrity", "Ensuring data is accurate and unaltered"],
            ["Availability", "Ensuring systems are accessible when needed"],
        ]),
    },
    "cloud-computing-c1-l3": {
        "data_table": table(["Cloud Provider", "Parent Company"], [
            ["AWS", "Amazon"], ["Azure", "Microsoft"], ["GCP", "Google"],
        ]),
    },
    "digital-marketing-c1-l3": {
        "data_table": table(["Marketing Funnel Stage", "Goal"], [
            ["Awareness", "Introduce the brand"], ["Consideration", "Build interest"],
            ["Conversion", "Drive a purchase"], ["Loyalty", "Retain the customer"],
        ]),
    },
    "ui/ux-design-c1-l3": {
        "data_table": table(["Double Diamond Phase", "Focus"], [
            ["Discover", "Explore the problem (divergent)"],
            ["Define", "Narrow to a clear problem (convergent)"],
            ["Develop", "Explore solutions (divergent)"],
            ["Deliver", "Finalize the solution (convergent)"],
        ]),
    },
    "project-management-c1-l3": {
        "data_table": table(["Project Charter Element", "Purpose"], [
            ["Objectives", "What the project aims to achieve"],
            ["Scope", "Boundaries of the project"],
            ["Stakeholders", "Who is involved or affected"],
        ]),
    },
    "economics-c1-l2": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price tends to rise"],
            ["Low demand, high supply", "Price tends to fall"],
        ]),
    },
    "finance-c1-l3": {
        "data_table": table(["Category", "Recommended % of Income (50/30/20 rule)"], [
            ["Needs", "50%"], ["Wants", "30%"], ["Savings / Debt Repayment", "20%"],
        ]),
    },
    "philosophy-c1-l3": {
        "data_table": table(["Truth Value", "Meaning"], [
            ["True", "The proposition matches reality"], ["False", "The proposition does not match reality"],
        ]),
    },
    "art-history-c1-l3": {
        "data_table": table(["Cave Art Site", "Location", "Approx. Age"], [
            ["Lascaux", "France", "c. 17,000 years old"],
            ["Altamira", "Spain", "c. 14,000-36,000 years old"],
        ]),
    },
    "python-c1-l3": {
        "data_table": table(["Python Type", "Example"], [
            ["int", "5"], ["float", "3.14"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "r-c1-l3": {
        "data_table": table(["Tool", "Purpose"], [
            ["R", "The programming language"], ["RStudio", "An IDE (development environment) for R"],
        ]),
    },
    "javascript-c1-l3": {
        "data_table": table(["Declaration", "Reassignable?"], [
            ["var", "Yes (function-scoped)"], ["let", "Yes (block-scoped)"], ["const", "No (block-scoped)"],
        ]),
    },
    "prompt-engineering-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["LLM", "A neural network trained on large text data to predict/generate language"],
            ["Token", "A chunk of text (word or sub-word) the model processes"],
        ]),
    },
    "computer-science-engineering-c1-l3": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["5", "101"],
        ]),
    },
    "big-data-c1-l3": {
        "data_table": table(["V (Big Data)", "Meaning"], [
            ["Volume", "Amount of data"], ["Velocity", "Speed of data generation"],
            ["Variety", "Different types of data"], ["Veracity", "Data quality/trustworthiness"],
            ["Value", "Usefulness of the data"],
        ]),
    },
    "mba-c1-l3": {
        "data_table": table(["Strategic Framework", "Purpose"], [
            ["SWOT", "Strengths, Weaknesses, Opportunities, Threats analysis"],
            ["Porter's Five Forces", "Analyzes industry competitive forces"],
        ]),
    },
    "operations-management-c1-l3": {
        "data_table": table(["KPI", "Measures"], [
            ["Throughput", "Units produced per time period"],
            ["Cycle time", "Time to complete one unit of work"],
            ["Defect rate", "Percentage of defective output"],
        ]),
    },
    "ai-tools-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["LLM", "A model trained on large text data to understand/generate language"],
            ["Prompt", "The input text given to an AI model"],
        ]),
    },
    "english-c1-l3": {
        "data_table": table(["Rhetorical Element", "Meaning"], [
            ["Author", "Who is communicating"], ["Audience", "Who receives the message"],
            ["Purpose", "Why the message is communicated"],
            ["Context", "The circumstances surrounding communication"],
        ]),
    },
    "science-c1-l3": {
        "data_table": table(["Scientific Method Step", "Description"], [
            ["1. Observation", "Notice a phenomenon"], ["2. Question", "Ask what/why/how"],
            ["3. Hypothesis", "Propose a testable explanation"], ["4. Experiment", "Test the hypothesis"],
            ["5. Conclusion", "Analyze results"],
        ]),
    },
    "geography-c1-l3": {
        "data_table": table(["Landform", "Description"], [
            ["Mountain", "Elevated landform with steep sides"],
            ["Plateau", "Flat, elevated land"], ["Plain", "Flat, low-lying land"],
        ]),
    },
    "world-history-c1-l3": {
        "data_table": table(["Civilization", "River"], [
            ["Mesopotamia", "Tigris and Euphrates"], ["Egypt", "Nile"],
        ]),
    },
    "islamic-studies-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Tafsir", "Interpretation and explanation of the Quran"],
            ["Mufassir", "A scholar who performs Tafsir"],
        ]),
    },
    "coding-c1-l3": {
        "data_table": table(["Big O Notation", "Meaning"], [
            ["O(1)", "Constant time"], ["O(n)", "Linear time"],
            ["O(log n)", "Logarithmic time"], ["O(n^2)", "Quadratic time"],
        ]),
    },
    "world-literature-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["World Literature", "Literature that circulates beyond its original culture/language"],
            ["Coined by", "Johann Wolfgang von Goethe (Weltliteratur, 1827)"],
        ]),
    },
    "art-c1-l3": {
        "data_table": table(["Element of Drawing", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D enclosed area"],
            ["Value", "The lightness or darkness of a tone"],
        ]),
    },
    "music-c1-l3": {
        "data_table": table(["Triad Type", "Structure (from root)"], [
            ["Major", "Root, Major 3rd, Perfect 5th"], ["Minor", "Root, Minor 3rd, Perfect 5th"],
        ]),
    },
    "survival-skills-c1-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-c1-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-c1-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-c1-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-c1-l3": {
        "data_table": table(["Sociologist", "Contribution"], [
            ["Auguste Comte", "Coined the term 'sociology'"],
            ["Emile Durkheim", "Pioneered the study of social facts"],
            ["Max Weber", "Studied social action and bureaucracy"],
        ]),
    },
    "physical-education-and-self-defense-c1-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Average resting heart rate (adult)", "60-100 beats per minute"],
            ["Max heart rate estimate", "220 minus your age (a common formula)"],
        ]),
    },
    "first-aid-c1-l3": {
        "data_table": table(["Wound Care Step", "Action"], [
            ["1", "Clean hands and wear gloves if available"],
            ["2", "Stop the bleeding with direct pressure"],
            ["3", "Clean the wound with water"],
            ["4", "Cover with a sterile dressing"],
        ]),
    },
    "physics-c1-l3": {
        "formulae": ["v = u + at", "s = ut + 1/2at^2"],
        "data_table": table(["Symbol", "Meaning"], [
            ["u", "Initial velocity"], ["v", "Final velocity"], ["a", "Acceleration"],
            ["t", "Time"], ["s", "Displacement"],
        ]),
    },
    "chemistry-c1-l3": {
        "data_table": table(["Particle", "Charge", "Location"], [
            ["Proton", "Positive", "Nucleus"], ["Neutron", "Neutral", "Nucleus"],
            ["Electron", "Negative", "Orbiting the nucleus"],
        ]),
    },
    "biology-c1-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Cell theory tenet", "All living things are made of cells"],
            ["First observed cells", "Robert Hooke, 1665 (cork cells)"],
        ]),
    },
    "critical-thinking-c1-l3": {
        "data_table": table(["Standard of Thinking", "Question It Asks"], [
            ["Clarity", "Could you elaborate?"], ["Accuracy", "Is that really true?"],
            ["Relevance", "How does that relate?"],
        ]),
    },
    "health-education-c1-l3": {
        "data_table": table(["Body System", "Main Function"], [
            ["Circulatory", "Pumps blood through the body"],
            ["Respiratory", "Brings oxygen in, removes carbon dioxide"],
            ["Digestive", "Breaks down food for energy"],
            ["Skeletal", "Supports and protects the body"],
        ]),
    },
    "ict-and-computer-science-c1-l3": {
        "data_table": table(["Information System Component", "Role"], [
            ["Hardware", "Physical devices"], ["Software", "Programs and applications"],
            ["Data", "Information processed"], ["People", "Users and IT staff"],
            ["Processes", "Procedures for using the system"],
        ]),
    },
    "business-studies-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-c1-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-c1-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-c1-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-c1-l1": {
        "data_table": table(["Hindu Deity", "Domain"], [
            ["Brahma", "Creation"], ["Vishnu", "Preservation"], ["Shiva", "Destruction / transformation"],
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
        raise SystemExit(f"Lesson ids not found in level_c1.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level C1 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
