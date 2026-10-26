#!/usr/bin/env python3
"""Depth pass, Grade 1 Music: fill in real, hand-checked data_table
content for the 17 Grade 1 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 1 Music to full 20/20 coverage.

Content covers real musical terminology (forte/piano, allegro/adagio,
call and response) and real instrument/region facts -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g1-l1": {
        "data_table": table(["Sound Source", "Example"], [
            ["Vibrating object", "A guitar string"], ["Moving air", "Wind blowing"],
        ]),
    },
    "music-g1-l2": {
        "data_table": table(["Dynamic Term", "Meaning"], [
            ["Forte (loud)", "Play strongly"], ["Piano (soft)", "Play gently"],
        ]),
    },
    "music-g1-l3": {
        "data_table": table(["Pitch", "Example"], [
            ["High", "A bird's chirp, a flute's top notes"], ["Low", "A drum's thump, a tuba's notes"],
        ]),
    },
    "music-g1-l4": {
        "data_table": table(["Tempo Term", "Meaning"], [
            ["Allegro", "Fast"], ["Adagio", "Slow"],
        ]),
    },
    "music-g1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Beat", "The steady pulse of music"], ["Rhythm", "A pattern of sounds and silences"],
        ]),
    },
    "music-g1-l6": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Drum", "Struck"], ["Guitar", "Strings plucked"], ["Flute", "Air blown across a hole"],
        ]),
    },
    "music-g1-l7": {
        "data_table": table(["Instrument", "How Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
            ["Tambourine", "Shaken or struck"],
        ]),
    },
    "music-g1-l10": {
        "data_table": table(["Singing Skill", "Example"], [
            ["Pitch matching", "Singing the right note"], ["Breath control", "Taking breaths at the right time"],
        ]),
    },
    "music-g1-l11": {
        "data_table": table(["Nursery Rhyme", "Rhythm Feel"], [
            ["Twinkle Twinkle Little Star", "Steady, gentle beat"],
            ["Row Row Row Your Boat", "Rocking, swaying beat"],
        ]),
    },
    "music-g1-l12": {
        "data_table": table(["Instrument", "Region"], [
            ["Djembe drum", "West Africa"], ["Sitar", "India"], ["Bagpipes", "Scotland"],
        ]),
    },
    "music-g1-l13": {
        "data_table": table(["Everyday Object", "Sound It Makes"], [
            ["Pots and pans", "Drum-like beats"], ["Rubber bands on a box", "Twangy string sound"],
        ]),
    },
    "music-g1-l14": {
        "data_table": table(["Music Speed", "Movement"], [
            ["Fast music", "Quick movements like running in place"], ["Slow music", "Slow, gentle swaying"],
        ]),
    },
    "music-g1-l15": {
        "data_table": table(["Instrument", "Animal Sound It Can Imitate"], [
            ["Violin", "Bird chirping (high notes)"], ["Tuba", "Elephant or bear (low notes)"],
        ]),
    },
    "music-g1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Call", "A phrase sung by one person or group"], ["Response", "The answering phrase sung back"],
        ]),
    },
    "music-g1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Repetition", "The same musical phrase played again"],
            ["Pattern", "A repeated sequence of notes or rhythms"],
        ]),
    },
    "music-g1-l19": {
        "data_table": table(["Note Name", "Beats (in 4/4 time)"], [
            ["Whole note", "4 beats"], ["Half note", "2 beats"],
            ["Quarter note", "1 beat"], ["Eighth note", "1/2 beat"],
        ]),
    },
    "music-g1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Rest", "A symbol showing silence in music"], ["Pianissimo", "Very, very soft"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Music lessons (completing 20/20).")


if __name__ == "__main__":
    main()
