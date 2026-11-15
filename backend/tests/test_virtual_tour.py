import json

import pytest
from fastapi.testclient import TestClient

from app import virtual_tour as vt
from app.main import app

client = TestClient(app)

COUNTRIES = [
    {"code": "FR", "name": "France", "capital": "Paris", "continent": "Europe", "currency": "Euro (EUR)", "flag_emoji": "🇫🇷",
     "coordinates": {"lat": 48.8566, "lng": 2.3522}, "landmarks": ["Eiffel Tower"]},
    {"code": "BR", "name": "Brazil", "capital": "Brasília", "continent": "Americas", "currency": "Brazilian real (BRL)",
     "coordinates": {"lat": -15.79, "lng": -47.88}},
    {"code": "US", "name": "United States", "capital": "Washington, D.C.", "continent": "Americas", "currency": "US dollar (USD)",
     "coordinates": {"lat": 38.9, "lng": -77.04}},
    {"code": "TR", "name": "Türkiye (Turkey)", "capital": "Ankara", "continent": "Asia/Europe", "currency": "Turkish lira (TRY)",
     "coordinates": {"lat": 39.93, "lng": 32.85}},
    {"code": "PA", "name": "Panama", "capital": "Panama City", "continent": "Americas", "currency": "Panamanian balboa / US dollar",
     "coordinates": {"lat": 8.98, "lng": -79.52}},
    {"code": "NR", "name": "Nauru", "capital": "Yaren", "continent": "Oceania", "currency": "Australian dollar (AUD)"},
]
TOUR = {"countries": {
    "FR": {
        "places": [
            {"name": "Eiffel Tower", "type": "architecture"}, {"name": "Louvre Museum", "type": "museum"},
            {"name": "Gorges du Verdon", "type": "nature"}, {"name": "Mont-Saint-Michel", "type": "attraction"},
        ],
        "cities": ["Paris", "Lyon"],
        "guide": {"tier": "$$$", "transport": "TGV trains", "stay": "Hotels", "food": "Cheese", "buy": "Perfume", "warn": "Pickpockets", "climate": "Mild", "cost": "Pricey"},
    },
    "BR": {"places": [{"name": "Iguazu Falls", "type": "nature"}], "cities": ["Brasília", "Rio de Janeiro"], "guide": None},
}}


TRIPS = [
    {"id": "route-napoleon", "name": "Route Napoleon", "countries": ["FR"], "start": "Golfe-Juan", "end": "Grenoble",
     "via": ["Grasse", "Gap"], "km": 325, "duration": "2 days", "best_time": "May to September", "kind": "historic",
     "summary": "Follow Napoleon's 1815 return.", "highlights": ["Grasse", "Castellane", "Gap"], "tip": "Passes can be icy."},
    {"id": "pan-american", "name": "Pan-American Highway", "countries": ["US", "BR"], "start": "Prudhoe Bay", "end": "Ushuaia",
     "via": [], "km": 30000, "duration": "6-12 months", "best_time": "Varies", "kind": "cross-country",
     "summary": "Arctic to Patagonia.", "highlights": ["Alaska", "Andes", "Patagonia"], "tip": "No road at the Darien Gap."},
]


@pytest.fixture(autouse=True)
def _fixture_data(monkeypatch, tmp_path):
    countries = tmp_path / "countries.json"
    countries.write_text(json.dumps({"countries": COUNTRIES}), encoding="utf-8")
    tour = tmp_path / "tour.json"
    tour.write_text(json.dumps(TOUR), encoding="utf-8")
    monkeypatch.setattr(vt, "COUNTRIES_PATH", countries)
    monkeypatch.setattr(vt, "TOUR_PATH", tour)
    trips = tmp_path / "road_trips.json"
    trips.write_text(json.dumps({"road_trips": TRIPS}), encoding="utf-8")
    monkeypatch.setattr(vt, "TRIPS_PATH", trips)
    monkeypatch.setattr(vt, "CACHE_DIR", tmp_path / "cache")
    vt._load.cache_clear()
    yield
    vt._load.cache_clear()


def test_continents_split_the_americas_and_place_transcontinental_countries_once():
    ids = {c["id"]: c for c in client.get("/api/virtual-tour").json()["continents"]}
    assert ids["south-america"]["country_count"] == 1 and ids["north-america"]["country_count"] == 2  # BR vs US+PA
    assert ids["europe"]["country_count"] == 1 and ids["asia"]["country_count"] == 1  # Turkey only in Asia
    assert ids["europe"]["place_count"] == 4
    totals = client.get("/api/virtual-tour").json()["totals"]
    assert totals == {"countries": 6, "places": 5, "cities": 4, "road_trips": 2}


