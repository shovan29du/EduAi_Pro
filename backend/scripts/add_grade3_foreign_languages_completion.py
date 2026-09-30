#!/usr/bin/env python3
"""Depth pass, Grade 3 Foreign Languages: fill in real, hand-checked
data_table content for the 18 Grade 3 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 3 Foreign
Languages to full 20/20 coverage.

All vocabulary/translations are real -- nothing fabricated or presented
as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g3-l1": {
        "data_table": table(["English", "Arabic"], [
            ["Red", "Ahmar"], ["Cat", "Qitta"], ["Dog", "Kalb"],
        ]),
    },
    "foreign-languages-g3-l2": {
        "data_table": table(["English", "Spanish"], [
            ["Hello", "Hola"], ["Goodbye", "Adios"], ["Please", "Por favor"],
        ]),
    },
    "foreign-languages-g3-l4": {
        "data_table": table(["English", "Spanish"], [
            ["Mother", "Madre"], ["Father", "Padre"], ["Sister", "Hermana"], ["Brother", "Hermano"],
        ]),
    },
    "foreign-languages-g3-l5": {
        "data_table": table(["English", "French"], [
            ["Monday", "Lundi"], ["Tuesday", "Mardi"], ["Wednesday", "Mercredi"],
        ]),
    },
    "foreign-languages-g3-l6": {
        "data_table": table(["English", "Mandarin"], [
            ["Red", "Hong"], ["Cat", "Mao"], ["Dog", "Gou"],
        ]),
    },
    "foreign-languages-g3-l7": {
        "data_table": table(["English", "Mandarin"], [
            ["Hello", "Ni hao"], ["Thank you", "Xie xie"],
        ]),
    },
    "foreign-languages-g3-l9": {
        "data_table": table(["English", "German"], [
            ["Hello", "Hallo"], ["Thank you", "Danke"], ["Please", "Bitte"],
        ]),
    },
    "foreign-languages-g3-l10": {
        "data_table": table(["English", "Arabic"], [
            ["Mother", "Umm"], ["Father", "Ab"], ["Sister", "Ukht"], ["Brother", "Akh"],
        ]),
    },
    "foreign-languages-g3-l11": {
        "data_table": table(["English", "French"], [
            ["Hello", "Bonjour"], ["Goodbye", "Au revoir"], ["Thank you", "Merci"],
        ]),
    },
    "foreign-languages-g3-l12": {
        "data_table": table(["English", "Arabic"], [
            ["One", "Wahid"], ["Two", "Ithnan"], ["Three", "Thalatha"], ["Four", "Arba'a"], ["Five", "Khamsa"],
        ]),
    },
    "foreign-languages-g3-l13": {
        "data_table": table(["English", "Spanish"], [
            ["Red", "Rojo"], ["Cat", "Gato"], ["Dog", "Perro"],
        ]),
    },
    "foreign-languages-g3-l14": {
        "data_table": table(["English", "Urdu"], [
            ["Hello", "Assalamu alaikum"], ["Thank you", "Shukriya"],
        ]),
    },
    "foreign-languages-g3-l15": {
        "data_table": table(["English", "Spanish"], [
            ["Monday", "Lunes"], ["Tuesday", "Martes"], ["Wednesday", "Miercoles"],
        ]),
    },
    "foreign-languages-g3-l16": {
        "data_table": table(["English", "Urdu"], [
            ["Goodbye", "Khuda Hafiz"], ["Please", "Meharbani"],
        ]),
    },
    "foreign-languages-g3-l17": {
        "data_table": table(["English", "Mandarin"], [
            ["One", "Yi"], ["Two", "Er"], ["Three", "San"], ["Four", "Si"], ["Five", "Wu"],
        ]),
    },
    "foreign-languages-g3-l18": {
        "data_table": table(["English", "Turkish"], [
            ["Hello", "Merhaba"], ["Thank you", "Tesekkur ederim"],
        ]),
    },
    "foreign-languages-g3-l19": {
        "data_table": table(["English", "French"], [
            ["Red", "Rouge"], ["Cat", "Chat"], ["Dog", "Chien"],
        ]),
    },
    "foreign-languages-g3-l20": {
        "data_table": table(["English", "French"], [
            ["Mother", "Mere"], ["Father", "Pere"], ["Sister", "Soeur"], ["Brother", "Frere"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Foreign Languages lessons (completing 20/20).")


if __name__ == "__main__":
    main()
