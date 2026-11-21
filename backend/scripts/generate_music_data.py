#!/usr/bin/env python3
"""Generate backend/data/music_instruments/music.json for the Music & Instruments section.

Re-run after editing the data below:
    python3 backend/scripts/generate_music_data.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "data" / "music_instruments"
OUT_PATH = OUT_DIR / "music.json"


def yt(query: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(query)


def pinterest(query: str) -> str:
    return "https://www.pinterest.com/search/pins/?q=" + quote_plus(query)


def wiki(topic: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(topic).replace("+", "_")


MUSICTHEORY_NET = "https://www.musictheory.net/"
EIGHT_NOTES = "https://www.8notes.com/"
IMSLP = "https://imslp.org/"


CATEGORIES = {
    "music_theory": {
        "label": "Music Theory",
        "emoji": "🎼",
        "description": "Notes, scales, key signatures, chords, and harmony — the building blocks that let you read and understand any piece of music.",
        "resources": [
            {"title": "Music Theory — free interactive lessons & exercises", "url": MUSICTHEORY_NET},
            {"title": "Music theory overview (Wikipedia)", "url": wiki("Music theory")},
            {"title": "Music theory crash course playlists", "url": yt("music theory crash course full playlist")},
        ],
        "topics": ["Staff, clefs & note names", "Scales & key signatures", "Intervals", "Chords & triads", "Chord progressions", "Harmony & voice leading"],
    },
    "singing_vocal_training": {
        "label": "Singing & Vocal Training",
        "emoji": "🎤",
        "description": "Breath support, pitch control, tone, and vocal health for anyone who wants to sing better, from first-timers to trained vocalists.",
        "resources": [
            {"title": "Vocal warm-up and technique videos", "url": yt("vocal warm up exercises for beginners")},
            {"title": "Singing technique overview (Wikipedia)", "url": wiki("Singing")},
            {"title": "Vocal health and care", "url": yt("vocal health tips for singers")},
        ],
        "topics": ["Breath support", "Pitch matching", "Vocal warm-ups", "Tone & resonance", "Vocal registers (chest/head/mix)", "Performance technique"],
    },
    "rhythm_ear_training": {
        "label": "Rhythm & Ear Training",
        "emoji": "🥁",
        "description": "Training your internal sense of time and pitch — the skill that lets musicians play together, improvise, and learn music by ear.",
        "resources": [
            {"title": "Ear training exercises", "url": MUSICTHEORY_NET + "exercises.php"},
            {"title": "Rhythm and ear training drills", "url": yt("rhythm training exercises for musicians")},
            {"title": "Ear training overview (Wikipedia)", "url": wiki("Ear training")},
        ],
        "topics": ["Steady beat & subdivision", "Time signatures", "Clapping & counting rhythms", "Interval recognition", "Chord quality recognition", "Transcribing simple melodies by ear"],
    },
    "world_music": {
        "label": "World Music",
        "emoji": "🌍",
        "description": "Explore musical traditions from around the globe — from Indian classical ragas to West African percussion and Latin American rhythms.",
        "resources": [
            {"title": "World music traditions overview (Wikipedia)", "url": wiki("World music")},
            {"title": "World music documentaries and performances", "url": yt("world music traditions documentary")},
        ],
        "topics": ["Indian classical music (Hindustani & Carnatic)", "African percussion traditions", "Latin American rhythms", "Middle Eastern maqam", "East Asian traditional music", "Folk music traditions worldwide"],
    },
    "classical_music": {
        "label": "Classical Music",
        "emoji": "🎻",
        "description": "The Western classical tradition, from Baroque counterpoint to Romantic symphonies — essential listening and theory for any serious musician.",
        "resources": [
            {"title": "Free public-domain classical sheet music (IMSLP)", "url": IMSLP},
            {"title": "Classical music eras overview (Wikipedia)", "url": wiki("Classical music")},
            {"title": "Classical music masterworks playlists", "url": yt("classical music masterpieces full playlist")},
        ],
        "topics": ["Baroque period", "Classical period (Mozart, Haydn)", "Romantic period", "20th-century & modern classical", "Orchestration basics", "Sonata form & symphonic structure"],
    },
    "modern_production": {
        "label": "Modern Music Production",
        "emoji": "🎧",
        "description": "Recording, mixing, and producing music with modern digital tools — DAWs, beat-making, mixing, and mastering basics.",
        "resources": [
            {"title": "Music production for beginners", "url": yt("music production tutorial for beginners DAW")},
            {"title": "Digital audio workstation overview (Wikipedia)", "url": wiki("Digital audio workstation")},
            {"title": "Mixing and mastering basics", "url": yt("mixing and mastering basics tutorial")},
        ],
        "topics": ["Intro to DAWs (Digital Audio Workstations)", "Recording basics", "Beat-making & sequencing", "Mixing fundamentals", "Mastering basics", "Sound design & synthesis"],
    },
}


def _instrument(label: str, emoji: str, beginner_topics: list[str], intermediate_topics: list[str], advanced_topics: list[str], routines: list[str]) -> dict:
    def _lessons(topics: list[str], stage: str) -> list[dict]:
        return [
            {
                "title": topic,
                "description": f"{stage.title()} {label.lower()} lesson: {topic.lower()}.",
                "youtube_search_url": yt(f"{label} {topic} lesson {stage}"),
            }
            for topic in topics
        ]

    return {
        "label": label,
        "emoji": emoji,
        "beginner": _lessons(beginner_topics, "beginner"),
        "intermediate": _lessons(intermediate_topics, "intermediate"),
        "advanced": _lessons(advanced_topics, "advanced"),
        "practice_routines": routines,
        "youtube_searches": [
            {"title": f"{label} lessons for beginners", "url": yt(f"{label} lessons for beginners")},
            {"title": f"{label} practice routine", "url": yt(f"{label} daily practice routine")},
            {"title": f"{label} advanced technique", "url": yt(f"{label} advanced technique masterclass")},
        ],
        "audio_resources": [
            {"title": f"{label} sheet music / tabs", "url": EIGHT_NOTES},
            {"title": f"{label} overview (Wikipedia)", "url": wiki(label)},
        ],
        "pinterest_search": pinterest(f"{label} lessons chart chords diagram"),
    }


INSTRUMENTS = {
    "piano": _instrument(
        "Piano", "🎹",
        ["Hand position & posture", "Reading treble & bass clef", "Simple five-finger melodies"],
        ["Major & minor scales", "Basic chords & triads", "Two-hand coordination pieces"],
        ["Arpeggios & inversions", "Sight-reading intermediate repertoire"],
        ["15 min scales/technique, 15 min sight-reading, 15 min repertoire, 5 min improvisation daily.",
         "Weekly: alternate technical drills with learning one new short piece."],
    ),
    "guitar": _instrument(
        "Guitar", "🎸",
        ["Holding the guitar & basic posture", "Open chords (E, A, D, G, C)", "Simple strumming patterns"],
        ["Barre chords", "Fingerpicking patterns", "Basic scales (pentatonic)"],
        ["Lead guitar improvisation", "Advanced strumming & rhythm techniques"],
        ["10 min chord changes, 10 min strumming, 10 min scales, 10 min playing a song daily.",
         "Weekly: learn one new song and one new technique exercise."],
    ),
    "violin": _instrument(
        "Violin", "🎻",
        ["Holding the violin & bow", "First position notes on all four strings", "Simple bowing exercises"],
        ["Scales in first position", "Vibrato introduction", "Shifting to third position"],
        ["Advanced bowing techniques", "Double stops & advanced repertoire"],
        ["10 min bowing exercises, 10 min scales, 10 min repertoire, 10 min intonation practice daily.",
         "Weekly: record yourself and compare intonation against a tuner."],
    ),
    "drums": _instrument(
        "Drums", "🥁",
        ["Drum kit setup & grip", "Basic rock beat", "Simple fills"],
        ["Rudiments (paradiddles, flams)", "Time signature variety (3/4, 6/8)", "Independence exercises"],
        ["Odd-meter grooves", "Advanced soloing & polyrhythms"],
        ["10 min rudiments, 10 min metronome grooves, 10 min fills, 10 min song play-along daily.",
         "Weekly: increase metronome tempo gradually for one groove."],
    ),
    "flute": _instrument(
        "Flute", "🪈",
        ["Embouchure & tone production", "First octave notes", "Simple breathing exercises"],
        ["Second & third octave notes", "Basic scales", "Articulation (tonguing)"],
        ["Advanced repertoire & vibrato", "Extended techniques"],
        ["10 min long tones, 10 min scales, 10 min articulation, 10 min repertoire daily.",
         "Weekly: work on breath control with long-tone endurance drills."],
    ),
    "saxophone": _instrument(
        "Saxophone", "🎷",
        ["Embouchure & reed care", "First notes & basic fingerings", "Simple long tones"],
        ["Major scales", "Basic jazz articulation", "Register key & altissimo intro"],
        ["Improvisation over changes", "Advanced jazz vocabulary & altissimo"],
        ["10 min long tones, 10 min scales, 10 min transcription, 10 min improvisation daily.",
         "Weekly: transcribe one short solo phrase by ear."],
    ),
    "tabla": _instrument(
        "Tabla", "🪘",
        ["Basic strokes (na, tin, ta)", "Teental (16-beat cycle) basics", "Hand posture & tuning"],
        ["Kaida compositions", "Laya (tempo) practice with a metronome", "Additional talas (Jhaptaal, Rupak)"],
        ["Advanced compositions (relas, tukdas)", "Solo performance & accompaniment technique"],
        ["10 min stroke practice, 10 min theka cycles, 10 min compositions, 10 min tempo drills daily.",
         "Weekly: practice accompanying a recorded vocal or instrumental piece."],
    ),
    "sitar": _instrument(
        "Sitar", "🪕",
        ["Sitting posture & holding the sitar", "Basic mizrab (plectrum) strokes", "Tuning basics"],
        ["Introductory ragas", "Basic alankaras (melodic patterns)", "Meend (glides) technique"],
        ["Advanced raga improvisation", "Jhala & fast passages"],
        ["10 min tuning & sound, 10 min alankaras, 10 min raga practice, 10 min improvisation daily.",
         "Weekly: focus on one raga in depth, exploring its mood and phrases."],
    ),
    "harmonium": _instrument(
        "Harmonium", "🪗",
        ["Bellows technique & posture", "Basic scale (sargam) practice", "Simple accompaniment patterns"],
        ["Raga-based melodies", "Accompanying vocal exercises", "Ornamentation basics"],
        ["Advanced raga repertoire", "Complex accompaniment for classical vocal performance"],
        ["10 min bellows control, 10 min sargam, 10 min raga phrases, 10 min accompaniment practice daily.",
         "Weekly: accompany a singer or recording to build ensemble timing."],
    ),
    "keyboard": _instrument(
        "Keyboard", "🎹",
        ["Basic hand position & keys", "Simple chords & backing patterns", "Using built-in rhythms/sounds"],
        ["Chord inversions & voicings", "Layering sounds & split keyboards", "Playing along with backing tracks"],
        ["Live performance arranging", "Advanced chord voicings & improvisation"],
        ["15 min technique, 15 min chords, 15 min playing songs, 5 min improvisation daily.",
         "Weekly: arrange one song using keyboard backing styles."],
    ),
    "voice_singing": _instrument(
        "Voice / Singing", "🎙️",
        ["Posture & breath support", "Pitch matching exercises", "Simple warm-up scales"],
        ["Vocal range extension", "Basic harmony singing", "Diction & phrasing"],
        ["Advanced vocal runs & control", "Genre-specific styling (jazz, pop, classical)"],
        ["10 min breathing, 10 min warm-ups, 10 min range exercises, 10 min song practice daily.",
         "Weekly: record and review one song to track vocal progress."],
    ),
}


def build() -> dict:
    for key, category in CATEGORIES.items():
        category.setdefault("resources", []).append({
            "title": f"{category['label']} — Pinterest boards",
            "url": pinterest(f"{category['label']} music"),
        })

    return {
        "title": "Music & Instruments",
        "description": (
            "A dedicated home for musical learning at every age and level: instrument lessons, music theory, "
            "singing and vocal training, rhythm and ear training, world and classical music traditions, and "
            "modern music production — with curated links to legitimate YouTube, Pinterest, and audio resources "
            "rather than embedded copyrighted media."
        ),
        "categories": CATEGORIES,
        "instruments": INSTRUMENTS,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(build(), f, indent=2, ensure_ascii=False)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
