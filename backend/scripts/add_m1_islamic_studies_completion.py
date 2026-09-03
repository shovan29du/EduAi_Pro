#!/usr/bin/env python3
"""Depth pass, M1 Islamic Studies: fill in real, hand-checked
data_table content for the 99 M1 Islamic Studies lessons not covered
by the earlier breadth-first batch. Brings M1 Islamic Studies to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Islamic ethics & jurisprudence", "Grounds moral and legal reasoning in Quran, Sunnah, and scholarly consensus"],
        ]),
    },
    "islamic-studies-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Comparative religious thought", "Analyzes religions using shared scholarly methods rather than a single faith's assumptions"],
        ]),
    },
    "islamic-studies-m1-l4": {
        "data_table": table(["Surah", "Content"], [
            ["Al-Baqarah legal verses", "Address topics including fasting, retribution, marriage, and financial dealings"],
        ]),
    },
    "islamic-studies-m1-l5": {
        "data_table": table(["Surah", "Feature"], [
            ["Surah Yusuf", "A cohesive extended narrative recounting the story of the Prophet Joseph"],
        ]),
    },
    "islamic-studies-m1-l6": {
        "data_table": table(["Component", "Focus"], [
            ["Isnad", "The chain of narrators transmitting a hadith"],
            ["Matn", "The textual content of a hadith itself"],
        ]),
    },
    "islamic-studies-m1-l7": {
        "data_table": table(["Element", "Purpose"], [
            ["Chapter heading (tarjama)", "Bukhari used headings to embed legal reasoning alongside the hadith text"],
        ]),
    },
    "islamic-studies-m1-l8": {
        "data_table": table(["Feature", "Detail"], [
            ["Sahih Muslim organization", "Groups hadith thematically to aid systematic legal and doctrinal reference"],
        ]),
    },
    "islamic-studies-m1-l9": {
        "data_table": table(["Approach", "Detail"], [
            ["Historical-critical hadith scholarship", "Applies critical historical methods to hadith transmission and authenticity"],
        ]),
    },
    "islamic-studies-m1-l10": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research project", "Applies rigorous textual methodology to an original hadith or Quranic research question"],
        ]),
    },
    "islamic-studies-m1-l11": {
        "data_table": table(["Event", "Consequence"], [
            ["Abbasid Revolution", "Overthrew the Umayyads and shifted the caliphate's center toward Baghdad"],
        ]),
    },
    "islamic-studies-m1-l12": {
        "data_table": table(["State", "Feature"], [
            ["Fatimid Egypt", "Ismaili Shi'a governance that fostered a distinctive intellectual and artistic culture"],
        ]),
    },
    "islamic-studies-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Convivencia", "A period of relative religious coexistence in Islamic Iberia, with real limits and tensions"],
        ]),
    },
    "islamic-studies-m1-l14": {
        "data_table": table(["Ruler", "Policy"], [
            ["Akbar", "Promoted religious tolerance and syncretic policy (Din-i-Ilahi)"],
            ["Aurangzeb", "Pursued stricter orthodox religious policy"],
        ]),
    },
    "islamic-studies-m1-l15": {
        "data_table": table(["Impact", "Detail"], [
            ["Mongol conquest", "Devastated centers of Islamic scholarship while later Mongol rulers converted to Islam"],
        ]),
    },
    "islamic-studies-m1-l16": {
        "data_table": table(["Empire", "Feature"], [
            ["Mali/Songhai", "Trans-Saharan trade empires that became major centers of West African Islamic scholarship"],
        ]),
    },
    "islamic-studies-m1-l17": {
        "data_table": table(["Region", "Feature"], [
            ["Southeast Asian Islam", "Spread primarily through trade networks and blended with existing local traditions"],
        ]),
    },
    "islamic-studies-m1-l18": {
        "data_table": table(["Dynasty", "Feature"], [
            ["Safavid dynasty", "Established Twelver Shi'ism as Persia's state religion"],
        ]),
    },
    "islamic-studies-m1-l19": {
        "data_table": table(["Movement", "Response"], [
            ["Islamic reform movement", "Responded to colonial encounter by reexamining tradition and modern institutions"],
        ]),
    },
    "islamic-studies-m1-l20": {
        "data_table": table(["Figure", "Contribution"], [
            ["Jamal al-Din al-Afghani", "Advocated pan-Islamic unity against European colonial encroachment"],
        ]),
    },
    "islamic-studies-m1-l21": {
        "data_table": table(["Figure", "Movement"], [
            ["Rashid Rida", "Advanced the Salafiyya movement calling for return to early Islamic practice"],
        ]),
    },
    "islamic-studies-m1-l22": {
        "data_table": table(["Event", "Year"], [
            ["Abolition of the Ottoman Caliphate", "1924, under the new Turkish Republic"],
        ]),
    },
    "islamic-studies-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Postcolonial Islamic states", "Navigated varied relationships between religious law and modern state governance"],
        ]),
    },
    "islamic-studies-m1-l24": {
        "data_table": table(["Concept", "Meaning"], [
            ["Usul al-Fiqh", "Methodology governing how Islamic legal rulings are derived from sources"],
        ]),
    },
    "islamic-studies-m1-l25": {
        "data_table": table(["Objective", "Category"], [
            ["Maqasid al-Shariah", "Preservation of religion, life, intellect, lineage, and property"],
        ]),
    },
    "islamic-studies-m1-l26": {
        "data_table": table(["Debate", "Detail"], [
            ["Closure of ijtihad", "Scholars debate whether independent legal reasoning was ever truly foreclosed"],
        ]),
    },
    "islamic-studies-m1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Ijma", "Scholarly consensus recognized as a source of Islamic law"],
        ]),
    },
    "islamic-studies-m1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Istihsan", "Juristic preference departing from strict analogy for a more equitable ruling"],
            ["Istislah", "Rulings based on public interest (maslaha)"],
        ]),
    },
    "islamic-studies-m1-l29": {
        "data_table": table(["School", "Feature"], [
            ["Hanafi", "Emphasizes reasoned analogy and flexibility, widely followed in South/Central Asia"],
        ]),
    },
    "islamic-studies-m1-l30": {
        "data_table": table(["School", "Feature"], [
            ["Maliki", "Draws heavily on the practice (amal) of the people of Medina as a legal source"],
        ]),
    },
    "islamic-studies-m1-l31": {
        "data_table": table(["School", "Feature"], [
            ["Shafi'i", "Systematized legal theory, formalizing hierarchical sources of law"],
        ]),
    },
    "islamic-studies-m1-l32": {
        "data_table": table(["School", "Feature"], [
            ["Hanbali", "Emphasizes close textual adherence to Quran and hadith over speculative reasoning"],
        ]),
    },
    "islamic-studies-m1-l33": {
        "data_table": table(["School", "Feature"], [
            ["Ja'fari jurisprudence", "The primary legal school within Twelver Shi'a Islam"],
        ]),
    },
    "islamic-studies-m1-l34": {
        "data_table": table(["Field", "Focus"], [
            ["Fiqh al-Aqalliyyat", "Addresses distinctive legal questions facing Muslims living as minorities"],
        ]),
    },
    "islamic-studies-m1-l35": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Kindi", "Among the first to systematically introduce Greek philosophy into Islamic thought"],
        ]),
    },
    "islamic-studies-m1-l36": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Farabi", "Developed a political philosophy modeled on an ideal virtuous city"],
        ]),
    },
    "islamic-studies-m1-l37": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn Sina", "Distinguished essence from existence in a systematic metaphysical framework"],
        ]),
    },
    "islamic-studies-m1-l38": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn Rushd", "Argued for the compatibility of philosophical reason and religious revelation"],
        ]),
    },
    "islamic-studies-m1-l39": {
        "data_table": table(["Figure", "Contribution"], [
            ["Mulla Sadra", "Developed transcendent theosophy, synthesizing mysticism, philosophy, and theology"],
        ]),
    },
    "islamic-studies-m1-l40": {
        "data_table": table(["School", "Feature"], [
            ["Ash'ari theology", "Affirms divine attributes while avoiding anthropomorphism through careful qualification"],
        ]),
    },
    "islamic-studies-m1-l41": {
        "data_table": table(["School", "Feature"], [
            ["Maturidi theology", "Assigns reason a significant independent role in ethical knowledge"],
        ]),
    },
    "islamic-studies-m1-l42": {
        "data_table": table(["Doctrine", "Detail"], [
            ["Created Quran (Mu'tazila)", "Held the Quran was created rather than eternal, a major theological controversy"],
        ]),
    },
    "islamic-studies-m1-l43": {
        "data_table": table(["Event", "Detail"], [
            ["The Mihna", "An Abbasid-era inquisition enforcing the doctrine of the Quran's createdness"],
        ]),
    },
    "islamic-studies-m1-l44": {
        "data_table": table(["Doctrine", "Meaning"], [
            ["Wahdat al-Wujud", "Ibn Arabi's concept of the unity of existence within divine reality"],
        ]),
    },
    "islamic-studies-m1-l45": {
        "data_table": table(["Figure", "Contribution"], [
            ["Rumi", "Persian poet whose mystical verse expressed themes of divine love and union"],
        ]),
    },
    "islamic-studies-m1-l46": {
        "data_table": table(["Order", "Feature"], [
            ["Naqshbandi", "Emphasizes silent remembrance (dhikr) rather than vocal recitation"],
        ]),
    },
    "islamic-studies-m1-l47": {
        "data_table": table(["Order", "Feature"], [
            ["Qadiriyya", "One of the oldest and most widely spread global Sufi orders"],
        ]),
    },
    "islamic-studies-m1-l48": {
        "data_table": table(["Work", "Contribution"], [
            ["Ihya Ulum al-Din", "Al-Ghazali's synthesis reconciling Sufi spirituality with orthodox Islamic practice"],
        ]),
    },
    "islamic-studies-m1-l49": {
        "data_table": table(["Concept", "Meaning"], [
            ["Al-Insan al-Kamil", "The Sufi concept of the Perfect Human embodying complete spiritual realization"],
        ]),
    },
    "islamic-studies-m1-l50": {
        "data_table": table(["Figure", "Contribution"], [
            ["Rabia al-Adawiyya", "An early and highly influential female Sufi saint known for pure devotional love"],
        ]),
    },
    "islamic-studies-m1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Jarh wa Ta'dil", "The scholarly discipline evaluating hadith narrators' reliability"],
        ]),
    },
    "islamic-studies-m1-l52": {
        "data_table": table(["Grade", "Meaning"], [
            ["Sahih", "Authentic hadith with an unbroken, reliable chain of narrators"],
            ["Da'if", "Weak hadith with a questionable chain or content"],
        ]),
    },
    "islamic-studies-m1-l53": {
        "data_table": table(["Approach", "Focus"], [
            ["Tafsir bi al-ma'thur", "Interprets Quran using Quran, hadith, and companion reports"],
        ]),
    },
    "islamic-studies-m1-l54": {
        "data_table": table(["Approach", "Focus"], [
            ["Tafsir bi al-ra'y", "Interprets Quran using scholarly reasoning"],
        ]),
    },
    "islamic-studies-m1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Asbab al-nuzul", "The historical context/occasions of revelation for specific verses"],
        ]),
    },
    "islamic-studies-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Naskh (abrogation)", "The theory that some Quranic rulings supersede earlier ones"],
        ]),
    },
    "islamic-studies-m1-l57": {
        "data_table": table(["Doctrine", "Meaning"], [
            ["I'jaz al-Quran", "The Quran's literary inimitability is held as a sign of its divine origin"],
        ]),
    },
    "islamic-studies-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Balagha", "The classical Arabic study of rhetorical eloquence and expression"],
        ]),
    },
    "islamic-studies-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Quranic translation history", "Scholars debate whether translation can fully capture the Quran's sacred original"],
        ]),
    },
    "islamic-studies-m1-l60": {
        "data_table": table(["Manuscript", "Significance"], [
            ["Early Quranic codex", "Comparative study helps trace the textual history of Quran compilation"],
        ]),
    },
    "islamic-studies-m1-l61": {
        "data_table": table(["Event", "Detail"], [
            ["Uthmanic compilation", "Standardized a single authoritative written Quranic text under Caliph Uthman"],
        ]),
    },
    "islamic-studies-m1-l62": {
        "data_table": table(["Figure", "Contribution"], [
            ["Aisha bint Abi Bakr", "Major early narrator of hadith and legal authority"],
        ]),
    },
    "islamic-studies-m1-l63": {
        "data_table": table(["Movement", "Focus"], [
            ["Islamic feminism", "Reinterprets textual sources to address gender equity within an Islamic framework"],
        ]),
    },
    "islamic-studies-m1-l64": {
        "data_table": table(["Topic", "Detail"], [
            ["Islamic family law", "Governs marriage, divorce, and inheritance through varied jurisprudential interpretation"],
        ]),
    },
    "islamic-studies-m1-l65": {
        "data_table": table(["Issue", "Detail"], [
            ["End-of-life bioethics", "Islamic scholars weigh preserving life against avoiding excessive medical burden"],
        ]),
    },
    "islamic-studies-m1-l66": {
        "data_table": table(["Issue", "Detail"], [
            ["Genetic engineering ethics", "Raises questions about intervening in creation within Islamic ethical bounds"],
        ]),
    },
    "islamic-studies-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Islamic environmental ethics", "Frames humans as trustees (khalifah) responsible for creation"],
        ]),
    },
    "islamic-studies-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Islamic commercial law", "Regulates contracts to ensure fairness and avoid excessive uncertainty (gharar)"],
        ]),
    },
    "islamic-studies-m1-l69": {
        "data_table": table(["Instrument", "Detail"], [
            ["Sukuk", "Asset-backed Islamic financial certificates structured to avoid interest"],
        ]),
    },
    "islamic-studies-m1-l70": {
        "data_table": table(["Structure", "Feature"], [
            ["Mudarabah", "Profit-sharing partnership between capital provider and manager"],
            ["Musharakah", "Joint venture partnership sharing both profit and loss"],
        ]),
    },
    "islamic-studies-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Riba", "The prohibition of interest is a foundational principle of Islamic finance"],
        ]),
    },
    "islamic-studies-m1-l72": {
        "data_table": table(["Institution", "Role"], [
            ["Waqf", "Charitable endowment historically funding schools, hospitals, and public works"],
        ]),
    },
    "islamic-studies-m1-l73": {
        "data_table": table(["Institution", "Role"], [
            ["Madrasa", "Traditional institution for higher Islamic religious and legal education"],
        ]),
    },
    "islamic-studies-m1-l74": {
        "data_table": table(["Institution", "Role"], [
            ["Al-Azhar University", "A historic and continuing center of authority in Sunni Islamic scholarship"],
        ]),
    },
    "islamic-studies-m1-l75": {
        "data_table": table(["Institution", "Role"], [
            ["Nizamiyya colleges", "State-sponsored Seljuk-era institutions formalizing Islamic higher education"],
        ]),
    },
    "islamic-studies-m1-l76": {
        "data_table": table(["Contribution", "Detail"], [
            ["Islamic astronomy", "Built major observatories and refined calendar calculation methods"],
        ]),
    },
    "islamic-studies-m1-l77": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Khwarizmi", "His work on systematic equation-solving gave algebra its name and method"],
        ]),
    },
    "islamic-studies-m1-l78": {
        "data_table": table(["Work", "Contribution"], [
            ["Canon of Medicine", "Ibn Sina's comprehensive medical text served as a standard reference for centuries"],
        ]),
    },
    "islamic-studies-m1-l79": {
        "data_table": table(["Element", "Symbolism"], [
            ["Geometric pattern/arabesque", "Reflects infinite divine order through repeating, non-figurative design"],
        ]),
    },
    "islamic-studies-m1-l80": {
        "data_table": table(["Site", "Feature"], [
            ["Great Mosque of Cordoba", "Famous for its hypostyle hall of double-tiered horseshoe arches"],
        ]),
    },
    "islamic-studies-m1-l81": {
        "data_table": table(["Architect", "Contribution"], [
            ["Mimar Sinan", "Designed masterworks of Ottoman mosque architecture like the Süleymaniye Mosque"],
        ]),
    },
    "islamic-studies-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Just war theory in Islamic law", "Sets conditions distinguishing legitimate defense from unjust aggression"],
        ]),
    },
    "islamic-studies-m1-l83": {
        "data_table": table(["Practice", "Detail"], [
            ["Early Islamic diplomacy", "Treaty-making established formal relations between the early Muslim community and other powers"],
        ]),
    },
    "islamic-studies-m1-l84": {
        "data_table": table(["Status", "Detail"], [
            ["Dhimmi", "Protected non-Muslim minority status under classical Islamic law, with associated rights and obligations"],
        ]),
    },
    "islamic-studies-m1-l85": {
        "data_table": table(["Movement", "Feature"], [
            ["Wahhabism", "Emerged in 18th-century Arabia calling for a return to strict textual practice"],
        ]),
    },
    "islamic-studies-m1-l86": {
        "data_table": table(["Movement", "Feature"], [
            ["Contemporary Salafism", "A modern movement emphasizing return to early Islamic practice, with varied strands"],
        ]),
    },
    "islamic-studies-m1-l87": {
        "data_table": table(["Figure", "Contribution"], [
            ["Fazlur Rahman", "Developed a neo-modernist hermeneutic reading the Quran's ethical trajectory"],
        ]),
    },
    "islamic-studies-m1-l88": {
        "data_table": table(["Figure", "Contribution"], [
            ["Abdolkarim Soroush", "Advanced a religious epistemology distinguishing revelation from its historical interpretation"],
        ]),
    },
    "islamic-studies-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Theories of the caliphate", "Islamic political thought offers multiple, sometimes competing, models of legitimate leadership"],
        ]),
    },
    "islamic-studies-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Contemporary Islamism", "A modern political movement seeking Islamic principles as the basis of governance"],
        ]),
    },
    "islamic-studies-m1-l91": {
        "data_table": table(["Work", "Contribution"], [
            ["Muqaddimah", "Ibn Khaldun's foundational work theorizing social cohesion (asabiyyah) and historical cycles"],
        ]),
    },
    "islamic-studies-m1-l92": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Biruni", "Pioneered comparative, empirical methods in studying Indian religion and culture"],
        ]),
    },
    "islamic-studies-m1-l93": {
        "data_table": table(["Movement", "Feature"], [
            ["Barelvi-Deobandi divide", "A major theological split within South Asian Sunni Islam over practice and interpretation"],
        ]),
    },
    "islamic-studies-m1-l94": {
        "data_table": table(["School", "Feature"], [
            ["Zaydi jurisprudence", "A distinct Shi'a legal tradition prominent in Yemen"],
        ]),
    },
    "islamic-studies-m1-l95": {
        "data_table": table(["School", "Feature"], [
            ["Ibadi Islam", "A distinct branch predating the Sunni-Shia split, dominant in Oman"],
        ]),
    },
    "islamic-studies-m1-l96": {
        "data_table": table(["System", "Feature"], [
            ["Ottoman millet system", "Granted religious communities autonomy over their own legal and communal affairs"],
        ]),
    },
    "islamic-studies-m1-l97": {
        "data_table": table(["Art Form", "Feature"], [
            ["Islamic manuscript illumination", "Combines calligraphy and decorative ornamentation in sacred and literary texts"],
        ]),
    },
    "islamic-studies-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Halal certification", "Standardizes compliance verification across the growing global halal trade"],
        ]),
    },
    "islamic-studies-m1-l99": {
        "data_table": table(["Issue", "Detail"], [
            ["Islamic AI ethics", "Applies Islamic ethical principles to emerging questions raised by artificial intelligence"],
        ]),
    },
    "islamic-studies-m1-l100": {
        "data_table": table(["Figure", "Contribution"], [
            ["Muhammad Abduh", "A foundational figure in Islamic modernism, reconciling tradition with modern reform"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Term", "Meaning"], [
        ["Tafsir", "Interpretation and explanation of the Quran"],
        ["Asbab al-nuzul", "The historical context/occasions of revelation for specific verses"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"islamic-studies-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"islamic-studies-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"islamic-studies-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Islamic Studies lessons (completing 120/120).")


if __name__ == "__main__":
    main()
