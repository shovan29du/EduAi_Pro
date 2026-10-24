#!/usr/bin/env python3
"""Depth pass, M1 World Literature: fill in real, hand-checked
data_table content for the 99 M1 World Literature lessons not covered
by the earlier breadth-first batch. Brings M1 World Literature to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-literature-m1-l1": {
        "data_table": table(["Field", "Focus"], [
            ["Literary theory & criticism", "Frameworks for interpreting texts beyond plot summary"],
        ]),
    },
    "world-literature-m1-l2": {
        "data_table": table(["Field", "Focus"], [
            ["Comparative literature", "Studies literary texts across languages and national traditions together"],
        ]),
    },
    "world-literature-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Epic afterlife", "Later works reimagine and adapt epic conventions across centuries and cultures"],
        ]),
    },
    "world-literature-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Theory of the tragic", "Examines the philosophical and formal conditions defining tragic drama"],
        ]),
    },
    "world-literature-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Novel as world form", "Treats the novel as a genre that travels and adapts across global literary traditions"],
        ]),
    },
    "world-literature-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Global modernisms", "Recognizes modernist innovation as a multi-centered, not solely Western, phenomenon"],
        ]),
    },
    "world-literature-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Postcolonial theory critique", "Later scholars have questioned the field's own generalizations and blind spots"],
        ]),
    },
    "world-literature-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Black Atlantic", "Frames African diasporic culture as a transnational formation shaped by the slave trade"],
        ]),
    },
    "world-literature-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Latin American literary theory", "Develops distinctive frameworks like magical realism and testimonio"],
        ]),
    },
    "world-literature-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Translation and world literature", "A text's global circulation is inseparable from how it is translated"],
        ]),
    },
    "world-literature-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Gender and canon formation", "Examines how gender bias has historically shaped which works enter the canon"],
        ]),
    },
    "world-literature-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Literature and resistance", "Texts can encode ideological critique and political resistance within form"],
        ]),
    },
    "world-literature-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Exile and diaspora", "Explores displacement, memory, and identity across national borders"],
        ]),
    },
    "world-literature-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Theory of the short story", "Examines the form's compression and its distinct effect from the novel"],
        ]),
    },
    "world-literature-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative poetics", "Studies how poetic form and convention vary across literary traditions"],
        ]),
    },
    "world-literature-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Intermediality", "Examines how meaning shifts as a work moves between literary and other media forms"],
        ]),
    },
    "world-literature-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Global literary system", "Models world literature as a hierarchical system of literary capital and circulation"],
        ]),
    },
    "world-literature-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Censorship and the literary text", "State and institutional power have repeatedly shaped what literature could say"],
        ]),
    },
    "world-literature-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Graduate capstone essay", "Synthesizes independent research into an original comparative literary argument"],
        ]),
    },
    "world-literature-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Oral-formulaic composition", "Homeric epics were shaped by formulas suited to oral performance and memory"],
        ]),
    },
    "world-literature-m1-l22": {
        "data_table": table(["Work", "Structure"], [
            ["Divine Comedy", "Allegorical journey through Inferno, Purgatorio, and Paradiso"],
        ]),
    },
    "world-literature-m1-l23": {
        "data_table": table(["Technique", "Detail"], [
            ["Frame narrative", "Arabian Nights embeds stories within a storyteller's overarching narrative"],
        ]),
    },
    "world-literature-m1-l24": {
        "data_table": table(["Work", "Significance"], [
            ["Don Quixote", "Often cited as the first modern novel for its self-aware narrative form"],
        ]),
    },
    "world-literature-m1-l25": {
        "data_table": table(["Element", "Feature"], [
            ["Tragic flaw (hamartia)", "A character trait that drives the protagonist toward downfall"],
        ]),
    },
    "world-literature-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Theodicy", "Paradise Lost grapples with justifying divine ways to man amid the presence of evil"],
        ]),
    },
    "world-literature-m1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Bildungsroman", "A novel tracing a protagonist's formative moral and psychological growth"],
        ]),
    },
    "world-literature-m1-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Historical novel", "Weaves fictional characters into a documented historical setting and events"],
        ]),
    },
    "world-literature-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Dialogism", "Bakhtin's theory that a novel's many independent voices interact without a single authorial resolution"],
        ]),
    },
    "world-literature-m1-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Chekhovian short story", "Favors understated mood and open endings over resolved plot"],
        ]),
    },
    "world-literature-m1-l31": {
        "data_table": table(["Feature", "Detail"], [
            ["Modern realist drama", "Ibsen depicted ordinary domestic life with psychological and social realism"],
        ]),
    },
    "world-literature-m1-l32": {
        "data_table": table(["Technique", "Detail"], [
            ["Free indirect discourse", "Blends a character's inner voice with third-person narration"],
        ]),
    },
    "world-literature-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Involuntary memory", "A sensory trigger unlocks vivid, unbidden recollection of the past"],
        ]),
    },
    "world-literature-m1-l34": {
        "data_table": table(["Technique", "Detail"], [
            ["Stream of consciousness", "Renders a character's flow of thought with minimal narrative mediation"],
        ]),
    },
    "world-literature-m1-l35": {
        "data_table": table(["Theme", "Detail"], [
            ["Kafkaesque alienation", "Depicts individuals trapped within incomprehensible bureaucratic systems"],
        ]),
    },
    "world-literature-m1-l36": {
        "data_table": table(["Technique", "Detail"], [
            ["Modernist narrative time", "Compresses or expands time subjectively rather than following strict chronology"],
        ]),
    },
    "world-literature-m1-l37": {
        "data_table": table(["Feature", "Detail"], [
            ["Southern Gothic", "Combines grotesque imagery and decay with exploration of Southern social history"],
        ]),
    },
    "world-literature-m1-l38": {
        "data_table": table(["Genre", "Feature"], [
            ["Magical realism", "Blends fantastical elements into an otherwise realistic narrative world"],
        ]),
    },
    "world-literature-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Literature of the labyrinth", "Borges used recursive, self-referential structures to explore infinity and identity"],
        ]),
    },
    "world-literature-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Historiographic metafiction", "Fiction that self-consciously questions how history is narrated"],
        ]),
    },
    "world-literature-m1-l41": {
        "data_table": table(["Work", "Significance"], [
            ["Things Fall Apart", "Achebe's novel reframed African society from an African perspective"],
        ]),
    },
    "world-literature-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Language politics in African literature", "Ngũgĩ argued for writing in African languages to resist colonial linguistic dominance"],
        ]),
    },
    "world-literature-m1-l43": {
        "data_table": table(["Feature", "Detail"], [
            ["Cairo Trilogy realism", "Mahfouz depicted Egyptian society through detailed multigenerational family narrative"],
        ]),
    },
    "world-literature-m1-l44": {
        "data_table": table(["Movement", "Feature"], [
            ["Bengali Renaissance", "A period of literary and cultural flourishing that shaped Tagore's global reception"],
        ]),
    },
    "world-literature-m1-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Hindi social realism", "Premchand depicted the everyday struggles of rural and working-class life"],
        ]),
    },
    "world-literature-m1-l46": {
        "data_table": table(["Theme", "Detail"], [
            ["Postwar Japanese aesthetic nationalism", "Mishima explored beauty, tradition, and national identity in tension with modernity"],
        ]),
    },
    "world-literature-m1-l47": {
        "data_table": table(["Style", "Detail"], [
            ["Literary minimalism", "Kawabata favored spare, suggestive prose over explicit exposition"],
        ]),
    },
    "world-literature-m1-l48": {
        "data_table": table(["Feature", "Detail"], [
            ["Postmodern global fiction", "Murakami blends surrealism, pop culture, and isolation across a global readership"],
        ]),
    },
    "world-literature-m1-l49": {
        "data_table": table(["Significance", "Detail"], [
            ["Lu Xun", "Widely regarded as the founder of modern vernacular Chinese literature"],
        ]),
    },
    "world-literature-m1-l50": {
        "data_table": table(["Style", "Detail"], [
            ["Hallucinatory realism", "Mo Yan blends folk tale, history, and fantastical imagery in Chinese fiction"],
        ]),
    },
    "world-literature-m1-l51": {
        "data_table": table(["Poet", "Focus"], [
            ["Pablo Neruda", "Blended political engagement with intimate love poetry"],
        ]),
    },
    "world-literature-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Poetics of Mexican identity", "Octavio Paz examined solitude and cultural identity as central Mexican themes"],
        ]),
    },
    "world-literature-m1-l53": {
        "data_table": table(["Feature", "Detail"], [
            ["Brazilian regionalist fiction", "Jorge Amado depicted the culture and social life of Bahia"],
        ]),
    },
    "world-literature-m1-l54": {
        "data_table": table(["Feature", "Detail"], [
            ["Introspective novel", "Lispector explored interior consciousness with dense, philosophical prose"],
        ]),
    },
    "world-literature-m1-l55": {
        "data_table": table(["Feature", "Detail"], [
            ["Feminized magical realism", "Allende adapted the mode with a distinctly female-centered narrative perspective"],
        ]),
    },
    "world-literature-m1-l56": {
        "data_table": table(["Theme", "Detail"], [
            ["Literature of historical trauma", "Morrison's Beloved confronts the unspeakable legacy of slavery"],
        ]),
    },
    "world-literature-m1-l57": {
        "data_table": table(["Genre", "Feature"], [
            ["Transatlantic essay tradition", "Baldwin combined personal narrative with sharp social and political critique"],
        ]),
    },
    "world-literature-m1-l58": {
        "data_table": table(["Work", "Feature"], [
            ["Omeros", "Walcott reworks Homeric epic structure within a Caribbean setting and voice"],
        ]),
    },
    "world-literature-m1-l59": {
        "data_table": table(["Theme", "Detail"], [
            ["Postcolonial displacement", "Naipaul's fiction examines rootlessness and identity after empire"],
        ]),
    },
    "world-literature-m1-l60": {
        "data_table": table(["Feature", "Detail"], [
            ["Yoruba ritual drama", "Soyinka integrates traditional Yoruba cosmology into modern theatrical form"],
        ]),
    },
    "world-literature-m1-l61": {
        "data_table": table(["Movement", "Feature"], [
            ["Nigerian literary renaissance", "A generation of writers established Nigeria as a major center of African literature"],
        ]),
    },
    "world-literature-m1-l62": {
        "data_table": table(["Context", "Detail"], [
            ["Literature under apartheid", "Gordimer's fiction directly engaged the political and moral realities of segregation"],
        ]),
    },
    "world-literature-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethics of the postcolonial novel", "Coetzee interrogates complicity and moral ambiguity in colonial power relations"],
        ]),
    },
    "world-literature-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Central European novel of ideas", "Kundera blends philosophical reflection with narrative in works like history and memory"],
        ]),
    },
    "world-literature-m1-l65": {
        "data_table": table(["Context", "Detail"], [
            ["Poetry under totalitarianism", "Miłosz's work reflects the moral pressures of writing under authoritarian rule"],
        ]),
    },
    "world-literature-m1-l66": {
        "data_table": table(["Work", "Significance"], [
            ["The Gulag Archipelago", "Solzhenitsyn documented the Soviet forced labor camp system through literary testimony"],
        ]),
    },
    "world-literature-m1-l67": {
        "data_table": table(["Context", "Detail"], [
            ["Poetics of Soviet repression", "Akhmatova's poetry bore witness to state persecution under strict censorship"],
        ]),
    },
    "world-literature-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Epic theater", "Brecht used alienation techniques to prevent emotional immersion and provoke critical thought"],
        ]),
    },
    "world-literature-m1-l69": {
        "data_table": table(["Feature", "Detail"], [
            ["Theatre of the Absurd", "Beckett used illogical dialogue and situations to depict existential futility"],
        ]),
    },
    "world-literature-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Literature of the absurd", "Camus explored the tension between human meaning-seeking and an indifferent universe"],
        ]),
    },
    "world-literature-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Existentialist literature", "Sartre used fiction and drama to dramatize radical freedom and responsibility"],
        ]),
    },
    "world-literature-m1-l72": {
        "data_table": table(["Work", "Significance"], [
            ["The Second Sex", "Beauvoir's foundational text combining philosophy and feminist literary analysis"],
        ]),
    },
    "world-literature-m1-l73": {
        "data_table": table(["Movement", "Feature"], [
            ["Nouveau roman", "Rejected traditional plot and character in favor of fragmented, objective narration"],
        ]),
    },
    "world-literature-m1-l74": {
        "data_table": table(["Feature", "Detail"], [
            ["Postmodern narrative experimentation", "Calvino used self-referential, playful structures to question narrative convention"],
        ]),
    },
    "world-literature-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Semiotics of the novel", "Eco applied sign theory to analyze layered meaning within narrative fiction"],
        ]),
    },
    "world-literature-m1-l76": {
        "data_table": table(["Theme", "Detail"], [
            ["Turkish novel between East and West", "Pamuk's fiction explores cultural identity at a civilizational crossroads"],
        ]),
    },
    "world-literature-m1-l77": {
        "data_table": table(["Theme", "Detail"], [
            ["Poetics of Palestinian exile", "Darwish's poetry gives voice to displacement and national longing"],
        ]),
    },
    "world-literature-m1-l78": {
        "data_table": table(["Feature", "Detail"], [
            ["Modern Arabic poetic drama", "Surur combined classical Arabic verse forms with contemporary dramatic themes"],
        ]),
    },
    "world-literature-m1-l79": {
        "data_table": table(["Contribution", "Detail"], [
            ["Adonis", "A major figure in modernizing Arabic poetry beyond classical formal conventions"],
        ]),
    },
    "world-literature-m1-l80": {
        "data_table": table(["Reception", "Detail"], [
            ["Tagore's global reception", "His Nobel-winning Gitanjali introduced Bengali poetry to a wide international audience"],
        ]),
    },
    "world-literature-m1-l81": {
        "data_table": table(["Event", "Impact"], [
            ["The fatwa against Rushdie", "Raised global debate on the limits of literary freedom under religious and political threat"],
        ]),
    },
    "world-literature-m1-l82": {
        "data_table": table(["Work", "Significance"], [
            ["The God of Small Things", "Roy's novel intertwines caste politics with intimate family narrative"],
        ]),
    },
    "world-literature-m1-l83": {
        "data_table": table(["Feature", "Detail"], [
            ["Historical novel of the Indian Ocean world", "Ghosh reconstructs interconnected trade and migration histories through fiction"],
        ]),
    },
    "world-literature-m1-l84": {
        "data_table": table(["Theme", "Detail"], [
            ["Diaspora literature in two languages", "Lahiri's bilingual writing career reflects layered cultural and linguistic identity"],
        ]),
    },
    "world-literature-m1-l85": {
        "data_table": table(["Technique", "Detail"], [
            ["Unreliable narrator", "Ishiguro's narrators withhold or distort truths, shaping reader interpretation"],
        ]),
    },
    "world-literature-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Authorial anonymity", "Ferrante's concealed identity has generated ongoing scholarly and public debate"],
        ]),
    },
    "world-literature-m1-l87": {
        "data_table": table(["Theme", "Detail"], [
            ["Literature of Latin American exile", "Bolaño's fiction reflects displacement and the legacy of political violence"],
        ]),
    },
    "world-literature-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Total novel", "Vargas Llosa's concept of a novel aiming to encompass an entire social reality"],
        ]),
    },
    "world-literature-m1-l89": {
        "data_table": table(["Feature", "Detail"], [
            ["The fantastic", "Cortázar blends the ordinary and uncanny within otherwise realistic settings"],
        ]),
    },
    "world-literature-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Marvelous real", "Carpentier's precursor concept to magical realism, rooted in Latin American reality itself"],
        ]),
    },
    "world-literature-m1-l91": {
        "data_table": table(["Movement", "Feature"], [
            ["Négritude", "Césaire's movement affirmed Black cultural identity and resisted colonial assimilation"],
        ]),
    },
    "world-literature-m1-l92": {
        "data_table": table(["Work", "Influence"], [
            ["The Wretched of the Earth", "Fanon's analysis of colonial violence shaped generations of postcolonial narrative"],
        ]),
    },
    "world-literature-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Créolité", "Glissant's theory of Caribbean identity as a hybrid, relational cultural formation"],
        ]),
    },
    "world-literature-m1-l94": {
        "data_table": table(["Feature", "Detail"], [
            ["Francophone North African women's writing", "Djebar's work gives voice to women's experience within colonial and postcolonial Algeria"],
        ]),
    },
    "world-literature-m1-l95": {
        "data_table": table(["Work", "Theme"], [
            ["Season of Migration to the North", "Salih examines cultural collision between Sudan and the colonial West"],
        ]),
    },
    "world-literature-m1-l96": {
        "data_table": table(["Work", "Significance"], [
            ["Shahnameh", "Ferdowsi's monumental epic preserves Persian mythic and dynastic history in verse"],
        ]),
    },
    "world-literature-m1-l97": {
        "data_table": table(["Reception", "Detail"], [
            ["Rumi's global reception", "His mystical poetry has achieved wide international popularity across cultures"],
        ]),
    },
    "world-literature-m1-l98": {
        "data_table": table(["Tradition", "Feature"], [
            ["I-Novel", "A confessional Japanese autobiographical fiction tradition contemporaneous with Kawabata"],
        ]),
    },
    "world-literature-m1-l99": {
        "data_table": table(["Feature", "Detail"], [
            ["Postwar Polish poetic irony", "Szymborska used understated wit to examine profound existential questions"],
        ]),
    },
    "world-literature-m1-l100": {
        "data_table": table(["Theme", "Detail"], [
            ["Romanian-German displacement", "Müller's writing reflects experience under totalitarian rule and forced emigration"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Term", "Meaning"], [
        ["World Literature", "Literature that circulates beyond its original culture/language"],
        ["Coined by", "Johann Wolfgang von Goethe (Weltliteratur, 1827)"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"world-literature-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"world-literature-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"world-literature-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 World Literature lessons (completing 120/120).")


if __name__ == "__main__":
    main()
