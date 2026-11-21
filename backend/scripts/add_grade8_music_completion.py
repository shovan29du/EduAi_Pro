#!/usr/bin/env python3
"""Depth pass, Grade 8 Music: fill in real, hand-checked data_table
content for the 38 Grade 8 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Music to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "music-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of long and short sounds"], ["Beat", "The steady pulse of music"],
        ]),
    },
    "music-g8-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes forming a tune"], ["Harmony", "Notes played together"],
        ]),
    },
    "music-g8-l4": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Treble clef", "Indicates higher-pitched notes"],
        ]),
    },
    "music-g8-l5": {
        "data_table": table(["Time Signature", "Meaning"], [
            ["4/4", "4 beats per measure"], ["3/4", "3 beats per measure (waltz time)"],
        ]),
    },
    "music-g8-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Chord", "Three or more notes played at once"], ["Chord progression", "A sequence of chords"],
        ]),
    },
    "music-g8-l7": {
        "data_table": table(["Key Type", "Mood"], [
            ["Major key", "Often sounds happy or bright"], ["Minor key", "Often sounds sad or mysterious"],
        ]),
    },
    "music-g8-l8": {
        "data_table": table(["Instrument", "How It Makes Sound"], [
            ["Violin", "Bowed or plucked strings"],
        ]),
    },
    "music-g8-l9": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Clarinet", "Woodwind"],
        ]),
    },
    "music-g8-l10": {
        "data_table": table(["Instrument", "Family"], [
            ["Trumpet", "Brass"], ["Trombone", "Brass"],
        ]),
    },
    "music-g8-l11": {
        "data_table": table(["Instrument", "How It's Played"], [
            ["Drum", "Struck with hands or sticks"],
        ]),
    },
    "music-g8-l12": {
        "data_table": table(["Voice Type", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-g8-l13": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"],
        ]),
    },
    "music-g8-l14": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Classical", "1750-1820"],
        ]),
    },
    "music-g8-l15": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Romantic", "1820-1900"],
        ]),
    },
    "music-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Djembe", "A West African hand drum"],
        ]),
    },
    "music-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Raga", "A melodic framework in Indian classical music"],
        ]),
    },
    "music-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Maqam", "A system of melodic modes in Middle Eastern music"],
        ]),
    },
    "music-g8-l20": {
        "data_table": table(["Rhythm Style", "Region"], [
            ["Samba", "Brazil"], ["Salsa", "Cuba/Latin America"],
        ]),
    },
    "music-g8-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Jazz origin", "Early 20th century, New Orleans"],
        ]),
    },
    "music-g8-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["The Blues", "Originated among African Americans in the American South"],
        ]),
    },
    "music-g8-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Rock and roll emerged", "1950s in the United States"],
        ]),
    },
    "music-g8-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Hip-hop originated", "1970s, in the Bronx, New York"],
        ]),
    },
    "music-g8-l25": {
        "data_table": table(["Folk Tradition", "Region"], [
            ["Bluegrass", "Appalachian United States"],
        ]),
    },
    "music-g8-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Choose a scale", "Sets the notes to use"],
        ]),
    },
    "music-g8-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Lyrics", "The words of a song"], ["Verse", "A section that changes lyrics each repetition"],
        ]),
    },
    "music-g8-l28": {
        "data_table": table(["Technology", "Use"], [
            ["Digital audio workstation", "Recording and editing music"],
        ]),
    },
    "music-g8-l29": {
        "data_table": table(["Software Feature", "Purpose"], [
            ["Notation entry", "Adding notes to a digital score"],
        ]),
    },
    "music-g8-l30": {
        "data_table": table(["Conductor's Role", "Detail"], [
            ["Sets the tempo", "Guides the pace of the piece"],
        ]),
    },
    "music-g8-l31": {
        "data_table": table(["Ensemble Skill", "Purpose"], [
            ["Listening to others", "Keeps the group together"],
        ]),
    },
    "music-g8-l32": {
        "data_table": table(["Ensemble Type", "Example"], [
            ["String quartet", "Two violins, viola, and cello"],
        ]),
    },
    "music-g8-l33": {
        "data_table": table(["Musical Element", "Emotional Effect"], [
            ["Minor key", "Often sounds sad or mysterious"],
        ]),
    },
    "music-g8-l34": {
        "data_table": table(["Interval", "Example"], [
            ["Octave", "C to the next C"], ["Fifth", "C to G"],
        ]),
    },
    "music-g8-l35": {
        "data_table": table(["Dynamic Term", "Meaning"], [
            ["Forte", "Play loudly"], ["Piano", "Play softly"],
        ]),
    },
    "music-g8-l36": {
        "data_table": table(["Composer", "Known For"], [
            ["Johann Sebastian Bach", "Baroque master of counterpoint"], ["George Frideric Handel", "Composer of Messiah"],
        ]),
    },
    "music-g8-l37": {
        "data_table": table(["Composer", "Known For"], [
            ["Wolfgang Amadeus Mozart", "Classical era symphonies and operas"],
            ["Ludwig van Beethoven", "Symphonies, including the Ninth"],
        ]),
    },
    "music-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Film score", "Music composed to accompany a film"],
        ]),
    },
    "music-g8-l39": {
        "data_table": table(["Cultural Connection", "Example"], [
            ["National anthem", "Represents a country's identity through music"],
        ]),
    },
    "music-g8-l40": {
        "data_table": table(["Career", "Focus"], [
            ["Music producer", "Oversees recording and production"], ["Music teacher", "Teaches music skills"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Music lessons (completing 40/40).")


if __name__ == "__main__":
    main()
