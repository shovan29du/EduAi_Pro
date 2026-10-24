#!/usr/bin/env python3
"""Populate the "Social Reform & Activism" biography category with real,
verified civil-rights, human-rights, and reform leaders. See
_biography_engine.py for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_activism.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="martin_luther_king_jr", name="Martin Luther King Jr.", years="1929-1968", nationality="American",
        field="civil rights leader and minister", wiki_title="Martin Luther King Jr.",
        significance="he led the American civil rights movement through nonviolent protest, helping secure landmark legislation banning racial discrimination, and remains one of the most influential advocates of nonviolent social change in history",
        facts=[
            "Martin Luther King Jr. was born in Atlanta, Georgia, in 1929, the son of a Baptist minister",
            "He rose to national prominence leading the Montgomery Bus Boycott in Alabama in 1955-1956, sparked by Rosa Parks's arrest",
            "He co-founded the Southern Christian Leadership Conference in 1957 to coordinate nonviolent civil rights activism across the South",
            "He delivered his 'I Have a Dream' speech at the March on Washington in August 1963, before a crowd of roughly 250,000 people",
            "He won the Nobel Peace Prize in 1964 for his leadership of the nonviolent civil rights movement, becoming the youngest recipient at the time",
            "His activism helped pave the way for the Civil Rights Act of 1964 and the Voting Rights Act of 1965",
            "He was assassinated in Memphis, Tennessee, in April 1968, while supporting a sanitation workers' strike",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="rosa_parks", name="Rosa Parks", years="1913-2005", nationality="American",
        field="civil rights activist", wiki_title="Rosa Parks",
        significance="her refusal in 1955 to give up her bus seat to a white passenger in Montgomery, Alabama, sparked the Montgomery Bus Boycott and became a defining moment of the American civil rights movement",
        facts=[
            "Rosa Parks was born in Tuskegee, Alabama, in 1913",
            "She was already an active member of the Montgomery, Alabama chapter of the NAACP before her famous act of resistance",
            "On December 1, 1955, she refused to give up her seat on a Montgomery city bus to a white passenger, in violation of local segregation laws, and was arrested",
            "Her arrest sparked the Montgomery Bus Boycott, a 381-day boycott of the city's bus system organized in part by a then-largely-unknown minister named Martin Luther King Jr.",
            "The boycott ended after the US Supreme Court ruled that Montgomery's bus segregation laws were unconstitutional",
            "She continued civil rights activism for decades afterward, later working for US Congressman John Conyers in Detroit",
            "She was awarded the Presidential Medal of Freedom in 1996 and the Congressional Gold Medal in 1999",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="malala_yousafzai", name="Malala Yousafzai", years="1997-present", nationality="Pakistani",
        field="education activist", wiki_title="Malala Yousafzai",
        significance="after surviving a 2012 assassination attempt by the Taliban for advocating girls' education, she became the youngest-ever Nobel Peace Prize laureate and a leading global advocate for children's education",
        facts=[
            "Malala Yousafzai was born in Mingora, in the Swat Valley of Pakistan, in 1997",
            "As a young teenager she began writing an anonymous blog for the BBC about life under Taliban rule, which had banned girls from attending school in her region",
            "In October 2012, at age 15, she was shot in the head by a Taliban gunman while riding a school bus, in direct retaliation for her advocacy",
            "She survived the attack after emergency treatment and was later transferred to a hospital in Birmingham, England, for further care and recovery",
            "In 2013 she addressed the United Nations, calling for universal access to education, in a speech that drew global attention",
            "In 2014 she won the Nobel Peace Prize at age 17, becoming the youngest Nobel laureate in history",
            "She co-founded the Malala Fund, an organization working to expand access to education for girls around the world",
        ], related_subjects=["Civics", "World Politics"],
    ),
    dict(
        id="frederick_douglass", name="Frederick Douglass", years="1818-1895", nationality="American",
        field="abolitionist and writer", wiki_title="Frederick Douglass",
        significance="after escaping slavery, he became one of the most influential abolitionist speakers and writers in American history, and later served as an advisor to President Abraham Lincoln",
        facts=[
            "Frederick Douglass was born into slavery in Talbot County, Maryland, around 1818, and never knew his exact birth date",
            "He taught himself to read and write as a child, despite laws in many Southern states prohibiting the education of enslaved people",
            "He escaped slavery in 1838 by disguising himself as a sailor and traveling by train and boat to New York",
            "His 1845 autobiography, Narrative of the Life of Frederick Douglass, an American Slave, became a bestseller and a powerful piece of abolitionist literature",
            "He published his own abolitionist newspaper, The North Star, beginning in 1847",
            "He met with President Abraham Lincoln during the Civil War and advocated for Black soldiers to be allowed to fight for the Union",
            "He continued to advocate for civil rights and women's suffrage throughout his life, and died in Washington, D.C., in 1895",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="susan_b_anthony", name="Susan B. Anthony", years="1820-1906", nationality="American",
        field="women's suffrage leader", wiki_title="Susan B. Anthony",
        significance="a leading figure in the movement for women's right to vote in the United States, her decades of activism helped pave the way for the 19th Amendment, ratified 14 years after her death",
        facts=[
            "Susan B. Anthony was born in Adams, Massachusetts, in 1820, into a Quaker family active in social reform",
            "She became active first in the temperance and abolitionist movements before dedicating most of her later life to women's suffrage",
            "She co-founded the American Equal Rights Association in 1866 with Elizabeth Cady Stanton, advocating for voting rights regardless of race or gender",
            "In 1872 she was arrested for voting in the presidential election in Rochester, New York, in deliberate violation of laws restricting voting to men",
            "She was tried and convicted, and though fined $100, she refused to pay it, and authorities chose not to pursue collection to avoid further public attention",
            "She traveled extensively giving speeches advocating for women's suffrage, sometimes delivering as many as 75 to 100 speeches a year",
            "She died in 1906, 14 years before the 19th Amendment, granting women the right to vote nationwide, was ratified in 1920",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="mother_teresa", name="Mother Teresa", years="1910-1997", nationality="Albanian-Indian",
        field="missionary and humanitarian", wiki_title="Mother Teresa",
        significance="she founded the Missionaries of Charity, dedicating her life to caring for the poor and dying in Calcutta, India, and won the Nobel Peace Prize in 1979",
        facts=[
            "Mother Teresa was born Anjeze Gonxhe Bojaxhiu in Skopje, in what is now North Macedonia, in 1910",
            "She joined the Sisters of Loreto religious order as a young woman and was sent to Calcutta, India, in 1929",
            "In 1948 she left her teaching position to work directly among the poorest residents of Calcutta's slums",
            "In 1950 she founded the Missionaries of Charity, a religious congregation dedicated to caring for the sick, dying, orphaned, and destitute",
            "The organization she founded grew from 13 members in Calcutta to thousands of members operating in dozens of countries by the time of her death",
            "She won the Nobel Peace Prize in 1979, using the prize money to further her charitable work",
            "She was canonized as a saint by the Catholic Church in 2016, becoming Saint Teresa of Calcutta",
        ], related_subjects=["Civics", "World Religions"],
    ),
    dict(
        id="cesar_chavez", name="Cesar Chavez", years="1927-1993", nationality="American",
        field="labor and civil rights activist", wiki_title="Cesar Chavez",
        significance="he co-founded the United Farm Workers union and led major campaigns to improve working conditions for agricultural laborers in the United States through nonviolent organizing",
        facts=[
            "Cesar Chavez was born near Yuma, Arizona, in 1927, and his family lost their farm during the Great Depression, becoming migrant farm laborers",
            "He co-founded the National Farm Workers Association in 1962 with Dolores Huerta, which later became the United Farm Workers",
            "He led a five-year Delano grape strike and national boycott beginning in 1965, drawing widespread public support for farm worker rights",
            "He undertook several extended hunger strikes over the course of his activism to draw attention to farm worker conditions and to promote nonviolence within the movement",
            "His organizing helped secure the 1975 California Agricultural Labor Relations Act, the first law in the United States recognizing farm workers' right to collectively bargain",
            "He worked closely with Dolores Huerta throughout his career, and the two are often credited jointly with building the modern farm labor movement",
            "He died in 1993, and his birthday, March 31, is now recognized as a state holiday in several US states",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="dolores_huerta", name="Dolores Huerta", years="1930-present", nationality="American",
        field="labor and civil rights activist", wiki_title="Dolores Huerta",
        significance="co-founder of the United Farm Workers union with Cesar Chavez, she was a primary strategist and negotiator behind major farm labor victories and coined the rallying phrase 'Si, se puede'",
        facts=[
            "Dolores Huerta was born in Dawson, New Mexico, in 1930",
            "She worked as a schoolteacher before turning to community organizing, reportedly motivated by seeing so many hungry farm worker children in her classroom",
            "She co-founded the National Farm Workers Association with Cesar Chavez in 1962, which later became the United Farm Workers",
            "She was the lead negotiator in many of the union's major labor contracts, including after the successful Delano grape strike and boycott",
            "She coined the phrase 'Si, se puede' ('Yes, we can') during a 1972 campaign, which later became a widely used rallying cry in American political movements",
            "She was seriously injured by a police officer's baton during a 1988 protest in San Francisco, an incident that led to a change in the police department's crowd-control policies",
            "President Barack Obama awarded her the Presidential Medal of Freedom in 2012",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="harriet_tubman", name="Harriet Tubman", years="c. 1822-1913", nationality="American",
        field="abolitionist", wiki_title="Harriet Tubman",
        significance="after escaping slavery herself, she made roughly 13 missions back into the South to guide about 70 enslaved people to freedom via the Underground Railroad, and later served as a Union scout and spy during the Civil War",
        facts=[
            "Harriet Tubman was born into slavery in Dorchester County, Maryland, around 1822",
            "As a teenager she suffered a severe head injury when an overseer struck her, causing lifelong seizures and health issues",
            "She escaped slavery in 1849, traveling roughly 90 miles to Philadelphia",
            "She returned to the South an estimated 13 times over the following decade, guiding about 70 enslaved people, including family members, to freedom via the Underground Railroad network of safe houses",
            "She reportedly said she 'never lost a passenger' during her many dangerous missions",
            "During the Civil War she served the Union Army as a scout, spy, and nurse, and led an armed expedition, the Combahee Ferry Raid, that freed more than 700 enslaved people in South Carolina in 1863",
            "She spent her later years advocating for women's suffrage and died in 1913",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="desmond_tutu", name="Desmond Tutu", years="1931-2021", nationality="South African",
        field="archbishop and anti-apartheid activist", wiki_title="Desmond Tutu",
        significance="as a leading voice against apartheid in South Africa, he won the Nobel Peace Prize in 1984 and later chaired the Truth and Reconciliation Commission that examined the crimes of the apartheid era",
        facts=[
            "Desmond Tutu was born in Klerksdorp, South Africa, in 1931",
            "He was ordained as an Anglican priest in 1961 and became increasingly prominent in the anti-apartheid movement through the 1970s and 1980s",
            "He became the first Black general secretary of the South African Council of Churches in 1978, using the position to campaign against apartheid",
            "He won the Nobel Peace Prize in 1984 for his nonviolent campaign against apartheid",
            "He became the first Black Archbishop of Cape Town in 1986, the senior leadership position in the Anglican Church of Southern Africa",
            "After apartheid ended, he chaired South Africa's Truth and Reconciliation Commission from 1996, which investigated human rights abuses committed under apartheid",
            "He coined the term 'Rainbow Nation' to describe post-apartheid South Africa's racial and cultural diversity",
        ], related_subjects=["Civics", "World Politics", "World Religions"],
    ),
    dict(
        id="emmeline_pankhurst", name="Emmeline Pankhurst", years="1858-1928", nationality="British",
        field="suffragette leader", wiki_title="Emmeline Pankhurst",
        significance="she founded the Women's Social and Political Union and led a militant campaign for women's suffrage in Britain, helping secure the vote for British women in 1918 and 1928",
        facts=[
            "Emmeline Pankhurst was born in Manchester, England, in 1858",
            "She founded the Women's Social and Political Union (WSPU) in 1903, adopting the slogan 'Deeds, not words'",
            "The WSPU pursued increasingly militant tactics, including window-smashing campaigns and arson, to draw attention to the demand for women's voting rights",
            "She was arrested and imprisoned multiple times, and went on hunger strikes while incarcerated, which authorities responded to with force-feeding",
            "The British government passed the Cat and Mouse Act in 1913 in response to suffragette hunger strikes, allowing authorities to release and rearrest weakened prisoners",
            "In 1918 the Representation of the People Act granted voting rights to some British women over 30, and full equal voting rights for women followed in 1928, the year of her death",
            "She died in June 1928, just weeks before the Equal Franchise Act granted British women the vote on the same terms as men",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="wangari_maathai", name="Wangari Maathai", years="1940-2011", nationality="Kenyan",
        field="environmental and political activist", wiki_title="Wangari Maathai",
        significance="she founded the Green Belt Movement, which has planted tens of millions of trees across Kenya, and became the first African woman to win the Nobel Peace Prize, in 2004",
        facts=[
            "Wangari Maathai was born in Nyeri, Kenya, in 1940, and became the first woman in East and Central Africa to earn a doctoral degree, in biological sciences",
            "In 1977 she founded the Green Belt Movement, an organization encouraging Kenyan women to plant trees to combat deforestation, soil erosion, and poverty",
            "The Green Belt Movement is credited with planting tens of millions of trees across Kenya over the following decades",
            "She was arrested and beaten on several occasions by Kenyan authorities for her environmental and pro-democracy activism during the 1980s and 1990s",
            "She was elected to the Kenyan Parliament in 2002 following the country's transition to a more open multi-party democracy",
            "In 2004 she won the Nobel Peace Prize for her contribution to sustainable development, democracy, and peace, becoming the first African woman to receive the award",
            "She died in 2011, and her environmental advocacy continues to influence conservation movements across Africa",
        ], related_subjects=["Civics", "Environmental Science"],
    ),
    dict(
        id="nelson_mandela_activism_ref", name="__CROSSREF__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "nelson_mandela_activism_ref"]

PEOPLE += [
    dict(
        id="elizabeth_cady_stanton", name="Elizabeth Cady Stanton", years="1815-1902", nationality="American",
        field="women's rights leader", wiki_title="Elizabeth Cady Stanton",
        significance="a principal organizer of the 1848 Seneca Falls Convention, the first women's rights convention in the United States, she drafted its Declaration of Sentiments demanding equal rights including the right to vote",
        facts=[
            "Elizabeth Cady Stanton was born in Johnstown, New York, in 1815",
            "She organized the 1848 Seneca Falls Convention in New York alongside Lucretia Mott, the first women's rights convention held in the United States",
            "At that convention she drafted the Declaration of Sentiments, modeled on the Declaration of Independence, which called for women's suffrage and broader legal equality",
            "She partnered closely with Susan B. Anthony for decades, with Stanton often writing speeches and strategy that Anthony delivered and organized around the country",
            "She co-founded the National Woman Suffrage Association in 1869",
            "She helped compile and edit the multi-volume History of Woman Suffrage, documenting the movement's early decades",
            "She died in 1902, 18 years before the 19th Amendment granted women the right to vote nationwide in the United States",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="john_lewis", name="John Lewis", years="1940-2020", nationality="American",
        field="civil rights leader and congressman", wiki_title="John Lewis",
        significance="a leader of the American civil rights movement who helped organize the 1963 March on Washington and was severely beaten leading the 1965 Selma to Montgomery march, he later served over three decades in the US Congress",
        facts=[
            "John Lewis was born near Troy, Alabama, in 1940, the son of sharecroppers",
            "He became a leader of the Student Nonviolent Coordinating Committee (SNCC) and helped organize the Freedom Rides challenging segregated interstate bus travel in the early 1960s",
            "He was one of the organizers and youngest speakers at the 1963 March on Washington, where Martin Luther King Jr. delivered his 'I Have a Dream' speech",
            "On March 7, 1965, later known as 'Bloody Sunday', he was severely beaten by state troopers while leading a voting rights march across the Edmund Pettus Bridge in Selma, Alabama, suffering a fractured skull",
            "The televised violence of Bloody Sunday helped build public and political support for the Voting Rights Act of 1965, passed later that year",
            "He was elected to the US House of Representatives from Georgia in 1986 and served until his death in 2020, becoming known as the 'conscience of the Congress'",
            "He continued to promote what he called 'good trouble, necessary trouble' as a description of principled nonviolent activism throughout his life",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="jane_addams", name="Jane Addams", years="1860-1935", nationality="American",
        field="social reformer", wiki_title="Jane Addams",
        significance="a pioneer of the settlement house movement and social work profession, she co-founded Hull House in Chicago and won the Nobel Peace Prize in 1931 for her international peace activism",
        facts=[
            "Jane Addams was born in Cedarville, Illinois, in 1860",
            "In 1889 she co-founded Hull House in Chicago with Ellen Gates Starr, a settlement house providing education, childcare, and social services to poor immigrant communities",
            "Hull House became a model for the broader settlement house movement, which spread to dozens of other American cities",
            "She was a pioneering advocate for child labor laws, workplace safety regulations, and public health reforms in Chicago and nationally",
            "She helped found the National Association for the Advancement of Colored People (NAACP) in 1909",
            "She was a prominent international peace activist, serving as president of the Women's International League for Peace and Freedom",
            "In 1931 she became the first American woman to win the Nobel Peace Prize, sharing the award with fellow activist Nicholas Murray Butler",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="ida_b_wells", name="Ida B. Wells", years="1862-1931", nationality="American",
        field="journalist and civil rights activist", wiki_title="Ida B. Wells",
        significance="an investigative journalist who documented and campaigned against the lynching of Black Americans, she became one of the most important early leaders in the American civil rights and anti-lynching movements",
        facts=[
            "Ida B. Wells was born into slavery in Holly Springs, Mississippi, in 1862, just months before the Emancipation Proclamation",
            "She became a journalist and co-owner of a newspaper in Memphis, Tennessee, using it as a platform to investigate and document lynching, which was rarely reported accurately by mainstream newspapers at the time",
            "After a mob destroyed her newspaper's offices in 1892 in retaliation for her anti-lynching writing, she continued her investigative work from the North",
            "Her pamphlet Southern Horrors, published in 1892, used detailed statistical documentation to challenge the common false justifications given for lynching at the time",
            "She was a co-founder of the National Association for the Advancement of Colored People (NAACP) in 1909, though she later had some disagreements with the organization's direction",
            "She was also active in the women's suffrage movement, and famously refused to march at the back of a 1913 suffrage parade in Washington, D.C., as Black participants had been asked to do, instead joining the white Illinois delegation",
            "She died in Chicago in 1931, and was posthumously awarded a special citation by the Pulitzer Prize board in 2020 for her pioneering investigative journalism",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="elie_wiesel", name="Elie Wiesel", years="1928-2016", nationality="Romanian-American",
        field="writer and Holocaust survivor", wiki_title="Elie Wiesel",
        significance="a Holocaust survivor whose memoir Night became one of the most widely read accounts of the genocide, he devoted much of his life to human rights advocacy and won the Nobel Peace Prize in 1986",
        facts=[
            "Elie Wiesel was born in Sighet, in present-day Romania, in 1928, into a Jewish family",
            "In 1944 he and his family were deported to the Auschwitz concentration camp; his mother and younger sister were killed there, and his father later died at Buchenwald shortly before its liberation",
            "His 1956 memoir, published in English in 1960 as Night, described his experiences in the camps in spare, devastating prose, and became one of the most widely read Holocaust memoirs in the world",
            "He became an American citizen and worked as a journalist and university professor, teaching at Boston University for decades",
            "He was a founding chairman of the United States Holocaust Memorial Council, helping establish the US Holocaust Memorial Museum in Washington, D.C.",
            "He won the Nobel Peace Prize in 1986 for his advocacy against violence, repression, and racism",
            "He continued to speak out on human rights issues around the world, including genocides in Cambodia, Bosnia, and Rwanda, until his death in 2016",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="harvey_milk", name="Harvey Milk", years="1930-1978", nationality="American",
        field="politician and LGBT rights activist", wiki_title="Harvey Milk",
        significance="in 1977 he became one of the first openly gay elected officials in the United States, serving on the San Francisco Board of Supervisors before being assassinated in 1978",
        facts=[
            "Harvey Milk was born in Woodmere, New York, in 1930, and served in the US Navy before later settling in San Francisco",
            "He opened a camera shop in San Francisco's Castro district in the early 1970s, which became a hub for local political organizing within the growing gay community there",
            "He ran unsuccessfully for public office several times before being elected to the San Francisco Board of Supervisors in 1977, becoming one of the first openly gay people elected to public office in the United States",
            "As supervisor he championed a citywide gay rights ordinance and worked on a range of other municipal issues affecting his diverse district",
            "He played a key public role in campaigning against California's Proposition 6 in 1978, a ballot measure that would have banned gay and lesbian individuals from working in public schools; the measure was defeated",
            "He was assassinated in November 1978, along with San Francisco Mayor George Moscone, by former city supervisor Dan White",
            "He is widely remembered as a pioneering figure in LGBT political representation, and was posthumously awarded the Presidential Medal of Freedom in 2009",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="bayard_rustin", name="Bayard Rustin", years="1912-1987", nationality="American",
        field="civil rights strategist", wiki_title="Bayard Rustin",
        significance="a key strategist and organizer of the American civil rights movement, he was the principal organizer of the 1963 March on Washington, though his contributions were often downplayed at the time due to his being openly gay",
        facts=[
            "Bayard Rustin was born in West Chester, Pennsylvania, in 1912, and was raised largely by his Quaker grandparents",
            "He studied Mahatma Gandhi's philosophy of nonviolent resistance closely, and helped introduce these tactics into the American civil rights movement",
            "He advised Martin Luther King Jr. on nonviolent strategy during the Montgomery Bus Boycott in the mid-1950s",
            "He served as the chief organizer of the 1963 March on Washington for Jobs and Freedom, coordinating the logistics for a gathering of roughly 250,000 people in a matter of weeks",
            "Because he was openly gay, at a time of significant social stigma and legal discrimination, some civil rights leaders kept his organizing role deliberately out of the public spotlight",
            "He was arrested in 1953 on a morals charge related to his sexuality, an event later used by political opponents to try to discredit the civil rights movement",
            "He continued to work on civil rights, labor, and international human rights causes until his death in 1987, and was posthumously awarded the Presidential Medal of Freedom in 2013",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="greta_thunberg", name="Greta Thunberg", years="2003-present", nationality="Swedish",
        field="climate activist", wiki_title="Greta Thunberg",
        significance="beginning with a solitary school strike outside the Swedish parliament in 2018, she became the face of a global youth climate movement, addressing the United Nations and inspiring school climate strikes involving millions of young people worldwide",
        facts=[
            "Greta Thunberg was born in Stockholm, Sweden, in 2003, and has spoken publicly about being diagnosed with Asperger's syndrome, which she has described as giving her a particular focus and clarity on the climate issue",
            "In August 2018, at age 15, she began skipping school to sit alone outside the Swedish parliament with a sign reading 'Skolstrejk for klimatet' ('School strike for climate')",
            "Her solitary protest grew into the global 'Fridays for Future' movement, inspiring school climate strikes involving millions of students in cities around the world",
            "In 2019 she sailed across the Atlantic Ocean on a zero-emissions racing yacht to attend a UN climate summit in New York, rather than fly, citing the carbon footprint of air travel",
            "She delivered a widely covered speech to the United Nations Climate Action Summit in 2019, sharply criticizing world leaders for insufficient action on climate change",
            "She was named Time magazine's Person of the Year in 2019, the youngest individual to receive that recognition",
            "She has continued to be a prominent, sometimes controversial voice in global climate activism, and has faced both widespread admiration and significant public criticism for her direct, uncompromising style",
        ], related_subjects=["Civics", "Environmental Science"],
    ),
]


def main() -> None:
    upsert_section(
        "social_reform_activism",
        "Social Reform & Activism",
        "✊",
        "Civil rights leaders, suffragists, and humanitarians who organized and sacrificed to expand rights and dignity for others.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
