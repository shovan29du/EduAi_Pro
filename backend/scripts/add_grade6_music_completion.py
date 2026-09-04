#!/usr/bin/env python3
"""Depth pass, Grade 6 Music: fill in real, hand-checked data_table
content for the 28 Grade 6 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Music to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g6-l1": {
        "data_table": table(["Tradition", "Region"], [
            ["Flamenco", "Spain"], ["Gamelan", "Indonesia"],
        ]),
    },
    "music-g6-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of long and short sounds"], ["Beat", "The steady pulse of music"],
        ]),
    },
    "music-g6-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes forming a tune"], ["Harmony", "Notes played together"],
        ]),
    },
    "music-g6-l4": {
        "data_table": table(["Note Value", "Beats"], [
            ["Whole note", "4 beats"], ["Quarter note", "1 beat"],
        ]),
    },
    "music-g6-l5": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Violin", "Bowed or plucked strings"], ["Cello", "Bowed strings, larger and lower-pitched"],
        ]),
    },
    "music-g6-l6": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Clarinet", "Woodwind"],
        ]),
    },
    "music-g6-l7": {
        "data_table": table(["Instrument", "Family"], [
            ["Trumpet", "Brass"], ["Trombone", "Brass"],
        ]),
    },
    "music-g6-l8": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
        ]),
    },
    "music-g6-l9": {
        "data_table": table(["Voice Type", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-g6-l10": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"],
        ]),
    },
    "music-g6-l12": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Romantic", "1820-1900"],
        ]),
    },
    "music-g6-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["The Blues", "Originated among African Americans in the American South"],
        ]),
    },
    "music-g6-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Rock and roll emerged", "1950s in the United States"],
        ]),
    },
    "music-g6-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Hip-hop originated", "1970s, in the Bronx, New York"],
        ]),
    },
    "music-g6-l17": {
        "data_table": table(["Folk Tradition", "Region"], [
            ["Bluegrass", "Appalachian United States"],
        ]),
    },
    "music-g6-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Raga", "A melodic framework in Indian classical music"],
        ]),
    },
    "music-g6-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Djembe", "A West African hand drum"],
        ]),
    },
    "music-g6-l20": {
        "data_table": table(["Rhythm Style", "Region"], [
            ["Samba", "Brazil"], ["Salsa", "Cuba/Latin America"],
        ]),
    },
    "music-g6-l21": {
        "data_table": table(["Step", "Purpose"], [
            ["Choose a scale", "Sets the notes to use"], ["Arrange notes into a pattern", "Creates the melody"],
        ]),
    },
    "music-g6-l22": {
        "data_table": table(["Dynamic Term", "Meaning"], [
            ["Forte", "Play loudly"], ["Piano", "Play softly"],
        ]),
    },
    "music-g6-l23": {
        "data_table": table(["Note Value", "Beats"], [
            ["Half note", "2 beats"], ["Eighth note", "1/2 beat"],
        ]),
    },
    "music-g6-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Recorder", "Woodwind instrument played by blowing through a mouthpiece"],
        ]),
    },
    "music-g6-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Piano keys", "88 total on a full-size piano"],
        ]),
    },
    "music-g6-l26": {
        "data_table": table(["Guitar String", "Note"], [
            ["Thickest string", "E"], ["Thinnest string", "E (higher octave)"],
        ]),
    },
    "music-g6-l27": {
        "data_table": table(["Vocal Skill", "Description"], [
            ["Breath control", "Managing air while singing"], ["Pitch matching", "Singing the correct note"],
        ]),
    },
    "music-g6-l28": {
        "data_table": table(["Musical Element", "Emotional Effect"], [
            ["Minor key", "Often sounds sad or mysterious"], ["Fast tempo", "Often sounds exciting"],
        ]),
    },
    "music-g6-l29": {
        "data_table": table(["Technology", "Use"], [
            ["Digital audio workstation", "Recording and editing music"],
        ]),
    },
    "music-g6-l30": {
        "data_table": table(["Composer", "Known For"], [
            ["Wolfgang Amadeus Mozart", "Classical era symphonies and operas"],
            ["Ludwig van Beethoven", "Symphonies, including the Ninth"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Music lessons (completing 30/30).")


if __name__ == "__main__":
    main()
