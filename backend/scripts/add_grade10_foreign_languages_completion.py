#!/usr/bin/env python3
"""Depth pass, Grade 10 Foreign Languages: fill in real, hand-checked
data_table content for the Grade 10 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 10 Foreign
Languages to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g10-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Debate structure", "Organizes persuasive argument in Arabic"],
        ]),
    },
    "foreign-languages-g10-l3": {
        "data_table": table(["Spanish", "English"], [
            ["Estacion", "Station / season"], ["Equipaje", "Luggage"],
        ]),
    },
    "foreign-languages-g10-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Gabriel Garcia Marquez", "Colombian author, pioneer of magical realism"],
        ]),
    },
    "foreign-languages-g10-l5": {
        "data_table": table(["Mood", "Use"], [
            ["Subjunctive", "Expresses doubt, emotion, or hypothetical situations"],
        ]),
    },
    "foreign-languages-g10-l6": {
        "data_table": table(["French", "English"], [
            ["Fromage", "Cheese"], ["Boulangerie", "Bakery"],
        ]),
    },
    "foreign-languages-g10-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Albert Camus", "French-Algerian author, wrote The Stranger"],
        ]),
    },
    "foreign-languages-g10-l8": {
        "data_table": table(["German Case", "Use"], [
            ["Nominative", "Subject of the sentence"], ["Dative", "Indirect object"],
        ]),
    },
    "foreign-languages-g10-l9": {
        "data_table": table(["German", "English"], [
            ["Guten Tag", "Good day"], ["Wie geht's?", "How are you?"],
        ]),
    },
    "foreign-languages-g10-l10": {
        "data_table": table(["Festival", "Country"], [
            ["Oktoberfest", "Germany"],
        ]),
    },
    "foreign-languages-g10-l11": {
        "data_table": table(["Tone", "Description"], [
            ["1st tone", "High and flat"], ["4th tone", "Sharp falling"],
        ]),
    },
    "foreign-languages-g10-l12": {
        "data_table": table(["Character", "Meaning"], [
            ["人", "person"], ["水", "water"],
        ]),
    },
    "foreign-languages-g10-l13": {
        "data_table": table(["Mandarin", "English"], [
            ["Ni hao", "Hello"], ["Xie xie", "Thank you"],
        ]),
    },
    "foreign-languages-g10-l14": {
        "data_table": table(["Script", "Use"], [
            ["Hiragana", "Native Japanese words and grammar"], ["Katakana", "Foreign loanwords"],
        ]),
    },
    "foreign-languages-g10-l15": {
        "data_table": table(["Rule", "Example"], [
            ["Subject-Object-Verb order", "Watashi wa ringo o tabemasu"],
        ]),
    },
    "foreign-languages-g10-l16": {
        "data_table": table(["Custom", "Meaning"], [
            ["Bowing", "A common greeting and sign of respect in Japan"],
        ]),
    },
    "foreign-languages-g10-l18": {
        "data_table": table(["Rule", "Example"], [
            ["Subject-Object-Verb order", "Common sentence structure in Korean"],
        ]),
    },
    "foreign-languages-g10-l19": {
        "data_table": table(["Italian Verb (parlare)", "Conjugation"], [
            ["io", "parlo"], ["tu", "parli"], ["lui/lei", "parla"],
        ]),
    },
    "foreign-languages-g10-l20": {
        "data_table": table(["Italian", "English"], [
            ["Arte", "Art"], ["Museo", "Museum"],
        ]),
    },
    "foreign-languages-g10-l21": {
        "data_table": table(["Portuguese Verb (falar)", "Conjugation"], [
            ["eu", "falo"], ["tu", "falas"], ["ele/ela", "fala"],
        ]),
    },
    "foreign-languages-g10-l22": {
        "data_table": table(["Portuguese", "English"], [
            ["Bom dia", "Good morning"], ["Obrigado/a", "Thank you"],
        ]),
    },
    "foreign-languages-g10-l23": {
        "data_table": table(["Cyrillic Letter", "Sound"], [
            ["А", "a"], ["Б", "b"],
        ]),
    },
    "foreign-languages-g10-l24": {
        "data_table": table(["Rule", "Note"], [
            ["Cases", "Russian nouns change form based on grammatical role"],
        ]),
    },
    "foreign-languages-g10-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Devanagari script", "Used to write Hindi"],
        ]),
    },
    "foreign-languages-g10-l26": {
        "data_table": table(["Hindi", "English"], [
            ["Namaste", "Greeting"], ["Dhanyavaad", "Thank you"],
        ]),
    },
    "foreign-languages-g10-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Urdu script", "Written right to left, based on the Perso-Arabic alphabet"],
        ]),
    },
    "foreign-languages-g10-l28": {
        "data_table": table(["Swahili", "English"], [
            ["Jambo", "Hello"], ["Asante", "Thank you"],
        ]),
    },
    "foreign-languages-g10-l29": {
        "data_table": table(["Concept", "Meaning"], [
            ["Vowel harmony", "Vowels within a Turkish word tend to match in quality"],
        ]),
    },
    "foreign-languages-g10-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Persian script", "Written right to left, related to the Arabic script"],
        ]),
    },
    "foreign-languages-g10-l31": {
        "data_table": table(["Concept", "Meaning"], [
            ["Verb forms", "Arabic verbs conjugate through derived forms from a triliteral root"],
        ]),
    },
    "foreign-languages-g10-l32": {
        "data_table": table(["Arabic", "English"], [
            ["Akhbar", "News"], ["I'lam", "Media"],
        ]),
    },
    "foreign-languages-g10-l33": {
        "data_table": table(["Language", "Family"], [
            ["Spanish, French, Italian", "Romance languages, derived from Latin"],
        ]),
    },
    "foreign-languages-g10-l34": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Spaced repetition", "Improves long-term vocabulary retention"],
        ]),
    },
    "foreign-languages-g10-l35": {
        "data_table": table(["Language", "Idiom"], [
            ["English", "'Break a leg' means good luck"],
        ]),
    },
    "foreign-languages-g10-l36": {
        "data_table": table(["Skill", "Benefit"], [
            ["Cross-cultural communication", "Reduces misunderstanding between cultures"],
        ]),
    },
    "foreign-languages-g10-l37": {
        "data_table": table(["Register", "Use"], [
            ["Formal", "Business or unfamiliar contexts"], ["Informal", "Friends and family"],
        ]),
    },
    "foreign-languages-g10-l38": {
        "data_table": table(["Challenge", "Example"], [
            ["Idiom translation", "Phrases that don't translate literally"],
        ]),
    },
    "foreign-languages-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Charles Baudelaire", "19th-century French poet, author of Les Fleurs du mal"],
        ]),
    },
    "foreign-languages-g10-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Pablo Neruda", "Chilean poet, Nobel laureate in Literature, 1971"],
        ]),
    },
    "foreign-languages-g10-l41": {
        "data_table": table(["Concept", "Meaning"], [
            ["Language and identity", "A person's language often shapes their sense of belonging"],
        ]),
    },
    "foreign-languages-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Sign language", "A visual-manual language with its own grammar"],
        ]),
    },
    "foreign-languages-g10-l43": {
        "data_table": table(["Language Family", "Example Languages"], [
            ["Indo-European", "English, Spanish, Hindi"],
        ]),
    },
    "foreign-languages-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Loanword", "A word borrowed from another language"],
        ]),
    },
    "foreign-languages-g10-l45": {
        "data_table": table(["Skill", "Example"], [
            ["Business email etiquette", "Varies by culture and formality expectations"],
        ]),
    },
    "foreign-languages-g10-l46": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Context clues", "Helps guess unfamiliar word meanings"],
        ]),
    },
    "foreign-languages-g10-l47": {
        "data_table": table(["Skill", "Benefit"], [
            ["Exposure to varied accents", "Improves real-world listening comprehension"],
        ]),
    },
    "foreign-languages-g10-l48": {
        "data_table": table(["Skill", "Example"], [
            ["Introducing yourself", "Basic conversational building block"],
        ]),
    },
    "foreign-languages-g10-l49": {
        "data_table": table(["Skill", "Example"], [
            ["Giving opinions", "Expressing agreement or disagreement politely"],
        ]),
    },
    "foreign-languages-g10-l50": {
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
        raise SystemExit(f"Lesson ids not found in grade10.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Foreign Languages lessons (completing 50/50).")


if __name__ == "__main__":
    main()
