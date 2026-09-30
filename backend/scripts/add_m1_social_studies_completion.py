#!/usr/bin/env python3
"""Depth pass, M1 Social Studies: fill in real, hand-checked
data_table content for the 99 M1 Social Studies lessons not covered
by the earlier breadth-first batch. Brings M1 Social Studies to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "social-studies-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative social systems", "Societies organize labor, family, and authority in differing structures"],
        ]),
    },
    "social-studies-m1-l2": {
        "data_table": table(["Method", "Feature"], [
            ["Social research methods", "Combines qualitative and quantitative tools to study human behavior"],
        ]),
    },
    "social-studies-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Anthropological theory", "Provides frameworks for interpreting culture through comparative fieldwork"],
        ]),
    },
    "social-studies-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Class and power", "Economic position shapes access to social and political influence"],
        ]),
    },
    "social-studies-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Critical race theory", "Examines how race and racism are embedded within legal and social structures"],
        ]),
    },
    "social-studies-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Gender and power", "Examines how gender shapes access to authority and resources"],
        ]),
    },
    "social-studies-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Social psychology", "Studies how individual thought and behavior are shaped by social context"],
        ]),
    },
    "social-studies-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Contentious politics", "Studies collective action and conflict outside routine institutional channels"],
        ]),
    },
    "social-studies-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Urban theory", "Examines how cities are socially, economically, and spatially organized"],
        ]),
    },
    "social-studies-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Kinship", "Studies how societies structure family relationships and descent"],
        ]),
    },
    "social-studies-m1-l12": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Strain theory", "Crime results from a gap between societal goals and legitimate means to achieve them"],
        ]),
    },
    "social-studies-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["World-systems analysis", "Frames global inequality through core-periphery economic relationships"],
        ]),
    },
    "social-studies-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Research methodology", "The systematic design choices underlying credible social science inquiry"],
        ]),
    },
    "social-studies-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Population and development", "Demographic trends shape and are shaped by a country's economic trajectory"],
        ]),
    },
    "social-studies-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Media sociology", "Examines how mass and digital media shape social attitudes and behavior"],
        ]),
    },
    "social-studies-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Social reproduction", "Education systems can perpetuate existing class advantage across generations"],
        ]),
    },
    "social-studies-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Economic sociology", "Examines how social relationships shape markets and economic behavior"],
        ]),
    },
    "social-studies-m1-l19": {
        "data_table": table(["Debate", "Detail"], [
            ["Secularization debate", "Scholars dispute whether modernization inevitably reduces religious influence"],
        ]),
    },
    "social-studies-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research project", "Applies social science methods to an original research question"],
        ]),
    },
    "social-studies-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Political sociology of the state", "Examines the state as a social institution shaped by contested power relations"],
        ]),
    },
    "social-studies-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Religion beyond secularization", "Global religious resurgence has challenged simple decline narratives"],
        ]),
    },
    "social-studies-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Climate justice", "Examines unequal responsibility for and exposure to climate change impacts"],
        ]),
    },
    "social-studies-m1-l24": {
        "data_table": table(["Field", "Focus"], [
            ["Science and Technology Studies (STS)", "Examines how scientific knowledge and technology are socially shaped"],
        ]),
    },
    "social-studies-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Platform studies", "Examines how digital platforms structure social and economic interaction"],
        ]),
    },
    "social-studies-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Labor market sociology", "Examines how social structures shape employment access and outcomes"],
        ]),
    },
    "social-studies-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Transnationalism", "Migrants maintain active social and economic ties across more than one nation"],
        ]),
    },
    "social-studies-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Embodiment", "Examines the body as a site where social meaning and power are enacted"],
        ]),
    },
    "social-studies-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of emotions", "Studies how social context shapes emotional experience and expression"],
        ]),
    },
    "social-studies-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative historical sociology", "Uses historical cases to test broad theories of social change"],
        ]),
    },
    "social-studies-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Social movement mobilization", "Examines the resources and conditions that enable collective action"],
        ]),
    },
    "social-studies-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Collective memory", "Studies how societies construct shared narratives of the past"],
        ]),
    },
    "social-studies-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Social control", "Examines the formal and informal mechanisms enforcing conformity to norms"],
        ]),
    },
    "social-studies-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Political economy of development", "Examines how power and institutions shape economic outcomes"],
        ]),
    },
    "social-studies-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Decolonial social theory", "Reframes social theory beyond a single dominant Western intellectual tradition"],
        ]),
    },
    "social-studies-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Intersectionality", "Examines how overlapping identities compound experiences of disadvantage"],
        ]),
    },
    "social-studies-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Material culture", "Studies how consumption practices express and shape social identity"],
        ]),
    },
    "social-studies-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of health", "Examines how social position shapes illness experience and health outcomes"],
        ]),
    },
    "social-studies-m1-l39": {
        "data_table": table(["Field", "Focus"], [
            ["Medical anthropology", "Studies how culture shapes understanding and treatment of illness"],
        ]),
    },
    "social-studies-m1-l40": {
        "data_table": table(["Field", "Focus"], [
            ["Political anthropology", "Studies power and governance across diverse cultural systems"],
        ]),
    },
    "social-studies-m1-l41": {
        "data_table": table(["Field", "Focus"], [
            ["Economic anthropology", "Studies how exchange and production are culturally organized"],
        ]),
    },
    "social-studies-m1-l42": {
        "data_table": table(["Method", "Purpose"], [
            ["Ethnographic film", "Uses visual documentation as a method of cultural anthropological research"],
        ]),
    },
    "social-studies-m1-l43": {
        "data_table": table(["Field", "Focus"], [
            ["Linguistic anthropology", "Studies how language shapes and reflects cultural worldview"],
        ]),
    },
    "social-studies-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Ritual and symbolism", "Studies how symbolic action reinforces shared cultural meaning"],
        ]),
    },
    "social-studies-m1-l45": {
        "data_table": table(["Framework", "Focus"], [
            ["Structuralism", "Analyzes underlying systems of relationships that generate social meaning"],
            ["Post-structuralism", "Questions the stability of those underlying structures themselves"],
        ]),
    },
    "social-studies-m1-l46": {
        "data_table": table(["School", "Focus"], [
            ["Frankfurt School", "Critical theory examining culture, ideology, and mass society"],
        ]),
    },
    "social-studies-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Governmentality/biopolitics", "Foucault's concept of power operating through the regulation of populations"],
        ]),
    },
    "social-studies-m1-l48": {
        "data_table": table(["Regime Type", "Feature"], [
            ["Social-democratic welfare model", "Broad universal benefits funded through high taxation"],
            ["Liberal welfare model", "Means-tested benefits with reliance on market provision"],
        ]),
    },
    "social-studies-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Social stratification", "Examines how societies rank individuals into hierarchical social classes"],
        ]),
    },
    "social-studies-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Global city", "A major urban center that functions as a command node in the world economy"],
        ]),
    },
    "social-studies-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Agrarian change", "Studies how rural social structures transform under economic development"],
        ]),
    },
    "social-studies-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster vulnerability", "Combines hazard exposure with social factors to determine disaster impact"],
        ]),
    },
    "social-studies-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Political demography", "Examines how population trends influence political power and conflict"],
        ]),
    },
    "social-studies-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Nationalism theory", "Examines how national identity is constructed and mobilized politically"],
        ]),
    },
    "social-studies-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative ethnic conflict", "Studies the conditions under which ethnic tension escalates to violence"],
        ]),
    },
    "social-studies-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Social network analysis", "Maps relationships to study influence and information flow"],
        ]),
    },
    "social-studies-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Mixed-methods design", "Combines qualitative and quantitative approaches within a single study"],
        ]),
    },
    "social-studies-m1-l58": {
        "data_table": table(["Method", "Detail"], [
            ["Grounded theory", "Builds theory inductively from qualitative data patterns"],
        ]),
    },
    "social-studies-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Measurement theory", "Ensures survey instruments validly and reliably capture intended concepts"],
        ]),
    },
    "social-studies-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Research ethics", "Protects participant welfare and consent throughout the research process"],
        ]),
    },
    "social-studies-m1-l61": {
        "data_table": table(["Method", "Focus"], [
            ["Institutional ethnography", "Traces how everyday experience connects to broader institutional processes"],
        ]),
    },
    "social-studies-m1-l62": {
        "data_table": table(["Method", "Focus"], [
            ["Discourse analysis", "Examines how language use reflects and reproduces power relations"],
        ]),
    },
    "social-studies-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative legal sociology", "Examines how legal systems reflect and shape a society's social order"],
        ]),
    },
    "social-studies-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of human rights", "Examines how rights frameworks are socially constructed and contested"],
        ]),
    },
    "social-studies-m1-l65": {
        "data_table": table(["Field", "Focus"], [
            ["Peace and conflict studies", "Examines the causes of conflict and the conditions for durable peace"],
        ]),
    },
    "social-studies-m1-l66": {
        "data_table": table(["Field", "Focus"], [
            ["Genocide studies", "Examines the causes, mechanisms, and historical memory of mass atrocities"],
        ]),
    },
    "social-studies-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Democratization theory", "Examines the conditions that enable transition toward democratic governance"],
        ]),
    },
    "social-studies-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Civil society", "Voluntary organizations operating outside government and the market"],
        ]),
    },
    "social-studies-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Elite power networks", "Examines how concentrated networks of influence shape major decisions"],
        ]),
    },
    "social-studies-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Social capital", "Networks of trust and reciprocity that enable collective action"],
        ]),
    },
    "social-studies-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of childhood", "Treats childhood as a socially constructed category rather than a fixed biological stage"],
        ]),
    },
    "social-studies-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Life course theory", "Individual trajectories are shaped by historical timing and social context"],
        ]),
    },
    "social-studies-m1-l73": {
        "data_table": table(["Structure", "Feature"], [
            ["Nuclear family", "Two parents and children forming an independent household"],
            ["Extended family", "Multiple generations or relatives sharing close ties or a household"],
        ]),
    },
    "social-studies-m1-l74": {
        "data_table": table(["Model", "Feature"], [
            ["Social model of disability", "Locates disability in societal barriers rather than individual impairment"],
        ]),
    },
    "social-studies-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Sexuality studies", "Examines how sexual identity and norms are socially constructed"],
        ]),
    },
    "social-studies-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Masculinity studies", "Examines how masculine identity is socially constructed and enacted"],
        ]),
    },
    "social-studies-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Feminist political theory", "Examines power and justice through the lens of gendered experience"],
        ]),
    },
    "social-studies-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative social policy", "Analyzes how different nations structure responses to shared social problems"],
        ]),
    },
    "social-studies-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Bureaucracy", "Weber's model of rational-legal authority organized through formal rules and hierarchy"],
        ]),
    },
    "social-studies-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Political behavior", "Studies the factors shaping how citizens form opinions and cast votes"],
        ]),
    },
    "social-studies-m1-l81": {
        "data_table": table(["System", "Feature"], [
            ["Proportional representation", "Allocates seats roughly in proportion to vote share"],
            ["First-past-the-post", "Awards seats to the single highest vote-getter in each district"],
        ]),
    },
    "social-studies-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Social mobility model", "Measures how likely individuals are to move between social class positions"],
        ]),
    },
    "social-studies-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Postmodernity", "Questions modernity's grand narratives of progress and universal truth"],
        ]),
    },
    "social-studies-m1-l84": {
        "data_table": table(["System", "Feature"], [
            ["Comparative colonial administration", "Colonial powers governed differently through direct or indirect rule"],
        ]),
    },
    "social-studies-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Indigenous sovereignty", "Self-governance rights rooted in prior and continuing occupancy of land"],
        ]),
    },
    "social-studies-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Punishment systems", "Examines the social functions and consequences of different penal approaches"],
        ]),
    },
    "social-studies-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Surveillance studies", "Examines how monitoring practices shape social control and privacy"],
        ]),
    },
    "social-studies-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Global governance institutions", "Coordinates policy among states and institutions without a central world government"],
        ]),
    },
    "social-studies-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["World society theory", "Argues shared global norms increasingly shape national institutions worldwide"],
        ]),
    },
    "social-studies-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Temporality", "Examines how social groups construct and experience time differently"],
        ]),
    },
    "social-studies-m1-l91": {
        "data_table": table(["Movement", "Focus"], [
            ["Environmental justice movement", "Addresses unequal exposure to environmental harm across communities"],
        ]),
    },
    "social-studies-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Food systems sociology", "Examines the social structures shaping how food is produced and distributed"],
        ]),
    },
    "social-studies-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of sport", "Examines how sport reflects and reinforces broader social structures"],
        ]),
    },
    "social-studies-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Trust theory", "Examines how generalized trust supports functioning social and economic institutions"],
        ]),
    },
    "social-studies-m1-l95": {
        "data_table": table(["Method", "Focus"], [
            ["Comparative regional methodology", "Systematically compares political and social patterns across world regions"],
        ]),
    },
    "social-studies-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Historical materialism", "Marx's theory that material economic conditions drive historical social change"],
        ]),
    },
    "social-studies-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster resilience", "Examines the social factors enabling communities to recover from catastrophic events"],
        ]),
    },
    "social-studies-m1-l98": {
        "data_table": table(["Design Choice", "Effect"], [
            ["Federal constitution", "Divides power between national and regional governments"],
        ]),
    },
    "social-studies-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of knowledge", "Examines how social context shapes what counts as legitimate knowledge"],
        ]),
    },
    "social-studies-m1-l100": {
        "data_table": table(["Method", "Purpose"], [
            ["Applied policy analysis", "Uses social science evidence to evaluate and inform real-world policy decisions"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Sociological Perspective", "Core Idea"], [
        ["Functionalism", "Society is a system of interdependent parts working together"],
        ["Conflict theory", "Society is shaped by competition over scarce resources"],
        ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"social-studies-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"social-studies-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"social-studies-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Social Studies lessons (completing 120/120).")


if __name__ == "__main__":
    main()
