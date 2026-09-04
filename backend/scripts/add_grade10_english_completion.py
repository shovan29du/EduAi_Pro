#!/usr/bin/env python3
"""Depth pass, Grade 10 English: fill in real, hand-checked data_table
content for the Grade 10 English lessons not covered by the earlier
breadth-first batch. Brings Grade 10 English to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g10-l1": {
        "data_table": table(["Essay Part", "Purpose"], [
            ["Thesis statement", "States the essay's central argument"], ["Topic sentence", "Introduces a paragraph's main idea"],
        ]),
    },
    "eng-g10-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Language and power", "How word choice can assert or challenge authority"],
        ]),
    },
    "english-g10-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Hamlet", "Shakespeare tragedy about a Danish prince seeking revenge"],
        ]),
    },
    "english-g10-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Harper Lee"], ["Setting", "Depression-era Alabama"],
        ]),
    },
    "english-g10-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "George Orwell"], ["Genre", "Dystopian novel, published 1949"],
        ]),
    },
    "english-g10-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "F. Scott Fitzgerald"], ["Setting", "Jazz Age Long Island"],
        ]),
    },
    "english-g10-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Dystopia", "A fictional society depicted as undesirable, used to critique real issues"],
        ]),
    },
    "english-g10-l9": {
        "data_table": table(["Element", "Meaning"], [
            ["Stanza", "A grouped set of lines in a poem"], ["Meter", "The rhythmic pattern of a poem"],
        ]),
    },
    "english-g10-l10": {
        "data_table": table(["Device", "Meaning"], [
            ["Imagery", "Descriptive language appealing to the senses"], ["Symbolism", "Using an object to represent an idea"],
        ]),
    },
    "english-g10-l12": {
        "data_table": table(["Poet", "Known For"], [
            ["Wilfred Owen", "War poetry depicting the horrors of WWI"],
        ]),
    },
    "english-g10-l13": {
        "data_table": table(["Device", "Purpose"], [
            ["Ethos", "Appeals to credibility"], ["Pathos", "Appeals to emotion"], ["Logos", "Appeals to logic"],
        ]),
    },
    "english-g10-l14": {
        "data_table": table(["Part", "Purpose"], [
            ["Claim", "States the position"], ["Evidence", "Supports the claim"], ["Rebuttal", "Addresses counterarguments"],
        ]),
    },
    "english-g10-l15": {
        "data_table": table(["Part", "Purpose"], [
            ["Introduction", "Presents the thesis"], ["Body paragraphs", "Analyze evidence supporting the thesis"],
        ]),
    },
    "english-g10-l16": {
        "data_table": table(["Point of View", "Example"], [
            ["First person", "'I walked to the store.'"], ["Third person omniscient", "Narrator knows all characters' thoughts"],
        ]),
    },
    "english-g10-l17": {
        "data_table": table(["Method", "Example"], [
            ["Direct characterization", "Author states a trait outright"], ["Indirect characterization", "Trait shown through actions or dialogue"],
        ]),
    },
    "english-g10-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Setting", "The time and place of a story"], ["Atmosphere", "The emotional mood created by the setting"],
        ]),
    },
    "english-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Theme", "The central message of a work"], ["Motif", "A recurring element that supports the theme"],
        ]),
    },
    "english-g10-l20": {
        "data_table": table(["Device", "Meaning"], [
            ["Satire", "Uses humor to criticize"], ["Irony", "Contrast between expectation and reality"],
        ]),
    },
    "english-g10-l21": {
        "data_table": table(["Feature", "Example"], [
            ["Gothic literature", "Combines horror, romance, and the supernatural"],
        ]),
    },
    "english-g10-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Bildungsroman", "A novel focused on the moral and psychological growth of its protagonist"],
        ]),
    },
    "english-g10-l23": {
        "data_table": table(["Approach", "Focus"], [
            ["Literary criticism", "Interpreting and evaluating literature through a critical lens"],
        ]),
    },
    "english-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Postcolonial literature", "Literature examining the effects of colonialism"],
        ]),
    },
    "english-g10-l25": {
        "data_table": table(["Skill", "Purpose"], [
            ["Comparative analysis", "Examines similarities and differences between texts"],
        ]),
    },
    "english-g10-l26": {
        "data_table": table(["Skill", "Purpose"], [
            ["Eye contact", "Engages the audience during a speech"],
        ]),
    },
    "english-g10-l27": {
        "data_table": table(["Element", "Purpose"], [
            ["Rebuttal", "Responds directly to the opposing argument"],
        ]),
    },
    "english-g10-l28": {
        "data_table": table(["Concept", "Meaning"], [
            ["Media bias", "Slanted presentation of information favoring a viewpoint"],
        ]),
    },
    "english-g10-l29": {
        "data_table": table(["Style", "Feature"], [
            ["Journalistic writing", "Concise, factual, and objective"],
        ]),
    },
    "english-g10-l30": {
        "data_table": table(["Element", "Purpose"], [
            ["Plot arc", "The sequence of events building tension in a short story"],
        ]),
    },
    "english-g10-l31": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sensory detail", "Helps the reader vividly picture a scene"],
        ]),
    },
    "english-g10-l32": {
        "data_table": table(["Clause Type", "Example"], [
            ["Independent clause", "Can stand alone as a sentence"], ["Dependent clause", "Cannot stand alone"],
        ]),
    },
    "english-g10-l33": {
        "data_table": table(["Voice", "Example"], [
            ["Active voice", "'She wrote the letter.'"], ["Passive voice", "'The letter was written by her.'"],
        ]),
    },
    "english-g10-l34": {
        "data_table": table(["Root", "Meaning"], [
            ["'bio'", "Life"], ["'graph'", "Write"],
        ]),
    },
    "english-g10-l35": {
        "data_table": table(["Format", "Use"], [
            ["Formal letter", "Business or official correspondence"], ["Report", "Structured presentation of findings"],
        ]),
    },
    "english-g10-l36": {
        "data_table": table(["Citation Style", "Common Use"], [
            ["MLA", "Humanities"], ["APA", "Social sciences"],
        ]),
    },
    "english-g10-l37": {
        "data_table": table(["Technique", "Purpose"], [
            ["Close reading", "Careful, detailed analysis of a short passage"],
        ]),
    },
    "english-g10-l38": {
        "data_table": table(["Element", "Meaning"], [
            ["Stage direction", "Instructions describing actor movement or setting"],
        ]),
    },
    "english-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Tennessee Williams"], ["Genre", "American modern drama"],
        ]),
    },
    "english-g10-l40": {
        "data_table": table(["Feature", "Example"], [
            ["Absurdist theatre", "Depicts illogical, meaningless situations"],
        ]),
    },
    "english-g10-l41": {
        "data_table": table(["Feature", "Example"], [
            ["Short story", "A compact narrative form focused on a single incident"],
        ]),
    },
    "english-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Memoir", "A first-person account focused on a specific period or theme in the author's life"],
        ]),
    },
    "english-g10-l43": {
        "data_table": table(["Element", "Purpose"], [
            ["Rhetorical question", "Engages the audience without expecting an answer"],
        ]),
    },
    "english-g10-l44": {
        "data_table": table(["Skill", "Purpose"], [
            ["Identifying author's purpose", "Reveals intent behind a non-fiction text"],
        ]),
    },
    "english-g10-l45": {
        "data_table": table(["Element", "Purpose"], [
            ["Target audience", "Shapes an advertisement's tone and imagery"],
        ]),
    },
    "english-g10-l46": {
        "data_table": table(["Format", "Example"], [
            ["Multimedia composition", "Combines text, image, and sound to communicate"],
        ]),
    },
    "english-g10-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Proofreading", "Catches spelling and grammar errors"], ["Editing", "Improves clarity and structure"],
        ]),
    },
    "english-g10-l48": {
        "data_table": table(["Variety", "Region"], [
            ["British English", "United Kingdom"], ["American English", "United States"],
        ]),
    },
    "english-g10-l49": {
        "data_table": table(["Period", "Feature"], [
            ["Old English", "c. 450-1150 CE"], ["Middle English", "c. 1150-1500 CE, includes Chaucer"],
        ]),
    },
    "english-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Adaptation", "Reworking a text into a new medium, e.g. a novel into a film"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 English lessons (completing 50/50).")


if __name__ == "__main__":
    main()
