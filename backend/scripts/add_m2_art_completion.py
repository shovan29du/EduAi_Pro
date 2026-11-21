#!/usr/bin/env python3
"""Depth pass, M2 Art: fill in real, hand-checked data_table content
for the M2 Art lessons not covered by the earlier breadth-first
batch. Brings M2 Art to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning critical
theory in contemporary art practice, studio research methods,
conservation science, curatorial practice, new media/technology art,
socially-engaged art, and the professional art ecosystem; l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Phenomenology of making", "Merleau-Ponty's philosophy applied to how embodied studio practice shapes artistic knowledge"],
    ["Studio practice", "The lived, hands-on process of making art as a form of knowing"],
])

CHARTS: dict[str, dict] = {
    "art-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Contemporary/critical art practice research", "Systematic methods for studying and situating current art within critical theory"],
    ])},
    "art-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Art fundamentals/technique research", "Rigorous study of the technical and formal foundations underlying artistic production"],
    ])},
    "art-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Relational aesthetics", "Bourriaud's theory judging art by the social relationships and interactions it generates"],
    ])},
    "art-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Institutional critique", "Art that examines and challenges the museum or gallery's own authority"],
    ])},
    "art-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Expanded field", "Krauss's structural model showing how sculpture expanded beyond traditional categories"],
    ])},
    "art-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Object-oriented ontology (sculpture)", "Grants objects independent existence and reality apart from human perception, applied to sculpture"],
    ])},
    "art-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Affect theory (painting)", "Studies emotional and bodily intensities that a painting produces, beyond conscious meaning"],
    ])},
    "art-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Aura (Benjamin)", "The unique presence of an original artwork, which Benjamin argued is diminished by mechanical reproduction"],
    ])},
    "art-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Distribution of the sensible", "Rancière's concept of how art can reconfigure what is visible and sayable within a political order"],
    ])},
    "art-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Anachronic images", "Didi-Huberman's theory that images collapse linear time, mixing past and present"],
    ])},
    "art-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Thing theory (art object)", "Examines how an art object accrues meaning beyond its function as a mere physical thing"],
    ])},
    "art-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Practice-based research", "Treats the act of art-making itself as a legitimate method of generating new knowledge"],
    ])},
    "art-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Reflective journaling", "Documents an artist's evolving thought process as part of studio research methodology"],
    ])},
    "art-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Serial iteration", "Uses repeated variations on a form as a research strategy for artistic discovery"],
    ])},
    "art-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Failure and contingency", "Treats unexpected or 'failed' outcomes in experimental process as generative research material"],
    ])},
    "art-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Cross-media translation", "Reworks an idea or image across different artistic mediums in studio practice"],
    ])},
    "art-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Site-responsive methodology", "Develops artwork in direct dialogue with the specific characteristics of a location"],
    ])},
    "art-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Archival research (studio)", "Uses historical archives as raw source material to generate new studio work"],
    ])},
    "art-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Collaborative authorship", "Structures artistic production around shared, distributed creative ownership"],
    ])},
    "art-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Durational performance documentation", "Methods for capturing and preserving evidence of extended-duration performance art"],
    ])},
    "art-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Thesis exhibition development", "The process of moving a graduate thesis project from proposal through physical installation"],
    ])},
    "art-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Contemporary synthetic media conservation", "Addresses the unique preservation challenges of modern plastic and synthetic art materials"],
    ])},
    "art-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Pigment analysis", "Scientific methods for identifying the materials used in a historical or contemporary artwork"],
    ])},
    "art-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Time-based media conservation", "Addresses the distinct preservation problems of video, film, and software-dependent artworks"],
    ])},
    "art-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Non-invasive imaging (authentication)", "Uses techniques like X-ray or infrared imaging to examine artworks without damaging them"],
    ])},
    "art-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Bio-based studio materials", "Uses sustainable, biologically-sourced materials in contemporary art-making"],
    ])},
    "art-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Software-based art deterioration", "Studies how digital and software-dependent artworks degrade as technology changes"],
    ])},
    "art-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Forensic art authentication", "Applies scientific and technical analysis to determine an artwork's true origin"],
    ])},
    "art-m2-l30": {"data_table": table(["Type", "Feature"], [
        ["Traditional binder", "Natural materials like egg tempera or oil"],
        ["Synthetic binder", "Modern acrylic and polymer-based media"],
    ])},
    "art-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Curatorial dramaturgy", "Sequences artworks within an exhibition to construct meaning through spatial narrative"],
    ])},
    "art-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Para-curatorial practice", "Artist-led exhibitions that operate outside conventional institutional curatorial structures"],
    ])},
    "art-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Biennial culture", "Analyzes the globalized circuit of recurring international contemporary art exhibitions"],
    ])},
    "art-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Exhibition histories", "Studies past exhibitions themselves as a research method for understanding art's reception"],
    ])},
    "art-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Universal design (exhibitions)", "Designs exhibition spaces to be accessible to visitors of all abilities"],
    ])},
    "art-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Decolonizing museum display", "Rethinks collection presentation to address colonial histories and power imbalances"],
    ])},
    "art-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin exhibition", "Creates a virtual replica of a physical exhibition for remote curatorial exploration"],
    ])},
    "art-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Provenance research (museums)", "Traces an artwork's ownership history to inform acquisition decisions"],
    ])},
    "art-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Generative AI as co-author", "Examines authorship questions when AI tools contribute directly to artmaking"],
    ])},
    "art-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["NFT art market", "Uses blockchain to establish verifiable digital ownership and provenance for artworks"],
    ])},
    "art-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Bio-art", "Uses living organisms and biological processes as the artistic medium itself"],
    ])},
    "art-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Spatial audio composition", "Composes sound art that uses three-dimensional positioning as a compositional element"],
    ])},
    "art-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Augmented reality (exhibitions)", "Overlays digital content onto physical exhibition spaces for viewers"],
    ])},
    "art-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Data visualization as aesthetics", "Treats the visual representation of data itself as a form of artistic practice"],
    ])},
    "art-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Kinetic sculpture engineering", "Combines robotics and mechanical design to create moving sculptural artworks"],
    ])},
    "art-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Post-internet aesthetics", "Art that reflects a condition where internet culture is fully embedded in daily life"],
    ])},
    "art-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Social practice art ethics", "Considers the ethical responsibilities of art made collaboratively with communities"],
    ])},
    "art-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Reparative art practice", "Art created specifically to process and repair harm in post-conflict contexts"],
    ])},
    "art-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Tactical media", "Uses accessible media technologies as a strategy for artistic and political activism"],
    ])},
    "art-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Environmental/ecological restoration art", "Art practices that actively participate in restoring degraded ecosystems"],
    ])},
    "art-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Surveillance capitalism (artistic response)", "Art that critiques the commercial extraction and use of personal data"],
    ])},
    "art-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Politics of spectatorship", "Examines the power dynamics between artwork, audience, and participation in interactive art"],
    ])},
    "art-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Craftivism", "Uses traditional craft and textile techniques as a vehicle for political activism"],
    ])},
    "art-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora narratives in art", "Contemporary artwork exploring migration, displacement, and transnational identity"],
    ])},
    "art-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Grant writing (studio artists)", "Strategic approaches to securing funding and fellowships for artistic practice"],
    ])},
    "art-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Artist studio business models", "Approaches to structuring a financially sustainable independent art practice"],
    ])},
    "art-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Fair use (appropriation art)", "Legal doctrine determining when borrowing existing material is permissible in new artworks"],
    ])},
    "art-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Artist residency design", "Structures programs and selection criteria for supporting artists' focused creative time"],
    ])},
    "art-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Rights management (exhibiting artists)", "Manages contracts governing how an artist's work is displayed, sold, and reproduced"],
    ])},
    "art-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Critical portfolio (graduate application)", "Assembles and articulates a body of work for graduate art program admission"],
    ])},
    "art-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Gallery representation model", "Studies how art fairs and galleries structure economic relationships with artists"],
    ])},
    "art-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Public art commissioning", "The formal process, including community review, for creating art in public spaces"],
    ])},
    "art-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Arte Povera legacy", "Traces the continuing influence of using humble materials in contemporary practice"],
    ])},
    "art-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Fluxus event scores", "Text-based instructions used by Fluxus artists as a generative method for performance"],
    ])},
    "art-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Minimalism's phenomenological turn", "Re-examines Minimalism's emphasis on the viewer's bodily experience of the object"],
    ])},
    "art-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Site specificity (Land Art)", "Examines the political dimensions of art created for and tied to a particular location"],
    ])},
    "art-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Détournement", "A Situationist method of subverting existing media by repurposing it against its original intent"],
    ])},
    "art-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Bauhaus pedagogy (contemporary teaching)", "Applies the Bauhaus's integrated art-and-craft teaching model to current studio education"],
    ])},
    "art-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Abstract Expressionism's gendered historiography", "Critiques how art history has historically marginalized women Abstract Expressionists"],
    ])},
    "art-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Dematerialization thesis reassessed", "Re-examines the claim that Conceptual Art fully dissolved the physical art object"],
    ])},
    "art-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Superflat theory", "Murakami's theory linking Japanese contemporary art to flat, historically-rooted visual traditions"],
    ])},
    "art-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Afrofuturism", "A visual and conceptual strategy imagining Black futures through science fiction and technology"],
    ])},
    "art-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Feminist body art", "Uses the artist's own body to interrogate gendered self-representation"],
    ])},
    "art-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Queer theory and portraiture", "Destabilizes fixed identity categories within the tradition of portrait art"],
    ])},
    "art-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Ethnographic display critique", "Postcolonial critique of how museums historically displayed non-Western cultural objects"],
    ])},
    "art-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Intersectionality (curatorial framework)", "Uses overlapping identity categories to shape curatorial and critical approaches"],
    ])},
    "art-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Crip theory / disability aesthetics", "Centers disabled experience and embodiment as a critical lens for contemporary art"],
    ])},
    "art-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Indigenous repatriation debates", "Examines contemporary debates over returning cultural objects to Indigenous communities"],
    ])},
    "art-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Secondary market speculation", "Studies price volatility and speculation affecting emerging artists' resale markets"],
    ])},
    "art-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Art investment funds", "Financial vehicles that treat artworks as an investable, financialized asset class"],
    ])},
    "art-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Auction data analytics", "Uses statistical models to predict artwork prices based on auction house data"],
    ])},
    "art-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Artist estate management", "Oversees an artist's legacy, authentication, and market after their death"],
    ])},
    "art-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Nonprofit art ecosystem", "Studies the grant-funded institutions and economies supporting non-commercial art"],
    ])},
    "art-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Public arts funding models", "Compares how different countries structure government support for the arts"],
    ])},
    "art-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Critique pedagogy", "Structures the studio critique session as a rigorous method of artistic research"],
    ])},
    "art-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["MFA thesis mentorship models", "Compares approaches to advising graduate students through their thesis projects"],
    ])},
    "art-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Studio-based assessment rubrics", "Develops criteria for evaluating graduate research conducted through art-making"],
    ])},
    "art-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cultural art pedagogy", "Examines how art education methods vary and translate across different cultural contexts"],
    ])},
    "art-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Artist-scientist collaboration", "Structures partnerships between artists and researchers within scientific labs"],
    ])},
    "art-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Choreographic thinking (static composition)", "Applies concepts of movement and time from dance to static visual arrangement"],
    ])},
    "art-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Architecture-art hybrid practice", "Blends architectural and artistic methods in large-scale spatial installation"],
    ])},
    "art-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Sonification of scientific data", "Converts data patterns into sound as an artistic and analytical practice"],
    ])},
    "art-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Wearable art technology", "Combines textile engineering with electronics to create interactive wearable art"],
    ])},
    "art-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Culinary arts as contemporary practice", "Treats cooking and food presentation as a legitimate contemporary art medium"],
    ])},
    "art-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Critical mapping (art)", "Uses cartographic techniques critically to reveal hidden power structures through art"],
    ])},
    "art-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Artist books", "A hybrid medium combining print, sculpture, and narrative in book form"],
    ])},
    "art-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Aesthetics of testimony", "Applies trauma theory to how art formally represents witnessed suffering"],
    ])},
    "art-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Ecological materialism (sculpture)", "New sculptural practices centering material's ecological origins and impact"],
    ])},
    "art-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Artistic research ethics boards", "Reviews artistic research involving human subjects for ethical compliance"],
    ])},
    "art-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level artist writing", "Strategies for publishing scholarly writing that accompanies graduate studio research"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"art-m2-l{base_n}"
    worked_key = f"art-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Art lessons.")


if __name__ == "__main__":
    main()
