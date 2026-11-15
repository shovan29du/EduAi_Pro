"""Virtual Tour: places to see, major cities and a travel guide for every country.

Authored content (places, cities, travel guide) lives in data/virtual_tour/
tour.json, built from backend/scripts/vt_data/ by scripts/build_virtual_tour.py.
Country profiles come from data/countries/countries.json (the former Countries
Explorer), so the two are one feature. Video, blog, photo, map and 3D links are
generated from names, so they never go stale in a data file. Live weather
(Open-Meteo) and exchange rates (open.er-api.com) are fetched on demand and
cached; if they are unreachable the rest of the page still works.
"""
from __future__ import annotations

import json
import re
import time
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote, quote_plus
from urllib.request import Request, urlopen

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/virtual-tour", tags=["virtual-tour"])

_BASE = Path(__file__).resolve().parent.parent
COUNTRIES_PATH = _BASE / "data" / "countries" / "countries.json"
TOUR_PATH = _BASE / "data" / "virtual_tour" / "tour.json"
CACHE_DIR = _BASE / "data" / "virtual_tour_cache"
WEATHER_TTL = 30 * 60
RATES_TTL = 6 * 3600
HEADERS = {"User-Agent": "EduAI-Pro/1.0 (educational app)"}

CONTINENTS = [
    ("africa", "Africa", "🌍"),
    ("asia", "Asia", "🌏"),
    ("europe", "Europe", "🏰"),
    ("north-america", "North America", "🗽"),
    ("south-america", "South America", "🦙"),
    ("oceania", "Oceania", "🏝️"),
]
CONTINENT_LABEL = {cid: label for cid, label, _ in CONTINENTS}
SOUTH_AMERICA = {"AR", "BO", "BR", "CL", "CO", "EC", "GY", "PY", "PE", "SR", "UY", "VE"}
# Transcontinental countries are listed once, under the continent most atlases use.
TRANSCONTINENTAL = {"RU": "europe", "CY": "europe", "TR": "asia"}
PLACE_TYPES = ("attraction", "nature", "museum", "architecture")
PLACE_TYPE_LABEL = {
    "attraction": "Tourist attractions",
    "nature": "Natural wonders",
    "museum": "Museums",
    "architecture": "Architecture",
}

# Wikipedia/Wikivoyage/Numbeo titles that differ from the app's country names.
TITLE_OVERRIDES = {
    "TR": "Turkey", "CG": "Republic of the Congo", "CD": "Democratic Republic of the Congo",
    "CV": "Cape Verde", "TL": "East Timor", "FM": "Federated States of Micronesia",
    "BS": "The Bahamas", "GM": "The Gambia", "CZ": "Czech Republic", "MM": "Myanmar",
}
NUMBEO_OVERRIDES = {"TR": "Turkey", "CG": "Congo", "CD": "Democratic Republic Of The Congo", "CV": "Cape Verde", "TL": "Timor-Leste"}


def continent_of(country: dict) -> str:
    code = country["code"]
    if code in TRANSCONTINENTAL:
        return TRANSCONTINENTAL[code]
    raw = country.get("continent", "")
    if raw == "Americas":
        return "south-america" if code in SOUTH_AMERICA else "north-america"
    return {"Africa": "africa", "Asia": "asia", "Europe": "europe", "Oceania": "oceania"}.get(raw, "asia")


def short_name(country: dict) -> str:
    """Plain country name for searches, e.g. 'Türkiye (Turkey)' -> 'Turkey'."""
    override = TITLE_OVERRIDES.get(country["code"])
    if override:
        return override
    return re.sub(r"\s*\([^)]*\)", "", country["name"]).strip()


# ── links (generated, so they cannot go stale in the data file) ───────────────
def _search(query: str) -> str:
    return quote_plus(query)


def place_links(name: str, country: str) -> dict:
    full = f"{name} {country}"
    return {
        "video": f"https://www.youtube.com/results?search_query={_search(full + ' virtual tour 4K')}",
        "blog": f"https://www.google.com/search?q={_search(full + ' travel blog')}",
        "photos": f"https://commons.wikimedia.org/w/index.php?search={_search(full)}&ns6=1",
        "map": f"https://www.google.com/maps/search/?api=1&query={_search(full)}",
        "earth": f"https://earth.google.com/web/search/{quote(name + ', ' + country)}",
    }


def city_links(city: str, country: str) -> dict:
    full = f"{city} {country}"
    return {
        "video": f"https://www.youtube.com/results?search_query={_search(full + ' 4K walking tour')}",
        "blog": f"https://www.google.com/search?q={_search(full + ' city guide travel blog')}",
        "photos": f"https://commons.wikimedia.org/w/index.php?search={_search(full)}&ns6=1",
        "map": f"https://www.google.com/maps/search/?api=1&query={_search(full)}",
        "earth_3d": f"https://earth.google.com/web/search/{quote(city + ', ' + country)}",
        "hotels": f"https://www.booking.com/searchresults.html?ss={_search(full)}",
    }


