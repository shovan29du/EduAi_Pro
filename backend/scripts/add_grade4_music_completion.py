#!/usr/bin/env python3
"""Depth pass, Grade 4 Music: fill in real, hand-checked data_table
content for the 28 Grade 4 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 4 Music to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g4-l1": {
        "data_table": table(["Note Value", "Beats"], [
            ["Whole note", "4 beats"], ["Half note", "2 beats"], ["Quarter note", "1 beat"],
        ]),
    },
    "music-g4-l2": {
        "data_table": table(["Instrument Family", "Example"], [
            ["String", "Violin"], ["Wind", "Flute"], ["Percussion", "Drum"], ["Brass", "Trumpet"],
        ]),
    },
    "music-g4-l3": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
        ]),
    },
    "music-g4-l4": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Violin", "Bowed or plucked strings"], ["Cello", "Bowed strings, larger and lower-pitched"],
        ]),
    },
    "music-g4-l5": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Trumpet", "Brass"],
        ]),
    },
    "music-g4-l6": {
        "data_table": table(["Vocal Skill", "Description"], [
            ["Breath control", "Managing air while singing"], ["Pitch matching", "Singing the correct note"],
        ]),
    },
    "music-g4-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Tempo", "The speed of the music"], ["Dynamics", "How loud or soft the music is"],
        ]),
    },
    "music-g4-l8": {
        "data_table": table(["Scale", "Notes (C Major)"], [
            ["C Major", "C, D, E, F, G, A, B, C"],
        ]),
    },
    "music-g4-l9": {
        "data_table": table(["Pattern Type", "Example"], [
            ["Steady beat", "Clap on every count"], ["Syncopation", "Accenting off-beats"],
        ]),
    },
    "music-g4-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes forming a tune"],
        ]),
    },
    "music-g4-l13": {
        "data_table": table(["Song", "Country of Origin"], [
            ["Frere Jacques", "France"], ["Sakura Sakura", "Japan"],
        ]),
    },
    "music-g4-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Recorder type", "Woodwind instrument"], ["How it's played", "Blowing air through a mouthpiece"],
        ]),
    },
    "music-g4-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Keyboard/piano", "Has 88 keys on a full-size piano"],
        ]),
    },
    "music-g4-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Call and response", "A leader sings a phrase and others answer"],
        ]),
    },
    "music-g4-l17": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Treble clef", "Indicates higher-pitched notes"], ["Bar line", "Divides music into measures"],
        ]),
    },
    "music-g4-l18": {
        "data_table": table(["Rhythm Element", "Example"], [
            ["Beat", "The steady pulse"], ["Pattern", "A repeated rhythmic sequence"],
        ]),
    },
    "music-g4-l19": {
        "data_table": table(["Musical Element", "Emotional Effect"], [
            ["Minor key", "Often sounds sad or mysterious"], ["Major key", "Often sounds happy or bright"],
        ]),
    },
    "music-g4-l20": {
        "data_table": table(["Ensemble Skill", "Purpose"], [
            ["Listening to others", "Keeps the group together"], ["Staying in time", "Keeps rhythm unified"],
        ]),
    },
    "music-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Reading sheet music", "Following note lengths while playing"],
        ]),
    },
    "music-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Orchestra seating", "Instruments grouped by family"],
        ]),
    },
    "music-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Marching band", "Percussion keeps the beat for marchers"],
        ]),
    },
    "music-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["String quartet", "Violins, viola, and cello play together"],
        ]),
    },
    "music-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Jazz band", "Trumpets and saxophones lead the melody"],
        ]),
    },
    "music-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Choir practice", "Warming up before singing together"],
        ]),
    },
    "music-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Movie soundtracks", "Tempo and dynamics build tension"],
        ]),
    },
    "music-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Songwriting", "Using a scale to compose a melody"],
        ]),
    },
    "music-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Clapping games", "Practicing rhythm patterns with friends"],
        ]),
    },
    "music-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Singing along to songs", "Following the melody line"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Music lessons (completing 30/30).")


if __name__ == "__main__":
    main()
