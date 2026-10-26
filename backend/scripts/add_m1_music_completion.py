#!/usr/bin/env python3
"""Depth pass, M1 Music: fill in real, hand-checked data_table content
for the 99 M1 Music lessons not covered by the earlier breadth-first
batch. Brings M1 Music to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "music-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Performance & ear training", "Builds recognition of intervals, chords, and rhythm through active listening"],
        ]),
    },
    "music-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Music technology & composition", "Integrates digital tools directly into the compositional process"],
        ]),
    },
    "music-m1-l4": {
        "data_table": table(["Skill", "Detail"], [
            ["Advanced aural skills", "Rapid, accurate identification of complex harmonic and rhythmic material by ear"],
        ]),
    },
    "music-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Historiography of Western music", "Examines how musical narratives themselves have been constructed over time"],
        ]),
    },
    "music-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative world music systems", "Analyzes tuning, rhythm, and form across distinct global musical traditions"],
        ]),
    },
    "music-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced jazz analysis", "Examines harmonic substitution and voice leading within jazz repertoire"],
        ]),
    },
    "music-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced composition technique", "Develops sophisticated structural and harmonic tools for original works"],
        ]),
    },
    "music-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Orchestration analysis", "Studies how composers combine instrumental timbres for expressive effect"],
        ]),
    },
    "music-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced music production", "Applies professional-level recording and mixing techniques to original work"],
        ]),
    },
    "music-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Music industry strategy", "Navigates distribution, branding, and revenue models for a music career"],
        ]),
    },
    "music-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethnomusicological theory", "Provides frameworks for studying music within its cultural context"],
        ]),
    },
    "music-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced film scoring", "Synchronizes musical cues precisely with narrative and emotional timing"],
        ]),
    },
    "music-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Emerging music technology", "Explores new tools reshaping composition, performance, and production"],
        ]),
    },
    "music-m1-l15": {
        "data_table": table(["Skill", "Detail"], [
            ["Conducting interpretation", "Shapes tempo, dynamics, and phrasing decisions from score analysis"],
        ]),
    },
    "music-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced vocal pedagogy", "Teaches breath support, resonance, and healthy technique at a professional level"],
        ]),
    },
    "music-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Philosophy of music education", "Examines the underlying values and goals shaping how music is taught"],
        ]),
    },
    "music-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Popular music criticism", "Applies rigorous analytical frameworks to commercially popular musical forms"],
        ]),
    },
    "music-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Music, politics, and society", "Examines music's role in shaping and reflecting political and social movements"],
        ]),
    },
    "music-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Graduate thesis project", "Culminates study in an original composition or performance body of work"],
        ]),
    },
    "music-m1-l21": {
        "data_table": table(["Method", "Purpose"], [
            ["Schenkerian analysis", "Reduces a piece to underlying structural voice-leading layers"],
        ]),
    },
    "music-m1-l22": {
        "data_table": table(["Method", "Purpose"], [
            ["Pitch-class set theory", "Analyzes atonal music through interval relationships rather than tonal function"],
        ]),
    },
    "music-m1-l23": {
        "data_table": table(["Technique", "Detail"], [
            ["Spectral composition", "Derives musical material from the acoustic properties of sound spectra"],
        ]),
    },
    "music-m1-l24": {
        "data_table": table(["Technique", "Detail"], [
            ["Twelve-tone serialism", "Organizes pitch using a fixed ordering of all twelve chromatic tones"],
        ]),
    },
    "music-m1-l25": {
        "data_table": table(["Technique", "Detail"], [
            ["Process-based composition", "Builds music from a defined, gradually unfolding compositional procedure"],
        ]),
    },
    "music-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Metric dissonance", "Rhythmic patterns conflict with the established underlying meter"],
        ]),
    },
    "music-m1-l27": {
        "data_table": table(["Theory", "Detail"], [
            ["Neo-Riemannian theory", "Analyzes chord relationships through voice-leading transformations rather than function"],
        ]),
    },
    "music-m1-l28": {
        "data_table": table(["Section", "Function"], [
            ["Exposition", "Presents primary and secondary thematic material"],
            ["Development", "Explores and transforms thematic material"],
        ]),
    },
    "music-m1-l29": {
        "data_table": table(["Element", "Function"], [
            ["Subject", "The main melodic idea introduced at the start of a fugue"],
            ["Countersubject", "A secondary theme paired against the subject"],
        ]),
    },
    "music-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Basso continuo", "A harmonic bass line realized improvisationally by a keyboard/continuo player"],
        ]),
    },
    "music-m1-l31": {
        "data_table": table(["Convention", "Detail"], [
            ["Classical-era form", "Standardized structures like sonata and rondo form organized musical logic"],
        ]),
    },
    "music-m1-l32": {
        "data_table": table(["Feature", "Detail"], [
            ["Romantic harmonic innovation", "Expanded chromaticism and tonal ambiguity beyond Classical convention"],
        ]),
    },
    "music-m1-l33": {
        "data_table": table(["Innovation", "Detail"], [
            ["20th-century notation", "Composers devised new symbols to represent extended and unconventional techniques"],
        ]),
    },
    "music-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Aleatoric composition", "Deliberately introduces chance elements into musical structure or performance"],
        ]),
    },
    "music-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Electroacoustic music", "Combines acoustic sound sources with electronic processing and manipulation"],
        ]),
    },
    "music-m1-l36": {
        "data_table": table(["Technique", "Detail"], [
            ["Additive synthesis", "Builds complex timbre by combining simple sine wave components"],
            ["Subtractive synthesis", "Shapes a rich source waveform by filtering out frequencies"],
        ]),
    },
    "music-m1-l37": {
        "data_table": table(["Technique", "Detail"], [
            ["Granular synthesis", "Assembles sound from many tiny fragments (grains) of audio"],
        ]),
    },
    "music-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital signal processing", "Manipulates audio signals mathematically for effects and analysis"],
        ]),
    },
    "music-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Tonal hierarchy expectation", "Listeners develop implicit expectations about which pitches are structurally central"],
        ]),
    },
    "music-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational music analysis", "Uses algorithmic methods to identify patterns in musical scores or audio"],
        ]),
    },
    "music-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Music information retrieval", "Extracts structured information like tempo or key from raw audio data"],
        ]),
    },
    "music-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Algorithmic composition", "Uses defined rules or procedures to generate musical material"],
        ]),
    },
    "music-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Machine learning music generation", "Trains models on musical data to generate new, stylistically consistent material"],
        ]),
    },
    "music-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Music and emotion", "Studies how musical structure elicits predictable emotional response in listeners"],
        ]),
    },
    "music-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Timbral blending", "Combines instrumental colors to create a unified or contrasting orchestral texture"],
        ]),
    },
    "music-m1-l46": {
        "data_table": table(["Technique", "Purpose"], [
            ["Leitmotif", "A recurring musical theme associated with a character or idea in film scoring"],
        ]),
    },
    "music-m1-l47": {
        "data_table": table(["Era", "Feature"], [
            ["Film scoring history", "Evolved from live orchestral accompaniment to fully synchronized recorded scores"],
        ]),
    },
    "music-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Adaptive game music", "Dynamically responds to player action rather than following a fixed linear track"],
        ]),
    },
    "music-m1-l49": {
        "data_table": table(["Method", "Purpose"], [
            ["Ethnomusicological fieldwork", "Documents music within its cultural and social context"],
        ]),
    },
    "music-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative rhythmic systems", "Different traditions organize time using distinct metric and cyclic structures"],
        ]),
    },
    "music-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Gamelan theory", "Interlocking parts on tuned metallophones structure Indonesian ensemble music"],
        ]),
    },
    "music-m1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Raga", "A melodic framework guiding improvisation in Hindustani classical music"],
        ]),
    },
    "music-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Carnatic theory", "South Indian classical tradition with its own distinct raga and tala systems"],
        ]),
    },
    "music-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["West African polyrhythm", "Layers multiple independent rhythmic patterns simultaneously"],
        ]),
    },
    "music-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Blues/jazz harmonic language", "Built on extended and altered chords beyond simple triads"],
        ]),
    },
    "music-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Jazz improvisation theory", "Structures spontaneous melodic invention over a given harmonic progression"],
        ]),
    },
    "music-m1-l57": {
        "data_table": table(["Feature", "Detail"], [
            ["Bebop vocabulary", "Fast, chromatic melodic lines built on extended chord tones"],
        ]),
    },
    "music-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Production aesthetics", "Studio choices like compression and layering shape a recording's signature sound"],
        ]),
    },
    "music-m1-l59": {
        "data_table": table(["Model", "Detail"], [
            ["Streaming royalty model", "Compensates artists based on proportional share of total platform streams"],
        ]),
    },
    "music-m1-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Mechanical royalty", "Paid for reproducing a composition, e.g. on a recording"],
            ["Performance royalty", "Paid for public performance or broadcast of a work"],
        ]),
    },
    "music-m1-l61": {
        "data_table": table(["Movement", "Feature"], [
            ["Protest song tradition", "Uses accessible melody and lyrics to advance social and political causes"],
        ]),
    },
    "music-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Gender in music scholarship", "Examines how gender has shaped composition, performance, and reception"],
        ]),
    },
    "music-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Postcolonial music historiography", "Reframes music history beyond a single dominant cultural narrative"],
        ]),
    },
    "music-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Music therapy", "Uses structured musical intervention for clinical therapeutic goals"],
        ]),
    },
    "music-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Neurologic music therapy", "Applies music-based techniques to support neurological rehabilitation"],
        ]),
    },
    "music-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Curriculum design theory", "Sequences musical learning objectives to build skills progressively"],
        ]),
    },
    "music-m1-l67": {
        "data_table": table(["Method", "Focus"], [
            ["Kodály approach", "Uses solfège and folk song to build musical literacy sequentially"],
            ["Orff approach", "Uses movement and simple instruments for active musical exploration"],
        ]),
    },
    "music-m1-l68": {
        "data_table": table(["Skill", "Purpose"], [
            ["Advanced choral conducting", "Coordinates diction, breath, and blend across a full choral ensemble"],
        ]),
    },
    "music-m1-l69": {
        "data_table": table(["Skill", "Purpose"], [
            ["Advanced instrumental conducting", "Communicates precise technical and expressive intent to an instrumental ensemble"],
        ]),
    },
    "music-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Rehearsal pedagogy", "Efficiently identifies and resolves ensemble issues within limited rehearsal time"],
        ]),
    },
    "music-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Vocal resonance", "Shapes vocal tract acoustics to project and color the singing voice"],
        ]),
    },
    "music-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Vocal injury prevention", "Proper technique and vocal hygiene reduce risk of chronic vocal damage"],
        ]),
    },
    "music-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Technique transfer", "Skills built on one instrument can partially generalize to related instruments"],
        ]),
    },
    "music-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Cross-cultural music perception", "Listeners' musical expectations are shaped by their own cultural exposure"],
        ]),
    },
    "music-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Minimalist process music", "Gradually transforms a simple musical pattern according to an audible process"],
        ]),
    },
    "music-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Music notation software", "Enables precise digital engraving and editing of complex scores"],
        ]),
    },
    "music-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Live coding performance", "Generates music in real time by writing and editing code on stage"],
        ]),
    },
    "music-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial audio", "Positions sound sources three-dimensionally for immersive listening experience"],
        ]),
    },
    "music-m1-l79": {
        "data_table": table(["System", "Feature"], [
            ["Equal temperament", "Divides the octave into equal steps, enabling free modulation between keys"],
            ["Just intonation", "Tunes intervals to pure whole-number frequency ratios"],
        ]),
    },
    "music-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Opera dramaturgy", "Examines how musical structure and stage narrative interact in opera"],
        ]),
    },
    "music-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Music semiotics", "Studies how musical elements come to signify meaning beyond pure sound"],
        ]),
    },
    "music-m1-l82": {
        "data_table": table(["Skill", "Purpose"], [
            ["Music contract negotiation", "Protects an artist's rights and revenue in industry agreements"],
        ]),
    },
    "music-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Sound installation", "Positions audio as a spatial artwork responsive to a specific site"],
        ]),
    },
    "music-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Bioacoustics", "Studies the production and function of sound in animal communication"],
        ]),
    },
    "music-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Historical instrument reconstruction", "Recreates lost instruments to better understand historical performance practice"],
        ]),
    },
    "music-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Music and community healing", "Group musical practice can support collective processing of shared trauma"],
        ]),
    },
    "music-m1-l87": {
        "data_table": table(["Skill", "Purpose"], [
            ["Advanced score analysis", "Prepares a conductor to make informed interpretive decisions before rehearsal"],
        ]),
    },
    "music-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["DAW signal flow", "Traces audio from input through processing chains to final output in software"],
        ]),
    },
    "music-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Mastering", "Final processing stage that ensures consistent, translatable sound across playback systems"],
        ]),
    },
    "music-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Contemporary concert music aesthetics", "Explores current stylistic directions in notated concert composition"],
        ]),
    },
    "music-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Improvisation pedagogy", "Different traditions teach spontaneous musical creation through distinct methods"],
        ]),
    },
    "music-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Early chant performance", "Historical performance practice attempts to recover authentic period vocal style"],
        ]),
    },
    "music-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Hypermeter", "Organizes measures themselves into larger perceived rhythmic groupings"],
        ]),
    },
    "music-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Polytonality", "Simultaneously combines two or more distinct tonal centers"],
        ]),
    },
    "music-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Historiography of music criticism", "Traces how the practice and standards of writing about music have changed"],
        ]),
    },
    "music-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Vocal chamber repertoire", "Small-ensemble vocal works demand distinctive interpretive and technical skills"],
        ]),
    },
    "music-m1-l97": {
        "data_table": table(["System", "Feature"], [
            ["Oktoechos", "An eight-mode system structuring Byzantine chant"],
        ]),
    },
    "music-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Cante jondo", "Deep, emotionally intense flamenco vocal style built on distinctive modal patterns"],
        ]),
    },
    "music-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Makam theory", "Turkish modal system incorporating microtonal pitch inflections"],
        ]),
    },
    "music-m1-l100": {
        "data_table": table(["Tradition", "Feature"], [
            ["Sikuri performance", "Andean panpipe ensembles split melodic lines between interlocking players"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Roman Numeral", "Chord Function"], [
        ["I", "Tonic"], ["IV", "Subdominant"], ["V", "Dominant"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"music-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"music-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"music-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Music lessons (completing 120/120).")


if __name__ == "__main__":
    main()
