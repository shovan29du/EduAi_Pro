#!/usr/bin/env python3
"""Depth pass, Grade 7 Music: fill in real, hand-checked data_table
content for the 38 Grade 7 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Music to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g7-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Harmony", "Notes played together"], ["Chord", "Three or more notes played at once"],
        ]),
    },
    "music-g7-l2": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Treble clef", "Indicates higher-pitched notes"], ["Bass clef", "Indicates lower-pitched notes"],
        ]),
    },
    "music-g7-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of long and short sounds"], ["Meter", "How beats are grouped into measures"],
        ]),
    },
    "music-g7-l4": {
        "data_table": table(["Time Signature", "Meaning"], [
            ["4/4", "4 beats per measure"], ["3/4", "3 beats per measure (waltz time)"],
        ]),
    },
    "music-g7-l6": {
        "data_table": table(["Key Signature", "Sharps/Flats"], [
            ["C Major", "None"], ["G Major", "1 sharp (F#)"],
        ]),
    },
    "music-g7-l8": {
        "data_table": table(["Step", "Purpose"], [
            ["Choose a scale", "Sets the notes to use"], ["Arrange notes into a pattern", "Creates the melody"],
        ]),
    },
    "music-g7-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Dynamics", "How loud or soft the music is"], ["Tempo", "The speed of the music"],
        ]),
    },
    "music-g7-l10": {
        "data_table": table(["Skill", "Purpose"], [
            ["Interval recognition", "Identifying the distance between two notes by ear"],
        ]),
    },
    "music-g7-l11": {
        "data_table": table(["Instrument Family", "Example"], [
            ["String", "Violin"], ["Wind", "Flute"], ["Brass", "Trumpet"], ["Percussion", "Drum"],
        ]),
    },
    "music-g7-l12": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Violin", "Bowed or plucked strings"], ["Cello", "Bowed strings, larger and lower-pitched"],
        ]),
    },
    "music-g7-l13": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Clarinet", "Woodwind"],
        ]),
    },
    "music-g7-l14": {
        "data_table": table(["Instrument", "Family"], [
            ["Trumpet", "Brass"], ["Trombone", "Brass"],
        ]),
    },
    "music-g7-l15": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
        ]),
    },
    "music-g7-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Piano keys", "88 total on a full-size piano"],
        ]),
    },
    "music-g7-l17": {
        "data_table": table(["Guitar String", "Note"], [
            ["Thickest string", "E"], ["Thinnest string", "E (higher octave)"],
        ]),
    },
    "music-g7-l18": {
        "data_table": table(["Voice Type", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-g7-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Improvisation", "Creating music spontaneously"],
        ]),
    },
    "music-g7-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Choose a scale", "Sets the notes to use"], ["Arrange notes into a pattern", "Creates the melody"],
        ]),
    },
    "music-g7-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Lyrics", "The words of a song"], ["Melody", "The tune of a song"],
        ]),
    },
    "music-g7-l22": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"],
        ]),
    },
    "music-g7-l23": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Classical", "1750-1820"],
        ]),
    },
    "music-g7-l24": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Romantic", "1820-1900"],
        ]),
    },
    "music-g7-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["20th century music", "Included jazz, atonal music, and electronic music"],
        ]),
    },
    "music-g7-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Jazz origin", "Early 20th century, New Orleans"],
        ]),
    },
    "music-g7-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["The Blues", "Originated among African Americans in the American South"],
        ]),
    },
    "music-g7-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Rock and roll emerged", "1950s in the United States"],
        ]),
    },
    "music-g7-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Hip-hop originated", "1970s, in the Bronx, New York"],
        ]),
    },
    "music-g7-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Electronic music", "Music produced using electronic instruments and technology"],
        ]),
    },
    "music-g7-l31": {
        "data_table": table(["Folk Tradition", "Region"], [
            ["Bluegrass", "Appalachian United States"],
        ]),
    },
    "music-g7-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Djembe", "A West African hand drum"],
        ]),
    },
    "music-g7-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Raga", "A melodic framework in Indian classical music"],
        ]),
    },
    "music-g7-l34": {
        "data_table": table(["Rhythm Style", "Region"], [
            ["Samba", "Brazil"], ["Salsa", "Cuba/Latin America"],
        ]),
    },
    "music-g7-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Maqam", "A system of melodic modes in Middle Eastern music"],
        ]),
    },
    "music-g7-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Film score", "Music composed to accompany a film"],
        ]),
    },
    "music-g7-l37": {
        "data_table": table(["Technology", "Use"], [
            ["Digital audio workstation", "Recording and editing music"],
        ]),
    },
    "music-g7-l38": {
        "data_table": table(["Software Feature", "Purpose"], [
            ["Notation entry", "Adding notes to a digital score"],
        ]),
    },
    "music-g7-l39": {
        "data_table": table(["Ensemble Skill", "Purpose"], [
            ["Listening to others", "Keeps the group together"], ["Staying in time", "Keeps rhythm unified"],
        ]),
    },
    "music-g7-l40": {
        "data_table": table(["Cultural Connection", "Example"], [
            ["National anthem", "Represents a country's identity through music"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Music lessons (completing 40/40).")


if __name__ == "__main__":
    main()
