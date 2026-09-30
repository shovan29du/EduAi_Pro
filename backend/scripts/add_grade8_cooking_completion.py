#!/usr/bin/env python3
"""Depth pass, Grade 8 Cooking: fill in real, hand-checked data_table
content for the 38 Grade 8 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Cooking to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g8-l1": {
        "data_table": table(["Planning Step", "Purpose"], [
            ["List meals for the week", "Saves time and reduces waste"], ["Set a budget", "Controls spending"],
        ]),
    },
    "cooking-g8-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"],
        ]),
    },
    "cooking-g8-l3": {
        "data_table": table(["Cut Type", "Description"], [
            ["Julienne", "Thin matchstick strips"], ["Dice", "Small cubes"],
        ]),
    },
    "cooking-g8-l4": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"],
        ]),
    },
    "cooking-g8-l5": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"],
        ]),
    },
    "cooking-g8-l6": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g8-l8": {
        "data_table": table(["Method", "Description"], [
            ["Frying", "Cooking in hot oil"], ["Sauteing", "Quick cooking in a small amount of fat"],
        ]),
    },
    "cooking-g8-l9": {
        "data_table": table(["Method", "Description"], [
            ["Baking", "Dry-heat cooking in an oven"], ["Roasting", "Dry-heat cooking, often for meats/vegetables"],
        ]),
    },
    "cooking-g8-l10": {
        "data_table": table(["Method", "Description"], [
            ["Steaming", "Cooking with vapor over boiling water"], ["Grilling", "Cooking over direct heat"],
        ]),
    },
    "cooking-g8-l12": {
        "data_table": table(["Breakfast Food", "Food Group"], [
            ["Oatmeal", "Grains"], ["Eggs", "Protein"],
        ]),
    },
    "cooking-g8-l13": {
        "data_table": table(["Salad Element", "Example"], [
            ["Base", "Leafy greens"], ["Dressing", "Olive oil and vinegar"],
        ]),
    },
    "cooking-g8-l14": {
        "data_table": table(["Soup Element", "Example"], [
            ["Base", "Broth or stock"], ["Aromatics", "Onion, garlic, celery"],
        ]),
    },
    "cooking-g8-l15": {
        "data_table": table(["Bread Ingredient", "Purpose"], [
            ["Flour", "Provides structure"], ["Yeast", "Makes the dough rise"],
        ]),
    },
    "cooking-g8-l16": {
        "data_table": table(["Step", "Purpose"], [
            ["Creaming butter and sugar", "Adds air for a lighter texture"],
        ]),
    },
    "cooking-g8-l17": {
        "data_table": table(["Pastry Type", "Example"], [
            ["Shortcrust", "Pie crusts"], ["Puff pastry", "Croissants, flaky layers"],
        ]),
    },
    "cooking-g8-l18": {
        "data_table": table(["Preservation Method", "Example"], [
            ["Canning", "Sealing food in jars"], ["Freezing", "Preserves food for longer periods"],
        ]),
    },
    "cooking-g8-l19": {
        "data_table": table(["Storage Method", "Purpose"], [
            ["Refrigeration", "Slows bacterial growth"],
        ]),
    },
    "cooking-g8-l20": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"],
        ]),
    },
    "cooking-g8-l21": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooked in the shell in water"], ["Scrambling", "Whisked and cooked in a pan"],
        ]),
    },
    "cooking-g8-l22": {
        "data_table": table(["Grain", "Common Use"], [
            ["Rice", "Side dish or base for many meals"],
        ]),
    },
    "cooking-g8-l23": {
        "data_table": table(["Pasta Shape", "Common Use"], [
            ["Spaghetti", "Long noodles, sauces cling to the surface"],
        ]),
    },
    "cooking-g8-l24": {
        "data_table": table(["Protein Source", "Type"], [
            ["Lentils", "Plant-based"], ["Tofu", "Plant-based"],
        ]),
    },
    "cooking-g8-l25": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Mexican", "Tacos"],
        ]),
    },
    "cooking-g8-l26": {
        "data_table": table(["Sauce", "Common Use"], [
            ["Tomato sauce", "Pasta dishes"],
        ]),
    },
    "cooking-g8-l27": {
        "data_table": table(["Dessert Type", "Example"], [
            ["Baked", "Cookies, cake"],
        ]),
    },
    "cooking-g8-l28": {
        "data_table": table(["Food", "Example Portion"], [
            ["Cooked rice", "About the size of a fist"],
        ]),
    },
    "cooking-g8-l29": {
        "data_table": table(["Step", "Purpose"], [
            ["Cook in bulk", "Saves time during the week"],
        ]),
    },
    "cooking-g8-l30": {
        "data_table": table(["Diet Type", "Restriction"], [
            ["Vegetarian", "No meat"], ["Gluten-free", "No wheat/gluten"],
        ]),
    },
    "cooking-g8-l31": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"],
        ]),
    },
    "cooking-g8-l32": {
        "data_table": table(["Tool", "Use"], [
            ["Measuring cup", "Measures liquids or dry ingredients"],
        ]),
    },
    "cooking-g8-l33": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Composting scraps", "Reduces landfill waste"],
        ]),
    },
    "cooking-g8-l34": {
        "data_table": table(["Beverage Type", "Example"], [
            ["Smoothie", "Blended fruit and milk/yogurt"],
        ]),
    },
    "cooking-g8-l35": {
        "data_table": table(["Benefit", "Detail"], [
            ["Seasonal produce", "Often fresher and less expensive"],
        ]),
    },
    "cooking-g8-l36": {
        "data_table": table(["Grilling Technique", "Use"], [
            ["Direct heat", "Fast cooking, searing"], ["Indirect heat", "Slower cooking of larger cuts"],
        ]),
    },
    "cooking-g8-l37": {
        "data_table": table(["Fermented Food", "Made By"], [
            ["Yogurt", "Fermenting milk with bacteria cultures"],
        ]),
    },
    "cooking-g8-l38": {
        "data_table": table(["Legume", "Common Use"], [
            ["Lentils", "Soups and stews"], ["Chickpeas", "Hummus"],
        ]),
    },
    "cooking-g8-l39": {
        "data_table": table(["Presentation Tip", "Why"], [
            ["Balanced colors", "Makes the dish visually appealing"],
        ]),
    },
    "cooking-g8-l40": {
        "data_table": table(["Career", "Focus"], [
            ["Chef", "Prepares and oversees food in a restaurant"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Cooking lessons (completing 40/40).")


if __name__ == "__main__":
    main()
