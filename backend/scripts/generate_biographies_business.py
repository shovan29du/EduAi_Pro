#!/usr/bin/env python3
"""Populate the "Business & Economics" biography category with real,
verified entrepreneurs, business leaders, and economists. See
_biography_engine.py for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_business.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="steve_jobs", name="Steve Jobs", years="1955-2011", nationality="American",
        field="entrepreneur and inventor", wiki_title="Steve Jobs",
        significance="as co-founder and longtime CEO of Apple, he helped bring the personal computer, the iPod, the iPhone, and the iPad to mass markets, transforming the technology and consumer electronics industries",
        facts=[
            "Steve Jobs was born in San Francisco in 1955 and was adopted shortly after birth by Paul and Clara Jobs",
            "He co-founded Apple Computer in 1976 with Steve Wozniak in the Jobs family garage",
            "He was forced out of Apple in 1985 after a power struggle with the company's board, and went on to found NeXT and acquire what became Pixar Animation Studios",
            "Pixar, under his ownership, produced Toy Story in 1995, the first entirely computer-animated feature film",
            "He returned to Apple in 1997 when it acquired NeXT, and led the company's turnaround, launching the iMac, iPod, iPhone, and iPad over the following years",
            "The iPhone, launched in 2007, fundamentally reshaped the mobile phone and technology industries",
            "He died in 2011 from complications of pancreatic cancer, after stepping down as Apple's CEO just weeks earlier",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="warren_buffett", name="Warren Buffett", years="1930-present", nationality="American",
        field="investor and businessman", wiki_title="Warren Buffett",
        significance="widely regarded as one of the most successful investors in history, he built Berkshire Hathaway into a multinational conglomerate through disciplined value-investing principles",
        facts=[
            "Warren Buffett was born in Omaha, Nebraska, in 1930, and bought his first stock at age 11",
            "He studied under economist Benjamin Graham at Columbia Business School, whose 'value investing' philosophy strongly shaped his own approach",
            "He took control of Berkshire Hathaway, then a struggling textile company, in 1965, and transformed it into a diversified holding company",
            "Under his leadership, Berkshire Hathaway's stock has grown by a compound annual rate far exceeding the broader stock market over more than five decades",
            "He is known for his relatively frugal personal lifestyle despite his enormous wealth, including continuing to live in the same Omaha house he bought in 1958",
            "In 2010 he co-founded the Giving Pledge with Bill and Melinda Gates, encouraging billionaires to commit the majority of their wealth to philanthropy",
            "He has pledged to give away the vast majority of his own fortune, primarily to the Bill and Melinda Gates Foundation",
        ], related_subjects=["Business Studies", "Finance", "Economics"],
    ),
    dict(
        id="bill_gates", name="Bill Gates", years="1955-present", nationality="American",
        field="entrepreneur and philanthropist", wiki_title="Bill Gates",
        significance="as co-founder of Microsoft, he helped bring personal computing to a mass market, and has since become one of the world's largest private philanthropic donors through the Gates Foundation",
        facts=[
            "Bill Gates was born in Seattle, Washington, in 1955, and began programming computers as a teenager",
            "He co-founded Microsoft with Paul Allen in 1975, initially to develop software for early personal computers",
            "Microsoft's MS-DOS and later Windows operating systems became the dominant software platform for personal computers worldwide",
            "He served as Microsoft's CEO until 2000 and remained chairman of the board for many years afterward",
            "In 2000 he and his then-wife Melinda French Gates founded the Bill and Melinda Gates Foundation, which has since become one of the largest private charitable foundations in the world",
            "The foundation has focused heavily on global health initiatives, including vaccination campaigns and efforts to eliminate diseases such as polio and malaria",
            "He stepped down from Microsoft's board in 2020 to focus more fully on his philanthropic work",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="henry_ford", name="Henry Ford", years="1863-1947", nationality="American",
        field="industrialist", wiki_title="Henry Ford",
        significance="he revolutionized manufacturing through the moving assembly line, dramatically lowering the cost of automobiles and making car ownership accessible to a mass American market",
        facts=[
            "Henry Ford was born on a farm near Dearborn, Michigan, in 1863",
            "He founded the Ford Motor Company in 1903 after two earlier failed attempts to establish automobile companies",
            "In 1908 he introduced the Model T, an affordable and durable car intended for the average American family",
            "In 1913 his factories adopted the moving assembly line, drastically reducing the time and cost needed to produce each vehicle",
            "In 1914 he introduced the $5 workday, roughly double the prevailing wage, to reduce high worker turnover, a decision that drew wide public attention",
            "By the mid-1920s Ford Motor Company had produced over 15 million Model T vehicles",
            "He also held and promoted deeply antisemitic views later in life, a legacy that remains a significant and controversial part of his historical record",
        ], related_subjects=["Business Studies", "Economics"],
    ),
    dict(
        id="oprah_winfrey", name="Oprah Winfrey", years="1954-present", nationality="American",
        field="media executive and philanthropist", wiki_title="Oprah Winfrey",
        significance="host of the highest-rated daytime television talk show in American history for 25 years, she became one of the most influential media figures and one of the wealthiest self-made women in the world",
        facts=[
            "Oprah Winfrey was born in Kosciusko, Mississippi, in 1954, and experienced significant childhood poverty and hardship",
            "She began her broadcasting career as a local news anchor before hosting a Chicago talk show that became The Oprah Winfrey Show in 1986",
            "The Oprah Winfrey Show ran for 25 seasons, from 1986 to 2011, and became the highest-rated television talk show in American history",
            "Her book club, launched in 1996, was credited with dramatically boosting sales for the books she selected, a phenomenon sometimes called the 'Oprah Effect'",
            "She co-founded the cable network OWN (Oprah Winfrey Network) in 2011",
            "She has also had a notable acting career, receiving an Academy Award nomination for her role in the 1985 film The Color Purple",
            "She has donated tens of millions of dollars to educational causes, including founding the Oprah Winfrey Leadership Academy for Girls in South Africa in 2007",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="jeff_bezos", name="Jeff Bezos", years="1964-present", nationality="American",
        field="entrepreneur", wiki_title="Jeff Bezos",
        significance="he founded Amazon in 1994 as an online bookstore and built it into one of the world's largest e-commerce and cloud computing companies",
        facts=[
            "Jeff Bezos was born in Albuquerque, New Mexico, in 1964",
            "He founded Amazon in 1994, initially operating out of his garage in Bellevue, Washington, selling books online",
            "Amazon went public in 1997 and gradually expanded from books into nearly every category of retail",
            "He launched Amazon Web Services (AWS) in 2006, which became a major provider of cloud computing infrastructure for businesses worldwide",
            "He founded the aerospace company Blue Origin in 2000, pursuing goals including reusable rockets and space tourism",
            "He purchased The Washington Post newspaper in 2013",
            "He stepped down as Amazon's CEO in 2021, transitioning to executive chairman, and flew to space aboard a Blue Origin rocket later that year",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="elon_musk", name="Elon Musk", years="1971-present", nationality="South African-American",
        field="entrepreneur", wiki_title="Elon Musk",
        significance="he founded or led companies including Tesla, SpaceX, and PayPal, becoming a major figure in electric vehicles, private spaceflight, and online payments",
        facts=[
            "Elon Musk was born in Pretoria, South Africa, in 1971, and moved to Canada and later the United States as a young man",
            "He co-founded X.com in 1999, which later merged with a competitor to become PayPal, an early and influential online payment platform",
            "He founded SpaceX in 2002 with the goal of reducing the cost of space travel and eventually enabling human settlement of Mars",
            "SpaceX's Falcon 9 rocket became the first orbital-class rocket capable of reflight after a successful landing, in 2015",
            "He joined Tesla, an electric vehicle company, as an early investor and chairman in 2004, later becoming CEO, and led it into becoming the world's most valuable automaker by market capitalization",
            "He acquired the social media platform Twitter in 2022 and later renamed it X",
            "He has served in various capacities advising the US government on efficiency initiatives",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="john_d_rockefeller", name="John D. Rockefeller", years="1839-1937", nationality="American",
        field="industrialist and philanthropist", wiki_title="John D. Rockefeller",
        significance="founder of Standard Oil, he became the wealthiest American in history relative to the size of the national economy, and later became one of the largest philanthropic donors of his era",
        facts=[
            "John D. Rockefeller was born in Richford, New York, in 1839",
            "He co-founded Standard Oil in 1870, which grew to control roughly 90 percent of oil refining capacity in the United States by the 1880s",
            "Standard Oil's dominant market position led to major antitrust concerns, and the US Supreme Court ordered the company broken up into 34 separate companies in 1911",
            "Several of the companies that emerged from that breakup, including ExxonMobil and Chevron, remain major oil companies today",
            "He is often cited as the wealthiest American in history when his fortune is measured as a share of the US economy at the time",
            "He donated more than $500 million during his lifetime to causes including medical research, education, and public health",
            "His philanthropy helped fund the founding of the University of Chicago and the Rockefeller Foundation, established in 1913",
        ], related_subjects=["Business Studies", "Economics"],
    ),
    dict(
        id="adam_smith", name="Adam Smith", years="1723-1790", nationality="Scottish",
        field="economist and philosopher", wiki_title="Adam Smith",
        significance="his 1776 book The Wealth of Nations is considered the foundational text of modern economics, introducing ideas such as the division of labor and the 'invisible hand' of market self-interest",
        facts=[
            "Adam Smith was born in Kirkcaldy, Scotland, in 1723",
            "He was a professor of moral philosophy at the University of Glasgow before turning his focus to economic theory",
            "His 1776 book An Inquiry into the Nature and Causes of the Wealth of Nations argued that free markets, guided by self-interest, could efficiently allocate resources",
            "He introduced the metaphor of the 'invisible hand' to describe how individuals pursuing their own interest can unintentionally benefit society as a whole",
            "He described the concept of division of labor, using the example of a pin factory to show how specialization dramatically increases productivity",
            "His earlier 1759 book, The Theory of Moral Sentiments, explored the psychological and ethical foundations of human behavior and sympathy",
            "He died in Edinburgh in 1790, and is widely regarded today as the father of modern economics",
        ], related_subjects=["Economics", "Business Studies"],
    ),
    dict(
        id="john_maynard_keynes", name="John Maynard Keynes", years="1883-1946", nationality="British",
        field="economist", wiki_title="John Maynard Keynes",
        significance="his economic theories, developed largely in response to the Great Depression, argued for active government intervention to manage economic cycles, and reshaped 20th-century economic policy worldwide",
        facts=[
            "John Maynard Keynes was born in Cambridge, England, in 1883",
            "He was part of the British delegation to the Paris Peace Conference after World War I, and his 1919 book The Economic Consequences of the Peace warned that harsh reparations on Germany would cause future instability",
            "His 1936 book The General Theory of Employment, Interest and Money argued that government spending could be used to boost demand and reduce unemployment during economic downturns",
            "His ideas, later called Keynesian economics, heavily influenced government policy responses to the Great Depression and later economic crises around the world",
            "He played a key role in the 1944 Bretton Woods Conference, which established the framework for the post-World War II international monetary system, including the founding of the International Monetary Fund and World Bank",
            "He was also an active investor and art collector, and served as bursar of King's College, Cambridge, managing its investment portfolio",
            "He died in 1946, shortly after helping negotiate a major postwar loan from the United States to Britain",
        ], related_subjects=["Economics", "Business Studies"],
    ),
    dict(
        id="andrew_carnegie", name="Andrew Carnegie", years="1835-1919", nationality="Scottish-American",
        field="industrialist and philanthropist", wiki_title="Andrew Carnegie",
        significance="he built the Carnegie Steel Company into the dominant force in the American steel industry before selling it in 1901 and devoting the rest of his life to large-scale philanthropy",
        facts=[
            "Andrew Carnegie was born in Dunfermline, Scotland, in 1835, and emigrated with his family to the United States as a child, settling near Pittsburgh",
            "He worked his way up from a factory bobbin boy to a position at the Pennsylvania Railroad before investing heavily in the emerging steel industry",
            "He built the Carnegie Steel Company into the largest steel producer in the United States by the late 1800s",
            "He sold Carnegie Steel to financier J.P. Morgan in 1901 for $480 million, forming what became United States Steel, and became one of the wealthiest people in the world",
            "His 1889 essay 'The Gospel of Wealth' argued that the wealthy have a moral obligation to give away their fortunes for the public good during their lifetimes",
            "He funded the construction of more than 2,500 public libraries across the English-speaking world, many of which still operate today",
            "He gave away an estimated 90 percent of his fortune before his death in 1919",
        ], related_subjects=["Business Studies", "Economics"],
    ),
    dict(
        id="ratan_tata", name="Ratan Tata", years="1937-2024", nationality="Indian",
        field="industrialist", wiki_title="Ratan Tata",
        significance="as chairman of the Tata Group for over two decades, he transformed the Indian conglomerate into a global business with major international acquisitions, while remaining widely respected for his philanthropy and personal integrity",
        facts=[
            "Ratan Tata was born in Mumbai, India, in 1937, into the family that founded the Tata Group business conglomerate",
            "He studied architecture and structural engineering at Cornell University in the United States before returning to India to join the family business",
            "He became chairman of the Tata Group in 1991, at a time when India's economy was undergoing major liberalization reforms",
            "Under his leadership Tata Group made major international acquisitions, including the British steelmaker Corus in 2007 and the British car brands Jaguar and Land Rover in 2008",
            "He championed the development of the Tata Nano, launched in 2008 and marketed as one of the world's most affordable cars",
            "He stepped down as chairman in 2012 but remained chairman emeritus and continued to be closely associated with the company's public image",
            "He was widely respected in India for his personal modesty and extensive philanthropic giving through Tata Trusts, which hold a majority stake in Tata Sons",
        ], related_subjects=["Business Studies", "Economics"],
    ),
    dict(
        id="milton_friedman", name="Milton Friedman", years="1912-2006", nationality="American",
        field="economist", wiki_title="Milton Friedman",
        significance="a leading advocate of free-market economics and monetarism, he won the Nobel Memorial Prize in Economic Sciences in 1976 and profoundly influenced economic policy in the United States and United Kingdom",
        facts=[
            "Milton Friedman was born in Brooklyn, New York, in 1912, to immigrant parents",
            "He became a leading figure of the 'Chicago school' of economics while a professor at the University of Chicago for over three decades",
            "His 1963 book A Monetary History of the United States, co-written with Anna Schwartz, argued that mistakes in monetary policy significantly worsened the Great Depression",
            "He was a prominent advocate of monetarism, the theory that controlling the money supply is the most effective tool for managing inflation",
            "He won the Nobel Memorial Prize in Economic Sciences in 1976 for his work on consumption analysis, monetary history, and monetary policy",
            "His 1980 television series and book Free to Choose, co-written with his wife Rose Friedman, popularized free-market economic ideas for a general audience",
            "He served as an economic advisor to US President Ronald Reagan and UK Prime Minister Margaret Thatcher",
        ], related_subjects=["Economics", "Business Studies"],
    ),
    dict(
        id="sam_walton", name="Sam Walton", years="1918-1992", nationality="American",
        field="retail entrepreneur", wiki_title="Sam Walton",
        significance="he founded Walmart in 1962 and built it into the largest retailer in the world through a strategy of low prices and efficient supply chain management",
        facts=[
            "Sam Walton was born in Kingfisher, Oklahoma, in 1918",
            "He opened his first Walmart discount store in Rogers, Arkansas, in 1962, focused on offering low prices in small-town markets that larger retailers had overlooked",
            "He emphasized aggressive cost control and supply chain efficiency, passing savings on to customers through consistently low prices",
            "Walmart went public in 1970, and rapid store expansion followed throughout the 1970s and 1980s",
            "By the time of his death in 1992, Walmart had grown to over 1,700 stores and become one of the largest retailers in the United States",
            "He was known for his frugal personal habits despite his enormous wealth, including continuing to drive an older pickup truck",
            "Walmart is, as of the mid-2020s, the largest company in the world by revenue",
        ], related_subjects=["Business Studies", "Economics"],
    ),
    dict(
        id="walt_disney_biz_ref", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "walt_disney_biz_ref"]

PEOPLE += [
    dict(
        id="ray_kroc", name="Ray Kroc", years="1902-1984", nationality="American",
        field="businessman", wiki_title="Ray Kroc",
        significance="he transformed a single California hamburger stand into McDonald's, one of the largest fast-food chains in the world, by pioneering franchising and operational standardization",
        facts=[
            "Ray Kroc was born in Oak Park, Illinois, in 1902, and worked for decades as a traveling salesman, including selling milkshake mixers",
            "In 1954 he visited a California hamburger restaurant run by brothers Richard and Maurice McDonald that used an efficient, standardized production system",
            "He convinced the McDonald brothers to let him franchise their restaurant concept nationally, opening his first franchised location in Des Plaines, Illinois, in 1955",
            "He emphasized strict standardization of food quality, cleanliness, and service across every franchise location, an approach that became central to the fast-food industry model",
            "He bought out the McDonald brothers' ownership stake in the company in 1961",
            "Under his leadership McDonald's expanded into one of the largest and most recognizable restaurant chains in the world",
            "He died in 1984, having built McDonald's into an international symbol of American fast food and franchising",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="ingvar_kamprad", name="Ingvar Kamprad", years="1926-2018", nationality="Swedish",
        field="entrepreneur", wiki_title="Ingvar Kamprad",
        significance="he founded IKEA in 1943 and built it into the world's largest furniture retailer, pioneering flat-pack furniture design that customers assemble themselves",
        facts=[
            "Ingvar Kamprad was born near Agunnaryd, Sweden, in 1926, and began selling matches and small goods to neighbors as a young child",
            "He founded IKEA in 1943 at age 17, initially selling a range of small household goods by mail order",
            "He began selling furniture in the late 1940s and pioneered the concept of flat-pack furniture, which customers transport and assemble themselves, significantly reducing shipping and storage costs",
            "The first IKEA store opened in Almhult, Sweden, in 1958",
            "By the time of his death, IKEA had grown into the world's largest furniture retailer, with hundreds of stores across dozens of countries",
            "He was known for a famously frugal personal lifestyle despite his enormous wealth, including reportedly driving an older Volvo for many years",
            "He died in 2018, having built IKEA's Swedish minimalist design and low-cost model into a globally recognized brand",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="estee_lauder", name="Estee Lauder", years="1908/1906-2004", nationality="American",
        field="businesswoman", wiki_title="Estee Lauder (businesswoman)",
        significance="she built a small cosmetics business into the Estee Lauder Companies, one of the largest cosmetics and beauty companies in the world, pioneering marketing techniques like the free sample and gift-with-purchase",
        facts=[
            "Estee Lauder was born in Queens, New York, likely in 1908, to immigrant parents, and began experimenting with skin creams developed by her uncle as a young woman",
            "She and her husband Joseph Lauter (later Lauder) founded the Estee Lauder company in 1946, initially selling four skincare products",
            "She personally demonstrated her products to customers in department stores, an early and effective form of direct marketing in the cosmetics industry",
            "She pioneered the 'gift with purchase' marketing technique, offering free samples with cosmetics purchases, a strategy that became an industry standard",
            "The company expanded internationally beginning in the 1960s, and eventually grew to include brands such as Clinique, MAC, and Bobbi Brown",
            "She was the only woman on Time magazine's 1998 list of the 20 most influential business geniuses of the 20th century",
            "She died in 2004, having built one of the most successful and enduring cosmetics companies in the world",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="akio_morita", name="Akio Morita", years="1921-1999", nationality="Japanese",
        field="businessman", wiki_title="Akio Morita",
        significance="co-founder of Sony, he helped transform it from a small postwar electronics repair shop into one of the world's leading consumer electronics companies, and championed the Walkman portable cassette player",
        facts=[
            "Akio Morita was born in Nagoya, Japan, in 1921, into a family that had run a sake brewing business for generations",
            "He co-founded Tokyo Tsushin Kogyo in 1946 with engineer Masaru Ibuka, in the ruins of postwar Tokyo, which was later renamed Sony in 1958",
            "He pushed the company toward producing some of Japan's first transistor radios in the 1950s, helping establish Japan's reputation for compact consumer electronics",
            "He championed the development of the Sony Walkman, launched in 1979, a portable cassette player that transformed how people listened to music on the go",
            "He was an early advocate of building direct international sales operations rather than relying solely on foreign distributors, helping Sony establish a strong global brand presence",
            "He wrote the internationally influential 1986 book Made in Japan, describing Sony's rise and offering his views on Japanese business management",
            "He stepped back from active management in the 1990s after a stroke, and died in 1999",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="indra_nooyi", name="Indra Nooyi", years="1955-present", nationality="Indian-American",
        field="business executive", wiki_title="Indra Nooyi",
        significance="as CEO of PepsiCo from 2006 to 2018, she was one of the first women of color to lead a Fortune 50 company, and pushed the company toward healthier product lines and long-term sustainability strategy",
        facts=[
            "Indra Nooyi was born in Chennai (then Madras), India, in 1955, and moved to the United States in the mid-1970s for graduate business studies at Yale University",
            "She joined PepsiCo in 1994 and rose through a series of senior strategy and finance roles before becoming CEO in 2006",
            "As CEO, she led PepsiCo's roughly $13 billion acquisition of Quaker Oats and Tropicana era expansion into healthier food and beverage categories",
            "She introduced a long-term corporate strategy she called 'Performance with Purpose', pushing the company to reduce sugar, salt, and fat across its product lines while maintaining financial performance",
            "She was regularly ranked among the most powerful women in global business during her tenure, including by Forbes and Fortune magazines",
            "She stepped down as CEO in 2018 after 12 years leading the company, one of the longest tenures of any Fortune 500 CEO at the time",
            "She has continued to serve on multiple corporate and advisory boards and has written and spoken widely on leadership and work-life balance",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="walt_j_p_morgan", name="J.P. Morgan", years="1837-1913", nationality="American",
        field="banker and financier", wiki_title="J. P. Morgan",
        significance="the most powerful banker of his era, he financed and reorganized major American industries and personally organized a rescue of the US financial system during the Panic of 1907",
        facts=[
            "J.P. Morgan was born in Hartford, Connecticut, in 1837, into a prominent banking family",
            "He built J.P. Morgan & Co. into one of the most powerful financial institutions in the United States by the late 19th century",
            "He financed and reorganized major American railroads during a period of financial instability, consolidating competing lines into more efficient systems",
            "In 1901 he financed the creation of United States Steel by combining Andrew Carnegie's steel company with several competitors, forming the first billion-dollar corporation in history",
            "During the Panic of 1907, a severe financial crisis, he personally organized a group of bankers to provide emergency funding that helped stabilize the US financial system, in the absence of a central bank at the time",
            "That crisis and his central role in resolving it directly contributed to the creation of the Federal Reserve System in 1913, intended to prevent the need for a private banker to play that role again",
            "He died in 1913, and the banking institution he built remains, through later mergers, part of JPMorgan Chase, one of the largest banks in the world today",
        ], related_subjects=["Business Studies", "Economics", "Finance"],
    ),
    dict(
        id="mary_kay_ash", name="Mary Kay Ash", years="1918-2001", nationality="American",
        field="entrepreneur", wiki_title="Mary Kay Ash",
        significance="she founded Mary Kay Cosmetics in 1963 after being passed over for promotions in her earlier sales career, building a direct-sales cosmetics company that created significant financial opportunities for women",
        facts=[
            "Mary Kay Ash was born Mary Kathlyn Wagner in Hot Wells, Texas, in 1918",
            "She worked for over 25 years in direct sales before retiring after being repeatedly passed over for promotion in favor of male colleagues she had trained",
            "In 1963 she founded Mary Kay Cosmetics with her life savings, building a direct-sales model in which independent sales consultants, primarily women, sold products and earned commissions, including from recruiting and mentoring others",
            "The company became known for its incentive programs, including its famous pink Cadillac awards given to top-performing sales consultants",
            "By the time of her death the company had grown into a major multinational cosmetics business, with hundreds of thousands of independent sales consultants worldwide",
            "She wrote several books on business management and motivation, and her company's marketing and management principles were later studied in business school case studies",
            "She died in 2001, having built one of the largest direct-sales cosmetics companies in the world, providing income opportunities to generations of women",
        ], related_subjects=["Business Studies"],
    ),
    dict(
        id="jack_ma", name="Jack Ma", years="1964-present", nationality="Chinese",
        field="entrepreneur", wiki_title="Jack Ma",
        significance="he co-founded Alibaba in 1999 and built it into one of the world's largest e-commerce and technology companies, becoming one of China's most prominent entrepreneurs",
        facts=[
            "Jack Ma was born in Hangzhou, China, in 1964, and reportedly failed his university entrance exams twice before eventually being admitted to Hangzhou Normal University",
            "He worked as an English teacher before founding several early internet ventures in China during the mid-1990s",
            "In 1999 he co-founded Alibaba, an e-commerce platform connecting Chinese manufacturers with international buyers, working initially out of his apartment with a small group of co-founders",
            "Alibaba later expanded into consumer e-commerce through platforms including Taobao and Tmall, becoming central to China's rapidly growing online retail market",
            "Alibaba's 2014 initial public offering on the New York Stock Exchange raised approximately $25 billion, at the time the largest IPO in history",
            "He stepped down as Alibaba's executive chairman in 2019, saying he wanted to focus on philanthropy and education",
            "He largely disappeared from public view for a period in 2020 and 2021 following public criticism of Chinese financial regulators, before later re-emerging in more limited public appearances",
        ], related_subjects=["Business Studies", "ICT & Computer Science"],
    ),
    dict(
        id="phil_knight", name="Phil Knight", years="1938-present", nationality="American",
        field="entrepreneur", wiki_title="Phil Knight",
        significance="he co-founded Nike in 1964, building it from a small distributor of Japanese running shoes into the largest athletic footwear and apparel company in the world",
        facts=[
            "Phil Knight was born in Portland, Oregon, in 1938, and ran track at the University of Oregon under legendary coach Bill Bowerman",
            "He co-founded Blue Ribbon Sports with Bowerman in 1964, initially importing and selling Japanese running shoes out of the trunk of his car at track meets",
            "The company was renamed Nike in 1971, and adopted its now-iconic 'Swoosh' logo, designed by a graphic design student for a modest fee",
            "Bowerman's early experimentation with a waffle iron to create a new shoe sole tread pattern led to Nike's popular 'Waffle Trainer' shoe",
            "The company signed basketball star Michael Jordan to an endorsement deal in 1984, launching the Air Jordan sneaker line, which became one of the most commercially successful athletic shoe partnerships in history",
            "Nike grew under his leadership into the largest athletic footwear and apparel company in the world by revenue",
            "He wrote a memoir, Shoe Dog, published in 2016, describing the company's early struggles and growth, which became a bestseller",
        ], related_subjects=["Business Studies", "Physical Education & Self-Defense"],
    ),
]


def main() -> None:
    upsert_section(
        "business_economics",
        "Business & Economics",
        "💼",
        "Entrepreneurs, industrialists, and economists whose ideas and companies reshaped how the world works and trades.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
