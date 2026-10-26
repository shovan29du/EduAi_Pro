#!/usr/bin/env python3
"""Add real, globally famous music videos that are well-documented as
having surpassed 1 billion views on YouTube, to the Song Centre
(backend/data/song_centre/songs.json).

Only metadata is stored (title, artist, year, genre, description, one
fun fact) -- no lyrics -- plus a YouTube-search-based video link,
consistent with every other entry in this collection. Exact current view
counts are not stated as precise numbers (they change constantly and
cannot be verified live from this environment); each entry is described
as having crossed the 1-billion-view milestone, which is a stable,
well-documented fact for every song on this list, not a live figure.

Re-run after editing:
    python3 backend/scripts/add_billion_view_songs.py
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
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", norm(s)).strip("_")


# (title, artist, year, genres, country, language, description, fun_fact)
SONGS = [
    ("See You Again", "Wiz Khalifa feat. Charlie Puth", 2015, ["hip hop", "pop"], "United States", "English", "A tribute track written for the Furious 7 film in memory of actor Paul Walker.", "Its music video was, for a time, the most-viewed video in YouTube history."),
    ("Baby Shark Dance", "Pinkfong", 2016, ["children's music", "dance"], "South Korea", "English", "A viral children's sing-and-dance video based on a traditional campfire chant.", "In 2022 it became the first YouTube video ever to reach 10 billion views."),
    ("Bad Romance", "Lady Gaga", 2009, ["pop", "electropop"], "United States", "English", "A theatrical electropop anthem about obsessive love, one of the defining pop videos of its era.", "Its avant-garde fashion and choreography made it one of the most influential music videos of the 2000s."),
    ("Party Rock Anthem", "LMFAO feat. Lauren Bennett & GoonRock", 2011, ["electro house", "pop"], "United States", "English", "An electro-house party anthem that popularized the 'shuffling' dance move worldwide.", "It topped charts in more than a dozen countries."),
    ("Love the Way You Lie", "Eminem feat. Rihanna", 2010, ["hip hop"], "United States", "English", "A raw, dramatic depiction of a toxic relationship, one of Eminem's most acclaimed collaborations.", "It spent seven weeks at #1 on the Billboard Hot 100."),
    ("Girls Like You", "Maroon 5 feat. Cardi B", 2018, ["pop"], "United States", "English", "A feel-good pop anthem with a video featuring dozens of prominent women.", "The music video cameos over 20 well-known actresses, athletes, and musicians."),
    ("Photograph", "Ed Sheeran", 2015, ["pop"], "United Kingdom", "English", "A tender ballad about holding onto memories of a loved one.", "It became one of Ed Sheeran's most streamed ballads worldwide."),
    ("Dark Horse", "Katy Perry feat. Juicy J", 2013, ["pop", "trap pop"], "United States", "English", "An Egyptian-themed pop track blending trap beats with dramatic pop production.", "It spent four weeks at #1 on the Billboard Hot 100."),
    ("Firework", "Katy Perry", 2010, ["pop"], "United States", "English", "An empowering anthem encouraging listeners to let their inner light shine.", "It became one of Katy Perry's signature songs and a staple at fireworks displays and celebrations."),
    ("Cheap Thrills", "Sia feat. Sean Paul", 2016, ["pop", "dancehall"], "Australia", "English", "An upbeat dance-pop track about having fun without needing money.", "It topped charts in numerous countries during the summer of 2016."),
    ("New Rules", "Dua Lipa", 2017, ["pop"], "United Kingdom", "English", "A breakup anthem laying out rules for resisting an ex's advances, with a widely praised choreographed video.", "It became Dua Lipa's first UK #1 single."),
    ("Watch Me (Whip/Nae Nae)", "Silento", 2015, ["hip hop", "dance"], "United States", "English", "A dance-instruction song that sparked one of the biggest viral dance crazes of the mid-2010s.", "Its accompanying dance was recreated by celebrities, athletes, and schools worldwide."),
    ("All About That Bass", "Meghan Trainor", 2014, ["pop", "doo-wop"], "United States", "English", "A body-positivity anthem blending retro doo-wop influences with modern pop.", "It spent eight weeks at #1 on the Billboard Hot 100."),
    ("Attention", "Charlie Puth", 2017, ["pop"], "United States", "English", "A pop track about calling out an ex who only reappears for attention.", "It became one of Charlie Puth's biggest solo hits."),
    ("Thunder", "Imagine Dragons", 2017, ["pop rock", "electropop"], "United States", "English", "An energetic anthem about persevering as an underdog until you find your own kind of power.", "It became one of Imagine Dragons' most streamed songs worldwide."),
    ("Faded", "Alan Walker", 2015, ["electronic", "progressive house"], "Norway", "English", "An atmospheric electronic track built around a haunting vocal hook.", "It became one of the most-viewed electronic dance music videos on YouTube."),
    ("Kill This Love", "Blackpink", 2019, ["k-pop"], "South Korea", "Korean/English", "A high-energy K-pop anthem with a brass-driven hook and elaborate choreography.", "Its music video broke the record for most views in 24 hours at the time of release."),
    ("How You Like That", "Blackpink", 2020, ["k-pop"], "South Korea", "Korean/English", "A hard-hitting K-pop comeback single released after a lengthy hiatus.", "Its video set a new YouTube 24-hour premiere view record upon release."),
    ("We Don't Talk Anymore", "Charlie Puth feat. Selena Gomez", 2016, ["pop"], "United States", "English", "A pop duet about the awkward silence following a breakup.", "It became one of Charlie Puth's most successful singles as a solo artist."),
    ("Wolves", "Selena Gomez & Marshmello", 2017, ["pop", "electropop"], "United States", "English", "An atmospheric pop-EDM collaboration about seeking comfort and belonging.", "It marked one of Selena Gomez's biggest collaborations with an electronic producer."),
    ("Rockabye", "Clean Bandit feat. Sean Paul & Anne-Marie", 2016, ["pop", "dancehall"], "United Kingdom", "English", "A dancehall-pop song about a single mother's love for her child.", "It spent multiple weeks at #1 on the UK Singles Chart."),
    ("Symphony", "Clean Bandit feat. Zara Larsson", 2017, ["pop", "dance-pop"], "United Kingdom", "English", "An uplifting dance-pop track about finding harmony in a relationship.", "It topped the UK Singles Chart upon release."),
    ("Friends", "Marshmello & Anne-Marie", 2018, ["pop", "electropop"], "United States/United Kingdom", "English", "A playful pop-EDM duet about staying platonic despite one-sided feelings.", "Its animated-style video became one of the most-viewed of 2018."),
    ("Happier", "Marshmello feat. Bastille", 2018, ["pop", "electropop"], "United States/United Kingdom", "English", "A bittersweet dance-pop track about wanting an ex to be happier without you.", "It became one of Marshmello's most streamed collaborations."),
    ("Something Just Like This", "The Chainsmokers & Coldplay", 2017, ["electropop", "pop rock"], "United States/United Kingdom", "English", "A soaring collaboration between an EDM duo and a stadium rock band about wanting to feel extraordinary.", "It became one of the best-selling singles of 2017."),
    ("Hymn for the Weekend", "Coldplay", 2016, ["pop rock", "electropop"], "United Kingdom", "English", "An anthemic track blending Coldplay's rock sound with electronic and Indian musical influences.", "Its video was filmed on location in Mumbai, India."),
    ("Bohemian Rhapsody", "Queen", 1975, ["rock", "progressive rock"], "United Kingdom", "English", "A genre-defying rock operetta widely regarded as one of the greatest songs ever recorded.", "It became the first music video from before 1990 to surpass 1 billion YouTube views."),
    ("Take On Me", "a-ha", 1985, ["synth-pop"], "Norway", "English", "A synth-pop classic famous for its pioneering rotoscope-animated music video.", "The video's blend of live action and pencil-sketch animation won six MTV Video Music Awards."),
    ("Africa", "Toto", 1982, ["soft rock", "pop rock"], "United States", "English", "A soft-rock classic evoking the imagined landscapes and spirit of Africa.", "It experienced a major streaming resurgence in the late 2010s thanks to internet memes and covers."),
    ("Counting Stars", "OneRepublic", 2013, ["pop rock"], "United States", "English", "An anthemic pop-rock song about chasing dreams over material wealth.", "It became one of OneRepublic's best-selling singles worldwide."),
    ("Happy", "Pharrell Williams", 2013, ["soul", "pop"], "United States", "English", "An infectious feel-good soul-pop anthem originally written for the film Despicable Me 2.", "Its innovative 24-hour music video features people dancing continuously across Los Angeles."),
    ("Believer", "Imagine Dragons", 2017, ["pop rock", "arena rock"], "United States", "English", "A pounding, drum-driven anthem about transforming pain into strength.", "It became one of the most-streamed rock songs of the 2010s."),
    ("DDU-DU DDU-DU", "Blackpink", 2018, ["k-pop"], "South Korea", "Korean/English", "A bold, trap-influenced K-pop single that helped cement Blackpink's global breakout.", "Its video broke the record for the most-viewed K-pop group video within 24 hours at the time."),
    ("Sugar", "Maroon 5", 2015, ["pop", "funk pop"], "United States", "English", "An upbeat, funk-influenced pop song with a widely loved music video showing the band crashing real weddings.", "The video's surprise wedding-crashing concept made it one of the most shared music videos of 2015."),
    ("That's What I Like", "Bruno Mars", 2017, ["r&b", "funk"], "United States", "English", "A smooth R&B-funk track celebrating luxury and romance.", "It won the Grammy Award for Song of the Year."),
    ("24K Magic", "Bruno Mars", 2016, ["funk", "r&b"], "United States", "English", "A funk-driven celebration track inspired by 1980s and 90s R&B and funk sounds.", "It won the Grammy Award for Record of the Year."),
    ("Roar", "Katy Perry", 2013, ["pop"], "United States", "English", "An empowerment anthem about finding your voice after being underestimated.", "It debuted at #1 on the Billboard Hot 100."),
    ("Dynamite", "BTS", 2020, ["disco pop", "k-pop"], "South Korea", "English", "An upbeat, retro-disco-influenced pop song, BTS's first all-English single.", "Its video broke YouTube's record for most views in 24 hours at the time of release."),
    ("Boy With Luv", "BTS feat. Halsey", 2019, ["k-pop", "pop"], "South Korea", "Korean/English", "A bright, danceable K-pop single celebrating the joy fans bring to the group.", "Its music video set a new record for the fastest K-pop video to reach 100 million views."),
]


def build_song(title, artist, year, genres, country, language, description, fun_fact):
    decade = f"{(year // 10) * 10}s"
    return {
        "id": f"billion_view_{slug(title)}",
        "title": title,
        "artist": artist,
        "album": "",
        "year": year,
        "genre": genres,
        "origin_country": country,
        "language": language,
        "duration_approx": "",
        "description": description,
        "educational_notes": f"A widely documented example of a music video that surpassed 1 billion views on YouTube.",
        "fun_fact": fun_fact,
        "awards": ["1+ billion YouTube views"],
        "links": {
            "youtube_search": yt_search(f"{title} {artist} official music video"),
            "wiki_search": wiki_search(f"{title} {artist}"),
            "lyrics_search": lyrics_search(f"{title} {artist} lyrics"),
        },
        "tags": genres + [decade, "1 billion+ views"],
        "decade": decade,
        "suitable_for_ages": "10+",
    }


def main() -> None:
    with open(SONGS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_keys = {(norm(s["title"]), norm(s["artist"])) for s in data["songs"]}
    existing_ids = {s["id"] for s in data["songs"]}

    added = 0
    skipped = []
    for item in SONGS:
        song = build_song(*item)
        key = (norm(item[0]), norm(item[1]))
        if key in existing_keys or song["id"] in existing_ids:
            skipped.append(item[0])
            continue
        data["songs"].append(song)
        existing_keys.add(key)
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

    print(f"Added {added} songs (skipped {len(skipped)} already-present: {skipped}). "
          f"Collection total: {data['total']}")


if __name__ == "__main__":
    main()
