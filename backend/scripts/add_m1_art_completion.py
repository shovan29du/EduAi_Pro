#!/usr/bin/env python3
"""Depth pass, M1 Art: fill in real, hand-checked data_table content
for the 99 M1 Art lessons not covered by the earlier breadth-first
batch. Brings M1 Art to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Design & visual communication", "Uses layout, color, and typography to convey a message clearly"],
        ]),
    },
    "art-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Contemporary & critical art practice", "Engages current theoretical discourse as part of studio process"],
        ]),
    },
    "art-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Color as material", "Treats color choice as a conceptual and perceptual decision, not just decoration"],
        ]),
    },
    "art-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Material investigation", "The chosen medium itself carries and shapes conceptual meaning"],
        ]),
    },
    "art-m1-l6": {
        "data_table": table(["Theory", "Detail"], [
            ["Perceptual theory of space", "Examines how the eye and mind construct spatial depth from visual cues"],
        ]),
    },
    "art-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["The body in contemporary art", "Uses the artist's or subject's body as primary material and site of meaning"],
        ]),
    },
    "art-m1-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Professional portfolio", "Frames a body of work with a coherent artistic statement of intent"],
        ]),
    },
    "art-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital art practice", "Uses digital tools not just for production but as a conceptual medium itself"],
        ]),
    },
    "art-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["New media art theory", "Examines how emerging technologies reshape artistic form and audience interaction"],
        ]),
    },
    "art-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Public art ethics", "Community collaboration raises questions of authorship, consent, and representation"],
        ]),
    },
    "art-m1-l12": {
        "data_table": table(["Method", "Purpose"], [
            ["Art criticism methodology", "Provides structured frameworks for evaluating and interpreting artworks"],
        ]),
    },
    "art-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Curatorial practice", "Shapes meaning through the selection and arrangement of works in an exhibition"],
        ]),
    },
    "art-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Professional practice", "Covers the practical business skills required to sustain an art career"],
        ]),
    },
    "art-m1-l15": {
        "data_table": table(["Skill", "Focus"], [
            ["Advanced illustration", "Develops a distinctive visual voice suited to narrative or editorial commission"],
        ]),
    },
    "art-m1-l16": {
        "data_table": table(["Skill", "Focus"], [
            ["Advanced animation production", "Manages the full pipeline from storyboard through final rendered sequence"],
        ]),
    },
    "art-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Photography as research", "Treats the camera as a tool for investigating a sustained conceptual question"],
        ]),
    },
    "art-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Installation/performance as research", "Uses embodied, spatial practice to investigate and generate new knowledge"],
        ]),
    },
    "art-m1-l19": {
        "data_table": table(["Theory", "Detail"], [
            ["Art education theory", "Examines pedagogical approaches to teaching creative practice and critique"],
        ]),
    },
    "art-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Thesis exhibition", "Culminates graduate study in a curated public presentation of original work"],
        ]),
    },
    "art-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Dematerialization", "Post-studio practice shifts focus from crafted objects toward idea and process"],
        ]),
    },
    "art-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Site-specificity", "A work is conceived in direct relation to its particular physical location"],
        ]),
    },
    "art-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Feminist art theory", "Examines gender's role in artistic production, representation, and reception"],
        ]),
    },
    "art-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Postcolonial art perspective", "Reframes artistic value beyond a single dominant cultural tradition"],
        ]),
    },
    "art-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Expanded printmaking", "Extends traditional print processes into installation and hybrid media"],
        ]),
    },
    "art-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Industrial fabrication", "Applies manufacturing processes and materials to sculptural production"],
        ]),
    },
    "art-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Artist as researcher", "Treats archival investigation as a generative source for new artistic work"],
        ]),
    },
    "art-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Textile/fiber medium", "Elevates craft-associated materials into contemporary fine art practice"],
        ]),
    },
    "art-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Land art", "Uses the natural landscape itself as sculptural material and site"],
        ]),
    },
    "art-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Ceramics as sculpture", "Positions clay as a serious sculptural language beyond functional craft"],
        ]),
    },
    "art-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Institutional critique", "Art that examines and challenges the museum or gallery's own power structures"],
        ]),
    },
    "art-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Sound art", "Uses auditory experience as the primary medium of an installation"],
        ]),
    },
    "art-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Appropriation", "Reuses existing imagery to raise questions about originality and authorship"],
        ]),
    },
    "art-m1-l34": {
        "data_table": table(["Skill", "Focus"], [
            ["Nonlinear video editing", "Structures video narrative outside strict chronological sequence"],
        ]),
    },
    "art-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Tactical media", "Uses accessible media tools for short-term, activist-driven artistic intervention"],
        ]),
    },
    "art-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Artist's book", "Treats the book form itself as a sculptural or conceptual artwork"],
        ]),
    },
    "art-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Psychoanalytic image-making", "Applies concepts like the unconscious and desire to interpreting visual art"],
        ]),
    },
    "art-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Kinetic art", "Incorporates real or apparent movement as a core element of the work"],
        ]),
    },
    "art-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Craft hierarchy critique", "Questions the traditional divide separating fine art from craft materials"],
        ]),
    },
    "art-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Artist-run publishing", "Independent print production as a form of artistic distribution and community"],
        ]),
    },
    "art-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Biennial culture", "Large recurring international exhibitions shape global contemporary art discourse"],
        ]),
    },
    "art-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Light as medium", "Treats illumination itself as a sculptural material rather than mere display"],
        ]),
    },
    "art-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["The artist's studio", "Functions historically as both a workspace and a socially significant site"],
        ]),
    },
    "art-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Collage/assemblage", "Combines disparate found materials into a unified new composition"],
        ]),
    },
    "art-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Queer theory in visual culture", "Examines how images construct and challenge norms of gender and sexuality"],
        ]),
    },
    "art-m1-l46": {
        "data_table": table(["Technique", "Purpose"], [
            ["Mold-making and casting", "Reproduces a form precisely for editioned or multiple sculptural works"],
        ]),
    },
    "art-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Cybernetics to AI in art", "Traces a lineage of artists engaging feedback systems and machine intelligence"],
        ]),
    },
    "art-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Drawing machine", "Automated or mechanical systems generate mark-making beyond the artist's direct hand"],
        ]),
    },
    "art-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Diaspora in contemporary art", "Displacement and migration shape identity as recurring artistic subject matter"],
        ]),
    },
    "art-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Large-format painting", "Scale itself becomes a deliberate strategy shaping viewer physical experience"],
        ]),
    },
    "art-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Object-oriented ontology", "Philosophical framework treating objects as having existence independent of human perception"],
        ]),
    },
    "art-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Ephemeral materials", "Uses perishable substances to foreground time, decay, and impermanence"],
        ]),
    },
    "art-m1-l53": {
        "data_table": table(["Skill", "Focus"], [
            ["Art criticism writing", "Develops a clear, evidence-based critical voice for evaluating artworks"],
        ]),
    },
    "art-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Augmented reality exhibition", "Overlays digital content onto physical gallery space for viewers"],
        ]),
    },
    "art-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Commemorative art", "Uses artistic form to process collective trauma and preserve memory"],
        ]),
    },
    "art-m1-l56": {
        "data_table": table(["Technique", "Detail"], [
            ["Encaustic painting", "Uses heated pigmented wax built up in translucent layers"],
        ]),
    },
    "art-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Global contemporary art since 1989", "Marks a shift toward genuinely global, decentralized art discourse"],
        ]),
    },
    "art-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Artist residency", "Provides dedicated time and space abroad to develop new work and networks"],
        ]),
    },
    "art-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Disability studies in art", "Examines accessibility and representation of disabled experience in contemporary art"],
        ]),
    },
    "art-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Performance documentation", "Raises questions about how ephemeral live work is preserved and represented"],
        ]),
    },
    "art-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Commercial gallery system", "Art fairs and galleries shape which artists gain market visibility"],
        ]),
    },
    "art-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Collective studio practice", "Shared authorship challenges the myth of the solitary individual artist"],
        ]),
    },
    "art-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Politics of display", "Vitrines and pedestals subtly shape how a work is perceived and valued"],
        ]),
    },
    "art-m1-l64": {
        "data_table": table(["Technique", "Detail"], [
            ["Glassblowing", "Shapes molten glass using controlled heat and breath in a hot-shop environment"],
        ]),
    },
    "art-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Ecocritical materials sourcing", "Considers environmental impact in choosing studio materials"],
        ]),
    },
    "art-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Painterly abstraction after modernism", "Extends abstract painting's formal legacy into contemporary concerns"],
        ]),
    },
    "art-m1-l67": {
        "data_table": table(["Skill", "Purpose"], [
            ["Grant narrative writing", "Communicates an artistic vision persuasively to funding bodies"],
        ]),
    },
    "art-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Wearable art", "Blurs the line between garment, sculpture, and body-based performance object"],
        ]),
    },
    "art-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Iconoclasm", "The deliberate destruction of images carries political and religious significance"],
        ]),
    },
    "art-m1-l70": {
        "data_table": table(["Technique", "Detail"], [
            ["Intaglio etching", "Uses acid to incise lines into a plate, which are then inked and printed"],
        ]),
    },
    "art-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["The uncanny", "Art that evokes an unsettling familiarity mixed with strangeness"],
        ]),
    },
    "art-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Public sculpture commissioning", "Involves navigating stakeholder review and site logistics beyond studio work"],
        ]),
    },
    "art-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Art and the Anthropocene", "Contemporary art increasingly grapples with human-driven environmental change"],
        ]),
    },
    "art-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Algorithmic drawing", "Generates visual mark-making through defined computational rules"],
        ]),
    },
    "art-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Private patronage", "Individual collectors continue to shape which artists gain sustained support"],
        ]),
    },
    "art-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Neon as medium", "Illuminated signage techniques repurposed as fine art material"],
        ]),
    },
    "art-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Art restitution debate", "Contemporary museums face growing pressure to return contested colonial-era holdings"],
        ]),
    },
    "art-m1-l78": {
        "data_table": table(["Structure", "Feature"], [
            ["Coptic binding", "Exposed spine stitching allows an artist's book to lie flat"],
        ]),
    },
    "art-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Studio visit", "A structured critical dialogue between artist and viewer within the working space"],
        ]),
    },
    "art-m1-l80": {
        "data_table": table(["Technique", "Detail"], [
            ["Fresco", "Applies pigment to wet plaster so color bonds permanently as the wall dries"],
        ]),
    },
    "art-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Art world social capital", "Professional networks significantly shape opportunity and visibility for artists"],
        ]),
    },
    "art-m1-l82": {
        "data_table": table(["Technique", "Detail"], [
            ["3D printing", "Builds sculptural forms additively, layer by layer, from digital models"],
        ]),
    },
    "art-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Decolonizing the museum", "Reexamines how collections were acquired and how they are interpreted today"],
        ]),
    },
    "art-m1-l84": {
        "data_table": table(["Technique", "Detail"], [
            ["Large-scale watercolor", "Extends a traditionally intimate medium to work at monumental scale"],
        ]),
    },
    "art-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Affect theory in viewing", "Studies emotional and bodily response as central to how art is experienced"],
        ]),
    },
    "art-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Tattoo as artistic surface", "Positions skin-based art within broader contemporary artistic discourse"],
        ]),
    },
    "art-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Economics of studio production", "Examines the often-invisible labor costs behind finished artwork"],
        ]),
    },
    "art-m1-l88": {
        "data_table": table(["Technique", "Detail"], [
            ["Mosaic tessellation", "Arranges small tiles (tesserae) into a unified image or pattern"],
        ]),
    },
    "art-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Semiotics of visual signs", "Studies how images generate meaning through systems of signs and symbols"],
        ]),
    },
    "art-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Artist book as sequence", "Uses page-turning structure to build narrative meaning over time"],
        ]),
    },
    "art-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Art therapy theory", "Applies creative practice as a tool for psychological processing and healing"],
        ]),
    },
    "art-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Papermaking as practice", "Treats paper's fabrication itself as a meaningful artistic process"],
        ]),
    },
    "art-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Politics of portraiture", "Representing a subject's likeness carries questions of power and consent"],
        ]),
    },
    "art-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Projection mapping", "Transforms architectural surfaces into dynamic digital canvases"],
        ]),
    },
    "art-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Art historical methodology for studio artists", "Applies scholarly research methods to inform contemporary studio practice"],
        ]),
    },
    "art-m1-l96": {
        "data_table": table(["Technique", "Detail"], [
            ["Welding fabrication", "Joins metal components using heat, requiring strict safety protocol"],
        ]),
    },
    "art-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Press release as text", "Even promotional gallery writing functions as a form of critical framing"],
        ]),
    },
    "art-m1-l98": {
        "data_table": table(["Technique", "Detail"], [
            ["Stop-motion animation", "Builds motion illusion from a sequence of individually captured still frames"],
        ]),
    },
    "art-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Iconography of protest", "Visual symbols recur across movements to communicate collective political meaning"],
        ]),
    },
    "art-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Grant/fellowship strategy", "Sustaining an artistic career often depends on securing external funding support"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Element of Drawing", "Meaning"], [
        ["Line", "A mark connecting two points"],
        ["Shape", "A 2D enclosed area"],
        ["Value", "The lightness or darkness of a tone"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"art-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"art-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"art-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Art lessons (completing 120/120).")


if __name__ == "__main__":
    main()