def country_links(country: dict) -> dict:
    name = short_name(country)
    wiki = quote(name.replace(" ", "_"))
    return {
        "video": f"https://www.youtube.com/results?search_query={_search(name + ' virtual tour 4K travel')}",
        "blog": f"https://www.google.com/search?q={_search(name + ' travel blog itinerary')}",
        "photos": f"https://commons.wikimedia.org/w/index.php?search={_search(name + ' landscape')}&ns6=1",
        "street_food": f"https://www.youtube.com/results?search_query={_search(name + ' street food tour')}",
        "wikivoyage": f"https://en.wikivoyage.org/wiki/{wiki}",
        "stay_safe": f"https://en.wikivoyage.org/wiki/{wiki}#Stay_safe",
        "advisory": f"https://www.google.com/search?q={_search(name + ' travel advisory')}",
        "cost_of_living": "https://www.numbeo.com/cost-of-living/country_result.jsp?country="
        + quote_plus(NUMBEO_OVERRIDES.get(country["code"], name)),
        "hotels": f"https://www.booking.com/searchresults.html?ss={_search(country.get('capital', '') + ' ' + name)}",
        "advisory_uk": "https://www.gov.uk/foreign-travel-advice",
        "advisory_us": "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/",
    }


# ── data ──────────────────────────────────────────────────────────────────────
@lru_cache(maxsize=4)
def _load(countries_mtime: float, tour_mtime: float) -> dict:
    countries = json.loads(COUNTRIES_PATH.read_text(encoding="utf-8")).get("countries", [])
    tour = {}
    if TOUR_PATH.exists():
        tour = json.loads(TOUR_PATH.read_text(encoding="utf-8")).get("countries", {})
    return {"countries": {c["code"].upper(): c for c in countries}, "tour": tour}


def data() -> dict:
    tour_mtime = TOUR_PATH.stat().st_mtime if TOUR_PATH.exists() else 0.0
    return _load(COUNTRIES_PATH.stat().st_mtime, tour_mtime)


def _entry(code: str) -> dict:
    return data()["tour"].get(code.upper(), {})


def _summary(country: dict) -> dict:
    entry = _entry(country["code"])
    return {
        "code": country["code"], "name": country["name"], "capital": country.get("capital", ""),
        "flag_emoji": country.get("flag_emoji", ""), "flag_url": country.get("flag_url", ""),
        "coordinates": country.get("coordinates"), "continent_id": continent_of(country),
        "place_count": len(entry.get("places", [])), "city_count": len(entry.get("cities", [])),
    }


def _all_summaries() -> list[dict]:
    return sorted((_summary(c) for c in data()["countries"].values()), key=lambda s: s["name"])


@router.get("")
def overview():
    summaries = _all_summaries()
    continents = []
    for cid, label, emoji in CONTINENTS:
        members = [s for s in summaries if s["continent_id"] == cid]
        continents.append({
            "id": cid, "label": label, "emoji": emoji, "country_count": len(members),
            "place_count": sum(s["place_count"] for s in members),
        })
    return {
        "continents": continents,
        "totals": {
            "countries": len(summaries),
            "places": sum(s["place_count"] for s in summaries),
            "cities": sum(s["city_count"] for s in summaries),
        },
        "place_types": [{"id": t, "label": PLACE_TYPE_LABEL[t]} for t in PLACE_TYPES],
    }


@router.get("/countries")
def all_countries():
    """Every country (for the world map and search)."""
    return {"countries": _all_summaries()}


@router.get("/continents/{continent_id}")
def continent(continent_id: str):
    if continent_id not in CONTINENT_LABEL:
        raise HTTPException(status_code=404, detail="Continent not found")
    return {
        "id": continent_id, "label": CONTINENT_LABEL[continent_id],
        "countries": [s for s in _all_summaries() if s["continent_id"] == continent_id],
    }


@router.get("/countries/{code}")
def country_tour(code: str):
    country = data()["countries"].get(code.upper())
    if not country:
        raise HTTPException(status_code=404, detail=f"Country '{code}' not found")
    entry = _entry(code)
    name = short_name(country)
    places = [
        {**p, "links": place_links(p["name"], name)}
        for p in entry.get("places", [])
    ]
    cities = [
        {"name": c, "is_capital": c == country.get("capital") or i == 0, "links": city_links(c, name)}
        for i, c in enumerate(entry.get("cities", []))
    ]
    return {
        "profile": country,
        "continent_id": continent_of(country),
        "continent": CONTINENT_LABEL[continent_of(country)],
        "places": places,
        "cities": cities,
        "guide": entry.get("guide"),
        "links": country_links(country),
        "currency_code": currency_code(country),
    }


