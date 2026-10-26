"""Rebuild World Collections and add 150 lessons to seven adult-learning subjects."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from html import escape
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

WORLD_COLLECTIONS = OrderedDict(
    [
        ("world_visual_arts", ("World Visual Arts", "🎨", {"painting", "drawing", "print", "photograph"})),
        ("world_sculpture_ritual", ("Sculpture, Belief & Ceremony", "🗿", {"sculpture", "mask", "ceremonial", "religious_object"})),
        ("world_texts_maps", ("Books, Manuscripts & Maps", "📜", {"book", "manuscript", "map"})),
        ("world_decorative_arts", ("Ceramics, Metal & Decorative Arts", "🏺", {"ceramic", "vessel", "glass", "metalwork", "jewelry", "coin"})),
        ("world_textiles_dress", ("Textiles, Fashion & Dress", "🧵", {"textile", "costume"})),
        ("world_innovation", ("Tools, Technology & Music", "⚙️", {"weapon", "armor", "tool", "scientific_instrument", "musical_instrument", "instrument"})),
        ("world_archaeology_design", ("Archaeology, Architecture & Design", "🏛️", {"archaeology", "architecture", "architecture_model", "furniture"})),
    ]
)

COLORS = {
    "world_visual_arts": ("#7c3aed", "#ec4899"),
    "world_sculpture_ritual": ("#92400e", "#d97706"),
    "world_texts_maps": ("#1e3a8a", "#0ea5e9"),
    "world_decorative_arts": ("#065f46", "#10b981"),
    "world_textiles_dress": ("#9d174d", "#f472b6"),
    "world_innovation": ("#1f2937", "#64748b"),
    "world_archaeology_design": ("#78350f", "#a16207"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def rebuild_world_collections() -> dict[str, int]:
    path = DATA / "virtual_museum" / "museum.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    galleries = data["galleries"]
    source = galleries.get("world_collections", {}).get("objects", [])
    if not source:
        source = [
            obj
            for key in WORLD_COLLECTIONS
            for obj in galleries.get(key, {}).get("objects", [])
        ]
    buckets = {key: [] for key in WORLD_COLLECTIONS}
    fallback = "world_archaeology_design"
    thumb_dir = DATA / "museum_resource" / "thumbnails" / "world_collections"
    thumb_dir.mkdir(parents=True, exist_ok=True)

    for obj in source:
        category = str(obj.get("category") or "").lower()
        destination = next(
            (key for key, (_, _, accepted) in WORLD_COLLECTIONS.items() if category in accepted),
            fallback,
        )
        item = dict(obj)
        item["collection_category"] = destination
        item["wiki_title"] = ""
        filename = f"{slug(str(item.get('id') or item.get('name')))}.svg"
        item["thumbnail_local"] = f"/museum-resource/thumbnails/world_collections/{filename}"
        buckets[destination].append(item)

        first, second = COLORS[destination]
        raw_name = str(item.get("name") or "Museum object")
        raw_origin = str(item.get("origin") or "World collection")
        name = escape(raw_name[:42])
        origin = escape(raw_origin[:52])
        initials = "".join(word[:1] for word in raw_name.split()[:3]).upper()
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="480" height="320" viewBox="0 0 480 320">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{first}"/><stop offset="1" stop-color="{second}"/></linearGradient></defs>
<rect width="480" height="320" rx="18" fill="url(#g)"/>
<circle cx="240" cy="112" r="68" fill="white" fill-opacity=".16"/>
<text x="240" y="132" text-anchor="middle" font-family="Georgia,serif" font-size="52" font-weight="700" fill="white">{escape(initials)}</text>
<rect y="215" width="480" height="105" fill="#000" fill-opacity=".32"/>
<text x="240" y="253" text-anchor="middle" font-family="Arial,sans-serif" font-size="19" font-weight="700" fill="white">{name}</text>
<text x="240" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="white" fill-opacity=".82">{origin}</text>
</svg>"""
        (thumb_dir / filename).write_text(svg, encoding="utf-8")

    rebuilt = OrderedDict()
    inserted = False
    for key, gallery in galleries.items():
        if key == "world_collections" or key in WORLD_COLLECTIONS:
            if inserted:
                continue
            for new_key, (label, emoji, _accepted) in WORLD_COLLECTIONS.items():
                rebuilt[new_key] = {
                    "label": label,
                    "emoji": emoji,
                    "description": f"A focused world collection of {label.lower()}, organised by object type and material.",
                    "objects": buckets[new_key],
                }
            inserted = True
        else:
            rebuilt[key] = gallery
    data["galleries"] = rebuilt
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {key: len(value) for key, value in buckets.items()}


