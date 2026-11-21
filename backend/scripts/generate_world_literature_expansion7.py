#!/usr/bin/env python3
"""Final top-up batch for the "World Literature — Global Voices" section.

Fixes an id-assignment bug in expansion scripts 2-6 (ids were assigned by
enumerating ALL candidates including duplicates, so the "next" script's
start index -- based on the *count* of kept books -- collided with ids
already consumed by discarded candidates in earlier runs, causing valid
new titles to be silently rejected). This script assigns ids using a
counter based on the highest existing numeric wl_global_NNN id + 1,
incrementing only for records actually kept, and adds a further batch of
real, distinct titles to close out the requested net +200 new
world-literature works.

Re-run after editing:
    python3 backend/scripts/generate_world_literature_expansion7.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
LIBRARY_PATH = BASE_DIR / "data" / "world_literature" / "library.json"


def gutenberg_search(q: str) -> str:
    return "https://www.gutenberg.org/ebooks/search/?query=" + quote_plus(q)


def open_library_search(q: str) -> str:
    return "https://openlibrary.org/search?q=" + quote_plus(q)


def goodreads_search(q: str) -> str:
    return "https://www.goodreads.com/search?q=" + quote_plus(q)


def wikipedia(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def youtube_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


# (title, author, year, origin, themes) -- re-includes the genuinely new
# (not-yet-present) candidates from batch 6 plus a further top-up batch.
BOOKS = [
    ("Godaan", "Munshi Premchand", "1936", "India", ["Poverty", "Land", "Injustice"]),
    ("Gaban", "Munshi Premchand", "1931", "India", ["Corruption", "Greed"]),
    ("Nirmala", "Munshi Premchand", "1925", "India", ["Marriage", "Gender", "Society"]),
    ("Thanda Gosht", "Saadat Hasan Manto", "1950", "Pakistan/India", ["Partition", "Violence"]),
    ("Lihaaf (The Quilt)", "Ismat Chughtai", "1942", "India", ["Gender", "Sexuality", "Society"]),
    ("The Crooked Line", "Ismat Chughtai", "1944", "India", ["Gender", "Coming of Age"]),
    ("Chandrakanta", "Devaki Nandan Khatri", "1888", "India", ["Adventure", "Romance", "Fantasy"]),
    ("Yayati", "V. S. Khandekar", "1959", "India", ["Desire", "Morality", "Mythology"]),
    ("Kayar", "Thakazhi Sivasankara Pillai", "1978", "India", ["Land", "Society", "Change"]),
    ("Ponniyin Selvan", "Kalki Krishnamurthy", "1955", "India", ["History", "Empire", "Adventure"]),
    ("Sivakamiyin Sabatham", "Kalki Krishnamurthy", "1944", "India", ["History", "Art", "Love"]),
    ("Karukku", "Bama", "1992", "India", ["Caste", "Identity", "Testimony"]),
    ("Yashodhara", "Maithili Sharan Gupt", "1932", "India", ["Devotion", "Renunciation"]),
    ("Kanthapura", "Raja Rao", "1938", "India", ["Independence Movement", "Village Life"]),
    ("The Serpent and the Rope", "Raja Rao", "1960", "India", ["Philosophy", "Identity"]),
    ("Samskara", "U. R. Ananthamurthy", "1965", "India", ["Caste", "Ritual", "Morality"]),
    ("Aavarana", "S. L. Bhyrappa", "2007", "India", ["History", "Faith", "Identity"]),
    ("Parva", "S. L. Bhyrappa", "1979", "India", ["Mythology", "Morality"]),
    ("The Three-Body Problem", "Liu Cixin", "2008", "China", ["Science Fiction", "First Contact", "Physics"]),
    ("The Dark Forest", "Liu Cixin", "2008", "China", ["Science Fiction", "Survival"]),
    ("Death's End", "Liu Cixin", "2010", "China", ["Science Fiction", "Time", "Civilization"]),
    ("Ball Lightning", "Liu Cixin", "2004", "China", ["Science Fiction", "Obsession"]),
    ("Folding Beijing", "Hao Jingfang", "2014", "China", ["Science Fiction", "Class"]),
    ("Vita Nostra", "Marina and Sergey Dyachenko", "2007", "Ukraine", ["Fantasy", "Coming of Age", "Fear"]),
    ("Death in Spring", "Mercè Rodoreda", "1986", "Spain (Catalonia)", ["Death", "Ritual", "Village Life"]),
    ("In Diamond Square", "Mercè Rodoreda", "1962", "Spain (Catalonia)", ["War", "Womanhood"]),
    ("The Time of the Doves", "Mercè Rodoreda", "1962", "Spain (Catalonia)", ["War", "Resilience"]),
    ("Solenoid", "Mircea Cărtărescu", "2015", "Romania", ["Identity", "Dream", "Existentialism"]),
    ("Nostalgia", "Mircea Cărtărescu", "1989", "Romania", ["Memory", "Childhood", "Surrealism"]),
    ("The Museum of Unconditional Surrender", "Dubravka Ugrešić", "1997", "Croatia", ["Exile", "Memory"]),
    ("Baba Yaga Laid an Egg", "Dubravka Ugrešić", "2007", "Croatia", ["Myth", "Aging", "Gender"]),
    ("Ministry of Pain", "Dubravka Ugrešić", "2004", "Croatia", ["Exile", "Nostalgia"]),
    ("Death and the Penguin", "Andrey Kurkov", "1996", "Ukraine", ["Absurdism", "Loneliness"]),
    ("Grey Bees", "Andrey Kurkov", "2018", "Ukraine", ["War", "Neutrality", "Survival"]),
    ("The Aviator", "Eugene Vodolazkin", "2016", "Russia", ["Memory", "Time", "Identity"]),
    ("Laurus", "Eugene Vodolazkin", "2012", "Russia", ["Faith", "Healing", "Time"]),
    ("A Gentleman in Moscow", "Amor Towles", "2016", "Russia", ["Confinement", "Grace", "History"]),
    # --- Further top-up: safe, distinct additions across regions/genres ---
    ("The Weight of Ink", "Rachel Kadish", "2017", "United Kingdom/Israel", ["History", "Scholarship", "Faith"]),
    ("Stoner", "John Williams", "1965", "United States", ["Quiet Life", "Disappointment", "Perseverance"]),
    ("Butcher's Crossing", "John Williams", "1960", "United States", ["Nature", "Obsession"]),
    ("The Sympathizer (companion) — The Committed", "Viet Thanh Nguyen", "2021", "Vietnam/France", ["Identity", "Exile", "Crime"]),
    ("Salt Houses", "Hala Alyan", "2017", "Palestine/Kuwait", ["Displacement", "Family", "Exile"]),
    ("Minaret", "Leila Aboulela", "2005", "Sudan/United Kingdom", ["Faith", "Migration", "Identity"]),
    ("The Translator", "Leila Aboulela", "1999", "Sudan/United Kingdom", ["Faith", "Love", "Exile"]),
    ("The Parisian", "Isabella Hammad", "2019", "Palestine", ["Identity", "History", "Love"]),
    ("Enter Ghost", "Isabella Hammad", "2023", "Palestine", ["Theater", "Identity", "Occupation"]),
    ("The Beekeeper of Aleppo", "Christy Lefteri", "2019", "Syria", ["War", "Displacement", "Survival"]),
    ("In Praise of Older Women", "Stephen Vizinczey", "1965", "Hungary", ["Desire", "Memory"]),
    ("Under a Cruel Star", "Heda Margolius Kovály", "1973", "Czech Republic", ["Holocaust", "Survival", "Testimony"]),
    ("Life With a Star", "Jiří Weil", "1949", "Czech Republic", ["Holocaust", "Survival"]),
    ("Too Loud a Solitude", "Bohumil Hrabal", "1976", "Czech Republic", ["Books", "Isolation", "Meaning"]),
    ("Closely Watched Trains", "Bohumil Hrabal", "1965", "Czech Republic", ["War", "Coming of Age"]),
    ("The Painted Bird", "Jerzy Kosiński", "1965", "Poland", ["War", "Survival", "Cruelty"]),
    ("The Street of Crocodiles", "Bruno Schulz", "1934", "Poland", ["Imagination", "Family", "Memory"]),
    ("Drive Your Plow Over the Bones of the Dead", "Olga Tokarczuk", "2009", "Poland", ["Justice", "Nature", "Astrology"]),
    ("Flights", "Olga Tokarczuk", "2007", "Poland", ["Travel", "Fragmentation", "Body"]),
    ("The Books of Jacob", "Olga Tokarczuk", "2014", "Poland", ["Faith", "History", "Identity"]),
    ("Compulsory Games", "Robert Aickman", "various", "United Kingdom", ["Strange Fiction", "Unease"]),
    ("The Hearing Trumpet", "Leonora Carrington", "1974", "Mexico/United Kingdom", ["Surrealism", "Aging", "Rebellion"]),
    ("Down Below", "Leonora Carrington", "1944", "Mexico/United Kingdom", ["Madness", "Survival"]),
    ("Recollections of Things to Come", "Elena Garro", "1963", "Mexico", ["Memory", "Time", "Revolution"]),
    ("Balun Canán", "Rosario Castellanos", "1957", "Mexico", ["Childhood", "Indigenous Rights"]),
    ("The Book of Lamentations", "Rosario Castellanos", "1962", "Mexico", ["Injustice", "Indigenous Rights"]),
    ("Seeing", "José Saramago", "2004", "Portugal", ["Democracy", "Power", "Satire"]),
    ("The Cave", "José Saramago", "2000", "Portugal", ["Labor", "Consumerism"]),
    ("The Double", "José Saramago", "2002", "Portugal", ["Identity", "Doubling"]),
    ("Big Machine", "Victor LaValle", "2009", "United States", ["Faith", "Doubt", "Fantasy"]),
    ("The Changeling", "Victor LaValle", "2017", "United States", ["Fatherhood", "Fantasy", "Fear"]),
    ("Freshwater", "Akwaeke Emezi", "2018", "Nigeria", ["Identity", "Spirituality", "Mental Health"]),
    ("Pet", "Akwaeke Emezi", "2019", "Nigeria", ["Justice", "Monsters", "Truth"]),
    ("Praisesong for the Widow", "Paule Marshall", "1983", "Barbados/United States", ["Heritage", "Identity", "Renewal"]),
    ("Brown Girl, Brownstones", "Paule Marshall", "1959", "Barbados/United States", ["Immigration", "Family"]),
    ("The Autobiography of My Mother", "Jamaica Kincaid", "1996", "Antigua", ["Identity", "Colonialism", "Solitude"]),
    ("Kamila Shamsie's A God in Every Stone", "Kamila Shamsie", "2014", "Pakistan", ["War", "Archaeology", "Empire"]),
    ("The Association of Small Bombs", "Karan Mahajan", "2016", "India", ["Violence", "Trauma", "Terrorism"]),
    ("Latitudes of Longing", "Shubhangi Swarup", "2018", "India", ["Nature", "Love", "Time"]),
    ("Ghachar Ghochar", "Vivek Shanbhag", "2013", "India", ["Family", "Wealth", "Morality"]),
    ("Em and the Big Hoom", "Jerry Pinto", "2012", "India", ["Family", "Mental Illness", "Love"]),
]


def build_records(existing_titles: set[str], next_num: int) -> list[dict]:
    records = []
    n = next_num
    for title, author, year, origin, themes in BOOKS:
        if title in existing_titles:
            continue
        book_id = f"wl_global_{n:03d}"
        n += 1
        summary = (
            f"{title} by {author} ({year}) from {origin} is a celebrated work of world literature exploring "
            f"{', '.join(themes[:-1]) + (' and ' + themes[-1] if len(themes) > 1 else themes[0])}. "
            f"It broadens the platform's global literary coverage and is widely studied and translated "
            f"around the world."
        )
        records.append({
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "origin": origin,
            "summary": summary,
            "themes": themes,
            "reading_level": "Adult / College & University",
            "moral_lessons": [f"Explores {theme.lower()}" for theme in themes[:2]],
            "discussion_questions": [
                f"What does {title} suggest about {themes[0].lower()}?",
                f"How does {author}'s background in {origin} shape the perspective of {title}?",
            ],
            "links": {
                "read_online": gutenberg_search(title),
                "open_library": open_library_search(f"{title} {author}"),
                "video_summary": youtube_search(f"{title} {author} summary analysis"),
                "wikipedia": wikipedia(title),
                "goodreads": goodreads_search(f"{title} {author}"),
            },
        })
    return records


def main() -> None:
    with open(LIBRARY_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_titles = set()
    max_num = 0
    for section in data["sections"].values():
        for book in section.get("books", []):
            existing_titles.add(book["title"])
            m = re.match(r"wl_global_(\d+)$", book["id"])
            if m:
                max_num = max(max_num, int(m.group(1)))

    section = data["sections"].setdefault("world_literature_global", {
        "label": "World Literature — Global Voices",
        "emoji": "🌍",
        "age_range": "Adult / College+",
        "books": [],
    })

    records = build_records(existing_titles, max_num + 1)
    section["books"].extend(records)

    with open(LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(s.get("books", [])) for s in data["sections"].values())
    print(f"Added {len(records)} books. world_literature_global now has {len(section['books'])} books. "
          f"Library now has {total} books across {len(data['sections'])} sections.")


if __name__ == "__main__":
    main()
