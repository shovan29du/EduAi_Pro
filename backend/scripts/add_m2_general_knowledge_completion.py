#!/usr/bin/env python3
"""Depth pass, M2 General Knowledge: fill in real, hand-checked
data_table content for the M2 General Knowledge lessons not covered
by the earlier breadth-first batch. Brings M2 General Knowledge to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
international relations and law, science/history landmark events,
global governance institutions, and interdisciplinary knowledge
(philosophy, game theory, demography); l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Treaty of Westphalia (1648)", "Ended the Thirty Years' War and established the modern concept of state sovereignty"],
    ["State sovereignty", "The principle that states have supreme authority within their own territory"],
])

CHARTS: dict[str, dict] = {
    "general-knowledge-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Interdisciplinary general studies research", "Systematic scholarly methods for integrating knowledge across multiple fields"],
    ])},
    "general-knowledge-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Current affairs research fundamentals", "Rigorous methods for critically analyzing contemporary events and their context"],
    ])},
    "general-knowledge-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Bretton Woods Conference", "Established the postwar international monetary system, IMF, and World Bank in 1944"],
    ])},
    "general-knowledge-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Non-Aligned Movement", "A coalition of states declining formal alignment with either Cold War superpower bloc"],
    ])},
    "general-knowledge-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Congress of Vienna", "Redrew Europe's borders after Napoleon and established a balance-of-power diplomatic system"],
    ])},
    "general-knowledge-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Sykes-Picot Agreement", "A secret WWI-era pact that shaped the modern borders of the Middle East"],
    ])},
    "general-knowledge-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["International Court of Justice", "The UN's principal judicial body, resolving legal disputes between states"],
    ])},
    "general-knowledge-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Nuremberg Trials", "Post-WWII tribunals that established key precedents in international criminal law"],
    ])},
    "general-knowledge-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Universal Declaration of Human Rights", "A 1948 UN document establishing a common global standard for fundamental rights"],
    ])},
    "general-knowledge-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Marshall Plan", "US aid that helped rebuild postwar European economies"],
    ])},
    "general-knowledge-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Non-Proliferation Treaty", "An international agreement limiting the spread of nuclear weapons"],
    ])},
    "general-knowledge-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Montreal Protocol", "A highly successful international treaty that phased out ozone-depleting substances"],
    ])},
    "general-knowledge-m2-l14": {"data_table": table(["Agreement", "Feature"], [
        ["Kyoto Protocol", "Set binding emission targets for developed countries only"],
        ["Paris Agreement", "Uses nationally determined contributions from all countries"],
    ])},
    "general-knowledge-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["WTO dispute settlement", "A formal mechanism for resolving trade disagreements between member countries"],
    ])},
    "general-knowledge-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Bologna Process", "Harmonizes higher education standards and degree structures across European countries"],
    ])},
    "general-knowledge-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Human Genome Project", "Mapped the complete human genetic sequence, raising major scientific and ethical questions"],
    ])},
    "general-knowledge-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["CRISPR", "A precise gene-editing technology that has sparked significant ethical debate over its applications"],
    ])},
    "general-knowledge-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Higgs boson discovery", "Confirmed at the Large Hadron Collider in 2012, validating a key part of the Standard Model"],
    ])},
    "general-knowledge-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Voyager Golden Record", "A phonograph record attached to the Voyager probes intended as a message for extraterrestrial life"],
    ])},
    "general-knowledge-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Antikythera mechanism", "An ancient Greek device now understood as a remarkably early analog astronomical computer"],
    ])},
    "general-knowledge-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Rosetta Stone", "A trilingual inscription that enabled the decipherment of Egyptian hieroglyphs"],
    ])},
    "general-knowledge-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Dead Sea Scrolls", "Ancient manuscripts of major significance for biblical and religious textual scholarship"],
    ])},
    "general-knowledge-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Library of Alexandria", "An ancient center of scholarship whose destruction is explained by several competing theories"],
    ])},
    "general-knowledge-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Silk Road", "A network of trade routes enabling extensive premodern cultural and economic exchange across Eurasia"],
    ])},
    "general-knowledge-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Columbian Exchange", "The transfer of plants, animals, and diseases between the Old and New Worlds after 1492"],
    ])},
    "general-knowledge-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Bronze Age Collapse", "A poorly understood societal collapse around 1200 BCE with multiple competing explanations"],
    ])},
    "general-knowledge-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Print Revolution", "Gutenberg's movable type dramatically accelerated the spread of information across Europe"],
    ])},
    "general-knowledge-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Scientific Revolution", "A period of major paradigm shifts in how early modern Europeans understood the natural world"],
    ])},
    "general-knowledge-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Enlightenment", "A movement promoting reason and secular political philosophy over traditional authority"],
    ])},
    "general-knowledge-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Industrial Revolution diffusion", "Traces how industrialization spread unevenly across different world regions"],
    ])},
    "general-knowledge-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Berlin Conference", "Formalized the European colonial partition of Africa in 1884-85"],
    ])},
    "general-knowledge-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Bandung Conference", "A 1955 meeting of newly independent Asian and African states promoting solidarity"],
    ])},
    "general-knowledge-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Apollo Program", "The US space program that landed humans on the moon, shaped by Cold War politics"],
    ])},
    "general-knowledge-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["International Space Station", "Governed by a multinational agreement coordinating operations among partner nations"],
    ])},
    "general-knowledge-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Plate tectonic theory", "Explains Earth's surface as divided into moving plates, developed from earlier continental drift ideas"],
    ])},
    "general-knowledge-m2-l37": {"data_table": table(["Scientist", "Claim"], [
        ["Alfred Wegener", "Proposed continental drift, initially rejected before plate tectonics validated the core idea"],
    ])},
    "general-knowledge-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Thermohaline circulation", "A global ocean current system driven by differences in water temperature and salinity"],
    ])},
    "general-knowledge-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Anthropocene", "A proposed geological epoch defined by human activity's dominant effect on Earth's systems"],
    ])},
    "general-knowledge-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Biodiversity hotspot", "A region with exceptional species richness prioritized for conservation efforts"],
    ])},
    "general-knowledge-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["IUCN Red List", "A globally recognized system for assessing species' extinction risk"],
    ])},
    "general-knowledge-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Green Revolution", "High-yield crop varieties dramatically raised global agricultural output in the mid-20th century"],
    ])},
    "general-knowledge-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["WHO pandemic preparedness", "Frameworks the World Health Organization uses to prepare for global disease outbreaks"],
    ])},
    "general-knowledge-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Smallpox eradication", "The only human disease successfully eradicated globally, achieved through vaccination campaigns"],
    ])},
    "general-knowledge-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Herd immunity threshold", "The vaccination coverage level needed to prevent sustained disease spread in a population"],
    ])},
    "general-knowledge-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Demographic transition model", "Describes how birth and death rates shift as a country develops economically"],
    ])},
    "general-knowledge-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Global fertility decline", "Traces the causes and regional patterns of falling birth rates worldwide"],
    ])},
    "general-knowledge-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Gini coefficient", "A statistical measure quantifying income inequality within a population"],
    ])},
    "general-knowledge-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Purchasing power parity", "Adjusts currency comparisons for differences in local price levels across countries"],
    ])},
    "general-knowledge-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Human Development Index", "A composite measure combining income, health, and education to assess development"],
    ])},
    "general-knowledge-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Sovereign wealth fund", "A state-owned investment fund managing national savings, often from resource revenue"],
    ])},
    "general-knowledge-m2-l52": {"data_table": table(["Institution", "Mandate"], [
        ["IMF", "Promotes global monetary cooperation and financial stability"],
        ["World Bank", "Provides financing for development projects"],
    ])},
    "general-knowledge-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Central bank independence", "The degree to which monetary policy is insulated from direct political control"],
    ])},
    "general-knowledge-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Eurozone", "A monetary union sharing a single currency without full fiscal union, exposed by crisis response challenges"],
    ])},
    "general-knowledge-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["BRICS", "An economic and geopolitical coalition of Brazil, Russia, India, China, and South Africa"],
    ])},
    "general-knowledge-m2-l56": {"data_table": table(["Group", "Feature"], [
        ["G7", "Seven major advanced economies"],
        ["G20", "A broader group including major emerging economies"],
    ])},
    "general-knowledge-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Arctic Council", "An intergovernmental forum coordinating policy among Arctic nations"],
    ])},
    "general-knowledge-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Antarctic Treaty System", "Suspends territorial claims and dedicates Antarctica to peaceful scientific cooperation"],
    ])},
    "general-knowledge-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["UNCLOS", "The Law of the Sea Convention establishing rules for maritime boundaries and resource rights"],
    ])},
    "general-knowledge-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["ICANN", "Coordinates the global internet's domain name system and address allocation"],
    ])},
    "general-knowledge-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Undersea cable network", "The physical infrastructure carrying the vast majority of international internet data"],
    ])},
    "general-knowledge-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Cultural heritage repatriation", "Debates over returning cultural artifacts to their communities or countries of origin"],
    ])},
    "general-knowledge-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Elgin Marbles dispute", "An ongoing debate between Greece and the British Museum over ownership of ancient sculptures"],
    ])},
    "general-knowledge-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["World Expo history", "International exhibitions that historically showcased new technology and national achievement"],
    ])},
    "general-knowledge-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Nobel Prize selection", "A process managed by Swedish and Norwegian institutions, with a history of notable controversies"],
    ])},
    "general-knowledge-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Olympic Movement", "A global sporting institution with a complex governance and political history"],
    ])},
    "general-knowledge-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["FIFA World Cup", "The world's most-watched sporting event, often serving as a vehicle for national diplomacy"],
    ])},
    "general-knowledge-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["UNESCO Intangible Cultural Heritage", "A designation protecting traditions, practices, and skills rather than physical sites"],
    ])},
    "general-knowledge-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["World religions demographics", "Comparative statistical distribution of the world's major religious traditions"],
    ])},
    "general-knowledge-m2-l70": {"data_table": table(["Type", "Feature"], [
        ["Solar calendar", "Based on Earth's orbit around the sun"],
        ["Lunar calendar", "Based on the moon's phases"],
        ["Lunisolar calendar", "Combines both solar and lunar cycles"],
    ])},
    "general-knowledge-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["International Date Line", "An imaginary line established to manage the change of calendar date across time zones"],
    ])},
    "general-knowledge-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Metric system standardization", "Traces the global history of adopting a unified system of measurement"],
    ])},
    "general-knowledge-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["SI redefinition", "The International System of Units now defines base units via fixed physical constants"],
    ])},
    "general-knowledge-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Greenwich Meridian Conference", "Established Greenwich as the global prime meridian and standard for world time"],
    ])},
    "general-knowledge-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Periodic table (Mendeleev)", "Mendeleev's table successfully predicted the properties of then-undiscovered elements"],
    ])},
    "general-knowledge-m2-l76": {"data_table": table(["Tradition", "Feature"], [
        ["Continental philosophy", "Emphasizes historical, interpretive approaches"],
        ["Analytic philosophy", "Emphasizes logical and linguistic precision"],
    ])},
    "general-knowledge-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Trolley problem", "A classic thought experiment probing the ethics of action versus inaction in causing harm"],
    ])},
    "general-knowledge-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Prisoner's dilemma", "A game theory scenario showing rational individual choices can produce a worse collective outcome"],
    ])},
    "general-knowledge-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Tragedy of the commons", "Individuals overusing a shared resource can deplete it, harming the whole group"],
    ])},
    "general-knowledge-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Nudge theory", "Uses subtle choice-architecture changes to influence behavior without restricting options"],
    ])},
    "general-knowledge-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Butterfly effect", "In chaos theory, small initial changes can lead to vastly different outcomes over time"],
    ])},
    "general-knowledge-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Occam's Razor", "The principle that the simplest explanation consistent with the evidence is usually preferred"],
    ])},
    "general-knowledge-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Fermi Paradox", "Questions why, given the universe's scale, no evidence of extraterrestrial civilizations has been found"],
    ])},
    "general-knowledge-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Drake Equation", "Estimates the number of potentially communicative civilizations in the galaxy"],
    ])},
    "general-knowledge-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Comparative world mythology", "Structural analysis of recurring themes and patterns across different mythological traditions"],
    ])},
    "general-knowledge-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["UNHCR mandate", "The UN agency responsible for protecting and supporting refugees worldwide"],
    ])},
    "general-knowledge-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["World population milestones", "Tracks major thresholds and projection methods for global population growth"],
    ])},
    "general-knowledge-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Global literacy trends", "Examines improvements and measurement challenges in tracking worldwide literacy rates"],
    ])},
    "general-knowledge-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Map projection trade-offs", "Every flat map projection distorts some combination of area, shape, distance, or direction"],
    ])},
    "general-knowledge-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["UNESCO Biosphere Reserves", "Sites balancing conservation goals with sustainable human development"],
    ])},
    "general-knowledge-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["World Bank poverty line", "The methodology used to define a global threshold for extreme poverty"],
    ])},
    "general-knowledge-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Global supply chain vulnerability", "Case studies of how disruptions expose fragility in interconnected supply chains"],
    ])},
    "general-knowledge-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Semiconductor geopolitics", "The chip industry's concentrated supply chain has become a major strategic issue"],
    ])},
    "general-knowledge-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Rare earth elements", "Critical materials whose concentrated global production carries strategic significance"],
    ])},
    "general-knowledge-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Standardized time zones history", "Traces the development of the global time zone system from local solar time"],
    ])},
    "general-knowledge-m2-l96": {"data_table": table(["System", "Feature"], [
        ["Federalism", "Divides power between central and regional governments"],
        ["Unitary state", "Concentrates power in a central government"],
    ])},
    "general-knowledge-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Responsibility to Protect", "A doctrine holding states responsible for protecting populations from mass atrocities"],
    ])},
    "general-knowledge-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Global press freedom indices", "Measure and compare journalistic freedom across countries, with debated methodology"],
    ])},
    "general-knowledge-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Doctoral thesis seminar", "Presents and defends original interdisciplinary research contributing new knowledge"],
    ])},
    "general-knowledge-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Voynich Manuscript", "A mysterious undeciphered medieval manuscript that remains a subject of scholarly debate"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"general-knowledge-m2-l{base_n}"
    worked_key = f"general-knowledge-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 General Knowledge lessons.")


if __name__ == "__main__":
    main()
