#!/usr/bin/env python3
"""Depth pass, C1 World History: fill in real, hand-checked data_table
content for the 71 C1 World History lessons not covered by the earlier
breadth-first batch. Brings C1 World History to full 72/72 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_world_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-history-c1-l1": {
        "data_table": table(["Civilization", "Region"], [
            ["Mesopotamia", "Between the Tigris and Euphrates rivers"], ["Ancient Egypt", "Along the Nile River"],
        ]),
    },
    "world-history-c1-l2": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Medieval period", "c. 500-1500 CE"], ["Early modern period", "c. 1500-1800 CE"],
        ]),
    },
    "world-history-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Mandate of Heaven", "The belief that Chinese rulers governed with divine approval"],
        ]),
    },
    "world-history-c1-l5": {
        "data_table": table(["Period", "Feature"], [
            ["Indus Valley Civilization", "Advanced urban planning around 2500 BCE"], ["Vedic Age", "Composition of the Vedas, early Hindu texts"],
        ]),
    },
    "world-history-c1-l6": {
        "data_table": table(["Period", "Feature"], [
            ["Roman Kingdom", "Early monarchy period before the Republic"], ["Roman Republic", "Governed by elected officials and the Senate"],
        ]),
    },
    "world-history-c1-l7": {
        "data_table": table(["Feature", "Detail"], [
            ["Silk Road", "Trade network connecting Han China to the West"],
        ]),
    },
    "world-history-c1-l8": {
        "data_table": table(["Empire", "Notable Ruler"], [
            ["Maurya Empire", "Ashoka the Great"], ["Gupta Empire", "Known as India's Golden Age"],
        ]),
    },
    "world-history-c1-l9": {
        "data_table": table(["Feature", "Detail"], [
            ["Feudalism", "A hierarchical system of land and loyalty exchange"],
        ]),
    },
    "world-history-c1-l10": {
        "data_table": table(["Field", "Contribution"], [
            ["Mathematics", "Advances in algebra by Al-Khwarizmi"], ["Medicine", "Ibn Sina's medical encyclopedia"],
        ]),
    },
    "world-history-c1-l11": {
        "data_table": table(["Empire", "Notable Feature"], [
            ["Mali Empire", "Ruled by Mansa Musa, known for immense wealth"], ["Songhai Empire", "Centered on the trade city of Timbuktu"],
        ]),
    },
    "world-history-c1-l12": {
        "data_table": table(["Feature", "Detail"], [
            ["Genghis Khan", "United Mongol tribes and founded the Mongol Empire"],
        ]),
    },
    "world-history-c1-l13": {
        "data_table": table(["Explorer", "Achievement"], [
            ["Christopher Columbus", "Reached the Americas in 1492"], ["Vasco da Gama", "Sailed a sea route to India"],
        ]),
    },
    "world-history-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Atlantic slave trade", "The forced transport of enslaved Africans to the Americas"],
        ]),
    },
    "world-history-c1-l15": {
        "data_table": table(["Figure", "Contribution"], [
            ["Galileo Galilei", "Supported heliocentrism through observation"], ["Isaac Newton", "Formulated laws of motion and gravity"],
        ]),
    },
    "world-history-c1-l16": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"], ["Montesquieu", "Separation of powers in government"],
        ]),
    },
    "world-history-c1-l17": {
        "data_table": table(["Innovation", "Impact"], [
            ["Steam engine", "Powered factories and transportation"],
        ]),
    },
    "world-history-c1-l18": {
        "data_table": table(["Country", "Unifying Figure"], [
            ["Italy", "Giuseppe Garibaldi"], ["Germany", "Otto von Bismarck"],
        ]),
    },
    "world-history-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Imperialism", "One nation extending power over other territories, often by colonization"],
        ]),
    },
    "world-history-c1-l20": {
        "data_table": table(["Cause", "Detail"], [
            ["Alliance system", "Complex treaties drew multiple nations into conflict"], ["Assassination of Franz Ferdinand", "Immediate trigger of the war"],
        ]),
    },
    "world-history-c1-l21": {
        "data_table": table(["Development", "Impact"], [
            ["Agricultural Revolution", "Shift from hunting-gathering to farming and permanent settlements"],
        ]),
    },
    "world-history-c1-l22": {
        "data_table": table(["Ruler", "Achievement"], [
            ["Cyrus the Great", "Founded the Achaemenid Persian Empire"], ["Darius I", "Expanded and administered the empire"],
        ]),
    },
    "world-history-c1-l23": {
        "data_table": table(["City-State", "Government Type"], [
            ["Athens", "Direct democracy"], ["Sparta", "Militaristic oligarchy"],
        ]),
    },
    "world-history-c1-l24": {
        "data_table": table(["Feature", "Detail"], [
            ["Alexander the Great", "Conquered territory from Greece to India"], ["Hellenistic period", "Spread of Greek culture across conquered lands"],
        ]),
    },
    "world-history-c1-l25": {
        "data_table": table(["Feature", "Detail"], [
            ["Phoenicians", "Seafaring traders who spread an alphabet across the Mediterranean"],
        ]),
    },
    "world-history-c1-l26": {
        "data_table": table(["Feature", "Detail"], [
            ["Kingdom of Kush", "Ancient civilization along the Nile, south of Egypt"],
        ]),
    },
    "world-history-c1-l27": {
        "data_table": table(["Cause", "Detail"], [
            ["Invasions", "Repeated attacks by Germanic tribes"], ["Economic decline", "Weakened trade and heavy taxation"],
        ]),
    },
    "world-history-c1-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Samurai", "Warrior class governed by the code of bushido"],
        ]),
    },
    "world-history-c1-l29": {
        "data_table": table(["Feature", "Detail"], [
            ["Aztec Empire", "Centered at Tenochtitlan, in present-day Mexico"],
        ]),
    },
    "world-history-c1-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Inca Empire", "Extensive road network across the Andes Mountains"],
        ]),
    },
    "world-history-c1-l31": {
        "data_table": table(["Feature", "Detail"], [
            ["Maya civilization", "Known for advanced astronomy and a written calendar system"],
        ]),
    },
    "world-history-c1-l32": {
        "data_table": table(["Ruler", "Achievement"], [
            ["Mehmed II", "Conquered Constantinople in 1453"],
        ]),
    },
    "world-history-c1-l33": {
        "data_table": table(["Figure", "Contribution"], [
            ["Martin Luther", "Wrote the Ninety-Five Theses challenging the Catholic Church"],
        ]),
    },
    "world-history-c1-l34": {
        "data_table": table(["Field", "Notable Figure"], [
            ["Art", "Leonardo da Vinci"], ["Literature", "William Shakespeare"],
        ]),
    },
    "world-history-c1-l35": {
        "data_table": table(["Ruler", "Country"], [
            ["Louis XIV", "France, epitome of absolute monarchy"],
        ]),
    },
    "world-history-c1-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Thirty Years' War", "Religious and political conflict across Central Europe (1618-1648)"],
        ]),
    },
    "world-history-c1-l37": {
        "data_table": table(["Feature", "Detail"], [
            ["Qing Dynasty", "China's last imperial dynasty, ruled by the Manchu"],
        ]),
    },
    "world-history-c1-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Tokugawa Shogunate", "Period of enforced isolation and stability in Japan"],
        ]),
    },
    "world-history-c1-l39": {
        "data_table": table(["Power", "Region Colonized"], [
            ["Spain", "Much of Central and South America"], ["Britain", "Parts of North America"],
        ]),
    },
    "world-history-c1-l40": {
        "data_table": table(["Feature", "Detail"], [
            ["Haitian Revolution", "Successful slave revolt leading to Haiti's independence in 1804"],
        ]),
    },
    "world-history-c1-l41": {
        "data_table": table(["Leader", "Region"], [
            ["Simon Bolivar", "Led independence movements across South America"],
        ]),
    },
    "world-history-c1-l42": {
        "data_table": table(["Feature", "Detail"], [
            ["Congress of Vienna", "1815 meeting redrawing European borders after Napoleon"],
        ]),
    },
    "world-history-c1-l43": {
        "data_table": table(["Feature", "Detail"], [
            ["Meiji Restoration", "Rapid modernization and industrialization of Japan after 1868"],
        ]),
    },
    "world-history-c1-l44": {
        "data_table": table(["Feature", "Detail"], [
            ["Opium Wars", "Conflicts between China and Britain over trade, weakening Qing power"],
        ]),
    },
    "world-history-c1-l45": {
        "data_table": table(["Cause", "Detail"], [
            ["Treaty of Versailles", "Harsh terms on Germany fueled resentment"], ["Rise of fascism", "Aggressive expansion by Germany, Italy, and Japan"],
        ]),
    },
    "world-history-c1-l46": {
        "data_table": table(["Event", "Year"], [
            ["Invasion of Poland", "1939, start of the war in Europe"], ["D-Day landings", "1944, Allied invasion of Normandy"],
        ]),
    },
    "world-history-c1-l47": {
        "data_table": table(["Event", "Year"], [
            ["Attack on Pearl Harbor", "1941, brought the US into the war"], ["Atomic bombings", "1945, ended the war in the Pacific"],
        ]),
    },
    "world-history-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["The Holocaust", "The systematic genocide of six million Jews by Nazi Germany"],
        ]),
    },
    "world-history-c1-l49": {
        "data_table": table(["Feature", "Detail"], [
            ["United Nations", "Founded in 1945 to promote peace and international cooperation"],
        ]),
    },
    "world-history-c1-l50": {
        "data_table": table(["Feature", "Detail"], [
            ["Cold War", "Ideological standoff between the US and Soviet Union after WWII"],
        ]),
    },
    "world-history-c1-l51": {
        "data_table": table(["Feature", "Detail"], [
            ["Decolonization in Africa", "Wave of African nations gaining independence, mostly 1950s-1960s"],
        ]),
    },
    "world-history-c1-l52": {
        "data_table": table(["Country", "Independence"], [
            ["India", "Gained independence from Britain in 1947"],
        ]),
    },
    "world-history-c1-l53": {
        "data_table": table(["Feature", "Detail"], [
            ["Chinese Communist Revolution", "Mao Zedong's Communist Party won control of China in 1949"],
        ]),
    },
    "world-history-c1-l54": {
        "data_table": table(["Feature", "Detail"], [
            ["Korean War", "1950-1953 conflict dividing the Korean Peninsula"],
        ]),
    },
    "world-history-c1-l55": {
        "data_table": table(["Feature", "Detail"], [
            ["Vietnam War", "Prolonged Cold War conflict between North and South Vietnam"],
        ]),
    },
    "world-history-c1-l56": {
        "data_table": table(["Feature", "Detail"], [
            ["Cuban Missile Crisis", "1962 standoff over Soviet missiles in Cuba"],
        ]),
    },
    "world-history-c1-l57": {
        "data_table": table(["Movement", "Feature"], [
            ["US Civil Rights Movement", "Fought to end racial segregation and discrimination"],
        ]),
    },
    "world-history-c1-l58": {
        "data_table": table(["Feature", "Detail"], [
            ["Fall of the Berlin Wall", "1989 event symbolizing the end of Cold War division"],
        ]),
    },
    "world-history-c1-l59": {
        "data_table": table(["Feature", "Detail"], [
            ["Collapse of the Soviet Union", "1991 dissolution into 15 independent states"],
        ]),
    },
    "world-history-c1-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing interconnection of economies and cultures worldwide"],
        ]),
    },
    "world-history-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating causes of decline", "Weighing invasion, economic strain, and political instability"],
        ]),
    },
    "world-history-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing Aztec society", "Examining its religious and political structure"],
        ]),
    },
    "world-history-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing religious reform", "Tracing how the Reformation split Western Christianity"],
        ]),
    },
    "world-history-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a European conflict", "Mapping the shifting alliances of the Thirty Years' War"],
        ]),
    },
    "world-history-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a revolution", "Assessing how the Haitian Revolution influenced abolition movements"],
        ]),
    },
    "world-history-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a peace settlement", "Evaluating how the Congress of Vienna aimed to prevent future wars"],
        ]),
    },
    "world-history-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing unequal treaties", "Examining the terms imposed on China after the Opium Wars"],
        ]),
    },
    "world-history-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing independence movements", "Contrasting decolonization paths across African nations"],
        ]),
    },
    "world-history-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing revolutionary ideology", "Examining Mao's approach to land reform and class struggle"],
        ]),
    },
    "world-history-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a divided nation", "Comparing the political systems of North and South Korea"],
        ]),
    },
    "world-history-c1-l71": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a Cold War standoff", "Assessing the diplomatic resolution of the Cuban Missile Crisis"],
        ]),
    },
    "world-history-c1-l72": {
        "data_table": table(["Application", "Example"], [
            ["Comparing classical Indian empires", "Contrasting the administrative approaches of the Maurya and Gupta empires"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 World History lessons (completing 72/72).")


if __name__ == "__main__":
    main()
