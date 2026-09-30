#!/usr/bin/env python3
"""Populate the "Visual Arts & Music" biography category with real,
verified painters, sculptors, and composers/musicians. See
_biography_engine.py for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_arts_music.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="leonardo_da_vinci", name="Leonardo da Vinci", years="1452-1519", nationality="Italian",
        field="painter, engineer, and scientist", wiki_title="Leonardo da Vinci",
        significance="regarded as the archetypal Renaissance man, he painted the Mona Lisa and The Last Supper while also producing detailed scientific and engineering studies far ahead of his time",
        facts=[
            "Leonardo da Vinci was born in Vinci, near Florence, Italy, in 1452, the illegitimate son of a notary",
            "He trained in the workshop of the Florentine painter Andrea del Verrocchio as a young man",
            "He painted the Mona Lisa, likely between 1503 and 1519, now housed in the Louvre in Paris and one of the most famous paintings in the world",
            "He painted The Last Supper, a mural in Milan, between approximately 1495 and 1498",
            "He filled thousands of pages of notebooks with studies on anatomy, flight, engineering, and hydraulics, often written in mirror-image handwriting",
            "His anatomical drawings, based on dissections he conducted himself, were remarkably accurate for their time",
            "He died in France in 1519, having spent his final years under the patronage of King Francis I",
        ], related_subjects=["Art", "Art History", "Science"],
    ),
    dict(
        id="michelangelo", name="Michelangelo", years="1475-1564", nationality="Italian",
        field="sculptor and painter", wiki_title="Michelangelo",
        significance="his sculpture David and his frescoes on the ceiling of the Sistine Chapel are considered among the greatest achievements of Renaissance art",
        facts=[
            "Michelangelo di Lodovico Buonarroti Simoni was born in Caprese, Italy, in 1475",
            "He carved the marble statue David between 1501 and 1504, depicting the biblical hero before his battle with Goliath, standing over 17 feet tall",
            "He painted the ceiling of the Sistine Chapel in Vatican City between 1508 and 1512, working largely alone on scaffolding for four years",
            "The Sistine Chapel ceiling includes the famous scene The Creation of Adam, depicting God's hand reaching toward Adam's",
            "He also carved the Pieta, a sculpture of the Virgin Mary holding the body of Jesus, completed around 1499 when he was in his early twenties",
            "He served as chief architect of St. Peter's Basilica in Rome later in life, designing its dome",
            "He died in Rome in 1564 at age 88, having worked as an artist for over 70 years",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="ludwig_van_beethoven", name="Ludwig van Beethoven", years="1770-1827", nationality="German",
        field="composer", wiki_title="Ludwig van Beethoven",
        significance="he composed some of the most influential music in Western classical tradition, including his Ninth Symphony, and continued composing after becoming almost completely deaf",
        facts=[
            "Ludwig van Beethoven was born in Bonn, in what is now Germany, in 1770, and showed early musical talent under his father's strict tutelage",
            "He moved to Vienna in 1792 to study composition, eventually with Joseph Haydn",
            "He began losing his hearing in his late twenties, and by his late forties was almost completely deaf",
            "Despite his deafness, he continued composing, reportedly using a wooden rod placed against the piano and his teeth to feel vibrations",
            "He composed nine symphonies, of which the Ninth, completed in 1824 and including the choral 'Ode to Joy', is among the most performed works in classical music",
            "He conducted the premiere of the Ninth Symphony despite his profound deafness, and had to be turned around by a singer to see the audience's applause, which he could not hear",
            "He died in Vienna in 1827, and an estimated 10,000 to 30,000 people attended his funeral procession",
        ], related_subjects=["Music"],
    ),
    dict(
        id="wolfgang_amadeus_mozart", name="Wolfgang Amadeus Mozart", years="1756-1791", nationality="Austrian",
        field="composer", wiki_title="Wolfgang Amadeus Mozart",
        significance="a child prodigy who composed his first pieces at age five, he produced over 600 works across nearly every musical genre of his era before his death at 35",
        facts=[
            "Wolfgang Amadeus Mozart was born in Salzburg, in what is now Austria, in 1756",
            "He began composing music at age five and was performing for European royalty by age six, touring with his father and sister",
            "He composed over 600 works during his lifetime, including symphonies, operas, concertos, and chamber music",
            "His operas include The Marriage of Figaro (1786), Don Giovanni (1787), and The Magic Flute (1791)",
            "He worked as a freelance composer for much of his career, unusual for the time when most composers relied on a single wealthy patron",
            "He composed his final work, the Requiem Mass, while gravely ill, and it remained unfinished at his death, later completed by his student Franz Xaver Sussmayr",
            "He died in Vienna in 1791 at age 35, and was buried in a common grave, as was standard practice in Vienna at the time",
        ], related_subjects=["Music"],
    ),
    dict(
        id="vincent_van_gogh", name="Vincent van Gogh", years="1853-1890", nationality="Dutch",
        field="painter", wiki_title="Vincent van Gogh",
        significance="though he sold only one painting during his lifetime, his bold, expressive works such as The Starry Night later became among the most beloved and valuable paintings in the world",
        facts=[
            "Vincent van Gogh was born in Groot-Zundert, in the Netherlands, in 1853",
            "He did not begin painting seriously until his late twenties, after earlier working as an art dealer, teacher, and missionary",
            "He produced over 2,100 artworks in roughly a decade, including around 860 oil paintings, working with extraordinary intensity",
            "He famously cut off part of his own ear in 1888 following a mental health crisis and a heated dispute with fellow painter Paul Gauguin",
            "He painted The Starry Night in 1889 while staying at an asylum in Saint-Remy-de-Provence, France, following a period of severe mental illness",
            "He sold only one painting during his lifetime, and relied financially on his brother Theo, an art dealer, for most of his life",
            "He died in 1890 from a gunshot wound, generally believed to be self-inflicted, at age 37",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="pablo_picasso", name="Pablo Picasso", years="1881-1973", nationality="Spanish",
        field="painter and sculptor", wiki_title="Pablo Picasso",
        significance="co-founder of the Cubist movement, he is considered one of the most influential artists of the 20th century, and produced an estimated 50,000 artworks over his career",
        facts=[
            "Pablo Picasso was born in Malaga, Spain, in 1881, and showed exceptional artistic talent from early childhood",
            "He moved to Paris as a young man and, along with Georges Braque, developed Cubism in the early 1900s, a style that depicted subjects from multiple angles simultaneously",
            "He painted Guernica in 1937, a large mural protesting the bombing of the Basque town of Guernica during the Spanish Civil War",
            "He worked across an extraordinary range of styles and periods, including his 'Blue Period' and 'Rose Period', in addition to Cubism",
            "He produced an estimated 50,000 artworks over his lifetime, including paintings, sculptures, ceramics, and prints",
            "He remained politically active, joining the French Communist Party in 1944 in the aftermath of World War II",
            "He died in France in 1973 at age 91, having remained artistically active until close to the end of his life",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="frida_kahlo", name="Frida Kahlo", years="1907-1954", nationality="Mexican",
        field="painter", wiki_title="Frida Kahlo",
        significance="her vivid, often surreal self-portraits explored themes of identity, pain, and Mexican culture, and she became a major figure of 20th-century art and a lasting cultural icon",
        facts=[
            "Frida Kahlo was born in Coyoacan, Mexico City, in 1907",
            "As a teenager she was severely injured in a bus accident in 1925 that fractured her spine and pelvis, leading to lifelong chronic pain and dozens of surgeries",
            "She began painting seriously during her long recovery, often working from a specially made bed with a mirror mounted above her",
            "About a third of her roughly 200 paintings are self-portraits, exploring physical and emotional pain, identity, and Mexican heritage",
            "She married the prominent Mexican muralist Diego Rivera in 1929, in a relationship marked by mutual artistic respect and personal turbulence",
            "She was closely connected to Mexican political and cultural movements and hosted exiled Soviet revolutionary Leon Trotsky at her family home for a period",
            "Her home in Coyoacan, known as the Blue House, is now a museum dedicated to her life and work",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="johann_sebastian_bach", name="Johann Sebastian Bach", years="1685-1750", nationality="German",
        field="composer and organist", wiki_title="Johann Sebastian Bach",
        significance="his mastery of counterpoint and harmonic structure in works such as the Brandenburg Concertos and the Mass in B Minor made him one of the most influential composers in the history of Western music",
        facts=[
            "Johann Sebastian Bach was born in Eisenach, in what is now Germany, in 1685, into a family with generations of professional musicians",
            "He worked as a church organist and choir director in several German towns, including a long tenure at St. Thomas Church in Leipzig from 1723 until his death",
            "He composed the six Brandenburg Concertos around 1721, dedicated to a German margrave, showcasing his skill with instrumental combinations",
            "He wrote hundreds of cantatas for weekly church services, in addition to major works like the Mass in B Minor and the St. Matthew Passion",
            "He was the father of 20 children, several of whom, including Carl Philipp Emanuel Bach and Johann Christian Bach, became notable composers themselves",
            "His music fell into relative obscurity after his death until a revival led by composer Felix Mendelssohn in the 1820s and 1830s",
            "He died in Leipzig in 1750, and is now widely regarded as one of the greatest composers in Western musical history",
        ], related_subjects=["Music"],
    ),
    dict(
        id="claude_monet", name="Claude Monet", years="1840-1926", nationality="French",
        field="painter", wiki_title="Claude Monet",
        significance="a founder of French Impressionist painting, his series of water lily paintings, created in his garden at Giverny, are among the most recognized works in modern art",
        facts=[
            "Claude Monet was born in Paris in 1840 and grew up largely in Le Havre, France",
            "His 1872 painting Impression, Sunrise gave the Impressionist movement its name, after a critic used the title mockingly",
            "He and fellow artists organized independent exhibitions starting in 1874, breaking from the official, more conservative Paris Salon",
            "He often painted the same subject repeatedly at different times of day to study changing light, including his series of Rouen Cathedral and haystacks",
            "In 1883 he moved to Giverny, France, where he created an elaborate garden with a Japanese-style bridge and water lily pond that became the subject of over 250 paintings",
            "He continued painting his water lily series even as cataracts severely affected his eyesight in his later years",
            "He died in Giverny in 1926, and his garden remains open to visitors today as a major cultural site",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="louis_armstrong", name="Louis Armstrong", years="1901-1971", nationality="American",
        field="jazz musician and singer", wiki_title="Louis Armstrong",
        significance="a foundational figure in jazz, his innovative trumpet playing and distinctive singing style helped shape jazz as a major American art form and brought it to global audiences",
        facts=[
            "Louis Armstrong was born in New Orleans, Louisiana, in 1901, and grew up in poverty in a neighborhood known for its jazz music",
            "He learned to play the cornet at the Colored Waif's Home for Boys, a reform school he was sent to as a child",
            "He moved to Chicago in 1922 to join King Oliver's Creole Jazz Band, and soon became known for his virtuosic trumpet improvisation",
            "His recordings with the Hot Five and Hot Seven groups in the late 1920s are considered foundational works in the development of jazz as a solo-improvisation art form",
            "His distinctive gravelly singing voice became widely known through hits including 'What a Wonderful World' in 1967",
            "He toured internationally for decades and was one of the first African American entertainers to achieve widespread crossover popularity with white audiences in the United States",
            "He died in New York City in 1971, and remains one of the most influential musicians in the history of jazz",
        ], related_subjects=["Music"],
    ),
    dict(
        id="beyonce", name="Beyonce", years="1981-present", nationality="American",
        field="singer, songwriter, and performer", wiki_title="Beyonce",
        significance="one of the best-selling music artists of all time, she holds the record for the most Grammy Awards won by any artist in history",
        facts=[
            "Beyonce Giselle Knowles was born in Houston, Texas, in 1981",
            "She rose to fame as the lead singer of Destiny's Child, one of the best-selling girl groups of all time, before launching a solo career in the early 2000s",
            "Her solo albums include Dangerously in Love (2003), Lemonade (2016), and Renaissance (2022)",
            "As of the mid-2020s she holds the record for the most Grammy Awards won by any artist in history, with more than 30 wins",
            "Her 2016 visual album Lemonade received widespread critical acclaim for its exploration of Black womanhood, identity, and personal narrative",
            "She has also pursued acting, appearing in films including Dreamgirls (2006) and voicing Nala in Disney's 2019 remake of The Lion King",
            "She co-founded the entertainment company Parkwood Entertainment and has been recognized repeatedly by Time magazine as one of the most influential people in the world",
        ], related_subjects=["Music"],
    ),
    dict(
        id="the_beatles", name="The Beatles (John Lennon, Paul McCartney, George Harrison, Ringo Starr)", years="1960-1970 (as a group)", nationality="British",
        field="rock band", wiki_title="The Beatles",
        significance="widely regarded as the most influential band in the history of popular music, they transformed songwriting, recording technique, and the culture surrounding popular music during the 1960s",
        facts=[
            "The Beatles formed in Liverpool, England, in 1960, with the classic lineup of John Lennon, Paul McCartney, George Harrison, and Ringo Starr solidifying by 1962",
            "Their 1964 appearance on The Ed Sullivan Show in the United States was watched by an estimated 73 million viewers and helped launch what became known as the British Invasion of American popular music",
            "They released 12 studio albums in just eight years, including Rubber Soul (1965), Revolver (1966), and Sgt. Pepper's Lonely Hearts Club Band (1967)",
            "Sgt. Pepper's Lonely Hearts Club Band is widely credited with elevating the rock album into a serious, cohesive artistic format rather than a simple collection of singles",
            "They stopped touring in 1966 to focus entirely on studio recording, pioneering new production and recording techniques with producer George Martin",
            "The band broke up in 1970 amid personal and business tensions, though all four members went on to notable solo careers",
            "They remain the best-selling music act in history, with estimated sales of over 600 million records worldwide",
        ], related_subjects=["Music"],
    ),
    dict(
        id="salvador_dali", name="Salvador Dali", years="1904-1989", nationality="Spanish",
        field="surrealist painter", wiki_title="Salvador Dali",
        significance="one of the most prominent Surrealist artists, his painting The Persistence of Memory, with its melting clocks, became one of the most recognized images in modern art",
        facts=[
            "Salvador Dali was born in Figueres, Spain, in 1904",
            "He studied at the Royal Academy of Fine Arts in Madrid before being drawn into the Surrealist movement in Paris in the late 1920s",
            "His 1931 painting The Persistence of Memory, depicting melting pocket watches in a desert landscape, became one of the most iconic Surrealist artworks",
            "He developed what he called the 'paranoiac-critical method', a technique for accessing subconscious imagery to inspire his art",
            "He cultivated an eccentric public persona, famous for his elaborately curled mustache and flamboyant behavior",
            "He worked across many media beyond painting, including sculpture, film (collaborating with director Luis Bunuel), and even a dream sequence for Alfred Hitchcock's 1945 film Spellbound",
            "He established the Dali Theatre-Museum in his hometown of Figueres, which he designed himself and which remains a major museum today",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="bob_marley", name="Bob Marley", years="1945-1981", nationality="Jamaican",
        field="reggae musician", wiki_title="Bob Marley",
        significance="he brought reggae music to a global audience and became an international symbol of Jamaican culture, social justice, and Rastafarian spirituality",
        facts=[
            "Bob Marley was born in Nine Mile, Jamaica, in 1945",
            "He formed the group The Wailers with Peter Tosh and Bunny Wailer in Kingston in the early 1960s",
            "His album Exodus, released in 1977, was later named Album of the Century by Time magazine",
            "Songs including 'No Woman, No Cry', 'One Love', and 'Redemption Song' became widely recognized anthems associated with peace and social justice",
            "In 1976 he survived an assassination attempt at his home in Kingston, an event widely believed to be linked to Jamaica's tense political climate at the time",
            "He was a devoted follower of the Rastafari religious and cultural movement, which strongly influenced both his music and his public image",
            "He died of cancer in 1981 at age 36, and remains one of the best-selling music artists of all time, with estimated sales of over 75 million records",
        ], related_subjects=["Music"],
    ),
    dict(
        id="georgia_okeeffe", name="Georgia O'Keeffe", years="1887-1986", nationality="American",
        field="painter", wiki_title="Georgia O'Keeffe",
        significance="often called the 'Mother of American Modernism', her large-scale paintings of flowers and New Mexico desert landscapes established a distinctly American form of modern art",
        facts=[
            "Georgia O'Keeffe was born on a farm near Sun Prairie, Wisconsin, in 1887",
            "She studied at the Art Institute of Chicago and the Art Students League of New York before developing her own distinctive style",
            "Her large-scale, close-up paintings of flowers, beginning in the 1920s, became some of her most recognized work",
            "She married photographer and gallery owner Alfred Stieglitz in 1924, who was also instrumental in promoting her early career",
            "Beginning in the 1930s she spent increasing time in New Mexico, and her paintings of desert landscapes, animal bones, and adobe architecture became central to her later work",
            "She moved permanently to New Mexico in 1949, three years after Stieglitz's death, settling at her Ghost Ranch property",
            "She continued painting into her nineties despite failing eyesight, and died in Santa Fe, New Mexico, in 1986 at age 98",
        ], related_subjects=["Art", "Art History"],
    ),
]

PEOPLE += [
    dict(
        id="andy_warhol", name="Andy Warhol", years="1928-1987", nationality="American",
        field="artist and filmmaker", wiki_title="Andy Warhol",
        significance="a leading figure of the Pop Art movement, his depictions of consumer products and celebrities, such as his Campbell's Soup Cans, redefined what could be considered fine art",
        facts=[
            "Andy Warhol was born Andrew Warhola in Pittsburgh, Pennsylvania, in 1928, to working-class immigrant parents",
            "He began his career as a commercial illustrator in New York before moving into fine art in the early 1960s",
            "His 1962 series Campbell's Soup Cans, depicting 32 canvases of soup can varieties, became a defining work of the Pop Art movement",
            "He pioneered the use of silkscreen printing in fine art, allowing him to mass-produce images in a way that echoed the consumer culture he depicted",
            "He established The Factory, his New York studio, as a hub for artists, musicians, and celebrities throughout the 1960s",
            "He survived a near-fatal shooting in 1968 by a woman associated with his studio, an event that led him to become more guarded in his later years",
            "He died in New York City in 1987 following complications from gallbladder surgery",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="freddie_mercury", name="Freddie Mercury", years="1946-1991", nationality="British",
        field="singer and songwriter", wiki_title="Freddie Mercury",
        significance="as the lead vocalist of the rock band Queen, his powerful four-octave vocal range and flamboyant stage presence made him one of the most celebrated performers in rock music history",
        facts=[
            "Freddie Mercury was born Farrokh Bulsara in Stone Town, Zanzibar, in 1946, to Parsi Indian parents",
            "His family relocated to England in 1964 following political unrest in Zanzibar",
            "He joined the band that became Queen in 1970 and suggested both the band's name and designed its crest logo",
            "He wrote or co-wrote many of Queen's biggest hits, including 'Bohemian Rhapsody' (1975), a genre-defying six-minute single that became one of the best-selling singles in UK chart history",
            "Queen's performance at the 1985 Live Aid benefit concert at Wembley Stadium is widely regarded as one of the greatest live rock performances ever recorded",
            "He was known for a vocal range spanning nearly four octaves and a highly theatrical stage presence",
            "He died in London in 1991, one day after publicly confirming he had AIDS, and his death significantly raised public awareness of the disease",
        ], related_subjects=["Music"],
    ),
    dict(
        id="frank_lloyd_wright", name="Frank Lloyd Wright", years="1867-1959", nationality="American",
        field="architect", wiki_title="Frank Lloyd Wright",
        significance="regarded as one of the greatest architects in American history, he designed over 1,000 structures, including Fallingwater, and pioneered the organic architecture movement",
        facts=[
            "Frank Lloyd Wright was born in Richland Center, Wisconsin, in 1867",
            "He developed the Prairie School style of architecture in the early 1900s, characterized by low horizontal lines that echoed the flat American Midwestern landscape",
            "He designed Fallingwater in Pennsylvania in 1935, a house built dramatically over a waterfall, widely regarded as one of the greatest works of American architecture",
            "He designed the Solomon R. Guggenheim Museum in New York City, with its distinctive spiral interior, completed in 1959, shortly after his death",
            "Over his roughly 70-year career he designed more than 1,000 structures, of which about 532 were completed",
            "He promoted a philosophy he called 'organic architecture', in which buildings were designed to be in harmony with their natural surroundings and inhabitants",
            "He died in 1959 at age 91, just months before the completion of the Guggenheim Museum",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="rembrandt", name="Rembrandt van Rijn", years="1606-1669", nationality="Dutch",
        field="painter", wiki_title="Rembrandt",
        significance="widely regarded as one of the greatest painters and printmakers in European art history, his mastery of light and shadow and psychologically penetrating portraits defined the Dutch Golden Age of painting",
        facts=[
            "Rembrandt van Rijn was born in Leiden, in the Dutch Republic, in 1606",
            "He became one of the most sought-after portrait painters in Amsterdam during the 1630s, running a large and successful workshop",
            "His 1642 painting The Night Watch, a large group portrait of a civic militia company, is considered one of the most important works of the Dutch Golden Age",
            "He was known for his distinctive use of dramatic light and shadow, a technique called chiaroscuro, which gave his paintings striking emotional depth",
            "He painted an unusually large number of self-portraits over his lifetime, around 40 paintings plus additional prints and drawings, offering a visual record of his own aging and changing circumstances",
            "He experienced serious financial difficulty later in life, declaring bankruptcy in 1656 after years of overspending on art and antiques",
            "He died in Amsterdam in 1669, and is now regarded as one of the most technically accomplished and influential painters in Western art history",
        ], related_subjects=["Art", "Art History"],
    ),
    dict(
        id="jimi_hendrix", name="Jimi Hendrix", years="1942-1970", nationality="American",
        field="guitarist and songwriter", wiki_title="Jimi Hendrix",
        significance="widely regarded as one of the most influential electric guitarists in the history of popular music, his innovative use of guitar feedback, distortion, and improvisation redefined the instrument's possibilities in rock music",
        facts=[
            "Jimi Hendrix was born in Seattle, Washington, in 1942, and taught himself to play guitar largely by ear",
            "He served briefly in the US Army before pursuing music full time, working as a backing guitarist for various rhythm and blues acts in the early 1960s",
            "He formed the Jimi Hendrix Experience in London in 1966, quickly gaining attention for his innovative and highly technical guitar playing",
            "His 1967 performance at the Monterey Pop Festival, during which he set his guitar on fire, became one of the most iconic moments in rock concert history",
            "His improvised, feedback-heavy rendition of 'The Star-Spangled Banner' at the 1969 Woodstock Festival became one of the most famous performances in American music history",
            "He pioneered numerous guitar effects and playing techniques, including creative use of feedback, distortion, and the wah-wah pedal, expanding what the electric guitar could do",
            "He died in London in 1970 at age 27, and remains widely regarded as one of the most influential guitarists in the history of popular music",
        ], related_subjects=["Music"],
    ),
    dict(
        id="maria_callas", name="Maria Callas", years="1923-1977", nationality="Greek-American",
        field="opera singer", wiki_title="Maria Callas",
        significance="widely regarded as one of the greatest opera singers of the 20th century, her combination of vocal skill and dramatic acting ability transformed expectations for operatic performance",
        facts=[
            "Maria Callas was born in New York City in 1923 to Greek immigrant parents, and moved to Greece as a teenager to study voice",
            "She rose to international fame in the late 1940s and 1950s, performing at major opera houses including La Scala in Milan and the Metropolitan Opera in New York",
            "She was known for an unusually wide vocal range and was able to perform demanding roles across different vocal categories that most singers specialized narrowly within",
            "She placed strong emphasis on dramatic acting alongside vocal technique, helping revive interest in bel canto opera works that had fallen out of the regular performance repertoire",
            "Her personal life, including a highly publicized relationship with Greek shipping magnate Aristotle Onassis, drew significant tabloid attention alongside her musical career",
            "Her vocal abilities declined significantly in her later career, a decline widely discussed and analyzed by music critics and historians",
            "She died in Paris in 1977, and remains widely regarded as one of the most influential opera singers of the 20th century",
        ], related_subjects=["Music"],
    ),
    dict(
        id="banksy", name="Banksy", years="active since c. 1990s-present", nationality="British (anonymous)",
        field="street artist", wiki_title="Banksy",
        significance="an anonymous street artist whose politically charged stencil-based works, often created illegally on public walls, have become some of the most recognized and highly valued art of the early 21st century",
        facts=[
            "Banksy is the pseudonym of an anonymous artist believed to be from Bristol, England, whose true identity has never been officially confirmed",
            "His works typically use a distinctive stencil technique, allowing pieces to be created quickly, often illegally, on public walls and structures",
            "His art frequently addresses political and social themes, including war, capitalism, consumerism, and authority, often blending dark humor with sharp critique",
            "In 2005 he created several works on the Israeli West Bank barrier wall, drawing international attention to the structure and to his own work",
            "In 2018 a version of his painting Girl with Balloon partially shredded itself via a hidden mechanism immediately after being sold at auction, an act widely covered internationally as a comment on the art market",
            "He directed the 2010 documentary film Exit Through the Gift Shop, examining street art culture, which was nominated for an Academy Award",
            "Despite his anonymity, his works regularly sell for millions of dollars at auction, and his identity remains one of the most persistent mysteries in contemporary art",
        ], related_subjects=["Art"],
    ),
]


def main() -> None:
    upsert_section(
        "arts_music",
        "Visual Arts & Music",
        "🎨",
        "Painters, sculptors, architects, and musicians whose work defined artistic movements and moved audiences across generations.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
