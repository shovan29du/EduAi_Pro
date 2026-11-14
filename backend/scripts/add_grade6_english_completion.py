#!/usr/bin/env python3
"""Depth pass, Grade 6 English: fill in real, hand-checked data_table
content for the 28 Grade 6 English lessons not covered by the earlier
breadth-first batch. Brings Grade 6 English to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g6-l1": {
        "data_table": table(["Element", "Purpose"], [
            ["Claim", "States the writer's opinion"], ["Evidence", "Supports the claim"],
        ]),
    },
    "english-g6-l2": {
        "data_table": table(["Structure Part", "Purpose"], [
            ["Exposition", "Introduces characters and setting"], ["Climax", "The most intense moment"],
        ]),
    },
    "english-g6-l3": {
        "data_table": table(["Sensory Detail", "Example"], [
            ["Sight", "The bright red apple"], ["Sound", "The crackling fire"],
        ]),
    },
    "english-g6-l4": {
        "data_table": table(["Text Type", "Purpose"], [
            ["Expository", "Explains or informs about a topic"],
        ]),
    },
    "english-g6-l5": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Noun", "book, city"], ["Verb", "run, think"], ["Adjective", "bright, tall"],
        ]),
    },
    "english-g6-l6": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Compound", "I like tea, and I like coffee."], ["Complex", "Although it rained, we went outside."],
        ]),
    },
    "english-g6-l7": {
        "data_table": table(["Subject", "Correct Verb"], [
            ["He (singular)", "runs"], ["They (plural)", "run"],
        ]),
    },
    "english-g6-l8": {
        "data_table": table(["Punctuation", "Use"], [
            ["Comma", "Separates items in a list"], ["Semicolon", "Joins two related independent clauses"],
        ]),
    },
    "english-g6-l9": {
        "data_table": table(["Voice", "Example"], [
            ["Active", "The dog chased the ball."], ["Passive", "The ball was chased by the dog."],
        ]),
    },
    "english-g6-l11": {
        "data_table": table(["Idiom", "Meaning"], [
            ["Break the ice", "Start a conversation"], ["Piece of cake", "Something very easy"],
        ]),
    },
    "english-g6-l12": {
        "data_table": table(["Term", "Definition"], [
            ["Theme", "The underlying message or lesson of a story"],
            ["Central idea", "The main point of a nonfiction text"],
        ]),
    },
    "english-g6-l13": {
        "data_table": table(["Concept", "Meaning"], [
            ["Character development", "How a character changes over the story"],
            ["Characterization", "How an author reveals a character's traits"],
        ]),
    },
    "english-g6-l14": {
        "data_table": table(["Plot Element", "Definition"], [
            ["Conflict", "The problem driving the story"], ["Resolution", "How the conflict is solved"],
        ]),
    },
    "english-g6-l15": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Third person", "he, she, they"],
        ]),
    },
    "english-g6-l17": {
        "data_table": table(["Text Feature", "Purpose"], [
            ["Heading", "Labels a section"], ["Caption", "Explains an image"],
        ]),
    },
    "english-g6-l18": {
        "data_table": table(["Skill", "Definition"], [
            ["Summarizing", "Retelling the main points briefly"], ["Paraphrasing", "Restating in your own words"],
        ]),
    },
    "english-g6-l19": {
        "data_table": table(["Skill", "Definition"], [
            ["Inference", "A conclusion drawn from clues and prior knowledge"],
        ]),
    },
    "english-g6-l20": {
        "data_table": table(["Structure", "Signal Words"], [
            ["Compare and contrast", "similarly, however, both"],
        ]),
    },
    "english-g6-l21": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Bullet points", "Captures key ideas quickly"], ["Source tracking", "Keeps citations organized"],
        ]),
    },
    "english-g6-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Citation", "Credit given to the original source"], ["Plagiarism", "Using someone's work without credit"],
        ]),
    },
    "english-g6-l23": {
        "data_table": table(["Step", "Purpose"], [
            ["Drafting", "Writing the first version"], ["Revising", "Improving content and organization"],
        ]),
    },
    "english-g6-l24": {
        "data_table": table(["Step", "Focus"], [
            ["Editing", "Fixing grammar and word choice"], ["Proofreading", "Catching remaining small errors"],
        ]),
    },
    "english-g6-l25": {
        "data_table": table(["Strategy", "Example"], [
            ["Context clues", "Using surrounding words to guess an unknown word's meaning"],
        ]),
    },
    "english-g6-l26": {
        "data_table": table(["Type", "Example", "Meaning Change"], [
            ["Prefix", "re + write = rewrite", "Write again"],
            ["Root", "'photo' (light) in 'photograph'", "Base meaning"],
        ]),
    },
    "english-g6-l27": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Eye contact", "Engages the audience"], ["Clear pace", "Helps listeners understand"],
        ]),
    },
    "english-g6-l28": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active listening", "Fully focusing on the speaker"], ["Note-taking", "Captures key points for later"],
        ]),
    },
    "english-g6-l29": {
        "data_table": table(["Purpose", "Example"], [
            ["To persuade", "An opinion editorial"], ["To inform", "A textbook"], ["To entertain", "A novel"],
        ]),
    },
    "english-g6-l30": {
        "data_table": table(["Rule", "Example"], [
            ["Use quotation marks", "\"Let's go,\" she said."], ["New line for new speaker", "Each character's dialogue starts a new paragraph"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 English lessons (completing 30/30).")


if __name__ == "__main__":
    main()
