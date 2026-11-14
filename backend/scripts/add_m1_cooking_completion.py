#!/usr/bin/env python3
"""Depth pass, M1 Cooking: fill in real, hand-checked data_table
content for the 99 M1 Cooking lessons not covered by the earlier
breadth-first batch. Brings M1 Cooking to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cooking-m1-l1": {
        "data_table": table(["Concept", "Purpose"], [
            ["Menu engineering", "Balances popularity and profitability to design an effective menu"],
        ]),
    },
    "cooking-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Culinary arts management", "Coordinates staffing, cost control, and quality across kitchen operations"],
        ]),
    },
    "cooking-m1-l4": {
        "data_table": table(["Factor", "Effect on Browning"], [
            ["Higher heat", "Accelerates the Maillard reaction and deepens flavor development"],
        ]),
    },
    "cooking-m1-l5": {
        "data_table": table(["Step", "Purpose"], [
            ["Critical control point", "A stage where a food safety hazard can be prevented or eliminated"],
        ]),
    },
    "cooking-m1-l6": {
        "data_table": table(["Metric", "Meaning"], [
            ["Food cost percentage", "Portion of menu price consumed by ingredient cost"],
        ]),
    },
    "cooking-m1-l7": {
        "data_table": table(["Region", "Culinary Feature"], [
            ["Mediterranean", "Olive oil, fresh produce, and grilled preparations dominate"],
        ]),
    },
    "cooking-m1-l8": {
        "data_table": table(["Technique", "Effect"], [
            ["Spherification", "Uses gelling agents to encase liquid in a thin, edible membrane"],
        ]),
    },
    "cooking-m1-l9": {
        "data_table": table(["Taste", "Pairing Principle"], [
            ["Umami", "Pairs well with salt and fat to deepen savory depth"],
        ]),
    },
    "cooking-m1-l10": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sustainable sourcing", "Prioritizes seasonal, local, and responsibly produced ingredients"],
        ]),
    },
    "cooking-m1-l11": {
        "data_table": table(["Area", "Focus"], [
            ["Restaurant operations", "Coordinates staffing, inventory, and service flow"],
        ]),
    },
    "cooking-m1-l12": {
        "data_table": table(["Agent", "Effect"], [
            ["Gluten", "Provides structure and chew through protein network development"],
            ["Baking soda", "A chemical leavener that produces carbon dioxide when activated"],
        ]),
    },
    "cooking-m1-l13": {
        "data_table": table(["Process", "Example"], [
            ["Lacto-fermentation", "Bacteria convert sugars to lactic acid, e.g. in sauerkraut"],
        ]),
    },
    "cooking-m1-l14": {
        "data_table": table(["Nutrient", "Culinary Application"], [
            ["Fiber", "Chefs balance texture and nutrition when designing plant-forward dishes"],
        ]),
    },
    "cooking-m1-l15": {
        "data_table": table(["Element", "Purpose"], [
            ["Natural light", "Produces soft, even food photography without harsh shadows"],
        ]),
    },
    "cooking-m1-l16": {
        "data_table": table(["Principle", "Detail"], [
            ["Wine pairing", "Matches acidity, weight, and flavor intensity between dish and beverage"],
        ]),
    },
    "cooking-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Culinary entrepreneurship", "Combines cooking skill with business planning and financial risk management"],
        ]),
    },
    "cooking-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Food anthropology", "Studies how cuisine reflects and shapes cultural identity"],
        ]),
    },
    "cooking-m1-l19": {
        "data_table": table(["Certification", "Focus"], [
            ["Culinary certification", "Validates standardized professional technique and safety knowledge"],
        ]),
    },
    "cooking-m1-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Food styling", "Arranges and prepares dishes to photograph well for media use"],
        ]),
    },
    "cooking-m1-l21": {
        "data_table": table(["Mother Sauce", "Derivative"], [
            ["Béchamel", "Mornay (with cheese)"],
            ["Espagnole", "Bordelaise (with red wine and shallots)"],
        ]),
    },
    "cooking-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Emulsion stability", "Requires an emulsifier to keep oil and water dispersed rather than separating"],
        ]),
    },
    "cooking-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Sous vide protein science", "Precise temperature control cooks protein evenly without overshooting doneness"],
        ]),
    },
    "cooking-m1-l24": {
        "data_table": table(["Agent", "Mechanism"], [
            ["Sodium alginate + calcium chloride", "Forms a gel membrane around liquid through ionic cross-linking"],
        ]),
    },
    "cooking-m1-l25": {
        "data_table": table(["Technique", "Detail"], [
            ["Culinary foam", "Incorporates air into a flavored liquid using a stabilizing agent"],
        ]),
    },
    "cooking-m1-l26": {
        "data_table": table(["Stage", "Temperature"], [
            ["Soft ball stage", "About 112-116°C, used for fudge and fondant"],
            ["Hard crack stage", "About 149-154°C, used for brittle"],
        ]),
    },
    "cooking-m1-l27": {
        "data_table": table(["Step", "Purpose"], [
            ["Tempering chocolate", "Stabilizes cocoa butter crystals for a glossy snap"],
        ]),
    },
    "cooking-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Gluten network development", "Kneading aligns protein strands to create bread's elastic structure"],
        ]),
    },
    "cooking-m1-l29": {
        "data_table": table(["Starter", "Detail"], [
            ["Sourdough starter", "A wild yeast and bacteria culture that leavens bread naturally"],
        ]),
    },
    "cooking-m1-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Lamination folds", "Creates alternating butter and dough layers for a flaky pastry"],
        ]),
    },
    "cooking-m1-l31": {
        "data_table": table(["Cut", "Use"], [
            ["Brunoise", "Fine 1-2mm dice used for delicate garnish"],
        ]),
    },
    "cooking-m1-l32": {
        "data_table": table(["Method", "Effect"], [
            ["Curing", "Salt draws out moisture, preserving and concentrating flavor"],
        ]),
    },
    "cooking-m1-l33": {
        "data_table": table(["Stage", "Result"], [
            ["Demi-glace", "Reduced brown stock and sauce espagnole for concentrated flavor"],
        ]),
    },
    "cooking-m1-l34": {
        "data_table": table(["Compound", "Source"], [
            ["Glutamate", "A key umami compound found in aged cheese, tomatoes, and fermented foods"],
        ]),
    },
    "cooking-m1-l35": {
        "data_table": table(["Method", "Detail"], [
            ["Cold smoking", "Applies smoke flavor at low temperature without cooking the food"],
            ["Hot smoking", "Applies smoke while simultaneously cooking the food through"],
        ]),
    },
    "cooking-m1-l36": {
        "data_table": table(["Agent", "Purpose"], [
            ["Cornstarch/egg yolk", "Stabilizes pastry cream by thickening and preventing curdling"],
        ]),
    },
    "cooking-m1-l37": {
        "data_table": table(["Pigment", "Detail"], [
            ["Chlorophyll", "Green pigment that degrades and dulls with prolonged heat exposure"],
        ]),
    },
    "cooking-m1-l38": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sustainable seafood sourcing", "Considers population health and catch method when selecting species"],
        ]),
    },
    "cooking-m1-l39": {
        "data_table": table(["Process", "Effect"], [
            ["Dry-aging", "Controlled moisture loss concentrates flavor and tenderizes via enzymatic breakdown"],
        ]),
    },
    "cooking-m1-l40": {
        "data_table": table(["Technique", "Detail"], [
            ["Risotto starch release", "Constant stirring releases surface starch to create a creamy texture"],
        ]),
    },
    "cooking-m1-l41": {
        "data_table": table(["Hydrocolloid", "Function"], [
            ["Xanthan gum", "Thickens liquids without requiring heat"],
            ["Agar-agar", "Forms a firm, heat-stable gel"],
        ]),
    },
    "cooking-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Koji fermentation", "Enzymes from koji mold break down starches and proteins into deep umami flavor"],
        ]),
    },
    "cooking-m1-l43": {
        "data_table": table(["Process", "Detail"], [
            ["Acetic fermentation", "Bacteria convert alcohol into acetic acid, producing vinegar"],
        ]),
    },
    "cooking-m1-l44": {
        "data_table": table(["Principle", "Detail"], [
            ["Textural contrast", "Pairs crunchy, creamy, and crisp elements for dynamic mouthfeel"],
        ]),
    },
    "cooking-m1-l45": {
        "data_table": table(["Principle", "Detail"], [
            ["Wine-food molecular pairing", "Complementary or contrasting flavor compounds shape a successful pairing"],
        ]),
    },
    "cooking-m1-l46": {
        "data_table": table(["Blend", "Region"], [
            ["Garam masala", "Warming spice blend common in South Asian cooking"],
        ]),
    },
    "cooking-m1-l47": {
        "data_table": table(["Technique", "Detail"], [
            ["Cryogenic freezing", "Liquid nitrogen freezes food nearly instantly, producing very small ice crystals"],
        ]),
    },
    "cooking-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Poultry yield optimization", "Careful fabrication minimizes trim waste and maximizes usable portions"],
        ]),
    },
    "cooking-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Fat clarification", "Removing impurities raises a fat's smoke point and extends shelf life"],
        ]),
    },
    "cooking-m1-l50": {
        "data_table": table(["Principle", "Detail"], [
            ["Visual balance", "Distributes color, height, and negative space for an appealing composed plate"],
        ]),
    },
    "cooking-m1-l51": {
        "data_table": table(["Enzyme", "Effect"], [
            ["Bromelain (pineapple)", "Breaks down protein structure to tenderize meat"],
        ]),
    },
    "cooking-m1-l52": {
        "data_table": table(["Step", "Purpose"], [
            ["Raft clarification", "Egg white mixture traps impurities, producing a clear consommé"],
        ]),
    },
    "cooking-m1-l53": {
        "data_table": table(["Station", "Role"], [
            ["Brigade system", "Assigns specialized kitchen roles like saucier and garde manger"],
        ]),
    },
    "cooking-m1-l54": {
        "data_table": table(["Blade", "Feature"], [
            ["Single-bevel Japanese knife", "Sharpened on one side for extremely precise, clean cuts"],
        ]),
    },
    "cooking-m1-l55": {
        "data_table": table(["Ingredient", "Role"], [
            ["Kombu/bonito flakes", "Base ingredients for dashi, providing layered umami extraction"],
        ]),
    },
    "cooking-m1-l56": {
        "data_table": table(["Process", "Detail"], [
            ["Cheese ripening", "Enzymes and microbes gradually transform texture and develop complex flavor"],
        ]),
    },
    "cooking-m1-l57": {
        "data_table": table(["Factor", "Detail"], [
            ["Optimizing the Maillard reaction", "Surface dryness and high dry heat accelerate browning and flavor development"],
        ]),
    },
    "cooking-m1-l58": {
        "data_table": table(["Method", "Detail"], [
            ["Quick pickling", "Acid-based brine preserves and flavors vegetables without full fermentation"],
        ]),
    },
    "cooking-m1-l59": {
        "data_table": table(["Technique", "Detail"], [
            ["Plant protein texturization", "Extrusion under heat and pressure creates a fibrous, meat-like structure"],
        ]),
    },
    "cooking-m1-l60": {
        "data_table": table(["Metric", "Meaning"], [
            ["Overrun", "The percentage of air incorporated into ice cream during churning"],
        ]),
    },
    "cooking-m1-l61": {
        "data_table": table(["Technique", "Purpose"], [
            ["Vacuum infusion", "Pressure differential forces flavor liquid directly into food's cellular structure"],
        ]),
    },
    "cooking-m1-l62": {
        "data_table": table(["Factor", "Effect"], [
            ["Oven steam injection", "Delays crust formation, allowing greater bread oven spring"],
        ]),
    },
    "cooking-m1-l63": {
        "data_table": table(["Principle", "Detail"], [
            ["Southeast Asian flavor balance", "Combines sweet, sour, salty, and spicy elements within a single dish"],
        ]),
    },
    "cooking-m1-l64": {
        "data_table": table(["Process", "Detail"], [
            ["Collagen conversion", "Slow, moist heat breaks tough collagen down into tender gelatin"],
        ]),
    },
    "cooking-m1-l65": {
        "data_table": table(["Technique", "Effect"], [
            ["Liquid nitrogen texture manipulation", "Rapid freezing creates distinctive brittle or shattering textures"],
        ]),
    },
    "cooking-m1-l66": {
        "data_table": table(["Protein", "Coagulation Temperature"], [
            ["Egg white", "Begins setting around 63°C (145°F)"],
            ["Egg yolk", "Begins setting around 65°C (149°F)"],
        ]),
    },
    "cooking-m1-l67": {
        "data_table": table(["Technique", "Detail"], [
            ["Middle Eastern preservation", "Combines salt curing and drying with distinctive regional spice blends"],
        ]),
    },
    "cooking-m1-l68": {
        "data_table": table(["Compound", "Effect"], [
            ["Furan/pyrazine compounds", "Formed during caramelization, contributing complex roasted flavor notes"],
        ]),
    },
    "cooking-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Pressure cooking kinetics", "Elevated pressure raises boiling point, accelerating cooking reactions"],
        ]),
    },
    "cooking-m1-l70": {
        "data_table": table(["Technique", "Detail"], [
            ["Terrine construction", "Layers ingredients within a mold, often set with gelatin or fat"],
        ]),
    },
    "cooking-m1-l71": {
        "data_table": table(["Process", "Detail"], [
            ["Nixtamalization", "Alkaline treatment of corn improves nutrition and enables masa dough formation"],
        ]),
    },
    "cooking-m1-l72": {
        "data_table": table(["Food", "Fermentation Feature"], [
            ["Kimchi", "Lacto-fermented with a distinctive spiced, layered flavor profile"],
            ["Sauerkraut", "Lacto-fermented cabbage with a simpler tangy profile"],
        ]),
    },
    "cooking-m1-l73": {
        "data_table": table(["Technique", "Detail"], [
            ["Reverse searing", "Cooks low and slow first, then finishes with a high-heat sear for crust"],
        ]),
    },
    "cooking-m1-l74": {
        "data_table": table(["Factor", "Effect"], [
            ["Dough hydration level", "Higher hydration produces a more extensible, open-crumb pasta or bread structure"],
        ]),
    },
    "cooking-m1-l75": {
        "data_table": table(["Technique", "Detail"], [
            ["Tempering (tadka)", "Frying whole spices in hot oil releases aromatic compounds before adding to a dish"],
        ]),
    },
    "cooking-m1-l76": {
        "data_table": table(["Technique", "Detail"], [
            ["Confit", "Slowly cooks and preserves food submerged in fat at low temperature"],
        ]),
    },
    "cooking-m1-l77": {
        "data_table": table(["Technique", "Detail"], [
            ["Ultrasonic homogenization", "High-frequency sound waves create extremely fine, stable emulsions"],
        ]),
    },
    "cooking-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Tasting menu sequencing", "Courses are ordered to build flavor intensity and textural variety progressively"],
        ]),
    },
    "cooking-m1-l79": {
        "data_table": table(["Technique", "Detail"], [
            ["West African fermentation", "Uses traditional fermented staples to develop deep regional flavor profiles"],
        ]),
    },
    "cooking-m1-l80": {
        "data_table": table(["Method", "Purpose"], [
            ["Sensory panel design", "Structured tasting protocols reduce bias in evaluating flavor and texture"],
        ]),
    },
    "cooking-m1-l81": {
        "data_table": table(["Method", "Purpose"], [
            ["Acidulation", "Citric or ascorbic acid slows enzymatic browning on cut produce"],
        ]),
    },
    "cooking-m1-l82": {
        "data_table": table(["Principle", "Detail"], [
            ["Nose-to-tail butchery", "Maximizes utilization of the entire animal to reduce waste"],
        ]),
    },
    "cooking-m1-l83": {
        "data_table": table(["Grade", "Detail"], [
            ["Extra virgin olive oil", "Highest quality grade based on low acidity and sensory evaluation"],
        ]),
    },
    "cooking-m1-l84": {
        "data_table": table(["Product", "Feature"], [
            ["Viennoiserie", "Enriched laminated pastries like croissants requiring precise butter-dough layering"],
        ]),
    },
    "cooking-m1-l85": {
        "data_table": table(["Process", "Effect"], [
            ["Dehydration", "Removes water to concentrate flavor and extend shelf life"],
        ]),
    },
    "cooking-m1-l86": {
        "data_table": table(["Metric", "Formula"], [
            ["Yield percentage", "Usable product weight divided by as-purchased weight"],
        ]),
        "formulae": ["yield_pct = usable_weight / purchased_weight * 100"],
    },
    "cooking-m1-l87": {
        "data_table": table(["Technique", "Detail"], [
            ["New Nordic cuisine", "Emphasizes hyper-local, foraged, and preserved regional ingredients"],
        ]),
    },
    "cooking-m1-l88": {
        "data_table": table(["Agent", "Purpose"], [
            ["Lecithin", "Stabilizes culinary foam by reducing surface tension at the air-liquid interface"],
        ]),
    },
    "cooking-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Retronasal aroma", "Aroma perceived through the back of the throat significantly shapes perceived flavor"],
        ]),
    },
    "cooking-m1-l90": {
        "data_table": table(["Method", "Purpose"], [
            ["Reverse engineering a dish", "Deconstructs technique and ratio to recreate a professional restaurant recipe"],
        ]),
    },
    "cooking-m1-l91": {
        "data_table": table(["Process", "Detail"], [
            ["Ceviche acid denaturation", "Citric acid denatures fish protein, achieving a cooked texture without heat"],
        ]),
    },
    "cooking-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Gelatin bloom strength", "Measures gel firmness, guiding how much gelatin a recipe requires"],
        ]),
    },
    "cooking-m1-l93": {
        "data_table": table(["Practice", "Purpose"], [
            ["Zero-waste cooking", "Uses trim, scraps, and byproducts as ingredients rather than discarding them"],
        ]),
    },
    "cooking-m1-l94": {
        "data_table": table(["Technique", "Purpose"], [
            ["Vacuum marination", "Reduced pressure accelerates marinade penetration into food"],
        ]),
    },
    "cooking-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Wok hei", "The distinctive smoky char flavor produced by extremely high-heat stir-frying"],
        ]),
    },
    "cooking-m1-l96": {
        "data_table": table(["Metric", "Purpose"], [
            ["Menu item profitability analysis", "Ranks dishes by margin and popularity to guide menu decisions"],
        ]),
    },
    "cooking-m1-l97": {
        "data_table": table(["Process", "Detail"], [
            ["Osmotic dehydration", "A sugar or salt solution draws moisture out of fruit without heat"],
        ]),
    },
    "cooking-m1-l98": {
        "data_table": table(["Process", "Detail"], [
            ["Whey protein clarification", "Heat and pH adjustment separate and purify whey proteins from liquid"],
        ]),
    },
    "cooking-m1-l99": {
        "data_table": table(["Process", "Detail"], [
            ["Injera fermentation", "Teff flour batter ferments over days to develop its characteristic sour flavor"],
        ]),
    },
    "cooking-m1-l100": {
        "data_table": table(["Agent", "Feature"], [
            ["Agar-agar", "A plant-based gelling agent that sets firm at room temperature, unlike gelatin"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Reaction", "Effect"], [
        ["Maillard reaction", "Browning and flavor development when proteins/sugars are heated"],
        ["Caramelization", "Browning of sugars when heated"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"cooking-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"cooking-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"cooking-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Cooking lessons (completing 120/120).")


if __name__ == "__main__":
    main()
