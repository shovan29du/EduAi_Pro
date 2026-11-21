"""Every rendered Practical Skills module and Survival Skills entry should
carry a wiki_title for a real photo lookup (PracticalSkills.jsx /
SurvivalSkills.jsx already render it), and the Cooking / Outdoor & Navigation
pilot batches should carry genuinely correct data_table / formulae content.
"""
import json

from app.main import BASE_DIR

PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"


def _practical_modules():
    data = json.loads(PRACTICAL_PATH.read_text(encoding="utf-8"))
    return [m for p in data["pathways"].values() for m in p.get("modules", [])]


def _survival_skills():
    data = json.loads(SURVIVAL_PATH.read_text(encoding="utf-8"))
    return [s for cat in data["categories"].values() for s in cat]


def test_every_practical_skills_module_has_a_wiki_title():
    modules = _practical_modules()
    assert len(modules) >= 1800
    missing = [m["title"] for m in modules if not m.get("wiki_title")]
    assert not missing, f"{len(missing)} modules missing wiki_title, e.g. {missing[:5]}"


def test_every_survival_skill_has_a_wiki_title():
    skills = _survival_skills()
    assert len(skills) >= 400
    missing = [s["name"] for s in skills if not s.get("wiki_title")]
    assert not missing, f"{len(missing)} skills missing wiki_title, e.g. {missing[:5]}"


def test_cooking_pilot_modules_have_real_reference_data():
    modules = {m["title"]: m for m in _practical_modules()}

    safety = modules["Kitchen Safety Basics"]
    assert safety["data_table"]["headers"] == ["Hazard", "Risk", "Prevention"]
    assert any(row[0] == "Sharp knives" for row in safety["data_table"]["rows"])

    rice = modules["Cooking Perfect Rice and Grains"]
    ratios = {row[0]: row[1] for row in rice["data_table"]["rows"]}
    assert ratios["White rice"] == "2:1"
    assert ratios["Brown rice"] == "2.5:1"


def test_outdoor_navigation_pilot_skills_have_real_reference_data():
    skills = {s["name"]: s for s in _survival_skills()}

    compass = skills["Using a Compass"]
    bearings = {row[0]: row[1] for row in compass["data_table"]["rows"]}
    assert bearings["North"] == "0° / 360°"
    assert bearings["East"] == "90°"
    assert bearings["South"] == "180°"
    assert bearings["West"] == "270°"

    boiling = skills["Water Purification by Boiling"]
    assert any("1 minute" in f for f in boiling["formulae"])

    hypothermia = skills["Recognizing and Preventing Hypothermia"]
    stages = [row[0] for row in hypothermia["data_table"]["rows"]]
    assert stages == ["Mild", "Moderate", "Severe"]
