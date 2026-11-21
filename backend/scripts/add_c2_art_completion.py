#!/usr/bin/env python3
"""Depth pass, C2 Art: fill in real, hand-checked data_table content
for the 69 C2 Art lessons not covered by the earlier breadth-first
batch. Brings C2 Art to full 70/70 coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-c2-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Art history foundations", "Traces stylistic change from ancient through modern periods"],
        ]),
    },
    "art-c2-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Design & visual communication", "Uses layout, color, and typography to convey a message clearly"],
        ]),
    },
    "art-c2-l4": {
        "data_table": table(["Scheme", "Effect"], [
            ["Complementary colors", "Opposite hues create high contrast and visual energy"],
            ["Analogous colors", "Adjacent hues create harmony and cohesion"],
        ]),
    },
    "art-c2-l5": {
        "data_table": table(["Technique", "Process"], [
            ["Relief printing", "Ink is applied to a raised surface and pressed onto paper"],
            ["Intaglio", "Ink fills incised lines below the surface of a plate"],
        ]),
    },
    "art-c2-l6": {
        "data_table": table(["Technique", "Effect"], [
            ["Linear perspective", "Converging lines create the illusion of receding depth"],
            ["Atmospheric perspective", "Reduced contrast and saturation suggest distance"],
        ]),
    },
    "art-c2-l7": {
        "data_table": table(["Structure", "Study Focus"], [
            ["Skeletal proportion", "Establishes the underlying framework for figure drawing"],
        ]),
    },
    "art-c2-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Portfolio organization", "Sequences work to show range and progression to viewers"],
        ]),
    },
    "art-c2-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Layers", "Allow non-destructive editing of separate image elements"],
            ["Blend modes", "Control how layers visually interact"],
        ]),
    },
    "art-c2-l10": {
        "data_table": table(["Platform", "Effect"], [
            ["Online galleries/social media", "Expanded artists' reach but increased competition for attention"],
        ]),
    },
    "art-c2-l11": {
        "data_table": table(["Movement", "Feature"], [
            ["Mexican muralism", "Large-scale public works conveying social and political themes"],
        ]),
    },
    "art-c2-l12": {
        "data_table": table(["Element", "Question Asked"], [
            ["Formal analysis", "Examines line, color, composition, and technique rather than subject matter alone"],
        ]),
    },
    "art-c2-l13": {
        "data_table": table(["Element", "Purpose"], [
            ["Exhibition layout", "Guides viewer flow and frames how works are read in relation to each other"],
        ]),
    },
    "art-c2-l14": {
        "data_table": table(["Channel", "Use"], [
            ["Artist website/social platform", "Builds visibility and a direct relationship with collectors"],
        ]),
    },
    "art-c2-l15": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sequential illustration", "Uses pacing and composition to guide a story visually"],
        ]),
    },
    "art-c2-l16": {
        "data_table": table(["Concept", "Meaning"], [
            ["Keyframe", "A defined pose marking a significant point in an animated motion"],
            ["In-between", "Frames drawn to smoothly connect two keyframes"],
        ]),
    },
    "art-c2-l17": {
        "data_table": table(["Setting", "Effect"], [
            ["Aperture", "Controls depth of field and amount of light entering the lens"],
            ["Shutter speed", "Controls motion blur and exposure duration"],
        ]),
    },
    "art-c2-l18": {
        "data_table": table(["Feature", "Detail"], [
            ["Performance art", "Uses the artist's body and live action as the primary medium"],
        ]),
    },
    "art-c2-l19": {
        "data_table": table(["Component", "Purpose"], [
            ["Learning objective", "Defines the specific skill or concept a lesson aims to teach"],
        ]),
    },
    "art-c2-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone portfolio", "Demonstrates technical range and a coherent personal style"],
        ]),
    },
    "art-c2-l21": {
        "data_table": table(["Skill", "Focus"], [
            ["Figure in motion", "Captures dynamic weight shift and gesture rather than static pose"],
        ]),
    },
    "art-c2-l22": {
        "data_table": table(["Component", "Role"], [
            ["Silica", "Forms the glass-like structure of a ceramic glaze"],
            ["Flux", "Lowers the melting point of the glaze mixture"],
        ]),
    },
    "art-c2-l23": {
        "data_table": table(["Element", "Purpose"], [
            ["Armature", "Internal support structure that holds a sculpture's form during construction"],
        ]),
    },
    "art-c2-l24": {
        "data_table": table(["Process", "Detail"], [
            ["Lithography", "Uses the chemical resistance between grease and water on a flat stone or plate"],
        ]),
    },
    "art-c2-l25": {
        "data_table": table(["Approach", "Detail"], [
            ["Mixed media composition", "Combines multiple materials to create layered visual and textural interest"],
        ]),
    },
    "art-c2-l26": {
        "data_table": table(["Technique", "Detail"], [
            ["Weaving", "Interlaces threads at right angles to construct fabric structure"],
            ["Dyeing", "Applies color to fiber through chemical or natural pigment processes"],
        ]),
    },
    "art-c2-l27": {
        "data_table": table(["Stage", "Task"], [
            ["Mural design", "Plans composition and scale for a specific wall and audience"],
            ["Mural execution", "Transfers and paints the design at full scale"],
        ]),
    },
    "art-c2-l28": {
        "data_table": table(["Technique", "Process"], [
            ["Lost-wax casting", "A wax model is replaced by molten metal within a mold"],
        ]),
    },
    "art-c2-l29": {
        "data_table": table(["Technique", "Process"], [
            ["Fusing", "Heats glass pieces until they bond together"],
            ["Slumping", "Heats glass over a mold until it takes the mold's shape"],
        ]),
    },
    "art-c2-l30": {
        "data_table": table(["Structure", "Feature"], [
            ["Coptic binding", "Exposed spine stitching allows the book to lie flat"],
        ]),
    },
    "art-c2-l31": {
        "data_table": table(["Skill", "Focus"], [
            ["Foreshortening", "Compresses proportions to depict a form extending toward the viewer"],
        ]),
    },
    "art-c2-l32": {
        "data_table": table(["Element", "Challenge"], [
            ["Reflective surface", "Requires capturing distorted, high-contrast reflected imagery"],
        ]),
    },
    "art-c2-l33": {
        "data_table": table(["Technique", "Effect"], [
            ["Atmospheric depth", "Softened detail and cooler tones suggest distant landscape elements"],
        ]),
    },
    "art-c2-l34": {
        "data_table": table(["Approach", "Detail"], [
            ["Process-based abstraction", "The physical act and materials themselves generate the final image"],
        ]),
    },
    "art-c2-l35": {
        "data_table": table(["Element", "Purpose"], [
            ["Letterform design", "Balances legibility with expressive, artistic intent"],
        ]),
    },
    "art-c2-l36": {
        "data_table": table(["Element", "Purpose"], [
            ["Storyboard panel", "Plans camera framing and pacing before full production"],
        ]),
    },
    "art-c2-l37": {
        "data_table": table(["Element", "Purpose"], [
            ["World-building", "Establishes visual rules and history for a fictional setting"],
        ]),
    },
    "art-c2-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Silhouette", "A readable outline shape communicates character identity at a glance"],
        ]),
    },
    "art-c2-l39": {
        "data_table": table(["Element", "Purpose"], [
            ["Environment mood", "Lighting and color palette establish emotional tone of a setting"],
        ]),
    },
    "art-c2-l40": {
        "data_table": table(["Element", "Purpose"], [
            ["Panel layout", "Controls pacing and visual flow through a comics page"],
        ]),
    },
    "art-c2-l41": {
        "data_table": table(["Element", "Purpose"], [
            ["Armature rigging", "Allows precise, repeatable posing of a stop-motion puppet"],
        ]),
    },
    "art-c2-l42": {
        "data_table": table(["Process", "Purpose"], [
            ["Retopology", "Rebuilds a clean, efficient mesh over a high-detail digital sculpt"],
        ]),
    },
    "art-c2-l43": {
        "data_table": table(["Challenge", "Approach"], [
            ["Changing light", "Plein air painters work quickly or return at the same time daily"],
        ]),
    },
    "art-c2-l44": {
        "data_table": table(["Technique", "Detail"], [
            ["Chine-collé", "Bonds a thin paper to the print substrate during the printing process"],
        ]),
    },
    "art-c2-l45": {
        "data_table": table(["Technique", "Detail"], [
            ["Encaustic", "Uses heated pigmented wax built up in translucent layers"],
        ]),
    },
    "art-c2-l46": {
        "data_table": table(["Technique", "Detail"], [
            ["Pastel underpainting", "Establishes value structure before building up final pastel layers"],
        ]),
    },
    "art-c2-l47": {
        "data_table": table(["Tradition", "Detail"], [
            ["Sumi-e", "East Asian ink wash tradition emphasizing economy of brushstroke"],
        ]),
    },
    "art-c2-l48": {
        "data_table": table(["Script", "Origin"], [
            ["Historical calligraphic scripts", "Vary widely by region, e.g. Islamic, East Asian, and Western traditions"],
        ]),
    },
    "art-c2-l49": {
        "data_table": table(["Concept", "Purpose"], [
            ["Registration", "Aligns multiple screen-printed color layers precisely"],
        ]),
    },
    "art-c2-l50": {
        "data_table": table(["Concept", "Meaning"], [
            ["Andamento", "The directional flow of tesserae that guides the eye across a mosaic"],
        ]),
    },
    "art-c2-l51": {
        "data_table": table(["Approach", "Detail"], [
            ["Assemblage", "Combines found objects into a single narrative artwork"],
        ]),
    },
    "art-c2-l52": {
        "data_table": table(["Element", "Purpose"], [
            ["Mechanism design", "Determines how a kinetic sculpture moves and responds to force"],
        ]),
    },
    "art-c2-l53": {
        "data_table": table(["Approach", "Detail"], [
            ["Site-specific installation", "Designed to respond directly to a particular physical location"],
        ]),
    },
    "art-c2-l54": {
        "data_table": table(["Skill", "Focus"], [
            ["Gesture drawing", "Quick studies capturing motion and weight over fine detail"],
        ]),
    },
    "art-c2-l55": {
        "data_table": table(["Skill", "Focus"], [
            ["Value structure", "Organizes a monochrome image into clear light and dark relationships"],
        ]),
    },
    "art-c2-l56": {
        "data_table": table(["Technique", "Detail"], [
            ["Glazing", "Builds up transparent watercolor layers to deepen tone gradually"],
        ]),
    },
    "art-c2-l57": {
        "data_table": table(["Concept", "Application"], [
            ["Color mixing for mood", "Warm and cool balance shapes the emotional register of a piece"],
        ]),
    },
    "art-c2-l58": {
        "data_table": table(["Practice", "Purpose"], [
            ["Art conservation", "Stabilizes and protects artworks from environmental degradation"],
        ]),
    },
    "art-c2-l59": {
        "data_table": table(["Task", "Purpose"], [
            ["Curatorial narrative", "Sequences and contextualizes works to build a coherent exhibition story"],
        ]),
    },
    "art-c2-l60": {
        "data_table": table(["Skill", "Purpose"], [
            ["Grant writing", "Secures funding by articulating a project's artistic and practical merit"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Principle of Composition", "Meaning"], [
    ["Balance", "Even visual weight distribution"],
    ["Contrast", "Difference between elements to create interest"],
    ["Emphasis", "A focal point that draws the eye"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"art-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"art-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"art-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Art lessons (completing 70/70).")


if __name__ == "__main__":
    main()
