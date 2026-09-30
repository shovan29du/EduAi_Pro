#!/usr/bin/env python3
"""Remove duplicate songs from the Song Centre
(backend/data/song_centre/songs.json).

Duplicates are identified by normalized (title, artist) pairs -- the same
song re-added by different expansion scripts over the life of this
project, sometimes with slightly different artist-credit formatting
(e.g. "Luis Fonsi feat. Daddy Yankee" vs "Luis Fonsi & Daddy Yankee" vs
"Luis Fonsi ft. Daddy Yankee"), which is why a light normalization is
used before comparing. Different artists performing a same-titled song
(e.g. two different "La Bamba" covers) are correctly NOT treated as
duplicates.

Among a group of duplicates, the entry with the most complete data (most
non-empty fields, then longest description) is kept; the rest are
dropped.

Re-run any time after new songs are added:
    python3 backend/scripts/dedupe_songs.py
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SONGS_PATH = BASE_DIR / "data" / "song_centre" / "songs.json"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("'", "")
    s = re.sub(r"\b(feat\.?|ft\.?|featuring|&|and|vs\.?|the)\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    # Collapse runs of standalone single-letter words (e.g. "u s a" -> "usa")
    # so period-separated abbreviations match their unpunctuated form.
    s = re.sub(r"(?:\b[a-z0-9]\b ){2,}\b[a-z0-9]\b", lambda m: m.group(0).replace(" ", ""), s)
    return re.sub(r"\s+", " ", s).strip()


def completeness_score(song: dict) -> tuple:
    non_empty_fields = sum(
        1 for v in song.values()
        if v not in (None, "", [], {}) and v != []
    )
    desc_len = len(song.get("description", "") or "")
    awards_len = len(song.get("awards", []) or [])
    return (non_empty_fields, awards_len, desc_len)


def main() -> None:
    with open(SONGS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    songs = data["songs"]
    groups: dict[tuple, list[dict]] = {}
    for song in songs:
        key = (norm(song.get("title", "")), norm(song.get("artist", "")))
        groups.setdefault(key, []).append(song)

    kept = []
    removed = 0
    for key, group in groups.items():
        if len(group) == 1:
            kept.append(group[0])
            continue
        best = max(group, key=completeness_score)
        kept.append(best)
        removed += len(group) - 1

    data["songs"] = kept
    data["total"] = len(kept)

    genres = set()
    decades = set()
    for s in kept:
        genres.update(s.get("genre", []))
        if s.get("decade"):
            decades.add(s["decade"])
    data["genres"] = sorted(genres)
    data["decades"] = sorted(decades)

    with open(SONGS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Removed {removed} duplicate songs. Collection now has {data['total']} songs "
          f"(was {len(songs)}).")


if __name__ == "__main__":
    main()
