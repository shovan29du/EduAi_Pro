#!/usr/bin/env python3
"""Depth pass, Grade 4 Foreign Languages: fill in real, hand-checked
data_table content for the 28 Grade 4 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 4 Foreign
Languages to full 30/30 coverage.

All vocabulary/translations are real -- nothing fabricated or presented
as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g4-l1": {
        "data_table": table(["English", "Arabic"], [
            ["House", "Bayt"], ["Family", "'A'ila"],
        ]),
    },
    "foreign-languages-g4-l2": {
        "data_table": table(["English", "Spanish"], [
            ["Hello", "Hola"], ["My name is...", "Me llamo..."],
        ]),
    },
    "foreign-languages-g4-l4": {
        "data_table": table(["English", "Mandarin"], [
            ["Red", "Hong"], ["Square", "Zheng fang xing"],
        ]),
    },
    "foreign-languages-g4-l5": {
        "data_table": table(["English", "German"], [
            ["Monday", "Montag"], ["Tuesday", "Dienstag"], ["Wednesday", "Mittwoch"],
        ]),
    },
    "foreign-languages-g4-l6": {
        "data_table": table(["English", "Spanish"], [
            ["Dog", "Perro"], ["Cat", "Gato"], ["Bird", "Pajaro"],
        ]),
    },
    "foreign-languages-g4-l7": {
        "data_table": table(["English", "Japanese"], [
            ["Hello", "Konnichiwa"], ["Thank you", "Arigato"],
        ]),
    },
    "foreign-languages-g4-l8": {
        "data_table": table(["English", "French"], [
            ["Bread", "Pain"], ["Water", "Eau"],
        ]),
    },
    "foreign-languages-g4-l9": {
        "data_table": table(["English", "Urdu"], [
            ["Mother", "Ammi"], ["Father", "Abbu"], ["Sister", "Baji"],
        ]),
    },
    "foreign-languages-g4-l10": {
        "data_table": table(["English", "Swahili"], [
            ["Hello", "Jambo"], ["Thank you", "Asante"],
        ]),
    },
    "foreign-languages-g4-l11": {
        "data_table": table(["English", "Spanish"], [
            ["Sunny", "Soleado"], ["Rainy", "Lluvioso"],
        ]),
    },
    "foreign-languages-g4-l13": {
        "data_table": table(["English", "Hindi"], [
            ["Hello", "Namaste"], ["Thank you", "Dhanyavaad"],
        ]),
    },
    "foreign-languages-g4-l14": {
        "data_table": table(["English", "French"], [
            ["Red", "Rouge"], ["Blue", "Bleu"], ["Yellow", "Jaune"],
        ]),
    },
    "foreign-languages-g4-l15": {
        "data_table": table(["English", "Spanish"], [
            ["School", "Escuela"], ["Teacher", "Maestro/Maestra"],
        ]),
    },
    "foreign-languages-g4-l16": {
        "data_table": table(["English", "Turkish"], [
            ["Hello", "Merhaba"], ["Thank you", "Tesekkur ederim"],
        ]),
    },
    "foreign-languages-g4-l17": {
        "data_table": table(["English", "French"], [
            ["Head", "Tete"], ["Hand", "Main"],
        ]),
    },
    "foreign-languages-g4-l18": {
        "data_table": table(["English", "Bengali"], [
            ["Hello", "Assalamu alaikum"], ["Thank you", "Dhonnobad"],
        ]),
    },
    "foreign-languages-g4-l19": {
        "data_table": table(["English", "German"], [
            ["Dog", "Hund"], ["Cat", "Katze"],
        ]),
    },
    "foreign-languages-g4-l20": {
        "data_table": table(["English", "Spanish"], [
            ["How are you?", "Como estas?"], ["I am well", "Estoy bien"],
        ]),
    },
    "foreign-languages-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Introducing family", "Describing home and family members in Arabic"],
        ]),
    },
    "foreign-languages-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Meeting someone new", "Greeting them in Spanish"],
        ]),
    },
    "foreign-languages-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Counting objects", "Counting to 20 in French"],
        ]),
    },
    "foreign-languages-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Describing an object", "Naming its color and shape in Mandarin"],
        ]),
    },
    "foreign-languages-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Making plans", "Naming the day of the week in German"],
        ]),
    },
    "foreign-languages-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Talking about pets", "Naming animals in Spanish"],
        ]),
    },
    "foreign-languages-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Traveling", "Using basic greetings in Japanese"],
        ]),
    },
    "foreign-languages-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Ordering food", "Naming foods in French"],
        ]),
    },
    "foreign-languages-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Talking about family", "Naming relatives in Urdu"],
        ]),
    },
    "foreign-languages-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Traveling", "Greeting people in Swahili"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Foreign Languages lessons (completing 30/30).")


if __name__ == "__main__":
    main()
