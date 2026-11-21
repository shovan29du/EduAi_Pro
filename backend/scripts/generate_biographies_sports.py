#!/usr/bin/env python3
"""Populate the "Sports & Athletics" biography category with real,
verified athletes. See _biography_engine.py for the no-fabrication
template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_sports.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="muhammad_ali", name="Muhammad Ali", years="1942-2016", nationality="American",
        field="boxer", wiki_title="Muhammad Ali",
        significance="a three-time world heavyweight boxing champion known for his speed and showmanship, he also became a prominent figure in the civil rights movement and a symbol of principled resistance",
        facts=[
            "Muhammad Ali was born Cassius Clay in Louisville, Kentucky, in 1942",
            "He won a gold medal in boxing at the 1960 Rome Olympics before turning professional",
            "He won the world heavyweight title for the first time in 1964 by defeating Sonny Liston, and shortly after announced his conversion to Islam and name change",
            "In 1967 he refused induction into the US military during the Vietnam War on religious grounds, and was stripped of his boxing titles and banned from the sport for over three years",
            "The US Supreme Court unanimously overturned his conviction for draft evasion in 1971",
            "He regained the heavyweight title in the famous 1974 'Rumble in the Jungle' fight against George Foreman in Kinshasa, Zaire",
            "He was diagnosed with Parkinson's syndrome in 1984, and lit the Olympic cauldron at the 1996 Atlanta Olympics despite his declining health",
        ], related_subjects=["Physical Education & Self-Defense", "Civics"],
    ),
    dict(
        id="serena_williams", name="Serena Williams", years="1981-present", nationality="American",
        field="tennis player", wiki_title="Serena Williams",
        significance="widely regarded as one of the greatest tennis players in history, she won 23 Grand Slam singles titles, the most of any player in the Open Era",
        facts=[
            "Serena Williams was born in Saginaw, Michigan, in 1981, and began playing tennis as a young child coached by her father, Richard Williams",
            "She turned professional in 1995 alongside her older sister Venus Williams, and the two became one of the most successful sibling pairs in sports history",
            "She won her first Grand Slam singles title at the 1999 US Open at age 17",
            "She achieved the 'Serena Slam', holding all four Grand Slam singles titles simultaneously, on two separate occasions, in 2002-2003 and 2014-2015",
            "She won 23 Grand Slam singles titles over her career, the most of any player, male or female, in the Open Era of tennis",
            "She won a singles Grand Slam title in 2017 while pregnant with her daughter, later revealed publicly after the tournament",
            "She retired from professional tennis in 2022, and has since been active in business investing through her venture capital firm",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="michael_jordan", name="Michael Jordan", years="1963-present", nationality="American",
        field="basketball player", wiki_title="Michael Jordan",
        significance="widely regarded as one of the greatest basketball players of all time, he led the Chicago Bulls to six NBA championships and became a global icon of the sport",
        facts=[
            "Michael Jordan was born in Brooklyn, New York, in 1963, and grew up in Wilmington, North Carolina",
            "He famously did not make his high school varsity basketball team as a sophomore, an experience often cited as motivating his relentless competitiveness",
            "He was drafted by the Chicago Bulls in 1984 and won the NBA Rookie of the Year award that season",
            "He led the Chicago Bulls to six NBA championships in the 1990s, winning the NBA Finals MVP award in all six of those finals",
            "He won five regular-season MVP awards over his career and was named an NBA All-Star 14 times",
            "His signature Air Jordan sneaker line with Nike, launched in 1985, became one of the most commercially successful athletic shoe brands in history",
            "He retired from professional basketball for the final time in 2003, and later became majority owner of the Charlotte Hornets NBA franchise",
        ], related_subjects=["Physical Education & Self-Defense", "Business Studies"],
    ),
    dict(
        id="pele", name="Pele", years="1940-2022", nationality="Brazilian",
        field="footballer (soccer player)", wiki_title="Pele",
        significance="widely regarded as one of the greatest footballers in history, he won three FIFA World Cups with Brazil, the only player ever to do so",
        facts=[
            "Pele was born Edson Arantes do Nascimento in Tres Coracoes, Brazil, in 1940",
            "He made his professional debut for the Santos club at age 15 and his debut for the Brazilian national team at age 16",
            "He helped Brazil win the FIFA World Cup in 1958 at age 17, becoming the youngest player to win a World Cup",
            "He went on to win the World Cup with Brazil two more times, in 1962 and 1970, making him the only player to win three World Cup titles",
            "He scored an estimated 1,281 goals over his career according to some counts, though methods of counting exhibition matches vary among historians",
            "He joined the New York Cosmos of the North American Soccer League in 1975, helping raise the profile of soccer in the United States",
            "He died in 2022, and was widely mourned across the football world as one of the sport's greatest ever players",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="usain_bolt", name="Usain Bolt", years="1986-present", nationality="Jamaican",
        field="sprinter", wiki_title="Usain Bolt",
        significance="he set world records in the 100m and 200m sprints that still stood as of the mid-2020s, and won eight Olympic gold medals, earning him recognition as the fastest human ever recorded",
        facts=[
            "Usain Bolt was born in Sherwood Content, Jamaica, in 1986",
            "He set the world junior record in the 200m at age 15, drawing early international attention",
            "At the 2008 Beijing Olympics he won gold in the 100m, 200m, and 4x100m relay, setting world records in the process",
            "His 100m world record of 9.58 seconds, set at the 2009 World Championships in Berlin, still stood as of the mid-2020s",
            "He won gold in the 100m, 200m, and 4x100m relay at three consecutive Olympic Games (2008, 2012, and 2016), earning the nickname 'triple triple'",
            "He is known for his celebratory 'lightning bolt' pose, which became one of the most recognizable gestures in world sports",
            "He retired from professional athletics in 2017 and has since pursued interests including business ventures and, briefly, professional football trials",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="simone_biles", name="Simone Biles", years="1997-present", nationality="American",
        field="gymnast", wiki_title="Simone Biles",
        significance="widely regarded as one of the greatest gymnasts of all time, she has won more world championship medals than any gymnast in history and has had four separate skills named after her",
        facts=[
            "Simone Biles was born in Columbus, Ohio, in 1997, and was raised primarily by her grandparents after being in foster care as a young child",
            "She won four gold medals and one bronze at the 2016 Rio Olympics",
            "As of the mid-2020s she holds the record for the most world championship medals won by any gymnast, male or female",
            "Four separate gymnastics skills across different apparatus have been named 'the Biles' after she was the first to successfully perform them in competition",
            "At the 2020 Tokyo Olympics (held in 2021), she withdrew from several events citing a mental health issue called 'the twisties', drawing wide public attention to athlete mental health",
            "She returned to elite competition and won further medals, including additional Olympic golds at the 2024 Paris Olympics",
            "She has been outspoken about the abuse scandal involving USA Gymnastics team doctor Larry Nassar, and testified before the US Senate about the organizations' handling of the case",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="jesse_owens", name="Jesse Owens", years="1913-1980", nationality="American",
        field="track and field athlete", wiki_title="Jesse Owens",
        significance="he won four gold medals at the 1936 Berlin Olympics, directly undermining Nazi Germany's promotion of the games as a showcase for Aryan racial supremacy",
        facts=[
            "Jesse Owens was born in Oakville, Alabama, in 1913, the son of a sharecropper and grandson of enslaved people",
            "He set three world records and tied a fourth in a span of about 45 minutes at a college track meet in Michigan in 1935, a performance often called one of the greatest in sports history",
            "At the 1936 Berlin Olympics, held under Nazi Germany, he won four gold medals in the 100m, 200m, long jump, and 4x100m relay",
            "His victories directly contradicted Nazi propaganda promoting the idea of Aryan racial superiority, in front of Adolf Hitler and a large German audience",
            "Despite his Olympic success, he faced ongoing racial segregation and discrimination upon returning to the United States, including being unable to secure well-paying sponsorship deals available to white athletes",
            "He was not invited to the White House by President Franklin Roosevelt after his Olympic victories, an omission widely noted by historians",
            "In 1976 President Gerald Ford awarded him the Presidential Medal of Freedom",
        ], related_subjects=["Physical Education & Self-Defense", "Civics"],
    ),
    dict(
        id="diego_maradona", name="Diego Maradona", years="1960-2020", nationality="Argentine",
        field="footballer (soccer player)", wiki_title="Diego Maradona",
        significance="widely regarded as one of the greatest footballers of all time, he led Argentina to victory in the 1986 FIFA World Cup, scoring two of the tournament's most famous goals in a single match",
        facts=[
            "Diego Maradona was born in Lanus, Argentina, in 1960, and grew up in poverty in a shantytown outside Buenos Aires",
            "He made his professional football debut at age 15 for Argentinos Juniors",
            "He captained Argentina to victory at the 1986 FIFA World Cup, scoring the controversial 'Hand of God' goal and the celebrated 'Goal of the Century' in the same quarter-final match against England",
            "He played for Napoli in Italy's Serie A from 1984 to 1991, leading the club to its only two league titles in its history",
            "He struggled publicly with cocaine addiction for much of his career, which contributed to bans and disruptions to his playing career",
            "He later managed the Argentine national team, including at the 2010 World Cup",
            "He died in 2020, and his death prompted three days of national mourning declared by the Argentine government",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="babe_ruth", name="Babe Ruth", years="1895-1948", nationality="American",
        field="baseball player", wiki_title="Babe Ruth",
        significance="widely regarded as one of the greatest baseball players ever, his prolific home-run hitting for the New York Yankees helped transform baseball into America's national pastime during the 1920s",
        facts=[
            "Babe Ruth was born George Herman Ruth Jr. in Baltimore, Maryland, in 1895, and spent much of his childhood at a reform school for troubled boys",
            "He began his professional career as a pitcher for the Boston Red Sox before being sold to the New York Yankees in 1919, a transaction later nicknamed 'the Curse of the Bambino' by Red Sox fans",
            "As a Yankee, he transitioned to a full-time hitter, and his prolific home-run totals helped popularize the long ball as a central part of baseball strategy",
            "He hit 60 home runs in the 1927 season, a single-season record that stood for 34 years until broken by Roger Maris in 1961",
            "He finished his career with 714 home runs, a record that stood for nearly 40 years until Hank Aaron surpassed it in 1974",
            "He was one of the first five players inducted into the Baseball Hall of Fame in 1936",
            "He died in 1948, and remains one of the most recognized figures in American sports history",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="billie_jean_king", name="Billie Jean King", years="1943-present", nationality="American",
        field="tennis player", wiki_title="Billie Jean King",
        significance="a champion tennis player who won 39 Grand Slam titles, she became a leading advocate for gender equality in sports, most famously by defeating Bobby Riggs in the 1973 'Battle of the Sexes' match",
        facts=[
            "Billie Jean King was born in Long Beach, California, in 1943",
            "She won 39 Grand Slam titles across singles, doubles, and mixed doubles over her career",
            "In 1973 she played former men's champion Bobby Riggs in a widely publicized exhibition match dubbed the 'Battle of the Sexes', which she won in straight sets in front of a record tennis audience",
            "That same year, she threatened to boycott the US Open unless it offered equal prize money for men and women, and the tournament became the first Grand Slam to do so",
            "She founded the Women's Tennis Association (WTA) in 1973 to represent professional female tennis players",
            "She publicly came out as gay in 1981, one of the first prominent professional athletes to do so, at a time when it cost her significant sponsorship income",
            "The USTA National Tennis Center in New York, home of the US Open, was renamed the Billie Jean King National Tennis Center in 2006 in her honor",
        ], related_subjects=["Physical Education & Self-Defense", "Civics"],
    ),
    dict(
        id="michael_phelps", name="Michael Phelps", years="1985-present", nationality="American",
        field="swimmer", wiki_title="Michael Phelps",
        significance="the most decorated Olympian in history, he won 28 Olympic medals, including 23 gold medals, across four consecutive Olympic Games",
        facts=[
            "Michael Phelps was born in Baltimore, Maryland, in 1985, and began swimming competitively as a child partly to help manage his ADHD",
            "He qualified for his first Olympics at age 15, at the 2000 Sydney Games, though he did not medal",
            "At the 2008 Beijing Olympics he won eight gold medals in a single Games, the most ever won by an athlete at one Olympics",
            "Over his Olympic career, spanning the 2004, 2008, 2012, and 2016 Games, he won 28 total medals, 23 of them gold, both records unmatched by any other Olympian",
            "He set numerous individual and relay world records in events including the 200m butterfly and 400m individual medley",
            "He has spoken openly about his struggles with depression and mental health following his competitive career, becoming an advocate for athlete mental health awareness",
            "He retired from competitive swimming after the 2016 Rio Olympics",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="lionel_messi", name="Lionel Messi", years="1987-present", nationality="Argentine",
        field="footballer (soccer player)", wiki_title="Lionel Messi",
        significance="widely regarded as one of the greatest footballers of all time, he has won a record eight Ballon d'Or awards and led Argentina to victory in the 2022 FIFA World Cup",
        facts=[
            "Lionel Messi was born in Rosario, Argentina, in 1987, and moved to Spain as a child to join FC Barcelona's youth academy after the club agreed to cover treatment for a growth hormone deficiency",
            "He made his first-team debut for Barcelona in 2004 and went on to spend 17 seasons with the club, becoming its all-time leading scorer",
            "He has won the Ballon d'Or, awarded to the world's best player, a record eight times as of the mid-2020s",
            "He won the Copa America with Argentina in 2021, his first major international title with the senior national team after several previous final losses",
            "He captained Argentina to victory at the 2022 FIFA World Cup in Qatar, widely regarded as one of the greatest World Cup finals ever played",
            "He moved to Paris Saint-Germain in 2021 after leaving Barcelona due to the club's financial constraints, before later joining Inter Miami in Major League Soccer in 2023",
            "His move to Inter Miami significantly boosted the profile and attendance of Major League Soccer in the United States",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="jackie_robinson", name="Jackie Robinson", years="1919-1972", nationality="American",
        field="baseball player", wiki_title="Jackie Robinson",
        significance="in 1947 he became the first African American to play in Major League Baseball in the modern era, breaking the sport's color barrier and becoming a pivotal figure in the civil rights movement",
        facts=[
            "Jackie Robinson was born in Cairo, Georgia, in 1919, and grew up largely in Pasadena, California",
            "He was a standout athlete at UCLA, competing in football, basketball, track, and baseball",
            "He served as a US Army officer during World War II, and was court-martialed, though ultimately acquitted, after refusing to move to the back of a segregated military bus",
            "In 1947 he signed with the Brooklyn Dodgers, becoming the first African American to play Major League Baseball in the modern era",
            "He endured significant racist abuse from fans, opposing players, and even some teammates during his early seasons, which Dodgers executive Branch Rickey had asked him to endure without retaliating",
            "He won the inaugural Major League Baseball Rookie of the Year award in 1947 and the National League MVP award in 1949",
            "Major League Baseball retired his uniform number, 42, across all teams in 1997, the only number universally retired throughout the league",
        ], related_subjects=["Physical Education & Self-Defense", "Civics"],
    ),
    dict(
        id="cristiano_ronaldo", name="Cristiano Ronaldo", years="1985-present", nationality="Portuguese",
        field="footballer (soccer player)", wiki_title="Cristiano Ronaldo",
        significance="one of the most prolific goal scorers in football history, he has won five Ballon d'Or awards and is, as of the mid-2020s, the all-time leading scorer in men's international football",
        facts=[
            "Cristiano Ronaldo was born on the island of Madeira, Portugal, in 1985",
            "He joined Manchester United's youth system in 2003 and quickly became one of the most exciting young talents in English football",
            "He moved to Real Madrid in 2009 for a then-world-record transfer fee, and became the club's all-time leading scorer",
            "He has won five Ballon d'Or awards, given annually to the world's best player, as of the mid-2020s",
            "He captained Portugal to victory at the UEFA European Championship in 2016, the country's first major international trophy",
            "As of the mid-2020s he holds the record for most goals scored in men's international football history, playing for Portugal",
            "He moved to Saudi Arabian club Al Nassr in 2023, a transfer that drew significant global attention to Saudi Arabia's growing football league",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="wilma_rudolph", name="Wilma Rudolph", years="1940-1994", nationality="American",
        field="sprinter", wiki_title="Wilma Rudolph",
        significance="after overcoming childhood polio that left her unable to walk without leg braces until age twelve, she became the first American woman to win three gold medals in track and field at a single Olympics",
        facts=[
            "Wilma Rudolph was born prematurely in Saint Bethlehem, Tennessee, in 1940, the 20th of 22 children",
            "She contracted polio as a young child, which left her with a paralyzed and weakened left leg requiring a brace until about age twelve",
            "She overcame this early physical disability through physical therapy and family support, and began competing in basketball and track in high school",
            "She won a bronze medal at the 1956 Melbourne Olympics as a 16-year-old, her first Olympic appearance",
            "At the 1960 Rome Olympics she won three gold medals, in the 100m, 200m, and 4x100m relay, becoming the first American woman to achieve that feat at a single Olympics",
            "Her success drew significant international media attention and made her one of the most celebrated American athletes of the era",
            "She later became a teacher and coach, and founded the Wilma Rudolph Foundation to support young athletes",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="tiger_woods", name="Tiger Woods", years="1975-present", nationality="American",
        field="golfer", wiki_title="Tiger Woods",
        significance="widely regarded as one of the greatest golfers of all time, he won 15 major championships and dramatically increased golf's global popularity and prize money during his career",
        facts=[
            "Tiger Woods was born in Cypress, California, in 1975, and began playing golf under his father's guidance before age two",
            "He won three consecutive US Junior Amateur titles and three consecutive US Amateur titles before turning professional in 1996",
            "He won the 1997 Masters Tournament by a record 12 strokes at age 21, his first major championship as a professional",
            "In 2000-2001 he held all four major golf championship titles simultaneously, an achievement dubbed the 'Tiger Slam'",
            "He has won 15 major championships over his career, second only to Jack Nicklaus's record of 18",
            "He survived a severe single-car accident in 2021 that badly injured his right leg, raising doubts about whether he would play competitively again",
            "He returned to competitive golf following extensive surgery and rehabilitation, and remains one of the most commercially significant figures in the sport's history",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="martina_navratilova", name="Martina Navratilova", years="1956-present", nationality="Czech-American",
        field="tennis player", wiki_title="Martina Navratilova",
        significance="widely regarded as one of the greatest tennis players in history, she won 18 Grand Slam singles titles and a record 31 Grand Slam women's doubles titles",
        facts=[
            "Martina Navratilova was born in Prague, Czechoslovakia, in 1956, and began playing tennis as a young child",
            "She defected from Communist Czechoslovakia to the United States in 1975, seeking greater freedom to pursue her tennis career, and became a US citizen in 1981",
            "She won 18 Grand Slam singles titles and a record 31 Grand Slam women's doubles titles over her career",
            "Her rivalry with American player Chris Evert, spanning the late 1970s and 1980s, became one of the most celebrated rivalries in tennis history",
            "She held the world number one ranking for a combined total of over 330 weeks across her career",
            "She publicly came out as bisexual, and later identified as lesbian, in 1981, becoming one of the first prominent professional athletes to do so",
            "She continued competing at a high level well into her 40s, winning a mixed doubles Grand Slam title at the 2006 US Open at age 49",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="roger_federer", name="Roger Federer", years="1981-present", nationality="Swiss",
        field="tennis player", wiki_title="Roger Federer",
        significance="widely regarded as one of the greatest tennis players in history, he won 20 Grand Slam singles titles and held the world number one ranking for a record total of 310 weeks",
        facts=[
            "Roger Federer was born in Basel, Switzerland, in 1981",
            "He turned professional in 1998 and won his first Grand Slam singles title at Wimbledon in 2003",
            "He won 20 Grand Slam singles titles over his career, including a record eight Wimbledon titles",
            "He held the ATP world number one ranking for a record total of 310 weeks, including 237 consecutive weeks from 2004 to 2008",
            "His rivalries with Rafael Nadal and Novak Djokovic became among the most celebrated in the history of men's tennis",
            "He was widely praised throughout his career for his fluid, elegant playing style and sportsmanship both on and off the court",
            "He retired from professional tennis in 2022, playing his final match as part of a doubles pairing with longtime rival Rafael Nadal",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="wayne_gretzky", name="Wayne Gretzky", years="1961-present", nationality="Canadian",
        field="ice hockey player", wiki_title="Wayne Gretzky",
        significance="widely regarded as the greatest ice hockey player of all time and nicknamed 'the Great One', he holds numerous NHL scoring records that remain unbroken decades after his retirement",
        facts=[
            "Wayne Gretzky was born in Brantford, Ontario, Canada, in 1961, and began playing organized hockey at age six, quickly showing exceptional talent",
            "He joined the Edmonton Oilers of the National Hockey League in 1979 and led the team to four Stanley Cup championships in the 1980s",
            "He set numerous NHL scoring records, including most career goals, assists, and total points, several of which remain unbroken decades later",
            "His 1988 trade from the Edmonton Oilers to the Los Angeles Kings, sometimes called 'the Trade', was a landmark moment credited with significantly boosting hockey's popularity in the United States",
            "He won the Hart Trophy, awarded to the NHL's most valuable player, nine times over his career",
            "He retired in 1999, and the NHL immediately retired his jersey number, 99, league-wide, an honor given to no other player",
            "He later worked as a head coach and executive in professional hockey following his playing career",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="babe_didrikson_zaharias", name="Babe Didrikson Zaharias", years="1911-1956", nationality="American",
        field="multi-sport athlete", wiki_title="Babe Zaharias",
        significance="widely regarded as one of the greatest all-around athletes in history, she won Olympic medals in track and field and later became one of the founders and dominant early stars of professional women's golf",
        facts=[
            "Babe Didrikson Zaharias was born Mildred Ella Didrikson in Port Arthur, Texas, in 1911",
            "At the 1932 Los Angeles Olympics she won gold medals in the javelin throw and 80m hurdles, and a silver medal in the high jump, competing in the maximum number of individual events allowed for women at the time",
            "She excelled across an unusually wide range of sports beyond track and field, including basketball, baseball, and golf",
            "She turned to professional golf in the 1930s and 1940s, winning numerous championships and becoming one of the sport's first major stars",
            "She was a co-founder of the Ladies Professional Golf Association (LPGA) in 1950, helping establish women's professional golf as an organized tour",
            "She continued competing in golf even after being diagnosed with colon cancer in 1953, winning a major championship the following year",
            "She died of cancer in 1956, and is widely regarded as one of the greatest and most versatile athletes, male or female, of the 20th century",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="mohammad_ali_jinnah_ref_removed", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "mohammad_ali_jinnah_ref_removed"]

PEOPLE += [
    dict(
        id="nadia_comaneci", name="Nadia Comaneci", years="1961-present", nationality="Romanian",
        field="gymnast", wiki_title="Nadia Comaneci",
        significance="at the 1976 Montreal Olympics she became the first gymnast in Olympic history to be awarded a perfect score of 10.0, a result the scoreboard technology was not even designed to display",
        facts=[
            "Nadia Comaneci was born in Onesti, Romania, in 1961, and began gymnastics training at a very young age under coach Bela Karolyi",
            "At the 1976 Montreal Olympics, at age 14, she scored a perfect 10.0 on the uneven bars, the first perfect score ever awarded in Olympic gymnastics",
            "Because scoreboards at the time were not designed to display a score of 10.0, her perfect score was shown on the board as '1.00'",
            "She went on to receive six more perfect 10.0 scores during those same Olympic Games, and won three gold medals",
            "She won two additional gold medals at the 1980 Moscow Olympics, along with other medals",
            "She defected from Communist Romania in 1989, shortly before the fall of the Romanian Communist government, fleeing on foot across the border into Hungary",
            "She later married American gymnast Bart Conner, and the two have worked together in gymnastics coaching, commentary, and philanthropic work",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
    dict(
        id="kobe_bryant", name="Kobe Bryant", years="1978-2020", nationality="American",
        field="basketball player", wiki_title="Kobe Bryant",
        significance="widely regarded as one of the greatest basketball players of all time, he won five NBA championships with the Los Angeles Lakers over a 20-year career spent entirely with a single franchise",
        facts=[
            "Kobe Bryant was born in Philadelphia, Pennsylvania, in 1978, and spent part of his childhood in Italy, where his father played professional basketball",
            "He was drafted directly out of high school by the Charlotte Hornets in 1996 and immediately traded to the Los Angeles Lakers, where he spent his entire 20-year career",
            "He won five NBA championships with the Lakers, including three consecutive titles from 2000 to 2002 alongside center Shaquille O'Neal",
            "In January 2006 he scored 81 points in a single game against the Toronto Raptors, the second-highest single-game scoring total in NBA history",
            "He won the NBA Most Valuable Player award in 2008 and was named an NBA All-Star 18 times over his career",
            "He was known for an intense, demanding work ethic that came to be referred to as the 'Mamba Mentality', inspired by his self-given nickname 'Black Mamba'",
            "He died in a helicopter crash in California in 2020, along with his 13-year-old daughter Gianna and seven others, a loss widely mourned across the sports world",
        ], related_subjects=["Physical Education & Self-Defense"],
    ),
]


def main() -> None:
    upsert_section(
        "sports_athletics",
        "Sports & Athletics",
        "🏆",
        "Athletes across many sports whose records, achievements, and perseverance made lasting marks on their sports and, often, society.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
