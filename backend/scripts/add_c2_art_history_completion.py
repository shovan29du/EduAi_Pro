#!/usr/bin/env python3
"""Depth pass, C2 Art History: fill in real, hand-checked data_table
content for the 69 C2 Art History lessons not covered by the earlier
breadth-first batch. Brings C2 Art History to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_art_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-history-c2-l1": {
        "data_table": table(["Period", "Feature"], [
            ["Medieval art", "Emphasized religious symbolism over naturalistic representation"],
        ]),
    },
    "art-history-c2-l2": {
        "data_table": table(["Period", "Feature"], [
            ["Renaissance art", "Revived classical ideals with linear perspective and naturalism"],
        ]),
    },
    "art-history-c2-l4": {
        "data_table": table(["Site", "Feature"], [
            ["Hagia Sophia", "Famous for its massive dome and gold-ground mosaics"],
        ]),
    },
    "art-history-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Iconoclasm", "A movement opposing the veneration of religious images"],
        ]),
    },
    "art-history-c2-l6": {
        "data_table": table(["Period", "Feature"], [
            ["Carolingian art", "Revived classical Roman artistic forms under Charlemagne"],
        ]),
    },
    "art-history-c2-l7": {
        "data_table": table(["Feature", "Detail"], [
            ["Romanesque architecture", "Thick walls, rounded arches, and small windows"],
        ]),
    },
    "art-history-c2-l8": {
        "data_table": table(["Feature", "Detail"], [
            ["Gothic cathedral", "Pointed arches, ribbed vaults, and flying buttresses enabling tall walls of stained glass"],
        ]),
    },
    "art-history-c2-l9": {
        "data_table": table(["Shift", "Detail"], [
            ["Gothic sculpture", "Figures became more naturalistic and emotionally expressive"],
        ]),
    },
    "art-history-c2-l10": {
        "data_table": table(["Feature", "Detail"], [
            ["Illuminated manuscript", "Hand-decorated religious text combining text and intricate imagery"],
        ]),
    },
    "art-history-c2-l11": {
        "data_table": table(["Artist", "Contribution"], [
            ["Giotto", "Introduced greater naturalism and emotional depth into religious painting"],
        ]),
    },
    "art-history-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear perspective", "A mathematical system creating the illusion of depth on a flat surface"],
        ]),
    },
    "art-history-c2-l13": {
        "data_table": table(["Artist", "Contribution"], [
            ["Masaccio", "Applied linear perspective and naturalistic light to fresco painting"],
        ]),
    },
    "art-history-c2-l14": {
        "data_table": table(["Artist", "Feature"], [
            ["Botticelli", "Blended mythological subjects with Neoplatonic philosophy"],
        ]),
    },
    "art-history-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Sfumato", "A soft blending technique creating smoky transitions between colors and tones"],
        ]),
    },
    "art-history-c2-l16": {
        "data_table": table(["Work", "Feature"], [
            ["Sistine Chapel ceiling", "A monumental fresco depicting scenes from Genesis"],
        ]),
    },
    "art-history-c2-l17": {
        "data_table": table(["Work", "Feature"], [
            ["School of Athens", "Depicts classical philosophers in an idealized architectural space"],
        ]),
    },
    "art-history-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Colorito", "The Venetian emphasis on color and painterly technique over precise drawing"],
        ]),
    },
    "art-history-c2-l19": {
        "data_table": table(["Innovation", "Detail"], [
            ["Oil painting technique", "Allowed richer color layering and finer detail than tempera"],
        ]),
    },
    "art-history-c2-l20": {
        "data_table": table(["Contribution", "Detail"], [
            ["Dürer's printmaking", "Elevated woodcuts and engravings to fine art status"],
        ]),
    },
    "art-history-c2-l21": {
        "data_table": table(["Feature", "Detail"], [
            ["Mannerism", "Elongated figures and artificial compositions breaking from High Renaissance balance"],
        ]),
    },
    "art-history-c2-l22": {
        "data_table": table(["Technique", "Detail"], [
            ["Tenebrism", "Caravaggio's dramatic use of extreme light-dark contrast"],
        ]),
    },
    "art-history-c2-l23": {
        "data_table": table(["Feature", "Detail"], [
            ["Bernini's sculpture", "Captured dynamic movement and emotional intensity in marble"],
        ]),
    },
    "art-history-c2-l24": {
        "data_table": table(["Genre", "Focus"], [
            ["Dutch genre painting", "Depicted everyday domestic life and middle-class subjects"],
        ]),
    },
    "art-history-c2-l25": {
        "data_table": table(["Feature", "Detail"], [
            ["Vermeer's light", "Rendered soft, luminous light entering quiet domestic interiors"],
        ]),
    },
    "art-history-c2-l26": {
        "data_table": table(["Technique", "Detail"], [
            ["Chiaroscuro", "Rembrandt's use of strong light-dark contrast for psychological depth"],
        ]),
    },
    "art-history-c2-l27": {
        "data_table": table(["Feature", "Detail"], [
            ["Rococo art", "Ornate, playful, and pastel-toned, reflecting aristocratic leisure"],
        ]),
    },
    "art-history-c2-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Neoclassicism", "Revived classical restraint and moral seriousness in reaction to Rococo excess"],
        ]),
    },
    "art-history-c2-l29": {
        "data_table": table(["Feature", "Detail"], [
            ["Romanticism", "Emphasized intense emotion, nature, and the sublime"],
        ]),
    },
    "art-history-c2-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Realism", "Courbet depicted ordinary subjects without idealization"],
        ]),
    },
    "art-history-c2-l31": {
        "data_table": table(["Feature", "Detail"], [
            ["Impressionism", "Captured fleeting light and modern life with visible brushstrokes"],
        ]),
    },
    "art-history-c2-l32": {
        "data_table": table(["Artist", "Technique"], [
            ["Cézanne", "Structured form through geometric planes of color"], ["Seurat", "Pioneered pointillism using dots of pure color"],
        ]),
    },
    "art-history-c2-l33": {
        "data_table": table(["Feature", "Detail"], [
            ["Symbolism", "Turned toward dreams, myth, and the inner psychological world"],
        ]),
    },
    "art-history-c2-l34": {
        "data_table": table(["Feature", "Detail"], [
            ["Fauvism", "Used bold, non-naturalistic color for emotional expression"],
        ]),
    },
    "art-history-c2-l35": {
        "data_table": table(["Feature", "Detail"], [
            ["Cubism", "Fragmented and reassembled forms into geometric, multi-perspective compositions"],
        ]),
    },
    "art-history-c2-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Futurism", "Celebrated speed, technology, and the dynamism of modern life"],
        ]),
    },
    "art-history-c2-l37": {
        "data_table": table(["Feature", "Detail"], [
            ["German Expressionism", "Distorted form and color to convey raw emotional states"],
        ]),
    },
    "art-history-c2-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Dada", "Rejected conventional aesthetics and logic in response to World War I"],
        ]),
    },
    "art-history-c2-l39": {
        "data_table": table(["Feature", "Detail"], [
            ["Surrealism", "Explored dreams and the unconscious mind through unexpected imagery"],
        ]),
    },
    "art-history-c2-l40": {
        "data_table": table(["Feature", "Detail"], [
            ["De Stijl", "Reduced art to primary colors and geometric abstraction"],
        ]),
    },
    "art-history-c2-l41": {
        "data_table": table(["Principle", "Detail"], [
            ["Bauhaus philosophy", "United fine art, craft, and functional design"],
        ]),
    },
    "art-history-c2-l42": {
        "data_table": table(["Feature", "Detail"], [
            ["Abstract Expressionism", "Emphasized spontaneous, large-scale gesture and emotion over representation"],
        ]),
    },
    "art-history-c2-l43": {
        "data_table": table(["Feature", "Detail"], [
            ["Pop Art", "Drew on advertising and mass media imagery to comment on consumer culture"],
        ]),
    },
    "art-history-c2-l44": {
        "data_table": table(["Feature", "Detail"], [
            ["Minimalism", "Reduced art to simple geometric forms and industrial materials"],
        ]),
    },
    "art-history-c2-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Conceptual art", "Prioritized the idea behind a work over its physical execution"],
        ]),
    },
    "art-history-c2-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Land art", "Created large-scale interventions directly in natural landscapes"],
        ]),
    },
    "art-history-c2-l47": {
        "data_table": table(["Focus", "Detail"], [
            ["Feminist art", "Challenged institutional exclusion of women artists and gendered representation"],
        ]),
    },
    "art-history-c2-l48": {
        "data_table": table(["Focus", "Detail"], [
            ["Postmodern critique", "Questioned the authority and biases of the traditional art canon"],
        ]),
    },
    "art-history-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Biennial circuit", "A global network of recurring international contemporary art exhibitions"],
        ]),
    },
    "art-history-c2-l50": {
        "data_table": table(["Shift", "Detail"], [
            ["Street art's institutional reception", "Moved from illegal public art to gallery and museum acceptance"],
        ]),
    },
    "art-history-c2-l51": {
        "data_table": table(["Level", "Focus"], [
            ["Iconography", "Identifies the subject matter of a work"], ["Iconology", "Interprets a work's deeper cultural and symbolic meaning"],
        ]),
    },
    "art-history-c2-l52": {
        "data_table": table(["Approach", "Focus"], [
            ["Marxist art history", "Analyzes art through class structure and economic conditions"],
        ]),
    },
    "art-history-c2-l53": {
        "data_table": table(["Approach", "Focus"], [
            ["Postcolonial art history", "Examines how colonialism shaped artistic production and its interpretation"],
        ]),
    },
    "art-history-c2-l54": {
        "data_table": table(["Critique", "Detail"], [
            ["The art historical canon", "Criticized for historically underrepresenting women and non-Western artists"],
        ]),
    },
    "art-history-c2-l55": {
        "data_table": table(["Method", "Use"], [
            ["X-ray imaging", "Reveals underdrawings and alterations beneath a painting's surface"],
        ]),
    },
    "art-history-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Restitution", "The return of looted or unethically acquired cultural artifacts to their origin"],
        ]),
    },
    "art-history-c2-l57": {
        "data_table": table(["Venue", "Role"], [
            ["Auction house", "Facilitates public sale of artworks, often setting market prices"],
        ]),
    },
    "art-history-c2-l58": {
        "data_table": table(["Role", "Focus"], [
            ["Curator", "Selects, organizes, and interprets works for public exhibition"],
        ]),
    },
    "art-history-c2-l59": {
        "data_table": table(["Shift", "Detail"], [
            ["Photography's acceptance", "Gradually recognized as fine art rather than purely mechanical reproduction"],
        ]),
    },
    "art-history-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Developing a visual argument", "Anchors an art history paper around close analysis of specific works"],
        ]),
    },
    "art-history-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Reading medieval symbolism", "Interpreting religious iconography in a specific work"],
        ]),
    },
    "art-history-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Identifying Renaissance techniques", "Spotting linear perspective in a specific painting"],
        ]),
    },
    "art-history-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing early Christian art", "Interpreting symbolism in a catacomb fresco"],
        ]),
    },
    "art-history-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing mosaic techniques", "Contrasting Ravenna and Constantinople mosaic styles"],
        ]),
    },
    "art-history-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Tracing theological debate in art", "Connecting iconoclasm to changes in Byzantine visual culture"],
        ]),
    },
    "art-history-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Identifying stylistic revival", "Spotting classical Roman influence in Carolingian art"],
        ]),
    },
    "art-history-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing pilgrimage architecture", "Explaining how church design accommodated large crowds"],
        ]),
    },
    "art-history-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing structural innovation", "Explaining how flying buttresses enabled taller Gothic walls"],
        ]),
    },
    "art-history-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Tracing stylistic change", "Comparing rigid Romanesque and naturalistic Gothic figures"],
        ]),
    },
    "art-history-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing manuscript illumination", "Interpreting the relationship between text and image on a page"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Art History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Art History lessons (completing 70/70).")


if __name__ == "__main__":
    main()
