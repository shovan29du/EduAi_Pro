#!/usr/bin/env python3
"""Depth pass, M2 World History: fill in real, hand-checked
data_table content for the M2 World History lessons not covered by
the earlier breadth-first batch. Brings M2 World History to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
historiographical schools and methods, global/comparative history,
and the twentieth-century global political-economic order; l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_world_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Longue durée", "Braudel's concept of slow-moving structural history unfolding over centuries"],
    ["Annales School", "A French historiographical movement emphasizing social and economic structures over events"],
])

CHARTS: dict[str, dict] = {
    "world-history-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Historiography", "The study of how history has been written and interpreted by historians over time"],
    ])},
    "world-history-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Ancient/classical civilization research", "Systematic scholarly study of early complex societies using textual and archaeological evidence"],
    ])},
    "world-history-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["World-systems analysis", "Wallerstein's framework analyzing global history through core-periphery economic structures"],
    ])},
    "world-history-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["California School", "Historians who argue East and West had comparable development until a 'Great Divergence' around 1800"],
    ])},
    "world-history-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Frontier thesis (comparative)", "Compares how expanding frontiers shaped identity and institutions across different empires"],
    ])},
    "world-history-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Subaltern studies", "Historiography recovering the perspectives of marginalized groups excluded from elite colonial narratives"],
    ])},
    "world-history-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Eurocentric periodization critique", "Challenges historical eras (e.g. 'Middle Ages') defined by European chronology as a global default"],
    ])},
    "world-history-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Columbian Exchange", "The transfer of plants, animals, and diseases between the Old and New Worlds after 1492"],
    ])},
    "world-history-m2-l10": {"data_table": table(["Pandemic", "Era"], [
        ["Justinianic Plague", "6th century CE"],
        ["Black Death", "14th century CE"],
        ["Third Pandemic", "19th-20th century CE"],
    ])},
    "world-history-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Anthropocene", "A proposed geological epoch defined by human activity's dominant effect on Earth's systems"],
    ])},
    "world-history-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Big History", "Synthesizes history across cosmic, geological, biological, and human timescales"],
    ])},
    "world-history-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Comparative genocide studies", "Analyzes causes and patterns across different genocides to identify common warning signs"],
    ])},
    "world-history-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Atlantic slave trade quantification", "Historians debate precise numbers of enslaved Africans transported using shipping records"],
    ])},
    "world-history-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Global microhistory", "Traces a small-scale local story to reveal broader global connections and processes"],
    ])},
    "world-history-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Connected histories", "Examines interlinked developments across early modern Eurasian societies rather than isolated national stories"],
    ])},
    "world-history-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Military revolution thesis", "Argues early modern changes in warfare technology and tactics reshaped European state power"],
    ])},
    "world-history-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Comparative absolutism", "Compares how centralized royal power developed differently in France, Russia, and the Ottoman Empire"],
    ])},
    "world-history-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Silk Road framework", "Views premodern Eurasia through the lens of long-distance trade and cultural exchange routes"],
    ])},
    "world-history-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Indian Ocean world", "Studies the interconnected trade and cultural networks spanning the Indian Ocean basin"],
    ])},
    "world-history-m2-l21": {"data_table": table(["Empire", "Comparison"], [
        ["Rome", "Fell to internal decline and external pressure in the west, c. 476 CE"],
        ["Han China", "Collapsed amid internal rebellion and fragmentation, c. 220 CE"],
    ])},
    "world-history-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Global bullion flows", "Traces how silver and gold moved across continents, linking early modern economies"],
    ])},
    "world-history-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Mongol world empire", "The largest contiguous land empire in history, which reshaped Eurasian trade and communication"],
    ])},
    "world-history-m2-l24": {"data_table": table(["System", "Feature"], [
        ["Serfdom", "Bound peasants to land under a lord, mainly in Europe"],
        ["Slavery", "Full legal ownership of enslaved persons as property"],
    ])},
    "world-history-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Printing revolution diffusion", "Traces how movable-type printing spread and transformed literacy across the world"],
    ])},
    "world-history-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Scientific Revolution's global context", "Situates early modern European science within broader global knowledge exchange"],
    ])},
    "world-history-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Enlightenment beyond Europe", "Examines parallel intellectual reform movements outside the traditional European Enlightenment narrative"],
    ])},
    "world-history-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Age of Revolutions", "A global wave of political upheaval spanning roughly 1775-1848 across multiple continents"],
    ])},
    "world-history-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Nation-building (19th century)", "Compares how new nation-states constructed shared identity and institutions"],
    ])},
    "world-history-m2-l30": {"data_table": table(["Type", "Feature"], [
        ["Formal empire", "Direct territorial rule and administration"],
        ["Informal empire", "Economic and political dominance without formal annexation"],
    ])},
    "world-history-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Global labor history", "Traces the formation of a worldwide industrial working class across national contexts"],
    ])},
    "world-history-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["19th-century migration systems", "Compares large-scale movements of people driven by industrialization and colonization"],
    ])},
    "world-history-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Commodity frontier", "A region newly incorporated into global markets to supply a specific raw material"],
    ])},
    "world-history-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Scramble for Africa", "The rapid European colonization and partition of Africa in the late 19th century"],
    ])},
    "world-history-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Settler colonialism", "A form of colonization where settlers aim to permanently replace indigenous populations"],
    ])},
    "world-history-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Total war", "20th-century warfare mobilizing an entire society's economy and population for the war effort"],
    ])},
    "world-history-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Origins of WWI historiography", "Historians debate the relative weight of alliances, militarism, and diplomacy in causing the war"],
    ])},
    "world-history-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Interwar fascism (comparative)", "Compares the rise and ideology of fascist movements across different interwar nations"],
    ])},
    "world-history-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Decolonization movements", "The global wave of former colonies achieving independence, mainly mid-20th century"],
    ])},
    "world-history-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Cold War as global conflict", "Frames the Cold War as a worldwide struggle extending well beyond the US-Soviet rivalry"],
    ])},
    "world-history-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Non-Aligned Movement", "A coalition of states declining formal alignment with either Cold War superpower bloc"],
    ])},
    "world-history-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Modernization theory", "A postwar development framework proposing all societies follow a similar path toward industrialization"],
    ])},
    "world-history-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Global 1968", "A wave of interconnected protest movements that erupted across many countries in 1968"],
    ])},
    "world-history-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Authoritarian transitions", "Compares how late 20th-century regimes shifted between authoritarian and democratic rule"],
    ])},
    "world-history-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Neoliberal restructuring", "Late 20th-century policy shift toward deregulation, privatization, and free markets globally"],
    ])},
    "world-history-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Globalization's long-term origins", "Debates whether globalization is a recent phenomenon or has much deeper historical roots"],
    ])},
    "world-history-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Refugee regimes (20th century)", "Compares how different eras and institutions managed mass displacement"],
    ])},
    "world-history-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Human rights discourse", "Traces the historical development of international human rights as a global political language"],
    ])},
    "world-history-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Transitional justice", "Studies how societies address mass atrocity after conflict, e.g. tribunals and truth commissions"],
    ])},
    "world-history-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Green Revolution's global impact", "Compares how high-yield agriculture transformed food production differently across regions"],
    ])},
    "world-history-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Disease eradication campaigns", "Traces global public health efforts like the smallpox eradication program"],
    ])},
    "world-history-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Global environmental governance origins", "Traces the emergence of international institutions for managing environmental issues"],
    ])},
    "world-history-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Global financial system evolution", "Compares how international monetary arrangements have changed over the 20th century"],
    ])},
    "world-history-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["IT revolution (global history)", "Traces how computing and networking technology reshaped global economy and society"],
    ])},
    "world-history-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Global urbanization (20th century)", "Compares patterns of rapid city growth across different world regions"],
    ])},
    "world-history-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["20th-century famine (comparative)", "Compares causes of major famines, distinguishing natural from policy-driven factors"],
    ])},
    "world-history-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["International organizations", "Traces the institutional growth of bodies like the UN across the 20th century"],
    ])},
    "world-history-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Bretton Woods order", "The post-WWII international monetary system establishing fixed exchange rates and the IMF/World Bank"],
    ])},
    "world-history-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Currency crises (20th century)", "Compares episodes of sudden currency collapse across different economies"],
    ])},
    "world-history-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sport as nationalism/diplomacy", "Examines how international sporting events have served political and diplomatic purposes"],
    ])},
    "world-history-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Global consumer culture spread", "Traces how mass consumption patterns spread internationally through the 20th century"],
    ])},
    "world-history-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Postcolonial state formation", "Compares how newly independent states built governing institutions after colonial rule"],
    ])},
    "world-history-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora/transnational communities", "Traces how dispersed communities maintain identity and connections across borders"],
    ])},
    "world-history-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Global religious revival", "Compares 20th-century movements of renewed religious observance across different faiths and regions"],
    ])},
    "world-history-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Global oil economy", "Traces how petroleum reshaped 20th-century geopolitics and economic power"],
    ])},
    "world-history-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Nuclear proliferation/arms control", "Traces the spread of nuclear weapons and international efforts to limit them"],
    ])},
    "world-history-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Space exploration as geopolitics", "Frames the Space Race as an extension of Cold War political competition"],
    ])},
    "world-history-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Global feminist movements", "Compares how women's rights movements developed differently across world regions"],
    ])},
    "world-history-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Indigenous rights movements", "Traces the global growth of Indigenous political mobilization for land and sovereignty"],
    ])},
    "world-history-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Trade union internationalism", "Traces efforts to coordinate labor movements across national borders"],
    ])},
    "world-history-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["20th-century land reform", "Compares how different states redistributed agricultural land in the 20th century"],
    ])},
    "world-history-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Famine relief and humanitarian intervention", "Traces the development of international disaster response mechanisms"],
    ])},
    "world-history-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Cold War proxy conflicts", "Wars fought by allied states or groups on behalf of the US and Soviet superpowers"],
    ])},
    "world-history-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Currency board systems", "Compares monetary arrangements pegging a currency rigidly to a foreign reserve currency"],
    ])},
    "world-history-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["International law codification", "Traces how customary international law became formalized into written treaties and conventions"],
    ])},
    "world-history-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Global anti-apartheid movement", "Traces the international solidarity campaign against South Africa's apartheid system"],
    ])},
    "world-history-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Global migration policy regimes", "Compares how different countries' immigration policies evolved over time"],
    ])},
    "world-history-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Cartography and sovereignty", "Examines how mapmaking has shaped and legitimized claims to territorial control"],
    ])},
    "world-history-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["International peacekeeping", "Traces the development of multinational forces deployed to maintain post-conflict peace"],
    ])},
    "world-history-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Currency union attempts", "Compares historical efforts by groups of countries to share a single currency"],
    ])},
    "world-history-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Telecommunications infrastructure expansion", "Traces the global spread of telegraph, telephone, and satellite networks"],
    ])},
    "world-history-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Global climate diplomacy origins", "Traces the earliest international institutions and agreements addressing climate change"],
    ])},
    "world-history-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Postwar reconstruction programs", "Compares efforts like the Marshall Plan to rebuild economies after WWII"],
    ])},
    "world-history-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Migration remittance economies", "Traces how money sent home by migrants has shaped sending-country economies"],
    ])},
    "world-history-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Anti-colonial intellectual networks", "Traces how activists and thinkers across colonies shared ideas and strategy"],
    ])},
    "world-history-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Currency devaluation episodes", "Compares historical cases of deliberate or forced currency value reductions"],
    ])},
    "world-history-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["International sporting boycotts", "Examines how nations used boycotts of sporting events as political protest"],
    ])},
    "world-history-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Refugee camp governance", "Traces how humanitarian organizations have administered large-scale refugee camps"],
    ])},
    "world-history-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Global debt crisis cycles", "Compares recurring patterns of sovereign debt crises across different eras and regions"],
    ])},
    "world-history-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["International development aid architecture", "Traces how global institutions for foreign aid were structured and evolved"],
    ])},
    "world-history-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Environmental disaster governance", "Traces international coordination in response to major environmental disasters"],
    ])},
    "world-history-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Currency peg regimes", "Compares historical systems of fixing one currency's value to another"],
    ])},
    "world-history-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Transnational corporate expansion", "Traces the historical growth of multinational corporations across borders"],
    ])},
    "world-history-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Intellectual property regime formation", "Traces how international IP rules like TRIPS were negotiated and formed"],
    ])},
    "world-history-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Global currency reserve systems", "Compares how different currencies have historically served as world reserve currencies"],
    ])},
    "world-history-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["International anti-trafficking movements", "Traces the history of global efforts against human trafficking"],
    ])},
    "world-history-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Pandemic preparedness institutions", "Traces the development of global bodies coordinating outbreak response"],
    ])},
    "world-history-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Bicycle/automobile mobility transition", "Traces how personal mobility technology reshaped global cities and society"],
    ])},
    "world-history-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Currency black markets", "Compares historical episodes of informal currency exchange emerging under controls"],
    ])},
    "world-history-m2-l100": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Presents original world history research demonstrating mastery of the field's methods"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"world-history-m2-l{base_n}"
    worked_key = f"world-history-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 World History lessons.")


if __name__ == "__main__":
    main()
