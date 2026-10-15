#!/usr/bin/env python3
"""Depth pass, Grade 8 English: fill in real, hand-checked data_table
content for the 38 Grade 8 English lessons not covered by the earlier
breadth-first batch. Brings Grade 8 English to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g8-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Analysis", "Breaking down a text's meaning and structure"], ["Evaluation", "Judging a text's effectiveness"],
        ]),
    },
    "english-g8-l2": {
        "data_table": table(["Voice", "Example"], [
            ["Active", "The dog chased the ball."], ["Passive", "The ball was chased by the dog."],
        ]),
    },
    "english-g8-l4": {
        "data_table": table(["Part of Speech", "Example"], [
            ["Noun", "book, city"], ["Verb", "run, think"], ["Adjective", "bright, tall"],
        ]),
    },
    "english-g8-l5": {
        "data_table": table(["Term", "Example"], [
            ["Clause", "A group of words with a subject and verb"],
            ["Phrase", "A group of words without a subject and verb"],
        ]),
    },
    "english-g8-l6": {
        "data_table": table(["Punctuation", "Common Error"], [
            ["Apostrophe", "'its' vs 'it's'"], ["Comma splice", "Joining two sentences with only a comma"],
        ]),
    },
    "english-g8-l7": {
        "data_table": table(["Word", "Synonym", "Antonym"], [
            ["Happy", "Joyful", "Sad"],
        ]),
    },
    "english-g8-l8": {
        "data_table": table(["Idiom", "Meaning"], [
            ["Break the ice", "Start a conversation"], ["Piece of cake", "Something very easy"],
        ]),
    },
    "english-g8-l10": {
        "data_table": table(["Poetic Element", "Meaning"], [
            ["Rhyme", "Words that end with the same sound"], ["Meter", "The rhythmic pattern of a poem"],
        ]),
    },
    "english-g8-l11": {
        "data_table": table(["Technique", "Effect"], [
            ["Flashback", "Shows an earlier event"], ["Foreshadowing", "Hints at what's to come"],
        ]),
    },
    "english-g8-l12": {
        "data_table": table(["Sensory Detail", "Example"], [
            ["Sight", "The bright red apple"], ["Sound", "The crackling fire"],
        ]),
    },
    "english-g8-l13": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeals to credibility"], ["Pathos", "Appeals to emotion"], ["Logos", "Appeals to logic"],
        ]),
    },
    "english-g8-l14": {
        "data_table": table(["Essay Part", "Purpose"], [
            ["Thesis statement", "States the main argument"], ["Supporting paragraph", "Provides evidence"],
        ]),
    },
    "english-g8-l15": {
        "data_table": table(["Letter Part", "Purpose"], [
            ["Formal greeting", "Dear Sir/Madam,"], ["Formal closing", "Sincerely,"],
        ]),
    },
    "english-g8-l16": {
        "data_table": table(["Format", "Use"], [
            ["Informal letter", "Personal correspondence"], ["Email", "Quick digital correspondence"],
        ]),
    },
    "english-g8-l17": {
        "data_table": table(["Report Section", "Purpose"], [
            ["Introduction", "States the topic"], ["Findings", "Presents the researched information"],
        ]),
    },
    "english-g8-l18": {
        "data_table": table(["Skill", "Definition"], [
            ["Note-making", "Recording key facts for later use"], ["Summarizing", "Retelling the main points briefly"],
        ]),
    },
    "english-g8-l19": {
        "data_table": table(["Strategy", "Example"], [
            ["Predicting", "Guessing what happens next using clues"], ["Questioning", "Asking about the text while reading"],
        ]),
    },
    "english-g8-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Playwright", "William Shakespeare"], ["Country", "England"],
        ]),
    },
    "english-g8-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Novel", "A long fictional narrative"],
        ]),
    },
    "english-g8-l22": {
        "data_table": table(["Story Element", "Definition"], [
            ["Character", "Who the story is about"], ["Setting", "Where and when it happens"], ["Plot", "The events"],
        ]),
    },
    "english-g8-l23": {
        "data_table": table(["Script Element", "Purpose"], [
            ["Stage direction", "Describes actor movement or setting"], ["Dialogue", "What characters say"],
        ]),
    },
    "english-g8-l24": {
        "data_table": table(["Skill", "Why It Matters"], [
            ["Eye contact", "Engages the audience"], ["Clear pace", "Helps listeners understand"],
        ]),
    },
    "english-g8-l25": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "english-g8-l26": {
        "data_table": table(["Journalism Term", "Meaning"], [
            ["Headline", "A short title summarizing the story"], ["Byline", "Credits the article's author"],
        ]),
    },
    "english-g8-l27": {
        "data_table": table(["Concept", "Meaning"], [
            ["Character development", "How a character changes over the story"],
        ]),
    },
    "english-g8-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Theme", "The underlying message or lesson of a story"], ["Symbolism", "An object representing a larger idea"],
        ]),
    },
    "english-g8-l29": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Third person", "he, she, they"],
        ]),
    },
    "english-g8-l30": {
        "data_table": table(["Comparison Type", "Example"], [
            ["Theme comparison", "Comparing themes of courage across two stories"],
        ]),
    },
    "english-g8-l31": {
        "data_table": table(["Plot Element", "Definition"], [
            ["Rising action", "Builds tension toward the climax"], ["Climax", "The turning point of the story"],
        ]),
    },
    "english-g8-l32": {
        "data_table": table(["Rule", "Example"], [
            ["Use quotation marks", "\"Let's go,\" she said."],
        ]),
    },
    "english-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Citation", "Credit given to the original source"], ["Plagiarism", "Using someone's work without credit"],
        ]),
    },
    "english-g8-l34": {
        "data_table": table(["Advertising Technique", "Example"], [
            ["Bandwagon", "'Everyone is doing it, so you should too'"],
        ]),
    },
    "english-g8-l35": {
        "data_table": table(["Pattern", "Example"], [
            ["ie vs ei", "believe, receive"],
        ]),
    },
    "english-g8-l36": {
        "data_table": table(["Modal Verb", "Use"], [
            ["Must", "Expresses obligation"], ["Might", "Expresses possibility"],
        ]),
    },
    "english-g8-l37": {
        "data_table": table(["Tense", "Example"], [
            ["Present perfect", "She has finished"], ["Past perfect", "She had finished"],
        ]),
    },
    "english-g8-l38": {
        "data_table": table(["Type", "Example", "Meaning Change"], [
            ["Prefix", "re + write = rewrite", "Write again"],
        ]),
    },
    "english-g8-l39": {
        "data_table": table(["Purpose", "Example"], [
            ["To persuade", "An opinion editorial"], ["To inform", "A textbook"],
        ]),
    },
    "english-g8-l40": {
        "data_table": table(["Genre", "Definition"], [
            ["Biography", "A true account of someone else's life"], ["Autobiography", "A true account written by the subject"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 English lessons (completing 40/40).")


if __name__ == "__main__":
    main()
