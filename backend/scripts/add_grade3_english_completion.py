#!/usr/bin/env python3
"""Depth pass, Grade 3 English: fill in real, hand-checked data_table
content for the 18 Grade 3 English lessons not covered by the earlier
breadth-first batch. Brings Grade 3 English to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g3-l1": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Predicting", "Guessing what happens next using clues"],
            ["Summarizing", "Retelling the main points in your own words"],
        ]),
    },
    "english-g3-l2": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Noun", "dog, city, happiness"], ["Verb", "run, think, is"],
        ]),
    },
    "english-g3-l3": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Adjective", "blue, tall, happy"], ["Adverb", "quickly, loudly, well"],
        ]),
    },
    "english-g3-l4": {
        "data_table": table(["Sentence Part", "Example"], [
            ["Subject", "The dog"], ["Predicate", "ran across the yard"],
        ]),
    },
    "english-g3-l5": {
        "data_table": table(["Conjunction", "Example Sentence"], [
            ["and", "I like tea, and I like coffee."], ["but", "I wanted to go, but it rained."],
        ]),
    },
    "english-g3-l6": {
        "data_table": table(["Punctuation Mark", "Use"], [
            ["Period (.)", "Ends a statement"], ["Question mark (?)", "Ends a question"],
            ["Exclamation mark (!)", "Shows strong feeling"],
        ]),
    },
    "english-g3-l7": {
        "data_table": table(["Rule", "Example"], [
            ["Capitalize the first word of a sentence", "The sun is bright."],
            ["Capitalize proper nouns", "London, Monday, Sarah"],
        ]),
    },
    "english-g3-l8": {
        "data_table": table(["Word", "Synonym", "Antonym"], [
            ["Happy", "Joyful", "Sad"], ["Big", "Large", "Small"],
        ]),
    },
    "english-g3-l10": {
        "data_table": table(["Type", "Example", "Meaning Change"], [
            ["Prefix", "un + happy = unhappy", "Not happy"],
            ["Suffix", "help + ful = helpful", "Full of help"],
        ]),
    },
    "english-g3-l11": {
        "data_table": table(["Fluency Skill", "Why It Matters"], [
            ["Reading at a steady pace", "Helps understanding"],
            ["Using expression", "Makes reading engaging"],
        ]),
    },
    "english-g3-l12": {
        "data_table": table(["Story Element", "Definition"], [
            ["Character", "A person or animal in the story"],
            ["Setting", "Where and when the story happens"],
            ["Plot", "The sequence of events"],
        ]),
    },
    "english-g3-l13": {
        "data_table": table(["Concept", "Definition"], [
            ["Main idea", "The most important point of a text"],
            ["Detail", "A fact that supports the main idea"],
        ]),
    },
    "english-g3-l14": {
        "data_table": table(["Sequence Word", "Use"], [
            ["First", "Shows the beginning"], ["Next", "Shows what comes after"], ["Finally", "Shows the ending"],
        ]),
    },
    "english-g3-l15": {
        "data_table": table(["Cause", "Effect"], [
            ["It rained heavily", "The picnic was cancelled"], ["She studied hard", "She passed the test"],
        ]),
    },
    "english-g3-l16": {
        "data_table": table(["Narrative Element", "Example"], [
            ["First person point of view", "Uses 'I' and 'me'"], ["Personal experience", "A real event from your life"],
        ]),
    },
    "english-g3-l17": {
        "data_table": table(["Descriptive Technique", "Example"], [
            ["Sensory detail", "The crisp, cold air"], ["Vivid adjective", "The sparkling blue ocean"],
        ]),
    },
    "english-g3-l18": {
        "data_table": table(["Letter Part", "Purpose"], [
            ["Greeting", "Dear [Name],"], ["Body", "The main message"], ["Closing", "Sincerely, [Your name]"],
        ]),
    },
    "english-g3-l20": {
        "data_table": table(["Poetry Term", "Meaning"], [
            ["Rhyme", "Words that end with the same sound"], ["Stanza", "A group of lines in a poem"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 English lessons (completing 20/20).")


if __name__ == "__main__":
    main()
