#!/usr/bin/env python3
"""Depth pass, C1 Art History: fill in real, hand-checked data_table
content for the 69 C1 Art History lessons not covered by the earlier
breadth-first batch. Brings C1 Art History to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_art_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-history-c1-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Formal analysis", "Examines composition, color, and technique in a work of art"],
        ]),
    },
    "art-history-c1-l2": {
        "data_table": table(["Period", "Feature"], [
            ["Prehistoric art", "Predates written records, e.g. cave paintings"], ["Ancient art", "Produced by early literate civilizations"],
        ]),
    },
    "art-history-c1-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Venus figurines", "Small carved female forms from the Paleolithic era"],
        ]),
    },
    "art-history-c1-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Stonehenge", "Neolithic megalithic monument in England, c. 3000-2000 BCE"],
        ]),
    },
    "art-history-c1-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Ziggurat", "A massive stepped temple structure in ancient Mesopotamia"],
        ]),
    },
    "art-history-c1-l7": {
        "data_table": table(["Convention", "Detail"], [
            ["Egyptian canon", "Figures shown in profile with frontal shoulders and eye"],
        ]),
    },
    "art-history-c1-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Great Pyramid of Giza", "Built c. 2560 BCE as a royal tomb"],
        ]),
    },
    "art-history-c1-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Book of the Dead", "A collection of spells to guide the deceased through the afterlife"],
        ]),
    },
    "art-history-c1-l10": {
        "data_table": table(["Civilization", "Region"], [
            ["Minoan", "Crete"], ["Mycenaean", "Mainland Greece"],
        ]),
    },
    "art-history-c1-l11": {
        "data_table": table(["Technique", "Feature"], [
            ["Black-figure", "Figures painted black on red clay background"], ["Red-figure", "Figures left in red clay, background painted black"],
        ]),
    },
    "art-history-c1-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["The Parthenon", "Temple to Athena built on the Athenian Acropolis, 447-432 BCE"],
        ]),
    },
    "art-history-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Kouros", "An archaic Greek standing male figure sculpture"], ["Contrapposto", "A pose with weight shifted onto one leg"],
        ]),
    },
    "art-history-c1-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Laocoon", "A dramatic Hellenistic sculpture showing intense emotion and movement"],
        ]),
    },
    "art-history-c1-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Etruscan art", "Predated and influenced early Roman art and architecture"],
        ]),
    },
    "art-history-c1-l16": {
        "data_table": table(["Feature", "Detail"], [
            ["Roman portraiture", "Known for realistic, individualized facial features"],
        ]),
    },
    "art-history-c1-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Colosseum", "Roman amphitheater completed c. 80 CE"], ["Pantheon", "Roman temple famous for its concrete dome"],
        ]),
    },
    "art-history-c1-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Pompeii", "Roman city preserved by the eruption of Mount Vesuvius in 79 CE"],
        ]),
    },
    "art-history-c1-l19": {
        "data_table": table(["Element to Examine", "Question"], [
            ["Composition", "How are elements arranged?"], ["Color", "What palette and contrasts are used?"],
        ]),
    },
    "art-history-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Iconography", "The study of symbols and their meanings in visual art"],
        ]),
    },
    "art-history-c1-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Cuneiform", "One of the earliest writing systems, developed in Sumer"],
        ]),
    },
    "art-history-c1-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Assyrian reliefs", "Carved palace walls depicting royal power and military victory"],
        ]),
    },
    "art-history-c1-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Achaemenid Empire", "Persian empire, c. 550-330 BCE, known for Persepolis"],
        ]),
    },
    "art-history-c1-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Bronze Age China", "Known for elaborate ritual bronze vessels"],
        ]),
    },
    "art-history-c1-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Terracotta Army", "Thousands of life-sized clay soldiers guarding Qin Shi Huang's tomb"],
        ]),
    },
    "art-history-c1-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Indus Valley civilization", "Known for standardized seals and urban planning"],
        ]),
    },
    "art-history-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Aniconic tradition", "Early Buddhist art represented the Buddha through symbols rather than his image"],
        ]),
    },
    "art-history-c1-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Gandharan art", "Blended Greek and Buddhist artistic styles"],
        ]),
    },
    "art-history-c1-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Olmec colossal heads", "Massive carved stone heads from Mesoamerica's earliest major civilization"],
        ]),
    },
    "art-history-c1-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Maya stelae", "Carved stone monuments recording history in hieroglyphic script"],
        ]),
    },
    "art-history-c1-l31": {
        "data_table": table(["Culture", "Region"], [
            ["Chavin", "Early Andean culture, known for stone carving"], ["Nazca", "Known for large-scale geoglyphs (the Nazca Lines)"],
        ]),
    },
    "art-history-c1-l32": {
        "data_table": table(["Culture", "Known For"], [
            ["Nok", "Early terracotta sculpture in West Africa"], ["Ife", "Naturalistic bronze and terracotta heads"],
        ]),
    },
    "art-history-c1-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Polynesian art", "Includes tattooing, wood carving, and monumental sculpture like Moai"],
        ]),
    },
    "art-history-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Formline design", "A stylized ovoid-and-curve visual system used in Pacific Northwest Coast art"],
        ]),
    },
    "art-history-c1-l35": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Islamic calligraphy", "Ornate stylized script, often used to write the Quran"], ["Geometric pattern", "Repeating shapes based on mathematical principles"],
        ]),
    },
    "art-history-c1-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Great Mosque of Cordoba", "Built starting 785 CE in Islamic Spain"],
        ]),
    },
    "art-history-c1-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Persian miniature painting", "Detailed illustrated manuscripts, flourished under Persian courts"],
        ]),
    },
    "art-history-c1-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Mughal Empire art", "Blended Persian, Indian, and Islamic artistic traditions"],
        ]),
    },
    "art-history-c1-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Hindu temple architecture", "Often features a tower (shikhara) symbolizing a cosmic mountain"],
        ]),
    },
    "art-history-c1-l40": {
        "data_table": table(["Site", "Location"], [
            ["Ajanta caves", "India"], ["Dunhuang caves", "China"],
        ]),
    },
    "art-history-c1-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Zen ink painting", "Emphasizes simplicity and spontaneous brushwork"],
        ]),
    },
    "art-history-c1-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Ukiyo-e", "Japanese woodblock print tradition, flourished 17th-19th century"],
        ]),
    },
    "art-history-c1-l43": {
        "data_table": table(["Ware", "Dynasty"], [
            ["Celadon", "Goryeo dynasty"], ["Porcelain", "Joseon dynasty"],
        ]),
    },
    "art-history-c1-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["Aztec art", "Featured monumental stone sculpture and featherwork"],
        ]),
    },
    "art-history-c1-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Inca art", "Known for precise stone masonry and metalwork"],
        ]),
    },
    "art-history-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Syncretism", "The blending of Indigenous and European artistic traditions in colonial Latin America"],
        ]),
    },
    "art-history-c1-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["African art's influence", "Shaped early 20th-century modernists like Picasso"],
        ]),
    },
    "art-history-c1-l48": {
        "data_table": table(["Label Element", "Info Provided"], [
            ["Title and date", "Identifies the artwork"], ["Medium", "The materials used"],
        ]),
    },
    "art-history-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Art conservation", "Preserving and restoring artworks for future generations"],
        ]),
    },
    "art-history-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Provenance", "The documented history of an artwork's ownership"],
        ]),
    },
    "art-history-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Patronage", "Financial support for artists, historically by churches, courts, or wealthy individuals"],
        ]),
    },
    "art-history-c1-l52": {
        "data_table": table(["Tradition", "Example Sacred Art"], [
            ["Christianity", "Icons and stained glass"], ["Buddhism", "Statues and mandalas"],
        ]),
    },
    "art-history-c1-l53": {
        "data_table": table(["Approach", "Focus"], [
            ["Gender studies in art history", "Examines how gender shapes artistic representation and reception"],
        ]),
    },
    "art-history-c1-l54": {
        "data_table": table(["Material", "Era"], [
            ["Tempera", "Common before oil paint"], ["Fresco", "Pigment applied to wet plaster"],
        ]),
    },
    "art-history-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Connoisseurship", "Expert judgment of an artwork's quality, authenticity, and attribution"],
        ]),
    },
    "art-history-c1-l56": {
        "data_table": table(["Fact", "Detail"], [
            ["Museums", "Evolved from private cabinets of curiosities into public institutions"],
        ]),
    },
    "art-history-c1-l57": {
        "data_table": table(["Method", "Purpose"], [
            ["Pigment analysis", "Detects materials inconsistent with a claimed date"],
        ]),
    },
    "art-history-c1-l58": {
        "data_table": table(["Tool", "Use"], [
            ["Digital imaging", "Reveals underdrawings and restoration history"],
        ]),
    },
    "art-history-c1-l59": {
        "data_table": table(["Fact", "Detail"], [
            ["UNESCO World Heritage Sites", "Recognized for outstanding cultural or natural value"],
        ]),
    },
    "art-history-c1-l60": {
        "data_table": table(["Part", "Purpose"], [
            ["Thesis", "States the essay's central argument"], ["Visual evidence", "Supports claims with specific formal details"],
        ]),
    },
    "art-history-c1-l61": {
        "data_table": table(["Fact", "Detail"], [
            ["Parthenon architecture", "Uses subtle curvature (entasis) to correct optical illusions"],
        ]),
    },
    "art-history-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing two periods", "Contrasting Prehistoric and Ancient Egyptian artistic conventions"],
        ]),
    },
    "art-history-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Dating an artifact", "Using stylistic clues to place an unlabeled object in a period"],
        ]),
    },
    "art-history-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing cave art technique", "Identifying pigment sources used at Lascaux"],
        ]),
    },
    "art-history-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting Venus figurines", "Discussing competing theories of their function"],
        ]),
    },
    "art-history-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing megalith construction", "Estimating the labor required to move Stonehenge's stones"],
        ]),
    },
    "art-history-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Reading cylinder seal impressions", "Identifying figures and scenes rolled onto clay"],
        ]),
    },
    "art-history-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Applying Egyptian conventions", "Identifying canon proportions in a tomb painting"],
        ]),
    },
    "art-history-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Comparing pyramid construction theories", "Weighing ramp versus lever construction hypotheses"],
        ]),
    },
    "art-history-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting funerary texts", "Analyzing a Book of the Dead spell's purpose"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Art History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Art History lessons (completing 70/70).")


if __name__ == "__main__":
    main()
