#!/usr/bin/env python3
"""Depth pass, Grade 3 Cooking: fill in real, hand-checked data_table
content for the 18 Grade 3 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Cooking to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g3-l1": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"],
            ["Ask an adult before using sharp tools", "Prevents injury"],
        ]),
    },
    "cooking-g3-l2": {
        "data_table": table(["Tool", "Use"], [
            ["Measuring cup", "Measures liquids or dry ingredients"], ["Whisk", "Mixes ingredients together"],
        ]),
    },
    "cooking-g3-l3": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Fruits", "Apples, bananas"], ["Vegetables", "Carrots, broccoli"],
            ["Protein", "Chicken, beans"],
        ]),
    },
    "cooking-g3-l5": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g3-l6": {
        "data_table": table(["Step", "Why"], [
            ["Rinse under running water", "Removes dirt and bacteria"],
        ]),
    },
    "cooking-g3-l7": {
        "data_table": table(["Ingredient", "Role"], [
            ["Bread", "Base of the sandwich"], ["Filling (cheese, veggies)", "Provides flavor and nutrition"],
        ]),
    },
    "cooking-g3-l8": {
        "data_table": table(["Fruit", "Preparation"], [
            ["Apple", "Wash, slice"], ["Banana", "Peel, slice"],
        ]),
    },
    "cooking-g3-l9": {
        "data_table": table(["Snack", "Key Ingredients"], [
            ["Energy balls", "Oats, honey, peanut butter"], ["Fruit skewers", "Cut fruit on a stick"],
        ]),
    },
    "cooking-g3-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Baking", "Cooking food using dry heat in an oven"],
        ]),
    },
    "cooking-g3-l11": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"], ["Knife and spoon", "Right of the plate"],
        ]),
    },
    "cooking-g3-l12": {
        "data_table": table(["Dish", "Country of Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"], ["Biryani", "South Asia"],
        ]),
    },
    "cooking-g3-l13": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Ingredients list", "What is in the food"], ["Expiration date", "When the food should be eaten by"],
        ]),
    },
    "cooking-g3-l14": {
        "data_table": table(["Food", "Source"], [
            ["Milk", "Cows"], ["Bread", "Wheat grown by farmers"],
        ]),
    },
    "cooking-g3-l15": {
        "data_table": table(["Smoothie Ingredient", "Example"], [
            ["Fruit", "Banana, berries"], ["Liquid", "Milk or yogurt"],
        ]),
    },
    "cooking-g3-l16": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"],
        ]),
    },
    "cooking-g3-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Keep raw meat separate from other foods", "Prevents cross-contamination"],
            ["Cook food to a safe temperature", "Kills harmful bacteria"],
        ]),
    },
    "cooking-g3-l18": {
        "data_table": table(["Holiday", "Traditional Food"], [
            ["Eid al-Fitr", "Sweet dishes like sheer khurma"], ["Thanksgiving", "Roast turkey"],
        ]),
    },
    "cooking-g3-l19": {
        "data_table": table(["Herb", "Common Use"], [
            ["Basil", "Italian dishes"], ["Mint", "Teas and desserts"],
        ]),
    },
    "cooking-g3-l20": {
        "data_table": table(["Bread Ingredient", "Purpose"], [
            ["Flour", "Provides structure"], ["Yeast", "Makes the dough rise"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Cooking lessons (completing 20/20).")


if __name__ == "__main__":
    main()