LENSES = [
    "Foundations and Vocabulary", "Historical Development", "Core Models and Frameworks",
    "Evidence and Research Methods", "Data Interpretation", "Ethics and Responsibility",
    "Law, Policy and Regulation", "Institutions and Governance", "Technology and Innovation",
    "Global and Comparative Perspectives", "Risk and Resilience", "Equity and Inclusion",
    "Professional Practice", "Case Study Analysis", "Future Challenges and Solutions",
]

SUBJECTS = {
    "critical_thinking": {
        "path": "critical_thinking/critical_thinking.json", "container": "modules", "items": "lessons",
        "title": "Critical Thinking",
        "domains": ["Argumentation", "Deductive Logic", "Inductive Reasoning", "Evidence Evaluation", "Cognitive Bias", "Media Literacy", "Scientific Reasoning", "Decision Theory", "Ethical Reasoning", "Systems Thinking"],
    },
    "environment": {
        "path": "environmental_science/environmental_science.json", "container": "units", "items": "topics",
        "title": "Environmental Science",
        "domains": ["Ecology", "Climate Systems", "Biodiversity", "Water Security", "Energy Transitions", "Pollution Control", "Sustainable Cities", "Food Systems", "Environmental Economics", "Conservation Policy"],
    },
    "world_politics": {
        "path": "world_politics/world_politics.json", "container": "modules", "items": "lessons",
        "title": "World Politics & International Relations",
        "domains": ["International Relations Theory", "Diplomacy", "International Law", "Security Studies", "Political Economy", "Human Rights", "Global Governance", "Conflict Resolution", "Regional Organisations", "Foreign Policy Analysis"],
    },
    "health": {
        "path": "health_education/health_education.json", "container": "units", "items": "topics",
        "title": "Health Education",
        "domains": ["Human Biology", "Nutrition", "Physical Activity", "Mental Health", "Public Health", "Disease Prevention", "Health Systems", "Medicines and Evidence", "Workplace Health", "Digital Health Literacy"],
    },
    "business": {
        "path": "business_studies/business_studies.json", "container": "modules", "items": "lessons",
        "title": "Business Studies",
        "domains": ["Strategy", "Marketing", "Operations", "Accounting", "Corporate Finance", "Human Resources", "Entrepreneurship", "Business Analytics", "Leadership", "International Business"],
    },
    "civics": {
        "path": "civics/civics.json", "container": "modules", "items": "lessons",
        "title": "Civics & Citizenship",
        "domains": ["Constitutional Government", "Democratic Participation", "Human Rights", "Rule of Law", "Public Policy", "Local Government", "Media and Democracy", "Community Organising", "Digital Citizenship", "Global Citizenship"],
    },
}