def test_continent_listing_and_unknown_continent():
    body = client.get("/api/virtual-tour/continents/europe").json()
    assert [c["code"] for c in body["countries"]] == ["FR"]
    assert body["countries"][0]["place_count"] == 4 and body["countries"][0]["flag_emoji"] == "🇫🇷"
    assert client.get("/api/virtual-tour/continents/atlantis").status_code == 404


def test_country_page_has_places_cities_guide_and_links_for_each():
    body = client.get("/api/virtual-tour/countries/fr").json()
    assert body["continent"] == "Europe" and body["profile"]["capital"] == "Paris" and body["currency_code"] == "EUR"
    eiffel = next(p for p in body["places"] if p["name"] == "Eiffel Tower")
    assert eiffel["type"] == "architecture"
    links = eiffel["links"]
    assert links["video"].startswith("https://www.youtube.com/results?search_query=Eiffel+Tower+France+virtual+tour+4K")
    assert "Eiffel+Tower+France+travel+blog" in links["blog"]
    assert links["photos"].startswith("https://commons.wikimedia.org/w/index.php?search=Eiffel+Tower+France")
    assert links["map"].startswith("https://www.google.com/maps/search/?api=1&query=Eiffel+Tower+France")
    assert links["earth"] == "https://earth.google.com/web/search/Eiffel%20Tower%2C%20France"
    paris = body["cities"][0]
    assert paris["name"] == "Paris" and paris["is_capital"] is True
    assert paris["links"]["earth_3d"] == "https://earth.google.com/web/search/Paris%2C%20France"
    assert "4K+walking+tour" in paris["links"]["video"] and paris["links"]["hotels"].startswith("https://www.booking.com/")
    assert body["guide"]["tier"] == "$$$"
    assert body["links"]["video"].startswith("https://www.youtube.com/") and body["links"]["blog"].startswith("https://www.google.com/")
    assert body["links"]["photos"].startswith("https://commons.wikimedia.org/")
    assert body["links"]["wikivoyage"] == "https://en.wikivoyage.org/wiki/France"
    assert body["links"]["cost_of_living"].endswith("country=France")


def test_country_names_use_plain_titles_in_searches_and_unknown_countries_404():
    tr = client.get("/api/virtual-tour/countries/TR").json()
    assert tr["links"]["wikivoyage"] == "https://en.wikivoyage.org/wiki/Turkey"
    assert "Turkey" in tr["links"]["advisory"] and "T%C3%BCrkiye" not in tr["links"]["advisory"]
    assert tr["places"] == [] and tr["guide"] is None  # countries without authored data still load
    assert client.get("/api/virtual-tour/countries/ZZ").status_code == 404


def test_search_finds_countries_places_and_cities():
    body = client.get("/api/virtual-tour/search", params={"q": "louvre"}).json()
    assert [p["name"] for p in body["places"]] == ["Louvre Museum"] and body["places"][0]["country"] == "France"
    assert body["places"][0]["links"]["video"].startswith("https://www.youtube.com/")
    assert [c["name"] for c in client.get("/api/virtual-tour/search", params={"q": "rio"}).json()["cities"]] == ["Rio de Janeiro"]
    assert [c["code"] for c in client.get("/api/virtual-tour/search", params={"q": "paris"}).json()["countries"]] == ["FR"]
    assert client.get("/api/virtual-tour/search", params={"q": "a"}).json() == {"countries": [], "places": [], "cities": []}


class _Resp:
    def __init__(self, payload): self._b = json.dumps(payload).encode()
    def read(self): return self._b
    def __enter__(self): return self
    def __exit__(self, *a): return False


WEATHER = {
    "current": {"temperature_2m": 12.5, "weather_code": 3, "wind_speed_10m": 9.0},
    "daily": {"time": ["2026-11-15", "2026-11-16"], "weather_code": [61, 0], "temperature_2m_max": [14, 16],
              "temperature_2m_min": [8, 9], "precipitation_sum": [2.5, 0.0]},
}


def test_live_weather_is_fetched_for_the_capital_and_cached(monkeypatch):
    calls = []
    monkeypatch.setattr(vt, "urlopen", lambda req, timeout=0: calls.append(req.full_url) or _Resp(WEATHER))
    body = client.get("/api/virtual-tour/weather/FR").json()
    assert body["available"] is True and body["place"] == "Paris"
    assert body["current"] == {"temperature_c": 12.5, "wind_kmh": 9.0, "summary": "Overcast"}
    assert body["daily"][0] == {"date": "2026-11-15", "min_c": 8, "max_c": 14, "rain_mm": 2.5, "summary": "Light rain"}
    assert "latitude=48.8566" in calls[0] and "api.open-meteo.com" in calls[0]
    assert client.get("/api/virtual-tour/weather/FR").json() == body and len(calls) == 1


