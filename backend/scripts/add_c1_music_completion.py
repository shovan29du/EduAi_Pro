#!/usr/bin/env python3
"""Depth pass, C1 Music: fill in real, hand-checked data_table content
for the 69 C1 Music lessons not covered by the earlier breadth-first
batch. Brings C1 Music to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "music-c1-l1": {
        "data_table": table(["Element", "Meaning"], [
            ["Pitch", "How high or low a sound is perceived to be"],
        ]),
    },
    "music-c1-l2": {
        "data_table": table(["Era", "Approximate Dates"], [
            ["Medieval", "500-1400"], ["Renaissance", "1400-1600"],
        ]),
    },
    "music-c1-l4": {
        "data_table": table(["Skill", "Purpose"], [
            ["Interval recognition", "Trains the ear to identify the distance between two pitches"],
        ]),
    },
    "music-c1-l5": {
        "data_table": table(["Feature", "Detail"], [
            ["Baroque era", "c. 1600-1750, marked by ornamentation and basso continuo"],
        ]),
    },
    "music-c1-l6": {
        "data_table": table(["Tradition", "Feature"], [
            ["Indian classical music", "Built on raga (melodic framework) and tala (rhythmic cycle)"],
        ]),
    },
    "music-c1-l7": {
        "data_table": table(["Style", "Feature"], [
            ["New Orleans jazz", "Early jazz style built on collective improvisation"],
        ]),
    },
    "music-c1-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Motif", "A short musical idea developed throughout a composition"],
        ]),
    },
    "music-c1-l9": {
        "data_table": table(["Family", "Example"], [
            ["Strings", "Violin, cello"], ["Woodwinds", "Flute, clarinet"],
        ]),
    },
    "music-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Mixing", "Balancing recorded tracks into a final stereo or surround mix"],
        ]),
    },
    "music-c1-l11": {
        "data_table": table(["Role", "Responsibility"], [
            ["A&R representative", "Scouts and develops recording artists for a label"],
        ]),
    },
    "music-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethnomusicology", "The study of music within its cultural and social context"],
        ]),
    },
    "music-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Film score", "Original music composed to accompany a film's narrative"],
        ]),
    },
    "music-c1-l14": {
        "data_table": table(["Tool", "Purpose"], [
            ["DAW", "Digital Audio Workstation, software for recording and editing audio"],
        ]),
    },
    "music-c1-l15": {
        "data_table": table(["Pattern", "Meter"], [
            ["Four-beat pattern", "4/4 time"], ["Three-beat pattern", "3/4 time"],
        ]),
    },
    "music-c1-l16": {
        "data_table": table(["Technique", "Purpose"], [
            ["Diaphragmatic breathing", "Supports sustained, controlled vocal tone"],
        ]),
    },
    "music-c1-l17": {
        "data_table": table(["Method", "Focus"], [
            ["Kodály method", "Builds musicianship through solfège and folk song"], ["Suzuki method", "Teaches instrumental skill through listening and imitation"],
        ]),
    },
    "music-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Popular music studies", "Academic analysis of commercially popular music genres"],
        ]),
    },
    "music-c1-l19": {
        "data_table": table(["Example", "Movement"], [
            ["'We Shall Overcome'", "US Civil Rights Movement"],
        ]),
    },
    "music-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Sketching a melody first", "Establishes the core musical idea before adding harmony"],
        ]),
    },
    "music-c1-l21": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Whole note", "A note held for four beats in common time"], ["Quarter note", "A note held for one beat"],
        ]),
    },
    "music-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Meter", "The recurring pattern of strong and weak beats in music"],
        ]),
    },
    "music-c1-l23": {
        "data_table": table(["Scale", "Pattern"], [
            ["Major scale", "Whole-whole-half-whole-whole-whole-half"], ["Natural minor scale", "Whole-half-whole-whole-half-whole-whole"],
        ]),
    },
    "music-c1-l24": {
        "data_table": table(["Interval", "Example"], [
            ["Perfect fifth", "C to G"], ["Major third", "C to E"],
        ]),
    },
    "music-c1-l25": {
        "data_table": table(["Chord Type", "Notes (from root)"], [
            ["Major triad", "Root, major third, perfect fifth"], ["Seventh chord", "Triad plus a seventh above the root"],
        ]),
    },
    "music-c1-l26": {
        "data_table": table(["Key", "Sharps/Flats"], [
            ["C major", "None"], ["G major", "One sharp (F#)"],
        ]),
    },
    "music-c1-l27": {
        "data_table": table(["Form", "Structure"], [
            ["Binary form", "Two contrasting sections, A-B"], ["Ternary form", "Three sections, A-B-A"],
        ]),
    },
    "music-c1-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Renaissance music", "Emphasized vocal polyphony and modal harmony"],
        ]),
    },
    "music-c1-l29": {
        "data_table": table(["Feature", "Detail"], [
            ["Classical era", "c. 1750-1820, valued balance, clarity, and formal structure"],
        ]),
    },
    "music-c1-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Romantic era", "c. 1820-1900, emphasized emotional expression and expanded orchestration"],
        ]),
    },
    "music-c1-l31": {
        "data_table": table(["Movement", "Feature"], [
            ["Serialism", "Organizes pitch using a fixed ordered series of tones"],
        ]),
    },
    "music-c1-l32": {
        "data_table": table(["Genre", "Origin"], [
            ["Samba", "Brazil"], ["Salsa", "Cuba and Puerto Rico, developed in New York"],
        ]),
    },
    "music-c1-l33": {
        "data_table": table(["Feature", "Detail"], [
            ["Raga", "A melodic framework for improvisation in Indian classical music"],
        ]),
    },
    "music-c1-l34": {
        "data_table": table(["Tradition", "Feature"], [
            ["Gagaku", "Ancient Japanese court music"],
        ]),
    },
    "music-c1-l35": {
        "data_table": table(["Feature", "Detail"], [
            ["Twelve-bar blues", "A common harmonic progression underlying blues music"],
        ]),
    },
    "music-c1-l36": {
        "data_table": table(["Element", "Feature"], [
            ["Sampling", "Reusing a portion of a previous recording in a new track"],
        ]),
    },
    "music-c1-l37": {
        "data_table": table(["Pioneer", "Contribution"], [
            ["Kraftwerk", "Pioneered electronic pop using synthesizers and drum machines"],
        ]),
    },
    "music-c1-l38": {
        "data_table": table(["Family", "Example"], [
            ["Brass", "Trumpet, trombone"], ["Percussion", "Drums, xylophone"],
        ]),
    },
    "music-c1-l39": {
        "data_table": table(["Section", "Instruments"], [
            ["Strings", "Violins, violas, cellos, basses"], ["Brass", "Trumpets, horns, trombones"],
        ]),
    },
    "music-c1-l40": {
        "data_table": table(["Ensemble", "Example"], [
            ["String quartet", "Two violins, viola, and cello"],
        ]),
    },
    "music-c1-l41": {
        "data_table": table(["Voice Part", "Range"], [
            ["Soprano", "Highest female voice"], ["Bass", "Lowest male voice"],
        ]),
    },
    "music-c1-l42": {
        "data_table": table(["Skill", "Purpose"], [
            ["Sight-reading", "Performing notated music accurately on first viewing"],
        ]),
    },
    "music-c1-l43": {
        "data_table": table(["Skill", "Purpose"], [
            ["Rhythmic dictation", "Notating a rhythm accurately after hearing it"],
        ]),
    },
    "music-c1-l44": {
        "data_table": table(["Skill", "Purpose"], [
            ["Melodic dictation", "Notating a melody's pitches after hearing it"],
        ]),
    },
    "music-c1-l45": {
        "data_table": table(["Section", "Role"], [
            ["Verse", "Advances the song's narrative"], ["Chorus", "Repeats the song's central hook"],
        ]),
    },
    "music-c1-l46": {
        "data_table": table(["Element", "Purpose"], [
            ["Hook", "A memorable, catchy phrase that anchors a song"],
        ]),
    },
    "music-c1-l47": {
        "data_table": table(["Tool", "Purpose"], [
            ["Notation software", "Digitally engraves sheet music for printing or playback"],
        ]),
    },
    "music-c1-l48": {
        "data_table": table(["Equipment", "Use"], [
            ["Microphone", "Captures acoustic sound as an electrical signal"], ["Audio interface", "Converts analog signals to digital for a computer"],
        ]),
    },
    "music-c1-l49": {
        "data_table": table(["Venue Type", "Feature"], [
            ["Concert hall", "Designed acoustics for classical performance"], ["Club venue", "Amplified sound for popular music"],
        ]),
    },
    "music-c1-l50": {
        "data_table": table(["Setting", "Etiquette"], [
            ["Classical concert", "Applause typically withheld until a piece fully concludes"],
        ]),
    },
    "music-c1-l51": {
        "data_table": table(["Genre", "Feature"], [
            ["Blues", "Built on the twelve-bar progression and expressive vocal bends"],
        ]),
    },
    "music-c1-l52": {
        "data_table": table(["Element", "Emotional Effect"], [
            ["Minor key", "Often perceived as sad or somber"], ["Fast tempo", "Often perceived as energetic or urgent"],
        ]),
    },
    "music-c1-l53": {
        "data_table": table(["Sector", "Role"], [
            ["Streaming platforms", "Primary distribution channel for recorded music today"],
        ]),
    },
    "music-c1-l54": {
        "data_table": table(["Equipment", "Purpose"], [
            ["PA system", "Amplifies sound for a live audience"],
        ]),
    },
    "music-c1-l55": {
        "data_table": table(["Practice", "Benefit"], [
            ["Sectional rehearsal", "Allows one instrument group to focus on difficult passages"],
        ]),
    },
    "music-c1-l56": {
        "data_table": table(["Practice", "Benefit"], [
            ["Practice log", "Tracks progress and identifies recurring problem areas"],
        ]),
    },
    "music-c1-l57": {
        "data_table": table(["Element", "Question"], [
            ["Harmonic analysis", "What chords and progressions structure this passage?"],
        ]),
    },
    "music-c1-l58": {
        "data_table": table(["Tradition", "Instrument"], [
            ["West African tradition", "Djembe drum"], ["Afro-Cuban tradition", "Conga drum"],
        ]),
    },
    "music-c1-l59": {
        "data_table": table(["Use", "Example"], [
            ["Video game music", "Adaptive scores that respond to gameplay"],
        ]),
    },
    "music-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Session musician", "Performs on recordings for other artists"], ["Music therapist", "Uses music to support health and wellbeing"],
        ]),
    },
    "music-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Fieldwork methods", "Recording and documenting a living musical tradition"],
        ]),
    },
    "music-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Applying scale and rhythm", "Building a simple melody over a steady beat"],
        ]),
    },
    "music-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Placing a work in context", "Linking a Baroque piece to its historical period"],
        ]),
    },
    "music-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a triad", "Stacking thirds above a given root note"],
        ]),
    },
    "music-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying intervals by ear", "Distinguishing a perfect fifth from a major third"],
        ]),
    },
    "music-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Recognizing ornamentation", "Spotting a trill in a Baroque keyboard piece"],
        ]),
    },
    "music-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing traditions", "Contrasting rhythmic cycles across two world music styles"],
        ]),
    },
    "music-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing improvisation", "Identifying call-and-response in a jazz recording"],
        ]),
    },
    "music-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Developing a motif", "Repeating and varying a short musical idea"],
        ]),
    },
    "music-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Scoring for instruments", "Choosing which instrument best carries a melodic line"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Music lessons (completing 70/70).")


if __name__ == "__main__":
    main()
