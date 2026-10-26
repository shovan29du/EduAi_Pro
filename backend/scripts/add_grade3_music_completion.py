#!/usr/bin/env python3
"""Depth pass, Grade 3 Music: fill in real, hand-checked data_table
content for the 18 Grade 3 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Music to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "music-g3-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of long and short sounds"], ["Beat", "The steady pulse of music"],
        ]),
    },
    "music-g3-l3": {
        "data_table": table(["Pitch", "Example"], [
            ["High pitch", "A bird's chirp"], ["Low pitch", "A tuba's note"],
        ]),
    },
    "music-g3-l4": {
        "data_table": table(["Dynamic Term", "Meaning"], [
            ["Forte", "Play loudly"], ["Piano", "Play softly"],
        ]),
    },
    "music-g3-l5": {
        "data_table": table(["Tempo Term", "Meaning"], [
            ["Allegro", "Fast"], ["Adagio", "Slow"],
        ]),
    },
    "music-g3-l6": {
        "data_table": table(["Instrument Family", "Example"], [
            ["String", "Violin"], ["Wind", "Flute"], ["Percussion", "Drum"],
        ]),
    },
    "music-g3-l7": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
        ]),
    },
    "music-g3-l8": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Violin", "Bowed or plucked strings"], ["Guitar", "Plucked or strummed strings"],
        ]),
    },
    "music-g3-l9": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Trumpet", "Brass"],
        ]),
    },
    "music-g3-l10": {
        "data_table": table(["Vocal Skill", "Description"], [
            ["Breath control", "Managing air while singing"], ["Pitch matching", "Singing the correct note"],
        ]),
    },
    "music-g3-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Recorder type", "Woodwind instrument"], ["How it's played", "Blowing air through a mouthpiece"],
        ]),
    },
    "music-g3-l12": {
        "data_table": table(["Note Value", "Beats"], [
            ["Whole note", "4 beats"], ["Half note", "2 beats"], ["Quarter note", "1 beat"],
        ]),
    },
    "music-g3-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes forming a tune"], ["Harmony", "Notes played together"],
        ]),
    },
    "music-g3-l14": {
        "data_table": table(["Song", "Country of Origin"], [
            ["Frere Jacques", "France"], ["Sakura Sakura", "Japan"],
        ]),
    },
    "music-g3-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Call and response", "A leader sings a phrase and others answer"],
        ]),
    },
    "music-g3-l16": {
        "data_table": table(["Composer", "Known For"], [
            ["Wolfgang Amadeus Mozart", "Classical era symphonies and operas"],
            ["Ludwig van Beethoven", "Symphonies, including the Ninth"],
        ]),
    },
    "music-g3-l17": {
        "data_table": table(["Body Percussion", "Sound"], [
            ["Clap", "Hands together"], ["Stomp", "Foot on the ground"],
        ]),
    },
    "music-g3-l19": {
        "data_table": table(["Listening Skill", "Purpose"], [
            ["Identifying tempo", "Notice if music is fast or slow"],
            ["Identifying mood", "Notice if music feels happy or sad"],
        ]),
    },
    "music-g3-l20": {
        "data_table": table(["Performance Element", "Purpose"], [
            ["Staying in time", "Keeps the group together"], ["Listening to others", "Helps the group sound unified"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Music lessons (completing 20/20).")


if __name__ == "__main__":
    main()
