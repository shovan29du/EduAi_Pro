from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_css_art():
    resp = client.get("/api/css-art")
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "CSS Art Gallery"
    assert len(data["pieces"]) >= 20
    # list view is metadata-only, no full source
    for piece in data["pieces"]:
        assert "source" not in piece
        assert piece["title"]


def test_list_css_art_ids_are_unique():
    data = client.get("/api/css-art").json()
    ids = [p["id"] for p in data["pieces"]]
    assert len(ids) == len(set(ids))


def test_get_single_css_art_piece():
    listing = client.get("/api/css-art").json()
    first_id = listing["pieces"][0]["id"]
    resp = client.get(f"/api/css-art/{first_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == first_id
    assert "<html" in data["source"].lower()
    assert "<style" in data["source"].lower()


def test_get_unknown_css_art_piece_404():
    resp = client.get("/api/css-art/not-a-real-piece")
    assert resp.status_code == 404


def test_every_css_art_piece_is_self_contained_html():
    """Each piece must be safely embeddable directly as an iframe srcDoc --
    no reliance on relative local asset paths that would be missing once the
    piece is served from this app's own data file."""
    data = client.get("/api/css-art").json()
    for meta in data["pieces"]:
        piece = client.get(f"/api/css-art/{meta['id']}").json()
        source = piece["source"]
        assert "<html" in source.lower()
        assert 'src="./' not in source and 'src="../' not in source
        assert "url(./" not in source and "url(../" not in source
