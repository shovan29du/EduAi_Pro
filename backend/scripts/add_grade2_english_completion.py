#!/usr/bin/env python3
"""Depth pass, Grade 2 English: fill in real, hand-checked data_table
content for the 18 Grade 2 English lessons not covered by the earlier
breadth-first batch. Brings Grade 2 English to full 20/20 coverage.

Content covers real grammar categories, real compound words and
contractions, and real letter-writing structure -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g2-l1": {
        "data_table": table(["Type", "Example"], [
            ["Fiction", "A made-up story about talking animals"],
            ["Non-fiction", "A true book about real animals"],
        ]),
    },
    "eng-g2-l2": {
        "data_table": table(["Word Type", "Example"], [
            ["Adjective (describes a noun)", "The big dog"], ["Adverb (describes a verb)", "She ran quickly"],
        ]),
    },
    "english-g2-l3": {
        "data_table": table(["Noun Type", "Example"], [
            ["Person", "Teacher"], ["Place", "Park"], ["Thing", "Book"],
        ]),
    },
    "english-g2-l4": {
        "data_table": table(["Verb", "Action"], [
            ["Run", "Moving fast on foot"], ["Jump", "Pushing off the ground"],
            ["Read", "Looking at and understanding words"],
        ]),
    },
    "english-g2-l5": {
        "data_table": table(["Pronoun", "Replaces"], [
            ["He", "A boy's or man's name"], ["She", "A girl's or woman's name"], ["It", "An object or animal"],
        ]),
    },
    "english-g2-l6": {
        "data_table": table(["Sentence Type", "Example", "End Punctuation"], [
            ["Statement", "The dog is brown.", "."], ["Question", "Is the dog brown?", "?"],
        ]),
    },
    "english-g2-l7": {
        "data_table": table(["Rule", "Example"], [
            ["Capitalize the first word", "The sun is shining."],
            ["Capitalize names", "My friend is Maria."],
        ]),
    },
    "english-g2-l8": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Predicting", "Guessing what happens next"], ["Summarizing", "Retelling the main points"],
        ]),
    },
    "english-g2-l9": {
        "data_table": table(["Clue Type", "Example"], [
            ["Definition clue", "'The canine, or dog, barked.'"],
            ["Example clue", "'Fruits, such as apples and bananas...'"],
        ]),
    },
    "english-g2-l11": {
        "data_table": table(["Compound Word", "Two Words Combined"], [
            ["Sunflower", "Sun + Flower"], ["Basketball", "Basket + Ball"], ["Snowman", "Snow + Man"],
        ]),
    },
    "english-g2-l12": {
        "data_table": table(["Contraction", "Full Words"], [
            ["Don't", "Do not"], ["Can't", "Cannot"], ["It's", "It is"],
        ]),
    },
    "english-g2-l13": {
        "data_table": table(["Paragraph Part", "Purpose"], [
            ["Topic sentence", "States the main idea"], ["Supporting sentences", "Give details"],
        ]),
    },
    "english-g2-l14": {
        "data_table": table(["Letter Part", "Example"], [
            ["Greeting", "Dear Grandma,"], ["Closing", "Love, Sam"],
        ]),
    },
    "english-g2-l15": {
        "data_table": table(["Element", "Meaning"], [
            ["Character", "Who the story is about"], ["Setting", "Where and when it happens"],
            ["Plot", "What happens in the story"],
        ]),
    },
    "english-g2-l16": {
        "data_table": table(["Sequence Word", "When to Use"], [
            ["First", "The beginning"], ["Next", "In the middle"], ["Finally", "The end"],
        ]),
    },
    "english-g2-l17": {
        "data_table": table(["Word Family", "Example Words"], [
            ["-at", "cat, hat, mat"], ["-og", "dog, log, fog"],
        ]),
    },
    "english-g2-l18": {
        "data_table": table(["Affix", "Meaning", "Example"], [
            ["un-", "not", "unhappy"], ["-ful", "full of", "joyful"],
        ]),
    },
    "english-g2-l20": {
        "data_table": table(["Skill", "Example"], [
            ["Eye contact", "Looking at your audience"], ["Active listening", "Nodding and paying attention"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 English lessons (completing 20/20).")


if __name__ == "__main__":
    main()
