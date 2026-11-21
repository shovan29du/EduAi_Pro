#!/usr/bin/env python3
"""Breadth-first pass, Grade 1: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade1.json (Math already covered by add_grade5_math_lesson_charts.py's
sibling add_math_charts_all_levels.py). SubjectLessons.jsx already renders
figure/wiki_title for every lesson in every subject (Phase 1) -- this adds
the missing data_table piece for a solid sample per subject.

Every fact here is real and independently verifiable (continent/ocean size
ranking, CDC sleep-duration guidance, ADA tooth-brushing guidance, real
historical dates, real Sanskrit yoga-pose names, etc.) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "eng-g1-l1": {
        "data_table": table(["Letter", "Sound (example word)"], [
            ["A", "/a/ as in apple"], ["B", "/b/ as in ball"], ["C", "/k/ as in cat"],
            ["D", "/d/ as in dog"], ["E", "/e/ as in egg"], ["F", "/f/ as in fish"],
        ]),
    },
    "english-g1-l9": {
        "data_table": table(["Type", "Letters"], [
            ["Vowels", "A, E, I, O, U"],
            ["Consonants", "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z"],
        ]),
    },
    "english-g1-l20": {
        "data_table": table(["Word", "First Letter", "Alphabetical Position"], [
            ["Apple", "A", "1"], ["Ball", "B", "2"], ["Cat", "C", "3"], ["Dog", "D", "4"],
        ]),
    },
    # ---- Science ----
    "sci-g1-l2": {
        "data_table": table(["Plant Part", "Function"], [
            ["Roots", "Absorb water and nutrients, anchor the plant"],
            ["Stem", "Supports the plant, carries water and nutrients"],
            ["Leaves", "Make food from sunlight (photosynthesis)"],
            ["Flower", "Makes seeds for new plants"],
        ]),
    },
    "science-g1-l14": {
        "data_table": table(["State", "Shape", "Volume", "Example"], [
            ["Solid", "Fixed shape", "Fixed volume", "Ice"],
            ["Liquid", "Takes shape of container", "Fixed volume", "Water"],
            ["Gas", "Fills its container", "No fixed volume", "Steam"],
        ]),
    },
    "science-g1-l7": {
        "data_table": table(["Object", "Fact"], [
            ["The Sun", "A star at the center of our solar system"],
            ["The Moon", "Earth's natural satellite; orbits Earth roughly every 27 days"],
            ["Earth", "The third planet from the Sun"],
        ]),
    },
    # ---- Geography ----
    "geography-g1-l3": {
        "data_table": table(["Direction", "Opposite Direction"], [
            ["North", "South"], ["East", "West"],
        ]),
    },
    "geography-g1-l8": {
        "data_table": table(["Continent", "Rank by Area"], [
            ["Asia", "1 (largest)"], ["Africa", "2"], ["North America", "3"],
            ["South America", "4"], ["Antarctica", "5"], ["Europe", "6"], ["Australia", "7 (smallest)"],
        ]),
    },
    "geography-g1-l7": {
        "data_table": table(["Ocean", "Rank by Size"], [
            ["Pacific Ocean", "1 (largest)"], ["Atlantic Ocean", "2"], ["Indian Ocean", "3"],
            ["Southern Ocean", "4"], ["Arctic Ocean", "5 (smallest)"],
        ]),
    },
    # ---- World History ----
    "world-history-g1-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Great Pyramid of Giza built for", "Pharaoh Khufu"],
            ["Approximate build date", "c. 2560 BCE"],
            ["Location", "Giza, Egypt"],
        ]),
    },
    "world-history-g1-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["First recorded Olympic Games", "776 BCE"],
            ["Location", "Olympia, Greece"],
            ["Held in honor of", "The god Zeus"],
        ]),
    },
    "world-history-g1-l20": {
        "data_table": table(["Event", "When"], [
            ["Ancient Egypt's Old Kingdom begins", "c. 3100 BCE"],
            ["Rome traditionally founded", "753 BCE"],
            ["First recorded Olympic Games", "776 BCE"],
        ]),
    },
    # ---- Islamic Studies ----
    "isl-g1-l1": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty (Sidq)", "Telling the truth"],
            ["Kindness (Rahma)", "Being gentle and caring"],
            ["Gratitude (Shukr)", "Being thankful"],
        ]),
    },
    "islamic-studies-g1-l4": {
        "data_table": table(["Time of Day", "Purpose of the Dua"], [
            ["Morning", "Asking for a good, blessed day"],
            ["Evening", "Giving thanks and asking for a peaceful night"],
        ]),
    },
    "islamic-studies-g1-l10": {
        "data_table": table(["Practice", "Purpose"], [
            ["Washing hands before eating", "Cleanliness before meals"],
            ["Wudu (ablution)", "Washing before prayer"],
            ["Bathing regularly", "Personal hygiene"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g1-l2": {
        "data_table": table(["Fable", "Moral Lesson"], [
            ["The Tortoise and the Hare", "Slow and steady wins the race"],
            ["The Boy Who Cried Wolf", "Lying makes people stop believing you"],
            ["The Ant and the Grasshopper", "Prepare for the future"],
        ]),
    },
    "world-literature-g1-l9": {
        "data_table": table(["Version", "Origin"], [
            ["Rhodopis", "Ancient Egypt/Greece (oldest known recorded version)"],
            ["Ye Xian", "China (Tang dynasty, 9th century)"],
            ["Cendrillon", "France (Charles Perrault, 1697)"],
        ]),
    },
    "world-literature-g1-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"],
            ["Frame narrator", "Scheherazade"],
            ["Famous tales included", "Aladdin, Ali Baba, Sinbad the Sailor"],
        ]),
    },
    # ---- Art ----
    "art-g1-l2": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g1-l19": {
        "data_table": table(["Colour Type", "Colours"], [
            ["Warm", "Red, Orange, Yellow"], ["Cool", "Blue, Green, Purple"],
        ]),
    },
    "art-g1-l14": {
        "data_table": table(["Artist", "Known For"], [
            ["Vincent van Gogh", "The Starry Night"],
            ["Pablo Picasso", "Co-founding Cubism"],
            ["Leonardo da Vinci", "The Mona Lisa"],
        ]),
    },
    # ---- Music ----
    "music-g1-l8": {
        "data_table": table(["Instrument", "How Sound is Made"], [
            ["Violin", "Bowing or plucking strings"],
            ["Guitar", "Plucking or strumming strings"],
            ["Harp", "Plucking strings"],
        ]),
    },
    "music-g1-l9": {
        "data_table": table(["Instrument", "How Sound is Made"], [
            ["Flute", "Blowing across an opening"],
            ["Trumpet", "Buzzing the lips into a mouthpiece"],
            ["Clarinet", "Blowing through a reed"],
        ]),
    },
    "music-g1-l16": {
        "data_table": table(["Orchestra Family", "Example Instruments"], [
            ["Strings", "Violin, Cello, Double Bass"],
            ["Woodwinds", "Flute, Clarinet, Oboe"],
            ["Brass", "Trumpet, Trombone, Tuba"],
            ["Percussion", "Drums, Xylophone, Cymbals"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g1-l2": {
        "data_table": table(["#", "Day"], [
            ["1", "Monday"], ["2", "Tuesday"], ["3", "Wednesday"], ["4", "Thursday"],
            ["5", "Friday"], ["6", "Saturday"], ["7", "Sunday"],
        ]),
    },
    "general-knowledge-g1-l3": {
        "data_table": table(["#", "Month", "Days"], [
            ["1", "January", "31"], ["2", "February", "28 (29 in a leap year)"], ["3", "March", "31"],
            ["4", "April", "30"], ["5", "May", "31"], ["6", "June", "30"], ["7", "July", "31"],
            ["8", "August", "31"], ["9", "September", "30"], ["10", "October", "31"],
            ["11", "November", "30"], ["12", "December", "31"],
        ]),
    },
    "general-knowledge-g1-l20": {
        "data_table": table(["Object", "Fact"], [
            ["Sun", "A star; the center of our solar system"],
            ["Moon", "Orbits Earth; reflects sunlight rather than making its own light"],
            ["Stars", "Distant suns that produce their own light"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g1-l12": {
        "data_table": table(["Category", "Examples"], [
            ["Needs", "Food, water, shelter, clothing"], ["Wants", "Toys, video games, candy"],
        ]),
    },
    "social-studies-g1-l2": {
        "data_table": table(["Rule", "Why It Matters"], [
            ["Raise your hand before speaking", "Keeps the classroom orderly"],
            ["Wait your turn in line", "Fair to everyone"],
            ["Wash hands before eating", "Prevents spreading germs"],
        ]),
    },
    "social-studies-g1-l14": {
        "data_table": table(["Common Map Symbol", "Typical Meaning"], [
            ["Blue line", "River or stream"], ["Green area", "Park or forest"],
            ["Red square", "School or important building"], ["Black line", "Road"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g1-l5": {
        "data_table": table(["Stretch", "Body Part Targeted"], [
            ["Toe touch", "Hamstrings, lower back"], ["Arm circles", "Shoulders"],
            ["Butterfly stretch", "Hips, inner thighs"],
        ]),
    },
    "physical-education-self-defense-g1-l8": {
        "data_table": table(["Phase", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles"],
            ["Cool-down", "Lowers heart rate gradually and helps prevent injury"],
        ]),
    },
    "physical-education-self-defense-g1-l18": {
        "data_table": table(["Yoga Pose", "Sanskrit Name"], [
            ["Tree Pose", "Vrksasana"], ["Downward Dog", "Adho Mukha Svanasana"], ["Cat Pose", "Marjaryasana"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g1-l3": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice a day (morning and night)"],
            ["Brushing time", "About 2 minutes"],
            ["Replace toothbrush", "Every 3 months"],
        ]),
    },
    "hlt-g1-l5": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"],
            ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g1-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
            ["General guidance", "Drink water throughout the day, more when active"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g1-l2": {
        "data_table": table(["Computer Part", "Function"], [
            ["Keyboard", "Used for typing text and commands"],
            ["Mouse", "Used for pointing and clicking"],
            ["Screen (Monitor)", "Displays what the computer is doing"],
        ]),
    },
    "ict-computer-science-g1-l11": {
        "data_table": table(["Step", "Action"], [
            ["1", "Turn on the computer"], ["2", "Open the program"],
            ["3", "Complete the task"], ["4", "Save the work"],
        ]),
    },
    "ict-g1-l1": {
        "data_table": table(["Device Type", "Description"], [
            ["Desktop computer", "Used at a desk, has a separate monitor"],
            ["Laptop", "Portable, all-in-one design"],
            ["Tablet", "Touchscreen, very portable"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    by_id: dict[str, dict] = {}
    for subject in data["subjects"].values():
        for lesson in subject.get("lessons", []):
            by_id[lesson["id"]] = lesson

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 1 lessons (all subjects).")


if __name__ == "__main__":
    main()