@router.get("/search")
def search(q: str = ""):
    needle = q.strip().lower()
    if len(needle) < 2:
        return {"countries": [], "places": [], "cities": []}
    countries, places, cities = [], [], []
    for country in data()["countries"].values():
        name = short_name(country)
        if needle in country["name"].lower() or needle in country.get("capital", "").lower():
            countries.append(_summary(country))
        entry = _entry(country["code"])
        for p in entry.get("places", []):
            if needle in p["name"].lower() and len(places) < 40:
                places.append({**p, "country": country["name"], "country_code": country["code"], "links": place_links(p["name"], name)})
        for c in entry.get("cities", []):
            if needle in c.lower() and len(cities) < 20:
                cities.append({"name": c, "country": country["name"], "country_code": country["code"], "links": city_links(c, name)})
    return {"countries": countries[:15], "places": places, "cities": cities}


# ── live data: weather and exchange rates ─────────────────────────────────────
WEATHER_TEXT = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast", 45: "Fog", 48: "Freezing fog",
    51: "Light drizzle", 53: "Drizzle", 55: "Heavy drizzle", 56: "Freezing drizzle", 57: "Freezing drizzle",
    61: "Light rain", 63: "Rain", 65: "Heavy rain", 66: "Freezing rain", 67: "Freezing rain",
    71: "Light snow", 73: "Snow", 75: "Heavy snow", 77: "Snow grains", 80: "Rain showers", 81: "Rain showers",
    82: "Violent rain showers", 85: "Snow showers", 86: "Heavy snow showers", 95: "Thunderstorm",
    96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}


def _get_json(url: str) -> dict:
    with urlopen(Request(url, headers=HEADERS), timeout=8) as response:
        return json.loads(response.read().decode("utf-8"))


def _cached(name: str, ttl: int):
    path = CACHE_DIR / name
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
        if time.time() - record["fetched_at"] < ttl:
            return record["payload"]
    except (OSError, ValueError, KeyError):
        pass
    return None


def _store(name: str, payload: dict) -> None:
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        (CACHE_DIR / name).write_text(json.dumps({"fetched_at": time.time(), "payload": payload}), encoding="utf-8")
    except OSError:
        pass


@router.get("/weather/{code}")
def weather(code: str):
    country = data()["countries"].get(code.upper())
    if not country or not country.get("coordinates"):
        raise HTTPException(status_code=404, detail="Country not found")
    cache_name = f"weather_{country['code']}.json"
    cached = _cached(cache_name, WEATHER_TTL)
    if cached:
        return cached
    lat, lng = country["coordinates"]["lat"], country["coordinates"]["lng"]
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}"
        "&current=temperature_2m,weather_code,wind_speed_10m"
        "&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&forecast_days=7&timezone=auto"
    )
    try:
        raw = _get_json(url)
        daily = raw["daily"]
        payload = {
            "available": True, "place": country.get("capital", ""), "source": "Open-Meteo",
            "current": {
                "temperature_c": raw["current"]["temperature_2m"],
                "wind_kmh": raw["current"]["wind_speed_10m"],
                "summary": WEATHER_TEXT.get(raw["current"]["weather_code"], "Unknown"),
            },
            "daily": [
                {
                    "date": daily["time"][i], "min_c": daily["temperature_2m_min"][i], "max_c": daily["temperature_2m_max"][i],
                    "rain_mm": daily["precipitation_sum"][i], "summary": WEATHER_TEXT.get(daily["weather_code"][i], "Unknown"),
                }
                for i in range(len(daily["time"]))
            ],
        }
    except Exception:
        return {"available": False}
    _store(cache_name, payload)
    return payload


_CODE_IN_TEXT = re.compile(r"\(([A-Z]{3})\)")
CURRENCY_FALLBACK = {"PA": "USD"}


def currency_code(country: dict) -> str | None:
    match = _CODE_IN_TEXT.search(country.get("currency", ""))
    return match.group(1) if match else CURRENCY_FALLBACK.get(country["code"])


@router.get("/rates/{code}")
def exchange_rate(code: str):
    country = data()["countries"].get(code.upper())
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    currency = currency_code(country)
    if not currency:
        return {"available": False}
    rates = _cached("rates_usd.json", RATES_TTL)
    if rates is None:
        try:
            raw = _get_json("https://open.er-api.com/v6/latest/USD")
            if raw.get("result") != "success":
                return {"available": False}
            rates = {"rates": raw["rates"], "updated": raw.get("time_last_update_utc", "")}
        except Exception:
            return {"available": False}
        _store("rates_usd.json", rates)
    per_usd = rates["rates"].get(currency)
    if per_usd is None:
        return {"available": False, "currency": currency}
    return {"available": True, "currency": currency, "per_usd": per_usd, "updated": rates.get("updated", ""), "source": "open.er-api.com"}
