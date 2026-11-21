#!/usr/bin/env python3
"""Depth pass, C1 World Religions: fill in real, hand-checked
data_table content for the 99 C1 World Religions lessons not covered
by the earlier breadth-first batch. Brings C1 World Religions to full
100/100 coverage.

Note: this subject has 100 lessons structured as 20 topics x 5 modes:
l1-20 Conceptual Foundations, l21-40 Worked Analysis, l41-60 Evidence
and Data, l61-80 Comparative Case Study, l81-100 Applied Research
Seminar (topic N maps to lessons N, N+20, N+40, N+60, N+80).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_world_religions_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPICS: list[dict] = [
    {  # 1
        "name": "Methods in Religious Studies",
        "foundations": table(["Approach", "Focus"], [["Phenomenology of religion", "Describes religious experience without judging its truth"], ["Comparative religion", "Studies similarities and differences across traditions"]]),
        "worked": table(["Step", "Example"], [["Applying comparative method", "Comparing creation narratives across two traditions"]]),
        "evidence": table(["Source", "Use"], [["Ethnographic fieldwork", "Provides firsthand data on lived religious practice"]]),
        "case_study": table(["Approach", "Insight"], [["Insider vs. outsider perspective", "Shapes how a tradition is interpreted and described"]]),
        "seminar": table(["Step", "Focus"], [["Conducting a comparative study", "Applying a consistent method across two religious traditions"]]),
    },
    {  # 2
        "name": "Indigenous Traditions",
        "foundations": table(["Feature", "Detail"], [["Oral tradition", "Knowledge and belief passed down through spoken narrative"]]),
        "worked": table(["Step", "Example"], [["Interpreting a creation story", "Analyzing its connection to land and community identity"]]),
        "evidence": table(["Source", "Use"], [["Elder testimony", "A primary source for preserving indigenous spiritual knowledge"]]),
        "case_study": table(["Tradition", "Feature"], [["Australian Aboriginal Dreamtime", "Connects ancestral stories to land and law"]]),
        "seminar": table(["Step", "Focus"], [["Researching an indigenous tradition", "Documenting its connection between belief and land"]]),
    },
    {  # 3
        "name": "Hindu Traditions",
        "foundations": table(["Term", "Meaning"], [["Dharma", "Duty or righteous conduct appropriate to one's role"], ["Moksha", "Liberation from the cycle of rebirth"]]),
        "worked": table(["Text", "Focus"], [["Bhagavad Gita", "A dialogue on duty and devotion within the Mahabharata"]]),
        "evidence": table(["Metric", "Insight"], [["Hindu population data", "Shows over a billion adherents, concentrated in South Asia"]]),
        "case_study": table(["Practice", "Region"], [["Bhakti devotion", "A major devotional movement across the Indian subcontinent"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a Hindu festival", "Tracing its ritual meaning and regional variation"]]),
    },
    {  # 4
        "name": "Buddhist Traditions",
        "foundations": table(["Term", "Meaning"], [["Four Noble Truths", "The Buddha's core teaching on suffering and its cessation"]]),
        "worked": table(["Branch", "Feature"], [["Theravada", "Emphasizes individual liberation through monastic practice"], ["Mahayana", "Emphasizes universal liberation and the bodhisattva ideal"]]),
        "evidence": table(["Metric", "Insight"], [["Buddhist population by region", "Concentrated across East and Southeast Asia"]]),
        "case_study": table(["Tradition", "Region"], [["Zen Buddhism", "A meditation-focused tradition prominent in Japan"]]),
        "seminar": table(["Step", "Focus"], [["Comparing Buddhist branches", "Contrasting Theravada and Mahayana practice"]]),
    },
    {  # 5
        "name": "Jain Traditions",
        "foundations": table(["Term", "Meaning"], [["Ahimsa", "Nonviolence toward all living beings, a core Jain principle"]]),
        "worked": table(["Practice", "Example"], [["Careful movement", "Avoiding harm to even small creatures underfoot"]]),
        "evidence": table(["Metric", "Insight"], [["Jain population data", "A small but historically influential community, mainly in India"]]),
        "case_study": table(["Practice", "Insight"], [["Jain fasting rituals", "Reflect the tradition's emphasis on self-discipline"]]),
        "seminar": table(["Step", "Focus"], [["Researching ahimsa in practice", "Tracing its influence on Jain daily life and diet"]]),
    },
    {  # 6
        "name": "Sikh Traditions",
        "foundations": table(["Term", "Meaning"], [["Guru Granth Sahib", "The central sacred text and eternal Guru of Sikhism"]]),
        "worked": table(["Practice", "Example"], [["Langar", "A communal free kitchen open to all, regardless of background"]]),
        "evidence": table(["Metric", "Insight"], [["Sikh population data", "Concentrated in Punjab, India, with a global diaspora"]]),
        "case_study": table(["Practice", "Insight"], [["The Five Ks", "Physical articles of faith worn by initiated Sikhs"]]),
        "seminar": table(["Step", "Focus"], [["Researching the langar tradition", "Analyzing its role in Sikh community and equality values"]]),
    },
    {  # 7
        "name": "Jewish Traditions",
        "foundations": table(["Term", "Meaning"], [["Torah", "The central text of Jewish law and teaching"]]),
        "worked": table(["Branch", "Feature"], [["Orthodox Judaism", "Emphasizes strict adherence to traditional law"], ["Reform Judaism", "Emphasizes adaptation of practice to modern life"]]),
        "evidence": table(["Metric", "Insight"], [["Jewish population data", "Concentrated in Israel and the United States"]]),
        "case_study": table(["Practice", "Insight"], [["Passover Seder", "A ritual meal commemorating the Exodus from Egypt"]]),
        "seminar": table(["Step", "Focus"], [["Comparing Jewish movements", "Contrasting Orthodox and Reform approaches to practice"]]),
    },
    {  # 8
        "name": "Christian Traditions",
        "foundations": table(["Branch", "Feature"], [["Catholicism", "Centered on the papacy and seven sacraments"], ["Protestantism", "Emphasizes scripture and faith over church hierarchy"]]),
        "worked": table(["Event", "Significance"], [["Protestant Reformation", "16th-century movement that reshaped Western Christianity"]]),
        "evidence": table(["Metric", "Insight"], [["Christian population data", "The world's largest religious group by adherents"]]),
        "case_study": table(["Branch", "Region"], [["Eastern Orthodoxy", "Prominent across Eastern Europe and Russia"]]),
        "seminar": table(["Step", "Focus"], [["Comparing Christian branches", "Contrasting Catholic, Protestant, and Orthodox practice"]]),
    },
    {  # 9
        "name": "Islamic Traditions",
        "foundations": table(["Pillar", "Practice"], [["Shahada", "Declaration of faith"], ["Salah", "Five daily prayers"]]),
        "worked": table(["Branch", "Feature"], [["Sunni Islam", "The majority branch, emphasizing consensus tradition"], ["Shia Islam", "Emphasizes the leadership line through Ali"]]),
        "evidence": table(["Metric", "Insight"], [["Muslim population data", "The world's second-largest religious group, growing rapidly"]]),
        "case_study": table(["Practice", "Insight"], [["Hajj pilgrimage", "Draws millions of Muslims to Mecca annually"]]),
        "seminar": table(["Step", "Focus"], [["Researching the Hajj", "Tracing its rituals and historical significance"]]),
    },
    {  # 10
        "name": "East Asian Traditions",
        "foundations": table(["Tradition", "Focus"], [["Confucianism", "Emphasizes social harmony, hierarchy, and ethics"], ["Daoism", "Emphasizes living in harmony with the natural Way"]]),
        "worked": table(["Text", "Focus"], [["Tao Te Ching", "A foundational Daoist text on the nature of the Way"]]),
        "evidence": table(["Metric", "Insight"], [["Practice blending data", "Many East Asian practitioners blend multiple traditions"]]),
        "case_study": table(["Tradition", "Region"], [["Shinto", "Japan's indigenous tradition, often practiced alongside Buddhism"]]),
        "seminar": table(["Step", "Focus"], [["Researching syncretism", "Documenting how two East Asian traditions blend in practice"]]),
    },
    {  # 11
        "name": "African Diasporic Traditions",
        "foundations": table(["Tradition", "Origin"], [["Yoruba religion", "West African tradition centered on orishas"], ["Vodou", "Blends West African and Catholic elements in Haiti"]]),
        "worked": table(["Step", "Example"], [["Tracing syncretism", "Following how enslaved Africans blended traditions with Catholicism"]]),
        "evidence": table(["Metric", "Insight"], [["Practitioner distribution", "Concentrated across the Caribbean, Brazil, and the US"]]),
        "case_study": table(["Tradition", "Region"], [["Santería", "Blends Yoruba orisha worship with Catholic saints in Cuba"]]),
        "seminar": table(["Step", "Focus"], [["Researching a diasporic tradition", "Tracing its West African roots and New World adaptation"]]),
    },
    {  # 12
        "name": "Sacred Texts",
        "foundations": table(["Text", "Tradition"], [["Quran", "Islam"], ["Bible", "Christianity"], ["Vedas", "Hinduism"]]),
        "worked": table(["Step", "Example"], [["Textual analysis", "Examining a passage's historical and literary context"]]),
        "evidence": table(["Metric", "Insight"], [["Translation count data", "Reflects a text's global reach and influence"]]),
        "case_study": table(["Text", "Insight"], [["Dead Sea Scrolls", "Provided major evidence about early biblical text transmission"]]),
        "seminar": table(["Step", "Focus"], [["Comparing translations", "Assessing how translation choices shift a passage's meaning"]]),
    },
    {  # 13
        "name": "Ritual and Practice",
        "foundations": table(["Term", "Meaning"], [["Rite of passage", "A ritual marking transition between life stages"]]),
        "worked": table(["Step", "Example"], [["Analyzing a ritual's structure", "Identifying its separation, transition, and reincorporation phases"]]),
        "evidence": table(["Metric", "Insight"], [["Ritual participation surveys", "Reveal how practice frequency varies across generations"]]),
        "case_study": table(["Ritual", "Tradition"], [["Bar/Bat Mitzvah", "A Jewish coming-of-age ritual"]]),
        "seminar": table(["Step", "Focus"], [["Observing or researching a real rite of passage", "Documenting its stages and symbolic meaning"]]),
    },
    {  # 14
        "name": "Religious Ethics",
        "foundations": table(["Concept", "Example"], [["Golden Rule", "A shared ethical principle appearing across many traditions"]]),
        "worked": table(["Step", "Example"], [["Comparing ethical codes", "Contrasting how two traditions address a shared moral question"]]),
        "evidence": table(["Metric", "Insight"], [["Cross-tradition ethics surveys", "Reveal shared and divergent moral priorities"]]),
        "case_study": table(["Tradition", "Principle"], [["Buddhist ethics", "Centers on reducing suffering through right action"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two traditions' ethical teachings", "Analyzing a shared moral dilemma from each perspective"]]),
    },
    {  # 15
        "name": "Mysticism",
        "foundations": table(["Term", "Meaning"], [["Mysticism", "The pursuit of direct, personal experience of the divine"]]),
        "worked": table(["Tradition", "Example"], [["Sufism", "Islamic mystical tradition emphasizing direct experience of God"]]),
        "evidence": table(["Source", "Use"], [["Mystic writings", "Provide firsthand accounts of transcendent religious experience"]]),
        "case_study": table(["Mystic", "Tradition"], [["Rumi", "A celebrated Sufi poet expressing mystical devotion"]]),
        "seminar": table(["Step", "Focus"], [["Reading mystical poetry", "Analyzing its imagery of divine union"]]),
    },
    {  # 16
        "name": "Religion and Art",
        "foundations": table(["Form", "Example"], [["Iconography", "Christian religious imagery depicting sacred figures"], ["Calligraphy", "Islamic sacred art centered on the written word"]]),
        "worked": table(["Step", "Example"], [["Interpreting sacred art", "Reading symbolism in a religious painting or sculpture"]]),
        "evidence": table(["Source", "Use"], [["Museum collections", "Preserve and contextualize religious artistic heritage"]]),
        "case_study": table(["Work", "Tradition"], [["The Sistine Chapel ceiling", "A major work of Christian devotional art"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a sacred artwork", "Interpreting its religious symbolism and function"]]),
    },
    {  # 17
        "name": "Religion and Politics",
        "foundations": table(["Model", "Feature"], [["State religion", "An officially established faith tied to government"], ["Separation of church and state", "Government neutrality toward religion"]]),
        "worked": table(["Step", "Example"], [["Analyzing church-state relations", "Comparing two countries' legal treatment of religion"]]),
        "evidence": table(["Metric", "Insight"], [["Religious freedom index", "Tracks how governments protect or restrict religious practice"]]),
        "case_study": table(["Country", "Model"], [["United States", "Constitutional separation of church and state"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two church-state models", "Assessing their effect on religious minorities"]]),
    },
    {  # 18
        "name": "Religion and Science",
        "foundations": table(["Model", "Feature"], [["Conflict model", "Views religion and science as fundamentally opposed"], ["Complementary model", "Views them as addressing different kinds of questions"]]),
        "worked": table(["Step", "Example"], [["Analyzing a historical debate", "Examining the Galileo affair's religious and scientific context"]]),
        "evidence": table(["Source", "Use"], [["Survey data on belief", "Shows how religious and scientific views coexist for many people"]]),
        "case_study": table(["Case", "Insight"], [["Evolution debates", "Illustrate ongoing tension in some religious communities"]]),
        "seminar": table(["Step", "Focus"], [["Researching a religion-science debate", "Summarizing the core disagreement and its historical context"]]),
    },
    {  # 19
        "name": "Secularism and Nonreligion",
        "foundations": table(["Term", "Meaning"], [["Secularism", "The principle of separating governance from religious institutions"]]),
        "worked": table(["Step", "Example"], [["Analyzing nonreligious identity", "Distinguishing atheism, agnosticism, and 'nones'"]]),
        "evidence": table(["Metric", "Insight"], [["Religiously unaffiliated population data", "Growing share in many industrialized countries"]]),
        "case_study": table(["Country", "Trend"], [["Northern Europe", "Notably high rates of religious nonaffiliation"]]),
        "seminar": table(["Step", "Focus"], [["Researching secularization trends", "Analyzing survey data from a specific country over time"]]),
    },
    {  # 20
        "name": "Interfaith Dialogue",
        "foundations": table(["Term", "Meaning"], [["Interfaith dialogue", "Cooperative engagement between people of different faiths"]]),
        "worked": table(["Step", "Example"], [["Facilitating dialogue", "Finding shared ethical ground between two traditions"]]),
        "evidence": table(["Metric", "Insight"], [["Interfaith initiative growth", "Reflects increasing cooperative engagement worldwide"]]),
        "case_study": table(["Initiative", "Insight"], [["Parliament of the World's Religions", "A major recurring global interfaith gathering"]]),
        "seminar": table(["Step", "Focus"], [["Researching an interfaith initiative", "Assessing its goals and measurable community impact"]]),
    },
]

MODE_TO_OFFSET = {
    "foundations": 0,
    "worked": 20,
    "evidence": 40,
    "case_study": 60,
    "seminar": 80,
}

CHARTS: dict[str, dict] = {}
for idx, topic in enumerate(TOPICS, start=1):
    for mode, offset in MODE_TO_OFFSET.items():
        lesson_num = idx + offset
        lesson_id = f"world-religions-c1-l{lesson_num}"
        CHARTS[lesson_id] = {"data_table": topic[mode]}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Religions"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json World Religions: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 World Religions lessons (completing 100/100).")


if __name__ == "__main__":
    main()
