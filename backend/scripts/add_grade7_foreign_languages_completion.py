#!/usr/bin/env python3
"""Depth pass, Grade 7 Foreign Languages: fill in real, hand-checked
data_table content for the 38 Grade 7 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Foreign
Languages to full 40/40 coverage.

All vocabulary/translations/scripts are real -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g7-l1": {
        "data_table": table(["Arabic Letter", "Sound"], [
            ["Alif (ا)", "a"], ["Ba (ب)", "b"],
        ]),
    },
    "foreign-languages-g7-l2": {
        "data_table": table(["English", "Spanish"], [
            ["Hello", "Hola"], ["My name is...", "Me llamo..."],
        ]),
    },
    "foreign-languages-g7-l3": {
        "data_table": table(["English", "Spanish"], [
            ["One", "Uno"], ["Ten", "Diez"],
        ]),
    },
    "foreign-languages-g7-l5": {
        "data_table": table(["English", "Spanish"], [
            ["Mother", "Madre"], ["Father", "Padre"],
        ]),
    },
    "foreign-languages-g7-l6": {
        "data_table": table(["English", "French"], [
            ["Hello", "Bonjour"], ["Thank you", "Merci"],
        ]),
    },
    "foreign-languages-g7-l7": {
        "data_table": table(["English", "French"], [
            ["One", "Un"], ["Ten", "Dix"],
        ]),
    },
    "foreign-languages-g7-l8": {
        "data_table": table(["French Verb (Parler = to speak)", "Conjugation"], [
            ["Je parle", "I speak"], ["Tu parles", "You speak"],
        ]),
    },
    "foreign-languages-g7-l9": {
        "data_table": table(["English", "French"], [
            ["Bread", "Pain"], ["Water", "Eau"],
        ]),
    },
    "foreign-languages-g7-l10": {
        "data_table": table(["English", "German"], [
            ["Hello", "Hallo"], ["Thank you", "Danke"],
        ]),
    },
    "foreign-languages-g7-l11": {
        "data_table": table(["English", "German"], [
            ["One", "Eins"], ["Ten", "Zehn"],
        ]),
    },
    "foreign-languages-g7-l12": {
        "data_table": table(["German Article", "Gender"], [
            ["der", "Masculine"], ["die", "Feminine"], ["das", "Neuter"],
        ]),
    },
    "foreign-languages-g7-l13": {
        "data_table": table(["English", "German"], [
            ["How are you?", "Wie geht es dir?"], ["Please", "Bitte"],
        ]),
    },
    "foreign-languages-g7-l14": {
        "data_table": table(["English", "Mandarin"], [
            ["Hello", "Ni hao"], ["Thank you", "Xie xie"],
        ]),
    },
    "foreign-languages-g7-l15": {
        "data_table": table(["English", "Mandarin"], [
            ["One", "Yi"], ["Ten", "Shi"],
        ]),
    },
    "foreign-languages-g7-l16": {
        "data_table": table(["English", "Mandarin Character"], [
            ["Person", "Ren (人)"], ["Big", "Da (大)"],
        ]),
    },
    "foreign-languages-g7-l17": {
        "data_table": table(["English", "Japanese"], [
            ["Hello", "Konnichiwa"], ["Thank you", "Arigato"],
        ]),
    },
    "foreign-languages-g7-l19": {
        "data_table": table(["Katakana Character", "Sound"], [
            ["ア", "a"], ["カ", "ka"],
        ]),
    },
    "foreign-languages-g7-l20": {
        "data_table": table(["English", "Swahili"], [
            ["Hello", "Jambo"], ["Thank you", "Asante"],
        ]),
    },
    "foreign-languages-g7-l21": {
        "data_table": table(["English", "Hindi"], [
            ["Hello", "Namaste"], ["Thank you", "Dhanyavaad"],
        ]),
    },
    "foreign-languages-g7-l22": {
        "data_table": table(["English", "Urdu"], [
            ["Hello", "Assalamu alaikum"], ["Thank you", "Shukriya"],
        ]),
    },
    "foreign-languages-g7-l23": {
        "data_table": table(["Writing System", "Example Language"], [
            ["Alphabetic", "English, Spanish"], ["Logographic", "Chinese"], ["Syllabic", "Japanese kana"],
        ]),
    },
    "foreign-languages-g7-l24": {
        "data_table": table(["Language Family", "Example Languages"], [
            ["Indo-European", "English, Hindi, Spanish"], ["Sino-Tibetan", "Mandarin, Burmese"],
        ]),
    },
    "foreign-languages-g7-l25": {
        "data_table": table(["Term", "Example"], [
            ["Cognate", "'Family' (English) and 'Familia' (Spanish)"],
            ["False friend", "'Embarazada' (Spanish, means pregnant, not embarrassed)"],
        ]),
    },
    "foreign-languages-g7-l26": {
        "data_table": table(["Language", "Idiom (translated meaning)"], [
            ["French", "'Il pleut des cordes' = It's raining ropes (raining hard)"],
        ]),
    },
    "foreign-languages-g7-l27": {
        "data_table": table(["Language", "Question Formation"], [
            ["English", "Adds a question word or inverts subject/verb"], ["Japanese", "Adds the particle 'ka' at the end"],
        ]),
    },
    "foreign-languages-g7-l28": {
        "data_table": table(["Language", "Adjective Agreement Example"], [
            ["Spanish", "'chico alto' (tall boy) vs 'chica alta' (tall girl)"],
        ]),
    },
    "foreign-languages-g7-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Phoneme", "The smallest unit of sound in a language"],
        ]),
    },
    "foreign-languages-g7-l30": {
        "data_table": table(["Number", "Spanish", "French"], [
            ["1", "Uno", "Un"], ["10", "Diez", "Dix"],
        ]),
    },
    "foreign-languages-g7-l31": {
        "data_table": table(["English", "Spanish"], [
            ["Where is...?", "Donde esta...?"], ["How much does it cost?", "Cuanto cuesta?"],
        ]),
    },
    "foreign-languages-g7-l32": {
        "data_table": table(["English", "French"], [
            ["Red", "Rouge"], ["Big", "Grand"],
        ]),
    },
    "foreign-languages-g7-l33": {
        "data_table": table(["English", "Spanish"], [
            ["Monday", "Lunes"], ["What time is it?", "Que hora es?"],
        ]),
    },
    "foreign-languages-g7-l34": {
        "data_table": table(["English", "French"], [
            ["Sunny", "Ensoleille"], ["Rainy", "Pluvieux"],
        ]),
    },
    "foreign-languages-g7-l35": {
        "data_table": table(["ASL Sign", "Meaning"], [
            ["Thumbs up moved from chin outward", "Thank you"],
        ]),
    },
    "foreign-languages-g7-l36": {
        "data_table": table(["Benefit of Bilingualism", "Example"], [
            ["Cognitive flexibility", "Easier switching between tasks"], ["Cultural connection", "Access to more communities"],
        ]),
    },
    "foreign-languages-g7-l37": {
        "data_table": table(["Language", "Cultural Insight"], [
            ["Japanese", "Different levels of politeness reflect social relationships"],
        ]),
    },
    "foreign-languages-g7-l38": {
        "data_table": table(["Register", "Example"], [
            ["Formal", "'Good afternoon, how may I help you?'"], ["Informal", "'Hey, what's up?'"],
        ]),
    },
    "foreign-languages-g7-l39": {
        "data_table": table(["English", "Portuguese"], [
            ["Hello", "Ola"], ["Thank you", "Obrigado/Obrigada"],
        ]),
    },
    "foreign-languages-g7-l40": {
        "data_table": table(["English", "Italian"], [
            ["Hello", "Ciao"], ["Thank you", "Grazie"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Foreign Languages lessons (completing 40/40).")


if __name__ == "__main__":
    main()
