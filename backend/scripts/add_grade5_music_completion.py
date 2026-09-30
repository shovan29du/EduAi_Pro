#!/usr/bin/env python3
"""Depth pass, Grade 5 Music: fill in real, hand-checked data_table
content for the 28 Grade 5 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 5 Music to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g5-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Harmony", "Notes played together"], ["Chord", "Three or more notes played at once"],
        ]),
    },
    "music-g5-l2": {
        "data_table": table(["Note Value", "Beats"], [
            ["Whole note", "4 beats"], ["Quarter note", "1 beat"], ["Eighth note", "1/2 beat"],
        ]),
    },
    "music-g5-l3": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Treble clef", "Indicates higher-pitched notes"], ["Staff", "The five lines music is written on"],
        ]),
    },
    "music-g5-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes forming a tune"], ["Pitch", "How high or low a note is"],
        ]),
    },
    "music-g5-l6": {
        "data_table": table(["Scale", "Notes (C Major)"], [
            ["C Major", "C, D, E, F, G, A, B, C"],
        ]),
    },
    "music-g5-l7": {
        "data_table": table(["Key Type", "Mood"], [
            ["Major key", "Often sounds happy or bright"], ["Minor key", "Often sounds sad or mysterious"],
        ]),
    },
    "music-g5-l8": {
        "data_table": table(["Dynamic Term", "Meaning"], [
            ["Forte", "Play loudly"], ["Piano", "Play softly"], ["Crescendo", "Gradually louder"],
        ]),
    },
    "music-g5-l9": {
        "data_table": table(["Tempo Term", "Meaning"], [
            ["Allegro", "Fast"], ["Adagio", "Slow"], ["Andante", "Walking pace"],
        ]),
    },
    "music-g5-l10": {
        "data_table": table(["Instrument Family", "Example"], [
            ["String", "Violin"], ["Wind", "Flute"], ["Percussion", "Drum"], ["Brass", "Trumpet"],
        ]),
    },
    "music-g5-l11": {
        "data_table": table(["Section", "Location on Stage"], [
            ["Strings", "Front"], ["Brass and Woodwinds", "Middle"], ["Percussion", "Back"],
        ]),
    },
    "music-g5-l12": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Bar line", "Divides music into measures"], ["Time signature", "Shows beats per measure"],
        ]),
    },
    "music-g5-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Call and response", "A leader sings a phrase and others answer"],
        ]),
    },
    "music-g5-l14": {
        "data_table": table(["Song", "Country of Origin"], [
            ["Frere Jacques", "France"], ["Sakura Sakura", "Japan"],
        ]),
    },
    "music-g5-l15": {
        "data_table": table(["Folk Tradition", "Region"], [
            ["Bluegrass", "Appalachian United States"], ["Flamenco", "Spain"],
        ]),
    },
    "music-g5-l17": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"], ["Classical", "1750-1820"], ["Romantic", "1820-1900"],
        ]),
    },
    "music-g5-l18": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
        ]),
    },
    "music-g5-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Round", "A song sung in overlapping repeating parts"],
        ]),
    },
    "music-g5-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Choose a scale", "Sets the notes to use"], ["Arrange notes into a pattern", "Creates the melody"],
        ]),
    },
    "music-g5-l21": {
        "data_table": table(["Musical Element", "Emotional Effect"], [
            ["Minor key", "Often sounds sad"], ["Fast tempo", "Often sounds exciting"],
        ]),
    },
    "music-g5-l22": {
        "data_table": table(["Technology", "Use"], [
            ["Digital audio workstation", "Recording and editing music"], ["Metronome app", "Keeps a steady tempo"],
        ]),
    },
    "music-g5-l23": {
        "data_table": table(["Note", "Fingering (simplified)"], [
            ["B", "Left thumb + first finger"], ["A", "Left thumb + first two fingers"],
        ]),
    },
    "music-g5-l24": {
        "data_table": table(["Ukulele String", "Note"], [
            ["Top string", "G"], ["Bottom string", "A"],
        ]),
    },
    "music-g5-l25": {
        "data_table": table(["Body Percussion", "Sound"], [
            ["Clap", "Hands together"], ["Stomp", "Foot on the ground"],
        ]),
    },
    "music-g5-l26": {
        "data_table": table(["Song Part", "Function"], [
            ["Verse", "Tells the story, changes lyrics each time"], ["Chorus", "Repeats with the same lyrics"],
        ]),
    },
    "music-g5-l27": {
        "data_table": table(["Sound Clue", "Likely Instrument"], [
            ["Deep, resonant, bowed", "Cello"], ["Bright, buzzy, brass", "Trumpet"],
        ]),
    },
    "music-g5-l28": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Sharp (#)", "Raises a note by a half step"], ["Flat (b)", "Lowers a note by a half step"],
        ]),
    },
    "music-g5-l29": {
        "data_table": table(["Conductor's Role", "Detail"], [
            ["Sets the tempo", "Guides the pace of the piece"], ["Cues sections", "Signals when to play"],
        ]),
    },
    "music-g5-l30": {
        "data_table": table(["Preparation Step", "Purpose"], [
            ["Rehearsal", "Practicing before the performance"], ["Warm-up", "Prepares the voice or instrument"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Music lessons (completing 30/30).")


if __name__ == "__main__":
    main()
