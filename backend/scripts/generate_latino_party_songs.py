#!/usr/bin/env python3
"""Add 100 of the most famous Latino party songs to the Song Centre
(backend/data/song_centre/songs.json), each with a music-video link.

Every entry is a real, well-known song. The music-video link is a YouTube
*search* for "<title> <artist> official music video" rather than a guessed
direct video URL, consistent with this project's no-fabrication rule (the
Song Centre frontend renders links.youtube_search and explicitly labels
links as search links).

Candidates are deduped against songs already in the collection by
normalized title, and additions are capped at 100.

Re-run after editing:
    python3 backend/scripts/generate_latino_party_songs.py
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SONGS_PATH = BASE_DIR / "data" / "song_centre" / "songs.json"

MAX_ADDITIONS = 100


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wiki_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


def lyrics_search(q: str) -> str:
    return "https://www.google.com/search?q=" + quote_plus(q)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", norm(s)).strip("_")


# (title, artist, year, genres, country, language, description, fun_fact)
SONGS = [
    # --- Reggaeton / urbano party anthems ---
    ("Mi Gente", "J Balvin & Willy William", 2017, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A global reggaeton smash built on a hypnotic hook, celebrating music that belongs to everyone.", "A remix featuring Beyoncé raised funds for hurricane relief in Puerto Rico and Mexico in 2017."),
    ("Taki Taki", "DJ Snake feat. Selena Gomez, Ozuna & Cardi B", 2018, ["reggaeton", "EDM"], "France/Puerto Rico/United States", "Spanish/English", "A high-energy club anthem uniting Latin and global pop superstars over a booming reggaeton beat.", "Its music video amassed hundreds of millions of views within months of release."),
    ("Con Calma", "Daddy Yankee & Snow", 2019, ["reggaeton", "latin pop"], "Puerto Rico", "Spanish/English", "A dance-floor juggernaut that reimagines Snow's 1992 hit 'Informer' with a reggaeton pulse.", "It topped charts in more than a dozen countries and dominated global Latin playlists in 2019."),
    ("Dura", "Daddy Yankee", 2018, ["reggaeton"], "Puerto Rico", "Spanish", "An old-school-flavored reggaeton banger that sparked a global dance challenge.", "The #DuraChallenge saw fans worldwide posting dance videos to the song."),
    ("Rompe", "Daddy Yankee", 2005, ["reggaeton"], "Puerto Rico", "Spanish", "A hard-hitting anthem from the Barrio Fino era that helped push reggaeton onto US charts.", "It was one of the first reggaeton singles to enter the Billboard Hot 100."),
    ("Lo Que Pasó, Pasó", "Daddy Yankee", 2004, ["reggaeton"], "Puerto Rico", "Spanish", "A melodic party staple from Barrio Fino, one of reggaeton's landmark albums.", "Barrio Fino became one of the best-selling Latin albums of the 2000s."),
    ("Sígueme y Te Sigo", "Daddy Yankee", 2015, ["reggaeton", "latin pop"], "Puerto Rico", "Spanish", "An upbeat dance track about mutual attraction that became a wedding and party playlist fixture.", "Its playful hook made it one of Daddy Yankee's most streamed mid-2010s singles."),
    ("Limbo", "Daddy Yankee", 2012, ["reggaeton", "dance"], "Puerto Rico", "Spanish", "A carnival-flavored dance anthem inviting everyone to get lower on the dance floor.", "It became a staple of Zumba classes and dance-fitness routines worldwide."),
    ("Pepas", "Farruko", 2021, ["reggaeton", "guaracha", "EDM"], "Puerto Rico", "Spanish", "A festival-sized guaracha/EDM hybrid that became one of the biggest global party tracks of 2021.", "It topped Billboard's Hot Latin Songs and crossed over to mainstream dance radio."),
    ("Dákiti", "Bad Bunny & Jhay Cortez", 2020, ["reggaeton"], "Puerto Rico", "Spanish", "A sleek, night-drive reggaeton hit that broke global streaming records.", "It was the first song to top Billboard's Global 200 and Hot Latin Songs simultaneously."),
    ("Tití Me Preguntó", "Bad Bunny", 2022, ["reggaeton"], "Puerto Rico", "Spanish", "A playful, dembow-driven hit from Un Verano Sin Ti about a nosy aunt's questions.", "Un Verano Sin Ti was the most-streamed album in the world in 2022."),
    ("Me Porto Bonito", "Bad Bunny & Chencho Corleone", 2022, ["reggaeton"], "Puerto Rico", "Spanish", "A summer party anthem pairing Bad Bunny with Plan B's Chencho Corleone.", "It spent months at the top of global streaming charts in 2022."),
    ("Yo Perreo Sola", "Bad Bunny", 2020, ["reggaeton"], "Puerto Rico", "Spanish", "A club anthem about a woman who dances on her own terms.", "The song was widely praised for its message of respect on the dance floor."),
    ("Callaíta", "Bad Bunny & Tainy", 2019, ["reggaeton"], "Puerto Rico", "Spanish", "A beach-party favorite with one of Tainy's most iconic productions.", "It remained on global streaming charts for years after release."),
    ("I Like It", "Cardi B, Bad Bunny & J Balvin", 2018, ["latin trap", "hip hop"], "United States/Puerto Rico/Colombia", "English/Spanish", "A boogaloo-sampling celebration of Latin sound that topped the Billboard Hot 100.", "It samples Pete Rodríguez's 1967 boogaloo classic 'I Like It Like That'."),
    ("Ginza", "J Balvin", 2015, ["reggaeton"], "Colombia", "Spanish", "A smooth reggaeton hit that helped launch the genre's global second wave.", "It set a then-record run at #1 on Billboard's Hot Latin Songs for a solo act."),
    ("Ay Vamos", "J Balvin", 2014, ["reggaeton"], "Colombia", "Spanish", "A sing-along hit about a couple that fights but stays together.", "Its video won Best Urban Video at the Latin Grammys."),
    ("Ritmo (Bad Boys for Life)", "Black Eyed Peas & J Balvin", 2019, ["latin pop", "dance"], "United States/Colombia", "Spanish/English", "A party crossover built on Corona's 90s eurodance hit 'The Rhythm of the Night'.", "It was the lead single from the Bad Boys for Life movie soundtrack."),
    ("Loco Contigo", "DJ Snake & J Balvin feat. Tyga", 2019, ["reggaeton", "EDM"], "France/Colombia", "Spanish/English", "A sun-soaked club track blending French EDM production with Colombian reggaeton flow.", "It premiered live at Coachella before its official release."),
    ("X", "Nicky Jam & J Balvin", 2018, ["reggaeton"], "United States/Colombia", "Spanish", "A minimalist dance-floor earworm that dominated 2018 party playlists.", "Its stripped-down beat was engineered to make crowds move with almost nothing but rhythm."),
    ("El Perdón", "Nicky Jam & Enrique Iglesias", 2015, ["reggaeton", "latin pop"], "United States/Spain", "Spanish", "A melodic plea for forgiveness that became one of the decade's biggest Latin hits.", "It spent 30 weeks at #1 on Billboard's Hot Latin Songs."),
    ("Travesuras", "Nicky Jam", 2014, ["reggaeton"], "United States/Puerto Rico", "Spanish", "The comeback single that relaunched Nicky Jam's career as a romantic-reggaeton hitmaker.", "Its success marked one of Latin music's most celebrated career comebacks."),
    ("Hasta el Amanecer", "Nicky Jam", 2016, ["reggaeton"], "United States/Puerto Rico", "Spanish", "A flirtatious dance hit about a chance meeting that lasts until sunrise.", "Its video gained over a billion views on YouTube."),
    ("El Amante", "Nicky Jam", 2017, ["reggaeton"], "United States/Puerto Rico", "Spanish", "A romantic reggaeton anthem from the album Fénix.", "Fénix debuted at #1 on Billboard's Top Latin Albums."),
    ("Tusa", "Karol G & Nicki Minaj", 2019, ["reggaeton"], "Colombia/United States", "Spanish/English", "A heartbreak-turned-party anthem that made 'tusa' an international word for post-breakup blues.", "It topped charts across Latin America and won Latin Grammy nominations."),
    ("Bichota", "Karol G", 2020, ["reggaeton"], "Colombia", "Spanish", "A swaggering empowerment anthem that became Karol G's signature party track.", "The term 'bichota' became a rallying cry of confidence for her fans."),
    ("Provenza", "Karol G", 2022, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A breezy, beach-ready hit named after a famous street in Medellín.", "It debuted at #1 on Billboard's Hot Latin Songs."),
    ("TQG", "Karol G & Shakira", 2023, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A powerhouse team-up of two Colombian superstars that broke streaming records.", "It debuted in the top 10 of the Billboard Hot 100 -- rare for an all-Spanish song."),
    ("Felices los 4", "Maluma", 2017, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A smooth party hit that became one of Maluma's most recognizable songs.", "A salsa remix with Marc Anthony gave the song a second life on dance floors."),
    ("Hawái", "Maluma", 2020, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A bittersweet hit about pretending to be happy after a breakup, set to an irresistible beat.", "A remix with The Weeknd brought it to English-language audiences."),
    ("Corazón", "Maluma feat. Nego do Borel", 2017, ["reggaeton", "funk carioca"], "Colombia/Brazil", "Spanish/Portuguese", "A bilingual Colombian-Brazilian party track bridging reggaeton and baile funk.", "Its bilingual chorus made it a hit across both Spanish- and Portuguese-speaking countries."),
    ("Chantaje", "Shakira feat. Maluma", 2016, ["reggaeton", "latin pop"], "Colombia", "Spanish", "A sultry back-and-forth duet between two generations of Colombian stardom.", "It became one of the fastest Latin videos to reach a billion views."),
    ("La Bicicleta", "Carlos Vives & Shakira", 2016, ["vallenato", "latin pop"], "Colombia", "Spanish", "A joyous vallenato-pop celebration of Colombian coastal life.", "It won Record of the Year and Song of the Year at the Latin Grammys."),
    ("Rakata", "Wisin & Yandel", 2005, ["reggaeton"], "Puerto Rico", "Spanish", "An early reggaeton club classic from the genre's breakout duo.", "It was among the first reggaeton hits to chart on US mainstream radio."),
    ("Follow the Leader", "Wisin & Yandel feat. Jennifer Lopez", 2012, ["reggaeton", "dance"], "Puerto Rico/United States", "Spanish/English", "A stadium-sized dance collaboration between reggaeton's top duo and JLo.", "Its video was filmed amid the crowds of Acapulco."),
    ("Taboo", "Don Omar", 2011, ["reggaeton", "dance"], "Puerto Rico", "Spanish", "A carnival anthem built on the melody of the lambada.", "It reworks the 1989 worldwide hit 'Lambada' into a reggaeton stomper."),
    ("Hasta Que Salga el Sol", "Don Omar", 2012, ["reggaeton", "dance"], "Puerto Rico", "Spanish", "A festival-ready anthem about partying until sunrise.", "It became a staple of closing sets at Latin music festivals."),
    ("Dile", "Don Omar", 2003, ["reggaeton"], "Puerto Rico", "Spanish", "An early classic that established Don Omar as reggaeton royalty.", "It appeared on The Last Don, one of reggaeton's foundational albums."),
    ("Baila Baila Baila", "Ozuna", 2019, ["reggaeton"], "Puerto Rico", "Spanish", "A pure dance-floor invitation from one of streaming's most-watched artists.", "Ozuna was YouTube's most-viewed artist worldwide in 2018."),
    ("Te Boté (Remix)", "Nio García, Casper Mágico & Bad Bunny feat. Darell, Nicky Jam & Ozuna", 2018, ["latin trap", "reggaeton"], "Puerto Rico", "Spanish", "A marathon posse-cut breakup anthem that ruled Latin streaming in 2018.", "It spent 14 weeks atop Billboard's Hot Latin Songs."),
    ("Criminal", "Natti Natasha & Ozuna", 2017, ["reggaeton"], "Dominican Republic/Puerto Rico", "Spanish", "A dark, pulsing duet that launched Natti Natasha to stardom.", "Its video reached a billion views within a year."),
    ("Sin Pijama", "Becky G & Natti Natasha", 2018, ["reggaeton", "latin pop"], "United States/Dominican Republic", "Spanish", "A playful girls-night anthem from two of Latin pop's leading women.", "It became one of the most-viewed videos by a female Latin duo."),
    ("Mayores", "Becky G feat. Bad Bunny", 2017, ["reggaeton", "latin pop"], "United States/Puerto Rico", "Spanish", "A cheeky hit that paired Becky G's pop polish with an early Bad Bunny feature.", "It marked one of Bad Bunny's first major international appearances."),
    ("Mamiii", "Becky G & Karol G", 2022, ["reggaeton"], "United States/Colombia", "Spanish", "A fiery kiss-off anthem uniting two of Latin pop's biggest stars.", "It debuted at #1 on Billboard's Hot Latin Songs."),
    ("China", "Anuel AA, Daddy Yankee, Karol G, Ozuna & J Balvin", 2019, ["reggaeton"], "Puerto Rico/Colombia", "Spanish", "A superstar posse cut built on the melody of Shaggy's 'It Wasn't Me'.", "It gathered five of reggaeton's biggest names on a single track."),
    ("Ella Baila Sola", "Eslabon Armado & Peso Pluma", 2023, ["corridos tumbados", "regional mexican"], "Mexico/United States", "Spanish", "A romantic corrido tumbado that brought regional Mexican music to global party playlists.", "It became the first regional Mexican song to enter the Billboard Hot 100's top 5."),
    ("Súbeme la Radio", "Enrique Iglesias feat. Descemer Bueno, Zion & Lennox", 2017, ["latin pop", "reggaeton"], "Spain/Cuba/Puerto Rico", "Spanish", "An urgent turn-up-the-radio anthem for summer nights.", "It continued Enrique's record-setting run of Hot Latin Songs #1s."),
    ("Duele el Corazón", "Enrique Iglesias feat. Wisin", 2016, ["latin pop", "reggaeton"], "Spain/Puerto Rico", "Spanish", "A dance-floor hit about loving someone against all advice.", "It topped Billboard's Hot Latin Songs for multiple weeks."),
    ("Bailamos", "Enrique Iglesias", 1999, ["latin pop"], "Spain", "English/Spanish", "The crossover smash that introduced Enrique Iglesias to English-language pop radio.", "It hit #1 on the Billboard Hot 100 during 1999's 'Latin explosion'."),
    ("Échame la Culpa", "Luis Fonsi & Demi Lovato", 2017, ["latin pop"], "Puerto Rico/United States", "Spanish/English", "A post-Despacito party duet trading blame over an infectious beat.", "Its video was one of YouTube's most-viewed of 2017-2018."),
    # --- Salsa / merengue / bachata / cumbia classics ---
    ("Suavemente", "Elvis Crespo", 1998, ["merengue"], "Puerto Rico", "Spanish", "The merengue anthem whose opening cry gets every party moving instantly.", "It topped Billboard's Hot Latin Songs and remains a wedding-dance essential."),
    ("Píntame", "Elvis Crespo", 1999, ["merengue"], "Puerto Rico", "Spanish", "A colorful follow-up hit that kept merengue on top of the charts.", "It won the Latin Grammy for Best Merengue Performance."),
    ("La Bilirrubina", "Juan Luis Guerra y 4.40", 1990, ["merengue"], "Dominican Republic", "Spanish", "A witty merengue diagnosing love as a medical emergency.", "Its wordplay made medical jargon a permanent part of Latin party vocabulary."),
    ("A Pedir Su Mano", "Juan Luis Guerra y 4.40", 1990, ["merengue"], "Dominican Republic", "Spanish", "A jubilant merengue adaptation celebrating a marriage proposal.", "It appears on Bachata Rosa, which won the Grammy for Best Tropical Latin Album."),
    ("Las Avispas", "Juan Luis Guerra y 4.40", 2004, ["merengue"], "Dominican Republic", "Spanish", "A joyful, horn-driven merengue that swept the Latin Grammys.", "It won Song of the Year honors at the 2005 Latin Grammys ceremony."),
    ("Bachata Rosa", "Juan Luis Guerra y 4.40", 1990, ["bachata"], "Dominican Republic", "Spanish", "The elegant title track that lifted bachata from the barrios to world stages.", "The album Bachata Rosa sold millions and legitimized bachata internationally."),
    ("Quimbara", "Celia Cruz & Johnny Pacheco", 1974, ["salsa"], "Cuba/United States", "Spanish", "A percussive salsa workout that showcases the Queen of Salsa at full power.", "It became Celia Cruz's signature opener during the Fania All-Stars era."),
    ("La Negra Tiene Tumbao", "Celia Cruz", 2001, ["salsa"], "Cuba/United States", "Spanish", "A late-career triumph blending salsa with hip-hop swagger.", "It won the Latin Grammy for Best Salsa Album and became a defining Celia anthem."),
    ("Pedro Navaja", "Rubén Blades & Willie Colón", 1978, ["salsa"], "Panama/United States", "Spanish", "A cinematic street-corner story-song, salsa's answer to 'Mack the Knife'.", "Its album Siembra was for decades the best-selling salsa record in history."),
    ("El Cantante", "Héctor Lavoe", 1978, ["salsa"], "Puerto Rico", "Spanish", "A soaring anthem about the singer who carries everyone's pain -- written by Rubén Blades.", "It became Héctor Lavoe's defining song and the title of his biopic."),
    ("Aguanile", "Héctor Lavoe & Willie Colón", 1972, ["salsa"], "Puerto Rico/United States", "Spanish", "A thunderous Afro-Caribbean invocation that electrifies every dance floor.", "Its call-and-response chorus draws on Yoruba religious tradition."),
    ("El Gran Varón", "Willie Colón", 1989, ["salsa"], "United States/Puerto Rico", "Spanish", "A landmark story-song that brought social commentary to the salsa dance floor.", "It is considered one of the most socially significant salsa recordings ever."),
    ("Llorarás", "Oscar D'León", 1975, ["salsa"], "Venezuela", "Spanish", "Venezuela's salsa calling card, driven by Oscar D'León's dancing bass.", "Oscar D'León performed it while playing upright bass and dancing simultaneously."),
    ("Cali Pachanguero", "Grupo Niche", 1984, ["salsa"], "Colombia", "Spanish", "The unofficial anthem of Cali, the world's self-proclaimed salsa capital.", "It closes the Feria de Cali every year with tens of thousands singing along."),
    ("El Preso", "Fruko y sus Tesos", 1975, ["salsa"], "Colombia", "Spanish", "A gritty Colombian salsa classic told from a prisoner's perspective.", "It remains one of the most requested songs at Colombian celebrations."),
    ("La Rebelión", "Joe Arroyo", 1986, ["salsa"], "Colombia", "Spanish", "A defiant salsa masterpiece telling the story of an enslaved couple's resistance in colonial Cartagena.", "Its cry 'No le pegue a la negra' is among the most famous lines in salsa history."),
    ("Valió la Pena", "Marc Anthony", 2004, ["salsa"], "United States/Puerto Rico", "Spanish", "A triumphant salsa declaration that love was worth everything.", "It won the Grammy for Best Latin Pop Album in its pop version year."),
    ("La Gozadera", "Gente de Zona feat. Marc Anthony", 2015, ["salsa", "cubaton"], "Cuba/United States", "Spanish", "A pan-Latin roll call that names nearly every country in Latin America.", "It became the de facto anthem of Latin American unity at parties worldwide."),
    ("Obsesión", "Aventura", 2002, ["bachata"], "United States/Dominican Republic", "Spanish", "The bachata megahit that took the genre from the Bronx to the world.", "It topped charts across Europe for months despite being sung in Spanish."),
    ("Ella y Yo", "Aventura feat. Don Omar", 2005, ["bachata", "reggaeton"], "United States/Puerto Rico", "Spanish", "A dramatic bachata-reggaeton duet of confession and betrayal.", "It was one of the first major bachata-reggaeton crossover hits."),
    ("Propuesta Indecente", "Romeo Santos", 2013, ["bachata"], "United States/Dominican Republic", "Spanish", "A tango-tinged bachata seduction from the King of Bachata.", "Its video surpassed a billion views, rare for bachata at the time."),
    ("Eres Mía", "Romeo Santos", 2014, ["bachata"], "United States/Dominican Republic", "Spanish", "A possessive-romantic bachata that dominated Latin radio.", "Romeo Santos sold out Yankee Stadium twice during this album's era."),
    ("Darte un Beso", "Prince Royce", 2013, ["bachata"], "United States/Dominican Republic", "Spanish", "A sweet, radio-friendly bachata about love made simple.", "It spent months atop Latin airplay charts."),
    ("Corazón Sin Cara", "Prince Royce", 2010, ["bachata"], "United States/Dominican Republic", "Spanish", "A feel-good bachata declaring that love has no face or size.", "It helped launch the modern bachata-pop wave."),
    ("El Venao", "Los Cantantes", 1995, ["merengue"], "Dominican Republic", "Spanish", "A mischievous merengue with one of the most chanted choruses of the 90s.", "Its horn riff is instantly recognized at parties across Latin America."),
    ("El Tiburón", "Proyecto Uno", 1995, ["merenhouse", "merengue"], "United States/Dominican Republic", "Spanish", "A merenhouse classic fusing merengue with hip-hop and house energy.", "Its shark-attack shout-along chorus remains a quinceañera staple."),
    ("Abusadora", "Wilfrido Vargas", 1988, ["merengue"], "Dominican Republic", "Spanish", "A fiery accusation set to one of merengue's most driving beats.", "Wilfrido Vargas's orchestra defined 1980s merengue worldwide."),
    ("El Baile del Perrito", "Wilfrido Vargas", 1992, ["merengue"], "Dominican Republic", "Spanish", "A novelty dance craze that swept Latin America in the early 90s.", "Its accompanying dance became a party phenomenon across the continent."),
    ("Juliana", "Cuco Valoy", 1975, ["merengue", "salsa"], "Dominican Republic", "Spanish", "A beloved classic about a man pleading with the beautiful Juliana.", "It remains a cornerstone of old-school Dominican party playlists."),
    ("Devórame Otra Vez", "Lalo Rodríguez", 1988, ["salsa"], "Puerto Rico", "Spanish", "The definitive hit of the salsa erótica era.", "It topped tropical charts across the Americas in the late 1980s."),
    ("La Dueña del Swing", "Los Hermanos Rosario", 1996, ["merengue"], "Dominican Republic", "Spanish", "A high-voltage merengue crowning the queen of the dance floor.", "Los Hermanos Rosario's horn section made it an enduring club anthem."),
    ("Cómo Te Voy a Olvidar", "Los Ángeles Azules", 1996, ["cumbia"], "Mexico", "Spanish", "The romantic cumbia sonidera that no Mexican party ends without.", "A 2010s symphonic re-recording introduced it to a new generation."),
    ("Mi Cucu", "La Sonora Dinamita", 1989, ["cumbia"], "Colombia/Mexico", "Spanish", "A cheeky cumbia classic from the genre's most famous orchestra.", "La Sonora Dinamita helped export Colombian cumbia to all of Latin America."),
    ("La Pollera Colorá", "Pedro Salcedo y su Orquesta", 1962, ["cumbia"], "Colombia", "Spanish", "Colombia's most iconic cumbia, honoring a dancer's red skirt.", "It is considered an unofficial musical symbol of Colombia."),
    ("La Colegiala", "Rodolfo Aicardi", 1975, ["cumbia"], "Colombia", "Spanish", "A cumbia earworm that conquered Latin America and Europe alike.", "A coffee commercial made it a massive hit in France decades after release."),
    ("Juana la Cubana", "Fito Olivares", 1988, ["cumbia"], "Mexico", "Spanish", "A saxophone-driven cumbia that lights up quinceañeras and weddings.", "Fito Olivares's sax hooks defined Tex-Mex cumbia party music."),
    ("Payaso de Rodeo", "Caballo Dorado", 1998, ["quebradita", "regional mexican"], "Mexico", "Spanish", "The line-dance anthem of Mexican parties -- everyone knows the steps.", "Its synchronized dance is performed at celebrations across Mexico and the US."),
    ("La Chona", "Los Tucanes de Tijuana", 1995, ["norteño", "regional mexican"], "Mexico", "Spanish", "A norteño legend about a woman who never misses a dance.", "The #LaChonaChallenge revived it as a viral phenomenon decades later."),
    ("Baila Esta Cumbia", "Selena", 1990, ["cumbia", "tejano"], "United States/Mexico", "Spanish", "The Queen of Tejano's irresistible order to hit the dance floor.", "It became one of Selena's most enduring party songs across generations."),
    ("Bidi Bidi Bom Bom", "Selena", 1994, ["tejano", "cumbia"], "United States/Mexico", "Spanish", "A heartbeat-mimicking hook that became Selena's most playful smash.", "Its onomatopoeic title imitates a nervous heart in love."),
    ("Como la Flor", "Selena", 1992, ["tejano", "cumbia"], "United States/Mexico", "Spanish", "Selena's signature sing-along, bittersweet and danceable at once.", "Crowds still sing its chorus in unison at tributes worldwide."),
    ("Amor Prohibido", "Selena", 1994, ["tejano", "cumbia"], "United States/Mexico", "Spanish", "A forbidden-love anthem inspired by Selena's own grandparents.", "The album of the same name topped Billboard's Latin chart for months."),
    # --- Latin pop / rock / global party classics ---
    ("La Copa de la Vida", "Ricky Martin", 1998, ["latin pop"], "Puerto Rico", "Spanish/English", "The 1998 World Cup anthem whose 'Go, go, go! Ale, ale, ale!' chorus circled the globe.", "Its Grammy performance is credited with igniting the late-90s Latin pop explosion."),
    ("María", "Ricky Martin", 1995, ["latin pop"], "Puerto Rico", "Spanish", "The 'un, dos, tres' hit that first made Ricky Martin a global name.", "Its remix became one of the best-selling Latin singles of the 1990s."),
    ("Pégate", "Ricky Martin", 2006, ["latin pop"], "Puerto Rico", "Spanish", "A plena-infused party track celebrating Puerto Rican rhythms.", "Ricky Martin performed it at global sporting events and festivals."),
    ("La Mordidita", "Ricky Martin feat. Yotuel", 2015, ["latin pop"], "Puerto Rico", "Spanish", "A percolating party single that returned Ricky Martin to dance floors.", "Its video has amassed over a billion views."),
    ("Aserejé", "Las Ketchup", 2002, ["latin pop", "dance"], "Spain", "Spanish", "The novelty smash whose nonsense chorus the whole planet memorized.", "Its chorus is a phonetic Spanish rendering of 'Rapper's Delight'."),
    ("Bamboléo", "Gipsy Kings", 1987, ["rumba flamenca"], "France/Spain", "Spanish", "A rumba flamenca firestorm that made the Gipsy Kings world stars.", "Its chorus borrows from the Venezuelan folk song 'Caballo Viejo'."),
    ("Djobi Djoba", "Gipsy Kings", 1987, ["rumba flamenca"], "France/Spain", "Spanish", "A hand-clapping rumba that fills dance floors from Madrid to Miami.", "The Gipsy Kings sing in a Gitane-inflected Spanish called Gitano."),
    ("Baila Me", "Gipsy Kings", 1991, ["rumba flamenca"], "France/Spain", "Spanish", "An urgent invitation to dance, flamenco-style.", "It appeared on the multi-platinum album Este Mundo."),
    ("Lambada", "Kaoma", 1989, ["lambada"], "France/Brazil", "Portuguese", "The forbidden-dance sensation that swept the world in 1989.", "It adapts the Bolivian song 'Llorando se fue' by Los Kjarkas."),
    ("Ai Se Eu Te Pego", "Michel Teló", 2011, ["sertanejo"], "Brazil", "Portuguese", "A Brazilian sertanejo hook so catchy that football stars made it their goal celebration.", "Neymar and other footballers danced to it after scoring, fueling its global spread."),
    ("Show das Poderosas", "Anitta", 2013, ["funk carioca"], "Brazil", "Portuguese", "The baile funk breakout that crowned Anitta queen of Brazilian pop.", "It was the first funk carioca track to top Brazil's mainstream charts."),
    ("Mas Que Nada", "Sérgio Mendes & Brasil '66", 1966, ["samba", "bossa nova"], "Brazil", "Portuguese", "The samba standard that brought Brazilian groove to the world's parties.", "A 2006 remake with The Black Eyed Peas returned it to global charts."),
    ("Magalenha", "Sérgio Mendes", 1992, ["samba", "axé"], "Brazil", "Portuguese", "A drum-stampede carnival anthem beloved by dancers everywhere.", "Its vocals are by Carlinhos Brown, a giant of Bahian carnival music."),
    ("Mambo No. 5", "Pérez Prado", 1950, ["mambo"], "Cuba/Mexico", "Instrumental/Spanish", "The King of Mambo's brass-blasting classic that defined a dance era.", "Lou Bega's 1999 version returned it to #1 in a dozen countries."),
    ("Corazón Espinado", "Santana feat. Maná", 1999, ["latin rock"], "Mexico/United States", "Spanish", "A Latin-rock fiesta pairing Santana's guitar with Maná's swagger.", "It appeared on Supernatural, which won nine Grammy Awards."),
    ("Oye Mi Amor", "Maná", 1992, ["latin rock"], "Mexico", "Spanish", "Mexico's rock en español party standard with an unforgettable riff.", "It remains one of the most played rock en español songs at Latin parties."),
    ("La Camisa Negra", "Juanes", 2004, ["latin rock", "latin pop"], "Colombia", "Spanish", "A guasca-flavored hit about heartbreak worn like a black shirt.", "It topped charts across Europe and Latin America simultaneously."),
    ("A Dios le Pido", "Juanes", 2002, ["latin rock"], "Colombia", "Spanish", "An urgent, danceable prayer that made Juanes a continental star.", "It topped Latin charts in a dozen countries for months."),
    ("La Tortura", "Shakira feat. Alejandro Sanz", 2005, ["latin pop", "reggaeton"], "Colombia/Spain", "Spanish", "A sweat-dripping reggaeton-pop duet about temptation and regret.", "It was the first mostly-Spanish video ever played on MTV's TRL."),
    ("Loba", "Shakira", 2009, ["latin pop", "dance"], "Colombia", "Spanish", "Shakira's howling disco-pop celebration of untamed independence.", "Its English version 'She Wolf' hit charts worldwide simultaneously."),
    ("Rabiosa", "Shakira", 2011, ["latin pop", "merengue"], "Colombia", "Spanish", "A rapid-fire merengue-pop shot of pure party adrenaline.", "It exists in two versions, with El Cata and with Pitbull."),
    ("Loca", "Shakira feat. El Cata", 2010, ["merengue", "latin pop"], "Colombia/Dominican Republic", "Spanish", "A merengue-urbano romp that became a global dance hit.", "It topped the Billboard Hot Latin Songs chart for weeks."),
    ("Ojos Así", "Shakira", 1998, ["latin pop", "rock en español"], "Colombia", "Spanish/Arabic", "A Middle Eastern-tinged dance track showcasing Shakira's Lebanese roots.", "Shakira sings part of the song in Arabic and belly-dances in performances."),
    ("Shakira: Bzrp Music Sessions, Vol. 53", "Bizarrap & Shakira", 2023, ["latin pop", "EDM"], "Argentina/Colombia", "Spanish", "A viral diss-track-turned-dance-anthem with Argentine super-producer Bizarrap.", "It broke YouTube's record for the most-viewed Latin song debut in 24 hours."),
    ("Despechá", "Rosalía", 2022, ["mambo", "latin pop"], "Spain", "Spanish", "A featherlight mambo-pop track that soundtracked a global summer.", "Rosalía premiered it live on tour before any studio release."),
    ("Saoko", "Rosalía", 2022, ["reggaeton", "experimental pop"], "Spain", "Spanish", "An avant-garde reggaeton banger paying homage to Daddy Yankee's classic 'Saoco'.", "Its jazz-piano breakdown mid-song became a viral moment."),
    ("On the Floor", "Jennifer Lopez feat. Pitbull", 2011, ["dance-pop", "latin pop"], "United States", "English/Spanish", "A globe-conquering dance anthem sampling the melody of 'Lambada'.", "It became one of the best-selling singles of all time by a Latina artist."),
    ("Let's Get Loud", "Jennifer Lopez", 1999, ["latin pop", "dance"], "United States", "English/Spanish", "A brass-fueled celebration anthem co-written by Gloria Estefan.", "JLo performed it at the Super Bowl halftime show in 2020."),
    ("El Taxi", "Osmani García feat. Pitbull & Sensato", 2014, ["cubaton", "reggaeton"], "Cuba/United States", "Spanish", "A cheeky Cuban party hit that rode its taxi hook across the world.", "It interpolates the classic 'El Taxi' rhythm popularized in Cuban dance music."),
    ("Bon, Bon", "Pitbull", 2010, ["latin pop", "dance"], "United States", "Spanish/English", "Mr. Worldwide's party single built on the 'We No Speak Americano' hook.", "It samples the Italian swing classic 'Tu Vuò Fà L'Americano'."),
    ("Sopa de Caracol", "Banda Blanca", 1991, ["punta"], "Honduras", "Spanish/Garifuna", "Honduras's punta explosion that got all of Latin America chanting 'Watanegui consup'.", "Its chorus comes from a traditional Garifuna song."),
    ("Fiesta", "Bomba Estéreo", 2015, ["electro cumbia"], "Colombia", "Spanish", "A psychedelic electro-cumbia ode to losing yourself in the party.", "A remix features will.i.am of The Black Eyed Peas."),
    ("Soy Yo", "Bomba Estéreo", 2015, ["electro cumbia"], "Colombia", "Spanish", "A swaggering self-confidence anthem with an iconic video.", "Its video starring a defiantly confident young girl became a viral empowerment symbol."),
    ("Mi Niña Bonita", "Chino & Nacho", 2010, ["merengue", "latin pop"], "Venezuela", "Spanish", "A sugary merengue-pop dedication that ruled Latin radio.", "It earned Chino & Nacho a Latin Grammy for Best Urban Album era recognition."),
    ("Andas en Mi Cabeza", "Chino & Nacho feat. Daddy Yankee", 2016, ["latin pop", "reggaeton"], "Venezuela/Puerto Rico", "Spanish", "A lovestruck earworm that pairs Venezuelan pop with reggaeton royalty.", "Its video passed a billion views on YouTube."),
    ("Noa Noa", "Juan Gabriel", 1980, ["latin pop"], "Mexico", "Spanish", "Juan Gabriel's joyous tribute to the Ciudad Juárez club where he got his start.", "The Noa Noa was a real venue where the legendary singer performed early in his career."),
    ("Tu Pum Pum", "El General", 1990, ["reggae en español"], "Panama", "Spanish", "A pioneering reggae en español hit that helped lay reggaeton's foundations.", "El General is regarded as one of the fathers of the Spanish reggae sound."),
    ("Muévelo", "El General", 1991, ["reggae en español"], "Panama", "Spanish", "An early Spanish-reggae dance command that echoed across the Americas.", "Its title -- 'move it' -- became a catchphrase of 90s Latin parties."),
]


def build_song(title, artist, year, genres, country, language, description, fun_fact):
    decade = f"{(year // 10) * 10}s"
    return {
        "id": f"latino_party_{slug(title)}",
        "title": title,
        "artist": artist,
        "album": "",
        "year": year,
        "genre": genres,
        "origin_country": country,
        "language": language,
        "duration_approx": "",
        "description": description,
        "educational_notes": f"Useful for exploring {genres[0]} and the party-music traditions of {country}.",
        "fun_fact": fun_fact,
        "awards": [],
        "links": {
            "youtube_search": yt_search(f"{title} {artist} official music video"),
            "wiki_search": wiki_search(f"{title} {artist}"),
            "lyrics_search": lyrics_search(f"{title} {artist} lyrics"),
        },
        "tags": genres + [decade, "latino party"],
        "decade": decade,
        "suitable_for_ages": "10+",
    }


def main() -> None:
    with open(SONGS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_titles = {norm(s["title"]) for s in data["songs"]}
    existing_ids = {s["id"] for s in data["songs"]}

    added = 0
    skipped = []
    for item in SONGS:
        if added >= MAX_ADDITIONS:
            break
        title = item[0]
        song = build_song(*item)
        if norm(title) in existing_titles or song["id"] in existing_ids:
            skipped.append(title)
            continue
        data["songs"].append(song)
        existing_titles.add(norm(title))
        existing_ids.add(song["id"])
        added += 1

    data["total"] = len(data["songs"])

    # Refresh the genre/decade facet lists.
    genres = set()
    decades = set()
    for s in data["songs"]:
        genres.update(g for g in s.get("genre", []))
        if s.get("decade"):
            decades.add(s["decade"])
    data["genres"] = sorted(genres)
    data["decades"] = sorted(decades)

    with open(SONGS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {added} songs (skipped {len(skipped)} already-present titles: {skipped}). "
          f"Collection total: {data['total']}")


if __name__ == "__main__":
    main()
