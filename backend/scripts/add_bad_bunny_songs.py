#!/usr/bin/env python3
"""Add a set of Bad Bunny's most famous songs to the Song Centre
(backend/data/song_centre/songs.json), beyond the eight already present
(Dákiti, Tití Me Preguntó, Me Porto Bonito, Yo Perreo Sola, Callaíta,
and features on I Like It, Te Boté Remix, and Mayores).

Every entry is a real, well-known song with a music-video YouTube
*search* link rather than a guessed direct video URL, consistent with the
Song Centre's search-link policy.

Re-run after editing:
    python3 backend/scripts/add_bad_bunny_songs.py
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SONGS_PATH = BASE_DIR / "data" / "song_centre" / "songs.json"


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wiki_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


def lyrics_search(q: str) -> str:
    return "https://www.google.com/search?q=" + quote_plus(q)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", norm(s)).strip("_")


# (title, artist, year, genres, language, description, fun_fact)
SONGS = [
    ("Mía", "Bad Bunny feat. Drake", 2018, ["reggaeton", "latin trap"], "Spanish", "A landmark collaboration with Drake singing entirely in Spanish over a sleek reggaeton groove.", "It debuted in the top 5 of the Billboard Hot 100, a milestone for Spanish-language music."),
    ("La Canción", "J Balvin & Bad Bunny", 2019, ["reggaeton"], "Spanish", "A melancholy trumpet-laced highlight from the joint album Oasis about a song that brings an ex flooding back.", "It won Record of the Year at the 2020 Latin Grammys."),
    ("Vete", "Bad Bunny", 2019, ["reggaeton", "latin trap"], "Spanish", "A brisk kiss-off anthem that opened the YHLQMDLG era.", "YHLQMDLG became the highest-charting all-Spanish album on the Billboard 200 at the time."),
    ("Si Veo a Tu Mamá", "Bad Bunny", 2020, ["reggaeton", "latin pop"], "Spanish", "A deceptively upbeat opener about running into an ex's mother, built on a playful melodic loop.", "It opens the acclaimed album YHLQMDLG -- 'Yo Hago Lo Que Me Da La Gana'."),
    ("La Santa", "Bad Bunny & Daddy Yankee", 2020, ["reggaeton"], "Spanish", "A generational torch-passing banger uniting reggaeton's past and present.", "It pairs Bad Bunny with the genre legend who inspired him, Daddy Yankee."),
    ("La Difícil", "Bad Bunny", 2020, ["reggaeton"], "Spanish", "A club-ready track about a woman who plays hard to get.", "Its retro video pays homage to early-2000s reggaeton culture."),
    ("Amorfoda", "Bad Bunny", 2018, ["latin trap", "ballad"], "Spanish", "A raw piano heartbreak ballad that showed the emotional range behind the trap star.", "Released on Valentine's Day 2018 as a surprise anti-valentine."),
    ("Estamos Bien", "Bad Bunny", 2018, ["latin trap"], "Spanish", "An uplifting anthem of resilience dedicated to Puerto Rico after Hurricane Maria.", "Bad Bunny performed it on The Tonight Show in his US TV debut."),
    ("Soy Peor", "Bad Bunny", 2017, ["latin trap"], "Spanish", "The brooding breakout hit that defined the Latin trap sound of the late 2010s.", "It is widely credited as the song that made Bad Bunny a star."),
    ("Yonaguni", "Bad Bunny", 2021, ["reggaeton", "latin pop"], "Spanish/Japanese", "A wistful summer hit named after Japan's westernmost island, ending with a verse sung in Japanese.", "It debuted at #10 on the Billboard Hot 100."),
    ("Volví", "Aventura & Bad Bunny", 2021, ["bachata", "reggaeton"], "Spanish", "A blockbuster bachata-reggaeton reunion pairing Bad Bunny with the kings of bachata.", "It marked Aventura's first new music in years and topped Latin charts instantly."),
    ("Moscow Mule", "Bad Bunny", 2022, ["reggaeton"], "Spanish", "The laid-back opener of Un Verano Sin Ti, made for beach sunsets.", "Un Verano Sin Ti was Spotify's most-streamed album globally for two consecutive years."),
    ("Después de la Playa", "Bad Bunny", 2022, ["mambo", "merengue"], "Spanish", "A beach-day track that erupts mid-song into a full-blown live mambo.", "Its merengue-mambo breakdown became a highlight of his stadium shows."),
    ("Ojitos Lindos", "Bad Bunny & Bomba Estéreo", 2022, ["reggaeton", "electro cumbia"], "Spanish", "A dreamy collaboration with Colombia's Bomba Estéreo about eyes that hold a whole world.", "It spent months near the top of the Billboard Global 200 without ever being a single."),
    ("Neverita", "Bad Bunny", 2022, ["reggaeton"], "Spanish", "A bouncy Un Verano Sin Ti favorite about keeping love on ice.", "Its retro video was shot as a tribute to classic 90s music television."),
    ("Efecto", "Bad Bunny", 2022, ["reggaeton"], "Spanish", "A hypnotic late-night track about an intoxicating attraction.", "It became a sleeper hit from Un Verano Sin Ti, charting worldwide."),
    ("Where She Goes", "Bad Bunny", 2023, ["jersey club", "latin trap"], "Spanish", "A moody Jersey club experiment that pushed reggaeton's boundaries.", "Its video features cameos from Frank Ocean, Lil Uzi Vert, and Ronaldinho."),
    ("Un x100to", "Grupo Frontera & Bad Bunny", 2023, ["norteño", "cumbia"], "Spanish", "A heartbroken norteño-cumbia collaboration bridging regional Mexican music and reggaeton's biggest star.", "It debuted in the top 5 of the Billboard Hot 100, a first for a norteño group."),
    ("Monaco", "Bad Bunny", 2023, ["latin trap"], "Spanish", "A lavish, orchestral-sampling flex anthem from Nadie Sabe Lo Que Va a Pasar Mañana.", "Its video features a cameo by Al Pacino."),
    ("Lo Siento BB:/", "Tainy, Bad Bunny & Julieta Venegas", 2021, ["reggaeton", "synth-pop"], "Spanish", "A moody apology anthem uniting three generations of Latin music talent.", "Julieta Venegas's dreamy hook made it one of 2021's most distinctive Latin hits."),
]


def build_song(title, artist, year, genres, language, description, fun_fact):
    decade = f"{(year // 10) * 10}s"
    return {
        "id": f"bad_bunny_{slug(title)}",
        "title": title,
        "artist": artist,
        "album": "",
        "year": year,
        "genre": genres,
        "origin_country": "Puerto Rico",
        "language": language,
        "duration_approx": "",
        "description": description,
        "educational_notes": f"Useful for exploring {genres[0]} and contemporary Puerto Rican music culture.",
        "fun_fact": fun_fact,
        "awards": [],
        "links": {
            "youtube_search": yt_search(f"{title} {artist} official music video"),
            "wiki_search": wiki_search(f"{title} {artist}"),
            "lyrics_search": lyrics_search(f"{title} {artist} lyrics"),
        },
        "tags": genres + [decade, "latino party"],
        "decade": decade,
        "suitable_for_ages": "10+",
    }


def main() -> None:
    with open(SONGS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_titles = {norm(s["title"]) for s in data["songs"]}
    existing_ids = {s["id"] for s in data["songs"]}

    added = 0
    skipped = []
    for item in SONGS:
        song = build_song(*item)
        if norm(item[0]) in existing_titles or song["id"] in existing_ids:
            skipped.append(item[0])
            continue
        data["songs"].append(song)
        existing_titles.add(norm(item[0]))
        existing_ids.add(song["id"])
        added += 1

    data["total"] = len(data["songs"])

    genres = set()
    decades = set()
    for s in data["songs"]:
        genres.update(s.get("genre", []))
        if s.get("decade"):
            decades.add(s["decade"])
    data["genres"] = sorted(genres)
    data["decades"] = sorted(decades)

    with open(SONGS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {added} Bad Bunny songs (skipped {len(skipped)}: {skipped}). "
          f"Collection total: {data['total']}")


if __name__ == "__main__":
    main()
