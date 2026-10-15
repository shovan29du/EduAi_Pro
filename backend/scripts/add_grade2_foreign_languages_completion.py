#!/usr/bin/env python3
"""Depth pass, Grade 2 Foreign Languages: fill in real, hand-checked
data_table content for the 18 Grade 2 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings Grade 2 Foreign
Languages to full 20/20 coverage.

Every word/phrase is a real, standard translation in the target language
-- nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fl-g2-l1": {
        "data_table": table(["English", "Arabic (transliteration)"], [
            ["Hello", "Marhaba"], ["Peace be upon you (greeting)", "As-salamu alaykum"],
        ]),
    },
    "foreign-languages-g2-l3": {
        "data_table": table(["English", "French"], [
            ["Red", "Rouge"], ["Blue", "Bleu"], ["Green", "Vert"], ["Yellow", "Jaune"],
        ]),
    },
    "foreign-languages-g2-l4": {
        "data_table": table(["English", "Bangla (transliteration)"], [
            ["Mother", "Ma"], ["Father", "Baba"],
        ]),
    },
    "foreign-languages-g2-l5": {
        "data_table": table(["Number", "Arabic (transliteration)"], [
            ["1", "wahid"], ["2", "ithnan"], ["3", "thalatha"], ["4", "arba'a"], ["5", "khamsa"],
            ["6", "sitta"], ["7", "sab'a"], ["8", "thamaniya"], ["9", "tis'a"], ["10", "'ashara"],
        ]),
    },
    "foreign-languages-g2-l6": {
        "data_table": table(["English", "Spanish"], [
            ["Monday", "Lunes"], ["Tuesday", "Martes"], ["Wednesday", "Miercoles"],
        ]),
    },
    "foreign-languages-g2-l7": {
        "data_table": table(["English", "French"], [
            ["Hello", "Bonjour"], ["Goodbye", "Au revoir"], ["Thank you", "Merci"],
        ]),
    },
    "foreign-languages-g2-l8": {
        "data_table": table(["English", "Bangla (transliteration)"], [
            ["Cat", "Beral"], ["Dog", "Kukur"],
        ]),
    },
    "foreign-languages-g2-l10": {
        "data_table": table(["English", "Arabic (transliteration)"], [
            ["Mother", "Umm"], ["Father", "Ab"],
        ]),
    },
    "foreign-languages-g2-l11": {
        "data_table": table(["English", "Spanish"], [
            ["Please", "Por favor"], ["Thank you", "Gracias"], ["You're welcome", "De nada"],
        ]),
    },
    "foreign-languages-g2-l12": {
        "data_table": table(["English", "Bangla (transliteration)"], [
            ["Red", "Lal"], ["Blue", "Nil"],
        ]),
    },
    "foreign-languages-g2-l13": {
        "data_table": table(["English", "Bangla (transliteration)"], [
            ["Hello", "Assalamu Alaikum / Nomoshkar"], ["Thank you", "Dhonnobad"],
        ]),
    },
    "foreign-languages-g2-l14": {
        "data_table": table(["Number", "French"], [
            ["1", "un"], ["2", "deux"], ["3", "trois"], ["4", "quatre"], ["5", "cinq"],
            ["6", "six"], ["7", "sept"], ["8", "huit"], ["9", "neuf"], ["10", "dix"],
        ]),
    },
    "foreign-languages-g2-l15": {
        "data_table": table(["English", "Urdu (transliteration)"], [
            ["Hello", "Assalamu Alaikum"], ["Thank you", "Shukriya"],
        ]),
    },
    "foreign-languages-g2-l16": {
        "data_table": table(["English", "Turkish"], [
            ["Hello", "Merhaba"], ["Thank you", "Tesekkur ederim"],
        ]),
    },
    "foreign-languages-g2-l17": {
        "data_table": table(["English", "Spanish"], [
            ["Mother", "Madre"], ["Father", "Padre"],
        ]),
    },
    "foreign-languages-g2-l18": {
        "data_table": table(["English", "Bangla (transliteration)"], [
            ["Monday", "Shombar"], ["Tuesday", "Mongolbar"],
        ]),
    },
    "foreign-languages-g2-l19": {
        "data_table": table(["English", "Spanish"], [
            ["Red", "Rojo"], ["Blue", "Azul"], ["Green", "Verde"],
        ]),
    },
    "foreign-languages-g2-l20": {
        "data_table": table(["English", "Arabic (transliteration)"], [
            ["Please", "Min fadlik"], ["Thank you", "Shukran"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Foreign Languages lessons (completing 20/20).")


if __name__ == "__main__":
    main()
