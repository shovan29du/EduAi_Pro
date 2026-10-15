#!/usr/bin/env python3
"""Depth pass, M1 Art History: fill in real, hand-checked data_table
content for the 119 M1 Art History lessons not covered by the
earlier breadth-first batch. Brings M1 Art History to full 120/120
coverage.

Structure: l1-l100 are unique graduate-level topics spanning the
methodology and historiography of art history, global art movements
from antiquity to the present, non-Western artistic traditions, and
conservation/provenance research; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_art_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Connoisseurship", "Attributing and dating artworks based on trained expert visual judgment"],
    ["Critique", "Argues connoisseurship's subjective judgments lack transparent, verifiable methodology"],
])

CHARTS: dict[str, dict] = {
    "art-history-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Curation", "Selects, organizes, and interprets artworks for public presentation in a museum context"],
    ])},
    "art-history-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Provenance", "The documented history of an artwork's ownership from creation to the present"],
    ])},
    "art-history-m1-l4": {"data_table": table(["Historian", "Method"], [
        ["T.J. Clark", "Reads paintings as embedded in and shaped by their social and political context"],
    ])},
    "art-history-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Decentering the canon", "Challenges the historical dominance of Western art in defining art historical value"],
    ])},
    "art-history-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Historiography of art history", "Studies how the discipline of art history itself has developed and changed over time"],
    ])},
    "art-history-m1-l7": {"data_table": table(["Philosopher", "Claim"], [
        ["Burke", "Distinguished the sublime (awe mixed with terror) from mere beauty"],
    ])},
    "art-history-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Gaze theory", "Analyzes how looking at art encodes gendered power relationships"],
    ])},
    "art-history-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Object biography", "Traces an artwork's changing meaning and use across its lifetime"],
    ])},
    "art-history-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Memorial art", "Examines how visual culture represents and processes collective trauma"],
    ])},
    "art-history-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Repatriation", "Debates the ethics of returning cultural artifacts to their communities of origin"],
    ])},
    "art-history-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Virtual museum", "Uses digital reconstruction to present artworks or sites outside their physical location"],
    ])},
    "art-history-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Archival research method", "Uses primary historical documents to reconstruct an artwork's original context"],
    ])},
    "art-history-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Patronage network", "The system of wealthy sponsors who commissioned and financed early modern art"],
    ])},
    "art-history-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Auction economics", "Studies how bidding dynamics and scarcity set prices in the contemporary art market"],
    ])},
    "art-history-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Biennial", "A large recurring international exhibition that has driven contemporary art's globalization"],
    ])},
    "art-history-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Ecological art", "Contemporary practice that engages environmental themes and materials"],
    ])},
    "art-history-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["New media art", "Art made with or about digital and electronic technologies"],
    ])},
    "art-history-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Art historical thesis", "Constructs an original, evidence-based argument about an artwork or movement"],
    ])},
    "art-history-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Independent research project", "Applies art historical method to an original scholarly investigation"],
    ])},
    "art-history-m1-l21": {"data_table": table(["Historian", "Method"], [
        ["Panofsky", "Reads an artwork's meaning in three levels, from motif to deep cultural symbolism (iconology)"],
    ])},
    "art-history-m1-l22": {"data_table": table(["Historian", "Method"], [
        ["Vasari", "Founded the tradition of art historical biography with his Lives of the Artists"],
    ])},
    "art-history-m1-l23": {"data_table": table(["Historian", "Method"], [
        ["Riegl and Wickhoff", "The Vienna School, which treated all periods of art as equally worthy of formal study"],
    ])},
    "art-history-m1-l24": {"data_table": table(["Historian", "Method"], [
        ["Warburg", "Traced the survival of ancient visual motifs across time using his image atlas"],
    ])},
    "art-history-m1-l25": {"data_table": table(["Method", "Focus"], [
        ["Formalism", "Analyzes an artwork's visual elements in isolation"],
        ["Contextualism", "Interprets an artwork through its social and historical circumstances"],
    ])},
    "art-history-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Byzantine icon theology", "Icons were understood as windows to the sacred, not mere decorative images"],
    ])},
    "art-history-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Islamic geometric ornament", "Uses mathematically precise repeating patterns instead of figural representation"],
    ])},
    "art-history-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Gothic cathedral program", "Architecture and decoration organized to express a unified theological narrative"],
    ])},
    "art-history-m1-l29": {"data_table": table(["Artist", "Feature"], [
        ["Van Eyck", "Embedded hidden symbolic meaning within realistic Northern Renaissance detail"],
    ])},
    "art-history-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Mannerism", "Exaggerated, artificial style emerging from tension with High Renaissance ideals"],
    ])},
    "art-history-m1-l31": {"data_table": table(["Artist", "Technique"], [
        ["Caravaggio", "Used tenebrism, dramatic contrasts of light and dark, to heighten emotional intensity"],
    ])},
    "art-history-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Dutch genre painting", "Depicted everyday domestic scenes reflecting the era's values and ideals"],
    ])},
    "art-history-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Rococo", "An ornate, playful style associated with aristocratic taste in 18th-century Europe"],
    ])},
    "art-history-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Romantic sublime landscape", "Depicted nature's overwhelming power to evoke awe in the viewer"],
    ])},
    "art-history-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Impressionism", "Captured fleeting visual sensations of modern urban life with loose, visible brushwork"],
    ])},
    "art-history-m1-l36": {"data_table": table(["Artist", "Technique"], [
        ["Seurat", "Applied small distinct dots of pure color (Divisionism) to build form through optical mixing"],
    ])},
    "art-history-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Symbolism", "Rejected realism in favor of evoking inner emotional and dreamlike states"],
    ])},
    "art-history-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Art Nouveau / Gesamtkunstwerk", "Aimed to unify architecture, decoration, and design into one total artwork"],
    ])},
    "art-history-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Cubism", "Fractured objects into multiple simultaneous viewpoints within a flattened pictorial space"],
    ])},
    "art-history-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Futurism", "Celebrated speed, technology, and machine dynamism as an artistic aesthetic"],
    ])},
    "art-history-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Dada", "Deliberately absurdist, anti-art response to the irrationality of World War I"],
    ])},
    "art-history-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["The uncanny (Surrealism)", "The unsettling effect of the familiar rendered strange, central to Surrealist imagery"],
    ])},
    "art-history-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Bauhaus pedagogy", "Taught art and craft as unified disciplines aimed at functional design"],
    ])},
    "art-history-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Abstract Expressionism", "Promoted as a symbol of American artistic freedom during the Cold War"],
    ])},
    "art-history-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Pop Art", "Appropriated consumer imagery to critique or celebrate mass commercial culture"],
    ])},
    "art-history-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Minimalism", "Emphasized the viewer's bodily, phenomenological experience of simple geometric objects"],
    ])},
    "art-history-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Arte Povera", "Used humble, everyday materials to challenge institutional art conventions"],
    ])},
    "art-history-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Land art", "Moved artmaking outside the gallery into the natural landscape itself"],
    ])},
    "art-history-m1-l49": {"data_table": table(["Historian", "Claim"], [
        ["Linda Nochlin", "Asked why there have been no 'great women artists', tracing the answer to institutional barriers"],
    ])},
    "art-history-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Harlem Renaissance", "A flourishing of African American art, literature, and culture in the early 20th century"],
    ])},
    "art-history-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Mexican muralism", "Large-scale public murals depicting revolutionary and national historical themes"],
    ])},
    "art-history-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Geometric abstraction (Latin America)", "A postwar movement using pure geometric form, distinct from European models"],
    ])},
    "art-history-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Colonial museum critique", "Examines how colonial collecting practices shaped African art historiography"],
    ])},
    "art-history-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["South Asian miniature painting", "Small-scale, detailed courtly painting traditions across South Asian empires"],
    ])},
    "art-history-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Literati painting theory", "Chinese scholar-artists valued expressive brushwork over technical realism"],
    ])},
    "art-history-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Ukiyo-e", "Japanese woodblock prints that significantly influenced European modernist painters"],
    ])},
    "art-history-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Pre-Columbian iconography", "Interprets symbolic visual systems of the Americas before European contact"],
    ])},
    "art-history-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Egyptian canon of proportion", "A standardized grid system governing the depiction of the human figure"],
    ])},
    "art-history-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Archaic smile", "A stylized facial expression on Greek kouros sculptures signaling life or vitality"],
    ])},
    "art-history-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Catacomb art", "Early Christian symbolic imagery used discreetly under religious persecution"],
    ])},
    "art-history-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Romanesque pilgrimage sculpture", "Church sculpture designed to guide and instruct traveling pilgrims"],
    ])},
    "art-history-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Illuminated manuscript", "A hand-decorated medieval book combining text with painted imagery"],
    ])},
    "art-history-m1-l63": {"data_table": table(["Work", "Debate"], [
        ["Arnolfini Portrait", "Scholars debate whether its objects carry hidden symbolic (disguised) meaning"],
    ])},
    "art-history-m1-l64": {"data_table": table(["Theorist", "Contribution"], [
        ["Brunelleschi / Alberti", "Developed the mathematical rules of linear perspective in Renaissance painting"],
    ])},
    "art-history-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Sistine Chapel program", "A unified theological and artistic scheme designed for its ceiling frescoes"],
    ])},
    "art-history-m1-l66": {"data_table": table(["City", "Emphasis"], [
        ["Venice (colorito)", "Prioritized color and painterly technique"],
        ["Florence (disegno)", "Prioritized drawing and design"],
    ])},
    "art-history-m1-l67": {"data_table": table(["Artist", "Feature"], [
        ["El Greco", "Combined Mannerist elongation with intense Spanish spiritual expression"],
    ])},
    "art-history-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Kunstkammer", "An early modern 'cabinet of curiosities' collecting art alongside natural specimens"],
    ])},
    "art-history-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Chiaroscuro woodcut", "A printmaking technique using multiple blocks to simulate light and shadow"],
    ])},
    "art-history-m1-l70": {"data_table": table(["Artist", "Feature"], [
        ["Rembrandt", "Used repeated self-portraits to explore and construct his own artistic identity"],
    ])},
    "art-history-m1-l71": {"data_table": table(["Artist", "Debate"], [
        ["Vermeer", "Scholars debate whether he used a camera obscura to achieve his precise optical effects"],
    ])},
    "art-history-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Academy / Salon system", "State-sanctioned institutions that controlled artistic training and exhibition in France"],
    ])},
    "art-history-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchy of genres", "Ranked history painting above portraiture, landscape, and still life in prestige"],
    ])},
    "art-history-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Orientalist photography", "Depicted the colonized 'East' through a Western imperial visual lens"],
    ])},
    "art-history-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Pre-Raphaelite Brotherhood", "Revived medieval styles and subjects in reaction to industrial modernity"],
    ])},
    "art-history-m1-l76": {"data_table": table(["Artist", "Feature"], [
        ["Whistler", "Championed art valued for its own aesthetic harmony rather than narrative or moral content"],
    ])},
    "art-history-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Photo-Secession", "A movement that argued photography deserved recognition as a fine art"],
    ])},
    "art-history-m1-l78": {"data_table": table(["Event", "Impact"], [
        ["Armory Show (1913)", "Introduced European modernism to American audiences, sparking controversy and influence"],
    ])},
    "art-history-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Constructivism", "Soviet art aligning abstract, industrial form with revolutionary political purpose"],
    ])},
    "art-history-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Socialist Realism", "State-mandated style depicting idealized workers and communist progress"],
    ])},
    "art-history-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Degenerate Art", "Nazi policy condemning and confiscating modernist art deemed culturally impure"],
    ])},
    "art-history-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Cold War cultural diplomacy", "Abstract art was promoted internationally as a symbol of Western artistic freedom"],
    ])},
    "art-history-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Performance art historiography", "Traces live, ephemeral art from Futurist provocations to Fluxus events"],
    ])},
    "art-history-m1-l84": {"data_table": table(["Artist", "Feature"], [
        ["Nam June Paik", "A pioneer of video art, using television as an artistic medium"],
    ])},
    "art-history-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Institutional critique", "Art that examines and challenges the museum or gallery's own authority"],
    ])},
    "art-history-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Pictures Generation", "Appropriated mass-media imagery to critique representation itself"],
    ])},
    "art-history-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Identity politics in art (1990s)", "Centered race, gender, and sexuality as core subjects of contemporary art"],
    ])},
    "art-history-m1-l88": {"data_table": table(["Theorist", "Claim"], [
        ["Bourriaud", "Argued art can be judged by the social relationships and interactions it generates"],
    ])},
    "art-history-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Documenta", "A major recurring exhibition that has shaped the postwar contemporary art canon"],
    ])},
    "art-history-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Nazi-era looted art restitution", "Traces and returns artworks stolen during the Nazi period to rightful heirs"],
    ])},
    "art-history-m1-l91": {"data_table": table(["Technique", "Reveals"], [
        ["X-radiography / infrared reflectography", "Underdrawings and hidden layers beneath an artwork's visible surface"],
    ])},
    "art-history-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Condition reporting", "Documents an artwork's physical state to guide conservation decisions ethically"],
    ])},
    "art-history-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Attribution science", "Combines traditional connoisseurship with forensic technical analysis"],
    ])},
    "art-history-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Art historical monograph", "A book-length scholarly study focused on a single artist or artwork"],
    ])},
    "art-history-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Exhibition history", "Studies how past exhibitions themselves shaped how art was received and understood"],
    ])},
    "art-history-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Chola bronze sculpture", "South Indian bronzes made using precise iconometric rules for ritual use"],
    ])},
    "art-history-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Aboriginal dot painting", "Encodes ancestral knowledge under culturally governed protocols of display"],
    ])},
    "art-history-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Kano school", "A dominant Japanese painting lineage known for large decorative screen compositions"],
    ])},
    "art-history-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Herat school", "A renowned center of Persian miniature painting known for refined courtly style"],
    ])},
    "art-history-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Andean textile art", "Inca weaving encoded complex iconographic and record-keeping systems"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"art-history-m1-l{base_n}"
    worked_key = f"art-history-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Art History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Art History lessons (completing 120/120).")


if __name__ == "__main__":
    main()
