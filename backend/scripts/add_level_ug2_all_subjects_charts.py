#!/usr/bin/env python3
"""Breadth-first pass, Level UG2 (second undergraduate-tier level): add
genuine, hand-checked data_table content to one real, verifiable lesson
per subject across all 52 non-Math subjects in level_ug2.json (Math
already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (Hobbes's Leviathan,
real WACC formula components, real Scrum roles, real logistic growth
concepts, etc.) -- nothing fabricated or presented as fact when it's
actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_ug2_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_ug2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["MDP", "A framework for modeling decision-making with states, actions, and rewards"],
            ["Policy", "A strategy defining which action to take in each state"],
        ]),
    },
    "machine-learning-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["DBSCAN", "Groups closely-packed points, marking sparse points as outliers/noise"],
            ["Core point", "A point with enough neighbors within a given radius"],
        ]),
    },
    "natural-language-processing-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Seq2Seq", "A model architecture mapping an input sequence to an output sequence"],
            ["Encoder", "Compresses the input sequence into a representation"],
            ["Decoder", "Generates the output sequence from that representation"],
        ]),
    },
    "data-science-ug2-l3": {
        "data_table": table(["Technique", "Purpose"], [
            ["Normalization", "Rescales values to a fixed range (e.g. 0-1)"],
            ["Standardization", "Rescales to have mean 0 and standard deviation 1"],
        ]),
    },
    "business-analytics-ug2-l3": {
        "data_table": table(["LP Component", "Meaning"], [
            ["Objective function", "The quantity to maximize or minimize"],
            ["Constraints", "Limits on the decision variables"],
            ["Decision variables", "The quantities being solved for"],
        ]),
    },
    "web-development-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["XSS", "Injecting malicious scripts into web pages viewed by other users"],
            ["Output encoding", "Escaping user input before rendering, a key XSS defense"],
        ]),
    },
    "cybersecurity-ug2-l3": {
        "data_table": table(["Analysis Type", "Approach"], [
            ["Static analysis", "Examining code/files without executing them"],
            ["Dynamic analysis", "Observing behavior by running the malware in a sandbox"],
        ]),
    },
    "cloud-computing-ug2-l3": {
        "data_table": table(["IAM Term", "Meaning"], [
            ["Principle of least privilege", "Grant only the access necessary to perform a task"],
            ["Role", "A set of permissions assigned to users or services"],
        ]),
    },
    "digital-marketing-ug2-l3": {
        "data_table": table(["Web Analytics Metric", "Meaning"], [
            ["Sessions", "A period of user activity on a site"],
            ["Bounce rate", "Percentage of visits with no meaningful engagement"],
            ["Conversion rate", "Percentage of visits resulting in a desired action"],
        ]),
    },
    "ui/ux-design-ug2-l3": {
        "data_table": table(["Interaction Pattern", "Use"], [
            ["Modal", "Focuses attention on a single task/decision"],
            ["Breadcrumb", "Shows the user's location within a site hierarchy"],
        ]),
    },
    "project-management-ug2-l3": {
        "data_table": table(["Scrum Role", "Responsibility"], [
            ["Product Owner", "Owns the product backlog and priorities"],
            ["Scrum Master", "Facilitates the process and removes obstacles"],
            ["Development Team", "Builds the product increment"],
        ]),
    },
    "economics-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Labor supply", "The quantity of labor workers are willing to offer at a given wage"],
            ["Labor demand", "The quantity of labor employers want to hire at a given wage"],
        ]),
    },
    "finance-ug2-l3": {
        "formulae": ["WACC = (E/V) x Re + (D/V) x Rd x (1-T)"],
        "data_table": table(["Symbol", "Meaning"], [
            ["E", "Market value of equity"], ["D", "Market value of debt"],
            ["Re", "Cost of equity"], ["Rd", "Cost of debt"],
        ]),
    },
    "philosophy-ug2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Thomas Hobbes"], ["Key work", "Leviathan (1651)"],
            ["Key idea", "Without government, life is a 'state of nature' - 'nasty, brutish, and short'"],
        ]),
    },
    "art-history-ug2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Famous painting", "The Starry Night (1889)"], ["Art movement", "Post-Impressionism"],
            ["Nationality", "Dutch"],
        ]),
    },
    "python-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Decorator", "A function that wraps another function to modify/extend its behavior"],
            ["Syntax", "@decorator_name placed above a function definition"],
        ]),
    },
    "r-ug2-l3": {
        "data_table": table(["R Markdown Component", "Purpose"], [
            ["YAML header", "Metadata (title, author, output format) at the top"],
            ["Code chunk", "A block of executable R code"],
        ]),
    },
    "javascript-ug2-l3": {
        "data_table": table(["Block", "Runs When"], [
            ["try", "Code that might throw an error"], ["catch", "An error was thrown"],
            ["finally", "Always, regardless of errors"],
        ]),
    },
    "prompt-engineering-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["System prompt", "Instructions setting the AI's role/behavior before the conversation starts"],
            ["User prompt", "The actual request/question from the user"],
        ]),
    },
    "computer-science-engineering-ug2-l3": {
        "data_table": table(["Normal Form", "Purpose"], [
            ["1NF", "Eliminate repeating groups; atomic values"],
            ["2NF", "Remove partial dependencies"], ["3NF", "Remove transitive dependencies"],
        ]),
    },
    "big-data-ug2-l3": {
        "data_table": table(["Kafka Term", "Meaning"], [
            ["Topic", "A category/feed to which records are published"],
            ["Producer", "Publishes messages to a topic"], ["Consumer", "Reads messages from a topic"],
        ]),
    },
    "mba-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["BATNA", "Best Alternative To a Negotiated Agreement"],
            ["ZOPA", "Zone Of Possible Agreement - the range both sides could accept"],
        ]),
    },
    "operations-management-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Capacity", "The maximum output a system can produce in a given period"],
            ["Bottleneck", "The step that limits the overall throughput of a process"],
        ]),
    },
    "ai-tools-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt chaining", "Using the output of one prompt as input to the next"],
        ]),
    },
    "english-ug2-l3": {
        "data_table": table(["Toulmin Element", "Meaning"], [
            ["Claim", "The conclusion being argued for"], ["Grounds", "The evidence supporting the claim"],
            ["Warrant", "The reasoning linking grounds to claim"],
        ]),
    },
    "science-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Control variable", "A factor kept constant to isolate the effect being tested"],
            ["Confounding variable", "An unaccounted-for factor that affects the results"],
        ]),
    },
    "geography-ug2-l3": {
        "data_table": table(["Fieldwork Method", "Use"], [
            ["Transect", "A line along which measurements are taken at intervals"],
            ["Quadrat", "A square frame used to sample a small area"],
        ]),
    },
    "world-history-ug2-l3": {
        "data_table": table(["Source Type", "Example"], [
            ["Primary source", "Original artifacts, inscriptions, contemporary accounts"],
            ["Secondary source", "Later historians' analysis and interpretation"],
        ]),
    },
    "islamic-studies-ug2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Surah number", "17"], ["Meaning of name", "The Night Journey"],
            ["Related event", "Isra and Mi'raj - the Prophet's night journey and ascension"],
        ]),
    },
    "coding-ug2-l3": {
        "data_table": table(["Complexity Class", "Meaning"], [
            ["P", "Problems solvable in polynomial time"],
            ["NP", "Problems whose solutions can be verified in polynomial time"],
            ["NP-complete", "The hardest problems in NP"],
        ]),
    },
    "world-literature-ug2-l3": {
        "data_table": table(["Framework", "Focus"], [
            ["Postcolonial theory", "Effects of colonization on literature and identity"],
            ["Reader-response theory", "How readers construct meaning from a text"],
        ]),
    },
    "art-ug2-l3": {
        "data_table": table(["Composition Technique", "Effect"], [
            ["Rule of thirds", "Places key elements along gridlines for balance"],
            ["Leading lines", "Guides the viewer's eye through the image"],
        ]),
    },
    "music-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Chromatic harmony", "Harmony that uses notes outside the standard diatonic scale"],
            ["Chromaticism", "The use of notes not belonging to the prevailing key"],
        ]),
    },
    "survival-skills-ug2-l3": {
        "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
            ["Air", "3 minutes"], ["Shelter (extreme conditions)", "3 hours"],
            ["Water", "3 days"], ["Food", "3 weeks"],
        ]),
    },
    "cooking-ug2-l3": {
        "data_table": table(["Reaction", "Effect"], [
            ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
            ["Caramelization", "Browning of sugars when heated"],
        ]),
    },
    "foreign-languages-ug2-l3": {
        "data_table": table(["Concept", "Meaning"], [
            ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
            ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
        ]),
    },
    "general-knowledge-ug2-l3": {
        "data_table": table(["Intellectual Movement", "Approx. Period"], [
            ["The Renaissance", "14th-17th century"], ["The Enlightenment", "17th-18th century"],
        ]),
    },
    "social-studies-ug2-l3": {
        "data_table": table(["Sociological Perspective", "Core Idea"], [
            ["Functionalism", "Society is a system of interdependent parts working together"],
            ["Conflict theory", "Society is shaped by competition over scarce resources"],
            ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
        ]),
    },
    "physical-education-and-self-defense-ug2-l3": {
        "data_table": table(["Adaptation", "Effect of Aerobic Training"], [
            ["VO2 max", "Increases (greater oxygen uptake capacity)"],
            ["Resting heart rate", "Decreases"], ["Stroke volume", "Increases (more blood pumped per beat)"],
        ]),
    },
    "first-aid-ug2-l3": {
        "data_table": table(["Wound Care Step", "Action"], [
            ["1", "Clean hands and wear gloves if available"],
            ["2", "Stop the bleeding with direct pressure"],
            ["3", "Clean the wound with water"], ["4", "Cover with a sterile dressing"],
        ]),
    },
    "physics-ug2-l3": {
        "formulae": ["v = u + at", "s = ut + 1/2at^2"],
        "data_table": table(["Symbol", "Meaning"], [
            ["u", "Initial velocity"], ["v", "Final velocity"], ["a", "Acceleration"],
            ["t", "Time"], ["s", "Displacement"],
        ]),
    },
    "chemistry-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Amino acid", "The building block of proteins (contains an amino group and carboxyl group)"],
            ["Peptide bond", "The bond linking amino acids together"],
        ]),
    },
    "biology-ug2-l3": {
        "data_table": table(["Growth Model", "Pattern"], [
            ["Exponential growth", "Unlimited resources; population grows continuously faster"],
            ["Logistic growth", "Growth slows as population nears carrying capacity"],
        ]),
    },
    "critical-thinking-ug2-l3": {
        "data_table": table(["Game", "Nash Equilibrium"], [
            ["Prisoner's Dilemma", "(Defect, Defect)"], ["Matching Pennies", "Mixed strategy (1/2, 1/2)"],
        ]),
    },
    "health-education-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Incidence", "Number of new cases in a population over a time period"],
            ["Prevalence", "Total number of existing cases at a given time"],
        ]),
    },
    "ict-and-computer-science-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital transformation", "Integrating digital technology into all areas of a business"],
            ["Legacy system", "An older technology system still in use"],
        ]),
    },
    "business-studies-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-ug2-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-ug2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-ug2-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-ug2-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
    "mythology-ug2-l1": {
        "data_table": table(["Hindu Text", "Type"], [
            ["The Vedas", "Oldest Hindu scriptures; hymns and rituals"],
            ["The Upanishads", "Philosophical texts exploring the nature of reality"],
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
        raise SystemExit(f"Lesson ids not found in level_ug2.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level UG2 lessons (all 52 subjects).")


if __name__ == "__main__":
    main()
