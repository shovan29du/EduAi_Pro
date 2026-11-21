#!/usr/bin/env python3
"""Depth pass, Grade 9 Music: fill in real, hand-checked data_table
content for the 48 Grade 9 Music lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Music to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mus-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Composition", "The process of creating an original piece of music"],
        ]),
    },
    "music-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhythm", "The pattern of sounds in time"], ["Beat", "The steady pulse underlying music"],
        ]),
    },
    "music-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Melody", "A sequence of single notes perceived as a musical line"],
        ]),
    },
    "music-g9-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Harmony", "Notes played or sung together to create chords"],
        ]),
    },
    "music-g9-l5": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Whole note", "4 beats in common time"], ["Quarter note", "1 beat in common time"],
        ]),
    },
    "music-g9-l6": {
        "data_table": table(["Key Signature", "Sharps/Flats"], [
            ["C major", "None"], ["G major", "1 sharp (F#)"],
        ]),
    },
    "music-g9-l8": {
        "data_table": table(["Chord", "Notes (C major example)"], [
            ["C major triad", "C, E, G"],
        ]),
    },
    "music-g9-l9": {
        "data_table": table(["Time Signature", "Meaning"], [
            ["4/4", "4 beats per measure, quarter note gets the beat"], ["3/4", "3 beats per measure"],
        ]),
    },
    "music-g9-l10": {
        "data_table": table(["Dynamic Marking", "Meaning"], [
            ["Forte (f)", "Loud"], ["Piano (p)", "Soft"],
        ]),
    },
    "music-g9-l11": {
        "data_table": table(["Tempo Marking", "Meaning"], [
            ["Allegro", "Fast, lively"], ["Adagio", "Slow"],
        ]),
    },
    "music-g9-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Music theory", "The study of the structure and language of music"],
        ]),
    },
    "music-g9-l13": {
        "data_table": table(["Skill", "Purpose"], [
            ["Ear training", "Developing the ability to identify pitches and intervals by ear"],
        ]),
    },
    "music-g9-l14": {
        "data_table": table(["Skill", "Purpose"], [
            ["Sight-singing", "Singing a written melody at first sight, without hearing it first"],
        ]),
    },
    "music-g9-l15": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Baroque", "1600-1750"], ["Classical", "1750-1820"], ["Romantic", "1820-1900"],
        ]),
    },
    "music-g9-l17": {
        "data_table": table(["Composer", "Era"], [
            ["Wolfgang Amadeus Mozart", "Classical period"], ["Joseph Haydn", "Classical period"],
        ]),
    },
    "music-g9-l18": {
        "data_table": table(["Composer", "Era"], [
            ["Ludwig van Beethoven", "Bridged Classical and Romantic periods"],
        ]),
    },
    "music-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["20th century classical", "Included experimental styles like atonality and minimalism"],
        ]),
    },
    "music-g9-l20": {
        "data_table": table(["Family", "Examples"], [
            ["Strings", "Violin, cello"], ["Brass", "Trumpet, trombone"], ["Percussion", "Drums, timpani"],
        ]),
    },
    "music-g9-l21": {
        "data_table": table(["Instrument", "Range"], [
            ["Violin", "Highest-pitched string instrument"], ["Double bass", "Lowest-pitched string instrument"],
        ]),
    },
    "music-g9-l22": {
        "data_table": table(["Instrument", "Family"], [
            ["Flute", "Woodwind"], ["Clarinet", "Woodwind"], ["Oboe", "Woodwind"],
        ]),
    },
    "music-g9-l23": {
        "data_table": table(["Instrument", "Family"], [
            ["Trumpet", "Brass"], ["French horn", "Brass"], ["Tuba", "Brass"],
        ]),
    },
    "music-g9-l24": {
        "data_table": table(["Instrument", "Type"], [
            ["Timpani", "Pitched percussion"], ["Snare drum", "Unpitched percussion"],
        ]),
    },
    "music-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Piano keys", "88 keys total, 52 white and 36 black"],
        ]),
    },
    "music-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Guitar strings", "6 strings, typically tuned E-A-D-G-B-E"],
        ]),
    },
    "music-g9-l27": {
        "data_table": table(["Voice Type", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-g9-l28": {
        "data_table": table(["Voice Part", "Range"], [
            ["Soprano", "Highest"], ["Alto", "Second-highest"], ["Tenor", "Second-lowest"], ["Bass", "Lowest"],
        ]),
    },
    "music-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Jazz origin", "Early 20th century, New Orleans"], ["Key feature", "Improvisation"],
        ]),
    },
    "music-g9-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Blues origin", "Late 19th century American South"],
        ]),
    },
    "music-g9-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Rock music origin", "1950s United States, roots in blues and country"],
        ]),
    },
    "music-g9-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Hip-hop origin", "1970s in the Bronx, New York City"],
        ]),
    },
    "music-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Pop production", "Studio techniques used to create polished, mainstream music"],
        ]),
    },
    "music-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Synthesizer", "An electronic instrument that generates sound"],
        ]),
    },
    "music-g9-l35": {
        "data_table": table(["Tradition", "Region"], [
            ["Djembe drumming", "West Africa"],
        ]),
    },
    "music-g9-l36": {
        "data_table": table(["Tradition", "Region"], [
            ["Gamelan", "Indonesia"], ["Sitar music", "India"],
        ]),
    },
    "music-g9-l37": {
        "data_table": table(["Tradition", "Region"], [
            ["Salsa", "Caribbean and Latin America"],
        ]),
    },
    "music-g9-l38": {
        "data_table": table(["Tradition", "Region"], [
            ["Maqam", "Middle Eastern melodic modal system"],
        ]),
    },
    "music-g9-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Recording", "Capturing sound for playback"],
        ]),
    },
    "music-g9-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["DAW", "Digital Audio Workstation, software for recording and editing music"],
        ]),
    },
    "music-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Film scoring", "Composing music to accompany a film"],
        ]),
    },
    "music-g9-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Minor keys", "Often associated with sadder or more somber emotion"],
        ]),
    },
    "music-g9-l43": {
        "data_table": table(["Element to Analyze", "Question"], [
            ["Form", "How is the piece structured?"], ["Instrumentation", "What instruments are used?"],
        ]),
    },
    "music-g9-l44": {
        "data_table": table(["Section", "Role"], [
            ["Verse", "Tells the story, changes lyrics each time"], ["Chorus", "Repeats, carries the main hook"],
        ]),
    },
    "music-g9-l45": {
        "data_table": table(["Form", "Structure"], [
            ["Sonata form", "Exposition, development, recapitulation"], ["Rondo form", "A recurring main theme (ABACA)"],
        ]),
    },
    "music-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Improvisation", "Composing music spontaneously while performing"],
        ]),
    },
    "music-g9-l47": {
        "data_table": table(["Skill", "Importance"], [
            ["Listening to fellow performers", "Keeps the ensemble in sync"],
        ]),
    },
    "music-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Royalties", "Payments made to musicians for use of their music"],
        ]),
    },
    "music-g9-l49": {
        "data_table": table(["Career", "Focus"], [
            ["Performer", "Plays or sings music"], ["Music producer", "Oversees recording and production"],
        ]),
    },
    "music-g9-l50": {
        "data_table": table(["Etiquette", "Reason"], [
            ["Silence phones", "Avoids distracting performers and audience"], ["Applaud at appropriate times", "Respects the performance flow"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Music lessons (completing 50/50).")


if __name__ == "__main__":
    main()
