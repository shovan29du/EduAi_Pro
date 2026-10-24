#!/usr/bin/env python3
"""Depth pass, Grade 10 Music: fill in real, hand-checked data_table
content for the Grade 10 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Music to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g10-l1": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"], ["Classical", "1750-1820"], ["Romantic", "1820-1900"],
        ]),
    },
    "music-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of sounds in time"], ["Meter", "The grouping of beats"],
        ]),
    },
    "music-g10-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes perceived as a musical line"],
        ]),
    },
    "music-g10-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Harmony", "Notes played or sung together to create chords"],
        ]),
    },
    "music-g10-l5": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Whole note", "4 beats in common time"], ["Quarter note", "1 beat in common time"],
        ]),
    },
    "music-g10-l6": {
        "data_table": table(["Skill", "Purpose"], [
            ["Sight-reading", "Playing or singing music from notation at first sight"],
        ]),
    },
    "music-g10-l7": {
        "data_table": table(["Key Signature", "Sharps/Flats"], [
            ["C major", "None"], ["G major", "1 sharp (F#)"],
        ]),
    },
    "music-g10-l9": {
        "data_table": table(["Chord", "Notes (C major example)"], [
            ["C major triad", "C, E, G"],
        ]),
    },
    "music-g10-l10": {
        "data_table": table(["Family", "Examples"], [
            ["Strings", "Violin, cello"], ["Brass", "Trumpet, trombone"], ["Percussion", "Drums, timpani"],
        ]),
    },
    "music-g10-l11": {
        "data_table": table(["Instrument", "Range"], [
            ["Violin", "Highest-pitched common string instrument"],
        ]),
    },
    "music-g10-l12": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Clarinet", "Woodwind"],
        ]),
    },
    "music-g10-l13": {
        "data_table": table(["Instrument", "Family"], [
            ["Trumpet", "Brass"], ["French horn", "Brass"],
        ]),
    },
    "music-g10-l14": {
        "data_table": table(["Instrument", "Type"], [
            ["Timpani", "Pitched percussion"], ["Snare drum", "Unpitched percussion"],
        ]),
    },
    "music-g10-l15": {
        "data_table": table(["Voice Type", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-g10-l16": {
        "data_table": table(["Period", "Feature"], [
            ["Medieval music", "c. 500-1400, dominated by chant"], ["Renaissance music", "c. 1400-1600, polyphonic vocal music"],
        ]),
    },
    "music-g10-l18": {
        "data_table": table(["Composer", "Era"], [
            ["Wolfgang Amadeus Mozart", "Classical period"], ["Joseph Haydn", "Classical period"],
        ]),
    },
    "music-g10-l19": {
        "data_table": table(["Composer", "Era"], [
            ["Ludwig van Beethoven", "Bridged Classical and Romantic periods"],
        ]),
    },
    "music-g10-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["20th century classical", "Included experimental styles like atonality and minimalism"],
        ]),
    },
    "music-g10-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Opera", "A dramatic work combining singing, orchestra, and staging"],
        ]),
    },
    "music-g10-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Jazz origin", "Early 20th century, New Orleans"], ["Key feature", "Improvisation"],
        ]),
    },
    "music-g10-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Blues origin", "Late 19th century American South"],
        ]),
    },
    "music-g10-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Rock and roll origin", "1950s United States, roots in blues and country"],
        ]),
    },
    "music-g10-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Folk music", "Traditional music passed down through generations, often orally"],
        ]),
    },
    "music-g10-l26": {
        "data_table": table(["Tradition", "Region"], [
            ["Djembe drumming", "West Africa"],
        ]),
    },
    "music-g10-l27": {
        "data_table": table(["Tradition", "Region"], [
            ["Sitar music", "India"],
        ]),
    },
    "music-g10-l28": {
        "data_table": table(["Tradition", "Region"], [
            ["Salsa", "Caribbean and Latin America"],
        ]),
    },
    "music-g10-l29": {
        "data_table": table(["Tradition", "Region"], [
            ["Gamelan", "Indonesia"],
        ]),
    },
    "music-g10-l30": {
        "data_table": table(["Tradition", "Region"], [
            ["Maqam", "Middle Eastern melodic modal system"],
        ]),
    },
    "music-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Reggae origin", "1960s Jamaica"],
        ]),
    },
    "music-g10-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Hip-hop origin", "1970s in the Bronx, New York City"],
        ]),
    },
    "music-g10-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Synthesizer", "An electronic instrument that generates sound"],
        ]),
    },
    "music-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Composition", "The process of creating an original piece of music"],
        ]),
    },
    "music-g10-l35": {
        "data_table": table(["Element", "Role"], [
            ["Verse", "Tells the story"], ["Chorus", "Repeats the main hook"],
        ]),
    },
    "music-g10-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Music technology", "Tools and software used to create, record, and produce music"],
        ]),
    },
    "music-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Sound engineering", "The technical process of recording and mixing audio"],
        ]),
    },
    "music-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Film scoring", "Composing music to accompany a film"],
        ]),
    },
    "music-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Minor keys", "Often associated with sadder or more somber emotion"],
        ]),
    },
    "music-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Royalties", "Payments made to musicians for use of their music"],
        ]),
    },
    "music-g10-l41": {
        "data_table": table(["Skill", "Importance"], [
            ["Listening to fellow performers", "Keeps the ensemble in sync"],
        ]),
    },
    "music-g10-l42": {
        "data_table": table(["Role", "Responsibility"], [
            ["Conductor", "Directs tempo, dynamics, and interpretation of an ensemble"],
        ]),
    },
    "music-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Syncopation", "Placing emphasis on an unexpected beat"],
        ]),
    },
    "music-g10-l44": {
        "data_table": table(["Mode", "Feature"], [
            ["Dorian", "A minor-like mode with a raised sixth"],
        ]),
    },
    "music-g10-l45": {
        "data_table": table(["Skill", "Purpose"], [
            ["Ear training", "Developing the ability to identify pitches and intervals by ear"],
        ]),
    },
    "music-g10-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Piano keys", "88 keys total, 52 white and 36 black"],
        ]),
    },
    "music-g10-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["Guitar strings", "6 strings, typically tuned E-A-D-G-B-E"],
        ]),
    },
    "music-g10-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Musical theatre", "Combines songs, spoken dialogue, and dance to tell a story"],
        ]),
    },
    "music-g10-l49": {
        "data_table": table(["Voice Part", "Range"], [
            ["Soprano", "Highest"], ["Alto", "Second-highest"], ["Tenor", "Second-lowest"], ["Bass", "Lowest"],
        ]),
    },
    "music-g10-l50": {
        "data_table": table(["Element to Analyze", "Question"], [
            ["Form", "How is the piece structured?"], ["Instrumentation", "What instruments are used?"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Music lessons (completing 50/50).")


if __name__ == "__main__":
    main()
