#!/usr/bin/env python3
"""Depth pass, C2 World Literature: fill in real, hand-checked data_table
content for the 69 C2 World Literature lessons not covered by the
earlier breadth-first batch. Brings C2 World Literature to full 70/70
coverage.

l61 is a "Foundations 2" lesson revisiting l28; l62-l70 are "Worked
Analysis" companions to l1-l9. l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-literature-c2-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Modern & contemporary literature", "Spans realism through experimental and globalized 21st-century writing"],
        ]),
    },
    "world-literature-c2-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Literary theory & criticism", "Frameworks for interpreting texts beyond plot summary"],
        ]),
    },
    "world-literature-c2-l4": {
        "data_table": table(["Epic", "Origin"], [
            ["Mahabharata", "Ancient Sanskrit epic centered on a dynastic war and questions of duty"],
            ["Ramayana", "Ancient Sanskrit epic recounting Rama's exile and quest to rescue Sita"],
        ]),
    },
    "world-literature-c2-l5": {
        "data_table": table(["Concept", "Meaning"], [
            ["Catharsis", "Emotional release Aristotle argued tragedy produces in an audience"],
        ]),
    },
    "world-literature-c2-l6": {
        "data_table": table(["Author", "Contribution"], [
            ["Charles Dickens", "Depicted industrial-era social conditions through serialized novels"],
        ]),
    },
    "world-literature-c2-l7": {
        "data_table": table(["Technique", "Example Author"], [
            ["Stream of consciousness", "Virginia Woolf, James Joyce"],
        ]),
    },
    "world-literature-c2-l8": {
        "data_table": table(["Work", "Significance"], [
            ["Things Fall Apart", "Chinua Achebe's novel reframed African society from an African perspective"],
        ]),
    },
    "world-literature-c2-l9": {
        "data_table": table(["Movement", "Feature"], [
            ["Harlem Renaissance", "1920s flourishing of African American literature, music, and art in New York"],
        ]),
    },
    "world-literature-c2-l10": {
        "data_table": table(["Genre", "Feature"], [
            ["Magical realism", "Blends fantastical elements into an otherwise realistic narrative world"],
        ]),
    },
    "world-literature-c2-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Translation loss", "Idiom, rhythm, and cultural nuance often resist exact translation"],
        ]),
    },
    "world-literature-c2-l12": {
        "data_table": table(["Issue", "Detail"], [
            ["Authorship question", "Early women writers often published anonymously or under male pseudonyms"],
        ]),
    },
    "world-literature-c2-l13": {
        "data_table": table(["Movement", "Literary Response"], [
            ["Anti-colonial movements", "Writers used fiction and poetry to challenge colonial narratives"],
        ]),
    },
    "world-literature-c2-l14": {
        "data_table": table(["Theme", "Detail"], [
            ["Immigrant narrative", "Explores displacement, identity, and belonging across cultures"],
        ]),
    },
    "world-literature-c2-l15": {
        "data_table": table(["Feature", "Detail"], [
            ["19th-century short story", "Compact form suited to magazine publication and a single dramatic effect"],
        ]),
    },
    "world-literature-c2-l16": {
        "data_table": table(["Form", "Origin"], [
            ["Ghazal", "Arabic/Persian lyric form on love and longing"],
            ["Haiku", "Japanese three-line form capturing a single moment"],
        ]),
    },
    "world-literature-c2-l17": {
        "data_table": table(["Process", "Consideration"], [
            ["Adapting a novel for theater", "Compresses narrative into dialogue and stage-viable action"],
        ]),
    },
    "world-literature-c2-l18": {
        "data_table": table(["Factor", "Effect"], [
            ["Global literary marketplace", "Translation and marketing decisions shape which books reach wide audiences"],
        ]),
    },
    "world-literature-c2-l19": {
        "data_table": table(["Reason", "Example"], [
            ["Political/religious content", "Books banned for challenging prevailing authority or social norms"],
        ]),
    },
    "world-literature-c2-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Comparative reading capstone", "Synthesize thematic and formal comparison across two novels"],
        ]),
    },
    "world-literature-c2-l21": {
        "data_table": table(["Work", "Structure"], [
            ["Divine Comedy", "Allegorical journey through Inferno, Purgatorio, and Paradiso"],
        ]),
    },
    "world-literature-c2-l22": {
        "data_table": table(["Work", "Significance"], [
            ["Don Quixote", "Often cited as the first modern novel for its self-aware narrative form"],
        ]),
    },
    "world-literature-c2-l23": {
        "data_table": table(["Element", "Feature"], [
            ["Tragic flaw (hamartia)", "A character trait that drives the protagonist toward downfall"],
        ]),
    },
    "world-literature-c2-l24": {
        "data_table": table(["Poet", "Style"], [
            ["Li Bai", "Romantic, imaginative Tang-era verse"],
            ["Du Fu", "Socially conscious, historically grounded Tang-era verse"],
        ]),
    },
    "world-literature-c2-l25": {
        "data_table": table(["Work", "Feature"], [
            ["The Tale of Genji", "Often considered the world's first novel, noted for psychological depth"],
        ]),
    },
    "world-literature-c2-l26": {
        "data_table": table(["Technique", "Detail"], [
            ["Frame narrative", "Arabian Nights embeds stories within a storyteller's overarching narrative"],
        ]),
    },
    "world-literature-c2-l27": {
        "data_table": table(["Author", "Focus"], [
            ["Tolstoy", "Explores history and moral choice on a broad social canvas"],
            ["Dostoevsky", "Explores psychological and existential extremity"],
        ]),
    },
    "world-literature-c2-l28": {
        "data_table": table(["Poet", "Contribution"], [
            ["Baudelaire", "Explored urban modernity and beauty in decay"],
            ["Mallarmé", "Emphasized suggestion and musicality of language over direct statement"],
        ]),
    },
    "world-literature-c2-l29": {
        "data_table": table(["Form", "Meaning"], [
            ["Bildungsroman", "A novel tracing a protagonist's formative moral and psychological growth"],
        ]),
    },
    "world-literature-c2-l30": {
        "data_table": table(["Convention", "Purpose"], [
            ["Gothic convention", "Uses decay, the uncanny, and confinement to externalize cultural anxiety"],
        ]),
    },
    "world-literature-c2-l31": {
        "data_table": table(["Feature", "Detail"], [
            ["Romanticism", "Emphasized emotion, nature, and individualism across national literatures"],
        ]),
    },
    "world-literature-c2-l32": {
        "data_table": table(["Author", "Critique"], [
            ["Victorian novelists", "Used fiction to critique industrial inequality and social convention"],
        ]),
    },
    "world-literature-c2-l33": {
        "data_table": table(["Movement", "Feature"], [
            ["Naturalism", "Applied a deterministic, quasi-scientific lens to depicting human behavior"],
        ]),
    },
    "world-literature-c2-l34": {
        "data_table": table(["Author", "Theme"], [
            ["Franz Kafka", "Depicted alienating, incomprehensible bureaucratic systems"],
        ]),
    },
    "world-literature-c2-l35": {
        "data_table": table(["Author", "Focus"], [
            ["Camus", "The absurd and the individual's response to a meaningless universe"],
            ["Sartre", "Radical freedom and existential responsibility"],
        ]),
    },
    "world-literature-c2-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Theater of the Absurd", "Uses illogical dialogue and situations to depict existential futility"],
        ]),
    },
    "world-literature-c2-l37": {
        "data_table": table(["Figure", "Contribution"], [
            ["Rabindranath Tagore", "Bridged Bengali and world literary traditions, first non-European Nobel laureate in literature"],
        ]),
    },
    "world-literature-c2-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Créolité", "Caribbean literary movement affirming hybrid, creole cultural identity"],
        ]),
    },
    "world-literature-c2-l39": {
        "data_table": table(["Region", "Example"], [
            ["Magical realism beyond Latin America", "Practiced by writers across Africa, South Asia, and elsewhere"],
        ]),
    },
    "world-literature-c2-l40": {
        "data_table": table(["Poet", "Focus"], [
            ["Pablo Neruda", "Blended political engagement with intimate love poetry"],
        ]),
    },
    "world-literature-c2-l41": {
        "data_table": table(["Theme", "Detail"], [
            ["South Asian diaspora fiction", "Explores dual identity and cultural negotiation abroad"],
        ]),
    },
    "world-literature-c2-l42": {
        "data_table": table(["Era", "Focus"], [
            ["Post-independence West African literature", "Addresses nation-building and postcolonial disillusionment"],
        ]),
    },
    "world-literature-c2-l43": {
        "data_table": table(["Concern", "Detail"], [
            ["Holocaust literature", "Grapples with the limits and ethics of representing atrocity"],
        ]),
    },
    "world-literature-c2-l44": {
        "data_table": table(["Genre", "Feature"], [
            ["Testimonio", "First-person witness narrative documenting political violence or injustice"],
        ]),
    },
    "world-literature-c2-l45": {
        "data_table": table(["Movement", "Goal"], [
            ["Decolonizing the canon", "Expands literary study beyond a Eurocentric set of texts"],
        ]),
    },
    "world-literature-c2-l46": {
        "data_table": table(["Field", "Focus"], [
            ["Queer theory", "Examines how texts construct and challenge norms of gender and sexuality"],
        ]),
    },
    "world-literature-c2-l47": {
        "data_table": table(["Challenge", "Detail"], [
            ["Translating children's literature", "Must balance cultural specificity with accessibility for young readers"],
        ]),
    },
    "world-literature-c2-l48": {
        "data_table": table(["Genre", "Function"], [
            ["Speculative fiction", "Uses imagined futures or worlds to comment on present social issues"],
        ]),
    },
    "world-literature-c2-l49": {
        "data_table": table(["Region", "Adaptation"], [
            ["Global detective fiction", "Adapts the genre's conventions to distinct cultural and legal contexts"],
        ]),
    },
    "world-literature-c2-l50": {
        "data_table": table(["Era", "Focus"], [
            ["War narrative", "Shifted from heroic framing toward depicting trauma and moral ambiguity"],
        ]),
    },
    "world-literature-c2-l51": {
        "data_table": table(["Question", "Detail"], [
            ["Ethics of memoir", "Raises questions of memory accuracy, consent, and representing others"],
        ]),
    },
    "world-literature-c2-l52": {
        "data_table": table(["Critique", "Detail"], [
            ["Realism's discontents", "Some global novelists reject realism as inadequate to lived experience"],
        ]),
    },
    "world-literature-c2-l53": {
        "data_table": table(["Form", "Feature"], [
            ["Graphic novel", "Combines visual and textual narrative as a distinct literary form"],
        ]),
    },
    "world-literature-c2-l54": {
        "data_table": table(["Process", "Detail"], [
            ["Transcription of oral epics", "Converting spoken tradition to written text raises questions of fidelity"],
        ]),
    },
    "world-literature-c2-l55": {
        "data_table": table(["Author", "Technique"], [
            ["Woolf", "Fluid, interior stream-of-consciousness narration"],
            ["Joyce", "Dense, allusive, formally experimental prose"],
        ]),
    },
    "world-literature-c2-l56": {
        "data_table": table(["Strategy", "Detail"], [
            ["Postmodern narrative", "Employs fragmentation, metafiction, and unreliable narration"],
        ]),
    },
    "world-literature-c2-l57": {
        "data_table": table(["Factor", "Effect"], [
            ["Publishing and reception", "Marketing and translator visibility shape how foreign fiction is received"],
        ]),
    },
    "world-literature-c2-l58": {
        "data_table": table(["Force", "Effect"], [
            ["Literary prizes", "Shape canon formation by conferring visibility and prestige"],
        ]),
    },
    "world-literature-c2-l59": {
        "data_table": table(["Approach", "Detail"], [
            ["Comparative national canons", "Examines how different nations construct their own literary traditions"],
        ]),
    },
    "world-literature-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone seminar", "Synthesizes literature's role in global cultural exchange"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Comparative Approach", "Focus"], [
    ["Thematic comparison", "Shared themes across texts"],
    ["Formal comparison", "Shared structures/techniques across texts"],
])

# l61 "Foundations 2" lesson revisits l28.
CHARTS["world-literature-c2-l61"] = {
    "data_table": CHARTS["world-literature-c2-l28"]["data_table"],
}

# l62-l70 "Worked Analysis" lessons reuse the data_table of l1-l9.
WORKED_ANALYSIS_MAP = {62: 1, 63: 2, 64: 3, 65: 4, 66: 5, 67: 6, 68: 7, 69: 8, 70: 9}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"world-literature-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"world-literature-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"world-literature-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 World Literature lessons (completing 70/70).")


if __name__ == "__main__":
    main()
