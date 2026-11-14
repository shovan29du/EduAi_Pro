from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sports_overview():
    r = client.get("/api/sports")
    assert r.status_code == 200
    data = r.json()
    ids = [s["id"] for s in data["sports"]]
    assert "football" in ids
    assert "cricket" in ids


def test_sport_detail():
    r = client.get("/api/sports/football")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "football"
    assert data["label"]


def test_sport_detail_not_found():
    assert client.get("/api/sports/quidditch").status_code == 404


def test_sports_detail_football_worldcup():
    assert client.get("/api/sports-detail/football-worldcup").status_code == 200


def test_sports_detail_football_leagues():
    assert client.get("/api/sports-detail/football-leagues").status_code == 200


def test_sports_detail_cricket_worldcup():
    assert client.get("/api/sports-detail/cricket-worldcup").status_code == 200


def test_sports_detail_cricket_leagues():
    assert client.get("/api/sports-detail/cricket-leagues").status_code == 200


def test_sports_detail_tennis():
    assert client.get("/api/sports-detail/tennis").status_code == 200


def test_sports_detail_players():
    r = client.get("/api/sports-detail/players")
    assert r.status_code == 200
    ids = [s["id"] for s in r.json()["sports"]]
    assert "football" in ids


def test_sports_players_by_sport():
    r = client.get("/api/sports-detail/players/football")
    assert r.status_code == 200
    assert r.json()["id"] == "football"


def test_sports_players_by_sport_not_found():
    assert client.get("/api/sports-detail/players/quidditch").status_code == 404