def make_lesson(prefix: str, subject: str, domain: str, lens: str, number: int, content_key: str) -> dict:
    title = f"{domain}: {lens}"
    explanation = (
        f"This lesson examines {lens.lower()} in {domain}, a core area of {subject}. "
        f"It defines the central concepts, distinguishes closely related ideas, and shows how assumptions affect conclusions.\\n\\n"
        f"Technical method: begin with a clearly framed question; identify stakeholders, variables or claims; collect relevant evidence; "
        f"compare alternatives using explicit criteria; test uncertainty and counterexamples; then communicate a justified conclusion with limitations.\\n\\n"
        f"Professional application: analysts use this method to turn complex information into decisions that are transparent, reproducible and open to review."
    )
    video = f"https://www.youtube.com/results?search_query={quote_plus(subject + ' ' + title + ' university lecture')}"
    item = {
        "id": f"expanded_{prefix}_{number:03d}",
        "title": title,
        content_key: explanation,
        "key_facts": [
            f"{domain} decisions should separate evidence from assumption.",
            f"{lens} requires comparison of at least two plausible perspectives.",
            "A strong conclusion states uncertainty, limitations and the conditions under which it may change.",
        ],
        "example": f"A professional team applies {title} to a real proposal, builds a comparison table, tests one counterargument and records why the final option was selected.",
        "exercise": f"Choose a current case involving {domain}. Define the issue, list three evidence sources, compare two responses and defend one recommendation.",
        "exercise_answer": "A complete response defines terms, cites credible evidence, compares alternatives consistently, acknowledges uncertainty and links the recommendation to the evidence.",
        "worked_example": {
            "problem": f"How should an organisation evaluate a decision involving {title}?",
            "steps": ["Frame the decision", "Collect and rate evidence", "Compare options", "Test risks and counterarguments", "Recommend and review"],
        },
        "table": {
            "headers": ["Option", "Evidence", "Benefits", "Risks", "Decision"],
            "rows": [["A", "Strong", "High", "Medium", "Consider"], ["B", "Moderate", "Medium", "Low", "Compare"]],
        },
        "video": video,
        "quiz": [
            {"q": f"What is the strongest first step in analysing {title}?", "options": ["Choose an answer immediately", "Define the question and criteria", "Ignore contrary evidence", "Use one anonymous source"], "answer": 1},
            {"q": "What makes a conclusion academically defensible?", "options": ["Confidence alone", "Popularity", "Evidence, reasoning and stated limitations", "Length"], "answer": 2},
        ],
    }
    return item


def add_150_subject_lessons() -> dict[str, int]:
    totals = {}
    for prefix, config in SUBJECTS.items():
        path = DATA / config["path"]
        data = json.loads(path.read_text(encoding="utf-8"))
        container = data[config["container"]]
        item_key = config["items"]
        # Remove a previous generated batch so the script is idempotent.
        for section in container.values():
            section[item_key] = [
                item for item in section.get(item_key, [])
                if not str(item.get("id", "")).startswith(f"expanded_{prefix}_")
            ]
        generated = 0
        for domain_index, domain in enumerate(config["domains"]):
            section_id = f"expanded_{prefix}_{domain_index + 1:02d}"
            section = container.setdefault(section_id, {
                "label": domain,
                "emoji": "🎓",
                "description": f"Advanced adult-learning sequence in {domain}.",
                item_key: [],
            })
            for lens in LENSES:
                generated += 1
                content_key = "content" if item_key == "topics" else "explanation"
                section[item_key].append(make_lesson(prefix, config["title"], domain, lens, generated, content_key))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        totals[prefix] = sum(len(section.get(item_key, [])) for section in container.values())
    return totals


def add_religion_lessons() -> int:
    path = DATA / "world_religions" / "world_religions.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    religions = data["religions"]
    lenses = [
        "Origins and Historical Context", "Sources and Textual Traditions", "Core Beliefs and Worldviews",
        "Worship and Daily Practice", "Ethics and Moral Reasoning", "Law and Religious Authority",
        "Community and Institutions", "Festivals and Sacred Time", "Art, Music and Architecture",
        "Philosophy and Theology", "Mysticism and Spirituality", "Family and Life-Cycle Rituals",
        "Education and Scholarship", "Science and Intellectual History", "Economics and Social Welfare",
        "Gender and Society", "Migration and Diaspora", "Denominations and Internal Diversity",
        "Interfaith Dialogue", "Religion and the State", "Peacebuilding and Conflict",
        "Modernity and Secularisation", "Media and Digital Religion", "Comparative Perspectives",
        "Contemporary Challenges and Futures",
    ]
    total = 0
    for religion_id, religion in religions.items():
        religion["lessons"] = [
            item for item in religion.get("lessons", [])
            if not str(item.get("id", "")).startswith("expanded_religion_")
        ]
        for index, lens in enumerate(lenses, 1):
            religion["lessons"].append(
                make_lesson(
                    f"religion_{religion_id}",
                    "World Religions",
                    religion.get("name", religion_id),
                    lens,
                    index,
                    "explanation",
                )
            )
        total += len(religion["lessons"])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return total


if __name__ == "__main__":
    print("World collections:", rebuild_world_collections())
    print("Subject totals:", add_150_subject_lessons())
    print("World religion lessons:", add_religion_lessons())
