#!/usr/bin/env python3
"""Depth pass, M2 Social Studies: fill in real, hand-checked
data_table content for the M2 Social Studies lessons not covered by
the earlier breadth-first batch. Brings M2 Social Studies to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
classical and contemporary social theory, social movements and
political sociology, urban/environmental sociology, and quantitative
and qualitative social science methodology; l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Habitus", "Bourdieu's concept of internalized dispositions shaped by one's social position"],
    ["Capital (social theory)", "Resources (economic, cultural, social) that determine one's position within a social field"],
])

CHARTS: dict[str, dict] = {
    "social-studies-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Social research methods", "Systematic techniques for studying human society and social behavior"],
    ])},
    "social-studies-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Society & institutions research", "Rigorous scholarly methods for studying how institutions shape social life"],
    ])},
    "social-studies-m2-l4": {"data_table": table(["Scholar", "Claim"], [
        ["Habermas", "Argued rational consensus can emerge through open, undistorted communication"],
    ])},
    "social-studies-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Governmentality", "Foucault's concept of how power operates through techniques of governing conduct, not just law"],
    ])},
    "social-studies-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Structuration theory", "Giddens's theory that social structures both shape and are shaped by human agency"],
    ])},
    "social-studies-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Social systems theory", "Luhmann's theory viewing society as composed of self-referential communication systems"],
    ])},
    "social-studies-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Actor-network theory", "Treats human and non-human elements as equal actors shaping social outcomes"],
    ])},
    "social-studies-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Intersectionality", "Analyzes how overlapping identity categories (race, gender, class) combine to shape experience"],
    ])},
    "social-studies-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["World-systems analysis", "Wallerstein's framework analyzing global history through core-periphery economic structures"],
    ])},
    "social-studies-m2-l11": {"data_table": table(["Scholar", "Feature"], [
        ["Putnam", "Emphasized declining civic associational social capital"],
        ["Coleman", "Emphasized social capital's role in individual and family outcomes"],
    ])},
    "social-studies-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Ethnomethodology", "Studies the everyday methods people use to make sense of and produce social order"],
    ])},
    "social-studies-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Risk society", "Beck's thesis that modern society is organized around managing manufactured risks"],
    ])},
    "social-studies-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Liquid modernity", "Bauman's concept describing the increasingly fluid, unstable nature of modern social bonds"],
    ])},
    "social-studies-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Network society", "Castells's theory that networks, especially digital ones, now organize social and economic life"],
    ])},
    "social-studies-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Theory of recognition", "Honneth's theory that social conflict often stems from struggles for mutual recognition"],
    ])},
    "social-studies-m2-l17": {"data_table": table(["Scholars", "Claim"], [
        ["Sen and Nussbaum", "Justice should be measured by people's real capabilities to live a life they value"],
    ])},
    "social-studies-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Deliberative democracy", "Argues legitimate political decisions should emerge from reasoned public deliberation"],
    ])},
    "social-studies-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Agonistic pluralism", "Mouffe's view that democracy should channel conflict productively rather than seek false consensus"],
    ])},
    "social-studies-m2-l20": {"data_table": table(["Scholars", "Contrast"], [
        ["Foucault", "Biopolitics as governing populations through knowledge and normalization"],
        ["Agamben", "Extended biopolitics to theorize sovereign power over 'bare life'"],
    ])},
    "social-studies-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Necropolitics", "Mbembe's concept describing sovereign power's use to determine who may live and who must die"],
    ])},
    "social-studies-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Settler colonialism (analytic framework)", "Treats settler replacement of Indigenous populations as an ongoing structure, not a past event"],
    ])},
    "social-studies-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Coloniality of power", "Quijano's concept that colonial racial hierarchies persist structurally after formal colonialism ends"],
    ])},
    "social-studies-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Frankfurt School critical theory", "Combines Marxist analysis with cultural critique to examine domination in modern society"],
    ])},
    "social-studies-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Cultural hegemony", "Gramsci's concept that ruling class power is maintained through cultural consent, not just force"],
    ])},
    "social-studies-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Social reproduction theory", "Examines the often-unpaid labor that sustains and renews a workforce and society"],
    ])},
    "social-studies-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Standpoint theory", "Argues knowledge is shaped by one's social position, giving marginalized groups distinct insight"],
    ])},
    "social-studies-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Queer theory (institutions)", "Examines how social institutions construct and enforce normative categories of gender and sexuality"],
    ])},
    "social-studies-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Social model of disability", "Locates disability in social barriers and exclusion, not solely in individual impairment"],
    ])},
    "social-studies-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Environmental justice theory", "Examines how environmental harms disproportionately affect marginalized communities"],
    ])},
    "social-studies-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Urban political ecology", "Examines how power shapes the flow of resources through urban infrastructure"],
    ])},
    "social-studies-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Assemblage theory", "DeLanda's approach analyzing social wholes as composed of interacting, detachable parts"],
    ])},
    "social-studies-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Affect theory (social research)", "Studies emotional and bodily intensities that circulate through social and political life"],
    ])},
    "social-studies-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["New materialism", "Rethinks social theory by granting matter and non-human agency active roles"],
    ])},
    "social-studies-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Social construction of technology", "Argues technology's design and meaning are shaped by social processes, not fixed by function alone"],
    ])},
    "social-studies-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Control societies", "Deleuze's extension of Foucault's panopticon to describe diffuse, continuous modern surveillance"],
    ])},
    "social-studies-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Platform capitalism", "Examines how digital platforms structure new forms of labor and economic extraction"],
    ])},
    "social-studies-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Gig economy sociology", "Studies working conditions and precarity within app-mediated, task-based labor"],
    ])},
    "social-studies-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Financialization theory", "Examines how financial logic increasingly shapes everyday economic and social life"],
    ])},
    "social-studies-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Neoliberalism as governmentality", "Treats neoliberalism as a mode of governing conduct, not merely an economic policy"],
    ])},
    "social-studies-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Austerity studies", "Examines the social policy effects of government spending cuts during economic crises"],
    ])},
    "social-studies-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Resource mobilization theory", "Explains social movement success by focus on organizational resources, not just grievance"],
    ])},
    "social-studies-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Political opportunity structure", "Explains social movement emergence through openings in the surrounding political context"],
    ])},
    "social-studies-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Framing theory (collective action)", "Studies how activists construct interpretive frames to mobilize participants"],
    ])},
    "social-studies-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Contentious politics", "Tilly and Tarrow's framework analyzing collective political struggle across varied contexts"],
    ])},
    "social-studies-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Civil society theory (comparative)", "Compares how independent associational life functions across different political systems"],
    ])},
    "social-studies-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Ethnic conflict theory", "Analyzes the social and political conditions that give rise to ethnic-based conflict"],
    ])},
    "social-studies-m2-l48": {"data_table": table(["Scholar", "Claim"], [
        ["Anderson (Imagined Communities)", "Argued nations are socially constructed communities imagined through shared media and symbols"],
    ])},
    "social-studies-m2-l49": {"data_table": table(["Scholar", "Claim"], [
        ["Hobsbawm (Invented Traditions)", "Showed many 'ancient' traditions were actually recently constructed for social purposes"],
    ])},
    "social-studies-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora studies", "Theoretical foundations for studying dispersed communities' identity and connection"],
    ])},
    "social-studies-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Transnationalism (migration)", "Studies how migrants maintain active ties across multiple nation-states simultaneously"],
    ])},
    "social-studies-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Segmented assimilation theory", "Explains how immigrant integration outcomes vary across different social pathways"],
    ])},
    "social-studies-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["World polity theory", "Argues shared global cultural scripts shape how nation-states organize themselves similarly"],
    ])},
    "social-studies-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Comparative historical sociology", "Uses systematic comparison across cases and time periods to explain social change"],
    ])},
    "social-studies-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Path dependency", "Early institutional choices constrain and shape a society's later possible developments"],
    ])},
    "social-studies-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Critical juncture", "A pivotal moment where contingent choices set an institution on a long-lasting path"],
    ])},
    "social-studies-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Historical institutionalism", "Explains political outcomes through the enduring effects of past institutional choices"],
    ])},
    "social-studies-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Rational choice institutionalism", "Models institutions as structures shaping strategic, self-interested individual behavior"],
    ])},
    "social-studies-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Foucauldian discourse analysis", "Examines how discourse produces power/knowledge and shapes what can be said as true"],
    ])},
    "social-studies-m2-l60": {"data_table": table(["Scholar", "Claim"], [
        ["Fairclough", "Analyzes discourse as text, discursive practice, and social practice together"],
    ])},
    "social-studies-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Strong program (cultural sociology)", "Alexander's approach treating culture as an autonomous force shaping social action, not mere reflection"],
    ])},
    "social-studies-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic boundaries", "Lamont's concept of the conceptual distinctions people use to classify and rank social groups"],
    ])},
    "social-studies-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Distinction (Bourdieu)", "Argues taste and cultural preference function to mark and reproduce class hierarchy"],
    ])},
    "social-studies-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Consumer culture theory", "Examines how consumption practices shape identity and meaning in modern society"],
    ])},
    "social-studies-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Disaster sociology", "Studies the social causes and consequences of disasters, beyond the physical hazard itself"],
    ])},
    "social-studies-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Treadmill of production", "Argues capitalism's growth imperative structurally drives increasing environmental harm"],
    ])},
    "social-studies-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Degrowth theory", "Argues sustainable social policy requires deliberately reducing economic production and consumption"],
    ])},
    "social-studies-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Political ecology of resource conflict", "Analyzes how power relations shape conflicts over natural resources"],
    ])},
    "social-studies-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Food regime theory", "Analyzes historical periods of global food production and trade shaped by political power"],
    ])},
    "social-studies-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Moral economy of the peasant", "Scott's theory that peasant behavior is shaped by norms of subsistence security, not pure profit"],
    ])},
    "social-studies-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Everyday forms of resistance", "Studies subtle, informal acts by which subordinate groups resist domination"],
    ])},
    "social-studies-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Subaltern studies", "Historiography recovering the perspectives of marginalized groups excluded from elite narratives"],
    ])},
    "social-studies-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Feminist political economy", "Analyzes development through the lens of gendered labor and economic power"],
    ])},
    "social-studies-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Care economy theory", "Examines the often-invisible economic value of caregiving labor"],
    ])},
    "social-studies-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Welfare regime typology", "Esping-Andersen's classification of welfare states into liberal, conservative, and social-democratic types"],
    ])},
    "social-studies-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Comparative welfare state analysis", "Compares how different countries structure social safety net policies"],
    ])},
    "social-studies-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Multidimensional poverty index", "Measures poverty using multiple deprivation indicators beyond income alone"],
    ])},
    "social-studies-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Intergenerational social mobility", "Studies how much a person's social position is determined by their parents' position"],
    ])},
    "social-studies-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Cultural capital and stratification", "Examines how cultural knowledge and taste help reproduce educational inequality"],
    ])},
    "social-studies-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Demographic transition (advanced models)", "Extends the classic model with additional stages and regional variation"],
    ])},
    "social-studies-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Population aging policy", "Analyzes policy responses to societies with growing proportions of older residents"],
    ])},
    "social-studies-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Global cities framework", "Sassen's theory identifying key cities as command nodes in the global economy"],
    ])},
    "social-studies-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Gentrification and displacement", "Examines how rising property values force out lower-income residents"],
    ])},
    "social-studies-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Right to the city", "Lefebvre's concept asserting urban residents' collective claim to shape city life"],
    ])},
    "social-studies-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Spatial justice theory", "Examines how the fair distribution of resources and opportunity has a geographic dimension"],
    ])},
    "social-studies-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Residential segregation measurement", "Statistical methods for quantifying how separated groups are across neighborhoods"],
    ])},
    "social-studies-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Social network analysis", "Studies patterns of relationships and their structural effect on social outcomes"],
    ])},
    "social-studies-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Homophily and diffusion", "Similar people tend to connect, which shapes how information and behavior spread through networks"],
    ])},
    "social-studies-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Computational social science", "Uses large-scale data and computational methods to study social phenomena"],
    ])},
    "social-studies-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Agent-based modeling", "Simulates social phenomena by modeling individual agents following simple behavioral rules"],
    ])},
    "social-studies-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Directed acyclic graphs (causal inference)", "Visualizes assumed causal relationships to guide valid statistical inference"],
    ])},
    "social-studies-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Event history analysis", "Statistical methods for modeling the timing of events in longitudinal social data"],
    ])},
    "social-studies-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Multilevel modeling", "Accounts for data nested within groups (e.g. students within schools) in statistical models"],
    ])},
    "social-studies-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Total survey error framework", "Comprehensively accounts for all sources of error affecting survey data quality"],
    ])},
    "social-studies-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Qualitative comparative analysis", "A method using set theory and Boolean logic to compare configurations across cases"],
    ])},
    "social-studies-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Multi-sited ethnography", "Extends ethnographic fieldwork across multiple connected locations rather than one site"],
    ])},
    "social-studies-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Participatory action research", "Involves the community being studied directly as co-researchers in the research process"],
    ])},
    "social-studies-m2-l98": {"data_table": table(["Scholar", "Claim"], [
        ["Freire", "Argued education should be a dialogical process that develops critical consciousness"],
    ])},
    "social-studies-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Cosmopolitanism theory", "Argues moral obligations and citizenship should extend beyond national boundaries"],
    ])},
    "social-studies-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Transitional justice studies", "Studies how societies address mass atrocity after conflict, e.g. tribunals and truth commissions"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"social-studies-m2-l{base_n}"
    worked_key = f"social-studies-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Social Studies lessons.")


if __name__ == "__main__":
    main()
