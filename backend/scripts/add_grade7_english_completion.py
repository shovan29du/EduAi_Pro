#!/usr/bin/env python3
"""Depth pass, Grade 7 English: fill in real, hand-checked data_table
content for the 38 Grade 7 English lessons not covered by the earlier
breadth-first batch. Brings Grade 7 English to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g7-l1": {
        "data_table": table(["Poetic Device", "Example"], [
            ["Metaphor", "Time is a thief"], ["Alliteration", "Peter Piper picked"],
        ]),
    },
    "english-g7-l2": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Noun", "book, city"], ["Verb", "run, think"], ["Adjective", "bright, tall"],
        ]),
    },
    "english-g7-l3": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Simple", "The dog ran."], ["Compound", "The dog ran, and it barked."],
            ["Complex", "Although it rained, the dog ran."],
        ]),
    },
    "english-g7-l4": {
        "data_table": table(["Term", "Example"], [
            ["Clause", "A group of words with a subject and verb"],
            ["Phrase", "A group of words without a subject and verb, like 'in the morning'"],
        ]),
    },
    "english-g7-l5": {
        "data_table": table(["Voice", "Example"], [
            ["Active", "The dog chased the ball."], ["Passive", "The ball was chased by the dog."],
        ]),
    },
    "english-g7-l6": {
        "data_table": table(["Punctuation", "Common Error"], [
            ["Apostrophe", "'its' (possessive) vs 'it's' (it is)"], ["Comma splice", "Joining two sentences with only a comma"],
        ]),
    },
    "english-g7-l7": {
        "data_table": table(["Pattern", "Example"], [
            ["Silent e", "make, bike"], ["ie vs ei", "believe, receive"],
        ]),
    },
    "english-g7-l9": {
        "data_table": table(["Academic Word", "Meaning"], [
            ["Analyze", "To examine in detail"], ["Synthesize", "To combine ideas into a whole"],
        ]),
    },
    "english-g7-l11": {
        "data_table": table(["Device", "Example"], [
            ["Foreshadowing", "Hints at what's to come"], ["Symbolism", "An object representing a larger idea"],
        ]),
    },
    "english-g7-l12": {
        "data_table": table(["Element", "Purpose"], [
            ["Voice", "The writer's distinctive style"], ["Structure", "How events are ordered"],
        ]),
    },
    "english-g7-l13": {
        "data_table": table(["Sensory Detail", "Example"], [
            ["Sight", "The bright red apple"], ["Sound", "The crackling fire"],
        ]),
    },
    "english-g7-l14": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeals to credibility"], ["Pathos", "Appeals to emotion"], ["Logos", "Appeals to logic"],
        ]),
    },
    "english-g7-l15": {
        "data_table": table(["Text Type", "Purpose"], [
            ["Expository", "Explains or informs about a topic"],
        ]),
    },
    "english-g7-l16": {
        "data_table": table(["Element", "Purpose"], [
            ["Thesis statement", "States the main argument of an essay"],
        ]),
    },
    "english-g7-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Topic sentence", "States the main idea of a paragraph"], ["Supporting detail", "Backs up the topic sentence"],
        ]),
    },
    "english-g7-l18": {
        "data_table": table(["Transition Word", "Use"], [
            ["However", "Shows contrast"], ["Therefore", "Shows a result"],
        ]),
    },
    "english-g7-l19": {
        "data_table": table(["Step", "Focus"], [
            ["Editing", "Fixing grammar and word choice"], ["Proofreading", "Catching remaining small errors"],
        ]),
    },
    "english-g7-l20": {
        "data_table": table(["Strategy", "Example"], [
            ["Predicting", "Guessing what happens next using clues"], ["Questioning", "Asking about the text while reading"],
        ]),
    },
    "english-g7-l21": {
        "data_table": table(["Concept", "Meaning"], [
            ["Character development", "How a character changes over the story"],
        ]),
    },
    "english-g7-l22": {
        "data_table": table(["Plot Element", "Definition"], [
            ["Rising action", "Builds tension toward the climax"], ["Falling action", "Events after the climax"],
        ]),
    },
    "english-g7-l23": {
        "data_table": table(["Term", "Definition"], [
            ["Theme", "The underlying message or lesson of a story"],
        ]),
    },
    "english-g7-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Tone", "The author's attitude toward the subject"], ["Mood", "The feeling created for the reader"],
        ]),
    },
    "english-g7-l25": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Third person limited", "he, she, they (one character's thoughts)"],
        ]),
    },
    "english-g7-l26": {
        "data_table": table(["Text Feature", "Purpose"], [
            ["Heading", "Labels a section"], ["Glossary", "Defines key terms"],
        ]),
    },
    "english-g7-l27": {
        "data_table": table(["Skill", "Definition"], [
            ["Summarizing", "Retelling the main points briefly"], ["Note-taking", "Recording key facts for later use"],
        ]),
    },
    "english-g7-l28": {
        "data_table": table(["Skill", "Purpose"], [
            ["Source evaluation", "Judging whether a source is trustworthy"],
        ]),
    },
    "english-g7-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Citation", "Credit given to the original source"], ["Plagiarism", "Using someone's work without credit"],
        ]),
    },
    "english-g7-l30": {
        "data_table": table(["Format", "Use"], [
            ["Formal letter", "Business or official communication"], ["Email", "Quick digital correspondence"],
        ]),
    },
    "english-g7-l31": {
        "data_table": table(["Journalism Term", "Meaning"], [
            ["Headline", "A short title summarizing the story"], ["Byline", "Credits the article's author"],
        ]),
    },
    "english-g7-l32": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Eye contact", "Engages the audience"], ["Clear pace", "Helps listeners understand"],
        ]),
    },
    "english-g7-l33": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "english-g7-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"], ["Media literacy", "Ability to evaluate media critically"],
        ]),
    },
    "english-g7-l35": {
        "data_table": table(["Script Element", "Purpose"], [
            ["Stage direction", "Describes actor movement or setting"], ["Dialogue", "What characters say"],
        ]),
    },
    "english-g7-l36": {
        "data_table": table(["Myth", "Culture"], [
            ["Prometheus", "Ancient Greece"], ["Anansi", "West Africa"],
        ]),
    },
    "english-g7-l37": {
        "data_table": table(["Genre", "Definition"], [
            ["Biography", "A true account of someone else's life"], ["Autobiography", "A true account written by the subject"],
        ]),
    },
    "english-g7-l38": {
        "data_table": table(["Genre", "Feature"], [
            ["Fiction", "Invented characters and events"], ["Nonfiction", "Factual, real events"],
        ]),
    },
    "english-g7-l39": {
        "data_table": table(["Purpose", "Example"], [
            ["To persuade", "An opinion editorial"], ["To inform", "A textbook"],
        ]),
    },
    "english-g7-l40": {
        "data_table": table(["Feedback Type", "Example"], [
            ["Constructive", "'Consider adding more detail here'"], ["Positive", "'This paragraph flows really well'"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 English lessons (completing 40/40).")


if __name__ == "__main__":
    main()
