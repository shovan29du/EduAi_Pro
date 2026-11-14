#!/usr/bin/env python3
"""Depth pass, Grade 9 Foreign Languages: fill in real, hand-checked
data_table content for the 48 Grade 9 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Foreign
Languages to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g9-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Arabic literature", "Includes classical poetry and the Maqama prose tradition"],
        ]),
    },
    "foreign-languages-g9-l2": {
        "data_table": table(["Spanish Verb (hablar)", "Conjugation"], [
            ["yo", "hablo"], ["tu", "hablas"], ["el/ella", "habla"],
        ]),
    },
    "foreign-languages-g9-l4": {
        "data_table": table(["Spanish", "English"], [
            ["Buenos dias", "Good morning"], ["Como estas?", "How are you?"],
        ]),
    },
    "foreign-languages-g9-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Miguel de Cervantes"], ["Famous work", "Don Quixote"],
        ]),
    },
    "foreign-languages-g9-l6": {
        "data_table": table(["French Article", "Gender"], [
            ["le", "Masculine"], ["la", "Feminine"],
        ]),
    },
    "foreign-languages-g9-l7": {
        "data_table": table(["French Verb (parler)", "Conjugation"], [
            ["je", "parle"], ["tu", "parles"], ["il/elle", "parle"],
        ]),
    },
    "foreign-languages-g9-l8": {
        "data_table": table(["French", "English"], [
            ["Bonjour", "Hello"], ["Merci", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Moliere", "17th-century French playwright known for comedies"],
        ]),
    },
    "foreign-languages-g9-l10": {
        "data_table": table(["German Case", "Use"], [
            ["Nominative", "Subject of the sentence"], ["Accusative", "Direct object"],
        ]),
    },
    "foreign-languages-g9-l11": {
        "data_table": table(["Rule", "Example"], [
            ["Verb-second word order", "The conjugated verb is the second element in a main clause"],
        ]),
    },
    "foreign-languages-g9-l12": {
        "data_table": table(["German", "English"], [
            ["Guten Tag", "Good day"], ["Danke", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Goethe", "German writer, author of Faust"],
        ]),
    },
    "foreign-languages-g9-l14": {
        "data_table": table(["Tone", "Description"], [
            ["1st tone", "High and flat"], ["4th tone", "Sharp falling"],
        ]),
    },
    "foreign-languages-g9-l15": {
        "data_table": table(["Character", "Meaning"], [
            ["人", "person"], ["水", "water"],
        ]),
    },
    "foreign-languages-g9-l16": {
        "data_table": table(["Mandarin", "English"], [
            ["Ni hao", "Hello"], ["Xie xie", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l17": {
        "data_table": table(["Script", "Use"], [
            ["Hiragana", "Native Japanese words and grammar"], ["Katakana", "Foreign loanwords"],
        ]),
    },
    "foreign-languages-g9-l18": {
        "data_table": table(["Rule", "Example"], [
            ["Subject-Object-Verb order", "Watashi wa ringo o tabemasu (I apple eat)"],
        ]),
    },
    "foreign-languages-g9-l19": {
        "data_table": table(["Japanese", "English"], [
            ["Konnichiwa", "Hello"], ["Arigatou", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l21": {
        "data_table": table(["Rule", "Example"], [
            ["Subject-Object-Verb order", "Common sentence structure in Korean"],
        ]),
    },
    "foreign-languages-g9-l22": {
        "data_table": table(["Italian Verb (parlare)", "Conjugation"], [
            ["io", "parlo"], ["tu", "parli"], ["lui/lei", "parla"],
        ]),
    },
    "foreign-languages-g9-l23": {
        "data_table": table(["Italian", "English"], [
            ["Buongiorno", "Good morning"], ["Grazie", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Dante Alighieri", "Author of the Divine Comedy"],
        ]),
    },
    "foreign-languages-g9-l25": {
        "data_table": table(["Portuguese Verb (falar)", "Conjugation"], [
            ["eu", "falo"], ["tu", "falas"], ["ele/ela", "fala"],
        ]),
    },
    "foreign-languages-g9-l26": {
        "data_table": table(["Portuguese", "English"], [
            ["Bom dia", "Good morning"], ["Obrigado/a", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l27": {
        "data_table": table(["Cyrillic Letter", "Sound"], [
            ["А", "a"], ["Б", "b"],
        ]),
    },
    "foreign-languages-g9-l28": {
        "data_table": table(["Rule", "Note"], [
            ["Cases", "Russian nouns change form based on grammatical role"],
        ]),
    },
    "foreign-languages-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Devanagari script", "Used to write Hindi"],
        ]),
    },
    "foreign-languages-g9-l30": {
        "data_table": table(["Hindi", "English"], [
            ["Namaste", "Greeting"], ["Dhanyavaad", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l31": {
        "data_table": table(["Swahili", "English"], [
            ["Jambo", "Hello"], ["Asante", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l32": {
        "data_table": table(["Concept", "Meaning"], [
            ["Root letters", "Most Arabic words derive from a three-letter root"],
        ]),
    },
    "foreign-languages-g9-l33": {
        "data_table": table(["Arabic", "English"], [
            ["Marhaba", "Hello"], ["Shukran", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l34": {
        "data_table": table(["Script Direction", "Detail"], [
            ["Arabic script", "Written right to left"],
        ]),
    },
    "foreign-languages-g9-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Turkish alphabet", "Latin-based since 1928"],
        ]),
    },
    "foreign-languages-g9-l36": {
        "data_table": table(["Turkish", "English"], [
            ["Merhaba", "Hello"], ["Tesekkur ederim", "Thank you"],
        ]),
    },
    "foreign-languages-g9-l37": {
        "data_table": table(["Language Family", "Example Languages"], [
            ["Indo-European", "English, Spanish, Hindi"], ["Sino-Tibetan", "Mandarin"],
        ]),
    },
    "foreign-languages-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Cognate", "Words in different languages with a shared origin"], ["False friend", "Words that look similar but differ in meaning"],
        ]),
    },
    "foreign-languages-g9-l39": {
        "data_table": table(["Language", "Idiom"], [
            ["English", "'Break a leg' means good luck"],
        ]),
    },
    "foreign-languages-g9-l40": {
        "data_table": table(["Tense", "Example Across Languages"], [
            ["Past tense", "Marked differently in each language's grammar"],
        ]),
    },
    "foreign-languages-g9-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Sign language", "A visual-manual language with its own grammar"],
        ]),
    },
    "foreign-languages-g9-l42": {
        "data_table": table(["Latin Root", "Example Word"], [
            ["'aqua' (water)", "Aquarium"],
        ]),
    },
    "foreign-languages-g9-l43": {
        "data_table": table(["Greek Root", "Example Word"], [
            ["'bio' (life)", "Biology"],
        ]),
    },
    "foreign-languages-g9-l44": {
        "data_table": table(["Practice", "Reason"], [
            ["Learning greetings and customs", "Shows respect in a new culture"],
        ]),
    },
    "foreign-languages-g9-l45": {
        "data_table": table(["Skill", "Example"], [
            ["Introducing yourself", "Basic conversational building block"],
        ]),
    },
    "foreign-languages-g9-l46": {
        "data_table": table(["Skill", "Example"], [
            ["Asking for directions", "Practical travel phrase"],
        ]),
    },
    "foreign-languages-g9-l47": {
        "data_table": table(["Skill", "Example"], [
            ["Ordering food", "Practical dining phrase"],
        ]),
    },
    "foreign-languages-g9-l48": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Context clues", "Helps guess unfamiliar word meanings"],
        ]),
    },
    "foreign-languages-g9-l49": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Outlining before writing", "Organizes ideas in the target language"],
        ]),
    },
    "foreign-languages-g9-l50": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Immersion", "Accelerates fluency through constant exposure"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Foreign Languages lessons (completing 50/50).")


if __name__ == "__main__":
    main()
