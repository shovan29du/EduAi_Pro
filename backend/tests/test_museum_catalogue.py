"""The Virtual Museum holds real, individually named objects, not generic placeholders."""
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MUSEUM = json.loads((BASE / "data" / "virtual_museum" / "museum.json").read_text(encoding="utf-8"))
OBJECTS = [(gid, o) for gid, g in MUSEUM["galleries"].items() for o in g["objects"]]
MET = [o for _, o in OBJECTS if str(o["id"]).startswith("met_")]


def test_no_generic_country_and_type_cards_remain():
    assert not [o["name"] for _, o in OBJECTS if o.get("museum") == "Various world collections"]
    assert not [o["id"] for _, o in OBJECTS if re.fullmatch(r"wc_\d+", str(o["id"]))]
    assert not [g for g in MUSEUM["galleries"] if g.startswith("world_") and g != "world_heritage_treasures"]


def test_object_ids_are_unique_within_each_gallery():
    for gid, gallery in MUSEUM["galleries"].items():
        ids = [o["id"] for o in gallery["objects"]]
        assert len(ids) == len(set(ids)), gid
    assert len([o["id"] for o in MET]) == len({o["id"] for o in MET})


def test_met_catalogue_is_large_and_ranked():
    assert len(MET) >= 5000
    assert sorted(o["source_rank"] for o in MET) == list(range(1, len(MET) + 1))
    assert len({o["met_id"] for o in MET}) == len(MET)


def test_met_objects_are_complete_and_credited():
    for o in MET:
        assert all(o.get(k) for k in ("id", "name", "description", "significance", "museum", "origin", "category", "links", "quiz", "activity")), o["id"]
        assert o["id"] == f"met_{o['met_id']}" and o["source_id"] == f"met-{o['met_id']}"
        assert o["museum"].startswith("The Metropolitan Museum of Art")
        assert o["links"]["museum_object"].startswith("https://www.metmuseum.org/") and "virtual_tour" in o["links"]
        assert "CC0" in o["source"]
        quiz = o["quiz"]
        assert len(quiz["options"]) == 4 and len(set(quiz["options"])) == 4 and 0 <= quiz["answer"] < 4


def test_met_names_are_specific_not_bare_generic_words():
    bare = {"bowl", "plate", "vase", "cup", "dish", "jar", "figure", "panel", "fragment", "relief", "untitled", "basket", "shield", "chair", "stove"}
    assert not [o["name"] for o in MET if o["name"].strip().lower() in bare]
    assert len({o["name"] for o in MET}) == len(MET)  # titles shared by several works are told apart


def test_met_catalogue_includes_famous_works():
    names = " ".join(o["name"] for o in MET)
    for famous in ("Wheat Field with Cypresses", "Madame X", "The Temple of Dendur", "The Death of Socrates", "The Harvesters"):
        assert famous in names, famous


def test_the_museum_api_serves_the_new_galleries_with_local_picture_overlay():
    from fastapi.testclient import TestClient
    from app.main import app
    c = TestClient(app)
    overview = c.get("/api/museum").json()
    assert overview["total_objects"] == len(OBJECTS)
    ids = {g["id"] for g in overview["galleries"]}
    assert {"met_european_paintings", "met_egyptian_art", "met_islamic_art"} <= ids
    body = c.get("/api/museum/met_egyptian_art").json()
    assert body["objects"] and all(o["id"].startswith("met_") for o in body["objects"])
