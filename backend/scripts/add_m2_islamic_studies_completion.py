#!/usr/bin/env python3
"""Depth pass, M2 Islamic Studies: fill in real, hand-checked
data_table content for the M2 Islamic Studies lessons not covered by
the earlier breadth-first batch. Brings M2 Islamic Studies to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning Islamic
legal theory and jurisprudence, Islamic intellectual and theological
history, Sufism, Quranic and hadith studies, and contemporary Islamic
scholarship; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed
by an earlier breadth-first batch, so its data_table is hard-coded
here for reuse (it falls within l1-l20, so it is also reused for
l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Usul al-Fiqh", "The methodology and theoretical principles underlying Islamic legal reasoning"],
    ["Legal reasoning sources", "Includes the Quran, Sunnah, consensus (ijma), and analogy (qiyas)"],
])

CHARTS: dict[str, dict] = {
    "islamic-studies-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Comparative religious thought research", "Systematic scholarly methods for studying and comparing religious traditions"],
    ])},
    "islamic-studies-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Quranic studies methodology", "Scholarly approaches to analyzing the Quran's text, context, and interpretation"],
    ])},
    "islamic-studies-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Maqasid al-Shari'ah", "The higher objectives of Islamic law, such as preserving life, faith, and property"],
    ])},
    "islamic-studies-m2-l5": {"data_table": table(["School", "Tradition"], [
        ["Hanafi, Maliki, Shafi'i, Hanbali", "The four major Sunni schools of Islamic jurisprudence"],
    ])},
    "islamic-studies-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Twelver Shi'a ijtihad", "The ongoing exercise of independent legal reasoning by qualified jurists in Twelver Shi'a law"],
    ])},
    "islamic-studies-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Early Islamic conquests historiography", "Scholarly debate over the sources and processes behind rapid 7th-century Islamic expansion"],
    ])},
    "islamic-studies-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Bayt al-Hikma", "The Abbasid 'House of Wisdom' that translated and preserved Greek and other classical texts"],
    ])},
    "islamic-studies-m2-l9": {"data_table": table(["School", "Position"], [
        ["Ash'ari", "Emphasized divine omnipotence and revelation over pure reason"],
        ["Mu'tazila", "Emphasized rationalist theology and human free will"],
    ])},
    "islamic-studies-m2-l10": {"data_table": table(["Scholar", "Contribution"], [
        ["Ibn Rushd (Averroes)", "Argued philosophy and revelation could be reconciled through careful interpretation"],
    ])},
    "islamic-studies-m2-l11": {"data_table": table(["Scholar", "Contribution"], [
        ["Ibn Arabi", "Developed influential Sufi metaphysical concepts like Wahdat al-Wujud (unity of being)"],
    ])},
    "islamic-studies-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Madrasa system", "The institutional structure of formal Islamic religious and legal education"],
    ])},
    "islamic-studies-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Women's legal agency (classical courts)", "Studies documented evidence of women's participation in Islamic legal proceedings"],
    ])},
    "islamic-studies-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Mecelle", "The Ottoman Empire's codification of Islamic civil law in the late 19th century"],
    ])},
    "islamic-studies-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Riba prohibition", "The Islamic legal prohibition of interest, shaping the structure of modern Islamic banking"],
    ])},
    "islamic-studies-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Sukuk", "Islamic financial certificates structured to comply with Sharia by representing asset ownership, not debt"],
    ])},
    "islamic-studies-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Maslaha", "Public interest or welfare used as a source of legal reasoning in Islamic jurisprudence"],
    ])},
    "islamic-studies-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Qawa'id Fiqhiyya", "General legal maxims that summarize broad principles across Islamic jurisprudence"],
    ])},
    "islamic-studies-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Ilm al-Rijal", "The science of evaluating the reliability of hadith narrators"],
    ])},
    "islamic-studies-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Isnad analysis", "Examines the chain of transmitters of a hadith to assess its authenticity"],
    ])},
    "islamic-studies-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Tafsir genres", "Different scholarly approaches to Quranic exegesis, from linguistic to mystical interpretation"],
    ])},
    "islamic-studies-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Asbab al-Nuzul", "The historical circumstances behind the revelation of specific Quranic verses"],
    ])},
    "islamic-studies-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Islamic cosmology (medieval philosophy)", "Medieval philosophical texts describing the structure and origin of the universe"],
    ])},
    "islamic-studies-m2-l24": {"data_table": table(["Scholar", "Contribution"], [
        ["Al-Farabi", "Described an ideal 'virtuous city' governed by philosophical wisdom"],
    ])},
    "islamic-studies-m2-l25": {"data_table": table(["Scholar", "Contribution"], [
        ["Ibn Khaldun", "Theorized asabiyyah (group solidarity) as driving the rise and fall of dynasties"],
    ])},
    "islamic-studies-m2-l26": {"data_table": table(["Field", "Contribution"], [
        ["Algebra/astronomy", "Islamic scholars like al-Khwarizmi advanced algebra and precise astronomical observation"],
    ])},
    "islamic-studies-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Convivencia debate", "Debates the extent of coexistence among Muslims, Christians, and Jews in medieval Iberia"],
    ])},
    "islamic-studies-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Crusades (Islamic perspectives)", "Examines how Muslim chroniclers understood and recorded the Crusades"],
    ])},
    "islamic-studies-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Mongol invasions (intellectual response)", "Studies how Islamic scholarship adapted and responded to Mongol conquest and rule"],
    ])},
    "islamic-studies-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Turuq (Sufi orders)", "Organized brotherhoods that institutionalized Sufi practice and transmission"],
    ])},
    "islamic-studies-m2-l31": {"data_table": table(["Scholar", "Contribution"], [
        ["Al-Junayd", "A foundational figure of the 'sober' school of Sufism emphasizing disciplined mysticism"],
    ])},
    "islamic-studies-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Masnavi (Rumi)", "A major work of Persian Sufi poetry expressing mystical love and spiritual teaching"],
    ])},
    "islamic-studies-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Wahhabi reform movement", "An 18th-century Arabian reform movement calling for a return to strict monotheism"],
    ])},
    "islamic-studies-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Salafi thought", "Modern reformist movement advocating a return to the practices of the earliest Muslim generations"],
    ])},
    "islamic-studies-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Colonial reform of Islamic education", "Studies how colonial encounters reshaped traditional Islamic educational institutions"],
    ])},
    "islamic-studies-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Post-colonial Islamic state formation", "Debates how newly independent Muslim-majority states incorporated Islamic law"],
    ])},
    "islamic-studies-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Collective ijtihad", "Modern fatwa councils issuing legal opinions through group scholarly deliberation"],
    ])},
    "islamic-studies-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Islamic bioethics (organ transplantation)", "Applies Islamic jurisprudence to modern medical ethical questions"],
    ])},
    "islamic-studies-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Genetic engineering/cloning (Islamic view)", "Examines contemporary Islamic jurisprudential responses to biotechnology"],
    ])},
    "islamic-studies-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Islamic environmental ethics", "Draws on Quranic stewardship concepts to address ecological responsibility"],
    ])},
    "islamic-studies-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Halal certification", "Systems verifying products meet Islamic dietary and production requirements for global trade"],
    ])},
    "islamic-studies-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Islamic just war theory", "Classical jurisprudential principles governing the conduct and justification of warfare"],
    ])},
    "islamic-studies-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Dhimmi status", "The historical legal status of protected non-Muslim minorities under classical Islamic law"],
    ])},
    "islamic-studies-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Christology debates (comparative)", "Compares Islamic and Christian theological views on the nature of Jesus"],
    ])},
    "islamic-studies-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Interfaith dialogue methodology", "Scholarly approaches to structuring respectful, substantive dialogue between religions"],
    ])},
    "islamic-studies-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Islamic calligraphy", "A revered sacred art form central to Islamic visual and religious culture"],
    ])},
    "islamic-studies-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Mosque design symbolism", "Examines how architectural elements express theological meaning in mosque design"],
    ])},
    "islamic-studies-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Waqf", "An inalienable Islamic charitable endowment supporting religious or public institutions"],
    ])},
    "islamic-studies-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Zakat administration", "Studies historical and modern systems for collecting and distributing obligatory almsgiving"],
    ])},
    "islamic-studies-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Caliphate theory", "Classical political theory on the ideal Islamic leadership institution and its critics"],
    ])},
    "islamic-studies-m2-l51": {"data_table": table(["Model", "Feature"], [
        ["Khilafa", "A unified transnational Islamic political authority"],
        ["Nation-state", "Sovereign states with defined territorial borders"],
    ])},
    "islamic-studies-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Feminist Islamic scholarship", "Reinterprets Islamic jurisprudence from a modern gender-critical perspective"],
    ])},
    "islamic-studies-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Family law reform (Muslim countries)", "Studies legal changes to marriage and family regulations across Muslim-majority states"],
    ])},
    "islamic-studies-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Quranic textual criticism", "Scholarly analysis of historical manuscript traditions of the Quranic text"],
    ])},
    "islamic-studies-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Quranic codex compilation", "Traces the historical process by which the Quran was compiled into its standard written form"],
    ])},
    "islamic-studies-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Qira'at", "The science of the accepted variant oral recitations of the Quran"],
    ])},
    "islamic-studies-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Mantiq", "Islamic philosophical logic, drawing on and adapting Aristotelian traditions"],
    ])},
    "islamic-studies-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Islamic eschatology", "Doctrines concerning the afterlife, judgment, and end times in Islamic theology"],
    ])},
    "islamic-studies-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Sira", "The genre of prophetic biography, a key historical source for early Islamic history"],
    ])},
    "islamic-studies-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Orientalist scholarship (critique)", "Examines biases in Western academic study of Islam and its later critical revision"],
    ])},
    "islamic-studies-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Revisionist historiography of early Islam", "Scholarly approaches questioning traditional narratives of Islam's earliest history"],
    ])},
    "islamic-studies-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Islamic legal pluralism (colonial/postcolonial)", "Studies how Islamic law coexisted with colonial and secular legal systems"],
    ])},
    "islamic-studies-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Sunni-Shi'a divergence", "Traces the historical origins and development of the major sectarian split in Islam"],
    ])},
    "islamic-studies-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Ismaili esoteric theology", "Studies the distinct doctrinal and institutional history of Ismaili Shi'a thought"],
    ])},
    "islamic-studies-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Sufi-orthodox tensions", "Traces historical debates between mystical Sufi practice and legalistic orthodoxy"],
    ])},
    "islamic-studies-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Manuscript illumination", "The tradition of decorating Islamic manuscripts, including the Quran, with intricate art"],
    ])},
    "islamic-studies-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Jewish-Muslim intellectual exchange (medieval Spain)", "Studies the shared scholarly culture of medieval Andalusian society"],
    ])},
    "islamic-studies-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Usury and economic ethics", "Applies Islamic legal views on interest to contemporary economic and financial questions"],
    ])},
    "islamic-studies-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Global da'wa movements", "Transnational networks engaged in Islamic religious outreach and education"],
    ])},
    "islamic-studies-m2-l70": {"data_table": table(["Concept", "Distinction"], [
        ["Ijtihad", "Independent legal reasoning"],
        ["Taqlid", "Following established legal precedent"],
    ])},
    "islamic-studies-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Political theology of Islamist movements", "Analyzes the theological and political frameworks of contemporary Islamist organizations"],
    ])},
    "islamic-studies-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Islamic human rights perspectives", "Compares Islamic legal traditions with international human rights frameworks"],
    ])},
    "islamic-studies-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Sharia court procedure", "Traces the historical development of Islamic legal court practices and procedures"],
    ])},
    "islamic-studies-m2-l74": {"data_table": table(["Work", "Author"], [
        ["Muqaddimah", "Ibn Khaldun's introduction to history, presenting a systematic philosophy of history"],
    ])},
    "islamic-studies-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Insan al-Kamil", "The Sufi concept of the 'Perfect Human' who fully realizes divine attributes"],
    ])},
    "islamic-studies-m2-l76": {"data_table": table(["Region", "Feature"], [
        ["Southeast Asia", "Islamic legal practice shaped by local adat (customary) traditions"],
    ])},
    "islamic-studies-m2-l77": {"data_table": table(["Region", "Feature"], [
        ["West Africa", "Islamic legal practice shaped by local Sufi orders and traditional structures"],
    ])},
    "islamic-studies-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Islamic manuscript libraries", "Traces the history of major libraries preserving Islamic scholarly manuscripts"],
    ])},
    "islamic-studies-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Predestination and human agency", "Classical theological debates over divine decree versus free human will"],
    ])},
    "islamic-studies-m2-l80": {"data_table": table(["Tradition", "Comparison"], [
        ["Islamic/Buddhist contemplative practice", "Compares meditative and mystical practices across the two traditions"],
    ])},
    "islamic-studies-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Jihad doctrine reinterpretation", "Traces the historical evolution and modern reinterpretation of jihad's meanings"],
    ])},
    "islamic-studies-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Uqud", "Islamic contract law governing commercial and financial agreements"],
    ])},
    "islamic-studies-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Ijma", "Scholarly consensus as a recognized source of Islamic law"],
    ])},
    "islamic-studies-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Qiyas", "Analogical reasoning used to extend Islamic legal rulings to new cases"],
    ])},
    "islamic-studies-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Islamic calendar/timekeeping", "The lunar Hijri calendar system used for religious observance"],
    ])},
    "islamic-studies-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Sufi poetry (divine love)", "A literary tradition expressing mystical devotion through the language of romantic love"],
    ])},
    "islamic-studies-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Adab", "Islamic educational philosophy emphasizing character formation alongside knowledge"],
    ])},
    "islamic-studies-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Muslim scientific observatories", "Historical institutions dedicated to astronomical observation in the Islamic world"],
    ])},
    "islamic-studies-m2-l89": {"data_table": table(["Tradition", "Debate"], [
        ["Zoroastrian influence debate", "Scholars debate the extent of Zoroastrian influence on Islamic eschatology"],
    ])},
    "islamic-studies-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Modern fatwa methodology", "Contemporary bioethical councils' processes for issuing considered religious rulings"],
    ])},
    "islamic-studies-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Islamic philanthropic institutions", "Traces the historical development of charitable giving structures in Islamic societies"],
    ])},
    "islamic-studies-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Islamic feminist Quranic hermeneutics", "Reinterprets Quranic verses using gender-conscious interpretive methods"],
    ])},
    "islamic-studies-m2-l93": {"data_table": table(["Empire", "Relationship"], [
        ["Ottoman/Safavid", "Both empires had complex relationships between Sufi orders and state political power"],
    ])},
    "islamic-studies-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Islamic medicine/hospitals", "Traces medieval Islamic contributions to medical institutions and practice"],
    ])},
    "islamic-studies-m2-l95": {"data_table": table(["Component", "Purpose"], [
        ["Thesis seminar", "Trains graduate students in rigorous research methods specific to Islamic Studies"],
    ])},
    "islamic-studies-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Urf", "Local custom, recognized as a secondary source informing Islamic legal rulings"],
    ])},
    "islamic-studies-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Islamic astronomy/prayer-time determination", "Traces how astronomical science supported precise Islamic ritual timekeeping"],
    ])},
    "islamic-studies-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Sama", "Sufi devotional practice involving music and sometimes movement to reach spiritual states"],
    ])},
    "islamic-studies-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Islamic AI/bioethics frontiers", "Applies Islamic jurisprudential methods to emerging technologies like artificial intelligence"],
    ])},
    "islamic-studies-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Fiqh al-Aqalliyyat", "Jurisprudence specifically addressing Muslim minorities living in non-Muslim majority states"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"islamic-studies-m2-l{base_n}"
    worked_key = f"islamic-studies-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Islamic Studies lessons.")


if __name__ == "__main__":
    main()
