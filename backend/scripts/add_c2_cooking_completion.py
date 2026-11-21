#!/usr/bin/env python3
"""Depth pass, C2 Cooking: fill in real, hand-checked data_table content
for the 69 C2 Cooking lessons not covered by the earlier breadth-first
batch. Brings C2 Cooking to full 70/70 coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cooking-c2-l1": {
        "data_table": table(["Cuisine", "Signature Technique"], [
            ["French cuisine", "Mother sauces as a foundation for countless derivative dishes"],
        ]),
    },
    "cooking-c2-l2": {
        "data_table": table(["Concept", "Purpose"], [
            ["Menu engineering", "Balances popularity and profitability to design an effective menu"],
        ]),
    },
    "cooking-c2-l4": {
        "data_table": table(["Factor", "Effect on Browning"], [
            ["Higher heat", "Accelerates the Maillard reaction and deepens flavor development"],
        ]),
    },
    "cooking-c2-l5": {
        "data_table": table(["Step", "Purpose"], [
            ["Critical control point", "A stage where a food safety hazard can be prevented or eliminated"],
        ]),
    },
    "cooking-c2-l6": {
        "data_table": table(["Metric", "Meaning"], [
            ["Food cost percentage", "Portion of menu price consumed by ingredient cost"],
        ]),
    },
    "cooking-c2-l7": {
        "data_table": table(["Region", "Culinary Feature"], [
            ["Mediterranean", "Olive oil, fresh produce, and grilled preparations dominate"],
        ]),
    },
    "cooking-c2-l8": {
        "data_table": table(["Technique", "Effect"], [
            ["Spherification", "Uses gelling agents to encase liquid in a thin, edible membrane"],
        ]),
    },
    "cooking-c2-l9": {
        "data_table": table(["Taste", "Pairing Principle"], [
            ["Umami", "Pairs well with salt and fat to deepen savory depth"],
        ]),
    },
    "cooking-c2-l10": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sustainable sourcing", "Prioritizes seasonal, local, and responsibly produced ingredients"],
        ]),
    },
    "cooking-c2-l11": {
        "data_table": table(["Area", "Focus"], [
            ["Restaurant operations", "Coordinates staffing, inventory, and service flow"],
        ]),
    },
    "cooking-c2-l12": {
        "data_table": table(["Agent", "Effect"], [
            ["Gluten", "Provides structure and chew through protein network development"],
            ["Baking soda", "A chemical leavener that produces carbon dioxide when activated"],
        ]),
    },
    "cooking-c2-l13": {
        "data_table": table(["Process", "Example"], [
            ["Lacto-fermentation", "Bacteria convert sugars to lactic acid, e.g. in sauerkraut"],
        ]),
    },
    "cooking-c2-l14": {
        "data_table": table(["Nutrient", "Culinary Application"], [
            ["Fiber", "Chefs balance texture and nutrition when designing plant-forward dishes"],
        ]),
    },
    "cooking-c2-l15": {
        "data_table": table(["Element", "Purpose"], [
            ["Natural light", "Produces soft, even food photography without harsh shadows"],
        ]),
    },
    "cooking-c2-l16": {
        "data_table": table(["Principle", "Detail"], [
            ["Wine pairing", "Matches acidity, weight, and flavor intensity between dish and beverage"],
        ]),
    },
    "cooking-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Culinary entrepreneurship", "Combines cooking skill with business planning and financial risk management"],
        ]),
    },
    "cooking-c2-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Food anthropology", "Studies how cuisine reflects and shapes cultural identity"],
        ]),
    },
    "cooking-c2-l19": {
        "data_table": table(["Certification", "Focus"], [
            ["Culinary certification", "Validates standardized professional technique and safety knowledge"],
        ]),
    },
    "cooking-c2-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Food styling", "Arranges and prepares dishes to photograph well for media use"],
        ]),
    },
    "cooking-c2-l21": {
        "data_table": table(["Cut", "Use"], [
            ["Brunoise", "Fine 1-2mm dice used for delicate garnish"],
            ["Julienne", "Thin matchstick cut for even cooking and presentation"],
        ]),
    },
    "cooking-c2-l22": {
        "data_table": table(["Stage", "Result"], [
            ["Demi-glace", "Reduced brown stock and sauce espagnole for concentrated flavor"],
        ]),
    },
    "cooking-c2-l23": {
        "data_table": table(["Mother Sauce", "Derivative"], [
            ["Béchamel", "Mornay (with cheese)"],
            ["Espagnole", "Bordelaise (with red wine and shallots)"],
        ]),
    },
    "cooking-c2-l24": {
        "data_table": table(["Step", "Purpose"], [
            ["Searing before braising", "Builds a browned flavor base before slow, moist-heat cooking"],
        ]),
    },
    "cooking-c2-l25": {
        "data_table": table(["Cut", "Roasting Consideration"], [
            ["Large roast", "Requires lower, longer heat for even internal doneness"],
        ]),
    },
    "cooking-c2-l26": {
        "data_table": table(["Starter", "Detail"], [
            ["Sourdough starter", "A wild yeast and bacteria culture that leavens bread naturally"],
        ]),
    },
    "cooking-c2-l27": {
        "data_table": table(["Dough", "Feature"], [
            ["Choux pastry", "Cooked dough that puffs from steam, used for éclairs and profiteroles"],
            ["Puff pastry", "Laminated dough that rises in flaky layers from steam between butter sheets"],
        ]),
    },
    "cooking-c2-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Torting and filling", "Splits and layers cake to distribute filling evenly"],
        ]),
    },
    "cooking-c2-l29": {
        "data_table": table(["Dish", "Key Technique"], [
            ["Soufflé", "Folded whipped egg whites provide rise through trapped air"],
        ]),
    },
    "cooking-c2-l30": {
        "data_table": table(["Technique", "Benefit"], [
            ["Sous vide", "Precise temperature-controlled water bath yields consistent doneness"],
        ]),
    },
    "cooking-c2-l31": {
        "data_table": table(["Shape", "Region"], [
            ["Ravioli", "Filled pasta associated with northern Italy"],
            ["Tortellini", "Ring-shaped filled pasta from Emilia-Romagna"],
        ]),
    },
    "cooking-c2-l32": {
        "data_table": table(["Step", "Purpose"], [
            ["Raft clarification", "Egg white mixture traps impurities, producing a clear consommé"],
        ]),
    },
    "cooking-c2-l33": {
        "data_table": table(["Salad Type", "Feature"], [
            ["Composed salad", "Ingredients arranged deliberately rather than tossed together"],
        ]),
    },
    "cooking-c2-l34": {
        "data_table": table(["Sauce", "Base"], [
            ["Hollandaise", "Emulsified butter and egg yolk, stabilized with gentle heat"],
        ]),
    },
    "cooking-c2-l35": {
        "data_table": table(["Method", "Effect"], [
            ["Curing", "Salt draws out moisture, preserving and concentrating flavor"],
        ]),
    },
    "cooking-c2-l36": {
        "data_table": table(["Blend", "Region"], [
            ["Garam masala", "Warming spice blend common in South Asian cooking"],
        ]),
    },
    "cooking-c2-l37": {
        "data_table": table(["Method", "Purpose"], [
            ["Oil infusion", "Extracts aromatic compounds from herbs into a neutral fat"],
        ]),
    },
    "cooking-c2-l38": {
        "data_table": table(["Principle", "Purpose"], [
            ["Negative space", "Empty plate area draws focus to the composed food elements"],
        ]),
    },
    "cooking-c2-l39": {
        "data_table": table(["Metric", "Purpose"], [
            ["Standard portion size", "Controls cost consistency and customer expectation"],
        ]),
    },
    "cooking-c2-l40": {
        "data_table": table(["Equipment", "Function"], [
            ["Combi oven", "Combines steam and convection heat for versatile cooking control"],
        ]),
    },
    "cooking-c2-l41": {
        "data_table": table(["Primal Cut", "Common Use"], [
            ["Chuck", "Braising and slow-cooked preparations"],
        ]),
    },
    "cooking-c2-l42": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sustainable seafood sourcing", "Considers population health and catch method when selecting species"],
        ]),
    },
    "cooking-c2-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Curdling milk with acid or rennet", "Separates curds from whey as the basis of cheese making"],
        ]),
    },
    "cooking-c2-l44": {
        "data_table": table(["Failure", "Likely Cause"], [
            ["Dense bread", "Underproofed dough or insufficient gluten development"],
        ]),
    },
    "cooking-c2-l45": {
        "data_table": table(["Step", "Purpose"], [
            ["Lamination folds", "Creates alternating butter and dough layers for a flaky croissant"],
        ]),
    },
    "cooking-c2-l46": {
        "data_table": table(["Batter", "Feature"], [
            ["Tempura batter", "Kept cold and minimally mixed to preserve a light, crisp texture"],
        ]),
    },
    "cooking-c2-l47": {
        "data_table": table(["Thickener", "Mechanism"], [
            ["Xanthan gum", "Modern thickener that adds viscosity without cooking"],
        ]),
    },
    "cooking-c2-l48": {
        "data_table": table(["Element", "Purpose"], [
            ["Professional food photography", "Controls lighting and composition for commercial-quality images"],
        ]),
    },
    "cooking-c2-l49": {
        "data_table": table(["Station", "Role"], [
            ["Brigade system", "Assigns specialized kitchen roles like saucier and garde manger"],
        ]),
    },
    "cooking-c2-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Farm-to-table menu", "Built around seasonal ingredients sourced directly from local producers"],
        ]),
    },
    "cooking-c2-l51": {
        "data_table": table(["Region", "Feature"], [
            ["Mediterranean variations", "Greek, Italian, and Levantine traditions share olive oil and fresh produce emphasis"],
        ]),
    },
    "cooking-c2-l52": {
        "data_table": table(["Technique", "Detail"], [
            ["Stir-frying", "High heat and constant motion cook ingredients quickly while retaining texture"],
        ]),
    },
    "cooking-c2-l53": {
        "data_table": table(["Element", "Purpose"], [
            ["Plated dessert composition", "Balances temperature, texture, and visual contrast on the plate"],
        ]),
    },
    "cooking-c2-l54": {
        "data_table": table(["Step", "Purpose"], [
            ["Tempering chocolate", "Stabilizes cocoa butter crystals for a glossy snap"],
        ]),
    },
    "cooking-c2-l55": {
        "data_table": table(["Stage", "Temperature"], [
            ["Soft ball stage", "About 112-116°C, used for fudge and fondant"],
            ["Hard crack stage", "About 149-154°C, used for brittle and spun sugar"],
        ]),
    },
    "cooking-c2-l56": {
        "data_table": table(["Course", "Purpose"], [
            ["Tasting menu course", "A small, focused dish contributing to a larger progression of flavors"],
        ]),
    },
    "cooking-c2-l57": {
        "data_table": table(["Principle", "Detail"], [
            ["Wine pairing principle", "Complementary or contrasting flavors both offer valid pairing strategies"],
        ]),
    },
    "cooking-c2-l58": {
        "data_table": table(["Component", "Purpose"], [
            ["HACCP plan", "Documents hazards, control points, and monitoring procedures"],
        ]),
    },
    "cooking-c2-l59": {
        "data_table": table(["Element", "Detail"], [
            ["Competition preparation", "Requires precise timing, mise en place, and presentation practice"],
        ]),
    },
    "cooking-c2-l60": {
        "data_table": table(["Component", "Purpose"], [
            ["Restaurant concept", "Aligns cuisine, service style, and target audience into a coherent identity"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Reaction", "Effect"], [
    ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
    ["Caramelization", "Browning of sugars when heated"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"cooking-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"cooking-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"cooking-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Cooking lessons (completing 70/70).")


if __name__ == "__main__":
    main()
