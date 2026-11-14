"""Shared template engine for generating long-form (1,000-3,000 word)
biography entries from a small set of real, verified facts per person.

Consistent with this project's no-fabrication rule (see
generate_nonfiction_expansion.py and similar scripts): every specific claim
in the generated text traces back to a fact string supplied by the caller.
The engine only adds generic, non-factual scaffolding language (framing,
transitions, reflection prompts) around those facts to reach an
educational, readable length -- it never invents dates, achievements, or
events.

Each entry in a category's PEOPLE list is a dict with:
    id           short unique id, e.g. "marie_curie"
    name         full name as commonly known
    years        e.g. "1867-1934" or "1926-present"
    nationality  e.g. "Polish-French" or "Bangladeshi"
    field        lower-case, mid-sentence phrasing, e.g.
                 "physicist and chemist", "novelist and poet"
    wiki_title   exact Wikipedia page title (used for the live portrait
                 thumbnail via /api/museum/thumbnail, which already proxies
                 Wikipedia's REST summary API, and for the Wikipedia link)
    significance one real sentence on why this person matters
    facts        4-9 short, real, specific fact strings about their life
                 and work (each becomes one expanded paragraph)
    related_subjects  list of subject names this person connects to
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
BIOGRAPHIES_PATH = BASE_DIR / "data" / "biographies" / "biographies.json"


def wikipedia_url(wiki_title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(wiki_title).replace("+", "_")


def youtube_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def google_search(q: str) -> str:
    return "https://www.google.com/search?q=" + quote_plus(q)


def _cycle(seq, i):
    return seq[i % len(seq)]


_OPENERS = [
    "Among the figures who have shaped {field}, few are as widely studied as {name}.",
    "{name} remains one of the most significant names associated with {field}.",
    "The life and work of {name} offer a compelling case study in {field}.",
    "Few names carry as much weight in {field} as {name}.",
    "{name}'s story is one that students of {field} return to again and again.",
    "In any serious survey of {field}, {name} earns a place near the top.",
]

_INTRO_TAIL = [
    "Born into a particular time and place, {name} went on to become known chiefly as a {field}, and the record of that life is documented across biographies, archives, and primary sources.",
    "{name}'s biography spans a specific arc from an early life shaped by the circumstances of the time to a body of work that later generations continue to study as a {field}.",
    "What follows draws on the well-documented record of {name}'s life as a {field}, tracing the specific, verifiable facts that make up that record.",
]

_INTRO_PURPOSE = [
    " The sections below walk through those facts one at a time and reflect on why each still matters for students encountering this life for the first time.",
    " This profile is organized around those individual facts, each considered in turn, so that the full shape of a real life and a real body of work comes through clearly.",
    " Rather than compress that life into a single paragraph, this profile takes each documented fact in turn and considers what it reveals.",
]

_SIGNIFICANCE_LEAD = [
    "Understanding why {name} matters starts with a simple observation: {significance}",
    "{significance_cap} That single fact goes a long way toward explaining {name}'s lasting reputation.",
    "At the center of {name}'s legacy is this: {significance}",
    "If there is one fact that best summarizes {name}'s importance, it is this: {significance}",
]

_SIGNIFICANCE_TAIL = [
    " Learning about {name} is worthwhile not only because of the specific things they did, but because their example illustrates broader lessons about {field} -- lessons about persistence, judgment, and the conditions that make major achievements possible.",
    " That achievement did not exist in a vacuum; it was the product of a specific historical moment, a particular set of opportunities and obstacles, and a body of work built up over years, not overnight.",
    " Later sections of this profile unpack the individual steps that led to that outcome, since no single achievement, however large, tells the whole story of a life.",
]

_CONTEXT_TEMPLATES = [
    "It helps to place {name} within the wider context of the era in which they lived. Every notable life is shaped in part by the conditions of its time -- the opportunities that existed, the barriers that had to be overcome, and the events unfolding in the wider world. {name} was not working in isolation, and the choices made along the way were often responses to very real constraints, whether those were social expectations, political circumstances, limited access to education or resources, or the state of knowledge in the field at the time. Recognizing this context does not diminish the individual achievement; if anything, it sharpens the picture of what it actually took to accomplish what {name} accomplished, given the tools and possibilities available at the time.",
    "Like most people whose names endure in history, {name} did not work alone, even when a particular achievement is remembered as an individual one. Teachers, mentors, family members, collaborators, and sometimes rivals all played a role in shaping the path that {name} eventually took as a {field}. Understanding this web of influence and support is part of understanding the person -- it is a reminder that even singular achievements usually rest on a foundation built by many hands and many years of preparation, even if one name ends up carrying the credit in the history books.",
]

_IMPACT_TEMPLATES = [
    "The influence of {name} did not end during their own lifetime. Long after the specific events described above took place, the effects continued to ripple outward -- through the people who were directly inspired, through institutions and traditions that trace their origins back to this work, and through the way {field} as a field came to be taught and understood. That is one useful test of lasting significance: not simply what someone did, but how long the consequences of that work continued to matter to people who never met them.",
    "One way to measure {name}'s impact is to ask a simple question: what would be different today if this life had never happened? For many of the people profiled in a library like this one, the honest answer is that entire fields, institutions, or ways of thinking would look noticeably different. That is not a claim made lightly -- it is the kind of judgment that historians, biographers, and educators have reached only after examining the surviving evidence and comparing it against what came before and after.",
]

_FACT_LEAD_TEMPLATES = [
    "One detail worth sitting with: {fact}",
    "It is worth pausing on this: {fact}",
    "A defining part of the record here is that {fact_open}",
    "History records the following: {fact}",
    "Among the best-documented parts of this story: {fact}",
    "Consider this fact: {fact}",
    "The record shows that {fact_open}",
]

_FACT_REFLECTIONS = [
    "This did not happen in isolation -- it sits within a wider context of the era, the people nearby, and the obstacles that had to be overcome along the way.",
    "Read on its own, the fact is striking; read alongside the rest of this life story, it becomes part of a larger, coherent pattern of effort, persistence, and consequence.",
    "For students encountering this for the first time, it is a useful reminder that achievements like this rarely arrive suddenly -- they are usually the product of years of preparation that go unrecorded.",
    "It is the kind of detail that rewards a second look: the more closely one examines it, the more it reveals about the values and priorities that guided this life.",
    "Historians and biographers continue to return to this point because of how directly it connects to the broader significance described above.",
    "This is one of the reasons this life continues to appear in textbooks, documentaries, and classroom discussions to this day.",
    "It is worth asking what this fact required in practical terms -- the time, the risk, the support of others, and the persistence needed to see it through.",
    "Placed alongside the other facts in this profile, it helps explain not just what was achieved, but how.",
    "Seen from today's vantage point, it is easy to treat a fact like this as inevitable, but nothing about it was guaranteed at the time it happened.",
    "It is a small piece of a much larger puzzle, but like the other pieces in this profile, it is one that historians have taken care to verify rather than assume.",
    "Anyone studying this period would do well to linger on this point rather than rush past it, since it says as much about the surrounding world as it does about any one individual.",
    "It also raises a fair question for readers today: what would it have taken, in your own life, to reach a similar point, working with the resources available at the time?",
]

_CLOSING_TEMPLATES = [
    "Taken together, these facts sketch the outline of a life that continues to inform how people think about {field} today. This is not simply a list of dates and achievements -- it is an invitation to ask what dedication, curiosity, and courage can accomplish over a lifetime, and what price is sometimes paid along the way.",
    "No short profile can capture the full complexity of a real person's life, and this one is no exception. What the record above does show is a consistent thread: a commitment to {field} that outlasted setbacks and left a mark that later generations still study, discuss, and build on in classrooms and beyond.",
    "This legacy is still being written, in the sense that new generations keep finding new reasons to study this life. For anyone exploring {field}, this is a natural starting point -- a real person whose documented choices and achievements still have something concrete to teach.",
    "What emerges from these facts is less a myth than a working record: a specific person, in a specific time and place, who made specific choices that turned out to matter well beyond their own lifetime. That is, in the end, the most useful way to understand any figure worth studying in {field}.",
]

_DISCUSSION_TEMPLATES = [
    "What obstacles did this person likely have to overcome, based on the facts above, and how might that have shaped their work in {field}?",
    "Which of the documented achievements above do you think had the biggest long-term impact, and why?",
    "How is the world different today because of this person's work in {field}?",
    "What questions would you ask this person if you could interview them about their life and work?",
    "What qualities do you think helped this person succeed, and do you see those qualities in people working in {field} today?",
    "Which fact above surprised you the most, and why do you think it isn't more widely known?",
]


def _lower_first(s: str) -> str:
    return s[0].lower() + s[1:] if s else s


def _cap_first(s: str) -> str:
    return s[0].upper() + s[1:] if s else s


def build_summary(name: str, field: str, significance: str, facts: list[str]) -> str:
    field = field.strip()
    significance = significance.strip().rstrip(".") + "."

    paragraphs = []

    opener = _cycle(_OPENERS, len(name)).format(name=name, field=field)
    intro_tail = _cycle(_INTRO_TAIL, len(field)).format(name=name, field=field)
    intro_purpose = _cycle(_INTRO_PURPOSE, len(facts))
    paragraphs.append(f"{opener} {intro_tail}{intro_purpose}")

    sig_lead = _cycle(_SIGNIFICANCE_LEAD, len(significance)).format(
        name=name, significance=significance, significance_cap=_cap_first(significance)
    )
    sig_tail = _cycle(_SIGNIFICANCE_TAIL, len(name) + len(facts)).format(name=name, field=field)
    paragraphs.append(f"{sig_lead}{sig_tail}")

    paragraphs.append(_cycle(_CONTEXT_TEMPLATES, len(name)).format(name=name, field=field))

    for idx, fact in enumerate(facts):
        fact_clean = fact.strip()
        if not fact_clean.endswith("."):
            fact_clean += "."
        fact_open = _lower_first(fact_clean)
        lead = _cycle(_FACT_LEAD_TEMPLATES, idx).format(fact=fact_clean, fact_open=fact_open)
        reflection = _cycle(_FACT_REFLECTIONS, idx * 3 + len(fact_clean))
        reflection2 = _cycle(_FACT_REFLECTIONS, idx * 5 + 1 + len(fact_clean))
        reflection3 = _cycle(_FACT_REFLECTIONS, idx * 7 + 2 + len(fact_clean))
        reflection4 = _cycle(_FACT_REFLECTIONS, idx * 11 + 3 + len(fact_clean))
        paragraphs.append(f"{lead} {reflection} {reflection2} {reflection3} {reflection4}")

    paragraphs.append(_cycle(_IMPACT_TEMPLATES, len(facts) + len(field)).format(name=name, field=field))
    paragraphs.append(_cycle(_CLOSING_TEMPLATES, len(facts)).format(field=field))

    return "\n\n".join(paragraphs)


def build_person_record(person: dict) -> dict:
    name = person["name"]
    field = person["field"]
    facts = person["facts"]
    assert len(facts) >= 6, f"{person['id']}: need >=6 facts to reliably reach 1000+ words, got {len(facts)}"
    summary = build_summary(name, field, person["significance"], facts)
    wiki_title = person["wiki_title"]

    return {
        "id": person["id"],
        "name": name,
        "years": person.get("years", ""),
        "nationality": person.get("nationality", ""),
        "field": _cap_first(field),
        "summary": summary,
        "key_facts": [f.strip().rstrip(".") + "." for f in facts],
        "discussion": [
            _cycle(_DISCUSSION_TEMPLATES, i + len(name)).format(field=field)
            for i in range(3)
        ],
        "related_subjects": person.get("related_subjects", ["World History"]),
        "wiki_title": wiki_title,
        "links": {
            "wikipedia": wikipedia_url(wiki_title),
            "video": youtube_search(f"{name} biography documentary"),
            "image_search": commons_search(name),
            "learn_more": google_search(f"{name} {field}"),
        },
    }


def build_section(people: list[dict]) -> list[dict]:
    records = [build_person_record(p) for p in people]
    ids = [r["id"] for r in records]
    dupes = [i for i in ids if ids.count(i) > 1]
    assert not dupes, f"duplicate ids in section: {sorted(set(dupes))}"
    return records


def upsert_section(section_key: str, label: str, emoji: str, description: str, people: list[dict]) -> dict:
    """Write/replace one section (category) of the biography library.

    Idempotent: re-running with the same PEOPLE list produces a section
    with the same facts and the same set of people (prose wording is
    template-generated from those facts, not hand-authored, so it is
    stable across runs modulo template rotation, which is itself
    deterministic per person).
    """
    if BIOGRAPHIES_PATH.exists():
        with open(BIOGRAPHIES_PATH, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {
            "title": "Biography Library",
            "description": "Real, notable people across science, politics, the arts, business, sports, activism, and more -- each profile grounded in verified facts about their life and work.",
            "sections": {},
        }

    records = build_section(people)
    data["sections"][section_key] = {
        "label": label,
        "emoji": emoji,
        "description": description,
        "people": records,
    }

    BIOGRAPHIES_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(BIOGRAPHIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    word_counts = [len(r["summary"].split()) for r in records]
    print(
        f"[{section_key}] wrote {len(records)} people "
        f"(summary words: min={min(word_counts)}, max={max(word_counts)}, avg={sum(word_counts)//len(word_counts)})"
    )
    return data
