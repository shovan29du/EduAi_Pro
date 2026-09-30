#!/usr/bin/env python3
"""Populate the "Film, Media & Entertainment" biography category with
real, verified filmmakers, actors, and entertainers. See
_biography_engine.py for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_entertainment.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="charlie_chaplin", name="Charlie Chaplin", years="1889-1977", nationality="British",
        field="actor, director, and comedian", wiki_title="Charlie Chaplin",
        significance="through his 'Tramp' character, he became the most famous entertainer in the world during the silent film era, and later became an influential writer, director, and composer of his own films",
        facts=[
            "Charlie Chaplin was born in London in 1889 into extreme poverty, and spent part of his childhood in workhouses after his mother's mental illness left the family unable to support itself",
            "He began performing on stage as a child and joined a touring comedy troupe that brought him to the United States in 1910",
            "He created his iconic 'Tramp' character, with bowler hat, cane, and toothbrush mustache, in 1914, which became one of the most recognized figures in film history",
            "He wrote, directed, produced, and starred in most of his own films, an unusually high degree of creative control for the era",
            "His films, including The Kid (1921), The Gold Rush (1925), and Modern Times (1936), combined slapstick comedy with social commentary and emotional depth",
            "He was investigated by the FBI over suspected Communist sympathies during the Red Scare, and in 1952 was barred from re-entering the United States, living the rest of his life largely in Switzerland",
            "He received an honorary Academy Award in 1972 during a rare return visit to the United States, receiving a lengthy standing ovation",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="walt_disney", name="Walt Disney", years="1901-1966", nationality="American",
        field="animator and film producer", wiki_title="Walt Disney",
        significance="he pioneered advances in animation, produced Snow White and the Seven Dwarfs, the first full-length animated feature film, and built the Walt Disney Company into one of the world's largest entertainment companies",
        facts=[
            "Walt Disney was born in Chicago, Illinois, in 1901",
            "He co-founded the Disney Brothers Studio with his brother Roy in 1923",
            "He created the character Mickey Mouse in 1928, first appearing in the sound cartoon Steamboat Willie, one of the earliest cartoons with synchronized sound",
            "In 1937 he released Snow White and the Seven Dwarfs, the first full-length animated feature film produced in the United States, a major financial and technical risk that succeeded",
            "He won 22 competitive Academy Awards during his lifetime, more than any individual in history",
            "In 1955 he opened Disneyland in Anaheim, California, the first of what became a global chain of Disney theme parks",
            "He died in 1966, and the company he founded went on to become one of the largest media and entertainment conglomerates in the world",
        ], related_subjects=["World Cinema", "Business Studies"],
    ),
    dict(
        id="alfred_hitchcock", name="Alfred Hitchcock", years="1899-1980", nationality="British",
        field="film director", wiki_title="Alfred Hitchcock",
        significance="known as the 'Master of Suspense', his innovative techniques for building tension in films such as Psycho and Vertigo profoundly shaped the thriller genre and film directing more broadly",
        facts=[
            "Alfred Hitchcock was born in London in 1899, and began his film career in the British film industry in the 1920s",
            "He moved to Hollywood in 1939, where he directed many of his most famous films over the following decades",
            "His 1960 film Psycho, including its famous shower scene, became one of the most influential and analyzed sequences in film history",
            "He directed Vertigo (1958), which decades later was ranked by some critical polls as the greatest film ever made",
            "He pioneered techniques including the 'MacGuffin', a plot device used to motivate characters without needing significant explanation, and innovative uses of camera movement and editing to build suspense",
            "He hosted the television anthology series Alfred Hitchcock Presents from 1955 to 1965, introducing each episode with his distinctive dry wit",
            "Despite directing over 50 feature films across a five-decade career, he never won a competitive Academy Award for Best Director, though he received an honorary award in 1968",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="steven_spielberg", name="Steven Spielberg", years="1946-present", nationality="American",
        field="film director and producer", wiki_title="Steven Spielberg",
        significance="one of the most commercially successful and influential directors in film history, his films including Jaws, E.T., and Jurassic Park helped define the modern Hollywood blockbuster",
        facts=[
            "Steven Spielberg was born in Cincinnati, Ohio, in 1946, and began making amateur films with a home movie camera as a child",
            "His 1975 film Jaws is widely credited with establishing the modern template for the summer box office blockbuster",
            "His film E.T. the Extra-Terrestrial, released in 1982, became one of the highest-grossing films of its era and a defining family film of the 1980s",
            "He directed the Jurassic Park franchise beginning in 1993, which pioneered groundbreaking computer-generated visual effects for depicting dinosaurs",
            "He won the Academy Award for Best Director for Schindler's List (1993), a film about the Holocaust based on the true story of Oskar Schindler",
            "He co-founded the film studio DreamWorks Pictures in 1994 alongside Jeffrey Katzenberg and David Geffen",
            "He founded the USC Shoah Foundation in 1994 to record and preserve testimonies from Holocaust survivors, following his work on Schindler's List",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="marilyn_monroe", name="Marilyn Monroe", years="1926-1962", nationality="American",
        field="actress and model", wiki_title="Marilyn Monroe",
        significance="one of the most iconic film stars of the 1950s and 1960s, her performances in films such as Some Like It Hot and her public persona made her an enduring symbol of Hollywood glamour",
        facts=[
            "Marilyn Monroe was born Norma Jeane Mortenson in Los Angeles in 1926, and spent much of her childhood in foster homes and an orphanage",
            "She began modeling during World War II and signed her first film contract in 1946, adopting the stage name Marilyn Monroe",
            "Her comedic performance in Some Like It Hot (1959) is widely regarded as one of the finest comedic performances in film history",
            "She also starred in Gentlemen Prefer Blondes (1953) and The Seven Year Itch (1955), the latter featuring the famous scene of her dress billowing over a subway grate",
            "She founded her own production company, Marilyn Monroe Productions, in 1955, an unusually independent move for an actress at the time",
            "She struggled publicly with insomnia, anxiety, and dependence on prescription medication in her later years",
            "She died in 1962 at age 36 from a barbiturate overdose, ruled a probable suicide, an event that remains widely discussed and the subject of continued public interest",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="akira_kurosawa", name="Akira Kurosawa", years="1910-1998", nationality="Japanese",
        field="film director", wiki_title="Akira Kurosawa",
        significance="widely regarded as one of the most influential filmmakers in cinema history, his films such as Seven Samurai and Rashomon introduced innovative narrative and visual techniques that shaped filmmakers worldwide",
        facts=[
            "Akira Kurosawa was born in Tokyo, Japan, in 1910",
            "His 1950 film Rashomon, which told the same story from multiple conflicting perspectives, won the Golden Lion at the Venice Film Festival and introduced Japanese cinema to a wide international audience",
            "The narrative technique of presenting contradictory accounts of the same event is now commonly referred to as the 'Rashomon effect'",
            "His 1954 film Seven Samurai, about villagers hiring samurai to defend against bandits, has influenced countless later films, including its direct American remake, The Magnificent Seven (1960)",
            "He worked closely for decades with actor Toshiro Mifune, who starred in many of his most celebrated films",
            "His visual style, including his innovative use of multiple cameras and weather elements like rain and wind, significantly influenced later filmmakers including George Lucas and Steven Spielberg",
            "He continued directing into his eighties, and received an honorary Academy Award in 1990 recognizing his lifetime achievement",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="oprah_placeholder_removed_ent", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "oprah_placeholder_removed_ent"]

PEOPLE += [
    dict(
        id="audrey_hepburn", name="Audrey Hepburn", years="1929-1993", nationality="British",
        field="actress and humanitarian", wiki_title="Audrey Hepburn",
        significance="a celebrated film actress known for roles in Roman Holiday and Breakfast at Tiffany's, she later devoted much of her life to humanitarian work as a UNICEF Goodwill Ambassador",
        facts=[
            "Audrey Hepburn was born in Brussels, Belgium, in 1929, and spent part of her childhood in the Netherlands during the German occupation in World War II, a period of significant hardship and malnutrition",
            "She trained as a ballet dancer before turning to acting, appearing first in British and European films",
            "She won the Academy Award for Best Actress for her role in Roman Holiday (1953), her first major American film",
            "She starred in Breakfast at Tiffany's (1961), one of her most iconic roles, and My Fair Lady (1964)",
            "She is one of a small number of performers to have won an Emmy, a Grammy, an Oscar, and a Tony award, sometimes described as achieving 'EGOT' status",
            "From 1988 until her death, she served as a Goodwill Ambassador for UNICEF, traveling to some of the most impoverished regions of the world to draw attention to children's needs",
            "She was posthumously awarded the Presidential Medal of Freedom in 1992 for her humanitarian work",
        ], related_subjects=["World Cinema", "Civics"],
    ),
    dict(
        id="satyajit_ray", name="Satyajit Ray", years="1921-1992", nationality="Indian (Bengali)",
        field="film director and writer", wiki_title="Satyajit Ray",
        significance="widely regarded as one of the greatest filmmakers of the 20th century, his Apu Trilogy brought international critical acclaim to Indian and Bengali cinema",
        facts=[
            "Satyajit Ray was born in Calcutta in 1921, into a Bengali family with a strong literary and artistic background",
            "His debut film, Pather Panchali (1955), the first installment of what became known as the Apu Trilogy, won a special award at the Cannes Film Festival",
            "The Apu Trilogy, completed with Aparajito (1956) and Apur Sansar (1959), follows a Bengali boy's life from childhood to adulthood, and is widely regarded as one of the great achievements in world cinema",
            "He wrote, directed, and often composed the music for his own films, and also designed typefaces and wrote popular fiction, including detective stories",
            "He directed 36 films over his career, spanning a wide range of genres, while remaining based primarily in Kolkata rather than relocating to a larger film industry hub",
            "In 1992, shortly before his death, he received an honorary Academy Award for lifetime achievement, presented to him in Kolkata due to his failing health",
            "He died in 1992, and remains widely regarded as the most internationally celebrated filmmaker in the history of Indian cinema",
        ], related_subjects=["World Cinema", "World Literature"],
    ),
    dict(
        id="charlie_parker", name="Charlie Parker", years="1920-1955", nationality="American",
        field="jazz saxophonist and composer", wiki_title="Charlie Parker",
        significance="a pioneering figure of bebop jazz, his innovative saxophone improvisation transformed jazz music in the 1940s and influenced generations of musicians across genres",
        facts=[
            "Charlie Parker was born in Kansas City, Kansas, in 1920, and grew up in Kansas City, Missouri, a major jazz hub of the era",
            "He began developing a new, harmonically complex style of jazz improvisation in the early 1940s, playing in small New York clubs alongside musicians like Dizzy Gillespie",
            "This new style, known as bebop, moved jazz away from big-band dance music toward a faster, more improvisational and musically complex form intended for close listening",
            "He was known for extraordinarily fast and inventive saxophone improvisation, earning him the nickname 'Bird'",
            "He struggled with heroin addiction for much of his adult life, which significantly affected his health and career",
            "The famous jazz club Birdland in New York City was named in his honor in 1949",
            "He died in 1955 at age 34, and remains one of the most influential and studied musicians in the history of jazz",
        ], related_subjects=["Music"],
    ),
    dict(
        id="meryl_streep", name="Meryl Streep", years="1949-present", nationality="American",
        field="actress", wiki_title="Meryl Streep",
        significance="widely regarded as one of the greatest film actors of her generation, she holds the record for the most Academy Award nominations for acting in history",
        facts=[
            "Meryl Streep was born in Summit, New Jersey, in 1949, and trained at the Yale School of Drama before beginning a stage and film career",
            "She has received more Academy Award nominations for acting than any other performer in history, with over 20 nominations as of the mid-2020s",
            "She has won three competitive Academy Awards, for Kramer vs. Kramer (1979), Sophie's Choice (1982), and The Iron Lady (2011)",
            "She is known for her ability to convincingly portray a wide range of accents and nationalities across her many roles",
            "Her performance as fashion editor Miranda Priestly in The Devil Wears Prada (2006) became one of her most widely recognized roles with a broad popular audience",
            "President Barack Obama awarded her the Presidential Medal of Freedom in 2014",
            "She continues to work regularly in film and television well into her seventies, maintaining one of the longest sustained leading careers in Hollywood history",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="michael_jackson", name="Michael Jackson", years="1958-2009", nationality="American",
        field="singer, songwriter, and dancer", wiki_title="Michael Jackson",
        significance="known as the 'King of Pop', his album Thriller remains the best-selling album of all time, and his innovative music videos and dance style transformed popular music and entertainment",
        facts=[
            "Michael Jackson was born in Gary, Indiana, in 1958, and began performing as a young child with his brothers in the Jackson 5",
            "He launched a solo career alongside his group work, and his 1979 album Off the Wall established him as a major solo artist",
            "His 1982 album Thriller became the best-selling album of all time, with estimated sales of over 70 million copies worldwide",
            "The music video for the title track 'Thriller', released in 1983, was groundbreaking in length, choreography, and production, and helped establish MTV-era music videos as a major art form",
            "He pioneered dance moves including the moonwalk, which he first performed publicly during a 1983 television special",
            "He won a record 13 Grammy Awards over his career and was inducted into the Rock and Roll Hall of Fame twice, once as a solo artist and once with the Jackson 5",
            "He died in 2009, and his career and personal life, including serious legal allegations against him, remain the subject of extensive ongoing public discussion and reassessment",
        ], related_subjects=["Music"],
    ),
    dict(
        id="charlie_chaplin_ref_removed_dup", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "charlie_chaplin_ref_removed_dup"]

PEOPLE += [
    dict(
        id="hayao_miyazaki", name="Hayao Miyazaki", years="1941-present", nationality="Japanese",
        field="animator and film director", wiki_title="Hayao Miyazaki",
        significance="co-founder of Studio Ghibli, his hand-drawn animated films, including Spirited Away, are widely regarded among the greatest animated films ever made and have earned major international acclaim for Japanese animation",
        facts=[
            "Hayao Miyazaki was born in Tokyo, Japan, in 1941, during World War II, and his family's aircraft parts factory shaped some of his lifelong fascination with flight, a recurring theme in his films",
            "He began his animation career at Toei Animation in the early 1960s before eventually co-founding Studio Ghibli in 1985 with producer Toshio Suzuki and fellow director Isao Takahata",
            "His films often feature strong, independent female protagonists and deal thoughtfully with environmental and antiwar themes",
            "His 2001 film Spirited Away won the Academy Award for Best Animated Feature in 2003, the first hand-drawn and non-English-language film to do so",
            "Spirited Away also became, at the time of its release, the highest-grossing film in Japanese history",
            "He announced retirement from feature filmmaking multiple times over his career before returning with new projects, including The Boy and the Heron (2023), which also won the Academy Award for Best Animated Feature",
            "He is widely regarded as one of the most influential animation directors in film history, admired for his intricate hand-drawn visual style even as the industry moved toward computer animation",
        ], related_subjects=["World Cinema", "Art"],
    ),
    dict(
        id="stan_lee", name="Stan Lee", years="1922-2018", nationality="American",
        field="comic book writer and editor", wiki_title="Stan Lee",
        significance="as the primary writer and editorial force behind Marvel Comics starting in the early 1960s, he co-created iconic characters including Spider-Man, the X-Men, and the Fantastic Four, reshaping the American comic book industry",
        facts=[
            "Stan Lee was born Stanley Lieber in New York City in 1922, and began working at Timely Comics, later Marvel Comics, as a teenager in 1939",
            "Beginning in the early 1960s, working closely with artists Jack Kirby and Steve Ditko, he co-created many of Marvel's most enduring characters, including Spider-Man, the Fantastic Four, the X-Men, the Hulk, and Iron Man",
            "He pioneered a style of superhero storytelling that emphasized flawed, relatable human characters facing real personal struggles, alongside their superhero adventures, a significant departure from earlier comic conventions",
            "He served as editor-in-chief and later publisher of Marvel Comics for decades, shaping the company's overall creative direction",
            "In later years, questions arose about how much creative credit Lee versus his artistic collaborators, especially Jack Kirby, deserved for co-creating specific characters, a debate that continues among comic historians",
            "He made numerous cameo appearances in Marvel superhero films beginning in the late 1990s and continuing through the Marvel Cinematic Universe films, which became a beloved tradition among fans",
            "He died in 2018, having lived to see the characters he helped create become the basis for one of the most commercially successful film franchises in history",
        ], related_subjects=["World Cinema", "World Literature"],
    ),
    dict(
        id="elvis_presley", name="Elvis Presley", years="1935-1977", nationality="American",
        field="singer and musician", wiki_title="Elvis Presley",
        significance="known as the 'King of Rock and Roll', he became one of the most commercially successful and culturally significant musicians of the 20th century, helping bring rock and roll music into the mainstream",
        facts=[
            "Elvis Presley was born in Tupelo, Mississippi, in 1935, and grew up in a poor family that later moved to Memphis, Tennessee",
            "He recorded his first commercial singles at Sun Records in Memphis in 1954, blending country, blues, and gospel influences into an energetic new style",
            "His 1956 single 'Heartbreak Hotel' became his first number-one hit and helped launch him to national fame",
            "His energetic performing style, including his distinctive hip movements, drew significant controversy on American television in the mid-1950s, with some broadcasts deliberately filming him only from the waist up",
            "He served in the US Army from 1958 to 1960, a period during which he continued to be closely followed by fans and the press",
            "He became one of the best-selling solo music artists in history, with estimated sales exceeding 500 million records worldwide",
            "He died at his home, Graceland, in Memphis, in 1977, and Graceland remains one of the most visited private residences in the United States, drawing hundreds of thousands of visitors annually",
        ], related_subjects=["Music"],
    ),
    dict(
        id="ingmar_bergman", name="Ingmar Bergman", years="1918-2007", nationality="Swedish",
        field="film director", wiki_title="Ingmar Bergman",
        significance="widely regarded as one of the greatest filmmakers in cinema history, his films, including The Seventh Seal and Wild Strawberries, explored profound questions of faith, mortality, and human relationships with distinctive visual and psychological depth",
        facts=[
            "Ingmar Bergman was born in Uppsala, Sweden, in 1918, the son of a Lutheran minister, an upbringing that deeply informed the religious themes in his later films",
            "He directed over 60 films across a career spanning more than five decades, along with extensive work in theater",
            "His 1957 film The Seventh Seal, featuring a medieval knight playing chess with the personification of Death, became one of the most iconic and widely referenced images in film history",
            "His films frequently explored questions of religious faith, mortality, and complex human psychology, often through close, intense character studies",
            "He worked repeatedly with a consistent group of actors, including Max von Sydow, Liv Ullmann, and Bibi Andersson, across many of his most celebrated films",
            "He won three Academy Awards for Best Foreign Language Film, for The Virgin Spring (1960), Through a Glass Darkly (1961), and Fanny and Alexander (1982)",
            "He died in 2007, and is widely regarded, alongside directors like Akira Kurosawa and Federico Fellini, as one of the most influential filmmakers in the history of world cinema",
        ], related_subjects=["World Cinema"],
    ),
    dict(
        id="whitney_houston", name="Whitney Houston", years="1963-2012", nationality="American",
        field="singer and actress", wiki_title="Whitney Houston",
        significance="widely regarded as one of the greatest vocalists in popular music history, she sold over 200 million records worldwide, and her rendition of 'I Will Always Love You' became one of the best-selling singles of all time",
        facts=[
            "Whitney Houston was born in Newark, New Jersey, in 1963, into a musical family, with her mother Cissy Houston a noted gospel and backing vocalist",
            "Her 1985 self-titled debut album became one of the best-selling debut albums by a female artist at the time",
            "She holds the Guinness World Record for the most consecutive number-one hits by a solo artist on the Billboard Hot 100, with seven consecutive chart-topping singles",
            "Her 1992 rendition of 'I Will Always Love You', recorded for the film The Bodyguard in which she also starred, became one of the best-selling singles in music history",
            "She won a total of six Grammy Awards over her career, along with numerous other major music industry honors",
            "She struggled publicly with substance abuse issues later in her career, which affected both her health and her public image",
            "She died in 2012 at age 48, and remains widely regarded as one of the most vocally gifted singers in the history of popular music",
        ], related_subjects=["Music"],
    ),
    dict(
        id="charlie_chaplin_ref2_removed", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "charlie_chaplin_ref2_removed"]

PEOPLE += [
    dict(
        id="bruce_lee", name="Bruce Lee", years="1940-1973", nationality="American (Hong Kong)",
        field="martial artist and actor", wiki_title="Bruce Lee",
        significance="a martial artist and film star whose combination of philosophy, physical skill, and screen charisma transformed global perceptions of martial arts and made him one of the most influential action film stars in history",
        facts=[
            "Bruce Lee was born in San Francisco, California, in 1940, while his father, a Cantonese opera performer, was touring the United States, and Lee was raised largely in Hong Kong",
            "He studied Wing Chun kung fu in Hong Kong before returning to the United States as a young man, where he began teaching martial arts",
            "He developed his own martial arts philosophy and style, Jeet Kune Do, emphasizing practicality, adaptability, and the rejection of rigid traditional forms",
            "He gained American television recognition playing Kato in the series The Green Hornet in the late 1960s",
            "He starred in a series of martial arts films produced in Hong Kong in the early 1970s, including Fist of Fury and Way of the Dragon, which became major box office successes across Asia",
            "His film Enter the Dragon, a US-Hong Kong co-production released in 1973, became a major international hit and helped popularize martial arts films with Western audiences",
            "He died suddenly in Hong Kong in 1973 at age 32, shortly before Enter the Dragon's release, from a reaction to medication, and remains one of the most influential figures in martial arts and action cinema history",
        ], related_subjects=["World Cinema", "Physical Education & Self-Defense"],
    ),
    dict(
        id="quentin_tarantino", name="Quentin Tarantino", years="1963-present", nationality="American",
        field="film director", wiki_title="Quentin Tarantino",
        significance="his distinctive nonlinear storytelling, stylized violence, and genre-blending films, including Pulp Fiction, helped define independent American cinema in the 1990s and beyond",
        facts=[
            "Quentin Tarantino was born in Knoxville, Tennessee, in 1963, and worked for years at a video rental store in Los Angeles, where he developed an encyclopedic knowledge of film",
            "His 1992 debut feature Reservoir Dogs, made on a modest budget, gained significant attention on the independent film festival circuit",
            "His 1994 film Pulp Fiction, known for its nonlinear narrative structure and sharp, stylized dialogue, won the Palme d'Or at the Cannes Film Festival and the Academy Award for Best Original Screenplay",
            "His films are known for blending and paying homage to multiple genres, including crime, martial arts, and exploitation cinema, drawing on his deep knowledge of film history",
            "He has stated a plan to retire after directing ten feature films, a self-imposed limit intended to preserve the overall quality and consistency of his body of work",
            "His frequent collaborators have included actors Samuel L. Jackson and Uma Thurman, appearing across multiple of his films",
            "He has won two Academy Awards for Best Original Screenplay, for Pulp Fiction and later Django Unchained (2012)",
        ], related_subjects=["World Cinema"],
    ),
]


def main() -> None:
    upsert_section(
        "film_media_entertainment",
        "Film, Media & Entertainment",
        "🎬",
        "Directors, actors, and performers whose work in film, television, and music entertained and influenced audiences worldwide.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