def test_weather_failure_is_reported_quietly_and_not_cached(monkeypatch, tmp_path):
    def down(*a, **k):
        raise OSError("offline")

    monkeypatch.setattr(vt, "urlopen", down)
    assert client.get("/api/virtual-tour/weather/FR").json() == {"available": False}
    assert not (tmp_path / "cache").exists()
    assert client.get("/api/virtual-tour/weather/NR").status_code == 404  # no coordinates
    assert client.get("/api/virtual-tour/weather/ZZ").status_code == 404


def test_exchange_rate_uses_the_currency_code_and_caches_the_whole_table(monkeypatch):
    calls = []
    table = {"result": "success", "time_last_update_utc": "Sun, 15 Nov 2026", "rates": {"EUR": 0.92, "BRL": 5.4, "USD": 1, "TRY": 41.0, "AUD": 1.5}}
    monkeypatch.setattr(vt, "urlopen", lambda req, timeout=0: calls.append(1) or _Resp(table))
    eur = client.get("/api/virtual-tour/rates/FR").json()
    assert eur == {"available": True, "currency": "EUR", "per_usd": 0.92, "updated": "Sun, 15 Nov 2026", "source": "open.er-api.com"}
    assert client.get("/api/virtual-tour/rates/BR").json()["per_usd"] == 5.4
    assert client.get("/api/virtual-tour/rates/PA").json()["currency"] == "USD"  # code-less "balboa / US dollar"
    assert len(calls) == 1


def test_exchange_rate_unavailable_cases(monkeypatch):
    monkeypatch.setattr(vt, "urlopen", lambda *a, **k: _Resp({"result": "error"}))
    assert client.get("/api/virtual-tour/rates/FR").json() == {"available": False}
    monkeypatch.setattr(vt, "urlopen", lambda *a, **k: _Resp({"result": "success", "rates": {"EUR": 1}}))
    assert client.get("/api/virtual-tour/rates/BR").json() == {"available": False, "currency": "BRL"}
    assert client.get("/api/virtual-tour/rates/ZZ").status_code == 404


def test_road_trip_links_include_a_driving_route_with_waypoints():
    body = client.get("/api/virtual-tour/road-trips").json()
    assert body["total"] == 2 and body["kinds"] == ["cross-country", "historic"]
    napoleon = next(t for t in body["road_trips"] if t["id"] == "route-napoleon")
    links = napoleon["links"]
    assert links["route"] == ("https://www.google.com/maps/dir/?api=1&origin=Golfe-Juan&destination=Grenoble"
                              "&travelmode=driving&waypoints=Grasse%7CGap")
    assert "Route+Napoleon+road+trip+drive+4K" in links["video"] and "road+trip+itinerary+blog" in links["blog"]
    assert links["photos"].startswith("https://commons.wikimedia.org/") and links["earth"].endswith("Golfe-Juan")
    assert napoleon["country_names"] == ["France"] and napoleon["continent_ids"] == ["europe"]
    pan = next(t for t in body["road_trips"] if t["id"] == "pan-american")
    assert "waypoints" not in pan["links"]["route"]
    assert pan["continent_ids"] == ["north-america", "south-america"]


def test_road_trips_can_be_filtered_and_appear_on_country_pages():
    assert [t["id"] for t in client.get("/api/virtual-tour/road-trips", params={"continent": "europe"}).json()["road_trips"]] == ["route-napoleon"]
    assert [t["id"] for t in client.get("/api/virtual-tour/road-trips", params={"continent": "south-america"}).json()["road_trips"]] == ["pan-american"]
    assert [t["id"] for t in client.get("/api/virtual-tour/road-trips", params={"country": "br"}).json()["road_trips"]] == ["pan-american"]
    assert [t["id"] for t in client.get("/api/virtual-tour/road-trips", params={"kind": "historic"}).json()["road_trips"]] == ["route-napoleon"]
    assert [t["id"] for t in client.get("/api/virtual-tour/road-trips", params={"q": "patagonia"}).json()["road_trips"]] == ["pan-american"]
    assert client.get("/api/virtual-tour/road-trips", params={"continent": "atlantis"}).status_code == 404
    assert [t["id"] for t in client.get("/api/virtual-tour/countries/FR").json()["road_trips"]] == ["route-napoleon"]
    assert client.get("/api/virtual-tour/countries/TR").json()["road_trips"] == []
    overview = client.get("/api/virtual-tour").json()
    assert overview["totals"]["road_trips"] == 2
    assert {c["id"]: c["road_trip_count"] for c in overview["continents"]}["north-america"] == 1
