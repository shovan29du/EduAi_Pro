#!/usr/bin/env python3
"""Depth pass, C1 Art: fill in real, hand-checked data_table content for
the 69 C1 Art lessons not covered by the earlier breadth-first batch.
Brings C1 Art to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-c1-l1": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points, the basic building block of drawing"],
        ]),
    },
    "art-c1-l2": {
        "data_table": table(["Period", "Feature"], [
            ["Renaissance", "Revival of classical ideals and realistic perspective"],
        ]),
    },
    "art-c1-l4": {
        "data_table": table(["Color Type", "Example"], [
            ["Primary colors", "Red, blue, yellow"], ["Complementary colors", "Pairs opposite on the color wheel, like red and green"],
        ]),
    },
    "art-c1-l5": {
        "data_table": table(["Medium", "Feature"], [
            ["Oil paint", "Slow-drying, blends smoothly for rich color"], ["Watercolor", "Fast-drying, transparent washes of color"],
        ]),
    },
    "art-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Vanishing point", "The point where parallel lines appear to converge in perspective drawing"],
        ]),
    },
    "art-c1-l7": {
        "data_table": table(["Technique", "Purpose"], [
            ["Proportion study", "Ensures accurate relative sizing of body parts"],
        ]),
    },
    "art-c1-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Cohesive theme", "Ties diverse works into a unified body of work"],
        ]),
    },
    "art-c1-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Digital tablet", "Enables pressure-sensitive drawing directly on screen"],
        ]),
    },
    "art-c1-l10": {
        "data_table": table(["Form", "Example"], [
            ["Video art", "Uses moving image as the primary medium"], ["Sound art", "Uses audio as the primary medium"],
        ]),
    },
    "art-c1-l11": {
        "data_table": table(["Type", "Example"], [
            ["Mural", "Large-scale painting on a public wall"], ["Sculpture", "Three-dimensional public monument"],
        ]),
    },
    "art-c1-l12": {
        "data_table": table(["Element", "Question"], [
            ["Formal analysis", "How do color and composition affect the work?"],
        ]),
    },
    "art-c1-l13": {
        "data_table": table(["Task", "Purpose"], [
            ["Selecting works", "Chooses pieces that create a coherent exhibition narrative"],
        ]),
    },
    "art-c1-l14": {
        "data_table": table(["Aspect", "Consideration"], [
            ["Pricing artwork", "Balances materials, time, and market demand"],
        ]),
    },
    "art-c1-l15": {
        "data_table": table(["Use", "Example"], [
            ["Editorial illustration", "Accompanies articles to visually convey ideas"],
        ]),
    },
    "art-c1-l16": {
        "data_table": table(["Principle", "Meaning"], [
            ["Squash and stretch", "Gives objects a sense of weight and flexibility in motion"],
        ]),
    },
    "art-c1-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Composition", "Arranges visual elements within the frame for impact"],
        ]),
    },
    "art-c1-l18": {
        "data_table": table(["Feature", "Detail"], [
            ["Installation art", "Immersive, often site-specific works that transform a space"],
        ]),
    },
    "art-c1-l19": {
        "data_table": table(["Method", "Purpose"], [
            ["Demonstration", "Shows students a technique step by step"],
        ]),
    },
    "art-c1-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Unifying theme", "Connects individual pieces into one cohesive statement"],
        ]),
    },
    "art-c1-l21": {
        "data_table": table(["Method", "Example"], [
            ["Additive sculpture", "Building up material, like clay modeling"], ["Subtractive sculpture", "Removing material, like carving stone"],
        ]),
    },
    "art-c1-l22": {
        "data_table": table(["Technique", "Example"], [
            ["Pinch pot", "Shaped by pinching clay between fingers"], ["Coil building", "Stacking rolled clay coils to build form"],
        ]),
    },
    "art-c1-l23": {
        "data_table": table(["Step", "Purpose"], [
            ["Centering the clay", "Aligns the clay on the wheel before shaping"],
        ]),
    },
    "art-c1-l24": {
        "data_table": table(["Type", "Feature"], [
            ["Relief printmaking", "Ink is applied to a raised surface, like a woodcut"], ["Intaglio", "Ink fills recessed lines, like etching"],
        ]),
    },
    "art-c1-l25": {
        "data_table": table(["Material", "Use"], [
            ["Found paper", "Adds texture and layered meaning to a collage"],
        ]),
    },
    "art-c1-l26": {
        "data_table": table(["Technique", "Example"], [
            ["Weaving", "Interlacing fibers to create fabric"], ["Embroidery", "Stitching decorative designs onto fabric"],
        ]),
    },
    "art-c1-l27": {
        "data_table": table(["Step", "Purpose"], [
            ["Grid transfer", "Scales a small design accurately onto a large wall"],
        ]),
    },
    "art-c1-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Soldering", "Joins metal pieces using heat and filler metal"],
        ]),
    },
    "art-c1-l29": {
        "data_table": table(["Technique", "Example"], [
            ["Glassblowing", "Shaping molten glass by blowing air through a tube"],
        ]),
    },
    "art-c1-l30": {
        "data_table": table(["Technique", "Purpose"], [
            ["Signature binding", "Folds and sews pages into a durable book structure"],
        ]),
    },
    "art-c1-l31": {
        "data_table": table(["Technique", "Purpose"], [
            ["Gesture drawing", "Quickly captures the model's overall pose and movement"],
        ]),
    },
    "art-c1-l32": {
        "data_table": table(["Element", "Consideration"], [
            ["Lighting", "Shapes shadow and form in a still life setup"],
        ]),
    },
    "art-c1-l33": {
        "data_table": table(["Element", "Purpose"], [
            ["Atmospheric perspective", "Uses color and clarity shifts to suggest distance"],
        ]),
    },
    "art-c1-l34": {
        "data_table": table(["Principle", "Meaning"], [
            ["Non-representational form", "Uses shape and color independent of recognizable subjects"],
        ]),
    },
    "art-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Typeface", "A consistent design of lettering used across a body of text"],
        ]),
    },
    "art-c1-l36": {
        "data_table": table(["Purpose", "Detail"], [
            ["Storyboard", "Plans the sequence and composition of shots before production"],
        ]),
    },
    "art-c1-l37": {
        "data_table": table(["Use", "Example"], [
            ["Concept art", "Visualizes characters, settings, or props before final production"],
        ]),
    },
    "art-c1-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Silhouette", "Tests whether a character reads clearly at a glance"],
        ]),
    },
    "art-c1-l39": {
        "data_table": table(["Element", "Purpose"], [
            ["Mood and lighting", "Establishes the emotional tone of a setting"],
        ]),
    },
    "art-c1-l40": {
        "data_table": table(["Element", "Purpose"], [
            ["Panel layout", "Guides the reader's pacing through a sequence"],
        ]),
    },
    "art-c1-l41": {
        "data_table": table(["Technique", "Detail"], [
            ["Frame-by-frame animation", "Physical objects photographed incrementally to simulate motion"],
        ]),
    },
    "art-c1-l42": {
        "data_table": table(["Tool", "Use"], [
            ["Sculpting software", "Digitally shapes 3D models, like clay in virtual space"],
        ]),
    },
    "art-c1-l43": {
        "data_table": table(["Challenge", "Detail"], [
            ["Changing light", "Requires quick decisions as natural light shifts outdoors"],
        ]),
    },
    "art-c1-l44": {
        "data_table": table(["Feature", "Detail"], [
            ["Monotype", "Produces a single, unique print from a painted plate"],
        ]),
    },
    "art-c1-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Encaustic painting", "Uses heated pigmented wax applied to a surface"],
        ]),
    },
    "art-c1-l46": {
        "data_table": table(["Technique", "Effect"], [
            ["Blending", "Softens transitions between pastel colors"],
        ]),
    },
    "art-c1-l47": {
        "data_table": table(["Technique", "Effect"], [
            ["Ink wash", "Creates gradients of tone using diluted ink"],
        ]),
    },
    "art-c1-l48": {
        "data_table": table(["Element", "Purpose"], [
            ["Stroke rhythm", "Gives calligraphic writing visual flow and expression"],
        ]),
    },
    "art-c1-l49": {
        "data_table": table(["Step", "Purpose"], [
            ["Creating a stencil", "Blocks ink from reaching specific areas of the print"],
        ]),
    },
    "art-c1-l50": {
        "data_table": table(["Material", "Use"], [
            ["Tesserae", "Small tiles or fragments assembled to form a mosaic image"],
        ]),
    },
    "art-c1-l51": {
        "data_table": table(["Material", "Use"], [
            ["Found objects", "Repurposed everyday items incorporated into a sculptural work"],
        ]),
    },
    "art-c1-l52": {
        "data_table": table(["Feature", "Detail"], [
            ["Kinetic art", "Incorporates movement, whether motorized or wind-driven, as part of the work"],
        ]),
    },
    "art-c1-l53": {
        "data_table": table(["Feature", "Detail"], [
            ["Site-specific art", "Created for and responsive to a particular location"],
        ]),
    },
    "art-c1-l54": {
        "data_table": table(["Technique", "Purpose"], [
            ["Timed poses", "Trains quick observation of overall form and motion"],
        ]),
    },
    "art-c1-l55": {
        "data_table": table(["Technique", "Effect"], [
            ["Cross-hatching", "Layers intersecting lines to build up shadow and value"],
        ]),
    },
    "art-c1-l56": {
        "data_table": table(["Technique", "Effect"], [
            ["Wet-on-wet", "Colors blend softly when applied to still-wet paper"],
        ]),
    },
    "art-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Pigment", "The colored substance that gives paint its hue"],
        ]),
    },
    "art-c1-l58": {
        "data_table": table(["Support", "Use"], [
            ["Canvas", "A woven fabric surface typically used for painting"], ["Panel", "A rigid wood or composite surface for painting"],
        ]),
    },
    "art-c1-l59": {
        "data_table": table(["Element", "Purpose"], [
            ["Artist statement", "Explains the intent and context behind a body of work"],
        ]),
    },
    "art-c1-l60": {
        "data_table": table(["Opportunity", "Purpose"], [
            ["Residency", "Provides artists time, space, and resources to focus on new work"],
        ]),
    },
    "art-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying line and value", "Sketching a simple object using varied line weight"],
        ]),
    },
    "art-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing art periods", "Contrasting Renaissance realism with Baroque drama"],
        ]),
    },
    "art-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Rendering form", "Using value gradients to suggest a rounded surface"],
        ]),
    },
    "art-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Mixing complementary colors", "Combining opposites to create a neutral gray"],
        ]),
    },
    "art-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Comparing painting media", "Contrasting the drying time of oil versus watercolor"],
        ]),
    },
    "art-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Drawing in perspective", "Constructing a simple room using a single vanishing point"],
        ]),
    },
    "art-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Studying proportion", "Comparing head-to-body ratios in a figure sketch"],
        ]),
    },
    "art-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Assembling a portfolio", "Selecting a consistent set of works to represent one's style"],
        ]),
    },
    "art-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Exploring digital brushes", "Comparing digital and traditional mark-making"],
        ]),
    },
    "art-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing new media", "Examining how video art changes the viewer's relationship to time"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Art lessons (completing 70/70).")


if __name__ == "__main__":
    main()
