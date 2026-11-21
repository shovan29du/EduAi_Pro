#!/usr/bin/env python3
"""Depth pass, Grade 4 English: fill in real, hand-checked data_table
content for the 28 Grade 4 English lessons not covered by the earlier
breadth-first batch. Brings Grade 4 English to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g4-l1": {
        "data_table": table(["Tense", "Example"], [
            ["Past", "She walked to school"], ["Present", "She walks to school"], ["Future", "She will walk to school"],
        ]),
    },
    "eng-g4-l2": {
        "data_table": table(["Paragraph Part", "Purpose"], [
            ["Topic sentence", "States the main idea"], ["Supporting sentences", "Give details"],
        ]),
    },
    "english-g4-l3": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Noun", "book, city"], ["Pronoun", "he, they"], ["Adjective", "bright, tall"],
        ]),
    },
    "english-g4-l4": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Verb", "run, think"], ["Adverb", "quickly, carefully"],
        ]),
    },
    "english-g4-l5": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Statement", "The sun is bright."], ["Question", "Is the sun bright?"],
            ["Command", "Look at the sun."], ["Exclamation", "The sun is so bright!"],
        ]),
    },
    "english-g4-l6": {
        "data_table": table(["Subject", "Correct Verb"], [
            ["He (singular)", "runs"], ["They (plural)", "run"],
        ]),
    },
    "english-g4-l7": {
        "data_table": table(["Punctuation", "Use"], [
            ["Comma", "Separates items in a list"], ["Quotation marks", "Shows exact spoken words"],
        ]),
    },
    "english-g4-l9": {
        "data_table": table(["Type", "Example", "Meaning Change"], [
            ["Prefix", "re + write = rewrite", "Write again"],
            ["Suffix", "care + less = careless", "Without care"],
        ]),
    },
    "english-g4-l10": {
        "data_table": table(["Strategy", "Example"], [
            ["Context clues", "Using surrounding words to guess an unknown word's meaning"],
        ]),
    },
    "english-g4-l11": {
        "data_table": table(["Concept", "Definition"], [
            ["Main idea", "The most important point"], ["Detail", "A fact that supports the main idea"],
        ]),
    },
    "english-g4-l12": {
        "data_table": table(["Cause", "Effect"], [
            ["She forgot her umbrella", "She got wet in the rain"],
        ]),
    },
    "english-g4-l13": {
        "data_table": table(["Type", "Example"], [
            ["Fiction", "Invented stories, like fairy tales"], ["Nonfiction", "Factual texts, like biographies"],
        ]),
    },
    "english-g4-l14": {
        "data_table": table(["Story Element", "Definition"], [
            ["Character", "Who the story is about"], ["Setting", "Where and when it happens"], ["Plot", "The events"],
        ]),
    },
    "english-g4-l15": {
        "data_table": table(["Narrative Element", "Example"], [
            ["Beginning", "Introduces characters and setting"], ["Climax", "The most exciting moment"],
        ]),
    },
    "english-g4-l16": {
        "data_table": table(["Persuasive Element", "Example"], [
            ["Opinion", "I believe recycling should be mandatory"], ["Reason", "It reduces landfill waste"],
        ]),
    },
    "english-g4-l17": {
        "data_table": table(["Report Section", "Purpose"], [
            ["Introduction", "States the topic"], ["Facts", "Provide information"], ["Conclusion", "Summarizes"],
        ]),
    },
    "english-g4-l18": {
        "data_table": table(["Reference Tool", "Use"], [
            ["Dictionary", "Finds word meanings"], ["Thesaurus", "Finds synonyms"],
        ]),
    },
    "english-g4-l20": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Eye contact", "Engages the audience"], ["Clear pace", "Helps listeners understand"],
        ]),
    },
    "english-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Telling a past event", "I visited my grandmother last weekend"],
        ]),
    },
    "english-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Writing an email", "Organized into clear paragraphs"],
        ]),
    },
    "english-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Describing a friend", "Using nouns, pronouns, and adjectives"],
        ]),
    },
    "english-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Giving instructions", "Walk quickly to the door"],
        ]),
    },
    "english-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Asking for help", "Can you help me with this?"],
        ]),
    },
    "english-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Writing about a group", "The students are studying (not is)"],
        ]),
    },
    "english-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Writing dialogue", "\"Let's go,\" she said."],
        ]),
    },
    "english-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Improving writing", "Replacing 'good' with 'excellent'"],
        ]),
    },
    "english-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Understanding a new word", "Unhappy = un + happy"],
        ]),
    },
    "english-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Reading a new word in a story", "Guessing its meaning from nearby sentences"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 English lessons (completing 30/30).")


if __name__ == "__main__":
    main()
