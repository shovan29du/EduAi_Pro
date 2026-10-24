#!/usr/bin/env python3
"""Depth pass, Grade 9 English: fill in real, hand-checked data_table
content for the 48 Grade 9 English lessons not covered by the earlier
breadth-first batch. Brings Grade 9 English to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "english-g9-l2": {
        "data_table": table(["Element", "Definition"], [
            ["Character", "Who the story is about"], ["Plot", "The sequence of events"],
        ]),
    },
    "english-g9-l3": {
        "data_table": table(["Poetic Form", "Structure"], [
            ["Sonnet", "14 lines, structured rhyme scheme"], ["Haiku", "3 lines, 5-7-5 syllables"],
        ]),
    },
    "english-g9-l5": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeals to credibility"], ["Pathos", "Appeals to emotion"], ["Logos", "Appeals to logic"],
        ]),
    },
    "english-g9-l6": {
        "data_table": table(["Essay Part", "Purpose"], [
            ["Thesis statement", "States the main argument"], ["Counterargument", "Addresses the opposing view"],
        ]),
    },
    "english-g9-l7": {
        "data_table": table(["Text Type", "Purpose"], [
            ["Expository", "Explains or informs about a topic"],
        ]),
    },
    "english-g9-l8": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Third person", "he, she, they"],
        ]),
    },
    "english-g9-l9": {
        "data_table": table(["Sensory Detail", "Example"], [
            ["Sight", "The bright red apple"], ["Sound", "The crackling fire"],
        ]),
    },
    "english-g9-l10": {
        "data_table": table(["Element", "Purpose"], [
            ["Short story", "A brief fictional narrative focused on a single effect"],
        ]),
    },
    "english-g9-l11": {
        "data_table": table(["Concept", "Meaning"], [
            ["Character development", "How a character changes over the story"],
        ]),
    },
    "english-g9-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Theme", "The underlying message of a story"], ["Symbolism", "An object representing a larger idea"],
        ]),
    },
    "english-g9-l13": {
        "data_table": table(["Element", "Definition"], [
            ["Setting", "Where and when a story takes place"], ["Atmosphere", "The mood created by the setting"],
        ]),
    },
    "english-g9-l14": {
        "data_table": table(["Plot Element", "Definition"], [
            ["Conflict", "The problem driving the story"], ["Climax", "The turning point"],
        ]),
    },
    "english-g9-l15": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["Third person omniscient", "Knows all characters' thoughts"], ["Third person limited", "One character's thoughts"],
        ]),
    },
    "english-g9-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Novel", "A long fictional narrative"],
        ]),
    },
    "english-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Coming-of-age story", "A story about a character growing from youth to maturity"],
        ]),
    },
    "english-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Dystopia", "An imagined society that is undesirable or frightening"],
        ]),
    },
    "english-g9-l19": {
        "data_table": table(["Genre", "Definition"], [
            ["Autobiography", "A true account written by the subject themselves"],
            ["Memoir", "A personal account focused on specific experiences"],
        ]),
    },
    "english-g9-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Essay", "A short piece of writing on a particular subject"],
        ]),
    },
    "english-g9-l21": {
        "data_table": table(["Device", "Example"], [
            ["Anaphora", "Repetition at the start of successive clauses"], ["Rhetorical question", "A question asked for effect"],
        ]),
    },
    "english-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Tone", "The author's attitude toward the subject"], ["Mood", "The feeling created for the reader"],
        ]),
    },
    "english-g9-l23": {
        "data_table": table(["Device", "Example"], [
            ["Metaphor", "Time is a thief"], ["Simile", "As brave as a lion"],
        ]),
    },
    "english-g9-l24": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Compound", "I like tea, and I like coffee."], ["Complex", "Although it rained, we went outside."],
        ]),
    },
    "english-g9-l25": {
        "data_table": table(["Voice", "Example"], [
            ["Active", "The dog chased the ball."], ["Passive", "The ball was chased by the dog."],
        ]),
    },
    "english-g9-l26": {
        "data_table": table(["Punctuation", "Use"], [
            ["Semicolon", "Joins two related independent clauses"], ["Colon", "Introduces a list or explanation"],
        ]),
    },
    "english-g9-l27": {
        "data_table": table(["Type", "Example", "Meaning Change"], [
            ["Prefix", "re + write = rewrite", "Write again"],
        ]),
    },
    "english-g9-l28": {
        "data_table": table(["Register", "Example"], [
            ["Formal", "'I would like to request'"], ["Informal", "'Wanna grab a snack?'"],
        ]),
    },
    "english-g9-l29": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Eye contact", "Engages the audience"], ["Clear pace", "Helps listeners understand"],
        ]),
    },
    "english-g9-l30": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "english-g9-l31": {
        "data_table": table(["Skill", "Purpose"], [
            ["Source evaluation", "Judging whether a source is trustworthy"],
        ]),
    },
    "english-g9-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Citation", "Credit given to the original source"], ["Plagiarism", "Using someone's work without credit"],
        ]),
    },
    "english-g9-l33": {
        "data_table": table(["Report Section", "Purpose"], [
            ["Introduction", "States the topic"], ["Findings", "Presents the researched information"],
        ]),
    },
    "english-g9-l34": {
        "data_table": table(["Journalism Term", "Meaning"], [
            ["Headline", "A short title summarizing the story"], ["Byline", "Credits the article's author"],
        ]),
    },
    "english-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"],
        ]),
    },
    "english-g9-l36": {
        "data_table": table(["Text Feature", "Purpose"], [
            ["Heading", "Labels a section"], ["Citation", "Credits a source"],
        ]),
    },
    "english-g9-l37": {
        "data_table": table(["Comparison Type", "Example"], [
            ["Theme comparison", "Comparing themes of courage across two stories"],
        ]),
    },
    "english-g9-l38": {
        "data_table": table(["Script Element", "Purpose"], [
            ["Stage direction", "Describes actor movement or setting"], ["Dialogue", "What characters say"],
        ]),
    },
    "english-g9-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Monologue", "A long speech by a single character"],
        ]),
    },
    "english-g9-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Satire", "Using humor or irony to criticize behavior or ideas"],
            ["Irony", "A contrast between expectation and reality"],
        ]),
    },
    "english-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Allegory", "A story with a hidden symbolic meaning"], ["Fable", "A short story with a moral, often using animals"],
        ]),
    },
    "english-g9-l42": {
        "data_table": table(["Epic", "Hero"], [
            ["The Iliad", "Achilles"], ["The Odyssey", "Odysseus"],
        ]),
    },
    "english-g9-l43": {
        "data_table": table(["Sonnet Type", "Rhyme Scheme"], [
            ["Shakespearean", "ABABCDCDEFEFGG"], ["Petrarchan", "ABBAABBA + sestet"],
        ]),
    },
    "english-g9-l44": {
        "data_table": table(["Poetic Form", "Feature"], [
            ["Free verse", "No fixed rhyme or meter"],
        ]),
    },
    "english-g9-l45": {
        "data_table": table(["Step", "Focus"], [
            ["Editing", "Fixing grammar and word choice"], ["Proofreading", "Catching remaining small errors"],
        ]),
    },
    "english-g9-l46": {
        "data_table": table(["Step", "Purpose"], [
            ["Drafting", "Writing the first version"], ["Revising", "Improving content and organization"],
        ]),
    },
    "english-g9-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["World-building", "Creating a fictional setting with its own rules"],
        ]),
    },
    "english-g9-l48": {
        "data_table": table(["Format", "Use"], [
            ["Formal letter", "Business or official communication"], ["Email", "Quick digital correspondence"],
        ]),
    },
    "english-g9-l49": {
        "data_table": table(["Advertising Technique", "Example"], [
            ["Bandwagon", "'Everyone is doing it, so you should too'"],
        ]),
    },
    "english-g9-l50": {
        "data_table": table(["Discussion Skill", "Purpose"], [
            ["Active listening", "Fully focusing on others' points"], ["Textual evidence", "Supports your interpretation"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 English lessons (completing 50/50).")


if __name__ == "__main__":
    main()
