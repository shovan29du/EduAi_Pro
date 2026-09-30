#!/usr/bin/env python3
"""Depth pass, M1 World History: fill in real, hand-checked data_table
content for the 99 M1 World History lessons not covered by the
earlier breadth-first batch. Brings M1 World History to full 120/120
coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_world_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-history-m1-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Modern world history", "Spans industrialization, nation-building, and global conflict from 1750 onward"],
        ]),
    },
    "world-history-m1-l2": {
        "data_table": table(["Method", "Purpose"], [
            ["Historiography", "Examines how historical interpretation itself has changed over time"],
        ]),
    },
    "world-history-m1-l4": {
        "data_table": table(["Theory", "Detail"], [
            ["State formation theory", "Explains how classical empires consolidated territory and administrative control"],
        ]),
    },
    "world-history-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Global Middle Ages", "Reframes the medieval period as an interconnected era across multiple continents"],
        ]),
    },
    "world-history-m1-l6": {
        "data_table": table(["Era", "Feature"], [
            ["Islamic Golden Age", "Trade networks spread scientific and mathematical knowledge across three continents"],
        ]),
    },
    "world-history-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["African historiography", "Reconstructs African history using oral tradition alongside archaeological evidence"],
        ]),
    },
    "world-history-m1-l8": {
        "data_table": table(["Empire", "Impact"], [
            ["Mongol Empire", "Unified trade routes across Eurasia, facilitating exchange but also plague spread"],
        ]),
    },
    "world-history-m1-l9": {
        "data_table": table(["Era", "Feature"], [
            ["Age of Exploration", "European voyages expanded global trade networks and colonial claims"],
        ]),
    },
    "world-history-m1-l10": {
        "data_table": table(["System", "Detail"], [
            ["Atlantic World slavery", "Forced labor migration structured a transatlantic economic system"],
        ]),
    },
    "world-history-m1-l11": {
        "data_table": table(["Movement", "Feature"], [
            ["Scientific Revolution", "Shifted authority toward empirical, mathematical explanation of nature"],
            ["Enlightenment", "Applied reason to politics, society, and human rights"],
        ]),
    },
    "world-history-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative industrialization", "Industrialization proceeded at different paces and forms across nations"],
        ]),
    },
    "world-history-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Nation-building", "Constructs shared identity and institutions to consolidate a modern state"],
        ]),
    },
    "world-history-m1-l14": {
        "data_table": table(["Event", "Detail"], [
            ["Empire and colonialism", "European powers extended political and economic control over distant territories"],
        ]),
    },
    "world-history-m1-l15": {
        "data_table": table(["Feature", "Detail"], [
            ["World War I", "Introduced industrialized trench warfare and mass casualties on an unprecedented scale"],
        ]),
    },
    "world-history-m1-l16": {
        "data_table": table(["Event", "Outcome"], [
            ["Russian Revolution", "Toppled the tsarist regime and installed the world's first communist state"],
        ]),
    },
    "world-history-m1-l17": {
        "data_table": table(["Feature", "Detail"], [
            ["World War II", "Mobilized entire civilian economies and populations for a truly global war"],
        ]),
    },
    "world-history-m1-l18": {
        "data_table": table(["Process", "Detail"], [
            ["Decolonization", "Former colonies gained independence, often reshaping global political alignment"],
        ]),
    },
    "world-history-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Cold War as global history", "Superpower rivalry shaped conflicts and alliances well beyond Europe"],
        ]),
    },
    "world-history-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Historical research capstone", "Applies original primary-source research to a defined historical question"],
        ]),
    },
    "world-history-m1-l21": {
        "data_table": table(["Factor", "Role"], [
            ["Bronze Age collapse", "Combination of invasion, drought, and trade breakdown ended several civilizations at once"],
        ]),
    },
    "world-history-m1-l22": {
        "data_table": table(["System", "Feature"], [
            ["Roman administration", "Provincial governance and road networks enabled control of a vast empire"],
        ]),
    },
    "world-history-m1-l23": {
        "data_table": table(["Empire", "Legacy"], [
            ["Byzantine Empire", "Preserved Roman law and Greek scholarship for over a thousand years"],
        ]),
    },
    "world-history-m1-l24": {
        "data_table": table(["Route", "Exchange"], [
            ["Silk Road", "Connected distant civilizations through goods, ideas, and disease"],
        ]),
    },
    "world-history-m1-l25": {
        "data_table": table(["Region", "Feature"], [
            ["European feudalism", "Land-based hierarchy of mutual obligation between lord and vassal"],
            ["Japanese feudalism", "Comparable hierarchy centered on samurai loyalty to a daimyo"],
        ]),
    },
    "world-history-m1-l26": {
        "data_table": table(["Event", "Global Context"], [
            ["The Crusades", "Intensified trade and cultural contact between Europe and the Islamic world"],
        ]),
    },
    "world-history-m1-l27": {
        "data_table": table(["Empire", "Feature"], [
            ["Mali Empire", "West African state whose wealth in gold and trade shaped regional power"],
        ]),
    },
    "world-history-m1-l28": {
        "data_table": table(["System", "Detail"], [
            ["Ottoman millet system", "Granted religious communities autonomy over their own legal and communal affairs"],
        ]),
    },
    "world-history-m1-l29": {
        "data_table": table(["Dynasty", "Feature"], [
            ["Ming dynasty", "Restored native Chinese rule and expanded maritime exploration under Zheng He"],
            ["Qing dynasty", "Manchu rulers who expanded China's territorial reach significantly"],
        ]),
    },
    "world-history-m1-l30": {
        "data_table": table(["Empire", "Feature"], [
            ["Mughal Empire", "Centralized South Asian rule blending Persian, Indian, and Islamic administrative traditions"],
        ]),
    },
    "world-history-m1-l31": {
        "data_table": table(["Civilization", "Feature"], [
            ["Maya", "Advanced calendar systems and a hieroglyphic script recorded political history"],
        ]),
    },
    "world-history-m1-l32": {
        "data_table": table(["Empire", "Feature"], [
            ["Aztec", "Tribute-based empire centered on the capital Tenochtitlan"],
            ["Inca", "Road- and administration-based empire spanning the Andes"],
        ]),
    },
    "world-history-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Columbian Exchange", "Transfer of crops, animals, people, and disease between the Old and New Worlds"],
        ]),
    },
    "world-history-m1-l34": {
        "data_table": table(["Empire", "Feature"], [
            ["Spanish colonial empire", "Centralized administration extracting resources like silver from the Americas"],
            ["Portuguese colonial empire", "Focused heavily on coastal trading posts and the sugar/slave economy"],
        ]),
    },
    "world-history-m1-l35": {
        "data_table": table(["Era", "Feature"], [
            ["Dutch Golden Age", "Commercial and maritime dominance built on global trading company networks"],
        ]),
    },
    "world-history-m1-l36": {
        "data_table": table(["System", "Detail"], [
            ["Transatlantic slave trade", "A forced labor system central to the Atlantic economy's plantation output"],
        ]),
    },
    "world-history-m1-l37": {
        "data_table": table(["Movement", "Feature"], [
            ["Abolition movement", "Coordinated activism gradually ended legal slavery across different nations"],
        ]),
    },
    "world-history-m1-l38": {
        "data_table": table(["Event", "Impact"], [
            ["Haitian Revolution", "First successful slave revolt to found an independent state, alarming slaveholding powers"],
        ]),
    },
    "world-history-m1-l39": {
        "data_table": table(["Revolution", "Outcome"], [
            ["French Revolution", "Overthrew the monarchy and spread ideas of popular sovereignty across Europe"],
        ]),
    },
    "world-history-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Napoleonic reorganization", "Reshaped European legal and administrative systems under French dominance"],
        ]),
    },
    "world-history-m1-l41": {
        "data_table": table(["System", "Detail"], [
            ["Congress of Vienna", "Great powers coordinated diplomacy after 1815 to preserve a European balance of power"],
        ]),
    },
    "world-history-m1-l42": {
        "data_table": table(["Event", "Detail"], [
            ["Opium Wars", "Forced concessions eroded Chinese sovereignty over trade and territory"],
        ]),
    },
    "world-history-m1-l43": {
        "data_table": table(["Event", "Detail"], [
            ["Taiping Rebellion", "One of history's deadliest civil conflicts, driven by religious and social upheaval"],
        ]),
    },
    "world-history-m1-l44": {
        "data_table": table(["Policy", "Effect"], [
            ["Meiji Restoration", "State-led modernization rapidly transformed Japan into an industrial power"],
        ]),
    },
    "world-history-m1-l45": {
        "data_table": table(["Event", "Detail"], [
            ["Scramble for Africa", "European powers partitioned the continent with little regard for existing societies"],
        ]),
    },
    "world-history-m1-l46": {
        "data_table": table(["System", "Detail"], [
            ["British Raj administration", "Combined direct and indirect rule to govern colonial India"],
        ]),
    },
    "world-history-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Settler colonialism", "Colonizers aimed to permanently replace indigenous populations on the land"],
        ]),
    },
    "world-history-m1-l48": {
        "data_table": table(["Event", "Detail"], [
            ["Armenian genocide", "Mass killing and deportation during World War I under Ottoman rule"],
        ]),
    },
    "world-history-m1-l49": {
        "data_table": table(["Event", "Detail"], [
            ["Balkan Wars", "Regional conflicts that heightened tensions leading directly into World War I"],
        ]),
    },
    "world-history-m1-l50": {
        "data_table": table(["Provision", "Consequence"], [
            ["Treaty of Versailles", "War-guilt and reparations clauses fueled German resentment and instability"],
        ]),
    },
    "world-history-m1-l51": {
        "data_table": table(["Event", "Detail"], [
            ["Interwar economic crisis", "The Great Depression destabilized economies and fueled political extremism"],
        ]),
    },
    "world-history-m1-l52": {
        "data_table": table(["Event", "Detail"], [
            ["Spanish Civil War", "Foreign intervention made it a proxy conflict foreshadowing World War II"],
        ]),
    },
    "world-history-m1-l53": {
        "data_table": table(["Field", "Focus"], [
            ["Holocaust historiography", "Examines evolving methods and debates in documenting and interpreting genocide"],
        ]),
    },
    "world-history-m1-l54": {
        "data_table": table(["Theater", "Outcome"], [
            ["Pacific War", "Ended with the atomic bombings of Hiroshima and Nagasaki and Japan's surrender"],
        ]),
    },
    "world-history-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Nuclear diplomacy", "Atomic weapons reshaped great-power strategy and deterrence after 1945"],
        ]),
    },
    "world-history-m1-l56": {
        "data_table": table(["Regime", "Feature"], [
            ["Comparative fascism", "Interwar fascist movements shared authoritarianism but varied by national context"],
        ]),
    },
    "world-history-m1-l57": {
        "data_table": table(["Event", "Outcome"], [
            ["Chinese Civil War", "Ended in Communist victory and the founding of the People's Republic of China"],
        ]),
    },
    "world-history-m1-l58": {
        "data_table": table(["Conflict", "Detail"], [
            ["Korean War", "A Cold War proxy conflict that entrenched the peninsula's division"],
        ]),
    },
    "world-history-m1-l59": {
        "data_table": table(["Conflict", "Detail"], [
            ["Vietnam War", "A prolonged Cold War conflict with major global political repercussions"],
        ]),
    },
    "world-history-m1-l60": {
        "data_table": table(["Movement", "Goal"], [
            ["Non-Aligned Movement", "States sought to avoid formal alignment with either Cold War bloc"],
        ]),
    },
    "world-history-m1-l61": {
        "data_table": table(["Event", "Detail"], [
            ["Cuban Revolution", "Established a communist government that shaped Latin American Cold War politics"],
        ]),
    },
    "world-history-m1-l62": {
        "data_table": table(["Movement", "Detail"], [
            ["African independence movements", "Achieved decolonization through varied paths, from negotiation to armed struggle"],
        ]),
    },
    "world-history-m1-l63": {
        "data_table": table(["Event", "Detail"], [
            ["Indian Partition", "Mass displacement and violence accompanied the creation of India and Pakistan"],
        ]),
    },
    "world-history-m1-l64": {
        "data_table": table(["Conflict", "Origin"], [
            ["Arab-Israeli conflict", "Rooted in competing national claims following the end of British Mandate rule"],
        ]),
    },
    "world-history-m1-l65": {
        "data_table": table(["Event", "Detail"], [
            ["Iranian Revolution", "Overthrew the monarchy and established an Islamic republic in 1979"],
        ]),
    },
    "world-history-m1-l66": {
        "data_table": table(["Event", "Significance"], [
            ["Fall of the Berlin Wall", "Symbolized the collapse of Soviet-aligned governments across Eastern Europe"],
        ]),
    },
    "world-history-m1-l67": {
        "data_table": table(["Event", "Detail"], [
            ["Soviet dissolution", "Ended the Cold War bipolar order and produced fifteen new independent states"],
        ]),
    },
    "world-history-m1-l68": {
        "data_table": table(["Conflict", "Detail"], [
            ["Yugoslav Wars", "Ethnic conflict accompanied the breakup of a multiethnic federal state"],
        ]),
    },
    "world-history-m1-l69": {
        "data_table": table(["Event", "Detail"], [
            ["Rwandan genocide", "Mass killing in 1994 rooted in colonial-era ethnic categorization"],
        ]),
    },
    "world-history-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Globalization discontents", "Economic integration produced uneven benefits, fueling political backlash"],
        ]),
    },
    "world-history-m1-l71": {
        "data_table": table(["Pattern", "Driver"], [
            ["Global migration", "Shaped by economic opportunity, conflict, and changing border policy over time"],
        ]),
    },
    "world-history-m1-l72": {
        "data_table": table(["Field", "Focus"], [
            ["Comparative genocide studies", "Examines shared and distinct causal patterns across mass atrocity events"],
        ]),
    },
    "world-history-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["International human rights law", "Developed gradually through treaties and institutions after World War II"],
        ]),
    },
    "world-history-m1-l74": {
        "data_table": table(["Institution", "Purpose"], [
            ["United Nations", "Created to maintain international peace and coordinate postwar global governance"],
        ]),
    },
    "world-history-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Anthropocene", "A proposed geological epoch defined by significant human impact on Earth systems"],
        ]),
    },
    "world-history-m1-l76": {
        "data_table": table(["Event", "Detail"], [
            ["Global pandemic history", "Recurring disease outbreaks have reshaped populations, economies, and policy"],
        ]),
    },
    "world-history-m1-l77": {
        "data_table": table(["Region", "Feature"], [
            ["Comparative industrialization", "Britain, Germany, Japan, and others industrialized on distinct timelines and models"],
        ]),
    },
    "world-history-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Global capitalism history", "Traces how market economies expanded and integrated across centuries"],
        ]),
    },
    "world-history-m1-l79": {
        "data_table": table(["Movement", "Detail"], [
            ["Labor movement", "Organized workers across countries won rights through strikes and legislation"],
        ]),
    },
    "world-history-m1-l80": {
        "data_table": table(["Movement", "Detail"], [
            ["Women's suffrage movement", "Achieved voting rights through sustained activism at different times worldwide"],
        ]),
    },
    "world-history-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative constitutional history", "Examines how founding legal documents shaped different political systems"],
        ]),
    },
    "world-history-m1-l82": {
        "data_table": table(["Technology", "Impact"], [
            ["Telegraph/internet", "Communication technologies successively compressed global information exchange"],
        ]),
    },
    "world-history-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Naval power projection", "Maritime strength enabled empires to secure and expand overseas influence"],
        ]),
    },
    "world-history-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Cartography and territorial claims", "Maps have historically served as tools of both knowledge and political assertion"],
        ]),
    },
    "world-history-m1-l85": {
        "data_table": table(["Movement", "Feature"], [
            ["The Reformation", "Fractured religious unity in Europe and reshaped political alliances along confessional lines"],
        ]),
    },
    "world-history-m1-l86": {
        "data_table": table(["Event", "Detail"], [
            ["Global famine history", "Recurring famines have reflected both natural causes and policy failure"],
        ]),
    },
    "world-history-m1-l87": {
        "data_table": table(["Event", "Detail"], [
            ["Berlin Conference", "Formalized European rules for partitioning African territory in 1884-85"],
        ]),
    },
    "world-history-m1-l88": {
        "data_table": table(["Theory", "Detail"], [
            ["Comparative revolutionary theory", "Examines shared structural conditions across successful and failed revolutions"],
        ]),
    },
    "world-history-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Intelligence services history", "Espionage institutions expanded significantly through the twentieth century's conflicts"],
        ]),
    },
    "world-history-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Global refugee crisis", "Conflict and persecution have repeatedly produced large-scale forced displacement"],
        ]),
    },
    "world-history-m1-l91": {
        "data_table": table(["Event", "Detail"], [
            ["Space Race", "Cold War rivalry extended into a technological and symbolic competition beyond Earth"],
        ]),
    },
    "world-history-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Postcolonial economic development", "Newly independent states pursued varied strategies for economic self-determination"],
        ]),
    },
    "world-history-m1-l93": {
        "data_table": table(["Method", "Purpose"], [
            ["Oral history methodology", "Records firsthand testimony to preserve perspectives absent from official archives"],
        ]),
    },
    "world-history-m1-l94": {
        "data_table": table(["Method", "Purpose"], [
            ["Digital humanities in history", "Applies computational tools to analyze and visualize large historical datasets"],
        ]),
    },
    "world-history-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative memorial studies", "Examines how societies choose to commemorate contested historical events"],
        ]),
    },
    "world-history-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Global trade agreement history", "Traces the postwar development of international trade governance"],
        ]),
    },
    "world-history-m1-l97": {
        "data_table": table(["Event", "Detail"], [
            ["Suez Crisis", "Marked a turning point in the decline of British and French imperial influence"],
        ]),
    },
    "world-history-m1-l98": {
        "data_table": table(["Mechanism", "Purpose"], [
            ["Truth and reconciliation commission", "Seeks accountability and healing after periods of mass political violence"],
        ]),
    },
    "world-history-m1-l99": {
        "data_table": table(["Movement", "Detail"], [
            ["Global environmental movement", "Grew from local activism into transnational advocacy for policy change"],
        ]),
    },
    "world-history-m1-l100": {
        "data_table": table(["Method", "Purpose"], [
            ["Microhistory", "Uses a small-scale case study to illuminate broader historical patterns"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Civilization", "River"], [
        ["Mesopotamia", "Tigris and Euphrates"],
        ["Egypt", "Nile"],
        ["Indus Valley", "Indus"],
        ["Ancient China (Shang)", "Yellow River (Huang He)"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"world-history-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"world-history-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"world-history-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 World History lessons (completing 120/120).")


if __name__ == "__main__":
    main()
