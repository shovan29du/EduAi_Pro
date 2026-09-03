#!/usr/bin/env python3
"""Depth pass, C2 Music: fill in real, hand-checked data_table content
for the 69 C2 Music lessons not covered by the earlier breadth-first
batch. Brings C2 Music to full 70/70 coverage.

l61-l63 are "Foundations 2" lessons revisiting l23, l24, and l6;
l64-l70 are "Worked Analysis" companions to l1-l7 (l69 revisits l6's
table since it points back to the "Foundations" lesson). l3 was
already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "music-c2-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Music history foundations", "Traces stylistic development from early notation through the present"],
        ]),
    },
    "music-c2-l2": {
        "data_table": table(["Skill", "Feature"], [
            ["Ear training", "Builds recognition of intervals, chords, and rhythm by listening"],
        ]),
    },
    "music-c2-l4": {
        "data_table": table(["Skill", "Detail"], [
            ["Sight-singing", "Reading and singing notated pitch and rhythm accurately at first sight"],
        ]),
    },
    "music-c2-l5": {
        "data_table": table(["Era", "Feature"], [
            ["Classical era", "Emphasized balance, clarity, and formal structures like sonata form"],
        ]),
    },
    "music-c2-l6": {
        "data_table": table(["Tradition", "Feature"], [
            ["Sub-Saharan African music", "Complex polyrhythms and call-and-response form central roles"],
        ]),
    },
    "music-c2-l7": {
        "data_table": table(["Concept", "Meaning"], [
            ["ii-V-I progression", "A core harmonic pattern underlying much jazz repertoire"],
        ]),
    },
    "music-c2-l8": {
        "data_table": table(["Form", "Structure"], [
            ["Binary form", "AB — two contrasting sections"],
            ["Ternary form", "ABA — a return to the opening section"],
        ]),
    },
    "music-c2-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Small-group arranging", "Distributes melody, harmony, and rhythm across available instruments"],
        ]),
    },
    "music-c2-l10": {
        "data_table": table(["Concept", "Purpose"], [
            ["Audio mixing", "Balances levels, panning, and EQ across tracks into a cohesive whole"],
        ]),
    },
    "music-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Mechanical royalty", "Paid for reproducing a composition, e.g. on a recording"],
            ["Performance royalty", "Paid for public performance or broadcast of a work"],
        ]),
    },
    "music-c2-l12": {
        "data_table": table(["Method", "Purpose"], [
            ["Ethnomusicological fieldwork", "Documents music within its cultural and social context"],
        ]),
    },
    "music-c2-l13": {
        "data_table": table(["Technique", "Purpose"], [
            ["Scoring to picture", "Aligns musical cues precisely with on-screen timing and action"],
        ]),
    },
    "music-c2-l14": {
        "data_table": table(["Concept", "Meaning"], [
            ["MIDI", "A protocol transmitting note and control data rather than audio itself"],
        ]),
    },
    "music-c2-l15": {
        "data_table": table(["Gesture", "Purpose"], [
            ["Cueing", "Signals an entrance to a specific performer or section"],
            ["Dynamic gesture", "Indicates changes in volume to the ensemble"],
        ]),
    },
    "music-c2-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Vocal pedagogy", "Teaches breath support, resonance, and healthy vocal technique"],
        ]),
    },
    "music-c2-l17": {
        "data_table": table(["Method", "Focus"], [
            ["Orff/Kodály approach", "Uses movement, singing, and simple instruments to teach young learners"],
        ]),
    },
    "music-c2-l18": {
        "data_table": table(["Era", "Feature"], [
            ["Rock music history", "Emerged from blues and R&B roots into a dominant popular genre"],
        ]),
    },
    "music-c2-l19": {
        "data_table": table(["Movement", "Feature"], [
            ["Folk revival/protest song", "Used accessible melodies and lyrics to advance social and political causes"],
        ]),
    },
    "music-c2-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone performance", "Demonstrates prepared technical and interpretive musical skill"],
        ]),
    },
    "music-c2-l21": {
        "data_table": table(["Chord", "Function"], [
            ["Secondary dominant", "Temporarily tonicizes a scale degree other than the tonic"],
        ]),
    },
    "music-c2-l22": {
        "data_table": table(["Technique", "Detail"], [
            ["Pivot chord modulation", "Uses a chord common to both keys to shift tonal center smoothly"],
        ]),
    },
    "music-c2-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Chromatic harmony", "Uses pitches outside the diatonic scale to color or destabilize tonality"],
        ]),
    },
    "music-c2-l24": {
        "data_table": table(["Rule", "Purpose"], [
            ["Voice leading", "Guides smooth, singable motion between chord tones in each voice"],
        ]),
    },
    "music-c2-l25": {
        "data_table": table(["Species", "Rule"], [
            ["First species", "Note against note, consonant intervals only"],
        ]),
    },
    "music-c2-l26": {
        "data_table": table(["Section", "Function"], [
            ["Exposition", "Presents primary and secondary thematic material"],
            ["Development", "Explores and transforms thematic material"],
            ["Recapitulation", "Returns themes, typically resolved in the tonic"],
        ]),
    },
    "music-c2-l27": {
        "data_table": table(["Form", "Detail"], [
            ["Theme and variations", "A stated theme is repeated with changing melodic, harmonic, or rhythmic treatment"],
        ]),
    },
    "music-c2-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Baroque ornamentation", "Trills, mordents, and turns embellish the melodic line"],
        ]),
    },
    "music-c2-l29": {
        "data_table": table(["Feature", "Detail"], [
            ["Symphonic development", "Classical composers expanded thematic transformation within larger orchestral forms"],
        ]),
    },
    "music-c2-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Program music", "Instrumental music that depicts a specific extra-musical narrative or scene"],
        ]),
    },
    "music-c2-l31": {
        "data_table": table(["Technique", "Detail"], [
            ["Twelve-tone serialism", "Organizes pitch using a fixed ordering of all twelve chromatic tones"],
        ]),
    },
    "music-c2-l32": {
        "data_table": table(["Technique", "Detail"], [
            ["Minimalism", "Builds music from repeating, gradually shifting short patterns"],
        ]),
    },
    "music-c2-l33": {
        "data_table": table(["Form", "Region"], [
            ["Bossa nova/salsa", "Latin American forms blending African rhythm with European harmony"],
        ]),
    },
    "music-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Raga", "A melodic framework guiding improvisation in Indian classical music"],
            ["Tala", "A rhythmic cycle organizing time in Indian classical music"],
        ]),
    },
    "music-c2-l35": {
        "data_table": table(["Ensemble", "Feature"], [
            ["Gamelan", "Indonesian ensemble centered on tuned metallophones and interlocking parts"],
        ]),
    },
    "music-c2-l36": {
        "data_table": table(["Element", "Detail"], [
            ["12-bar blues", "A recurring chord progression underlying most blues repertoire"],
        ]),
    },
    "music-c2-l37": {
        "data_table": table(["Technique", "Detail"], [
            ["Sampling", "Reuses recorded audio fragments as building blocks in new compositions"],
        ]),
    },
    "music-c2-l38": {
        "data_table": table(["Technique", "Detail"], [
            ["Synthesis/sequencing", "Builds electronic tracks from generated and arranged sound sources"],
        ]),
    },
    "music-c2-l39": {
        "data_table": table(["Family", "Role"], [
            ["Strings", "Provide sustained, blended harmonic and melodic texture"],
            ["Winds", "Add distinct timbral color and articulation"],
        ]),
    },
    "music-c2-l40": {
        "data_table": table(["Concept", "Purpose"], [
            ["Ensemble balance", "Ensures no single part overwhelms the collective chamber texture"],
        ]),
    },
    "music-c2-l41": {
        "data_table": table(["Technique", "Purpose"], [
            ["Choral conducting gesture", "Coordinates diction, breath, and dynamic shape across voice parts"],
        ]),
    },
    "music-c2-l42": {
        "data_table": table(["Skill", "Detail"], [
            ["Modulating sight-singing", "Tracks shifting tonal centers while reading a melody in real time"],
        ]),
    },
    "music-c2-l43": {
        "data_table": table(["Meter", "Feature"], [
            ["Complex/mixed meter", "Combines groupings like 3+2 within a single measure"],
        ]),
    },
    "music-c2-l44": {
        "data_table": table(["Skill", "Detail"], [
            ["Chromatic dictation", "Notates melodies that move outside the diatonic scale by ear"],
        ]),
    },
    "music-c2-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Concept album", "Uses song sequence and recurring motifs to build a unified narrative arc"],
        ]),
    },
    "music-c2-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Prosody", "Aligns natural speech stress with musical rhythm and melody"],
        ]),
    },
    "music-c2-l47": {
        "data_table": table(["Standard", "Purpose"], [
            ["Engraving standard", "Ensures notated scores are clear and consistent for performers"],
        ]),
    },
    "music-c2-l48": {
        "data_table": table(["Stage", "Role"], [
            ["Signal chain", "Traces audio from microphone through preamp, processing, to recorder"],
        ]),
    },
    "music-c2-l49": {
        "data_table": table(["Factor", "Effect"], [
            ["Reverberation time", "Longer decay suits sustained tone, shorter suits rhythmic clarity"],
        ]),
    },
    "music-c2-l50": {
        "data_table": table(["Practice", "Detail"], [
            ["Historically informed performance", "Uses period instruments and techniques to approximate original sound"],
        ]),
    },
    "music-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Genre hybridity", "Contemporary artists blend traditions to create new stylistic combinations"],
        ]),
    },
    "music-c2-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Music cognition", "Studies how the brain processes pitch, rhythm, and musical expectation"],
        ]),
    },
    "music-c2-l53": {
        "data_table": table(["Deal Type", "Detail"], [
            ["Publishing deal", "Grants a publisher rights to a composition in exchange for royalty share"],
        ]),
    },
    "music-c2-l54": {
        "data_table": table(["Task", "Purpose"], [
            ["Live sound mixing", "Balances levels in real time to suit the performance venue"],
        ]),
    },
    "music-c2-l55": {
        "data_table": table(["Skill", "Purpose"], [
            ["Rehearsal leadership", "Efficiently identifies and addresses ensemble issues within limited time"],
        ]),
    },
    "music-c2-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Deliberate practice", "Targets specific weaknesses with focused, structured repetition"],
        ]),
    },
    "music-c2-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Schenkerian analysis", "Reduces a piece to underlying structural voice-leading layers"],
        ]),
    },
    "music-c2-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Percussion ensemble writing", "Balances pitched and unpitched instruments across independent rhythmic parts"],
        ]),
    },
    "music-c2-l59": {
        "data_table": table(["Technique", "Purpose"], [
            ["Leitmotif", "A recurring musical theme associated with a character or idea in film/game scoring"],
        ]),
    },
    "music-c2-l60": {
        "data_table": table(["Factor", "Detail"], [
            ["Sustainable music career", "Combines performance, teaching, and diversified income streams"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Roman Numeral", "Chord Function"], [
    ["I", "Tonic"], ["IV", "Subdominant"], ["V", "Dominant"],
])

# l61-l63 "Foundations 2" lessons revisit l23, l24, and l6.
FOUNDATIONS_2_MAP = {61: 23, 62: 24, 63: 6}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"music-c2-l{base_n}"
    CHARTS[f"music-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l64-l70 "Worked Analysis" lessons reuse the data_table of l1-l7
# (l69 revisits l6, matching the "Foundations" lesson title it echoes).
WORKED_ANALYSIS_MAP = {64: 1, 65: 2, 66: 3, 67: 4, 68: 5, 69: 6, 70: 7}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"music-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"music-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"music-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Music lessons (completing 70/70).")


if __name__ == "__main__":
    main()
