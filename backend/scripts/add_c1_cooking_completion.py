#!/usr/bin/env python3
"""Depth pass, C1 Cooking: fill in real, hand-checked data_table content
for the 69 C1 Cooking lessons not covered by the earlier breadth-first
batch. Brings C1 Cooking to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cooking-c1-l1": {
        "data_table": table(["Zone", "Safe Temperature"], [
            ["Danger zone", "40°F-140°F (4°C-60°C), where bacteria grow fastest"],
        ]),
    },
    "cooking-c1-l2": {
        "data_table": table(["Region", "Signature Flavor Base"], [
            ["Mediterranean", "Olive oil, garlic, lemon"], ["East Asian", "Soy sauce, ginger, sesame"],
        ]),
    },
    "cooking-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Maillard reaction", "A chemical reaction between amino acids and sugars that browns food and creates flavor"],
        ]),
    },
    "cooking-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["HACCP", "Hazard Analysis Critical Control Point, a systematic food safety process"],
        ]),
    },
    "cooking-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Food cost percentage", "The ratio of ingredient cost to menu price"],
        ]),
    },
    "cooking-c1-l7": {
        "data_table": table(["Region", "Historical Influence"], [
            ["French cuisine", "Codified by Escoffier into structured technique"],
        ]),
    },
    "cooking-c1-l8": {
        "data_table": table(["Technique", "Effect"], [
            ["Spherification", "Turns liquids into gel spheres using sodium alginate"],
        ]),
    },
    "cooking-c1-l9": {
        "data_table": table(["Taste", "Example"], [
            ["Umami", "Savory taste found in mushrooms, tomatoes, aged cheese"],
        ]),
    },
    "cooking-c1-l10": {
        "data_table": table(["Practice", "Benefit"], [
            ["Buying seasonal produce", "Reduces environmental impact and often improves flavor"],
        ]),
    },
    "cooking-c1-l11": {
        "data_table": table(["Role", "Responsibility"], [
            ["Executive chef", "Oversees kitchen operations and menu development"],
        ]),
    },
    "cooking-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Gluten", "A protein network in wheat flour that gives bread its structure"],
        ]),
    },
    "cooking-c1-l13": {
        "data_table": table(["Food", "Fermentation Agent"], [
            ["Sauerkraut", "Lactic acid bacteria"], ["Bread", "Yeast"],
        ]),
    },
    "cooking-c1-l14": {
        "data_table": table(["Macronutrient", "Role"], [
            ["Protein", "Builds and repairs body tissue"], ["Carbohydrate", "Primary energy source"],
        ]),
    },
    "cooking-c1-l15": {
        "data_table": table(["Element", "Purpose"], [
            ["Natural lighting", "Produces the most accurate, appetizing food color in photos"],
        ]),
    },
    "cooking-c1-l16": {
        "data_table": table(["Principle", "Example"], [
            ["Balancing intensity", "Pairing a light white wine with delicate fish"],
        ]),
    },
    "cooking-c1-l17": {
        "data_table": table(["Step", "Purpose"], [
            ["Writing a business plan", "Defines concept, budget, and target market before opening"],
        ]),
    },
    "cooking-c1-l18": {
        "data_table": table(["Concept", "Meaning"], [
            ["Foodways", "The cultural, social, and economic practices around food"],
        ]),
    },
    "cooking-c1-l19": {
        "data_table": table(["Certification", "Focus"], [
            ["ServSafe", "Food safety and sanitation"], ["Certified Executive Chef", "Advanced culinary leadership skill"],
        ]),
    },
    "cooking-c1-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Negative space", "Draws focus to the plated dish in a photo composition"],
        ]),
    },
    "cooking-c1-l21": {
        "data_table": table(["Cut", "Shape"], [
            ["Julienne", "Thin matchstick strips"], ["Brunoise", "Very fine dice"],
        ]),
    },
    "cooking-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Mise en place", "French for 'everything in its place,' prepping ingredients before cooking"],
        ]),
    },
    "cooking-c1-l23": {
        "data_table": table(["Stock Type", "Base"], [
            ["Chicken stock", "Chicken bones and aromatics"], ["Vegetable stock", "Mirepoix and vegetable trimmings"],
        ]),
    },
    "cooking-c1-l24": {
        "data_table": table(["Mother Sauce", "Base"], [
            ["Béchamel", "Milk thickened with a roux"], ["Velouté", "White stock thickened with a roux"],
        ]),
    },
    "cooking-c1-l25": {
        "data_table": table(["Technique", "Heat Level"], [
            ["Sautéing", "High heat, small amount of fat, constant motion"],
        ]),
    },
    "cooking-c1-l26": {
        "data_table": table(["Method", "Effect"], [
            ["Roasting", "Dry heat that browns the exterior while cooking through"],
        ]),
    },
    "cooking-c1-l27": {
        "data_table": table(["Method", "Effect"], [
            ["Braising", "Combines searing with slow, moist cooking to tenderize tough cuts"],
        ]),
    },
    "cooking-c1-l28": {
        "data_table": table(["Technique", "Effect"], [
            ["Direct grilling", "High, direct heat for quick-cooking foods"],
        ]),
    },
    "cooking-c1-l29": {
        "data_table": table(["Method", "Best For"], [
            ["Steaming", "Preserves nutrients and delicate texture"], ["Poaching", "Gentle cooking in barely simmering liquid"],
        ]),
    },
    "cooking-c1-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Kneading", "Develops gluten structure for bread's chewy texture"],
        ]),
    },
    "cooking-c1-l31": {
        "data_table": table(["Dough Type", "Use"], [
            ["Pâte brisée", "Basic shortcrust for pies and tarts"],
        ]),
    },
    "cooking-c1-l32": {
        "data_table": table(["Ingredient", "Function"], [
            ["Baking powder", "Chemical leavener that helps cakes rise"],
        ]),
    },
    "cooking-c1-l33": {
        "data_table": table(["Method", "Result"], [
            ["Poached egg", "Cooked gently in simmering water, soft yolk"], ["Hard-boiled egg", "Fully cooked yolk and white"],
        ]),
    },
    "cooking-c1-l34": {
        "data_table": table(["Method", "Effect on Vegetables"], [
            ["Blanching", "Briefly cooks and sets color before shocking in ice water"],
        ]),
    },
    "cooking-c1-l35": {
        "data_table": table(["Food", "Cooking Ratio"], [
            ["Rice", "Roughly 2:1 water to rice"], ["Lentils", "Roughly 3:1 water to lentils"],
        ]),
    },
    "cooking-c1-l36": {
        "data_table": table(["Ingredient", "Role"], [
            ["Semolina flour", "Gives fresh pasta its firm texture"],
        ]),
    },
    "cooking-c1-l37": {
        "data_table": table(["Type", "Feature"], [
            ["Clear soup", "Thin, strained broth-based"], ["Cream soup", "Thickened with roux, cream, or puree"],
        ]),
    },
    "cooking-c1-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Textural contrast", "Combines crisp and soft ingredients in one salad"],
        ]),
    },
    "cooking-c1-l39": {
        "data_table": table(["Ratio", "Use"], [
            ["3:1 oil to acid", "A classic vinaigrette base ratio"],
        ]),
    },
    "cooking-c1-l40": {
        "data_table": table(["Term", "Purpose"], [
            ["Marinade", "Adds flavor and can tenderize before cooking"], ["Brine", "A salt solution that keeps meat moist"],
        ]),
    },
    "cooking-c1-l41": {
        "data_table": table(["Spice", "Flavor Profile"], [
            ["Cumin", "Earthy, warm"], ["Cinnamon", "Sweet, warm"],
        ]),
    },
    "cooking-c1-l42": {
        "data_table": table(["Herb", "Common Use"], [
            ["Basil", "Italian and Southeast Asian dishes"], ["Cilantro", "Latin American and Asian dishes"],
        ]),
    },
    "cooking-c1-l43": {
        "data_table": table(["Practice", "Reason"], [
            ["Honing before each use", "Keeps the blade edge aligned between sharpenings"],
        ]),
    },
    "cooking-c1-l44": {
        "data_table": table(["Principle", "Purpose"], [
            ["Rule of odd numbers", "Odd groupings of food elements look more visually balanced"],
        ]),
    },
    "cooking-c1-l45": {
        "data_table": table(["Practice", "Benefit"], [
            ["Standardized portioning", "Controls food cost and ensures consistency"],
        ]),
    },
    "cooking-c1-l46": {
        "data_table": table(["Equipment", "Use"], [
            ["Immersion circulator", "Maintains precise water temperature for sous vide cooking"],
        ]),
    },
    "cooking-c1-l47": {
        "data_table": table(["Cut", "Source"], [
            ["Tenderloin", "The most tender cut, from along the spine"],
        ]),
    },
    "cooking-c1-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Deveining shrimp", "Removes the digestive tract for cleaner flavor and appearance"],
        ]),
    },
    "cooking-c1-l49": {
        "data_table": table(["Ingredient", "Function"], [
            ["Cream", "Adds richness and can be reduced to thicken sauces"],
        ]),
    },
    "cooking-c1-l50": {
        "data_table": table(["Practice", "Reason"], [
            ["Weighing ingredients", "More accurate and consistent than volume measurement in baking"],
        ]),
    },
    "cooking-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Lamination", "Folding butter into dough repeatedly to create flaky layers"],
        ]),
    },
    "cooking-c1-l52": {
        "data_table": table(["Method", "Ideal Oil Temperature"], [
            ["Deep frying", "350°F-375°F (175°C-190°C)"],
        ]),
    },
    "cooking-c1-l53": {
        "data_table": table(["Method", "How It Thickens"], [
            ["Roux", "Cooked flour and fat combination"], ["Slurry", "Cornstarch mixed with cold liquid"],
        ]),
    },
    "cooking-c1-l54": {
        "data_table": table(["Element", "Purpose"], [
            ["Composition", "Guides the viewer's eye through the plated dish"],
        ]),
    },
    "cooking-c1-l55": {
        "data_table": table(["Practice", "Benefit"], [
            ["Working stations in sequence", "Reduces bottlenecks during service"],
        ]),
    },
    "cooking-c1-l56": {
        "data_table": table(["Region", "Signature Dish"], [
            ["Southern US", "Fried chicken and biscuits"], ["Tex-Mex", "Fusion of Texan and Mexican flavors"],
        ]),
    },
    "cooking-c1-l57": {
        "data_table": table(["Element", "Feature"], [
            ["Mediterranean diet", "Emphasizes olive oil, vegetables, and lean protein"],
        ]),
    },
    "cooking-c1-l58": {
        "data_table": table(["Technique", "Region"], [
            ["Stir-frying", "China, uses very high heat and constant motion"],
        ]),
    },
    "cooking-c1-l59": {
        "data_table": table(["Element", "Purpose"], [
            ["Height and layering", "Adds visual interest to dessert plating"],
        ]),
    },
    "cooking-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Pastry chef", "Specializes in baked goods and desserts"], ["Food stylist", "Prepares food for visual presentation in media"],
        ]),
    },
    "cooking-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Auditing kitchen safety", "Checking storage temperatures against the danger zone"],
        ]),
    },
    "cooking-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing flavor bases", "Contrasting a Mediterranean and East Asian sauce foundation"],
        ]),
    },
    "cooking-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Explaining a texture change", "Describing why an egg white foams when whipped"],
        ]),
    },
    "cooking-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Predicting browning", "Explaining why a seared steak develops a crust"],
        ]),
    },
    "cooking-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a critical control point", "Flagging the cooling step of a soup as a risk point"],
        ]),
    },
    "cooking-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Pricing a dish", "Calculating a target menu price from ingredient cost"],
        ]),
    },
    "cooking-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a technique's origin", "Linking a modern sauce back to classical French method"],
        ]),
    },
    "cooking-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Designing a molecular dish", "Planning a foam or gel component for a tasting menu"],
        ]),
    },
    "cooking-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Pairing flavors", "Matching a sweet element with a contrasting acidic one"],
        ]),
    },
    "cooking-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating sourcing choices", "Comparing the footprint of local versus imported produce"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Cooking lessons (completing 70/70).")


if __name__ == "__main__":
    main()
