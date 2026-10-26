#!/usr/bin/env python3
"""Depth pass, M2 Music: fill in real, hand-checked data_table
content for the M2 Music lessons not covered by the earlier
breadth-first batch. Brings M2 Music to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
compositional theory and analysis, music technology/computer music,
music cognition and psychoacoustics, ethnomusicology, historical
performance/notation, and the music business/therapy fields;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_music_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Spectralism", "A compositional movement that treats a sound's timbral spectrum as the basis for musical structure"],
    ["Timbre as structure", "Uses the analysis of overtones and sound color to generate harmonic and formal material"],
])

CHARTS: dict[str, dict] = {
    "music-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Music technology & composition research", "Systematic methods integrating digital tools into compositional research"],
    ])},
    "music-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Music theory fundamentals research", "Rigorous scholarly grounding in the principles underlying tonal and post-tonal music"],
    ])},
    "music-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Schenkerian analysis", "Reduces a tonal piece to underlying structural voice-leading layers"],
    ])},
    "music-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Pitch-class set theory", "Analyzes atonal music by categorizing collections of pitches independent of octave or order"],
    ])},
    "music-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Total serialism", "Extends serial technique beyond pitch to organize rhythm, dynamics, and timbre systematically"],
    ])},
    "music-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Sound mass composition", "Treats dense clusters of sound as a single evolving textural entity rather than discrete pitches"],
    ])},
    "music-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Just intonation", "A tuning system using pure mathematical frequency ratios rather than equal temperament"],
    ])},
    "music-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Neoclassicism (Schenkerian view)", "Applies structural voice-leading analysis to 20th-century music referencing older forms"],
    ])},
    "music-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Neo-Riemannian theory", "Analyzes chromatic harmony through transformations (like parallel, relative) between triads"],
    ])},
    "music-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic composition", "Uses computational rules or systems to generate musical material"],
    ])},
    "music-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Live electronics", "Real-time processing of sound signals during a live musical performance"],
    ])},
    "music-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Acousmatic music", "Music heard without seeing its sound source, emphasizing reduced, purely aural listening"],
    ])},
    "music-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Soundscape composition", "Uses recorded environmental sound as compositional material, rooted in acoustic ecology"],
    ])},
    "music-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Historically informed performance", "Researches period instruments and techniques to perform music as originally intended"],
    ])},
    "music-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Medieval musical notation", "Studies the early symbolic systems used to record pitch and rhythm before modern notation"],
    ])},
    "music-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Mensural notation", "A Renaissance notation system encoding proportional rhythmic relationships"],
    ])},
    "music-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Computational musicology", "Uses computational methods to analyze large corpora of musical scores"],
    ])},
    "music-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Automatic music transcription", "Software that converts recorded audio directly into notated musical scores"],
    ])},
    "music-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Auditory scene analysis", "Models how listeners perceptually separate overlapping sounds into distinct streams"],
    ])},
    "music-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Consonance/roughness", "Psychoacoustic models explaining why certain intervals sound smooth or rough together"],
    ])},
    "music-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Musical expectation (statistical learning)", "Models how listeners form and violate predictions about upcoming musical events"],
    ])},
    "music-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Embodied musical cognition", "Studies how physical gesture and bodily experience shape musical understanding"],
    ])},
    "music-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Critical organology", "Studies musical instrument design as embedded with cultural and social meaning"],
    ])},
    "music-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Ethnomusicological fieldwork ethics", "Establishes responsible research practices for studying living musical traditions"],
    ])},
    "music-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Raga theory", "The system of melodic frameworks and improvisational grammar in Hindustani classical music"],
    ])},
    "music-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Maqam theory", "The system of melodic modes underlying improvisation in Arabic classical music"],
    ])},
    "music-m2-l28": {"data_table": table(["Tuning", "Feature"], [
        ["Slendro", "A five-tone gamelan tuning system with roughly equal intervals"],
        ["Pelog", "A seven-tone gamelan tuning system with uneven intervals"],
    ])},
    "music-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Transcription of non-notated traditions", "Methods for analytically documenting orally transmitted musical practices"],
    ])},
    "music-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Groove and micro-timing", "Analyzes the subtle rhythmic deviations that give popular music its feel"],
    ])},
    "music-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Reharmonization", "Jazz technique of substituting alternate chords for a melody's original harmony"],
    ])},
    "music-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Improvisation cognition", "Models the real-time cognitive processes underlying spontaneous musical creativity"],
    ])},
    "music-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Leitmotif", "A recurring musical theme associated with a character or idea in film scoring"],
    ])},
    "music-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive video game scoring", "Music systems that dynamically respond and generate based on in-game player actions"],
    ])},
    "music-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Music and multimedia semiotics", "Studies how musical signs carry meaning within combined audio-visual media"],
    ])},
    "music-m2-l36": {"data_table": table(["Scholar", "Claim"], [
        ["Adorno", "Critiqued popular music as standardized and pacifying under the culture industry"],
    ])},
    "music-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["New musicology", "A movement critically examining how the classical canon was historically formed and by whom"],
    ])},
    "music-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Feminist musicology", "Examines gender's role in musical composition, performance, and critical discourse"],
    ])},
    "music-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Disability studies and music theory", "Examines how disability shapes and is represented within musical structures and discourse"],
    ])},
    "music-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Postcolonial music history", "Reexamines music historiography through the lens of colonial power relations"],
    ])},
    "music-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Sound studies", "Examines the politics and culture of listening as a broader field than music alone"],
    ])},
    "music-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Sampling copyright law", "Legal frameworks governing the reuse of recorded audio in new digital compositions"],
    ])},
    "music-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Statistical learning of tonal hierarchies", "Models how listeners implicitly learn a key's structure from exposure to music"],
    ])},
    "music-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Absolute pitch", "The rare ability to identify a musical note's pitch without a reference tone, studied cognitively"],
    ])},
    "music-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Probabilistic harmonic grammar", "Computational models predicting likely chord progressions using statistical rules"],
    ])},
    "music-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Deep learning for symbolic music", "Neural network architectures trained to generate notated musical sequences"],
    ])},
    "music-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Multidimensional timbre scaling", "Statistical models mapping how listeners perceive differences between instrument sounds"],
    ])},
    "music-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Spectral envelope", "The overall shape of a sound's frequency content, key to synthesizing realistic timbre"],
    ])},
    "music-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Granular synthesis", "Builds sound from thousands of tiny audio grains, enabling microsound composition"],
    ])},
    "music-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Ambisonics", "A full-sphere spatial audio format used for immersive contemporary composition"],
    ])},
    "music-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Networked music performance", "Compensates for network latency to enable musicians to perform together remotely"],
    ])},
    "music-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Euclidean rhythm", "An algorithm distributing beats as evenly as possible, generating many world music rhythms"],
    ])},
    "music-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Metrical dissonance", "A conflict between the notated meter and the rhythmic groupings a listener perceives"],
    ])},
    "music-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Hypermeter", "Large-scale rhythmic organization grouping measures into higher-level metrical units"],
    ])},
    "music-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Sonata theory", "A modern theoretical reconsideration of the sonata form's structural conventions"],
    ])},
    "music-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Formenlehre", "A theory analyzing musical form through recurring formal functions rather than fixed templates"],
    ])},
    "music-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Post-serial formal structure", "Analyzes how form is organized in music that extends beyond strict serialism"],
    ])},
    "music-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Opera dramaturgy", "Examines how music characterizes and drives narrative in operatic works"],
    ])},
    "music-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Vocal pedagogy (physiology)", "Studies the physiological mechanisms underlying healthy singing technique"],
    ])},
    "music-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Conducting gesture and ictus", "Analyzes the precise physical gestures conductors use to communicate timing to an ensemble"],
    ])},
    "music-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Orchestration analysis", "Studies how composers blend and contrast instrumental timbres"],
    ])},
    "music-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Chamber music interpretation", "Examines the collaborative decisions ensembles make in interpreting a shared score"],
    ])},
    "music-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Urtext scholarship", "Critical editing that aims to recover a composer's original intended text"],
    ])},
    "music-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Music archival preservation", "Digital humanities methods for preserving and cataloging historical musical documents"],
    ])},
    "music-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Reception history", "Studies how a musical work's status and interpretation changed across different eras"],
    ])},
    "music-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Patronage systems", "Examines how historical funding relationships shaped what music was composed and why"],
    ])},
    "music-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Music theory pedagogy", "Researches curriculum design and assessment methods for teaching music theory"],
    ])},
    "music-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Music therapy research methods", "Studies clinical outcome measures for evaluating therapeutic music interventions"],
    ])},
    "music-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Neurologic music therapy", "Uses rhythm and music to support motor rehabilitation after neurological injury"],
    ])},
    "music-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Music and memory (clinical)", "Clinical applications of music to support cognition in neurodegenerative disease"],
    ])},
    "music-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Streaming economics", "Analyzes how streaming platform payment structures affect musician revenue"],
    ])},
    "music-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["IP strategy (composers/producers)", "Strategic management of intellectual property rights for music creators"],
    ])},
    "music-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Physical modeling synthesis", "Simulates an instrument's actual physical vibration behavior to generate its sound digitally"],
    ])},
    "music-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Automatic genre classification", "Machine listening systems that categorize music by genre from audio features"],
    ])},
    "music-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Process music analysis", "Studies minimalist compositions built by unfolding a defined generative process"],
    ])},
    "music-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Non-Western polyphony", "Analyzes multi-voiced vocal traditions outside the Western classical canon"],
    ])},
    "music-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Notation reform historiography", "Traces historical movements attempting to redesign standard music notation"],
    ])},
    "music-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Musical borrowing/intertextuality", "Theorizes how composers quote, reference, and rework prior musical material"],
    ])},
    "music-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Species counterpoint critique", "Reassesses the traditional Fuxian pedagogical method for teaching counterpoint"],
    ])},
    "music-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Twelve-tone combinatoriality", "Analyzes how twelve-tone rows can be combined to form new complete aggregates"],
    ])},
    "music-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Minimalist/spectral rhythm", "Examines rhythmic organization distinct to minimalist and spectral compositional styles"],
    ])},
    "music-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Aleatoric/indeterminate composition", "Music that deliberately incorporates chance or performer choice into its outcome"],
    ])},
    "music-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Tuning and temperament history", "Compares how different cultures historically structured pitch systems"],
    ])},
    "music-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Orchestral score reduction/analysis", "Advanced study reducing complex orchestral scores for deep structural understanding"],
    ])},
    "music-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Musical topics/program music semiotics", "Studies conventional musical gestures that signify extra-musical meaning"],
    ])},
    "music-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora and genre formation", "Examines how migration has shaped the historical development of musical genres"],
    ])},
    "music-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Choral conducting repertoire analysis", "Advanced study of choral works for conducting interpretation"],
    ])},
    "music-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Sound installation art", "Composes sonic works designed for a specific physical exhibition space"],
    ])},
    "music-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Extended tertian jazz voice leading", "Studies how complex extended chords connect smoothly in jazz harmony"],
    ])},
    "music-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Metric modulation", "A technique smoothly transitioning tempo by reinterpreting a rhythmic subdivision as the new pulse"],
    ])},
    "music-m2-l91": {"data_table": table(["Tuning", "Feature"], [
        ["Meantone", "Prioritizes pure thirds at the expense of some fifths"],
        ["Well-temperament", "Balances all keys as usably in-tune, unlike strict meantone"],
    ])},
    "music-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Fugue stretto/augmentation", "Advanced contrapuntal techniques overlapping or lengthening a fugue subject"],
    ])},
    "music-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Machine co-improvisation", "Interactive systems where software improvises music alongside human performers in real time"],
    ])},
    "music-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Recording technology historiography", "Traces how recording technology has shaped how music is interpreted and performed"],
    ])},
    "music-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Harmonic tension and release", "Formal models quantifying perceived musical tension across a harmonic progression"],
    ])},
    "music-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Isorhythmic motet", "A medieval structural technique repeating a fixed rhythmic pattern across changing pitches"],
    ])},
    "music-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Zoomusicology", "Studies the structure of animal sounds using musical analytical frameworks"],
    ])},
    "music-m2-l98": {"data_table": table(["Component", "Purpose"], [
        ["Thesis research seminar", "Presents and defends original research toward a master's thesis in music scholarship or composition"],
    ])},
    "music-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic voice-leading analysis", "Computationally analyzes voice-leading patterns across large corpora of common-practice music"],
    ])},
    "music-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Turntablism", "Uses the turntable itself as a live instrument for compositional and performative practice"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"music-m2-l{base_n}"
    worked_key = f"music-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Music"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Music: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Music lessons.")


if __name__ == "__main__":
    main()
