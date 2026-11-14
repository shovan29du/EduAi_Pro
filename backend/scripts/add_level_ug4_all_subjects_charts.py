#!/usr/bin/env python3
"""Breadth-first pass, Level UG4 (fourth/final undergraduate-tier level):
add genuine, hand-checked data_table content to one real, verifiable
lesson per subject across all 52 non-Math subjects in level_ug4.json
(Math already covered by add_math_charts_all_levels.py). This is the last
of the 17 non-Grade-5 levels in the "all subjects, solid batch per grade"
breadth-first pass -- combined with add_math_charts_all_levels.py and the
Grade 5 Math pilot, every level from Grade 1 through Masters Year 2 now
has real chart/table content in every subject.

Every fact here is real and independently verifiable (real GAN
architecture, real ISO 27001/9001 facts, Kant's Critique of Judgment, real
comparative-mythology flood myths, etc.) -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_ug4_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_ug4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Generator", "Network that creates fake samples"],
            ["Discriminator", "Network that tries to distinguish real from fake samples"],
        ]),
    },
    "machine-learning-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["State", "The current situation of the agent"], ["Action", "A choice the agent can make"],
            ["Reward", "Feedback signal indicating success"],
        ]),
    },
    "natural-language-processing-ug4-l3": {
        "data_table": table(["QA Type", "Approach"], [
            ["Extractive QA", "Selects the answer span directly from a given passage"],
            ["Abstractive QA", "Generates a new answer in the model's own words"],
        ]),
    },
    "data-science-ug4-l3": {
        "data_table": table(["Storytelling Element", "Purpose"], [
            ["Narrative arc", "Structures data findings as a story with a beginning, middle, end"],
            ["Key takeaway", "The single most important insight for the audience"],
        ]),
    },
    "business-analytics-ug4-l3": {
        "data_table": table(["Metric", "Meaning"], [
            ["Precision", "Of predicted positives, how many were correct"],
            ["Recall", "Of actual positives, how many were correctly predicted"],
        ]),
    },
    "web-development-ug4-l3": {
        "data_table": table(["Testing Term", "Meaning"], [
            ["Unit test", "Tests a single small piece of code in isolation"],
            ["Assertion", "A check that a value matches an expected result"],
        ]),
    },
    "cybersecurity-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["ISO 27001", "An international standard for information security management systems"],
            ["Managed by", "ISO (International Organization for Standardization)"],
        ]),
    },
    "cloud-computing-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-region deployment", "Running an application across multiple geographic data center regions"],
            ["Benefit", "Improved availability and lower latency for distant users"],
        ]),
    },
    "digital-marketing-ug4-l3": {
        "data_table": table(["MarTech Category", "Example Function"], [
            ["CRM", "Manages customer relationships and data"],
            ["Email platform", "Sends and tracks email campaigns"],
        ]),
    },
    "ui/ux-design-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Human Interface Guidelines (HIG)", "Apple's official design guidance for iOS/macOS apps"],
            ["Published by", "Apple"],
        ]),
    },
    "project-management-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["ISO 9001", "An international standard for quality management systems"],
            ["Focus", "Consistent quality and continuous improvement"],
        ]),
    },
    "economics-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Mechanism design", "Designing rules/incentives so self-interested agents produce a desired outcome"],
            ["Sometimes called", "'Reverse game theory'"],
        ]),
    },
    "finance-ug4-l3": {
        "data_table": table(["Contract Type", "Trait"], [
            ["Forward", "Customized, traded privately (over-the-counter)"],
            ["Futures", "Standardized, traded on an exchange"],
        ]),
    },
    "philosophy-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Immanuel Kant"], ["Key work", "Critique of Judgment (1790)"],
            ["Key idea", "The sublime evokes awe from things vast or powerful beyond comprehension"],
        ]),
    },
    "art-history-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Critic", "Clement Greenberg"],
            ["Approach", "Formalism - focuses on an artwork's visual form rather than its subject/context"],
            ["Championed", "Abstract Expressionism"],
        ]),
    },
    "python-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["GIL (Global Interpreter Lock)", "A mutex allowing only one thread to execute Python bytecode at a time"],
            ["Effect", "Limits true parallelism for CPU-bound threads in standard Python"],
        ]),
    },
    "r-ug4-l3": {
        "data_table": table(["R Package/Class", "Purpose"], [
            ["ts", "Base R class for regular time series"],
            ["xts/zoo", "Extended classes for irregular time series"],
        ]),
    },
    "javascript-ug4-l3": {
        "data_table": table(["TypeScript Feature", "Purpose"], [
            ["interface", "Defines the shape of an object"],
            ["type alias", "Creates a custom name for a type"],
        ]),
    },
    "prompt-engineering-ug4-l3": {
        "data_table": table(["Evaluation Dimension", "What It Measures"], [
            ["Accuracy", "Is the response factually correct?"],
            ["Relevance", "Does it address the actual request?"],
        ]),
    },
    "computer-science-engineering-ug4-l3": {
        "data_table": table(["OOP Principle", "Meaning"], [
            ["Encapsulation", "Bundling data and methods, restricting direct access"],
            ["Inheritance", "A class reuses/extends another class's behavior"],
            ["Polymorphism", "Different classes respond differently to the same method call"],
        ]),
    },
    "big-data-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Data parallelism", "Splitting data across machines, each training on a subset"],
            ["Model parallelism", "Splitting the model itself across machines"],
        ]),
    },
    "mba-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Network effect", "A product/service becomes more valuable as more people use it"],
            ["Platform business", "Connects two or more distinct user groups (e.g. buyers and sellers)"],
        ]),
    },
    "operations-management-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The network of organizations involved in producing and delivering a product"],
            ["Network design", "Deciding the number/location of facilities in that network"],
        ]),
    },
    "ai-tools-ug4-l3": {
        "data_table": table(["Component", "Role"], [
            ["Planner", "Decides the sequence of actions to take"],
            ["Executor", "Carries out the chosen actions/tool calls"],
            ["Memory", "Stores context across steps"],
        ]),
    },
    "english-ug4-l3": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeal to credibility/character"], ["Pathos", "Appeal to emotion"],
            ["Logos", "Appeal to logic/reason"],
        ]),
    },
    "science-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Hypothesis", "A testable, falsifiable proposed explanation"],
            ["Independent variable", "The variable you change"],
            ["Dependent variable", "The variable you measure"],
        ]),
    },
    "geography-ug4-l3": {
        "data_table": table(["Fieldwork Method", "Use"], [
            ["Transect", "A line along which measurements are taken at intervals"],
            ["Quadrat", "A square frame used to sample a small area"],
        ]),
    },
    "world-history-ug4-l3": {
        "data_table": table(["Civilization", "River"], [
            ["Mesopotamia", "Tigris and Euphrates"], ["Egypt", "Nile"], ["Indus Valley", "Indus"],
            ["Ancient China (Shang)", "Yellow River (Huang He)"],
        ]),
    },
    "islamic-studies-ug4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Surah number", "30"], ["Meaning of name", "The Romans (Byzantines)"],
            ["Notable content", "References the Byzantine-Sassanid wars"],
        ]),
    },
    "coding-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Lower bound", "A proven minimum amount of work any algorithm must do for a problem"],
            ["Comparison sort lower bound", "Omega(n log n) comparisons required"],
        ]),
    },
    "world-literature-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["World Literature", "Literature that circulates beyond its original culture/language"],
            ["Coined by", "Johann Wolfgang von Goethe (Weltliteratur, 1827)"],
        ]),
    },
    "art-ug4-l3": {
        "data_table": table(["Composition Technique", "Effect"], [
            ["Rule of thirds", "Places key elements along gridlines for balance"],
            ["Leading lines", "Guides the viewer's eye through the image"],
        ]),
    },
    "music-ug4-l3": {
        "data_table": table(["20th-Century Technique", "Description"], [
            ["Atonality", "Music without a home key/tonal center"],
            ["Serialism", "Ordering pitches (or other elements) via a fixed series"],
        ]),
    },
    "survival-skills-ug4-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-ug4-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-ug4-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-ug4-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-ug4-l3": {
        "data_table": table(["Research Method", "Description"], [
            ["Participant observation", "Researcher joins and observes a group directly"],
            ["Structured interview", "Standardized set of questions asked to all participants"],
        ]),
    },
    "physical-education-and-self-defense-ug4-l3": {
        "data_table": table(["Adaptation", "Effect of Aerobic Training"], [
            ["VO2 max", "Increases (greater oxygen uptake capacity)"],
            ["Resting heart rate", "Decreases"], ["Stroke volume", "Increases (more blood pumped per beat)"],
        ]),
    },
    "first-aid-ug4-l3": {
        "data_table": table(["Wound Healing Phase", "What Happens"], [
            ["Hemostasis", "Blood clotting stops bleeding"], ["Inflammation", "Immune cells clean the wound"],
            ["Proliferation", "New tissue forms"], ["Remodeling", "Scar tissue strengthens"],
        ]),
    },
    "physics-ug4-l3": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    "chemistry-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Kinetic isotope effect", "A change in reaction rate caused by substituting an atom with its isotope"],
            ["Common use", "Deuterium (heavy hydrogen) substitution to probe reaction mechanisms"],
        ]),
    },
    "biology-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Control group", "A group not receiving the experimental treatment, for comparison"],
            ["Replication", "Repeating an experiment to ensure reliable results"],
        ]),
    },
    "critical-thinking-ug4-l3": {
        "data_table": table(["Case Study Element", "Purpose"], [
            ["Background", "Context needed to understand the situation"],
            ["Dilemma", "The central decision or conflict to analyze"],
            ["Analysis", "Applying frameworks/theory to evaluate options"],
        ]),
    },
    "health-education-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Health policy", "Decisions/plans that determine health outcomes for a population"],
            ["Advocacy", "Actively supporting a cause to influence policy or public opinion"],
        ]),
    },
    "ict-and-computer-science-ug4-l3": {
        "data_table": table(["Integration Approach", "Description"], [
            ["Point-to-point", "Direct connections between individual systems"],
            ["Middleware/ESB", "A central layer routing messages between systems"],
        ]),
    },
    "business-studies-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-ug4-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-ug4-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-ug4-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-ug4-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-ug4-l1": {
        "data_table": table(["Comparative Theme", "Hindu Example", "Cross-Cultural Parallel"], [
            ["Great Flood myth", "Manu and the flood (Matsya Purana)", "Noah's Ark; Epic of Gilgamesh"],
            ["Sky father / Earth mother", "Dyaus and Prithvi", "Greek Uranus and Gaia"],
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
        raise SystemExit(f"Lesson ids not found in level_ug4.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level UG4 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
