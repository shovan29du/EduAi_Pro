#!/usr/bin/env python3
"""Build backend/data/virtual_tour/tour.json from the authored files in vt_data/.

Each vt_data module defines, keyed by ISO country code:
  PLACES  "Name|t; Name|t; ..."   t = a attraction, n natural wonder, m museum, r architecture
  CITIES  "Capital; City; City"   major cities (capital first)
  GUIDE   (tier, cost, transport, stay, food, buy, warn, climate)
          tier is $ / $$ / $$$ / $$$$ (rough daily budget for a comfortable solo traveller)

Run after editing any vt_data file; it fails if a country is missing or malformed.

    python3 backend/scripts/build_virtual_tour.py
"""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
COUNTRIES = ROOT / "data" / "countries" / "countries.json"
OUT = ROOT / "data" / "virtual_tour" / "tour.json"
TRIPS_OUT = ROOT / "data" / "virtual_tour" / "road_trips.json"
MODULES = ["africa", "asia", "europe", "americas", "oceania"]
TYPES = {"a": "attraction", "n": "nature", "m": "museum", "r": "architecture"}
GUIDE_FIELDS = ("tier", "cost", "transport", "stay", "food", "buy", "warn", "climate")
MIN_PLACES, MIN_CITIES = 5, 1


def parse_places(code: str, text: str) -> list[dict]:
    places, seen = [], set()
    for chunk in (c.strip() for c in text.split(";") if c.strip()):
        name, _, kind = chunk.rpartition("|")
        name, kind = name.strip(), kind.strip()
        if not name or kind not in TYPES:
            raise SystemExit(f"{code}: bad place entry {chunk!r}")
        if name.lower() in seen:
            raise SystemExit(f"{code}: duplicate place {name!r}")
        seen.add(name.lower())
        places.append({"name": name, "type": TYPES[kind]})
    return places


def build_road_trips(known: dict) -> list[dict]:
    from vt_data.road_trips import ROAD_TRIPS

    seen, out = set(), []
    for trip in ROAD_TRIPS:
        tid = trip["id"]
        if tid in seen:
            raise SystemExit(f"road trip {tid}: duplicate id")
        seen.add(tid)
        bad = [c for c in trip["countries"] if c not in known]
        if bad or not trip["countries"]:
            raise SystemExit(f"road trip {tid}: unknown or missing countries {bad}")
        if not (trip["name"] and trip["start"] and trip["end"] and trip["summary"] and trip["tip"] and trip["best_time"]):
            raise SystemExit(f"road trip {tid}: empty field")
        if len(trip["highlights"]) < 3 or len(trip["via"]) > 8 or not isinstance(trip["km"], int) or trip["km"] <= 0:
            raise SystemExit(f"road trip {tid}: needs 3+ highlights, at most 8 waypoints and a positive km")
        out.append(trip)
    return out


def main() -> None:
    places, cities, guides = {}, {}, {}
    for module in MODULES:
        mod = importlib.import_module(f"vt_data.{module}")
        for source, target in ((mod.PLACES, places), (mod.CITIES, cities), (mod.GUIDE, guides)):
            dup = set(source) & set(target)
            if dup:
                raise SystemExit(f"{module}: codes defined twice: {sorted(dup)}")
            target.update(source)

    known = {c["code"]: c for c in json.loads(COUNTRIES.read_text(encoding="utf-8"))["countries"]}
    problems = []
    for code in sorted(set(known) | set(places) | set(cities) | set(guides)):
        if code not in known:
            problems.append(f"{code}: not in countries.json")
            continue
        for label, table in (("PLACES", places), ("CITIES", cities), ("GUIDE", guides)):
            if code not in table:
                problems.append(f"{code} ({known[code]['name']}): missing {label}")
    if problems:
        raise SystemExit("\n".join(problems))

    out = {}
    for code in sorted(known):
        parsed = parse_places(code, places[code])
        city_list = [c.strip() for c in cities[code].split(";") if c.strip()]
        guide = guides[code]
        if len(guide) != len(GUIDE_FIELDS):
            raise SystemExit(f"{code}: guide needs {len(GUIDE_FIELDS)} fields, has {len(guide)}")
        guide = dict(zip(GUIDE_FIELDS, (g.strip() for g in guide)))
        if guide["tier"] not in {"$", "$$", "$$$", "$$$$"}:
            raise SystemExit(f"{code}: bad tier {guide['tier']!r}")
        if any(not v for v in guide.values()):
            raise SystemExit(f"{code}: empty guide field")
        if len(parsed) < MIN_PLACES:
            raise SystemExit(f"{code}: only {len(parsed)} places (minimum {MIN_PLACES})")
        if len(city_list) < MIN_CITIES:
            raise SystemExit(f"{code}: needs at least {MIN_CITIES} city")
        out[code] = {"places": parsed, "cities": city_list, "guide": guide}

    trips = build_road_trips(known)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"updated": "2026-11", "countries": out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    TRIPS_OUT.write_text(json.dumps({"updated": "2026-11", "road_trips": trips}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(trips)} road trips -> {TRIPS_OUT}")
    total = sum(len(v["places"]) for v in out.values())
    print(f"{len(out)} countries, {total} places, {sum(len(v['cities']) for v in out.values())} cities -> {OUT}")


if __name__ == "__main__":
    main()
