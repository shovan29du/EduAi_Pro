from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_cuisine_overview():
    r = client.get("/api/cuisine")
    assert r.status_code == 200
    data = r.json()
    ids = [c["id"] for c in data["cuisines"]]
    assert "indian" in ids
    assert "italian" in ids


def test_cuisine_detail():
    r = client.get("/api/cuisine/indian")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "indian"
    assert data["famous_dishes"]
    assert data["quiz"]


def test_cuisine_detail_not_found():
    assert client.get("/api/cuisine/atlantis").status_code == 404


def test_cuisine_food_history():
    r = client.get("/api/cuisine-detail/food-history")
    assert r.status_code == 200
    data = r.json()
    assert len(data["timeline"]) >= 10


def test_cuisine_cooking_techniques():
    r = client.get("/api/cuisine-detail/techniques")
    assert r.status_code == 200
    data = r.json()
    assert len(data["categories"]) >= 3
    for cat in data["categories"]:
        assert cat["techniques"]


def test_cuisine_recipes_at_least_1000():
    r = client.get("/api/cuisine-detail/recipes?limit=1")
    assert r.status_code == 200
    assert r.json()["total"] >= 1500


def test_cuisine_recipes_no_pork():
    total = client.get("/api/cuisine-detail/recipes?limit=1").json()["total"]
    checked = 0
    offset = 0
    while offset < total:
        page = client.get(f"/api/cuisine-detail/recipes?limit=200&offset={offset}").json()
        for recipe in page["recipes"]:
            assert "pork" not in recipe["name"].lower()
            assert recipe["pork_free"] is True
            checked += 1
        offset += 200
    assert checked == total


def test_cuisine_recipes_filter_by_cuisine():
    r = client.get("/api/cuisine-detail/recipes?cuisine=indian&limit=1200")
    data = r.json()
    assert data["total"] > 0
    for recipe in data["recipes"]:
        assert recipe["cuisine_id"] == "indian"


def test_cuisine_recipes_filter_by_protein():
    r = client.get("/api/cuisine-detail/recipes?protein=Beef&limit=1200")
    data = r.json()
    assert data["total"] > 0
    for recipe in data["recipes"]:
        assert recipe["protein"] == "Beef"


def test_cuisine_recipes_search():
    r = client.get("/api/cuisine-detail/recipes?q=Butter Chicken")
    data = r.json()
    assert any(recipe["name"] == "Butter Chicken" for recipe in data["recipes"])


def test_cuisine_recipe_detail():
    r = client.get("/api/cuisine-detail/recipes/recipe_indian_0001")
    assert r.status_code == 200
    data = r.json()
    assert data["name"]
    assert data["links"]["video"]
    assert data["links"]["image_search"]
    assert data["links"]["wikipedia"]


def test_cuisine_recipe_detail_not_found():
    assert client.get("/api/cuisine-detail/recipes/does-not-exist").status_code == 404


def test_cuisine_recipe_cuisine_list():
    r = client.get("/api/cuisine-detail/recipe-cuisines")
    assert r.status_code == 200
    data = r.json()
    assert len(data["cuisines"]) >= 20
