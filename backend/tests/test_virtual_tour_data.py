import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
DATA = Path(__file__).resolve().parents[1] / "data"
COUNTRIES = json.loads((DATA / "countries" / "countries.json").read_text(encoding="utf-8"))["countries"]
TOUR = json.loads((DATA / "virtual_tour" / "tour.json").read_text(encoding="utf-8"))["countries"]
GUIDE_FIELDS = {"tier", "cost", "transport", "stay", "food", "buy", "warn", "climate"}


def test_every_country_has_places_cities_and_a_complete_guide():
    assert {c["code"] for c in COUNTRIES} == set(TOUR)
    for code, entry in TOUR.items():
        assert len(entry["places"]) >= 5, code
        assert len(entry["cities"]) >= 1, code
        assert set(entry["guide"]) == GUIDE_FIELDS, code
        assert entry["guide"]["tier"] in {"$", "$$", "$$$", "$$$$"}, code
        assert all(len(v) >= 3 for v in entry["guide"].values()), code


def test_places_have_valid_types_and_no_duplicates_or_leftovers():
    for code, entry in TOUR.items():
        names = [p["name"].lower() for p in entry["places"]]
        assert len(names) == len(set(names)), code
        for place in entry["places"]:
            assert place["type"] in {"attraction", "nature", "museum", "architecture"}, (code, place)
            assert ";" not in place["name"] and "|" not in place["name"] and "TODO" not in place["name"], (code, place)
        assert len(set(entry["cities"])) == len(entry["cities"]), code


@pytest.mark.parametrize("kind", ["nature", "museum", "architecture", "attraction"])
def test_each_kind_of_place_is_well_represented_worldwide(kind):
    assert sum(p["type"] == kind for e in TOUR.values() for p in e["places"]) >= 250


def test_api_overview_covers_the_whole_world_in_six_continents():
    body = client.get("/api/virtual-tour").json()
    assert body["totals"]["countries"] == len(COUNTRIES) >= 190
    assert body["totals"]["places"] >= 2000 and body["totals"]["cities"] >= 500
    assert [c["id"] for c in body["continents"]] == ["africa", "asia", "europe", "north-america", "south-america", "oceania"]
    assert all(c["country_count"] > 0 and c["place_count"] > 0 for c in body["continents"])
    assert sum(c["country_count"] for c in body["continents"]) == len(COUNTRIES)


def test_a_real_country_page_has_every_link_type_for_every_place_and_city():
    body = client.get("/api/virtual-tour/countries/JP").json()
    assert body["continent"] == "Asia" and body["profile"]["capital"] == "Tokyo"
    assert {p["type"] for p in body["places"]} == {"attraction", "nature", "museum", "architecture"}
    for place in body["places"]:
        assert {"video", "blog", "photos", "map", "earth"} <= set(place["links"])
        assert all(url.startswith("https://") for url in place["links"].values())
    for city in body["cities"]:
        assert {"video", "blog", "photos", "map", "earth_3d", "hotels"} <= set(city["links"])
    assert body["cities"][0]["is_capital"] is True
    assert body["guide"]["tier"] == "$$$" and "Shinkansen" in body["guide"]["transport"]


def test_americas_are_split_and_transcontinental_countries_listed_once():
    by_code = {s["code"]: s["continent_id"] for s in client.get("/api/virtual-tour/countries").json()["countries"]}
    assert by_code["BR"] == "south-america" and by_code["US"] == "north-america" and by_code["MX"] == "north-america"
    assert by_code["TR"] == "asia" and by_code["RU"] == "europe" and by_code["CY"] == "europe"
    assert client.get("/api/virtual-tour/continents/south-america").json()["countries"][0]["code"] in by_code
