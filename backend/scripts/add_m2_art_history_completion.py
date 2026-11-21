#!/usr/bin/env python3
"""Depth pass, M2 Art History: fill in real, hand-checked data_table
content for the M2 Art History lessons not covered by the earlier
breadth-first batch. Brings M2 Art History to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning art
historical methodology and theory (Panofsky, Warburg, connoisseurship,
feminist/postcolonial critique), digital and technical art history,
provenance and restitution, historiography across regions and periods
(Islamic, East Asian, Pre-Columbian, African, Ottoman art
scholarship), patronage and production systems, iconography and
reception, and dissertation-level research methodology; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_art_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Iconology", "Panofsky's method of interpreting an artwork's deeper cultural and symbolic meaning beyond its literal subject matter"],
    ["Post-structuralist critique", "Later theorists challenged iconology's assumption of a single recoverable authorial meaning behind an image"],
])

CHARTS: dict[str, dict] = {
    "art-history-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Digital art history", "Applies computational tools and methods to art historical research and analysis"],
        ["Application", "Includes image analysis software, digital archives, and large-scale corpus visualization techniques"],
    ])},
    "art-history-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Art history capstone", "An applied culminating project demonstrating original art historical research and argumentation skill"],
        ["Deliverable", "Typically a substantial research paper analyzing a specific artwork, artist, or movement using rigorous methodology"],
    ])},
    "art-history-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Mnemosyne Atlas", "Aby Warburg's unfinished project arranging image panels to trace the transmission of visual and emotional motifs across time"],
        ["Methodology", "Pioneered an associative, comparative image-based method of tracing cultural memory rather than linear chronological narrative"],
    ])},
    "art-history-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Connoisseurship", "The practice of attributing and dating artworks based on close visual analysis of style and technique"],
        ["Social history of art", "Emphasizes instead the social, economic, and political context shaping an artwork's production and meaning"],
    ])},
    "art-history-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Vienna School formalism", "An early art historical approach emphasizing the analysis of formal visual elements independent of subject matter"],
        ["Legacy", "Influenced later formalist and structuralist approaches to analyzing an artwork's compositional structure"],
    ])},
    "art-history-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Feminist art history", "Critically examines the historical exclusion and marginalization of women artists from the traditional art historical canon"],
        ["Canon intervention", "Works to recover overlooked women artists and critique the gendered assumptions embedded in canon formation itself"],
    ])},
    "art-history-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Global art history", "Studies art across all world regions and periods rather than centering a Western historical trajectory"],
        ["Eurocentric periodization critique", "Challenges the assumption that period categories developed for Western art apply universally to non-Western traditions"],
    ])},
    "art-history-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Visual culture studies", "A broader interdisciplinary field examining all visual imagery and practices, not limited to fine art objects"],
        ["Contrast with traditional art history", "Traditional art history has historically focused more narrowly on canonical fine art objects and named artists"],
    ])},
    "art-history-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Semiotics of the image", "Analyzes how images function as sign systems producing meaning, drawing on Barthes and Eco's semiotic theory"],
        ["Application", "Distinguishes denotative (literal) from connotative (culturally coded) levels of meaning within a visual image"],
    ])},
    "art-history-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Postcolonial historiography", "Critically examines how colonial power relations shaped the study and categorization of non-Western art traditions"],
        ["Application", "Interrogates inherited colonial-era frameworks and terminology still used to describe non-Western artistic production"],
    ])},
    "art-history-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Technical art history", "Combines art historical inquiry with scientific material analysis of an artwork's physical composition"],
        ["Material analysis", "Techniques like pigment analysis and X-ray imaging can reveal an artwork's creation process, alterations, and authenticity"],
    ])},
    "art-history-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Provenance research", "Traces an artwork's ownership history to establish its legitimate chain of custody"],
        ["Nazi-era looted art", "A specialized and ethically significant area of provenance research addressing art seized or coerced during the Nazi era"],
    ])},
    "art-history-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Digital humanities tools", "Computational methods applied to humanities research questions"],
        ["Large-scale image corpus analysis", "Enables identifying visual patterns and trends across thousands of images that manual review could not feasibly cover"],
    ])},
    "art-history-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Network analysis", "Analyzes relationships between entities as a graph to reveal structural patterns"],
        ["Renaissance patronage system", "Maps connections between artists, patrons, and institutions to reveal how influence and commissions actually flowed"],
    ])},
    "art-history-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Reception theory", "Studies how an artwork's meaning and value have been interpreted differently by audiences across different historical periods"],
        ["Historiography of taste", "Traces how aesthetic judgments about specific artworks or styles have shifted over time"],
    ])},
    "art-history-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Museum studies", "Examines the institutional practices and politics shaping how museums collect, display, and interpret art"],
        ["Politics of collection formation", "Museum collections reflect historical power relations and choices, not a neutral or complete record of art"],
    ])},
    "art-history-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Connoisseurial attribution dispute", "Disagreements among experts about which artist actually created a given artwork"],
        ["Old Master painting", "Attribution disputes are especially consequential for Old Master paintings given the significant value differences between attributions"],
    ])},
    "art-history-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Orientalism (art history)", "Edward Said's critique of how Western art depicted the Middle East and Asia through often stereotyped, exoticized imagery"],
        ["Nineteenth-century painting", "Applied to analyze how 19th-century Orientalist painters constructed romanticized, often inaccurate images of the 'East'"],
    ])},
    "art-history-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Gender and patronage", "Examines how gender shaped who could commission, produce, and be depicted in early modern art"],
        ["Early modern commissioning", "Reveals how women patrons navigated and sometimes challenged predominantly male-controlled artistic commissioning structures"],
    ])},
    "art-history-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Destroyed or lost works", "Artworks known only through documentary evidence, having been physically lost, destroyed, or never survived"],
        ["Methodological approach", "Reconstructs likely appearance and significance from written descriptions, copies, and preparatory studies"],
    ])},
    "art-history-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Ekphrasis", "A literary description of a visual artwork, historically used both as a rhetorical exercise and an art historical source"],
        ["Literary history application", "Ekphrastic texts can provide valuable evidence about artworks whose original appearance is otherwise poorly documented"],
    ])},
    "art-history-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Social history of art (Hauser and Clark)", "Analyzes art as fundamentally shaped by and reflective of its social and economic context"],
        ["Contemporary reconsideration", "Later scholars have both built on and critiqued their sometimes deterministic linking of social class to artistic style"],
    ])},
    "art-history-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Iconoclasm", "The deliberate destruction of images or monuments, often for religious or political reasons"],
        ["Image destruction history", "Studying iconoclastic episodes reveals what specific meanings and threats contemporaries attributed to images"],
    ])},
    "art-history-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Workshop practice", "The collaborative production system common in Renaissance studios, where a master oversaw assistants completing parts of a work"],
        ["Collaborative authorship", "Complicates simple single-artist attribution, since many Renaissance works involved substantial workshop contribution"],
    ])},
    "art-history-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Print culture", "The production and circulation of printed images, which dramatically expanded visual imagery's reach"],
        ["Dissemination of visual ideas", "Prints allowed compositions and motifs to spread rapidly across regions far beyond a single painting's physical location"],
    ])},
    "art-history-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Grand Tour", "A traditional travel itinerary through Europe undertaken by young elites, especially British aristocrats, from the 17th century onward"],
        ["Western taste formation", "Significantly shaped which classical and Renaissance artworks became canonically valued in Western art history"],
    ])},
    "art-history-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Marxist art theory", "Analyzes art production and patronage as shaped by underlying economic relations and class structures"],
        ["Application", "Examines how an artwork's material conditions of production relate to broader economic and social power structures"],
    ])},
    "art-history-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Psychoanalytic art interpretation", "Applies psychoanalytic theory to interpret unconscious symbolic content in artworks or artists' biographies"],
        ["Application", "Has been used to analyze recurring motifs and themes as expressions of psychological states or unconscious drives"],
    ])},
    "art-history-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Primitivism", "The modernist fascination with and appropriation of non-Western art forms, viewed as more 'authentic' or 'primitive'"],
        ["Historiography", "Increasingly critiqued for its often exploitative and reductive framing of non-Western artistic traditions"],
    ])},
    "art-history-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Comparative iconography", "Analyzes shared or divergent symbolic motifs across different religious and cultural artistic traditions"],
        ["Application", "Reveals both cross-cultural visual exchange and culturally specific symbolic meanings attached to similar imagery"],
    ])},
    "art-history-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Restitution", "The return of cultural objects to their country or community of origin"],
        ["Repatriation ethics", "Involves complex debates over historical acquisition legitimacy, cultural ownership, and museum stewardship"],
    ])},
    "art-history-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Archival methods", "Systematic research techniques for locating and interpreting primary historical documents"],
        ["Artist biography reconstruction", "Archival records like contracts and payment records help reconstruct otherwise poorly documented artists' lives and careers"],
    ])},
    "art-history-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Art historical photography", "The historical use of photographic reproduction as a research and teaching tool in art history"],
        ["Photography as evidence", "Early photographic documentation preserved records of artworks later damaged, lost, or altered"],
    ])},
    "art-history-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Cartographic history", "Studies maps as both functional documents and artistic, culturally meaningful objects"],
        ["Early modern mapmaking", "Early modern maps combined empirical geographic knowledge with decorative and ideological visual elements"],
    ])},
    "art-history-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Guild system", "Historical organizations regulating training, quality, and membership within a specific craft or artistic trade"],
        ["Artistic production regulation", "Guild membership requirements significantly shaped who could formally practice as an artist in many historical periods"],
    ])},
    "art-history-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Old Master category", "A traditional classification for major European painters working roughly before 1800"],
        ["Historiography of the category", "The category itself is now examined critically for the value judgments and exclusions embedded in its formation"],
    ])},
    "art-history-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Color theory history", "Traces the evolving understanding of color from Alberti's early treatises to Chevreul's scientific color theory"],
        ["Alberti to Chevreul", "Shows the gradual shift from artistic and philosophical color theory toward scientific and perceptual color analysis"],
    ])},
    "art-history-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Perspective system", "Techniques for representing three-dimensional space on a two-dimensional surface"],
        ["Cultural variant", "Different artistic traditions developed distinct, culturally specific approaches to representing spatial depth"],
    ])},
    "art-history-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Byzantine icon reception", "Studies how Western art history has historically interpreted and valued Byzantine religious icon painting"],
        ["Western reception history", "Byzantine icons were long marginalized in Western canon formation, valued mainly for anticipating later Western developments"],
    ])},
    "art-history-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Photography's historiographic challenge", "Photography's emergence disrupted painting's traditional claim to privileged representational authority"],
        ["Painting's primacy", "Forced art history to reconsider its historical hierarchy privileging painting over other visual media"],
    ])},
    "art-history-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Ephemeral and performance-based work", "Art forms that exist only temporarily or through live enactment, lacking a permanent physical object"],
        ["Methodological challenge", "Requires art historical methods relying on documentation, testimony, and reperformance rather than direct object analysis"],
    ])},
    "art-history-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Frankfurt School", "A group of critical theorists analyzing how culture and mass media can reinforce dominant ideology"],
        ["Critique of cultural production", "Applied critical theory to examine how artistic and cultural production relates to broader systems of social power"],
    ])},
    "art-history-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["East Asian painting historiography", "Compares how different scholarly traditions have interpreted and categorized East Asian painting"],
        ["Comparative approach", "Reveals differing indigenous versus Western frameworks for periodizing and evaluating East Asian art"],
    ])},
    "art-history-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Art restoration ethics", "Examines the philosophical and practical principles guiding how damaged or aged artworks should be conserved"],
        ["History of practice", "Restoration approaches have shifted significantly, from aggressive repainting toward minimal, reversible intervention"],
    ])},
    "art-history-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Court art", "Artworks produced for and displayed within a royal or aristocratic court"],
        ["Iconography of political legitimacy", "Court art frequently employed specific visual symbols to visually assert and reinforce a ruler's legitimate authority"],
    ])},
    "art-history-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Folk and vernacular art", "Art produced outside formal academic or elite artistic institutions, often by anonymous or untrained makers"],
        ["Historiography", "The category's boundaries and value have been contested, particularly regarding its historical exclusion from the fine art canon"],
    ])},
    "art-history-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora and displacement", "Examines how migration and forced displacement have shaped the history of art collecting"],
        ["Collecting history", "Reveals how diasporic communities' relationships to art objects intersect with broader histories of displacement"],
    ])},
    "art-history-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Structuralism (art history)", "Analyzes artworks as governed by underlying systematic structures of meaning, similar to language"],
        ["Post-structuralist debate", "Later theorists challenged structuralism's assumption of stable, fully recoverable underlying meaning systems"],
    ])},
    "art-history-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Women artists' recovery project", "Scholarly efforts to research and reintegrate historically overlooked women artists into art history"],
        ["Historiography", "Reflects a broader methodological shift toward correcting historical gaps and biases in the traditional canon"],
    ])},
    "art-history-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Anonymous master", "An artist known only through a body of attributed work, without a securely documented historical name"],
        ["Study methodology", "Scholars group and analyze stylistically related works under a conventional working name pending further attribution research"],
    ])},
    "art-history-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Art criticism", "Written evaluative and interpretive commentary on contemporary or historical art"],
        ["Literary genre history", "Art criticism developed its own distinct literary conventions and rhetorical strategies over its historical development"],
    ])},
    "art-history-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Trade route", "Historical pathways of commercial exchange that also facilitated the circulation of artistic motifs and techniques"],
        ["Artistic motif circulation", "Reveals how visual ideas traveled across vast distances well before modern global communication"],
    ])},
    "art-history-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Antiquarianism", "The early modern scholarly study and collection of ancient artifacts and ruins"],
        ["Historiography of ruins", "Antiquarian interest in ruins directly shaped the later development of formal archaeology and art history"],
    ])},
    "art-history-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Gender performance", "Analyzes how portraits construct and display gendered identity through pose, costume, and setting"],
        ["Historical portraiture analysis", "Reveals how gender norms were actively constructed and performed rather than simply reflected in period portraiture"],
    ])},
    "art-history-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Art market history", "Studies how commercial markets have historically shaped which artists and works became critically valued"],
        ["Canonical value formation", "Market forces and canonical art historical judgment have long been intertwined rather than fully independent"],
    ])},
    "art-history-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Ottoman court painting", "Painting produced for and within the Ottoman imperial court, including illustrated manuscripts"],
        ["Western reception historiography", "Western scholarship has historically both understudied and, at times, misread Ottoman court painting through European stylistic frameworks"],
    ])},
    "art-history-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Prehistoric cave art", "Some of the earliest known human visual imagery, found in caves such as Lascaux and Chauvet"],
        ["Interpretation historiography", "Scholarly interpretations have shifted from simple hunting-magic explanations toward more complex ritual and cognitive theories"],
    ])},
    "art-history-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Iconographic program", "A coordinated, deliberately planned system of imagery across a building's decoration, conveying a unified meaning"],
        ["Medieval cathedral sculpture", "Cathedral sculptural programs typically encoded complex theological narratives readable across the entire building"],
    ])},
    "art-history-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Slide library", "Historical collections of photographic slides used for art historical teaching before digital image databases"],
        ["Teaching tool history", "Reveals how the physical infrastructure of art historical pedagogy has shaped which images were widely studied and taught"],
    ])},
    "art-history-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Islamic art scholarship", "Compares how different scholarly traditions have historically categorized and interpreted Islamic art"],
        ["Comparative historiography", "Reveals tensions between regional specificity and treating 'Islamic art' as a single unified category"],
    ])},
    "art-history-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Classical antiquity reception", "Studies how Renaissance artists interpreted and revived ancient Greek and Roman artistic models"],
        ["Reception history", "Renaissance engagement with antiquity often involved selective reinterpretation rather than straightforward copying"],
    ])},
    "art-history-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Textile and decorative arts", "Art historical study of media like textiles, ceramics, and furniture, historically undervalued relative to painting"],
        ["Methodological approach", "Requires attention to material properties and functional use alongside traditional stylistic analysis"],
    ])},
    "art-history-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["National canon formation", "The process by which particular artists and works became designated as representative of a national artistic tradition"],
        ["Politics of canon", "National canon formation often served explicit political purposes of constructing shared cultural identity"],
    ])},
    "art-history-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Iconography of death", "Analyzes recurring visual symbols representing mortality in early modern art, such as memento mori imagery"],
        ["Early modern application", "Death iconography served both religious devotional and moral didactic purposes in period artistic production"],
    ])},
    "art-history-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Academic salon system", "The historical institutional structure by which official art academies exhibited and juried contemporary art"],
        ["Historiography", "The salon system significantly shaped which artists achieved official recognition prior to its later decline"],
    ])},
    "art-history-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Silk Road exchange", "The historical trade network connecting East Asia, Central Asia, and Europe, facilitating artistic and cultural exchange"],
        ["Cross-cultural production", "Silk Road exchange produced hybrid artistic styles reflecting the diverse cultures connected along its routes"],
    ])},
    "art-history-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Print connoisseurship", "The specialized practice of attributing, dating, and evaluating printed images"],
        ["Print room practice", "Historical museum print rooms developed distinct curatorial and study practices specific to works on paper"],
    ])},
    "art-history-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Lost architectural decoration", "Decorative programs (frescoes, sculpture) that no longer survive on their original buildings"],
        ["Reconstruction method", "Scholars use documentary sources, fragments, and comparative examples to reconstruct likely original appearance"],
    ])},
    "art-history-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Latin American colonial art", "Art produced in Spanish and Portuguese colonial territories, often blending European and Indigenous traditions"],
        ["Historiography", "Increasingly studied for its distinctive hybrid character rather than merely as a derivative of European models"],
    ])},
    "art-history-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Ecclesiastical patronage", "Art commissioning networks organized around church institutions and religious authorities"],
        ["Medieval production networks", "Religious institutions were major art patrons in medieval Europe, shaping much of the era's artistic output"],
    ])},
    "art-history-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["African art reception", "Examines how early 20th-century European artists and audiences encountered and interpreted African art"],
        ["Early twentieth-century Europe", "Often filtered through primitivist and colonial frameworks that distorted the original cultural context of African objects"],
    ])},
    "art-history-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Domestic and decorative interior study", "Examines the art historical significance of household objects and interior decoration"],
        ["Methodological approach", "Requires attention to how objects functioned within lived domestic space, not just as isolated aesthetic objects"],
    ])},
    "art-history-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Periodization historiography", "Examines the art historical practice of dividing history into named periods (Renaissance, Baroque, etc.) as itself a constructed scholarly choice"],
        ["Critical reflection", "Period categories are increasingly recognized as scholarly constructs imposed after the fact, not neutral historical facts"],
    ])},
    "art-history-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Manuscript illumination", "The historical practice of hand-decorating manuscript pages with painted images and ornament"],
        ["Comparative study", "Compares illumination traditions across different regions and religious contexts, revealing shared and distinct visual conventions"],
    ])},
    "art-history-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Copying in artistic training", "The historical practice of copying earlier master works as a fundamental part of an artist's training"],
        ["Replication history", "Copying served both pedagogical purposes and produced valued works in their own right within many artistic traditions"],
    ])},
    "art-history-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Allegory in Baroque ceiling painting", "Complex symbolic imagery representing abstract concepts, often used in large-scale Baroque decorative schemes"],
        ["Iconographic analysis", "Requires decoding often elaborate symbolic programs intended to convey specific political or religious messages"],
    ])},
    "art-history-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Art historical fieldwork", "Direct, in-person study of artworks and sites, as distinct from studying reproductions alone"],
        ["Site visit historiography", "The practice and value of firsthand site visits has evolved alongside the availability of photographic and digital reproductions"],
    ])},
    "art-history-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Cabinet of curiosities", "An early modern private collection combining natural specimens, artworks, and exotic objects"],
        ["Collecting practice", "A precursor to the modern museum, reflecting early modern approaches to categorizing and displaying diverse knowledge"],
    ])},
    "art-history-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Art and empire", "Examines how colonial exhibitions displayed art and artifacts to represent and justify imperial power"],
        ["Colonial exhibition historiography", "Colonial exhibitions often decontextualized non-Western objects to serve imperial narratives of civilization and progress"],
    ])},
    "art-history-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Gender and guild restriction", "Historical guild rules that formally or informally excluded women from full membership and training"],
        ["Historical workshop", "Significantly limited women's documented participation in many periods of formal artistic production"],
    ])},
    "art-history-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Art historical journal", "Academic publications through which art historical research is formally disseminated and validated"],
        ["Peer review history", "The development of formal peer review shaped how art historical scholarship's credibility and consensus have been established"],
    ])},
    "art-history-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Pre-Columbian art scholarship", "Studies the art of the Americas before European contact"],
        ["Comparative historiography", "Scholarship has shifted from framing Pre-Columbian art through European aesthetic categories toward indigenous frameworks"],
    ])},
    "art-history-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Ancient Near Eastern relief sculpture", "Carved stone imagery from ancient Mesopotamian and related civilizations, often depicting rulers"],
        ["Iconography of power", "Relief sculpture frequently encoded specific visual conventions asserting a ruler's military and divine legitimacy"],
    ])},
    "art-history-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Art restitution legal framework", "The evolving body of international and national law governing the return of cultural property"],
        ["Historiography", "Legal frameworks have developed significantly since mid-20th-century conventions on cultural property protection"],
    ])},
    "art-history-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Popular print culture", "Widely circulated, often anonymously produced printed images intended for a broad, non-elite audience"],
        ["Methodological approach", "Requires different analytical tools than fine art connoisseurship, given the anonymous, mass-produced nature of the material"],
    ])},
    "art-history-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Egyptian art reception", "Studies how Western scholarship has historically interpreted ancient Egyptian art"],
        ["Western scholarship history", "Early Western reception often filtered Egyptian art through classical aesthetic standards rather than its own context"],
    ])},
    "art-history-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Connoisseurship versus scientific dating", "Compares traditional stylistic attribution methods against modern scientific dating techniques"],
        ["Comparative methodology", "Scientific methods like dendrochronology can independently confirm or challenge attributions made on purely stylistic grounds"],
    ])},
    "art-history-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["South Asian court miniature painting", "Small-scale, detailed painting produced for South Asian royal courts, notably Mughal and Rajput traditions"],
        ["Historiography", "Scholarship has increasingly recovered the distinct regional schools and workshop practices within this broad tradition"],
    ])},
    "art-history-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Devotional object function", "Examines how religious objects were actually used in ritual practice, not just their visual appearance"],
        ["Methodological approach", "Requires attention to an object's functional and ritual context alongside its formal artistic qualities"],
    ])},
    "art-history-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Copyright and reproduction rights", "The historical development of legal rights governing the reproduction of artworks and images"],
        ["Art history application", "Copyright law significantly affects how freely art historians can reproduce images in scholarship and teaching"],
    ])},
    "art-history-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Aboriginal Australian art scholarship", "Studies the art historical treatment of Aboriginal Australian artistic traditions"],
        ["Comparative historiography", "Scholarship increasingly engages with Aboriginal frameworks for understanding art's relationship to land and law"],
    ])},
    "art-history-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Public monument controversy", "Debates over the meaning, removal, or recontextualization of public monuments"],
        ["Historiography", "Reflects broader ongoing debates about how societies should publicly commemorate contested historical figures and events"],
    ])},
    "art-history-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Renaissance palazzo fresco cycle", "Large-scale painted decorative programs within Renaissance palace interiors"],
        ["Iconographic program", "Often encoded specific political, dynastic, or moral messages tailored to the palace owner's status and aspirations"],
    ])},
    "art-history-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Connoisseur archive", "Personal research notes and records kept by art historical connoisseurs, valuable as primary source material"],
        ["Fieldnote historiography", "Studying these archives reveals the actual working methods and reasoning behind historical attribution judgments"],
    ])},
    "art-history-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Andean textile iconography", "The symbolic visual systems embedded in historical Andean textile production"],
        ["Comparative historiography", "Compares different scholarly approaches to interpreting the complex symbolic systems within Andean weaving traditions"],
    ])},
    "art-history-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Exhibition catalogue", "Publications accompanying art exhibitions that document and interpret the displayed works"],
        ["Historiography", "Exhibition catalogues have themselves become important primary sources for tracking shifts in art historical interpretation over time"],
    ])},
    "art-history-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Renaissance domestic devotional imagery", "Small-scale religious images intended for private household worship in Renaissance homes"],
        ["Gender and iconography", "Reveals gendered patterns in how domestic devotional objects were commissioned, used, and depicted"],
    ])},
    "art-history-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Aztec and Maya art reception", "Studies how modern scholarship has interpreted and valued ancient Aztec and Maya artistic production"],
        ["Reception history", "Modern scholarship increasingly emphasizes understanding these traditions on their own cultural and religious terms"],
    ])},
    "art-history-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Dissertation methodology", "The structured process of constructing and defending an original, evidence-based art historical argument"],
        ["Original argument construction", "Requires identifying a genuine gap in existing scholarship and building a rigorously supported new interpretive claim"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art History"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"art-history-m2-l{base_n}"
        worked_key = f"art-history-m2-l{worked_n}"
        if base_n == 3:
            CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
        elif base_key in CHARTS:
            CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Missing lesson ids: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Art History lessons.")


if __name__ == "__main__":
    main()
