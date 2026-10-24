#!/usr/bin/env python3
"""Depth pass, Grade 4 Cooking: fill in real, hand-checked data_table
content for the 28 Grade 4 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 4 Cooking to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g4-l1": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"],
        ]),
    },
    "cooking-g4-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"],
            ["Ask an adult before using sharp tools", "Prevents injury"],
        ]),
    },
    "cooking-g4-l3": {
        "data_table": table(["Habit", "Why"], [
            ["Washing hands for 20 seconds", "Removes germs effectively"],
        ]),
    },
    "cooking-g4-l4": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "cooking-g4-l5": {
        "data_table": table(["Rule", "Why"], [
            ["Cut away from your body", "Prevents injury"], ["Use a cutting board", "Protects the counter and knife"],
        ]),
    },
    "cooking-g4-l6": {
        "data_table": table(["Breakfast Food", "Food Group"], [
            ["Oatmeal", "Grains"], ["Eggs", "Protein"],
        ]),
    },
    "cooking-g4-l7": {
        "data_table": table(["Ingredient", "Role"], [
            ["Bread", "Base of the sandwich"], ["Filling", "Provides flavor and nutrition"],
        ]),
    },
    "cooking-g4-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Baking", "Cooking food using dry heat in an oven"],
        ]),
    },
    "cooking-g4-l9": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g4-l10": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"], ["Knife and spoon", "Right of the plate"],
        ]),
    },
    "cooking-g4-l11": {
        "data_table": table(["Fruit/Vegetable", "Origin"], [
            ["Mango", "South Asia"], ["Tomato", "Central and South America"],
        ]),
    },
    "cooking-g4-l12": {
        "data_table": table(["Snack", "Key Ingredients"], [
            ["Fruit skewers", "Cut fruit on a stick"], ["Energy balls", "Oats, honey, peanut butter"],
        ]),
    },
    "cooking-g4-l14": {
        "data_table": table(["Storage Method", "Purpose"], [
            ["Refrigeration", "Slows bacterial growth"], ["Freezing", "Preserves food for longer periods"],
        ]),
    },
    "cooking-g4-l15": {
        "data_table": table(["Salad Ingredient", "Example"], [
            ["Greens", "Lettuce, spinach"], ["Dressing", "Olive oil and vinegar"],
        ]),
    },
    "cooking-g4-l16": {
        "data_table": table(["Dish", "Country of Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"], ["Biryani", "South Asia"],
        ]),
    },
    "cooking-g4-l17": {
        "data_table": table(["Food", "Source"], [
            ["Milk", "Cows"], ["Bread", "Wheat grown by farmers"],
        ]),
    },
    "cooking-g4-l18": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Meal planning", "Reduces buying more than needed"], ["Composting scraps", "Reduces landfill waste"],
        ]),
    },
    "cooking-g4-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Turn pot handles inward", "Prevents accidental spills"],
            ["Never leave the stove unattended", "Prevents burns and fires"],
        ]),
    },
    "cooking-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Doubling a recipe", "Multiplying each ingredient amount by 2"],
        ]),
    },
    "cooking-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Cooking with family", "Following kitchen safety rules together"],
        ]),
    },
    "cooking-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Preparing lunch", "Washing hands before making food"],
        ]),
    },
    "cooking-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Planning meals", "Including all major food groups"],
        ]),
    },
    "cooking-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Slicing fruit", "Cutting with adult supervision"],
        ]),
    },
    "cooking-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Weekend breakfast", "Making oatmeal with fruit"],
        ]),
    },
    "cooking-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Packing lunch", "Making a sandwich for school"],
        ]),
    },
    "cooking-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Baking with family", "Following a cookie recipe together"],
        ]),
    },
    "cooking-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Trying a new dish", "Reading the recipe fully before starting"],
        ]),
    },
    "cooking-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Family dinner", "Setting the table before eating"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Cooking lessons (completing 30/30).")


if __name__ == "__main__":
    main()
