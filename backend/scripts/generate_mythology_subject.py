#!/usr/bin/env python3
"""Add "Mythology" as a subject to the syllabus files for levels C1
through M1 (M2 intentionally excluded, per this request's "from C1 to
M1"), covering 16 mythological traditions: Hindu, Greek, Egyptian, Norse,
Celtic, Mayan, Aztec, Inca, Roman, Mesopotamian, Chinese, Japanese,
Korean, Pacific (Oceanic), African, and a synthesis "Other World
Mythologies" module (Slavic, Native American, and Australian Aboriginal
traditions).

Each level gets one lesson per tradition (16 lessons/level), reusing the
existing college-curriculum lesson scaffold (books/quiz_bank/exam/
external_courses) via _mythology_engine.py, with reading_material built
from real facts and increasing in depth from an introductory overview at
C1 to a comparative, source-critical treatment at M1 -- see
_mythology_engine.py and _biography_engine.py for the shared
no-fabrication template approach used throughout this session's content
work.

Re-run after editing:
    python3 backend/scripts/generate_mythology_subject.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _mythology_engine import MYTHOLOGY_LEVEL_IDS, build_mythology_subject  # noqa: E402

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

TRADITIONS = [
    dict(
        key="hindu", name="Hindu Mythology", region="the Indian subcontinent",
        deities=[
            "Brahma, the creator god, one of the Trimurti (trinity) alongside Vishnu and Shiva",
            "Vishnu, the preserver god, believed to descend to Earth in avatars including Rama and Krishna to restore cosmic order (dharma)",
            "Shiva, the destroyer and transformer god, often depicted meditating on Mount Kailash or dancing as Nataraja",
            "Devi (the Goddess), worshipped in forms including Durga, Kali, Lakshmi (goddess of wealth), and Saraswati (goddess of knowledge)",
            "Ganesha, the elephant-headed son of Shiva and Parvati, worshipped as the remover of obstacles",
        ],
        creation="the universe undergoes endless cycles of creation, preservation, and destruction (Brahma creating, Vishnu preserving, Shiva destroying), and different texts describe creation emerging from a cosmic ocean or from the sound 'Om'",
        heroes=[
            "The Ramayana, an epic attributed to the sage Valmiki, follows Prince Rama's quest to rescue his wife Sita from the demon king Ravana",
            "The Mahabharata, one of the longest epic poems in world literature, recounts the Kurukshetra War between the Pandava and Kaurava families and includes the Bhagavad Gita, a philosophical dialogue between the prince Arjuna and the god Krishna",
            "Krishna, an avatar of Vishnu, appears throughout Hindu mythology as both a mischievous youth and a wise divine teacher",
            "Hanuman, the monkey-god devoted to Rama, is celebrated for his strength, loyalty, and role in the Ramayana",
        ],
        practices=[
            "The Vedas, composed over roughly a thousand years beginning around 1500 BCE, are the oldest surviving Hindu scriptures, including hymns, rituals, and philosophy",
            "The Puranas are a large body of later texts recounting the genealogies, deeds, and legends of the gods",
            "Temple worship (puja), pilgrimage to sacred sites such as Varanasi, and major festivals including Diwali (festival of lights) and Holi (festival of colors) remain central living practices",
        ],
        legacy=[
            "Hindu mythology has directly shaped the art, temple architecture, classical dance, and literature of South and Southeast Asia for over two thousand years",
            "Major Hindu temple complexes, including Angkor Wat in Cambodia, were built to honor Vishnu and later repurposed for Buddhist worship, showing the tradition's reach across Southeast Asia",
            "Hindu mythological figures and stories remain central to contemporary Indian cinema, television, and popular festivals",
        ],
    ),
    dict(
        key="greek", name="Greek Mythology", region="Ancient Greece",
        deities=[
            "Zeus, king of the gods and ruler of the sky, who overthrew his father Cronus",
            "Poseidon, god of the sea, earthquakes, and horses",
            "Athena, goddess of wisdom and strategic warfare, said to have been born fully armed from the head of Zeus",
            "Hades, god of the underworld and the dead",
            "Apollo, god of the sun, music, prophecy, and healing",
        ],
        creation="the world began with Chaos, from which emerged Gaia (Earth), Tartarus, and Eros, and successive generations of gods, the Titans and then the Olympians, fought for control of the cosmos in a conflict called the Titanomachy",
        heroes=[
            "Heracles (Hercules), who performed twelve legendary labors to atone for a crime committed in a fit of madness",
            "Odysseus, whose ten-year journey home from the Trojan War is recounted in Homer's epic poem the Odyssey",
            "Achilles, the greatest warrior at Troy, whose wrath is the central subject of Homer's Iliad",
            "Theseus, who slew the Minotaur in the labyrinth of Crete",
        ],
        practices=[
            "The epic poems of Homer, the Iliad and the Odyssey, composed around the 8th century BCE, are primary sources for Greek myth",
            "Hesiod's Theogony, also from around the 8th century BCE, systematically describes the genealogy of the gods",
            "Major sanctuaries such as Delphi, home to the Oracle of Apollo, and Olympia, site of the ancient Olympic Games, were centers of religious practice",
        ],
        legacy=[
            "Greek myths were extensively retold and adapted by later Roman writers, who equated their own gods with Greek counterparts",
            "Greek mythological figures and stories remain a staple of Western literature, art, and film",
            "Many English words and scientific terms derive from Greek myth, including 'herculean,' 'achilles heel,' and 'panic' (from the god Pan)",
        ],
    ),
    dict(
        key="egyptian", name="Egyptian Mythology", region="Ancient Egypt",
        deities=[
            "Ra, the sun god, believed to sail across the sky by day and through the underworld by night",
            "Osiris, god of the afterlife, the underworld, and resurrection, murdered and later restored by his wife Isis",
            "Isis, goddess of magic and motherhood, widely worshipped and later honored across the Roman Empire",
            "Anubis, jackal-headed god associated with mummification and guiding the dead",
            "Horus, falcon-headed god of kingship and the sky, whose eye (the Eye of Horus) became a powerful protective symbol",
        ],
        creation="several competing creation accounts existed across different Egyptian cult centers, including one in which the god Atum emerged from the primordial waters of Nun and created the first gods by himself",
        heroes=[
            "The myth of Osiris's murder by his brother Set, his dismemberment, and his restoration by Isis is the central narrative of Egyptian mythology, explaining both kingship and the promise of an afterlife",
            "Horus, son of Osiris and Isis, avenged his father by contesting the throne with Set in a prolonged mythological struggle",
            "The Book of the Dead, a collection of spells and instructions, guided the deceased through the dangers of the underworld toward judgment",
        ],
        practices=[
            "Elaborate mummification practices and monumental tombs, including the pyramids at Giza, reflect the central Egyptian belief in a physical afterlife requiring a preserved body",
            "The 'weighing of the heart' ceremony, in which the heart of the deceased was weighed against the feather of the goddess Ma'at (truth and order), determined the soul's fate",
            "Temples such as those at Karnak and Luxor were maintained by dedicated priesthoods performing daily rituals to sustain cosmic order",
        ],
        legacy=[
            "Egyptian religious ideas, including the cult of Isis, spread across the Mediterranean and were adopted throughout the Roman Empire",
            "Egyptian mythology and iconography remain widely referenced in art, architecture (including Egyptian Revival style), and popular culture",
            "The decipherment of Egyptian hieroglyphs in the 19th century, following the discovery of the Rosetta Stone, opened direct access to Egyptian myth in its own original texts",
        ],
    ),
    dict(
        key="norse", name="Norse Mythology", region="Scandinavia and the medieval Norse world",
        deities=[
            "Odin, the chief god, associated with wisdom, war, and poetry, who sacrificed an eye for knowledge",
            "Thor, god of thunder, known for his hammer Mjolnir and his role as protector of both gods and humans",
            "Loki, a trickster figure whose schemes both help and endanger the other gods",
            "Freyja, goddess associated with love, fertility, war, and gold",
            "Frigg, Odin's wife, associated with foresight and motherhood",
        ],
        creation="the cosmos began in the void of Ginnungagap, between the fire of Muspelheim and the ice of Niflheim, and the gods formed the world from the body of the slain primordial giant Ymir",
        heroes=[
            "Sigurd (Siegfried in later German tradition), a legendary hero who slew the dragon Fafnir, a story preserved in the Volsunga Saga",
            "The Poetic Edda and Prose Edda, compiled in 13th-century Iceland, are the primary surviving sources for Norse mythology",
            "Ragnarok, the prophesied final battle in which many of the gods, including Odin and Thor, are fated to die as the world is destroyed and later reborn",
        ],
        practices=[
            "Norse religious practice included seasonal sacrifices (blot) and reverence for ancestral spirits, though written records come mostly from Christian-era Icelandic sources written after conversion",
            "The Prose Edda was compiled by the Icelandic scholar Snorri Sturluson around 1220 CE, partly to preserve mythological knowledge for poets",
            "Runestones and skaldic poetry preserve additional fragments of Norse mythological belief from the Viking Age (roughly 793-1066 CE)",
        ],
        legacy=[
            "Norse mythology directly shaped the days of the week in English: Tuesday (Tyr), Wednesday (Woden/Odin), Thursday (Thor), and Friday (Frigg)",
            "Norse myth strongly influenced later fantasy literature, including J.R.R. Tolkien's work, and remains a major presence in modern film, television, and games",
            "Viking Age archaeology, including ship burials and rune inscriptions, continues to provide physical evidence connected to Norse mythological practice",
        ],
    ),
    dict(
        key="celtic", name="Celtic Mythology", region="Ireland, Britain, and Gaul",
        deities=[
            "The Tuatha De Danann, a race of supernatural beings in Irish mythology led by figures such as the Dagda (a father-god associated with abundance) and Lugh (a many-skilled god of craft and light)",
            "Brigid, goddess associated with healing, poetry, and smithcraft, whose worship was later absorbed into the Christian figure of Saint Brigid",
            "Cernunnos, a horned god associated with animals, nature, and fertility, known primarily from Gaulish (continental Celtic) imagery such as the Gundestrup Cauldron",
            "The Morrigan, an Irish goddess associated with war, fate, and sovereignty, often appearing in the form of a crow",
        ],
        creation="Irish mythological tradition, preserved in the medieval text the Lebor Gabala Erenn ('Book of Invasions'), describes a series of successive mythical peoples settling Ireland, culminating in the arrival of the Tuatha De Danann and later the Milesians (ancestors of the Gaelic Irish)",
        heroes=[
            "Cu Chulainn, the central hero of the Ulster Cycle, renowned for his superhuman battle prowess, recounted especially in the epic Tain Bo Cuailnge ('Cattle Raid of Cooley')",
            "Fionn mac Cumhaill, legendary leader of the Fianna warrior band, whose adventures form the Fenian Cycle of Irish mythology",
            "King Arthur and his knights, though heavily reshaped by later medieval French and English romance, draw partly on earlier British Celtic legendary tradition",
        ],
        practices=[
            "Much of what survives of Celtic mythology comes from medieval Irish and Welsh manuscripts, written down by Christian monks centuries after the practices they describe, meaning the original oral pre-Christian tradition survives only indirectly",
            "The druids, a learned class in Celtic society, are described by Roman writers such as Julius Caesar as religious leaders, though few direct Celtic sources on druidic belief survive",
            "Seasonal festivals including Samhain (autumn, associated with the origins of Halloween), Imbolc, Beltane, and Lughnasadh marked the Celtic ritual calendar",
        ],
        legacy=[
            "Celtic mythology strongly shaped later Arthurian legend, one of the most retold story cycles in Western literature",
            "The modern holiday of Halloween traces significant roots to the Celtic festival of Samhain",
            "Celtic mythological art and symbolism, including interlace knotwork, remain widely recognized and reproduced today, particularly in Ireland, Scotland, and Wales",
        ],
    ),
    dict(
        key="mayan", name="Mayan Mythology", region="the Maya civilization of Mesoamerica (present-day Mexico, Guatemala, Belize, and Honduras)",
        deities=[
            "Itzamna, a creator god associated with wisdom, writing, and healing",
            "Kukulkan, the feathered serpent deity, associated with wind, rain, and the planet Venus (closely related to the Aztec Quetzalcoatl)",
            "Chaac, the rain god, considered vital to agricultural survival in the region",
            "The Hero Twins, Hunahpu and Xbalanque, central figures of Maya mythology who defeated the lords of the underworld",
        ],
        creation="according to the Popol Vuh, the sacred narrative of the K'iche' Maya, the gods attempted to create humanity in several failed forms (including beings of mud and of wood) before successfully creating people from maize (corn), reflecting maize's central role in Maya life",
        heroes=[
            "The Hero Twins Hunahpu and Xbalanque descended into Xibalba, the Maya underworld, and defeated its lords through cunning after their father and uncle had been killed there",
            "The Popol Vuh, preserved in a written form dating to the 16th century but drawing on much older oral tradition, is the single most important surviving source for Maya mythology",
            "Maya mythology is closely tied to astronomy, with gods and myths connected to the tracking of Venus and the complex Maya calendar system",
        ],
        practices=[
            "Maya city-states built monumental step-pyramid temples, such as those at Chichen Itza, Tikal, and Palenque, aligned with astronomical events",
            "Bloodletting and, in some contexts, human sacrifice were part of Maya religious ritual, intended to nourish and sustain the gods",
            "The Maya developed one of the most sophisticated writing systems and calendar systems in the pre-Columbian Americas, closely interwoven with religious and mythological record-keeping",
        ],
        legacy=[
            "The Popol Vuh remains a foundational text of Guatemalan and broader Mesoamerican cultural identity today",
            "Maya mythological imagery and calendar concepts (including popular but often distorted references to the '2012 phenomenon') remain widely referenced in modern popular culture",
            "Millions of Maya people across Mexico and Central America maintain living cultural and, in some communities, religious traditions connected to this mythology today",
        ],
    ),
    dict(
        key="aztec", name="Aztec Mythology", region="the Aztec (Mexica) civilization of central Mexico",
        deities=[
            "Huitzilopochtli, god of war and the sun, and the patron deity of the Aztec capital Tenochtitlan",
            "Quetzalcoatl, the feathered serpent god, associated with wind, learning, and the creation of humanity",
            "Tlaloc, the rain god, whose favor was considered essential for agricultural survival",
            "Coatlicue, an earth mother goddess, described in myth as the mother of Huitzilopochtli",
        ],
        creation="Aztec mythology describes the world as having gone through five successive Suns (cosmic eras), each ending in destruction, with the current, fifth Sun created through the self-sacrifice of the gods at the sacred city of Teotihuacan",
        heroes=[
            "The myth of Huitzilopochtli's miraculous birth, fully armed, to defend his mother Coatlicue against his sister Coyolxauhqui and four hundred siblings, is central to Aztec religious identity",
            "The Aztecs' foundational migration myth describes them being guided by Huitzilopochtli to found their capital, Tenochtitlan, at the site of an eagle perched on a cactus eating a serpent -- an image now on the Mexican flag",
            "Quetzalcoatl was said to have created the current human race by retrieving the bones of previous humanity from the underworld and mixing them with his own blood",
        ],
        practices=[
            "The Aztecs practiced elaborate religious rituals, including ceremonial ball games and, notably, human sacrifice, which they believed was necessary to sustain the sun and cosmic order",
            "The Templo Mayor, the great dual temple to Huitzilopochtli and Tlaloc at the heart of Tenochtitlan, was the central site of Aztec state religious practice",
            "The Aztec ritual calendar (tonalpohualli), a 260-day cycle, governed religious observance and was interwoven with mythology",
        ],
        legacy=[
            "The eagle-on-a-cactus foundational image from Aztec mythology remains the central emblem of the modern Mexican flag",
            "Aztec mythological figures and stories remain a significant part of Mexican national cultural identity today",
            "Spanish colonial accounts, combined with surviving indigenous codices, are the main sources scholars use to reconstruct Aztec mythology, since many original texts were destroyed during the Spanish conquest of the 1500s",
        ],
    ),
    dict(
        key="inca", name="Inca Mythology", region="the Inca Empire of the Andes (present-day Peru, Bolivia, Ecuador, and Chile)",
        deities=[
            "Inti, the sun god, regarded as the divine ancestor of the Inca ruling dynasty",
            "Viracocha, a creator god credited with shaping the earth, sky, and the first humans",
            "Pachamama, the earth mother goddess, associated with fertility and still widely honored in Andean communities today",
            "Mama Killa, the moon goddess, associated with the calendar and considered the wife of Inti",
        ],
        creation="according to Inca myth, the creator god Viracocha emerged from Lake Titicaca and shaped the earth, sky, and the first generation of giants, later destroying them and creating humanity anew, sending the first Inca ruler and his sister-wife up from the depths of the lake or a nearby cave to found the Inca dynasty",
        heroes=[
            "Manco Capac, the legendary first Inca ruler, said to have emerged with his sister Mama Ocllo from Lake Titicaca (or, in an alternate version, from a cave at Pacaritambo) to found the city of Cusco",
            "The founding myth of Manco Capac testing the fertility of the soil with a golden staff at various locations before settling at Cusco reflects the practical agricultural concerns embedded in Inca origin mythology",
            "Inca mythology closely intertwined the ruling Sapa Inca's authority with descent from Inti, the sun god, reinforcing royal legitimacy",
        ],
        practices=[
            "The Inca performed the Inti Raymi, a major festival honoring the sun god Inti at the June solstice, which continues to be celebrated (in revived form) in Cusco, Peru, today",
            "Inca religious practice included offerings and, in some documented cases, ritual sacrifice at high mountain sites, including the well-preserved child sacrifices found by archaeologists at high-altitude sites such as Mount Llullaillaco",
            "Because the Inca had no fully developed writing system in the conventional sense (relying instead on knotted-cord quipu records for accounting and possibly narrative), most surviving accounts of Inca mythology come from early Spanish colonial chroniclers recording oral tradition after the conquest",
        ],
        legacy=[
            "Pachamama (Mother Earth) remains an actively honored figure in Andean indigenous communities across Peru, Bolivia, and Ecuador today, with continuing ritual offerings",
            "The Inti Raymi festival has been revived as a major modern cultural celebration in Cusco, Peru",
            "Machu Picchu and other Inca archaeological sites, closely tied to Inca religious geography, remain among the most visited cultural heritage sites in South America",
        ],
    ),
    dict(
        key="roman", name="Roman Mythology", region="Ancient Rome",
        deities=[
            "Jupiter, king of the gods, associated with the sky and thunder, closely identified with the Greek Zeus",
            "Mars, god of war, considered a divine ancestor of the Roman people through his sons Romulus and Remus",
            "Venus, goddess of love and beauty, claimed as a divine ancestor by Julius Caesar's family through her son Aeneas",
            "Juno, queen of the gods, protector of the Roman state and women",
            "Janus, the two-faced god of beginnings, transitions, and doorways, uniquely Roman with no direct Greek equivalent",
        ],
        creation="Roman mythology absorbed much of Greek cosmology directly, while adding its own distinctly Roman foundation myths, most importantly the story of Aeneas, a Trojan survivor whose descendants were said to have eventually founded Rome",
        heroes=[
            "Romulus and Remus, twin sons of Mars raised by a she-wolf, with Romulus traditionally credited as the founder of Rome in 753 BCE after killing his brother in a dispute",
            "Aeneas, a Trojan hero who, according to Virgil's epic poem the Aeneid (written around 19 BCE), survived the fall of Troy and journeyed to Italy, becoming an ancestor of the Roman people",
            "The Aeneid was deliberately composed to give Rome a legendary heritage connecting it to the Greek Trojan War tradition and to legitimize the rule of the emperor Augustus",
        ],
        practices=[
            "Roman state religion was highly organized, with official priesthoods (including the pontifex maximus, a title later adopted by the Catholic papacy) overseeing public ritual on behalf of the state",
            "Roman religious practice emphasized correct ritual performance (orthopraxy) as much as belief, since maintaining the 'pax deorum' (peace of the gods) was considered essential to the state's welfare",
            "Household worship of ancestral spirits (the Lares and Penates) was practiced daily within Roman homes, alongside the grander public state religion",
        ],
        legacy=[
            "Roman mythology transmitted much of Greek myth to later Western Europe, since Latin remained the dominant literary and scholarly language for over a thousand years after Rome's fall",
            "The names of the planets in English (Mercury, Venus, Mars, Jupiter, Saturn, Neptune) derive directly from Roman deities",
            "Roman mythological and religious concepts, including the title 'pontifex maximus,' directly influenced the structure and vocabulary of later Western institutions, including the Catholic Church",
        ],
    ),
    dict(
        key="mesopotamian", name="Mesopotamian Mythology", region="ancient Sumer, Akkad, Babylon, and Assyria (present-day Iraq)",
        deities=[
            "Anu, the sky god and head of the Mesopotamian pantheon in its earliest form",
            "Enlil, god of wind, storms, and authority, who played a central role in many myths including the Mesopotamian flood story",
            "Inanna/Ishtar, goddess of love, fertility, and war, one of the most widely worshipped deities across Mesopotamian history",
            "Marduk, the patron god of Babylon, who rose to become head of the pantheon in Babylonian religious tradition after defeating the primordial sea-goddess Tiamat",
        ],
        creation="the Babylonian creation epic Enuma Elish, written down by around 1100 BCE but likely reflecting older tradition, describes the god Marduk defeating the chaotic sea goddess Tiamat and forming the heavens and earth from her body",
        heroes=[
            "The Epic of Gilgamesh, based on a historical king of Uruk and preserved on cuneiform tablets dating back over 4,000 years, is considered one of the oldest surviving works of literature in the world",
            "Gilgamesh's quest for immortality after the death of his companion Enkidu, and his encounter with the flood survivor Utnapishtim, form the emotional core of the epic",
            "The Mesopotamian flood narrative recounted to Gilgamesh closely parallels the later biblical and Quranic accounts of Noah and the flood, and is widely studied by scholars as an important point of comparison between ancient Near Eastern traditions",
        ],
        practices=[
            "Mesopotamian cities built massive stepped temple towers called ziggurats, dedicated to the patron deity of each city-state",
            "Religious texts, myths, and administrative records were preserved on clay tablets using cuneiform script, one of the earliest writing systems in human history, allowing modern scholars unusually direct access to ancient Mesopotamian belief",
            "Professional priesthoods performed daily rituals believed necessary to sustain the gods and, by extension, the order of the cosmos",
        ],
        legacy=[
            "The Epic of Gilgamesh, rediscovered by archaeologists in the 19th century, is now studied worldwide as one of the foundational texts of world literature",
            "Mesopotamian mythology and its flood narrative are widely used in comparative religion courses to illustrate parallels among ancient Near Eastern flood traditions",
            "Mesopotamian astronomy and mythology, including the seven-day week and zodiac concepts, indirectly shaped later Western and Middle Eastern calendrical and astrological traditions",
        ],
    ),
    dict(
        key="chinese", name="Chinese Mythology", region="ancient and imperial China",
        deities=[
            "The Jade Emperor, ruler of Heaven in later Chinese folk religion and Taoist tradition",
            "Nuwa, a creator goddess credited with molding humanity from clay and repairing a broken sky",
            "Fuxi, a legendary culture-hero credited with inventing writing, fishing, and the trigrams later used in the I Ching",
            "Guanyin, the bodhisattva of compassion, one of the most widely venerated figures in Chinese Buddhist and folk religious tradition",
        ],
        creation="Chinese cosmological myth describes Pangu, a primordial giant, separating the sky and earth from a formless cosmic egg over eighteen thousand years, with his body, upon death, becoming the mountains, rivers, and other features of the natural world",
        heroes=[
            "Yu the Great, a legendary ruler credited with controlling catastrophic floods through careful engineering, said to have founded the semi-legendary Xia dynasty",
            "Houyi, the archer who, according to myth, shot down nine of ten suns that were scorching the earth, saving humanity",
            "Sun Wukong, the Monkey King of the classic 16th-century novel Journey to the West, blends earlier mythological and folk-religious tradition into one of the most beloved characters in Chinese literature",
        ],
        practices=[
            "Chinese mythology developed through a blend of ancient folk belief, Taoism, Confucianism, and later Buddhism, rather than a single unified religious system",
            "Ancestor veneration, a long-standing and central practice in Chinese religious life, connects mythology directly to family and household ritual",
            "Major festivals including the Mid-Autumn Festival (linked to the moon goddess Chang'e) and the Dragon Boat Festival preserve and transmit mythological narrative through annual public celebration",
        ],
        legacy=[
            "Chinese mythological figures remain central to contemporary Chinese literature, film, television, and video games, both within China and internationally",
            "The zodiac animals of the Chinese calendar, tied to mythological origin stories, remain a widely recognized cultural export around the world",
            "Chinese mythology has directly shaped mythological and folk traditions across East and Southeast Asia through centuries of cultural exchange",
        ],
    ),
    dict(
        key="japanese", name="Japanese Mythology", region="Japan",
        deities=[
            "Amaterasu, the sun goddess, regarded in traditional Shinto belief as the divine ancestor of the Japanese imperial line",
            "Susanoo, the storm god, brother of Amaterasu, known for both destructive and heroic mythological episodes, including slaying a monstrous eight-headed serpent",
            "Tsukuyomi, the moon god, brother of Amaterasu",
            "Izanagi and Izanami, the primordial creator deities credited in myth with birthing the Japanese islands and many of the other gods (kami)",
        ],
        creation="according to the Kojiki (712 CE), Japan's oldest surviving chronicle, the deities Izanagi and Izanami stirred the primordial ocean with a jeweled spear, and the drops that fell formed the first island, from which they went on to create the rest of the Japanese archipelago and many of the kami (spirits/deities)",
        heroes=[
            "The myth of Amaterasu hiding in a cave after a dispute with Susanoo, plunging the world into darkness until the other gods lured her out with a mirror and celebration, is one of the most important episodes in Japanese mythology",
            "Susanoo's defeat of the eight-headed serpent Yamata no Orochi to save a maiden is a major heroic episode, and the sword he found in the serpent's tail became one of the three sacred imperial regalia of Japan",
            "The Kojiki and the Nihon Shoki (720 CE) are the two primary written sources for Japanese mythology, both compiled in the early 8th century",
        ],
        practices=[
            "Shinto, Japan's indigenous religious tradition, centers on veneration of kami (spirits or deities) associated with natural features, ancestors, and abstract forces, and remains an active living religion in Japan today",
            "Ise Grand Shrine, dedicated to Amaterasu, is rebuilt in an identical form every 20 years in a ritual called shikinen sengu, a tradition maintained for over a thousand years",
            "Shinto shrines, torii gates, and seasonal festivals (matsuri) remain widespread and actively practiced throughout Japan today",
        ],
        legacy=[
            "Japanese mythology remains historically connected to the modern Japanese imperial family, which traditional belief holds descends from Amaterasu",
            "Japanese mythological figures and yokai (supernatural creatures) remain a major influence on globally popular Japanese anime, manga, and video games",
            "The three imperial regalia of Japan -- the sword, mirror, and jewel from mythology -- remain part of the symbolic basis of the modern Japanese imperial enthronement ceremony",
        ],
    ),
    dict(
        key="korean", name="Korean Mythology", region="the Korean peninsula",
        deities=[
            "Hwanin, the ruler of Heaven in the founding myth of Korea",
            "Hwanung, son of Hwanin, who descended to Earth to found a human settlement",
            "Dangun, the legendary founder of the first Korean kingdom, Gojoseon, born of Hwanung and a bear-woman",
            "Sanshin, the mountain spirit, still widely honored in Korean folk religion and Buddhist temple shrines today",
        ],
        creation="according to the Dangun myth, recorded in the 13th-century chronicle Samguk Yusa, Hwanung descended from heaven to a sacred mountain, and a bear and a tiger both prayed to become human; the bear endured a difficult trial of eating only mugwort and garlic in a cave for 100 days and was transformed into a woman, who then bore Dangun, the founder of Gojoseon, traditionally dated to 2333 BCE",
        heroes=[
            "Dangun is regarded as the legendary founding ancestor of the Korean people, and his story remains foundational to Korean national identity",
            "Jumong, the legendary founder of the ancient kingdom of Goguryeo, is described in myth as the son of a river goddess and a sky-god figure, gifted with extraordinary archery skill from birth",
            "Korean shamanic mythology (muism) includes a rich tradition of origin myths for individual deities, transmitted historically through oral epic songs (called 'muga') performed by shamans (mudang)",
        ],
        practices=[
            "Korean shamanism (muism), with practicing shamans called mudang, continues as a living folk-religious tradition in parts of Korea today, alongside Buddhism and Christianity",
            "The Samguk Yusa ('Memorabilia of the Three Kingdoms'), compiled by the Buddhist monk Iryeon in the 13th century, is the primary written source preserving the Dangun founding myth and other early Korean mythological material",
            "Mountain spirit shrines (sanshin-gak) are commonly found on the grounds of Korean Buddhist temples, reflecting the blending of older Korean folk belief with later Buddhist practice",
        ],
        legacy=[
            "National Foundation Day (Gaecheonjeol) is an official public holiday in South Korea, commemorating the legendary founding of Gojoseon by Dangun",
            "Dangun remains a significant symbol of Korean national identity and is referenced in modern Korean culture, education, and political discourse",
            "Korean shamanic and mythological themes continue to appear in contemporary Korean film, television dramas, and literature",
        ],
    ),
    dict(
        key="pacific", name="Pacific (Oceanic) Mythology", region="Polynesia, Melanesia, and Micronesia",
        deities=[
            "Tangaroa (also known as Kanaloa or Ta'aroa in different Polynesian island traditions), a major god associated with the sea",
            "Maui, a trickster demigod culture-hero appearing across many Polynesian traditions, credited with feats including fishing up islands from the ocean floor and slowing the sun's passage across the sky",
            "Pele, the Hawaiian goddess of volcanoes and fire, still actively honored in Hawaiian cultural tradition today",
            "Tane (or Kane), a major god associated with forests and the origin of the first humans in various Polynesian traditions",
        ],
        creation="Polynesian creation traditions vary by island group, but many describe the sky-father and earth-mother (such as Rangi and Papa in Maori tradition) being forcibly separated by their children to allow light into the world, a myth central to Maori cosmology in New Zealand",
        heroes=[
            "The demigod Maui appears in myth across Hawaii, New Zealand (Aotearoa), Samoa, Tonga, and other Pacific island cultures, with regionally varying versions of his exploits",
            "Maui's most widespread myth describes him fishing up islands, including New Zealand's North Island, from the depths of the ocean using a magical hook",
            "Traditional Polynesian navigators used deep knowledge of stars, ocean swells, and wildlife, closely bound up with mythological and ancestral knowledge, to voyage across the vast distances of the Pacific Ocean centuries before European contact, settling islands as remote as Hawaii, New Zealand, and Rapa Nui (Easter Island)",
        ],
        practices=[
            "Oral tradition, chant, and genealogical recitation (whakapapa in Maori tradition) were the primary means of preserving Pacific mythology across generations before extensive written documentation began after European contact",
            "The Hawaiian Kumulipo, a lengthy genealogical creation chant, links the Hawaiian royal family's ancestry back through myth to the origin of the cosmos",
            "Traditional Pacific carving, tattoo art (such as Maori ta moko and Polynesian tatau), and meeting-house architecture are closely tied to mythological and ancestral symbolism",
        ],
        legacy=[
            "Hawaiian and Maori mythological traditions remain actively practiced and taught as part of living indigenous cultural revival movements today",
            "Pele remains an actively honored figure in Hawaiian culture, and some residents interpret ongoing volcanic activity through this traditional lens alongside modern volcanology",
            "Pacific mythological figures, particularly Maui, reached a large global audience through popular media in the 21st century, prompting renewed public interest alongside ongoing discussion within Pacific communities about accurate and respectful representation",
        ],
    ),
    dict(
        key="african", name="African Mythology", region="the diverse cultures of the African continent",
        deities=[
            "Olodumare (also called Olorun), the supreme creator god in Yoruba religious tradition of West Africa",
            "Anansi, the trickster spider figure of Akan (Ghanaian) mythology, renowned for cleverness and storytelling",
            "Amma, the creator god of Dogon mythology in Mali",
            "Mawu-Lisa, a dual moon-and-sun creator deity in Fon and Ewe mythology of West Africa (Benin, Togo)",
        ],
        creation="African mythological traditions vary enormously across the continent's thousands of distinct cultures; in Yoruba tradition, the god Obatala was sent by Olodumare to create solid land from the primordial waters and to shape the first human beings from clay, while other regional traditions describe entirely different creation narratives suited to their own peoples and landscapes",
        heroes=[
            "Anansi the spider is one of the most widely known trickster figures in world mythology, using wit rather than strength to outsmart more powerful beings, and his stories spread with the transatlantic slave trade to become foundational to Caribbean and African American folklore as well",
            "Sundiata Keita, founder of the Mali Empire in the 13th century, became a legendary hero-king whose life is recounted in the Epic of Sundiata, a foundational oral epic of West Africa still performed by griot storytellers today",
            "Shaka Zulu, the early 19th-century Zulu king, became a major figure of Southern African historical legend for his military reforms and the rise of the Zulu Kingdom",
        ],
        practices=[
            "Because most African mythological traditions were preserved primarily through oral transmission, professional oral historians and storytellers -- griots in West Africa in particular -- have historically played a central role in preserving and transmitting myth, genealogy, and history together",
            "Yoruba religious tradition, including belief in the orishas (deities/spirits), spread with the transatlantic slave trade and directly shaped syncretic religions in the Americas, including Santeria in Cuba and Candomble in Brazil",
            "Ancestor veneration and belief in a spirit world closely connected to the living are common, though far from universal, threads across many distinct African mythological and religious traditions",
        ],
        legacy=[
            "Anansi stories remain widely told across West Africa and the Caribbean today, and directly shaped later African American folklore traditions such as the Br'er Rabbit stories",
            "Yoruba-derived religious traditions remain actively practiced by millions of people across the Americas today, particularly in Cuba, Brazil, and parts of the United States",
            "African mythological and oral epic traditions, including the Epic of Sundiata, remain the subject of active scholarly study and continue to be performed by griots in West Africa today",
        ],
    ),
    dict(
        key="other_world", name="Other World Mythologies (Slavic, Native American, and Australian Aboriginal)", region="Eastern Europe, the Americas, and Australia",
        deities=[
            "Perun, the Slavic god of thunder and the sky, considered the chief deity in the pre-Christian religion of the Eastern Slavs",
            "Coyote, a widespread trickster and creator figure appearing across many distinct Native American mythological traditions, particularly in the western United States",
            "The Rainbow Serpent, a major creator being found across many Australian Aboriginal Dreamtime traditions, associated with water sources and the shaping of the landscape",
            "Baiame, a sky-father creator figure central to the Dreaming traditions of several Aboriginal peoples of southeastern Australia",
        ],
        creation="each of these traditions has its own distinct account: Slavic myth describes a cosmic struggle between Perun (order/sky) and Veles (chaos/underworld); many Native American traditions describe an 'Earth-Diver' creation, in which an animal dives to the bottom of a primordial ocean to retrieve mud that becomes land; and Australian Aboriginal Dreamtime accounts describe ancestral beings shaping the landscape's rivers, mountains, and rock formations during a foundational creative period",
        heroes=[
            "In Slavic mythology, Baba Yaga, an ambiguous witch-like figure living in a hut on chicken legs, appears throughout Russian and broader Slavic folklore, sometimes as a villain and sometimes as an unlikely helper",
            "Native American trickster-hero figures, including Coyote, Raven (in Pacific Northwest traditions), and Iktomi (in Lakota tradition), use cunning to shape the world and teach moral lessons, often through their own mistakes and misadventures",
            "Australian Aboriginal Dreamtime narratives describe ancestral beings whose journeys across the land during the creative period are believed to have physically shaped specific landmarks, with those same routes preserved today as 'songlines' passed down through generations",
        ],
        practices=[
            "Slavic mythology survives mostly through fragments recorded by early Christian chroniclers, later folklore collection, and comparative linguistic reconstruction, since the pre-Christian Slavic peoples left few if any surviving written religious texts of their own",
            "Native American mythologies are extraordinarily diverse, reflecting hundreds of distinct nations and language groups across North America, each with its own specific traditions, ceremonies, and sacred narratives",
            "Australian Aboriginal Dreamtime (or 'the Dreaming') is not simply a set of past myths but an ongoing spiritual framework connecting land, law, ceremony, and identity for Aboriginal peoples, maintained through art, ceremony, and songlines across tens of thousands of years of continuous culture",
        ],
        legacy=[
            "Baba Yaga and other Slavic mythological figures remain widely recognized across Eastern European literature, folklore, and popular culture today",
            "Contemporary Native American communities across the United States and Canada continue to maintain, teach, and practice their specific tribal traditions and ceremonies today",
            "Aboriginal Dreamtime art and storytelling remain a living, actively practiced tradition among Aboriginal Australian communities, and are increasingly presented in Australian museums and schools with the direct involvement of Aboriginal knowledge-holders",
        ],
    ),
]

assert len(TRADITIONS) == 16, f"expected 16 traditions, got {len(TRADITIONS)}"


def main() -> None:
    for level in MYTHOLOGY_LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        subject = build_mythology_subject(level, TRADITIONS)
        data["subjects"]["Mythology"] = subject

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        word_counts = [len(l["reading_material"].split()) for l in subject["lessons"]]
        print(
            f"[{level}] Mythology: {len(subject['lessons'])} lessons "
            f"(reading_material words: min={min(word_counts)}, max={max(word_counts)}, "
            f"avg={sum(word_counts)//len(word_counts)}); {len(data['subjects'])} total subjects"
        )


if __name__ == "__main__":
    main()
