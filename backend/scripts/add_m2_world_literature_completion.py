#!/usr/bin/env python3
"""Depth pass, M2 World Literature: fill in real, hand-checked
data_table content for the M2 World Literature lessons not covered
by the earlier breadth-first batch. Brings M2 World Literature to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning literary
theory (Bakhtin, postcolonial theory, narratology), major world
authors and movements across regions, and comparative
literature/translation studies; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Dialogism", "Bakhtin's theory that a novel's meaning emerges from interacting, unmerged character voices"],
    ["Polyphonic novel", "A novel (like Dostoevsky's) featuring genuinely independent character perspectives, not one authorial voice"],
])

CHARTS: dict[str, dict] = {
    "world-literature-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Comparative literature research methods", "Systematic scholarly approaches for studying literature across languages and cultures"],
    ])},
    "world-literature-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Classic world literature research", "Rigorous scholarly methods for studying canonical works across global traditions"],
    ])},
    "world-literature-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Chronotope", "Bakhtin's term for how time and space are fused and represented within a narrative"],
    ])},
    "world-literature-m2-l5": {"data_table": table(["Scholar", "Contribution"], [
        ["Auerbach (Mimesis)", "Traced how Western literature's techniques for representing reality evolved across eras"],
    ])},
    "world-literature-m2-l6": {"data_table": table(["Scholar", "Contribution"], [
        ["Said (Orientalism)", "Argued Western representations of the East reflect and reinforce colonial power structures"],
    ])},
    "world-literature-m2-l7": {"data_table": table(["Scholar", "Contribution"], [
        ["Spivak (subaltern studies)", "Asked whether and how marginalized colonial subjects can 'speak' within dominant discourse"],
    ])},
    "world-literature-m2-l8": {"data_table": table(["Scholar", "Contribution"], [
        ["Bhabha (hybridity)", "Described ambivalent identities formed at the intersection of colonizer and colonized cultures"],
    ])},
    "world-literature-m2-l9": {"data_table": table(["Scholar", "Contribution"], [
        ["Glissant (Poetics of Relation)", "Theorized Caribbean identity through creolization and relational, non-hierarchical connection"],
    ])},
    "world-literature-m2-l10": {"data_table": table(["Scholar", "Contribution"], [
        ["Casanova (World Republic of Letters)", "Modeled global literature as a competitive system with unequal centers and peripheries"],
    ])},
    "world-literature-m2-l11": {"data_table": table(["Scholar", "Contribution"], [
        ["Moretti (distant reading)", "Analyzes large collections of texts computationally rather than reading individual works closely"],
    ])},
    "world-literature-m2-l12": {"data_table": table(["Scholar", "Contribution"], [
        ["Damrosch", "Defines world literature as works that gain meaning through circulation and translation beyond their origin"],
    ])},
    "world-literature-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Magical realism", "A mode blending everyday reality with matter-of-fact fantastical elements"],
    ])},
    "world-literature-m2-l14": {"data_table": table(["Work", "Feature"], [
        ["One Hundred Years of Solitude", "Uses cyclical, repeating time to structure the Buendía family's generational saga"],
    ])},
    "world-literature-m2-l15": {"data_table": table(["Work", "Feature"], [
        ["Ficciones", "Borges's stories built as self-referential labyrinths blurring fiction and philosophy"],
    ])},
    "world-literature-m2-l16": {"data_table": table(["Work", "Feature"], [
        ["Things Fall Apart", "Achebe reclaims Igbo narrative voice against colonial depictions of Africa"],
    ])},
    "world-literature-m2-l17": {"data_table": table(["Author", "Claim"], [
        ["Ngũgĩ wa Thiong'o", "Argued writing in colonial languages perpetuates mental colonization of African writers"],
    ])},
    "world-literature-m2-l18": {"data_table": table(["Author", "Feature"], [
        ["Soyinka", "Draws on Yoruba mythology to frame a distinctly African tragic vision"],
    ])},
    "world-literature-m2-l19": {"data_table": table(["Work", "Feature"], [
        ["Disgrace", "Coetzee examines ethical reckoning and moral ambiguity in post-apartheid South Africa"],
    ])},
    "world-literature-m2-l20": {"data_table": table(["Work", "Feature"], [
        ["The Trial", "Kafka portrays an individual crushed by an incomprehensible, alienating bureaucratic system"],
    ])},
    "world-literature-m2-l21": {"data_table": table(["Work", "Feature"], [
        ["The Magic Mountain", "Mann's novel exemplifies the European Bildungsroman tradition of intellectual formation"],
    ])},
    "world-literature-m2-l22": {"data_table": table(["Work", "Feature"], [
        ["In Search of Lost Time", "Proust structures narrative around involuntary memory triggered by sensory experience"],
    ])},
    "world-literature-m2-l23": {"data_table": table(["Work", "Feature"], [
        ["Mrs Dalloway", "Woolf uses stream-of-consciousness to represent characters' continuous inner thought"],
    ])},
    "world-literature-m2-l24": {"data_table": table(["Work", "Feature"], [
        ["Ulysses", "Joyce reworks Homer's Odyssey structure into a single day in modernist Dublin"],
    ])},
    "world-literature-m2-l25": {"data_table": table(["Work", "Feature"], [
        ["The Sound and the Fury", "Faulkner fractures chronology across multiple unreliable narrators"],
    ])},
    "world-literature-m2-l26": {"data_table": table(["Work", "Feature"], [
        ["The Sea of Fertility", "Mishima's tetralogy uses Buddhist reincarnation as its structuring narrative frame"],
    ])},
    "world-literature-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Mono no Aware", "A Japanese aesthetic of gentle sadness at the transience of things, central to Kawabata's Snow Country"],
    ])},
    "world-literature-m2-l28": {"data_table": table(["Work", "Feature"], [
        ["In Praise of Shadows", "Tanizaki articulates a Japanese aesthetic theory valuing shadow and subtlety over Western brightness"],
    ])},
    "world-literature-m2-l29": {"data_table": table(["Work", "Feature"], [
        ["My Name Is Red", "Pamuk uses multiple narrating voices, including objects, in a polyphonic historical mystery"],
    ])},
    "world-literature-m2-l30": {"data_table": table(["Work", "Feature"], [
        ["Cairo Trilogy", "Mahfouz's saga exemplifies social realism tracing a family across generations of Egyptian history"],
    ])},
    "world-literature-m2-l31": {"data_table": table(["Poet", "Feature"], [
        ["Darwish", "Palestinian poet whose work articulates the aesthetics and politics of exile"],
    ])},
    "world-literature-m2-l32": {"data_table": table(["Poet", "Feature"], [
        ["Adonis", "Led a modernist revolution transforming the forms and language of Arabic poetry"],
    ])},
    "world-literature-m2-l33": {"data_table": table(["Author", "Feature"], [
        ["Premchand", "Pioneered social realism depicting rural life and injustice in Hindi-Urdu fiction"],
    ])},
    "world-literature-m2-l34": {"data_table": table(["Author", "Feature"], [
        ["Manto", "Wrote unflinching short fiction depicting the trauma of Partition violence"],
    ])},
    "world-literature-m2-l35": {"data_table": table(["Work", "Feature"], [
        ["Diary of a Madman", "Lu Xun's story is considered the founding work of modern vernacular Chinese fiction"],
    ])},
    "world-literature-m2-l36": {"data_table": table(["Work", "Feature"], [
        ["Red Sorghum", "Mo Yan blends brutal historical realism with hallucinatory, folkloric elements"],
    ])},
    "world-literature-m2-l37": {"data_table": table(["Author", "Feature"], [
        ["Kenzaburo Oe", "Writes literature confronting the trauma and moral reckoning of postwar Japan"],
    ])},
    "world-literature-m2-l38": {"data_table": table(["Work", "Feature"], [
        ["One Day in the Life of Ivan Denisovich", "Solzhenitsyn's novel is foundational testimony literature of the Soviet Gulag system"],
    ])},
    "world-literature-m2-l39": {"data_table": table(["Work", "Feature"], [
        ["The Master and Margarita", "Bulgakov satirizes Soviet society through supernatural fantasy"],
    ])},
    "world-literature-m2-l40": {"data_table": table(["Work", "Feature"], [
        ["Requiem", "Akhmatova's poem bears poetic witness to suffering under Stalinist repression"],
    ])},
    "world-literature-m2-l41": {"data_table": table(["Work", "Feature"], [
        ["The Unbearable Lightness of Being", "Kundera weaves philosophical reflection directly into the novel's narrative structure"],
    ])},
    "world-literature-m2-l42": {"data_table": table(["Author", "Claim"], [
        ["Kundera (Art of the Novel)", "Argued the novel is uniquely suited to investigate the ambiguities of human existence"],
    ])},
    "world-literature-m2-l43": {"data_table": table(["Author", "Feature"], [
        ["Marías", "Known for long, meditative sentences exploring interiority in contemporary Spanish fiction"],
    ])},
    "world-literature-m2-l44": {"data_table": table(["Work", "Feature"], [
        ["The Feast of the Goat", "Vargas Llosa's novel exemplifies the Latin American 'dictator novel' tradition"],
    ])},
    "world-literature-m2-l45": {"data_table": table(["Work", "Feature"], [
        ["Hopscotch", "Cortázar's novel can be read in multiple orders, exemplifying open-form experimental fiction"],
    ])},
    "world-literature-m2-l46": {"data_table": table(["Author", "Feature"], [
        ["Lispector", "Wrote existentialist Brazilian prose exploring consciousness in works like The Passion According to G.H."],
    ])},
    "world-literature-m2-l47": {"data_table": table(["Author", "Feature"], [
        ["Amado", "A leading figure of the regionalist tradition depicting Bahian life in Brazilian fiction"],
    ])},
    "world-literature-m2-l48": {"data_table": table(["Work", "Feature"], [
        ["Canto General", "Neruda's epic poem constructs a sweeping vision of Latin American identity and history"],
    ])},
    "world-literature-m2-l49": {"data_table": table(["Work", "Feature"], [
        ["The Labyrinth of Solitude", "Paz's essay collection explores Mexican cultural identity and psychology"],
    ])},
    "world-literature-m2-l50": {"data_table": table(["Work", "Feature"], [
        ["Like Water for Chocolate", "Esquivel blends culinary detail with magical realism to structure the narrative"],
    ])},
    "world-literature-m2-l51": {"data_table": table(["Author", "Feature"], [
        ["Danticat", "Writes literature of Haitian diaspora memory and displacement"],
    ])},
    "world-literature-m2-l52": {"data_table": table(["Work", "Feature"], [
        ["Omeros", "Walcott reimagines Homer's epic within a Caribbean setting and consciousness"],
    ])},
    "world-literature-m2-l53": {"data_table": table(["Work", "Feature"], [
        ["A Bend in the River", "Naipaul portrays postcolonial disillusionment and instability in a fictional African state"],
    ])},
    "world-literature-m2-l54": {"data_table": table(["Work", "Feature"], [
        ["Annie John", "Kincaid's novel exemplifies the postcolonial Bildungsroman of a young Caribbean girl"],
    ])},
    "world-literature-m2-l55": {"data_table": table(["Work", "Feature"], [
        ["Half of a Yellow Sun", "Adichie's novel gives literary form to the trauma of the Nigerian-Biafran War"],
    ])},
    "world-literature-m2-l56": {"data_table": table(["Work", "Feature"], [
        ["July's People", "Gordimer imagines the collapse of white minority rule at apartheid's endgame"],
    ])},
    "world-literature-m2-l57": {"data_table": table(["Work", "Feature"], [
        ["A Question of Power", "Head's novel explores psychological exile and breakdown"],
    ])},
    "world-literature-m2-l58": {"data_table": table(["Work", "Feature"], [
        ["Beloved", "Morrison depicts slavery's traumatic afterlife haunting a formerly enslaved family"],
    ])},
    "world-literature-m2-l59": {"data_table": table(["Scholar", "Claim"], [
        ["Morrison (Africanist presence)", "Argued American literature is shaped throughout by an unacknowledged Black presence"],
    ])},
    "world-literature-m2-l60": {"data_table": table(["Work", "Feature"], [
        ["Invisible Man", "Ellison portrays a Black narrator rendered socially 'invisible' by American racism"],
    ])},
    "world-literature-m2-l61": {"data_table": table(["Work", "Feature"], [
        ["Giovanni's Room", "Baldwin explores queer identity and expatriation in postwar Paris"],
    ])},
    "world-literature-m2-l62": {"data_table": table(["Scholar", "Claim"], [
        ["Sontag (Against Interpretation)", "Argued critics over-emphasize hidden meaning at the expense of a work's sensory form"],
    ])},
    "world-literature-m2-l63": {"data_table": table(["Scholar", "Claim"], [
        ["Barthes (Death of the Author)", "Argued a text's meaning is produced by readers, independent of authorial intent"],
    ])},
    "world-literature-m2-l64": {"data_table": table(["Scholar", "Claim"], [
        ["Kristeva (intertextuality)", "Argued every text is a mosaic constructed from absorption of other texts"],
    ])},
    "world-literature-m2-l65": {"data_table": table(["Scholar", "Contribution"], [
        ["Genette (narratology)", "Developed a systematic formal vocabulary for analyzing narrative discourse"],
    ])},
    "world-literature-m2-l66": {"data_table": table(["Scholar", "Contribution"], [
        ["Iser (reader-response)", "Theorized reading as an active process where readers complete a text's meaning"],
    ])},
    "world-literature-m2-l67": {"data_table": table(["Scholar", "Contribution"], [
        ["Jauss (reception theory)", "Analyzed how a text's meaning shifts as readers' historical 'horizon of expectations' changes"],
    ])},
    "world-literature-m2-l68": {"data_table": table(["Scholar", "Contribution"], [
        ["Derrida (deconstruction)", "Reveals how a text's meaning is destabilized by internal contradictions and gaps"],
    ])},
    "world-literature-m2-l69": {"data_table": table(["Scholars", "Contribution"], [
        ["Deleuze & Guattari (minor literature)", "Theorized how minority writers subvert a major language from within"],
    ])},
    "world-literature-m2-l70": {"data_table": table(["Concept", "Distinction"], [
        ["Foreignization (Venuti)", "Retains a source text's foreign strangeness in translation"],
        ["Domestication", "Adapts a text to feel natural in the target language"],
    ])},
    "world-literature-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Comparative literature in a globalized field", "Examines methodological challenges of studying literature across an interconnected world"],
    ])},
    "world-literature-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Postcolonial Bildungsroman", "A coming-of-age novel form adapted to represent postcolonial identity formation"],
    ])},
    "world-literature-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Testimonio", "A Latin American genre of first-person witness narrative documenting political oppression"],
    ])},
    "world-literature-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Négritude movement", "A francophone Black literary and political movement affirming African cultural identity"],
    ])},
    "world-literature-m2-l75": {"data_table": table(["Work", "Feature"], [
        ["Notebook of a Return to the Native Land", "Césaire's poem is a foundational anticolonial and Négritude text"],
    ])},
    "world-literature-m2-l76": {"data_table": table(["Poet", "Theory"], [
        ["Senghor", "Developed a poetic theory affirming a distinct African civilizational and cultural identity"],
    ])},
    "world-literature-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Harlem Renaissance (transnational)", "Situates the Harlem Renaissance within broader Black internationalist literary networks"],
    ])},
    "world-literature-m2-l78": {"data_table": table(["Poet", "Feature"], [
        ["Hughes", "Drew on Black vernacular speech and jazz rhythms in African American poetry"],
    ])},
    "world-literature-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Beat Generation transnational influences", "Traces how postwar American Beat writers drew on and influenced global literary movements"],
    ])},
    "world-literature-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Modernist epiphany", "A sudden moment of insight used as a cross-cultural narrative device in modernist fiction"],
    ])},
    "world-literature-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Algerian War literature", "Compares how French and Arabic literary traditions represented the Algerian War"],
    ])},
    "world-literature-m2-l82": {"data_table": table(["Work", "Feature"], [
        ["The Stranger", "Camus depicts existential alienation and absurdism set in colonial Algeria"],
    ])},
    "world-literature-m2-l83": {"data_table": table(["Work", "Feature"], [
        ["Memoirs of Hadrian", "Yourcenar's historical novel functions as a philosophical meditation on power and mortality"],
    ])},
    "world-literature-m2-l84": {"data_table": table(["Work", "Feature"], [
        ["The Name of the Rose", "Eco applies semiotic theory within a medieval murder-mystery narrative"],
    ])},
    "world-literature-m2-l85": {"data_table": table(["Work", "Feature"], [
        ["If on a Winter's Night a Traveler", "Calvino's novel is self-reflexively postmodern, addressing the reader directly"],
    ])},
    "world-literature-m2-l86": {"data_table": table(["Work", "Feature"], [
        ["The Tin Drum", "Grass uses magical realism to narrate German history through a narrator who refuses to grow"],
    ])},
    "world-literature-m2-l87": {"data_table": table(["Work", "Feature"], [
        ["Austerlitz", "Sebald blends fiction and archival photography to explore traumatic historical memory"],
    ])},
    "world-literature-m2-l88": {"data_table": table(["Work", "Feature"], [
        ["The Remains of the Day", "Ishiguro's unreliable narrator becomes an ethical device revealing self-deception"],
    ])},
    "world-literature-m2-l89": {"data_table": table(["Author", "Theory"], [
        ["Rushdie", "Theorized migrant writers as inhabiting 'imaginary homelands' shaped by displacement"],
    ])},
    "world-literature-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Indian Partition literature (beyond Manto)", "Surveys the broader literary tradition depicting Partition's trauma"],
    ])},
    "world-literature-m2-l91": {"data_table": table(["Work", "Feature"], [
        ["The Inheritance of Loss", "Desai examines globalization's impact on postcolonial identity and inequality"],
    ])},
    "world-literature-m2-l92": {"data_table": table(["Work", "Feature"], [
        ["The God of Small Things", "Roy uses nonlinear narrative structure within Indian English fiction"],
    ])},
    "world-literature-m2-l93": {"data_table": table(["Work", "Feature"], [
        ["The Shadow Lines", "Ghosh explores how political borders fracture geography and memory"],
    ])},
    "world-literature-m2-l94": {"data_table": table(["Work", "Feature"], [
        ["The Famished Road", "Okri blends African spirit-world cosmology with narrative realism"],
    ])},
    "world-literature-m2-l95": {"data_table": table(["Author", "Feature"], [
        ["Diop", "A leading figure in the contemporary Francophone African literary renaissance"],
    ])},
    "world-literature-m2-l96": {"data_table": table(["Work", "Feature"], [
        ["2666", "Bolaño's sprawling novel confronts systemic violence through fragmented narrative"],
    ])},
    "world-literature-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Global anthology canon politics", "Examines how world literature pedagogy is shaped by anthology selection and exclusion"],
    ])},
    "world-literature-m2-l98": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Presents original comparative world literature research demonstrating scholarly mastery"],
    ])},
    "world-literature-m2-l99": {"data_table": table(["Author", "Feature"], [
        ["Alice Munro", "Constructs short story cycles that reveal deep complexity within seemingly ordinary lives"],
    ])},
    "world-literature-m2-l100": {"data_table": table(["Work", "Feature"], [
        ["Blindness", "Saramago's allegorical dystopia uses a mass epidemic of blindness to examine social collapse"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"world-literature-m2-l{base_n}"
    worked_key = f"world-literature-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 World Literature lessons.")


if __name__ == "__main__":
    main()
