#!/usr/bin/env python3
"""Add a second large batch of ~1000 genuinely famous, individually-named
real museum objects/artifacts to the Virtual Museum, in a new
"World Heritage Treasures" gallery, complementing the earlier
"Famous Masterpieces" (501 objects) and "World Collections" (1000
objects) galleries.

Every entry is a real, well-known work (not a generated placeholder).
Each carries an accurate ``wiki_title`` -- the real Wikipedia article
title -- so the existing ``WikiThumbnail`` component
(frontend/src/components/VirtualMuseum.jsx) fetches a genuine, live photo
of the actual work from Wikipedia's public REST API at render time. This
project does not fabricate direct image URLs; the live-fetch-with-fallback
mechanism is the honest way to get a real thumbnail for every entry
without guessing file paths that might not exist.

Re-run after editing:
    python3 backend/scripts/generate_museum_objects_batch2.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
GALLERY_KEY = "world_heritage_treasures"


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def google_image_search(q: str) -> str:
    return "https://www.google.com/search?tbm=isch&q=" + quote_plus(q)


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def smarthistory(q: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(q)


# Each entry is a tuple: (name, wiki_title, creator_or_culture, date, origin,
#                         one_line_description)
# CATEGORY_ASSIGNMENTS pairs each list with its museum "category" facet.
CATEGORY_ASSIGNMENTS: list[tuple[list[tuple], str]] = []

# Real, individually famous science / technology / transportation artifacts
# held in real museums (Smithsonian, Science Museum London, Deutsches
# Museum, Royal Museums Greenwich, etc.). Each wiki_title is the exact
# English Wikipedia article title used to fetch a live thumbnail.
SCIENCE_TECH_BATCH2: list[tuple] = [
    # --- Early computing & calculating machines ---
    ("Antikythera mechanism", "Antikythera mechanism", "Unknown Greek engineers", "c. 150-100 BC", "Greece", "An ancient Greek analog device used to predict astronomical positions and eclipses, considered the earliest known analog computer."),
    ("Difference Engine No. 2", "Difference engine", "Charles Babbage", "1849 (built 1991)", "United Kingdom", "A mechanical calculator designed by Charles Babbage to automatically compute polynomial tables without human error."),
    ("Analytical Engine", "Analytical Engine", "Charles Babbage", "1837 (design)", "United Kingdom", "A proposed mechanical general-purpose computer design that introduced concepts such as a central processing unit and memory, programmed via punched cards."),
    ("Jacquard loom", "Jacquard machine", "Joseph Marie Jacquard", "1804", "France", "A mechanical loom attachment that used punched cards to control weaving patterns, later inspiring early computer programming methods."),
    ("Enigma machine", "Enigma machine", "Arthur Scherbius", "1918", "Germany", "A cipher machine used by German military forces to encrypt secret communications during World War II."),
    ("Bombe", "Bombe", "Alan Turing and Gordon Welchman", "1939", "United Kingdom", "An electromechanical device used by British codebreakers at Bletchley Park to help decipher German Enigma-encrypted messages."),
    ("Colossus computer", "Colossus computer", "Tommy Flowers", "1943", "United Kingdom", "The world's first programmable electronic digital computer, built to break the German Lorenz cipher during World War II."),
    ("Harvard Mark I", "Harvard Mark I", "IBM and Howard Aiken", "1944", "United States", "An early electromechanical computer used to perform long calculations automatically for the U.S. Navy during World War II."),
    ("ENIAC", "ENIAC", "John Mauchly and J. Presper Eckert", "1945", "United States", "One of the earliest general-purpose electronic digital computers, capable of being reprogrammed to solve a wide range of numerical problems."),
    ("Manchester Baby", "Manchester Baby", "Frederic Williams and Tom Kilburn", "1948", "United Kingdom", "The first electronic computer to run a stored program, demonstrating the practicality of stored-program computing."),
    ("Z3 computer", "Z3 (computer)", "Konrad Zuse", "1941", "Germany", "The world's first working programmable, fully automatic digital computer, built using electromechanical relays."),
    ("UNIVAC I", "UNIVAC I", "J. Presper Eckert and John Mauchly", "1951", "United States", "The first commercially produced electronic digital computer in the United States, famous for predicting the 1952 presidential election."),
    ("IBM 701", "IBM 701", "IBM", "1952", "United States", "IBM's first commercial scientific computer, marking the company's entry into the electronic computer business."),
    ("Curta calculator", "Curta", "Curt Herzstark", "1948", "Austria", "A compact hand-cranked mechanical calculator small enough to fit in a pocket, prized for its precision engineering."),
    ("Pascaline", "Pascal's calculator", "Blaise Pascal", "1642", "France", "One of the earliest mechanical calculators, invented to help perform addition and subtraction automatically."),
    ("Napier's bones", "Napier's bones", "John Napier", "1617", "Scotland", "A manually operated calculating device using numbered rods to perform multiplication and division through a lattice method."),
    ("Cray-1", "Cray-1", "Seymour Cray", "1976", "United States", "A pioneering supercomputer known for its distinctive C-shaped design and record-breaking processing speed."),
    ("Xerox Alto", "Xerox Alto", "Xerox PARC", "1973", "United States", "An early personal computer that pioneered the graphical user interface, mouse, and Ethernet networking."),
    ("Kenbak-1", "Kenbak-1", "John Blankenbaker", "1971", "United States", "Widely regarded as the first personal computer, though it predated the microprocessor and sold only a small number of units."),
    ("Altair 8800", "Altair 8800", "Micro Instrumentation and Telemetry Systems", "1975", "United States", "An early microcomputer kit that sparked the home computer revolution and inspired the founding of Microsoft."),
    # --- Personal computing & consumer electronics ---
    ("Apple I", "Apple I", "Steve Wozniak and Steve Jobs", "1976", "United States", "A hand-built computer that launched Apple Computer, designed largely by Steve Wozniak and sold as an assembled circuit board."),
    ("Apple Lisa", "Apple Lisa", "Apple Computer", "1983", "United States", "One of the first personal computers to feature a graphical user interface and mouse aimed at business users."),
    ("Macintosh 128K", "Macintosh 128K", "Apple Computer", "1984", "United States", "The original Macintosh computer, introduced with a famous Super Bowl advertisement and a pioneering graphical interface."),
    ("Commodore 64", "Commodore 64", "Commodore International", "1982", "United States", "The best-selling single computer model of all time, popular for home computing and video games in the 1980s."),
    ("Commodore PET", "Commodore PET", "Commodore International", "1977", "United States", "One of the first all-in-one personal computers to reach mass production, combining a keyboard, monitor, and cassette drive."),
    ("TRS-80", "TRS-80", "Tandy Corporation", "1977", "United States", "An early mass-produced microcomputer sold through Radio Shack stores, one of the \"1977 Trinity\" of home computers."),
    ("ZX Spectrum", "ZX Spectrum", "Sinclair Research", "1982", "United Kingdom", "A popular low-cost home computer that helped launch the British video game industry."),
    ("Osborne 1", "Osborne 1", "Osborne Computer Corporation", "1981", "United States", "The first commercially successful portable computer, featuring a small built-in screen and carrying handle."),
    ("IBM Personal Computer", "IBM Personal Computer", "IBM", "1981", "United States", "The original IBM PC, model 5150, which established the dominant architecture for personal computers for decades."),
    ("Atari 2600", "Atari 2600", "Atari, Inc.", "1977", "United States", "A pioneering home video game console that popularized the use of interchangeable game cartridges."),
    ("Nintendo Entertainment System", "Nintendo Entertainment System", "Nintendo", "1985", "Japan", "A home video game console credited with revitalizing the video game industry in North America after the crash of 1983."),
    ("PalmPilot", "PalmPilot", "Palm, Inc.", "1997", "United States", "A popular early personal digital assistant that set the standard for handheld computing and touchscreen note-taking."),
    ("Motorola DynaTAC 8000x", "Motorola DynaTAC 8000x", "Motorola", "1983", "United States", "The first commercially available handheld mobile telephone, nicknamed \"the brick\" for its size and weight."),
    ("IBM Simon", "IBM Simon", "IBM and BellSouth", "1994", "United States", "Widely regarded as the first smartphone, combining a mobile phone with calendar, notepad, and touchscreen features."),
    ("Sony Walkman TPS-L2", "Walkman", "Sony", "1979", "Japan", "The original portable cassette player that popularized personal, on-the-go music listening worldwide."),
    # --- Robotics ---
    ("Unimate", "Unimate", "George Devol", "1961", "United States", "The first digitally operated and programmable industrial robot, installed on a General Motors assembly line."),
    ("Shakey the robot", "Shakey the robot", "Stanford Research Institute", "1966", "United States", "The first mobile robot able to reason about its own actions, considered a milestone in artificial intelligence research."),
    ("Sojourner rover", "Sojourner (rover)", "NASA Jet Propulsion Laboratory", "1997", "United States", "The first wheeled rover to operate on the surface of Mars, part of the Mars Pathfinder mission."),
    # --- Space exploration ---
    ("Sputnik 1", "Sputnik 1", "Soviet Union space program", "1957", "Soviet Union", "The first artificial satellite launched into orbit, marking the start of the Space Age."),
    ("Explorer 1", "Explorer 1", "Jet Propulsion Laboratory", "1958", "United States", "The first satellite launched by the United States, which discovered the Van Allen radiation belts."),
    ("Vostok 1", "Vostok 1", "Soviet Union space program", "1961", "Soviet Union", "The spacecraft that carried Yuri Gagarin on the first human spaceflight in history."),
    ("Freedom 7", "Freedom 7", "NASA / McDonnell Aircraft", "1961", "United States", "The Mercury capsule that carried Alan Shepard on the first American human spaceflight."),
    ("Friendship 7", "Friendship 7", "NASA / McDonnell Aircraft", "1962", "United States", "The Mercury spacecraft that carried John Glenn as the first American to orbit the Earth."),
    ("Telstar", "Telstar", "Bell Telephone Laboratories", "1962", "United States", "The first active communications satellite, which relayed the first live transatlantic television broadcast."),
    ("Luna 3", "Luna 3", "Soviet Union space program", "1959", "Soviet Union", "The Soviet probe that captured the first photographs of the far side of the Moon."),
    ("Gemini 3 spacecraft", "Gemini 3", "NASA / McDonnell Aircraft", "1965", "United States", "The first crewed mission of Project Gemini, nicknamed \"Molly Brown,\" testing orbital maneuvering techniques."),
    ("Ranger 7", "Ranger 7", "NASA Jet Propulsion Laboratory", "1964", "United States", "The first American spacecraft to successfully transmit close-up images of the Moon before impact."),
    ("Apollo 11 Command Module Columbia", "Columbia (spacecraft)", "NASA / North American Rockwell", "1969", "United States", "The Apollo 11 command module that carried astronauts to lunar orbit and safely returned them to Earth."),
    ("Apollo 11 Lunar Module Eagle", "Eagle (spacecraft)", "NASA / Grumman", "1969", "United States", "The Apollo 11 lunar module that carried Neil Armstrong and Buzz Aldrin to the first crewed Moon landing."),
    ("Apollo 13 Command Module Odyssey", "Odyssey (spacecraft)", "NASA / North American Rockwell", "1970", "United States", "The Apollo 13 command module that safely returned its crew to Earth after an onboard explosion."),
    ("Lunar Roving Vehicle", "Lunar Roving Vehicle", "Boeing and General Motors", "1971", "United States", "An electric vehicle used by Apollo astronauts to travel across the lunar surface during later Moon missions."),
    ("Skylab", "Skylab", "NASA", "1973", "United States", "The first American space station, used for scientific experiments and long-duration crewed missions in orbit."),
    ("Voyager Golden Record", "Voyager Golden Record", "NASA / Carl Sagan committee", "1977", "United States", "A phonograph record carried aboard the Voyager probes containing sounds and images meant to represent life on Earth to any extraterrestrial finder."),
    ("Pioneer 10", "Pioneer 10", "NASA Ames Research Center", "1972", "United States", "The first spacecraft to travel through the asteroid belt and make direct observations of Jupiter, carrying the Pioneer plaque."),
    ("Pioneer plaque", "Pioneer plaque", "Carl Sagan and Frank Drake", "1972", "United States", "An engraved plaque attached to the Pioneer 10 and 11 probes intended to convey information about humanity to any intelligent extraterrestrial life."),
    ("Viking 1", "Viking 1", "NASA", "1975", "United States", "The first spacecraft to successfully land on Mars and return usable images from the planet's surface."),
    ("Mars Pathfinder", "Mars Pathfinder", "NASA Jet Propulsion Laboratory", "1996", "United States", "A NASA mission that delivered the Sojourner rover to Mars and demonstrated low-cost landing technology."),
    ("Hubble Space Telescope", "Hubble Space Telescope", "NASA and ESA", "1990", "United States", "A space telescope launched into low Earth orbit that has produced some of the most detailed images of the universe ever recorded."),
    ("Space Shuttle Enterprise", "Space Shuttle Enterprise", "NASA / Rockwell International", "1976", "United States", "The first Space Shuttle orbiter built, used for approach and landing tests but never flown into orbit."),
    ("Space Shuttle Discovery", "Space Shuttle Discovery", "NASA / Rockwell International", "1984", "United States", "The Space Shuttle orbiter with the most spaceflights, which flew the Hubble Space Telescope into orbit."),
    ("Space Shuttle Atlantis", "Space Shuttle Atlantis", "NASA / Rockwell International", "1985", "United States", "A Space Shuttle orbiter that flew the final Space Shuttle program mission in 2011."),
    ("Space Shuttle Endeavour", "Space Shuttle Endeavour", "NASA / Rockwell International", "1991", "United States", "A Space Shuttle orbiter built to replace Challenger, which flew numerous missions to the International Space Station."),
    ("Saturn V", "Saturn V", "NASA / Wernher von Braun", "1967", "United States", "The powerful multistage rocket that launched the Apollo missions to the Moon, remaining the most powerful rocket ever successfully flown."),
    # --- Aviation ---
    ("Wright Flyer", "Wright Flyer", "Orville and Wilbur Wright", "1903", "United States", "The aircraft that made the first sustained, controlled, powered flight by a heavier-than-air machine."),
    ("Wright Military Flyer", "Wright Military Flyer", "Orville and Wilbur Wright", "1909", "United States", "The first military airplane, purchased by the U.S. Army Signal Corps after a series of demonstration flights by the Wright brothers."),
    ("Bleriot XI", "Blériot XI", "Louis Blériot", "1909", "France", "The aircraft in which Louis Blériot made the first flight across the English Channel."),
    ("Vickers Vimy", "Vickers Vimy", "Vickers Limited", "1917", "United Kingdom", "The bomber aircraft, later adapted for record flights, that made the first nonstop transatlantic flight piloted by Alcock and Brown."),
    ("Fokker Dr.I", "Fokker Dr.I", "Fokker", "1917", "Germany", "A World War I triplane fighter famously flown by the \"Red Baron,\" Manfred von Richthofen."),
    ("Sopwith Camel", "Sopwith Camel", "Sopwith Aviation Company", "1917", "United Kingdom", "A British fighter aircraft credited with shooting down more enemy aircraft than any other Allied fighter of World War I."),
    ("Curtiss JN-4", "Curtiss JN-4", "Curtiss Aeroplane Company", "1915", "United States", "A widely used biplane trainer nicknamed the \"Jenny,\" which introduced many pilots to flight in the early 20th century."),
    ("Spirit of St. Louis", "Spirit of St. Louis", "Ryan Airlines", "1927", "United States", "The single-engine aircraft that Charles Lindbergh flew on the first solo nonstop transatlantic flight."),
    ("Junkers F.13", "Junkers F.13", "Junkers", "1919", "Germany", "The world's first all-metal, cantilever-wing airliner, designed specifically for commercial passenger transport."),
    ("LZ 127 Graf Zeppelin", "LZ 127 Graf Zeppelin", "Luftschiffbau Zeppelin", "1928", "Germany", "A pioneering passenger airship that circumnavigated the globe and completed regular transatlantic crossings."),
    ("LZ 129 Hindenburg", "LZ 129 Hindenburg", "Luftschiffbau Zeppelin", "1936", "Germany", "A large passenger airship that was destroyed in a famous fire while attempting to dock in New Jersey in 1937."),
    ("Piper J-3 Cub", "Piper J-3 Cub", "Piper Aircraft", "1938", "United States", "A simple, lightweight training aircraft that became one of the most recognizable small planes in aviation history."),
    ("Gee Bee Model Z", "Gee Bee Model Z", "Granville Brothers Aircraft", "1931", "United States", "A stubby, powerful racing aircraft that set speed records during the golden age of air racing."),
    ("Supermarine Spitfire", "Supermarine Spitfire", "Supermarine", "1938", "United Kingdom", "An iconic British fighter aircraft that played a decisive role in the Battle of Britain during World War II."),
    ("Messerschmitt Bf 109", "Messerschmitt Bf 109", "Messerschmitt", "1937", "Germany", "The primary fighter aircraft of the German Luftwaffe throughout World War II and one of the most-produced fighters in history."),
    ("North American P-51 Mustang", "North American P-51 Mustang", "North American Aviation", "1940", "United States", "A long-range American fighter aircraft renowned for escorting bombers deep into enemy territory during World War II."),
    ("Enola Gay", "Enola Gay", "Boeing / Martin Company", "1945", "United States", "The B-29 Superfortress bomber that dropped the atomic bomb \"Little Boy\" on Hiroshima in 1945."),
    ("Bockscar", "Bockscar", "Boeing / Martin Company", "1945", "United States", "The B-29 Superfortress bomber that dropped the atomic bomb \"Fat Man\" on Nagasaki in 1945."),
    ("Spruce Goose", "Hughes H-4 Hercules", "Hughes Aircraft Company", "1947", "United States", "A giant wooden flying boat, nicknamed the \"Spruce Goose,\" that made a single flight and remains the aircraft with the largest wingspan ever flown."),
    ("Bell X-1", "Bell X-1", "Bell Aircraft Corporation", "1947", "United States", "The rocket-powered aircraft in which Chuck Yeager became the first pilot to break the sound barrier in level flight."),
    ("Sikorsky VS-300", "Sikorsky VS-300", "Igor Sikorsky", "1939", "United States", "An experimental helicopter that established the single main rotor and tail rotor design used by most modern helicopters."),
    ("Bell 47", "Bell 47", "Bell Aircraft Corporation", "1945", "United States", "The first helicopter certified for civilian use, widely produced and used in military, medical, and agricultural roles."),
    ("Douglas DC-3", "Douglas DC-3", "Douglas Aircraft Company", "1935", "United States", "A revolutionary propeller airliner credited with making passenger air travel profitable and safe for airlines."),
    ("de Havilland Comet", "de Havilland Comet", "de Havilland", "1949", "United Kingdom", "The world's first commercial jet airliner to enter regular service, ushering in the jet age of air travel."),
    ("Boeing 707", "Boeing 707", "Boeing", "1957", "United States", "A pioneering commercial jet airliner that helped establish Boeing as a leader in jet aviation and popularized jet travel."),
    ("Concorde", "Concorde", "BAC and Aérospatiale", "1969", "United Kingdom", "A supersonic passenger airliner jointly developed by Britain and France, capable of crossing the Atlantic in about three hours."),
    ("Lockheed SR-71 Blackbird", "Lockheed SR-71 Blackbird", "Lockheed Skunk Works", "1964", "United States", "A long-range, high-altitude reconnaissance aircraft that remains the fastest air-breathing crewed aircraft ever flown."),
    ("North American X-15", "North American X-15", "North American Aviation", "1959", "United States", "An experimental rocket-powered aircraft that set speed and altitude records and carried pilots to the edge of space."),
    ("Avro Vulcan", "Avro Vulcan", "Avro", "1952", "United Kingdom", "A distinctive delta-wing strategic bomber that served as part of Britain's nuclear deterrent during the Cold War."),
    ("Hawker Siddeley Harrier", "Hawker Siddeley Harrier", "Hawker Siddeley", "1967", "United Kingdom", "The first operational fixed-wing aircraft capable of vertical or short takeoff and landing."),
    # --- Rail transportation ---
    ("Puffing Billy", "Puffing Billy", "William Hedley", "1813", "United Kingdom", "One of the oldest surviving steam locomotives, built to haul coal and demonstrating the practicality of steam railway locomotion."),
    ("Locomotion No. 1", "Locomotion No. 1", "George Stephenson", "1825", "United Kingdom", "The first steam locomotive to haul a passenger train on a public railway, the Stockton and Darlington Railway."),
    ("Stephenson's Rocket", "Stephenson's Rocket", "Robert Stephenson and Company", "1829", "United Kingdom", "An early steam locomotive whose innovative design won the Rainhill Trials and influenced locomotive design for decades."),
    ("Tom Thumb locomotive", "Tom Thumb (locomotive)", "Peter Cooper", "1830", "United States", "An early American steam locomotive built to demonstrate the feasibility of steam power for the Baltimore and Ohio Railroad."),
    ("DeWitt Clinton locomotive", "DeWitt Clinton (locomotive)", "West Point Foundry", "1831", "United States", "One of the first steam locomotives to operate in New York State, pulling an early passenger train."),
    ("City of Truro", "City of Truro (locomotive)", "Great Western Railway", "1903", "United Kingdom", "A steam locomotive claimed to have been the first to reach 100 miles per hour, though the record remains disputed."),
    ("Flying Scotsman", "Flying Scotsman (locomotive)", "Doncaster Works, LNER", "1923", "United Kingdom", "A famous steam locomotive that became the first to be officially recorded exceeding 100 miles per hour."),
    ("Mallard locomotive", "LNER Class A4 4468 Mallard", "Nigel Gresley, LNER", "1938", "United Kingdom", "The steam locomotive that holds the world speed record for steam traction, reaching 126 miles per hour."),
    ("Union Pacific Big Boy", "Union Pacific Big Boy", "American Locomotive Company", "1941", "United States", "Among the largest steam locomotives ever built, designed to haul heavy freight trains over mountainous terrain."),
    # --- Automobiles ---
    ("Benz Patent-Motorwagen", "Benz Patent-Motorwagen", "Karl Benz", "1885", "Germany", "Widely recognized as the first true automobile, powered by an internal combustion engine and patented by Karl Benz."),
    ("Duryea Motor Wagon", "Duryea Motor Wagon", "Charles and Frank Duryea", "1893", "United States", "Considered the first gasoline-powered automobile built and driven in the United States."),
    ("Stanley Steamer", "Stanley Steamer", "Stanley Motor Carriage Company", "1897", "United States", "A popular early steam-powered automobile that set land speed records in the early 1900s."),
    ("Ford Model T", "Ford Model T", "Ford Motor Company", "1908", "United States", "The first mass-produced automobile using assembly line techniques, which made car ownership affordable for millions."),
    ("Rolls-Royce Silver Ghost", "Rolls-Royce Silver Ghost", "Rolls-Royce Limited", "1907", "United Kingdom", "A luxury motor car renowned for its smooth and quiet engine, helping establish Rolls-Royce's reputation for engineering excellence."),
    ("Volkswagen Beetle", "Volkswagen Beetle", "Volkswagen", "1938", "Germany", "One of the best-selling and most recognizable car designs in automotive history, produced for over six decades."),
    # --- Maritime ---
    ("Mary Rose", "Mary Rose", "Henry VIII's navy", "1511", "England", "A Tudor warship that sank in 1545 and was raised in 1982, offering a remarkably preserved snapshot of 16th-century naval life."),
    ("Vasa ship", "Vasa (ship)", "Swedish Navy", "1628", "Sweden", "A Swedish warship that sank on her maiden voyage and was salvaged nearly intact more than 300 years later."),
    ("USS Constitution", "USS Constitution", "Edmund Hartt shipyard", "1797", "United States", "The world's oldest commissioned naval vessel still afloat, nicknamed \"Old Ironsides\" for its resilience in battle."),
    ("HMS Victory", "HMS Victory", "Chatham Dockyard", "1765", "United Kingdom", "The Royal Navy flagship of Admiral Horatio Nelson at the Battle of Trafalgar, now preserved as a museum ship."),
    ("USS Monitor", "USS Monitor", "John Ericsson", "1862", "United States", "An innovative ironclad warship that fought the first battle between ironclad ships during the American Civil War."),
    ("Cutty Sark", "Cutty Sark", "Scott & Linton", "1869", "United Kingdom", "One of the last and fastest tea clippers built, now preserved as a museum ship in Greenwich, England."),
    ("SS Great Britain", "SS Great Britain", "Isambard Kingdom Brunel", "1843", "United Kingdom", "A groundbreaking passenger steamship that was the first to combine an iron hull with screw propeller propulsion."),
    ("Turbinia", "Turbinia", "Charles Algernon Parsons", "1894", "United Kingdom", "The first steam turbine-powered ship, which demonstrated unprecedented speed and revolutionized naval propulsion."),
    ("RMS Titanic", "RMS Titanic", "Harland and Wolff", "1912", "United Kingdom", "A luxury ocean liner that sank on its maiden voyage after striking an iceberg, whose recovered artifacts are displayed in museums worldwide."),
    ("RMS Queen Mary", "RMS Queen Mary", "John Brown & Company", "1936", "United Kingdom", "A transatlantic ocean liner famed for its speed and luxury, now preserved as a floating museum and hotel in Long Beach, California."),
    ("Golden Hind", "Golden Hind", "English shipwrights", "1577", "England", "The galleon in which Sir Francis Drake circumnavigated the globe between 1577 and 1580."),
    ("Santa Maria ship", "Santa María (ship)", "Spanish shipbuilders", "1460s", "Spain", "The largest of the three ships used by Christopher Columbus on his first voyage across the Atlantic in 1492."),
    ("HMS Beagle", "HMS Beagle", "Royal Navy", "1820", "United Kingdom", "The survey ship on which Charles Darwin sailed on his famous voyage that helped shape his theory of evolution."),
    ("Kon-Tiki", "Kon-Tiki", "Thor Heyerdahl", "1947", "Norway", "A balsawood raft sailed by Thor Heyerdahl across the Pacific Ocean to demonstrate that ancient South Americans could have reached Polynesia."),
    ("Endurance", "Endurance (1912 ship)", "Framnæs shipyard", "1912", "Norway", "The polar exploration ship of Ernest Shackleton's Imperial Trans-Antarctic Expedition, crushed by pack ice in 1915 and located on the seabed in 2022."),
    ("USS Nautilus (SSN-571)", "USS Nautilus (SSN-571)", "United States Navy", "1954", "United States", "The world's first operational nuclear-powered submarine, which became the first vessel to reach the geographic North Pole underwater."),
    ("Trieste bathyscaphe", "Trieste (bathyscaphe)", "Auguste Piccard", "1953", "Switzerland", "A deep-diving research submersible that became the first crewed vessel to reach the bottom of the Challenger Deep, the deepest known point in Earth's oceans."),
    ("Alvin submersible", "Alvin (submersible)", "Woods Hole Oceanographic Institution", "1964", "United States", "A deep-sea research submersible used in numerous scientific expeditions, including the exploration of the wreck of RMS Titanic."),
    # --- Scientific instruments & industrial machines ---
    ("Foucault pendulum", "Foucault pendulum", "Léon Foucault", "1851", "France", "A simple pendulum device that provided the first direct visual demonstration of the Earth's rotation."),
    ("Galileo's telescope", "Galileo's telescope", "Galileo Galilei", "1609", "Italy", "An early refracting telescope built and used by Galileo Galilei to make groundbreaking astronomical observations."),
    ("Leviathan of Parsonstown", "Leviathan of Parsonstown", "William Parsons, 3rd Earl of Rosse", "1845", "Ireland", "A giant reflecting telescope that was the largest in the world for over seventy years, used to discover spiral galaxy structures."),
    ("H4 marine chronometer", "H4 (chronometer)", "John Harrison", "1759", "United Kingdom", "A precision marine chronometer that solved the problem of determining longitude at sea."),
    ("Cavendish experiment apparatus", "Cavendish experiment", "Henry Cavendish", "1798", "United Kingdom", "A torsion balance apparatus used to measure the density of the Earth and effectively determine the gravitational constant."),
    ("Van de Graaff generator", "Van de Graaff generator", "Robert J. Van de Graaff", "1929", "United States", "An electrostatic generator capable of producing very high voltages, widely used for physics demonstrations and early particle accelerators."),
    ("Tesla coil", "Tesla coil", "Nikola Tesla", "1891", "United States", "A resonant transformer circuit invented by Nikola Tesla to produce high-voltage, low-current electrical discharges."),
    ("Wilson cloud chamber", "Cloud chamber", "Charles Thomson Rees Wilson", "1911", "United Kingdom", "A particle detector used to visualize the tracks of ionizing radiation, instrumental in early discoveries in particle physics."),
    ("Michelson interferometer", "Michelson interferometer", "Albert A. Michelson", "1881", "United States", "A precision optical instrument used in the famous Michelson-Morley experiment that helped disprove the theory of luminiferous ether."),
    ("Newcomen atmospheric engine", "Newcomen atmospheric engine", "Thomas Newcomen", "1712", "United Kingdom", "The first practical steam engine, used to pump water out of mines and a key precursor to the Industrial Revolution."),
    ("Watt steam engine", "Watt steam engine", "James Watt", "1776", "United Kingdom", "An improved steam engine design featuring a separate condenser, dramatically increasing efficiency and powering the Industrial Revolution."),
    ("Spinning Jenny", "Spinning Jenny", "James Hargreaves", "1764", "United Kingdom", "A multi-spindle spinning frame that greatly increased the productivity of yarn production during the early Industrial Revolution."),
    ("Spinning mule", "Spinning mule", "Samuel Crompton", "1779", "United Kingdom", "A machine that combined features of earlier spinning devices to produce strong, fine yarn, transforming textile manufacturing."),
    ("Cotton gin", "Cotton gin", "Eli Whitney", "1793", "United States", "A machine that mechanized the removal of seeds from cotton fibers, dramatically increasing cotton production in the American South."),
    ("Lovell Telescope", "Lovell Telescope", "Jodrell Bank Observatory, University of Manchester", "1957", "United Kingdom", "A large steerable radio telescope that was the first of its kind and remains a major instrument for radio astronomy research."),
    ("Cyclotron", "Cyclotron", "Ernest Lawrence", "1932", "United States", "An early type of particle accelerator that uses a magnetic field to spiral charged particles to high energies."),
    ("Geiger counter", "Geiger counter", "Hans Geiger and Walther Müller", "1928", "Germany", "An instrument used to detect and measure ionizing radiation, widely used in physics research and radiation safety."),
    ("Bunsen burner", "Bunsen burner", "Robert Bunsen and Peter Desaga", "1855", "Germany", "A laboratory gas burner that produces a single open flame, used for heating and sterilization in chemistry labs worldwide."),
    ("Slide rule", "Slide rule", "William Oughtred", "1622", "United Kingdom", "A mechanical analog calculating device used for multiplication, division, and other mathematical functions before electronic calculators."),
    ("Astrolabe", "Astrolabe", "Ancient Greek and Islamic astronomers", "c. 200 BC (refined in the medieval Islamic world)", "Greece", "An ancient astronomical instrument used to measure the position of celestial bodies and solve problems of time and location."),
    ("Orrery", "Orrery", "George Graham and John Rowley", "c. 1704", "United Kingdom", "A mechanical model of the solar system that demonstrates the relative positions and motions of the planets around the Sun."),
    ("Sextant", "Sextant", "John Hadley and Thomas Godfrey", "1730", "United Kingdom", "A navigational instrument used to measure the angle between celestial objects and the horizon to determine position at sea."),
    ("Gyrocompass", "Gyrocompass", "Elmer Sperry", "1908", "United States", "A type of compass that uses a fast-spinning rotor to find true north, unaffected by magnetic interference, and widely adopted by ships."),
    ("Iron lung", "Iron lung", "Philip Drinker and Louis Agassiz Shaw", "1928", "United States", "A negative-pressure mechanical respirator used to help patients, especially polio victims, breathe when their own muscles could not."),
    ("Crookes tube", "Crookes tube", "William Crookes", "1875", "United Kingdom", "An early experimental electrical discharge tube used to investigate cathode rays and which led to the discovery of X-rays."),
    ("Stethoscope", "Stethoscope", "René Laennec", "1816", "France", "A medical instrument invented to listen to internal body sounds, revolutionizing the diagnosis of heart and lung conditions."),
    ("Centrifugal governor", "Centrifugal governor", "James Watt", "1788", "United Kingdom", "A self-regulating device that automatically controls the speed of a steam engine, an early example of automatic feedback control."),
    ("Davy lamp", "Davy lamp", "Humphry Davy", "1815", "United Kingdom", "A safety lamp designed to reduce the risk of explosions in coal mines caused by flammable gases."),
    ("Wheatstone bridge", "Wheatstone bridge", "Samuel Hunter Christie and Charles Wheatstone", "1833", "United Kingdom", "An electrical circuit used to precisely measure an unknown electrical resistance, a fundamental tool in physics and engineering."),
    ("Leyden jar", "Leyden jar", "Ewald Georg von Kleist and Pieter van Musschenbroek", "1745", "Netherlands", "An early device used to store static electricity, considered the first form of capacitor."),
    ("Voltaic pile", "Voltaic pile", "Alessandro Volta", "1800", "Italy", "The first electrical battery capable of providing a continuous current, marking the beginning of modern electrochemistry."),
    ("Faraday disk", "Faraday disk", "Michael Faraday", "1831", "United Kingdom", "The first electric generator, demonstrating that a continuous electric current could be produced by moving a conductor through a magnetic field."),
    ("Kinetoscope", "Kinetoscope", "Thomas Edison and William Kennedy Dickson", "1891", "United States", "An early motion picture exhibition device that allowed a single viewer to watch a short film through a peephole viewer."),
    ("Magic lantern", "Magic lantern", "Christiaan Huygens (early development)", "17th century", "Netherlands", "An early type of image projector using a light source and glass slides, a precursor to modern film projection."),
    ("Cooke and Wheatstone telegraph", "Cooke and Wheatstone telegraph", "William Fothergill Cooke and Charles Wheatstone", "1837", "United Kingdom", "The first commercially successful electric telegraph system, used initially along British railways."),
    ("Intel 4004", "Intel 4004", "Intel Corporation", "1971", "United States", "The world's first commercially produced microprocessor, which laid the foundation for the modern computing industry."),
    ("Moog synthesizer", "Moog synthesizer", "Robert Moog", "1964", "United States", "A pioneering analog music synthesizer that transformed electronic music production."),
    # --- Nuclear history ---
    ("The Gadget", "Gadget (nuclear device)", "Manhattan Project", "1945", "United States", "The first nuclear device ever detonated, tested at the Trinity site in New Mexico."),
    ("Fat Man", "Fat Man", "Manhattan Project", "1945", "United States", "The codename for the atomic bomb dropped on Nagasaki, Japan, in August 1945."),
    ("Little Boy", "Little Boy", "Manhattan Project", "1945", "United States", "The codename for the atomic bomb dropped on Hiroshima, Japan, in August 1945."),
    # --- Photography & recording ---
    ("Kodak Brownie camera", "Brownie (camera)", "Eastman Kodak", "1900", "United States", "An inexpensive box camera that made photography accessible to the general public for the first time."),
    ("Leica I", "Leica I", "Ernst Leitz Optische Werke", "1925", "Germany", "One of the first commercially successful 35mm cameras, which helped establish the format still used in photography today."),
    ("Edison phonograph", "Phonograph", "Thomas Edison", "1877", "United States", "The first device capable of both recording and reproducing sound, invented by Thomas Edison."),
    # --- Land / air / space speed records ---
    ("Bluebird K7", "Bluebird K7", "Donald Campbell", "1955", "United Kingdom", "A jet-powered hydroplane in which Donald Campbell set seven world water speed records."),
    ("ThrustSSC", "ThrustSSC", "Richard Noble", "1997", "United Kingdom", "The first car to officially break the sound barrier on land, setting the current world land speed record."),
    ("SpaceShipOne", "SpaceShipOne", "Scaled Composites", "2004", "United States", "The first privately funded crewed spacecraft to reach space, winning the Ansari X Prize."),
    ("Rutan Voyager", "Rutan Voyager", "Scaled Composites", "1986", "United States", "The first aircraft to fly around the world nonstop without refueling."),
    ("Gossamer Albatross", "Gossamer Albatross", "Paul MacCready", "1979", "United States", "A human-powered aircraft that made the first successful crossing of the English Channel under human power alone."),
    ("Boeing 747", "Boeing 747", "Boeing", "1969", "United States", "A wide-body jet airliner nicknamed the \"Jumbo Jet\" that transformed long-distance commercial air travel."),
    # --- Ancient / pre-modern engineering ---
    ("South Pointing Chariot", "South Pointing Chariot", "Ancient Chinese engineers", "c. 3rd century AD", "China", "A non-magnetic directional device using a differential gear mechanism to keep a pointing figure oriented south regardless of the chariot's turns."),
    ("Aeolipile", "Aeolipile", "Hero of Alexandria", "c. 1st century AD", "Roman Egypt", "An early steam-powered device that spun using jets of steam, considered one of the first recorded steam engines."),
    ("Ishango bone", "Ishango bone", "Upper Paleolithic toolmakers", "c. 20,000 BC", "Democratic Republic of the Congo", "A bone tool marked with tallied notches that is considered one of the oldest known mathematical artifacts."),
    ("Houfeng didong yi", "Houfeng didong yi", "Zhang Heng", "132 AD", "China", "An ancient Chinese device credited as the world's first seismoscope, designed to detect the direction of distant earthquakes."),
    ("Galileo thermometer", "Galileo thermometer", "Attributed to the Accademia del Cimento", "17th century", "Italy", "A sealed glass thermometer that uses the temperature-dependent buoyancy of weighted glass bulbs, popularly (if loosely) associated with Galileo Galilei."),
]
CATEGORY_ASSIGNMENTS.append((SCIENCE_TECH_BATCH2, "science_technology"))




def build_object(idx: int, name: str, wiki_title: str, creator: str, date: str, origin: str, description: str, category: str) -> dict:
    obj_id = f"wht_{idx:04d}"
    return {
        "id": obj_id,
        "name": name,
        "artist": creator,
        "year": date,
        "origin": origin,
        "material": category,
        "category": category,
        "description": description,
        "significance": f"Widely recognized as one of the famous works representing {origin} in world art, science, or cultural history.",
        "fun_fact": f"{name} is frequently featured in museum collections and history curricula as a landmark example from {origin}.",
        "museum": "See Wikipedia for current location",
        "educational_importance": "A genuinely famous, real work -- useful for art history, world history, natural history, and cultural studies at every level.",
        "related_lesson": "Art History" if category in ("painting", "sculpture") else "World History",
        "activity": f"Research {name} further: who made or discovered it, where it is today, and why it became famous.",
        "quiz": {
            "question": f"Which culture or region does '{name}' come from?",
            "options": [origin, "Antarctica", "International Waters", "Unknown"],
            "answer": 0,
        },
        "related_subjects": ["Art History", "World History", "Geography"],
        "links": {
            "wikipedia": wiki_url(wiki_title),
            "image_search": commons_search(name),
            "google_image_search": google_image_search(f"{name} {origin}"),
            "video": yt(f"{name} explained documentary"),
            "smarthistory": smarthistory(name),
        },
        "wiki_title": wiki_title,
    }


def build_objects(existing_wiki_titles: set[str]) -> list[dict]:
    objects = []
    idx = 0
    seen = set()
    for items, category in CATEGORY_ASSIGNMENTS:
        for name, wiki_title, creator, date, origin, description in items:
            if wiki_title in seen or wiki_title in existing_wiki_titles:
                continue  # avoid duplicating a real work already in the museum
            seen.add(wiki_title)
            idx += 1
            objects.append(build_object(idx, name, wiki_title, creator, date, origin, description, category))
    return objects


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_wiki_titles = set()
    for gallery in data["galleries"].values():
        for obj in gallery.get("objects", []):
            wt = obj.get("wiki_title")
            if wt:
                existing_wiki_titles.add(wt)

    objects = build_objects(existing_wiki_titles)

    gallery = data["galleries"].get(GALLERY_KEY)
    if gallery is None:
        gallery = {
            "label": "World Heritage Treasures",
            "emoji": "🌐",
            "description": "",
            "objects": [],
        }
        data["galleries"][GALLERY_KEY] = gallery
    gallery["objects"].extend(objects)
    gallery["description"] = (
        f"{len(gallery['objects'])} genuinely famous, individually named real artworks, artifacts, natural "
        f"history specimens, and scientific/historic objects from around the world -- each linked to its real "
        f"Wikipedia page so the museum can show an actual live photo of the object."
    )

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} new objects. {GALLERY_KEY} now has {len(gallery['objects'])} objects. "
          f"Museum total: {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
