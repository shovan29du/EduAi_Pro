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


def test_cuisine_overview_covers_top_thirty_with_history():
    r = client.get("/api/cuisine")
    data = r.json()
    assert len(data["cuisines"]) >= 30
    for cuisine in data["cuisines"]:
        detail = client.get(f"/api/cuisine/{cuisine['id']}").json()
        assert detail.get("history"), cuisine["id"]


CATEGORIES_TO_COVER = [
    "soup", "appetizer", "bread", "rice", "noodle", "pasta", "soupy_noodle",
    "curry", "vegetable", "salad", "drink", "hot_drink", "ice_cream", "dessert",
]


def test_cuisine_recipes_cover_requested_categories():
    for category in CATEGORIES_TO_COVER:
        r = client.get(f"/api/cuisine-detail/recipes?category={category}&limit=1")
        data = r.json()
        assert data["total"] > 0, f"no recipes found for category '{category}'"


def test_cuisine_recipes_cover_beef_chicken_fish_seafood():
    for protein in ["Beef", "Chicken", "Fish", "Seafood"]:
        r = client.get(f"/api/cuisine-detail/recipes?protein={protein}&limit=1")
        data = r.json()
        assert data["total"] > 0, f"no recipes found for protein '{protein}'"


def test_cuisine_recipes_ingredient_filter():
    r = client.get("/api/cuisine-detail/recipes?ingredient=saffron&limit=1200")
    data = r.json()
    assert data["total"] > 0
    for recipe in data["recipes"]:
        assert recipe["cuisine"]

    r2 = client.get("/api/cuisine-detail/recipes?ingredient=nonexistentxyz&limit=1")
    assert r2.json()["total"] == 0


NEW_REGIONAL_CUISINES = [
    "eastern_european", "balkan", "central_asian", "gulf_arabian", "baltic",
    "latin_american",
]


def test_new_regional_cuisines_have_history_and_recipes():
    for cuisine_id in NEW_REGIONAL_CUISINES:
        detail = client.get(f"/api/cuisine/{cuisine_id}").json()
        assert detail.get("history"), cuisine_id
        assert detail.get("region"), cuisine_id
        recipes = client.get(f"/api/cuisine-detail/recipes?cuisine={cuisine_id}&limit=1").json()
        assert recipes["total"] > 0, cuisine_id


def test_israeli_cuisine_removed():
    assert client.get("/api/cuisine/israeli").status_code == 404
    r = client.get("/api/cuisine-detail/recipes?cuisine=israeli&limit=1")
    assert r.json()["total"] == 0


SOUTHEAST_ASIAN_ADDITIONS = ["burmese", "lao", "cambodian"]


def test_southeast_asian_additions_have_history_and_recipes():
    for cuisine_id in SOUTHEAST_ASIAN_ADDITIONS:
        detail = client.get(f"/api/cuisine/{cuisine_id}").json()
        assert detail.get("history"), cuisine_id
        recipes = client.get(f"/api/cuisine-detail/recipes?cuisine={cuisine_id}&limit=1").json()
        assert recipes["total"] > 0, cuisine_id


def test_no_pork_or_haram_animal_dish_names():
    total = client.get("/api/cuisine-detail/recipes?limit=1").json()["total"]
    offset = 0
    banned = ["pork", "escargot", "snail", "frog", "kangaroo"]
    while offset < total:
        page = client.get(f"/api/cuisine-detail/recipes?limit=200&offset={offset}").json()
        for recipe in page["recipes"]:
            lname = recipe["name"].lower()
            for word in banned:
                assert word not in lname, f"{recipe['name']} contains banned word '{word}'"
        offset += 200


def test_duck_is_a_distinct_protein():
    r = client.get("/api/cuisine-detail/recipes?protein=Duck&limit=1")
    assert r.json()["total"] > 0


def test_ingredient_alternatives_has_halal_substitutes_section():
    r = client.get("/api/cuisine-detail/ingredient-alternatives")
    assert r.status_code == 200
    data = r.json()
    halal = next((c for c in data["categories"] if c["id"] == "halal_substitutes"), None)
    assert halal is not None
    bacon_item = next(item for item in halal["items"] if item["ingredient"].lower() == "pork bacon")
    assert any("chicken bacon" in alt.lower() for alt in bacon_item["alternatives"])


def test_herbs_spices_endpoint():
    r = client.get("/api/cuisine-detail/herbs-spices")
    assert r.status_code == 200
    data = r.json()
    assert len(data["items"]) >= 20
    for item in data["items"]:
        assert item["wiki_title"]
        assert item["description"]
        assert item["uses"]


def test_cooking_problems_endpoint():
    r = client.get("/api/cuisine-detail/cooking-problems")
    assert r.status_code == 200
    data = r.json()
    assert len(data["categories"]) >= 3
    for cat in data["categories"]:
        for problem in cat["problems"]:
            assert problem["fixes"]


def test_measurement_equivalents_endpoint():
    r = client.get("/api/cuisine-detail/measurement-equivalents")
    assert r.status_code == 200
    data = r.json()
    table_ids = [t["id"] for t in data["tables"]]
    assert "volume" in table_ids
    assert "oven_temperature" in table_ids


def test_cooking_techniques_have_links_and_related_recipes():
    r = client.get("/api/cuisine-detail/techniques")
    data = r.json()
    grilling = None
    for cat in data["categories"]:
        for t in cat["techniques"]:
            assert t["links"]["video"]
            assert t["links"]["text_guide"]
            if t["name"] == "Grilling":
                grilling = t
    assert grilling is not None
    assert len(grilling["related_recipes"]) > 0


def test_cooking_techniques_has_knife_skills_category():
    r = client.get("/api/cuisine-detail/techniques")
    data = r.json()
    knife = next((c for c in data["categories"] if c["id"] == "knife-skills"), None)
    assert knife is not None
    names = [t["name"] for t in knife["techniques"]]
    assert "Julienne" in names
    assert "Brunoise" in names
    assert len(knife["techniques"]) >= 8


def test_recipes_have_expanded_tea_coffee_drinks():
    hot = client.get("/api/cuisine-detail/recipes?category=hot_drink&limit=1200").json()
    drink = client.get("/api/cuisine-detail/recipes?category=drink&limit=1200").json()
    assert hot["total"] >= 20
    assert drink["total"] >= 20
    hot_names = [r["name"] for r in hot["recipes"]]
    assert "Italian Espresso" in hot_names
    assert "Cappuccino" in hot_names
