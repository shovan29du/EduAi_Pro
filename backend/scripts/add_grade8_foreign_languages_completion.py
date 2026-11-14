#!/usr/bin/env python3
"""Depth pass, Grade 8 Foreign Languages: fill in real, hand-checked
data_table content for the 38 Grade 8 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Foreign
Languages to full 40/40 coverage.

All vocabulary/translations/scripts are real -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g8-l1": {
        "data_table": table(["Arabic Word", "Meaning"], [
            ["Maqal (مقال)", "Article/essay"],
        ]),
    },
    "foreign-languages-g8-l2": {
        "data_table": table(["Spanish Verb (Hablar = to speak)", "Conjugation"], [
            ["Yo hablo", "I speak"], ["Tu hablas", "You speak"],
        ]),
    },
    "foreign-languages-g8-l4": {
        "data_table": table(["Spanish Noun", "Gender"], [
            ["El libro", "Masculine"], ["La casa", "Feminine"],
        ]),
    },
    "foreign-languages-g8-l5": {
        "data_table": table(["English", "Spanish"], [
            ["Mother", "Madre"], ["House", "Casa"],
        ]),
    },
    "foreign-languages-g8-l6": {
        "data_table": table(["English", "Spanish"], [
            ["What?", "Que?"], ["Where?", "Donde?"],
        ]),
    },
    "foreign-languages-g8-l7": {
        "data_table": table(["French Article", "Gender"], [
            ["le", "Masculine"], ["la", "Feminine"],
        ]),
    },
    "foreign-languages-g8-l8": {
        "data_table": table(["French Verb (Parler = to speak)", "Conjugation"], [
            ["Je parle", "I speak"], ["Tu parles", "You speak"],
        ]),
    },
    "foreign-languages-g8-l9": {
        "data_table": table(["English", "French"], [
            ["One", "Un"], ["What time is it?", "Quelle heure est-il?"],
        ]),
    },
    "foreign-languages-g8-l10": {
        "data_table": table(["English", "French"], [
            ["Bread", "Pain"], ["Water", "Eau"],
        ]),
    },
    "foreign-languages-g8-l11": {
        "data_table": table(["French Adjective Rule", "Example"], [
            ["Usually follows the noun", "une maison bleue (a blue house)"],
        ]),
    },
    "foreign-languages-g8-l12": {
        "data_table": table(["German Article", "Gender"], [
            ["der", "Masculine"], ["die", "Feminine"], ["das", "Neuter"],
        ]),
    },
    "foreign-languages-g8-l13": {
        "data_table": table(["German Case", "Use"], [
            ["Nominative", "The subject of a sentence"], ["Accusative", "The direct object"],
        ]),
    },
    "foreign-languages-g8-l14": {
        "data_table": table(["German Rule", "Example"], [
            ["Verb in second position", "Ich gehe heute zur Schule"],
        ]),
    },
    "foreign-languages-g8-l15": {
        "data_table": table(["English", "German"], [
            ["School", "Schule"], ["Homework", "Hausaufgaben"],
        ]),
    },
    "foreign-languages-g8-l16": {
        "data_table": table(["German Modal Verb", "Meaning"], [
            ["Konnen", "Can/to be able to"], ["Mussen", "Must/have to"],
        ]),
    },
    "foreign-languages-g8-l17": {
        "data_table": table(["Mandarin Tone", "Description"], [
            ["1st tone", "High and flat"], ["4th tone", "Falling"],
        ]),
    },
    "foreign-languages-g8-l18": {
        "data_table": table(["Mandarin Sentence Structure", "Example"], [
            ["Subject-Verb-Object", "Wo xihuan ni (I like you)"],
        ]),
    },
    "foreign-languages-g8-l19": {
        "data_table": table(["English", "Mandarin"], [
            ["One", "Yi"], ["Ten", "Shi"],
        ]),
    },
    "foreign-languages-g8-l20": {
        "data_table": table(["English", "Mandarin"], [
            ["Hello", "Ni hao"], ["Thank you", "Xie xie"],
        ]),
    },
    "foreign-languages-g8-l21": {
        "data_table": table(["Radical", "Meaning"], [
            ["Ren (人)", "Person"], ["Shui (水)", "Water"],
        ]),
    },
    "foreign-languages-g8-l22": {
        "data_table": table(["Script", "Use"], [
            ["Hiragana", "Native Japanese words"], ["Katakana", "Foreign loanwords"],
        ]),
    },
    "foreign-languages-g8-l23": {
        "data_table": table(["Particle", "Function"], [
            ["Wa (は)", "Marks the topic of a sentence"], ["Ka (か)", "Marks a question"],
        ]),
    },
    "foreign-languages-g8-l24": {
        "data_table": table(["Verb Form", "Example"], [
            ["Polite form", "Tabemasu (to eat, polite)"],
        ]),
    },
    "foreign-languages-g8-l25": {
        "data_table": table(["English", "Japanese"], [
            ["One", "Ichi"], ["Ten", "Ju"],
        ]),
    },
    "foreign-languages-g8-l26": {
        "data_table": table(["Italian Article", "Gender"], [
            ["il", "Masculine"], ["la", "Feminine"],
        ]),
    },
    "foreign-languages-g8-l27": {
        "data_table": table(["Italian Verb (Parlare = to speak)", "Conjugation"], [
            ["Io parlo", "I speak"], ["Tu parli", "You speak"],
        ]),
    },
    "foreign-languages-g8-l28": {
        "data_table": table(["English", "Italian"], [
            ["Where is...?", "Dove e...?"], ["Left", "Sinistra"],
        ]),
    },
    "foreign-languages-g8-l29": {
        "data_table": table(["Cyrillic Letter", "Sound"], [
            ["А", "a"], ["Б", "b"],
        ]),
    },
    "foreign-languages-g8-l30": {
        "data_table": table(["Russian Case", "Use"], [
            ["Nominative", "The subject of a sentence"], ["Accusative", "The direct object"],
        ]),
    },
    "foreign-languages-g8-l31": {
        "data_table": table(["English", "Russian"], [
            ["Hello", "Zdravstvuyte"], ["One", "Odin"],
        ]),
    },
    "foreign-languages-g8-l32": {
        "data_table": table(["Portuguese Article", "Gender"], [
            ["o", "Masculine"], ["a", "Feminine"],
        ]),
    },
    "foreign-languages-g8-l33": {
        "data_table": table(["Portuguese Verb (Falar = to speak)", "Conjugation"], [
            ["Eu falo", "I speak"], ["Tu falas", "You speak"],
        ]),
    },
    "foreign-languages-g8-l34": {
        "data_table": table(["English", "Portuguese"], [
            ["Sunny", "Ensolarado"], ["Winter", "Inverno"],
        ]),
    },
    "foreign-languages-g8-l35": {
        "data_table": table(["Hangul Character", "Sound"], [
            ["ㄱ", "g/k"], ["ㅏ", "a"],
        ]),
    },
    "foreign-languages-g8-l36": {
        "data_table": table(["Korean Sentence Structure", "Example"], [
            ["Subject-Object-Verb", "Jeo-neun sagwa-reul meogeoyo (I eat an apple)"],
        ]),
    },
    "foreign-languages-g8-l37": {
        "data_table": table(["Honorific Level", "Use"], [
            ["Formal", "Used with strangers or elders"], ["Informal", "Used with close friends"],
        ]),
    },
    "foreign-languages-g8-l38": {
        "data_table": table(["Devanagari Letter", "Sound"], [
            ["अ", "a"], ["आ", "aa"],
        ]),
    },
    "foreign-languages-g8-l39": {
        "data_table": table(["Hindi Postposition", "Function"], [
            ["Mein", "In"], ["Ka/Ki/Ke", "Possessive marker (gender-agreeing)"],
        ]),
    },
    "foreign-languages-g8-l40": {
        "data_table": table(["English", "Hindi"], [
            ["Hello", "Namaste"], ["Mother", "Maa"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Foreign Languages lessons (completing 40/40).")


if __name__ == "__main__":
    main()
