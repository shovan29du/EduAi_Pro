#!/usr/bin/env python3
"""Populate the "Prophets & Religious Figures in the Quran" biography
category: the 25 prophets named in the Quran, plus Mary and 14 other
foundational early figures of Islam (Muhammad's family, the four Rightly
Guided Caliphs, and the founders of the four major Sunni schools of law).

This is a distinct, dedicated collection focused specifically on how these
figures are presented in the Quran and Islamic tradition -- three of these
individuals (Moses, Jesus, Muhammad) also have separate, more general
biographical entries in the Philosophy & Religion category; the entries
here are deliberately framed around their specific role in the Quranic
narrative rather than duplicating that prose.

Framing note (respecting the request "according to the Quran"): for
figures whose primary historical record is scriptural rather than
independent archaeological/historical documentation (all 25 named
prophets), facts are phrased as "According to the Quran..." or "Islamic
tradition holds..." rather than asserted as uncontested secular history.
For the later, well-documented historical figures (Muhammad's
companions, the Caliphs, the four Imams, 7th-9th century CE), verifiable
historical facts (dates, events) are stated directly, while purely
theological or miraculous claims are still attributed to belief/tradition.

Re-run after editing:
    python3 backend/scripts/generate_biographies_quran_prophets.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="prophet_adam", name="Adam", years="not historically dated", nationality="—",
        field="prophet in Islamic tradition", wiki_title="Adam in Islam",
        significance="according to the Quran, Adam was the first human being and the first prophet, created by God and taught the names of all things",
        facts=[
            "The Quran describes Adam as the first human being, created by God from clay and honored above other creation",
            "According to the Quran, God commanded the angels to bow to Adam, and all obeyed except Iblis (Satan), who refused out of pride",
            "The Quran describes God teaching Adam 'the names of all things', a sign of the knowledge given to humanity",
            "According to the Quran, Adam and his wife were placed in a garden but were deceived by Satan into eating from a forbidden tree, after which they were sent down to Earth",
            "Islamic tradition holds that Adam repented and that God accepted his repentance, a story used in Islamic teaching to illustrate that sincere repentance is always accepted",
            "Adam is regarded in Islam as the first prophet (nabi), given guidance to pass on to his descendants",
            "Adam is also a shared figure in Judaism and Christianity, appearing in the Book of Genesis as the first man created by God",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_idris", name="Idris (Enoch)", years="not historically dated", nationality="—",
        field="prophet in Islamic tradition", wiki_title="Idris",
        significance="the Quran describes Idris as a truthful man and prophet who was raised by God to a high station, and Islamic tradition often identifies him with the biblical Enoch",
        facts=[
            "Idris is mentioned by name twice in the Quran, in Surah Maryam and Surah Al-Anbiya",
            "The Quran describes him as 'truthful' (siddiq) and a prophet",
            "The Quran states that God 'raised him to a high station', a verse Islamic scholars have interpreted in various ways over the centuries",
            "Islamic tradition often identifies Idris with the biblical figure Enoch, described in the Book of Genesis as having 'walked with God'",
            "Later Islamic tradition, drawing on extra-Quranic sources, associates Idris with early knowledge of writing, astronomy, and mathematics, though these details are not found directly in the Quran itself",
            "He is counted among the prophets who lived before Noah, in the earliest period of the Quranic prophetic narrative",
            "His story in Islamic teaching is often used to illustrate the reward for truthfulness and steadfast devotion",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_nuh", name="Nuh (Noah)", years="not historically dated", nationality="—",
        field="prophet in Islamic tradition", wiki_title="Noah",
        significance="according to the Quran, Nuh preached to his people for centuries calling them to worship God alone, and was eventually commanded to build an ark to save the believers from a great flood",
        facts=[
            "Nuh is mentioned extensively in the Quran, and an entire chapter, Surah Nuh, is named after him",
            "According to the Quran, Nuh called his people to abandon idol worship and worship God alone, but most of them rejected his message for many generations",
            "The Quran states that Nuh preached for 950 years, a span emphasized in Islamic teaching to illustrate extraordinary patience in the face of rejection",
            "According to the Quran, God commanded Nuh to build an ark, and a great flood came that destroyed the disbelievers while the ark carried Nuh, his believing followers, and pairs of animals to safety",
            "The Quran recounts that even one of Nuh's own sons refused to board the ark and was among those who perished",
            "The story of Nuh and the ark is shared, with variations, across Judaism, Christianity, and Islam, and appears in the Book of Genesis as well as the Quran",
            "In Islamic teaching, Nuh's story is often cited as a model of patient, persistent preaching in the face of widespread rejection",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_hud", name="Hud", years="not historically dated", nationality="Arabian ('Ad tribe)",
        field="prophet in Islamic tradition", wiki_title="Hud (prophet)",
        significance="according to the Quran, Hud was sent to the people of 'Ad, a powerful ancient Arabian tribe, warning them against idolatry before they were destroyed by a violent windstorm",
        facts=[
            "Hud is named in the Quran, and Surah Hud, the eleventh chapter, is named after him",
            "According to the Quran, he was sent to the tribe of 'Ad, described as a physically powerful ancient Arabian people known for their skill in building",
            "The Quran describes Hud calling his people away from idol worship toward the worship of one God, but they largely rejected him and accused him of madness",
            "According to the Quran, the 'Ad were eventually destroyed by a violent, howling windstorm that lasted several days as punishment for their persistent rejection and arrogance",
            "The Quran describes Hud and the believers who accepted his message as having been saved before the destruction came",
            "The location and precise historical identity of the 'Ad people remain a subject of scholarly and archaeological discussion, with some researchers connecting references to the 'lost city of Iram' mentioned in the Quran to ancient South Arabian sites",
            "In Islamic teaching, the story of Hud is used to illustrate the consequences of arrogance and rejecting sincere warning",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_salih", name="Salih", years="not historically dated", nationality="Arabian (Thamud tribe)",
        field="prophet in Islamic tradition", wiki_title="Salih",
        significance="according to the Quran, Salih was sent to the Thamud people with a miraculous she-camel as a sign, but his people killed the camel and were subsequently destroyed",
        facts=[
            "Salih is named in the Quran and sent, according to the text, to the tribe of Thamud, described as skilled builders who carved dwellings into mountains",
            "According to the Quran, Salih called the Thamud to worship God alone and presented a she-camel as a divine sign, instructing the people not to harm it",
            "The Quran recounts that a group among the Thamud killed the she-camel in defiance, an act treated in the text as a grave transgression",
            "According to the Quran, the Thamud were subsequently struck by a devastating punishment, often described as a violent earthquake or blast, three days after they killed the camel",
            "Salih and the believers who followed him are described in the Quran as having been spared from the destruction",
            "The ancient rock-carved dwellings at Mada'in Salih (Al-Hijr), in present-day Saudi Arabia, are traditionally associated with the Thamud people in Islamic and regional tradition, and the site is now a UNESCO World Heritage Site",
            "In Islamic teaching, the story of Salih is used to illustrate the seriousness of violating a clear divine sign or covenant",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_ibrahim", name="Ibrahim (Abraham)", years="not historically dated", nationality="Mesopotamian/Levantine",
        field="prophet in Islamic tradition", wiki_title="Abraham",
        significance="regarded in the Quran as a central model of faith and monotheism, Ibrahim is described as having rebuilt the Kaaba in Mecca and is honored as the patriarchal figure common to Islam, Christianity, and Judaism",
        facts=[
            "Ibrahim is mentioned more often in the Quran than any other prophet, and Surah Ibrahim is named after him",
            "According to the Quran, Ibrahim questioned the idol worship of his own father and people from a young age, reasoning his way toward belief in one God through observing the sun, moon, and stars",
            "The Quran recounts that Ibrahim destroyed his people's idols and was thrown into a fire as punishment, but God commanded the fire to be 'cool and safe' for him, and he was unharmed",
            "According to the Quran, Ibrahim was tested with a command to sacrifice his son -- in Islamic tradition generally understood to be Ismail -- and both submitted to God's will before God provided a ram as a substitute sacrifice",
            "The Quran states that Ibrahim and his son Ismail raised the foundations of the Kaaba in Mecca, the building at the center of Muslim daily prayer direction and the annual Hajj pilgrimage",
            "Ibrahim is described in the Quran with the title 'khalil Allah', meaning 'friend of God'",
            "Ibrahim is also the shared patriarchal figure of Judaism (as Abraham) and Christianity, and the term 'Abrahamic religions' refers to the three faiths that trace their lineage of monotheistic belief back to him",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="prophet_lut", name="Lut (Lot)", years="not historically dated", nationality="Mesopotamian/Levantine",
        field="prophet in Islamic tradition", wiki_title="Lot (biblical person)",
        significance="according to the Quran, Lut was sent to warn the people of the cities of Sodom and Gomorrah against widespread sin and injustice before those cities were destroyed",
        facts=[
            "Lut is named in the Quran and described as a nephew of Ibrahim who was also given prophethood",
            "According to the Quran, Lut was sent to a community, traditionally identified with Sodom and Gomorrah, that was engaged in behavior the text describes as unprecedented moral transgression",
            "The Quran describes Lut warning his people repeatedly, but they rejected his message and threatened to expel him",
            "According to the Quran, angels visited Lut in human form, and his community's hostile response to the visitors was part of what confirmed the severity of their wrongdoing",
            "The Quran recounts that Lut and his believing family, except for his wife, were instructed to leave the city before it was destroyed by an overturning catastrophe, often described as a rain of stones",
            "The story of Lut parallels the account of Sodom and Gomorrah found in the Hebrew Bible's Book of Genesis, with both traditions treating the story as a warning against injustice and moral corruption",
            "In Islamic teaching, the story of Lut is used to illustrate that prophetic warning is extended even to communities engaged in severe wrongdoing, and that divine judgment follows persistent, unrepentant rejection",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_ismail", name="Ismail (Ishmael)", years="not historically dated", nationality="Arabian",
        field="prophet in Islamic tradition", wiki_title="Ishmael",
        significance="the elder son of Ibrahim, Ismail is honored in Islamic tradition for his willing submission to sacrifice and for helping his father rebuild the Kaaba, and is regarded as an ancestor of the Arab peoples",
        facts=[
            "Ismail is named in the Quran as a prophet and as the son of Ibrahim, born to Hajar (Hagar)",
            "According to Islamic tradition, Ibrahim settled Hajar and the infant Ismail near the site of what would become Mecca, and Hajar's desperate search for water there is commemorated today in the Hajj ritual of sa'i, walking between the hills of Safa and Marwah",
            "The well of Zamzam, which Islamic tradition holds sprang forth to save the infant Ismail from thirst, remains a site of religious significance at the Grand Mosque in Mecca today",
            "According to the Quran, Ismail is widely understood in Islamic tradition to be the son Ibrahim was commanded to sacrifice, and Ismail is described as submitting willingly to his father's account of the divine command",
            "The Quran describes Ismail helping his father Ibrahim raise the foundations of the Kaaba",
            "Ismail is traditionally regarded as an ancestor of the Arab peoples, and Islamic genealogical tradition traces the Prophet Muhammad's lineage back to him",
            "The annual ritual of animal sacrifice performed by Muslims during Eid al-Adha commemorates the account of Ibrahim's willingness to sacrifice his son and God's provision of a ram instead",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_ishaq", name="Ishaq (Isaac)", years="not historically dated", nationality="Levantine",
        field="prophet in Islamic tradition", wiki_title="Isaac",
        significance="the younger son of Ibrahim, Ishaq is honored in the Quran as a prophet and is regarded as an ancestor of the Israelite line of prophets that continues through Yaqub, Yusuf, and later figures",
        facts=[
            "Ishaq is named in the Quran as a prophet and the son of Ibrahim and his wife Sarah",
            "According to the Quran, angels brought Ibrahim and Sarah the news of Ishaq's coming birth, a moment described in the text as a joyful but astonishing announcement given their advanced age",
            "Ishaq is described in the Quran as righteous and blessed, continuing the prophetic line established through his father",
            "Islamic tradition holds Ishaq as the ancestor of the line of Israelite prophets, since his son Yaqub (Jacob) is also called Israel, from whom the Children of Israel take their name",
            "The Quran groups Ibrahim, Ismail, and Ishaq together repeatedly as models of righteous monotheistic faith",
            "Ishaq is also a shared figure across Judaism and Christianity, appearing as Isaac in the Hebrew Bible's Book of Genesis as the son through whom the covenant with Abraham's descendants continued",
            "In Islamic teaching, Ishaq's story is presented alongside his father's and brother's as an example of a family devoted across generations to monotheistic worship",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_yaqub", name="Yaqub (Jacob)", years="not historically dated", nationality="Levantine",
        field="prophet in Islamic tradition", wiki_title="Jacob",
        significance="according to the Quran, Yaqub, also called Israel, was the son of Ishaq and the father of twelve sons including Yusuf, and his patient grief over Yusuf's disappearance is a central emotional thread of the Quran's Surah Yusuf",
        facts=[
            "Yaqub is named in the Quran as a prophet, the son of Ishaq and grandson of Ibrahim",
            "According to Islamic and Jewish tradition, Yaqub was also given the name Israel, and his twelve sons became the ancestors of the twelve tribes of the Children of Israel",
            "The Quran's Surah Yusuf recounts that Yaqub deeply loved his son Yusuf, which caused jealousy among Yusuf's brothers who plotted against him",
            "According to the Quran, Yaqub grieved intensely over Yusuf's disappearance for many years, weeping until, the text states, his eyes turned white with sorrow, while never losing hope in God",
            "The Quran recounts that Yaqub's sight was restored when Yusuf's shirt was placed over his face, following the family's eventual joyful reunion in Egypt",
            "Yaqub's patience and unwavering faith throughout his prolonged grief are highlighted in Islamic teaching as a model of sabr, patient endurance trusting in God",
            "Yaqub is a shared figure across Judaism, Christianity, and Islam, appearing extensively in the Hebrew Bible's Book of Genesis",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_yusuf", name="Yusuf (Joseph)", years="not historically dated", nationality="Levantine/Egyptian",
        field="prophet in Islamic tradition", wiki_title="Joseph (Genesis)",
        significance="the Quran's Surah Yusuf tells his complete life story as a single unified narrative, from being sold into slavery by his own brothers to becoming a trusted minister of Egypt, describing the account as 'the best of stories'",
        facts=[
            "Yusuf is the subject of Surah Yusuf, the twelfth chapter of the Quran, which the text itself introduces as 'the best of stories'",
            "According to the Quran, Yusuf's brothers, jealous of their father's love for him, threw him into a well and told their father he had been killed by a wolf",
            "The Quran recounts that Yusuf was found by travelers, sold into slavery, and taken to Egypt, where he was purchased by a nobleman",
            "According to the Quran, Yusuf resisted an attempt at seduction by his master's wife and was subsequently imprisoned despite his innocence, where he became known for interpreting dreams",
            "The Quran describes Yusuf correctly interpreting the Egyptian king's dream about seven years of abundance followed by seven years of famine, leading to his appointment overseeing Egypt's grain stores",
            "According to the Quran, Yusuf's brothers eventually came to Egypt seeking grain during the famine, not recognizing him, and he ultimately revealed his identity and forgave them",
            "The story concludes with Yaqub and the whole family reuniting with Yusuf in Egypt, and it is widely regarded, across Islamic, Jewish, and Christian tradition alike, as one of the most detailed and emotionally developed narratives in scripture",
        ], related_subjects=["World Religions", "Islamic Studies", "World Literature"],
    ),
    dict(
        id="prophet_ayyub", name="Ayyub (Job)", years="not historically dated", nationality="Levantine",
        field="prophet in Islamic tradition", wiki_title="Job (biblical figure)",
        significance="according to the Quran, Ayyub endured prolonged severe illness and hardship with unwavering patience and faith, and his story is a central Islamic symbol of steadfastness through suffering",
        facts=[
            "Ayyub is named in the Quran as a prophet who endured a long period of severe illness, loss, and hardship",
            "According to the Quran, Ayyub called upon God, saying that affliction had touched him, but 'You are the Most Merciful of the merciful', a prayer widely quoted in Islamic teaching on patience",
            "The Quran describes God responding to Ayyub's prayer by relieving his affliction and restoring what he had lost, along with additional mercy",
            "Islamic tradition, drawing on both the Quran and extra-Quranic accounts, holds that Ayyub bore his suffering for many years without complaint against God, becoming a model of sabr (patient perseverance)",
            "The Quran instructs believers, in reference to Ayyub, to remember him as an excellent servant who was 'ever returning to God'",
            "Ayyub is a shared figure across Judaism, Christianity, and Islam, corresponding to Job in the Hebrew Bible's Book of Job, which similarly explores the theme of suffering and faith",
            "In Islamic teaching, the story of Ayyub is frequently cited to encourage patience and trust in God during illness or hardship",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_shuayb", name="Shuayb", years="not historically dated", nationality="Arabian (Midian)",
        field="prophet in Islamic tradition", wiki_title="Shuayb",
        significance="according to the Quran, Shuayb was sent to the people of Madyan (Midian) to call them away from fraudulent trade practices and idolatry, and is sometimes associated by scholars with the biblical Jethro",
        facts=[
            "Shuayb is named in the Quran and sent, according to the text, to the people of Madyan (Midian), a community in northwestern Arabia",
            "According to the Quran, Shuayb specifically condemned dishonest business practices among his people, including giving short measure and weight in trade",
            "The Quran describes Shuayb calling his people to worship God alone and to deal justly and honestly with one another in commerce",
            "According to the Quran, the people of Madyan largely rejected Shuayb's message and were subsequently struck by a devastating punishment, described in different Quranic passages as an earthquake or a scorching blast",
            "Some Islamic scholars have historically associated Shuayb with Jethro, the father-in-law of Moses mentioned in the Hebrew Bible, though this identification is a matter of scholarly discussion rather than explicit Quranic statement",
            "The Quran describes Shuayb as speaking to his people with notable eloquence and patience despite their rejection",
            "In Islamic teaching, the story of Shuayb is frequently used to emphasize the importance of honesty and fairness in economic dealings",
        ], related_subjects=["World Religions", "Islamic Studies", "Business Studies"],
    ),
    dict(
        id="prophet_musa_quran", name="Musa (Moses)", years="not historically dated", nationality="Egyptian/Israelite",
        field="prophet in Islamic tradition", wiki_title="Moses in Islam",
        significance="Musa is the prophet mentioned most frequently in the Quran, and his confrontation with Pharaoh, the parting of the sea, and receiving revelation on Mount Sinai form one of the Quran's most extensively retold prophetic narratives",
        facts=[
            "Musa is mentioned by name more often in the Quran than any other prophet, with his story recounted across many chapters, most extensively in Surah Al-Qasas and Surah Ta-Ha",
            "According to the Quran, Musa was raised in the household of Pharaoh after his mother, fearing for his life under a decree to kill Israelite infant boys, placed him in a basket on the river",
            "The Quran recounts that God spoke directly to Musa at the burning bush on Mount Sinai (Tur Sina) and commanded him to confront Pharaoh and free the Israelites from oppression",
            "According to the Quran, Musa's staff was transformed into a serpent as one of several miraculous signs given to him to demonstrate the truth of his message before Pharaoh and his magicians",
            "The Quran describes the sea parting to allow Musa and the Israelites to escape, with Pharaoh and his army drowning in pursuit",
            "According to the Quran, Musa received divine revelation on Mount Sinai, referred to as the tablets, containing guidance for his people",
            "The Quran describes an extended episode in which Musa travels with a figure often identified by later Islamic scholars as Al-Khidr, a story used to teach that some events carry a wisdom not immediately apparent to human understanding",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="prophet_harun", name="Harun (Aaron)", years="not historically dated", nationality="Egyptian/Israelite",
        field="prophet in Islamic tradition", wiki_title="Aaron",
        significance="according to the Quran, Harun was appointed by God as a prophet and helper to his brother Musa, supporting him in confronting Pharaoh and later guiding the Israelites in Musa's absence",
        facts=[
            "Harun is named in the Quran as the older brother of Musa and a prophet in his own right",
            "According to the Quran, Musa specifically prayed to God asking for Harun to be appointed as his helper and co-messenger, citing Harun's greater eloquence in speech",
            "The Quran recounts that Harun accompanied Musa in confronting Pharaoh and calling for the freedom of the Israelites",
            "According to the Quran, Harun was left in charge of the Israelites while Musa went to receive revelation on Mount Sinai, and struggled to prevent some of the people from worshipping a golden calf during that absence",
            "The Quran describes Harun expressing to Musa upon his return that he had tried to stop the people from idol worship but feared causing division among them",
            "Islamic tradition regards Harun as a model of loyal, supportive partnership in prophetic mission alongside his brother",
            "Harun is a shared figure across Judaism, Christianity, and Islam, corresponding to Aaron in the Hebrew Bible, described there as the first high priest of the Israelites",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_dhulkifl", name="Dhul-Kifl", years="not historically dated", nationality="uncertain",
        field="prophet in Islamic tradition", wiki_title="Dhul-Kifl",
        significance="Dhul-Kifl is named briefly in the Quran among the ranks of the patient and righteous, though the Quran itself gives few specific details of his story, and his exact historical identity remains debated among Islamic scholars",
        facts=[
            "Dhul-Kifl is mentioned by name twice in the Quran, in Surah Al-Anbiya and Surah Sad",
            "The Quran describes him among a group of individuals noted for patience and righteousness, alongside Ismail and Idris",
            "The Quran itself provides very little narrative detail about Dhul-Kifl's specific story, unlike the more extensive accounts given for prophets such as Musa or Yusuf",
            "Islamic scholars across history have debated his exact identity, with some historically identifying him with the biblical prophet Ezekiel, while others hold that he may not have been a prophet in the technical sense but a righteous, exemplary individual",
            "The name 'Dhul-Kifl' has been interpreted by some commentators as meaning 'possessor of a double portion' or 'one who guarantees', referencing later, non-Quranic traditions about his life",
            "Because of the limited textual detail, much of what is popularly said about Dhul-Kifl's specific deeds comes from later Islamic exegetical and historical literature (tafsir) rather than the Quran's own text",
            "His inclusion in the Quran's list of the patient and righteous is used in Islamic teaching primarily as an example of steadfastness, regardless of the specific historical details of his life",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_dawud", name="Dawud (David)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="David",
        significance="according to the Quran, Dawud was given both prophethood and kingship, was granted the Zabur (Psalms), and possessed a remarkably beautiful voice used to glorify God, as well as skill in ironworking",
        facts=[
            "Dawud is named in the Quran as a prophet who was also given kingship over the Israelites",
            "According to the Quran, Dawud defeated the giant warrior Jalut (Goliath) in his youth, an episode also described in the Hebrew Bible's Book of Samuel",
            "The Quran states that Dawud was given the Zabur, understood in Islamic tradition to correspond to the Psalms",
            "According to the Quran, mountains and birds would join Dawud in glorifying God, and iron was made supple in his hands, allowing him to craft protective coats of mail",
            "The Quran describes Dawud possessing an especially beautiful voice, and Islamic tradition holds that his recitation could move even the natural world around him",
            "According to the Quran, Dawud was given wisdom and the ability to judge fairly between people in disputes",
            "Dawud is the father of Sulayman, and together their stories in the Quran often emphasize wisdom, justice, and gratitude for divinely granted ability",
        ], related_subjects=["World Religions", "Islamic Studies", "Music"],
    ),
    dict(
        id="prophet_sulayman", name="Sulayman (Solomon)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="Solomon in Islam",
        significance="according to the Quran, Sulayman was given extraordinary wisdom and dominion, including the ability to understand the speech of animals and command the wind and jinn, and famously corresponded with the Queen of Sheba",
        facts=[
            "Sulayman is named in the Quran as a prophet and king, son of Dawud, given an especially vast kingdom",
            "According to the Quran, Sulayman was given the ability to understand the speech of birds and other animals, illustrated in a well-known passage involving an ant warning fellow ants of Sulayman's approaching army",
            "The Quran describes Sulayman commanding the wind and being served by jinn who performed construction and other tasks for him",
            "According to the Quran, a hoopoe bird brought Sulayman news of the Queen of Sheba (Bilqis) and her kingdom, leading to correspondence and her eventual visit to his court",
            "The Quran recounts that the Queen of Sheba was amazed by a grand palace hall with a floor made to look like water, and she ultimately submitted to belief in one God",
            "According to the Quran, Sulayman prayed for a kingdom unlike any other, and Islamic tradition holds his reign as an example of divinely granted wisdom, wealth, and power used righteously",
            "Sulayman is a shared figure across Judaism, Christianity, and Islam, corresponding to Solomon in the Hebrew Bible, renowned there for his wisdom and for building the Temple in Jerusalem",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_ilyas", name="Ilyas (Elijah)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="Elijah",
        significance="according to the Quran, Ilyas was sent to call his people away from the worship of the idol Ba'l and toward the worship of God alone",
        facts=[
            "Ilyas is named in the Quran, with his story briefly recounted in Surah As-Saffat",
            "According to the Quran, Ilyas was sent to warn his people against worshipping an idol called Ba'l, urging them instead to worship the one true God",
            "The Quran states that Ilyas's people rejected his message, except for a group of sincere believers among them",
            "Islamic tradition, drawing on the Quran's brief mention, regards Ilyas as a model of unwavering commitment to monotheism in the face of a community devoted to idol worship",
            "The Quran includes Ilyas among a list of righteous prophets alongside figures such as Ibrahim, Musa, and Harun",
            "Ilyas is a shared figure across Judaism, Christianity, and Islam, corresponding to the prophet Elijah in the Hebrew Bible, known there for his dramatic confrontation with the priests of Baal on Mount Carmel",
            "In some regional Islamic folk traditions, Ilyas has also become associated with legends of eternal life or periodic reappearance, though these popular traditions extend well beyond the Quran's own brief textual account",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_alyasa", name="Alyasa (Elisha)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="Elisha",
        significance="Alyasa is named briefly in the Quran among the ranks of the righteous and favored prophets, continuing the prophetic mission after Ilyas",
        facts=[
            "Alyasa is mentioned by name twice in the Quran, in Surah Al-An'am and Surah Sad",
            "The Quran lists him among a group of prophets described as righteous and favored above the worlds",
            "The Quran itself gives very little specific narrative detail about Alyasa's individual story, similar to the brief treatment given to Dhul-Kifl",
            "Islamic tradition, drawing on later exegetical literature rather than the Quran's direct text, generally holds that Alyasa continued the prophetic mission in the region after Ilyas",
            "Alyasa is widely identified by Islamic scholars with the biblical prophet Elisha, who in the Hebrew Bible's Books of Kings succeeded Elijah and performed a series of miracles",
            "As with several of the briefly mentioned Quranic prophets, most popularly circulated details about Alyasa's specific deeds come from later Islamic historical and exegetical writing rather than the Quran itself",
            "His mention in the Quran's list of the righteous is used in Islamic teaching to affirm the continuity of prophetic guidance across many generations",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_yunus", name="Yunus (Jonah)", years="not historically dated", nationality="Assyrian (Nineveh)",
        field="prophet in Islamic tradition", wiki_title="Jonah",
        significance="according to the Quran, Yunus left his people in frustration before completing his prophetic mission, was swallowed by a great fish, and was saved after calling out to God in repentance from within its belly",
        facts=[
            "Yunus is named in the Quran, and Surah Yunus, the tenth chapter, is named after him, though the chapter itself mostly addresses broader themes rather than telling his story in detail",
            "According to the Quran, Yunus was sent to a community, traditionally identified with the city of Nineveh, but left in anger and frustration before his mission was complete, without divine permission",
            "The Quran recounts that Yunus boarded a ship, and after being cast into the sea, he was swallowed by a great fish",
            "According to the Quran, within the darkness of the fish's belly, Yunus called out, 'There is no god but You; exalted are You. Indeed, I have been of the wrongdoers,' a supplication widely memorized and recited in Islamic tradition",
            "The Quran states that God accepted his repentance and had the fish cast him onto the shore, after which a plant grew to give him shade while he recovered",
            "According to the Quran, Yunus's people, unusually among the rejecting communities described in the Quran, later repented sincerely on their own and were spared destruction",
            "Yunus is a shared figure across Judaism, Christianity, and Islam, corresponding to the prophet Jonah in the Hebrew Bible's Book of Jonah",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_zakariya", name="Zakariya (Zechariah)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="Zechariah (biblical figure)",
        significance="according to the Quran, Zakariya was an elderly priest who prayed earnestly for a son despite his advanced age and his wife's inability to conceive, and was granted his prayer with the birth of Yahya",
        facts=[
            "Zakariya is named in the Quran as a prophet and the guardian of Maryam (Mary), caring for her in the Temple",
            "According to the Quran, Zakariya was inspired to pray for a righteous heir upon witnessing that Maryam was miraculously provided with sustenance beyond the ordinary season",
            "The Quran recounts Zakariya's prayer, acknowledging his old age and his wife's barrenness, yet asking God for an heir who would carry on righteous devotion",
            "According to the Quran, angels brought Zakariya the news that his prayer had been answered with a son, Yahya, and that God gave him a sign: he would be unable to speak to people for three days despite being in good health",
            "The Quran describes Zakariya's astonishment and gratitude at this news, given the natural circumstances of his and his wife's age",
            "Islamic tradition presents Zakariya's story as an example of persistent, sincere prayer even when a request seems naturally impossible",
            "Zakariya is a shared figure across Judaism, Christianity, and Islam, corresponding to Zechariah, the father of John the Baptist, in the New Testament's Gospel of Luke",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_yahya", name="Yahya (John the Baptist)", years="not historically dated", nationality="Israelite",
        field="prophet in Islamic tradition", wiki_title="John the Baptist",
        significance="according to the Quran, Yahya was given wisdom while still a child, along with compassion, purity, and righteousness, and the Quran describes him as devoted, dutiful to his parents, and never arrogant or rebellious",
        facts=[
            "Yahya is named in the Quran as the son of Zakariya, born in answer to his father's prayer in old age",
            "The Quran states that God gave Yahya wisdom while he was still a child, and describes him as compassionate and pure",
            "According to the Quran, Yahya was dutiful to his parents and was never arrogant or disobedient",
            "The Quran pronounces peace upon Yahya on the day he was born, the day he died, and the day he will be raised alive, a formula also used for Isa in the same chapter",
            "Islamic tradition holds Yahya as a model of righteous character maintained from childhood, distinguishing him among the prophets for receiving wisdom at such a young age",
            "Yahya is a shared figure across Christianity and Islam, corresponding to John the Baptist in the New Testament Gospels, described there as a preacher who baptized in the Jordan River and foretold the coming of Jesus",
            "Islamic accounts, drawing on tradition beyond the Quran's own text, generally hold that Yahya lived an ascetic life devoted to worship and calling people to righteousness",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="prophet_isa_quran", name="Isa (Jesus)", years="not historically dated", nationality="Judean (Roman province)",
        field="prophet in Islamic tradition", wiki_title="Jesus in Islam",
        significance="according to the Quran, Isa was born miraculously to the virgin Maryam, spoke as an infant in her defense, performed miracles by God's permission, and is honored as one of the most significant prophets sent to the Children of Israel",
        facts=[
            "Isa is named in the Quran, and Surah Maryam and portions of Surah Al Imran recount his birth and early life in detail",
            "According to the Quran, Isa was born to Maryam (Mary) through a miraculous conception, without a father, as a sign from God, and the Quran affirms her virginity",
            "The Quran describes Isa speaking as a newborn infant in Maryam's defense, testifying to his own prophethood, when her community accused her of wrongdoing",
            "According to the Quran, Isa was given the ability, by God's permission, to heal the blind and the leper and to bring clay birds to life, miracles presented in the text as signs granted to him rather than powers of his own",
            "The Quran states that Isa was given the Injil (Gospel), and affirms him as the Messiah (al-Masih) sent to the Children of Israel",
            "According to the Quran, Isa was not crucified but was raised up to God, a matter of central theological difference between Islamic and mainstream Christian understanding of the crucifixion",
            "Islam does not regard Isa as divine or as the son of God, understanding him instead as one of the greatest prophets and messengers sent by God, a significant point of theological distinction from Christian doctrine even as many narrative details are shared",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="prophet_muhammad_quran", name="Muhammad", years="c. 570-632 CE", nationality="Arabian",
        field="the final prophet in Islamic tradition", wiki_title="Muhammad",
        significance="Muslims believe Muhammad was the final prophet sent by God, and the Quran, believed by Muslims to have been revealed to him over 23 years, remains the central text of Islam",
        facts=[
            "Muhammad was born in Mecca, in the Arabian Peninsula, around 570 CE, and was orphaned at a young age",
            "According to Islamic tradition, he received his first revelation around 610 CE, at approximately age 40, while meditating in a cave called Hira near Mecca",
            "Muslims believe the revelations he received over the following 23 years were preserved and later compiled into the Quran, regarded by Muslims as the literal word of God",
            "In 622 CE he and his followers migrated from Mecca to Medina, an event called the Hijra, which marks the start of the Islamic calendar",
            "He is described in Islamic tradition as having united the tribes of Arabia under Islam by the time of his death, largely through a combination of negotiation, treaty, and, in some conflicts, warfare",
            "His sayings and actions, recorded by his companions and later compiled as Hadith, form a major source of Islamic guidance alongside the Quran",
            "The Quran refers to him as the 'Seal of the Prophets' (khatam an-nabiyyin), understood in Islamic theology to mean that he is the final prophet in the line that includes all those named above",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="maryam_mary", name="Maryam (Mary)", years="not historically dated", nationality="Judean (Roman province)",
        field="honored woman in Islamic tradition, mother of Isa", wiki_title="Mary, mother of Jesus",
        significance="Maryam is the only woman named directly in the Quran, an entire chapter (Surah Maryam) is named after her, and the Quran describes her as chosen and purified above the women of all nations",
        facts=[
            "Maryam is the only woman mentioned by name in the Quran, and the nineteenth chapter, Surah Maryam, is named after her",
            "According to the Quran, Maryam was dedicated to the service of the Temple by her mother even before her birth, and was raised under the guardianship of the prophet Zakariya",
            "The Quran describes Maryam being miraculously provided with food in her private chamber, a sign of God's favor that reportedly inspired Zakariya's own prayer for a son",
            "According to the Quran, an angel appeared to Maryam to announce that she would bear a son, Isa, through a miraculous conception, without a father",
            "The Quran recounts that Maryam withdrew to give birth alone, experienced great hardship during labor, and was comforted and provided for by God during this difficult time",
            "According to the Quran, when Maryam returned to her people with the newborn Isa and faced accusations, the infant Isa spoke from the cradle to defend her honor",
            "The Quran states that God chose Maryam and purified her, and preferred her above the women of all nations, and she is honored across Islamic tradition as a model of piety and devotion",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="khadija_bint_khuwaylid", name="Khadija bint Khuwaylid", years="c. 555-620 CE", nationality="Arabian (Meccan)",
        field="wife of the Prophet Muhammad, first believer in Islam", wiki_title="Khadija bint Khuwaylid",
        significance="a successful independent merchant in Mecca, she was Muhammad's first wife and the first person to accept his message, providing him crucial emotional and financial support in Islam's earliest and most difficult years",
        facts=[
            "Khadija bint Khuwaylid was born in Mecca around 555 CE into a respected merchant family, and became a successful businesswoman in her own right, unusual for a woman in that society at the time",
            "She employed the young Muhammad to lead her trade caravan to Syria, and was reportedly impressed by his honesty and skill",
            "She proposed marriage to Muhammad, and the two married around 595 CE, when she was roughly 40 and he was around 25",
            "When Muhammad received his first revelation and was deeply shaken by the experience, Khadija comforted and reassured him, and is regarded in Islamic tradition as the first person to believe in his message",
            "She used her own wealth to support Muhammad and the earliest Muslim community, particularly during a period when Meccan clans imposed a harsh economic boycott on Muhammad's family",
            "Islamic tradition holds that Muhammad did not marry another wife during Khadija's lifetime, and he continued to speak of her with deep affection and honor for the rest of his life",
            "She died in 620 CE, in a year Islamic tradition calls 'the Year of Sorrow' due to her death occurring close to that of Muhammad's uncle and protector, Abu Talib",
        ], related_subjects=["World Religions", "Islamic Studies", "Business Studies"],
    ),
    dict(
        id="abu_bakr", name="Abu Bakr", years="c. 573-634 CE", nationality="Arabian (Meccan)",
        field="first Caliph of Islam", wiki_title="Abu Bakr",
        significance="a close companion of Muhammad and one of the earliest converts to Islam, he became the first Caliph after Muhammad's death and helped preserve the fledgling Muslim community during a period of significant political instability",
        facts=[
            "Abu Bakr was born in Mecca around 573 CE and was a respected merchant, known for his reputation for honesty",
            "He is widely regarded in Islamic tradition as the first adult male to accept Islam, becoming one of Muhammad's closest and most trusted companions",
            "He accompanied Muhammad during the migration (Hijra) from Mecca to Medina in 622 CE, including the well-known episode of the two hiding together in a cave to evade pursuers",
            "Following Muhammad's death in 632 CE, he was selected as the first Caliph, the political and religious leader of the Muslim community",
            "During his roughly two-year rule he faced the Ridda Wars, a series of conflicts against Arabian tribes who renounced allegiance to the new Muslim state after Muhammad's death, and successfully reunified the region",
            "He ordered the initial compilation of the Quran's revealed verses into a single collected text, following the deaths of a number of those who had memorized it during the Ridda Wars",
            "He died in 634 CE, and his daughter Aisha had earlier married Muhammad, making Abu Bakr also the Prophet's father-in-law",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="umar_ibn_al_khattab", name="Umar ibn al-Khattab", years="c. 584-644 CE", nationality="Arabian (Meccan)",
        field="second Caliph of Islam", wiki_title="Umar",
        significance="the second Caliph, his roughly decade-long rule saw the rapid expansion of the early Muslim state across the Middle East and North Africa, along with significant administrative and legal reforms",
        facts=[
            "Umar ibn al-Khattab was born in Mecca around 584 CE, and was initially a strong opponent of Muhammad's message before his own dramatic conversion to Islam",
            "He became one of Muhammad's most trusted advisors, known for his strong, decisive character",
            "He became the second Caliph in 634 CE, following Abu Bakr's death, and adopted the title 'Amir al-Mu'minin' (Commander of the Faithful)",
            "Under his roughly ten-year rule, the Muslim state rapidly expanded, bringing the Byzantine province of Syria, Egypt, and the Sasanian Persian Empire under Muslim control",
            "He established significant administrative institutions, including a system for public treasury (bayt al-mal), organized welfare provisions, and a formal calendar (the Islamic Hijri calendar), which he introduced counting from the year of Muhammad's migration to Medina",
            "He was known for personally overseeing the conduct of his governors and for a reputation of strict, personal justice regardless of rank",
            "He was assassinated in 644 CE by a Persian slave with a personal grievance, while leading morning prayer in Medina",
        ], related_subjects=["World Religions", "Islamic Studies", "World History", "Civics"],
    ),
    dict(
        id="uthman_ibn_affan", name="Uthman ibn Affan", years="c. 579-656 CE", nationality="Arabian (Meccan)",
        field="third Caliph of Islam", wiki_title="Uthman",
        significance="the third Caliph, he is especially remembered for commissioning the standardized written compilation of the Quran that remains the basis of the text used by Muslims worldwide today",
        facts=[
            "Uthman ibn Affan was born in Mecca around 579 CE into the wealthy Umayyad clan, and was an early convert to Islam and a successful merchant",
            "He married two of Muhammad's daughters consecutively, Ruqayyah and then, after her death, Umm Kulthum, earning him the honorific title 'Dhun-Nurayn' ('possessor of two lights')",
            "He became the third Caliph in 644 CE, following Umar's assassination, chosen by a council of senior companions",
            "His most significant lasting achievement was commissioning a single standardized written text of the Quran around 650 CE, sending copies to major cities of the growing Muslim empire to ensure a uniform text and reduce regional recitation differences",
            "This 'Uthmanic codex' forms the basis of the standard Quran text used by Muslims worldwide today",
            "His later rule faced growing political unrest over issues including the appointment of relatives to governorships, which some segments of the Muslim community viewed as favoritism",
            "He was killed in 656 CE by rebels who besieged his home in Medina, an event that marked the beginning of the first major civil conflict (fitna) within the early Muslim community",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="ali_ibn_abi_talib", name="Ali ibn Abi Talib", years="c. 600-661 CE", nationality="Arabian (Meccan)",
        field="fourth Caliph of Islam", wiki_title="Ali",
        significance="the cousin and son-in-law of Muhammad, he became the fourth Caliph and is a central figure of reverence in both Sunni and Shia Islam, with Shia Muslims regarding him as Muhammad's rightful immediate successor",
        facts=[
            "Ali ibn Abi Talib was born in Mecca around 600 CE, raised in Muhammad's household from a young age, and is widely regarded as among the earliest, if not the first, young person to accept Islam",
            "He married Muhammad's daughter Fatimah, and their descendants are honored across the Muslim world as the Prophet's family line (ahl al-bayt)",
            "He served as a trusted advisor and warrior for Muhammad throughout his prophetic mission, including notable roles in several early battles",
            "He became the fourth Caliph in 656 CE, following Uthman's assassination, during a period of significant political division within the Muslim community",
            "His caliphate was marked by civil conflict, including the Battle of the Camel against a coalition led by Muhammad's widow Aisha, and the Battle of Siffin against the governor of Syria, Muawiyah",
            "The political and theological disagreements of this period contributed to the historical divide between Sunni and Shia Islam, with Shia Muslims holding that Ali should have succeeded Muhammad directly as the first rightful Caliph",
            "He was assassinated in 661 CE in Kufa, in present-day Iraq, and his death is commemorated with particular significance in Shia Islamic tradition",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="bilal_ibn_rabah", name="Bilal ibn Rabah", years="c. 580-640 CE", nationality="Abyssinian-Arabian",
        field="companion of the Prophet Muhammad, first muezzin", wiki_title="Bilal ibn Rabah",
        significance="an enslaved man of Abyssinian descent who was among the earliest converts to Islam, he endured severe persecution for his faith before being freed, and became the first person appointed to call the Muslim call to prayer",
        facts=[
            "Bilal ibn Rabah was born in Mecca around 580 CE to an enslaved mother, and was himself enslaved by a prominent Meccan clan",
            "He was among the earliest converts to Islam, and his enslaver reportedly subjected him to severe torture, including being made to lie on hot sand under a heavy stone, in an attempt to force him to renounce his faith",
            "According to Islamic tradition, throughout this persecution Bilal repeated the word 'Ahad' ('One'), affirming his belief in the oneness of God despite the torment",
            "He was purchased and freed by Abu Bakr specifically because of his suffering for his faith, becoming one of the most well-known formerly enslaved companions of Muhammad",
            "Following the establishment of the Muslim community in Medina, Muhammad appointed Bilal as the first muezzin, the person who calls the adhan (call to prayer), a role chosen partly for his powerful voice",
            "He accompanied Muhammad on military campaigns and was present at the conquest of Mecca in 630 CE, reportedly giving the call to prayer from atop the Kaaba itself",
            "He is remembered across the Muslim world as a powerful symbol of the Islamic principle of racial and social equality among believers regardless of their origin or former social status",
        ], related_subjects=["World Religions", "Islamic Studies", "Civics"],
    ),
    dict(
        id="aisha_bint_abi_bakr", name="Aisha bint Abi Bakr", years="c. 613/614-678 CE", nationality="Arabian (Meccan)",
        field="wife of the Prophet Muhammad, scholar of Hadith", wiki_title="Aisha",
        significance="a wife of Muhammad and the daughter of Abu Bakr, she became one of the most significant transmitters of Hadith and a respected scholar of Islamic law and Quranic interpretation in the generation after the Prophet's death",
        facts=[
            "Aisha bint Abi Bakr was born in Mecca around 613 or 614 CE, the daughter of Abu Bakr, Muhammad's closest companion and later the first Caliph",
            "She married Muhammad in Medina, and Islamic tradition describes her as his favorite among his later wives",
            "After Muhammad's death, she became one of the most important transmitters of Hadith (sayings and actions of the Prophet), and thousands of Hadith are traced back to her testimony",
            "She was recognized in her own time and by later generations as a scholar of Quranic interpretation, Islamic law, medicine, and Arabic poetry, and other companions frequently consulted her on religious matters",
            "She played a significant political role during the early caliphate period, notably leading forces at the Battle of the Camel in 656 CE against Ali's caliphate, a conflict during the first major civil war within the Muslim community",
            "She spent much of her later life teaching in Medina, and many prominent early Islamic scholars, including some of the earliest jurists, studied under her",
            "She died in 678 CE, and remains one of the most frequently cited sources for understanding the details of Muhammad's daily life and teachings",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="fatimah_bint_muhammad", name="Fatimah bint Muhammad", years="c. 605/615-632 CE", nationality="Arabian (Meccan)",
        field="daughter of the Prophet Muhammad", wiki_title="Fatimah",
        significance="the youngest daughter of Muhammad and wife of Ali ibn Abi Talib, she is honored across the Muslim world, and especially in Shia Islam, as a model of piety, and her descendants through her sons Hasan and Husayn are revered as the Prophet's family line",
        facts=[
            "Fatimah bint Muhammad was born in Mecca, with her exact birth year debated by historians, generally placed sometime between 605 and 615 CE",
            "She was the youngest daughter of Muhammad and his first wife Khadija, and remained especially close to her father throughout his life",
            "She married Ali ibn Abi Talib, Muhammad's cousin, in Medina, and their household is remembered in Islamic tradition for its notable simplicity despite Ali's prominence",
            "She had several children, including sons Hasan and Husayn, whose descendants are honored across the Muslim world, and especially in Shia Islam, as the Prophet's family line (ahl al-bayt)",
            "Islamic tradition holds that Muhammad spoke of her with particular tenderness, reportedly describing her as 'a part of me'",
            "She died within several months of her father's death in 632 CE, and the circumstances of her final months, including a disputed inheritance matter, are treated with particular significance in Shia historical and theological tradition",
            "She is honored with the title 'al-Zahra' ('the radiant one') and remains one of the most revered women in Islamic history",
        ], related_subjects=["World Religions", "Islamic Studies"],
    ),
    dict(
        id="khalid_ibn_al_walid", name="Khalid ibn al-Walid", years="c. 585-642 CE", nationality="Arabian (Meccan)",
        field="military commander, companion of the Prophet Muhammad", wiki_title="Khalid ibn al-Walid",
        significance="a formerly opposing Meccan military commander who converted to Islam and went on to lead Muslim forces to a series of major victories, he is remembered as one of the most successful generals in early Islamic history and earned the title 'Sword of Allah'",
        facts=[
            "Khalid ibn al-Walid was born in Mecca around 585 CE into a prominent clan, and gained early military experience fighting against Muslim forces before his conversion",
            "He commanded Meccan cavalry at the Battle of Uhud in 625 CE, where his tactics contributed to a setback for the early Muslim army",
            "He converted to Islam in 629 CE and quickly became one of Muhammad's most trusted military commanders",
            "Muhammad is reported to have given him the title 'Sayf Allah' ('Sword of God') following a difficult but skillfully managed retreat at the Battle of Mu'tah in 629 CE",
            "He led Muslim forces during the Ridda Wars following Muhammad's death, helping to reunify Arabia under the new Caliphate of Abu Bakr",
            "He led early Muslim campaigns into Persian Mesopotamia and Byzantine Syria during the 630s, including the decisive Battle of Yarmouk in 636 CE against Byzantine forces",
            "Despite his military success, he was later removed from top command by Caliph Umar, reportedly to ensure that victories were attributed to God's cause rather than to any one general's individual reputation, and he died in 642 CE",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
    dict(
        id="imam_abu_hanifa", name="Abu Hanifa", years="c. 699-767 CE", nationality="Persian (Kufa, Iraq)",
        field="Islamic jurist, founder of the Hanafi school of law", wiki_title="Abu Hanifa",
        significance="a foundational Islamic legal scholar, his approach to Islamic jurisprudence became the basis of the Hanafi school, today the most widely followed of the four major Sunni schools of Islamic law",
        facts=[
            "Abu Hanifa was born in Kufa, in present-day Iraq, around 699 CE, into a family of Persian merchant background",
            "He initially worked in the silk trade before dedicating himself to the study of Islamic law and theology under prominent scholars of his time",
            "He developed a methodology of Islamic jurisprudence that placed significant emphasis on reasoned analogy (qiyas) and juristic discretion (istihsan) alongside the Quran and Hadith",
            "His students, particularly Abu Yusuf and Muhammad al-Shaybani, compiled and systematized his legal teachings, since he himself left relatively few direct written works",
            "The school of Islamic legal thought that developed from his teachings, known as the Hanafi school, became especially influential across the historical Ottoman, Mughal, and Central Asian Islamic states",
            "He reportedly declined offers of formal judicial and government positions on more than one occasion, a decision Islamic biographical tradition attributes to his desire to maintain independent scholarly judgment",
            "He died in Baghdad around 767 CE, and the Hanafi school he founded remains, as of today, the school of Islamic law followed by the largest number of Sunni Muslims worldwide",
        ], related_subjects=["World Religions", "Islamic Studies", "Civics"],
    ),
    dict(
        id="imam_malik_ibn_anas", name="Malik ibn Anas", years="c. 711-795 CE", nationality="Arabian (Medina)",
        field="Islamic jurist, founder of the Maliki school of law", wiki_title="Malik ibn Anas",
        significance="based for his entire life in Medina, the city where Muhammad had lived and taught, his legal compilation the Muwatta and his teaching became the foundation of the Maliki school of Islamic law",
        facts=[
            "Malik ibn Anas was born in or near Medina around 711 CE, and spent nearly his entire life in that city, which he considered to hold special authority in matters of Islamic legal tradition",
            "He compiled the Muwatta, one of the earliest written collections of Hadith and Islamic legal rulings, drawing heavily on the practices observed among the people of Medina during his lifetime",
            "His legal methodology placed particular weight on the customary practice ('amal) of the people of Medina, reasoning that this practice preserved an especially direct continuity with the time of Muhammad and his companions",
            "He taught for decades in Medina, and his students, who came from across the Muslim world to study under him, later spread his teachings widely, especially across North and West Africa and parts of the Arabian Peninsula",
            "He reportedly endured hardship, including being physically punished by local authorities, for legal opinions that put him at odds with the ruling Abbasid governor of Medina, though accounts of the exact circumstances vary among historians",
            "The Maliki school of Islamic law that developed from his teaching remains, today, the predominant school followed across much of North and West Africa",
            "He died in Medina around 795 CE, having taught and influenced generations of Islamic scholars from that single city",
        ], related_subjects=["World Religions", "Islamic Studies", "Civics"],
    ),
    dict(
        id="imam_al_shafii", name="Al-Shafi'i", years="c. 767-820 CE", nationality="Arabian/Palestinian",
        field="Islamic jurist, founder of the Shafi'i school of law", wiki_title="Al-Shafi'i",
        significance="he developed a systematic methodology for Islamic legal reasoning in his work Al-Risala, considered the first formal treatise on the principles of Islamic jurisprudence, and his teaching became the basis of the Shafi'i school of law",
        facts=[
            "Al-Shafi'i was born around 767 CE, generally recorded as in Gaza, in present-day Palestine, and was raised largely in Mecca after being orphaned young",
            "He studied Islamic law under both Malik ibn Anas in Medina and later scholars connected to the Hanafi tradition in Iraq, giving him direct exposure to two major existing schools of legal thought",
            "His work Al-Risala is widely regarded as the first systematic treatise on usul al-fiqh, the foundational principles and methodology of Islamic jurisprudence",
            "He argued for a structured hierarchy of legal sources, prioritizing the Quran, then the Hadith of Muhammad, followed by scholarly consensus (ijma) and analogical reasoning (qiyas), a framework that significantly influenced how later Islamic legal scholars approached jurisprudence generally, not only within his own school",
            "He spent his later years teaching in Egypt, where he revised some of his earlier legal opinions based on further study, a body of work later distinguished by scholars as his 'new' school of thought",
            "The Shafi'i school of Islamic law that developed from his teaching remains widely followed today, particularly in Egypt, East Africa, and Southeast Asia, including Indonesia and Malaysia",
            "He died in Cairo, Egypt, around 820 CE",
        ], related_subjects=["World Religions", "Islamic Studies", "Civics"],
    ),
    dict(
        id="imam_ahmad_ibn_hanbal", name="Ahmad ibn Hanbal", years="c. 780-855 CE", nationality="Arabian (Baghdad)",
        field="Islamic jurist and Hadith scholar, founder of the Hanbali school of law", wiki_title="Ahmad ibn Hanbal",
        significance="renowned for his vast knowledge of Hadith and his refusal to renounce his theological views under government pressure and imprisonment, his teachings formed the basis of the Hanbali school, the most textually literalist of the four major Sunni schools",
        facts=[
            "Ahmad ibn Hanbal was born in Baghdad around 780 CE, and dedicated much of his early life to traveling widely across the Islamic world collecting and verifying Hadith",
            "He compiled the Musnad, a massive collection reported to contain tens of thousands of Hadith organized by the companion who transmitted each report, one of the largest such collections in Islamic scholarship",
            "His legal approach placed particularly strong emphasis on adhering closely to the literal text of the Quran and authenticated Hadith, with comparatively limited reliance on independent reasoning compared to some other schools",
            "During the Mihna, a period of religious inquisition under the Abbasid Caliph al-Ma'mun and his immediate successors, he was imprisoned and reportedly physically punished for refusing to publicly affirm a theological position on the nature of the Quran that he believed was incorrect",
            "His steadfast refusal to renounce his position despite this pressure earned him enormous respect and religious authority among later generations of Sunni Muslims",
            "The Hanbali school of Islamic law that developed from his teaching became, particularly from the 18th century onward, especially influential in the Arabian Peninsula, including through its connection to later religious reform movements there",
            "He died in Baghdad around 855 CE, and an enormous public funeral procession was reported to have taken place in his honor",
        ], related_subjects=["World Religions", "Islamic Studies", "Civics"],
    ),
    dict(
        id="zayd_ibn_harithah", name="Zayd ibn Harithah", years="c. 581-629 CE", nationality="Arabian",
        field="companion of the Prophet Muhammad", wiki_title="Zayd ibn Harithah",
        significance="a formerly enslaved man adopted by Muhammad as a son, Zayd is notably the only companion of the Prophet mentioned by name directly in the Quran",
        facts=[
            "Zayd ibn Harithah was born around 581 CE, and as a child was captured and sold into slavery before eventually being given as a gift to Khadija, who later gave him to Muhammad",
            "Muhammad freed Zayd and formally adopted him as a son, and Zayd was known for years afterward as 'Zayd ibn Muhammad' before later Quranic revelation clarified rules distinguishing adoption from biological parentage",
            "Zayd is the only companion of Muhammad mentioned by name directly in the Quran, in a passage in Surah Al-Ahzab discussing his marriage and subsequent divorce",
            "He was among the earliest converts to Islam, and Islamic tradition holds him in high regard for his close, trusted relationship with Muhammad over many years",
            "Muhammad appointed him to command several early Muslim military expeditions, reflecting the trust placed in him despite his background as a formerly enslaved man, notable in the social context of the time",
            "He was killed in 629 CE at the Battle of Mu'tah against Byzantine forces, one of the first major Muslim military engagements against the Byzantine Empire",
            "His son, Usama ibn Zayd, was later appointed by Muhammad to lead a military expedition at a young age, a decision that also drew on the family's standing within the early Muslim community",
        ], related_subjects=["World Religions", "Islamic Studies", "World History"],
    ),
]


def main() -> None:
    upsert_section(
        "quran_prophets_religious_figures",
        "Prophets & Religious Figures in the Quran",
        "☪️",
        "The 25 prophets named in the Quran, alongside Mary and other foundational figures of early Islam -- presented with care, framed around how each is described in the Quran and Islamic tradition.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
