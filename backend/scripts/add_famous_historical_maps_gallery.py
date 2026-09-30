#!/usr/bin/env python3
"""Add a dedicated "Famous Historical Maps" gallery to the Virtual Museum --
a focused virtual tour of real, individually named historical map artifacts,
from the oldest known world map to the first modern national survey.

Each entry has a real, verifiable wiki_title (so the existing WikiThumbnail
component fetches a genuine live photo from Wikipedia's REST API) and a real
holding institution in `museum`, which powers the existing virtual_tour /
google_image_search backfill scripts (add_museum_virtual_tours.py,
add_museum_google_image_links.py) -- re-run those after this script.

A few of these same real maps also appear individually inside the larger
"Famous Masterpieces" gallery; that's expected curatorial overlap (the same
real artifact can legitimately be featured in more than one themed
collection), not a data error.

Re-run after editing:
    python3 backend/scripts/add_famous_historical_maps_gallery.py
    python3 backend/scripts/add_museum_virtual_tours.py
    python3 backend/scripts/add_museum_google_image_links.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def smarthistory(q: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(q)


# (name, wiki_title, origin, period, museum, description, significance, fun_fact)
MAPS = [
    (
        "Babylonian Map of the World",
        "Babylonian Map of the World",
        "Mesopotamia (Babylon)",
        "c. 700–500 BCE",
        "British Museum, London",
        "A small clay tablet (Imago Mundi) showing Babylon at the centre of a circular world, surrounded by a ring of ocean and eight outer regions.",
        "The oldest known map of the world to survive from antiquity, revealing how the Babylonians conceived of the world's shape and their own place at its centre.",
        "The tablet is only about the size of a hand, yet it is one of the most studied objects in the history of cartography.",
    ),
    (
        "Map of Nippur",
        "Nippur",
        "Kassite Babylonia (Mesopotamia)",
        "c. 1300 BCE",
        "Hilprecht Collection of Babylonian Antiquities, University of Jena, Germany",
        "A Kassite-period clay tablet depicting the city of Nippur in Mesopotamia, showing its city walls, gates, temples, canals, and gardens in schematic plan view.",
        "Widely regarded as the oldest known map of a single city, rather than the wider world — a rare window into how an ancient civilization recorded its own urban space.",
        "The tablet even labels specific features such as the temple of Enlil and the city's irrigation canals, making it remarkably legible as a city plan more than 3,000 years later.",
    ),
    (
        "Turin Papyrus Map",
        "Turin Papyrus Map",
        "Ancient Egypt (New Kingdom)",
        "c. 1160 BCE",
        "Museo Egizio, Turin, Italy",
        "A papyrus map of a gold-mining region in Egypt's Eastern Desert near Wadi Hammamat, marking mountains, roads, miners' huts, and a temple to the god Amun.",
        "Considered the oldest surviving geological and topographic map from the ancient world, drawn to help plan a real royal quarrying and mining expedition.",
        "Unlike many ancient maps made for symbolic or religious purposes, this one was a working document used to organize an actual state expedition.",
    ),
    (
        "Forma Urbis Romae",
        "Forma Urbis Romae",
        "Roman Empire (city of Rome)",
        "c. 203–211 CE",
        "Museo della Civiltà Romana, Rome, Italy",
        "A giant marble map of ancient Rome carved at a scale of roughly 1:240, once covering an entire wall inside the Temple of Peace and showing the ground-plan of every building in the city.",
        "The most detailed map of any city to survive from antiquity, giving archaeologists a uniquely precise record of ancient Rome's streets and buildings.",
        "Only a small fraction of the original marble map survives today, in over a thousand fragments that scholars are still working to piece back together.",
    ),
    (
        "Mawangdui Silk Maps",
        "Mawangdui",
        "Han Dynasty China (Changsha Kingdom)",
        "c. 168 BCE",
        "Hunan Museum, Changsha, China",
        "Silk maps excavated from the Mawangdui Han-dynasty tombs, including a detailed topographic map of the Changsha region and a military map showing troop garrison positions.",
        "Among the oldest surviving maps from China, demonstrating remarkably advanced surveying and map-making skill over 2,000 years ago.",
        "The topographic map correctly shows the region's river systems and mountain ranges with an accuracy that surprised modern cartographers when it was rediscovered in 1973.",
    ),
    (
        "Bedolina Map",
        "Bedolina Map",
        "Prehistoric Italy (Camonica Valley)",
        "c. 2nd–1st millennium BCE",
        "In situ at Naquane National Park, Capo di Ponte, Italy (Rock Drawings in Valcamonica UNESCO World Heritage Site)",
        "A large prehistoric petroglyph carved into rock, depicting fields, paths, houses, and figures in a schematic bird's-eye layout of an inhabited valley landscape.",
        "One of the oldest surviving examples of a map showing an inhabited landscape from above, offering a rare window into how prehistoric Alpine communities understood their own territory.",
        "The carving was added to over many centuries by different generations, layering together views of the same valley landscape from different time periods.",
    ),
    (
        "Ptolemy's Geographia",
        "Geography (Ptolemy)",
        "Roman Egypt (Alexandria)",
        "c. 150 CE",
        "Vatican Library (a notable surviving Byzantine manuscript copy)",
        "Claudius Ptolemy's treatise set out a coordinate system of latitude and longitude for mapping the known world, along with instructions for map projections.",
        "Its coordinate-grid approach shaped Western cartography for over a thousand years and directly inspired Renaissance-era world maps, including Waldseemüller's.",
        "Ptolemy's original maps are lost entirely — every map we associate with the Geographia today is a later reconstruction drawn from his written coordinates.",
    ),
    (
        "Tabula Peutingeriana",
        "Tabula Peutingeriana",
        "Roman Empire",
        "Medieval copy of a 4th/5th-century Roman original",
        "Austrian National Library, Vienna",
        "A schematic strip map of the Roman road network (the cursus publicus), stretching from Britain and Iberia in the west to India in the east on a long narrow scroll.",
        "One of the only surviving maps to show the full extent of the Roman road system, giving historians a unique view of how the Empire connected its territories.",
        "The surviving copy is over 6.75 metres long but only about 34 centimetres tall, distorting geography to fit the scroll format.",
    ),
    (
        "Cotton Mappa Mundi",
        "Cotton Mappa Mundi",
        "Anglo-Saxon England",
        "c. 1025–1050",
        "British Library, London",
        "An Anglo-Saxon world map, one of the earliest surviving European maps to show recognisable landmasses rather than purely symbolic shapes.",
        "Predates the more famous Hereford Mappa Mundi by roughly 250 years, offering a rare window into pre-Norman English geographic knowledge.",
        "It's bound into a manuscript alongside a poem and other texts, rather than existing as a standalone map — a reminder that medieval maps were often part of larger books.",
    ),
    (
        "Tabula Rogeriana",
        "Tabula Rogeriana",
        "Norman Sicily / Islamic world",
        "1154",
        "Bodleian Library, Oxford (a surviving manuscript copy)",
        "Created by Arab geographer Muhammad al-Idrisi for the Norman King Roger II of Sicily, combining Islamic, classical, and contemporary sailors' knowledge into one of the most accurate world maps of its time.",
        "Considered one of the most advanced world maps of the medieval period, remaining a key geographic reference in Europe for centuries.",
        "Al-Idrisi drew the map with south at the top, a common convention in medieval Islamic cartography, the reverse of most maps today.",
    ),
    (
        "Hereford Mappa Mundi",
        "Hereford Mappa Mundi",
        "England",
        "c. 1300",
        "Hereford Cathedral, England",
        "The largest surviving medieval map, a \"T-O\" style map centred on Jerusalem and filled with hundreds of illustrations of biblical events, mythical creatures, and known cities.",
        "A landmark of medieval European cartography, showing how map-making, religion, and mythology were deeply intertwined before the Age of Exploration.",
        "It's drawn on a single sheet of vellum (calfskin) measuring about 1.6 by 1.35 metres, and is still displayed at Hereford Cathedral today.",
    ),
    (
        "Waldseemüller Map",
        "Waldseemüller map",
        "Germany",
        "1507",
        "Library of Congress, Washington D.C.",
        "The first map to use the name \"America\" for the New World, created by German cartographer Martin Waldseemüller based on the voyages of Amerigo Vespucci.",
        "Often called \"America's birth certificate\", it's the first document to give the continent its modern name.",
        "The U.S. Library of Congress purchased its only surviving complete copy in 2003 for $10 million, the highest price ever paid for a single map at the time.",
    ),
    (
        "Cantino Planisphere",
        "Cantino planisphere",
        "Portugal",
        "1502",
        "Biblioteca Estense, Modena, Italy",
        "An early Portuguese world map smuggled to Italy by an agent named Alberto Cantino, showing the results of Portuguese exploration including the coast of Brazil.",
        "One of the earliest surviving maps to depict the line dividing Spanish and Portuguese claims under the 1494 Treaty of Tordesillas.",
        "The map was commissioned as an act of espionage — Portugal guarded its exploration discoveries closely, so acquiring a copy required secrecy.",
    ),
    (
        "Piri Reis Map",
        "Piri Reis map",
        "Ottoman Empire (Turkey)",
        "1513",
        "Topkapı Palace Museum, Istanbul",
        "A world map drawn by Ottoman admiral and cartographer Piri Reis, compiling roughly 20 older source maps, including some said to trace back to Columbus's own charts.",
        "Renowned for its unusually accurate depiction of the Atlantic coastlines of Europe, Africa, and South America for such an early date.",
        "Only a fragment of the original map survives, covering the Atlantic Ocean, West Africa, and the eastern coast of South America.",
    ),
    (
        "Fra Mauro Map",
        "Fra Mauro map",
        "Republic of Venice, Italy",
        "c. 1450",
        "Biblioteca Marciana, Venice",
        "A large, richly detailed circular world map created by the Venetian monk Fra Mauro, drawing on merchant and traveller accounts from across Europe and Asia.",
        "Considered one of the greatest achievements of medieval cartography, remarkably accurate for its era and notably free of many earlier religious/mythical distortions.",
        "Unusually for its time, the map is oriented with south at the top, and it was among the first European maps to suggest ships could sail around Africa to reach Asia.",
    ),
    (
        "Mercator World Map (1569)",
        "Mercator 1569 world map",
        "Flanders (modern Belgium)",
        "1569",
        "Bibliothèque nationale de France, Paris",
        "Gerardus Mercator's landmark world map introduced the Mercator projection, designed so sailors could plot a straight compass-bearing course across the curved Earth.",
        "The Mercator projection became the standard for nautical charts for centuries and is still the basis of most web mapping tools, including Google Maps, today.",
        "Only a handful of complete original copies of the 1569 map are known to survive anywhere in the world.",
    ),
    (
        "Cassini Map of France",
        "Cassini map",
        "France",
        "Completed 1789",
        "Bibliothèque nationale de France, Paris",
        "The first map of an entire country based on precise triangulated survey, produced across four generations of the Cassini family of astronomers and cartographers.",
        "A foundational achievement in scientific cartography, establishing the survey methods that national mapping agencies still build on today.",
        "The full project took over 70 years to complete and used more than 800 individually surveyed triangulation points across France.",
    ),
]


def build_map_object(idx: int, name: str, wiki_title: str, origin: str, period: str, museum: str, description: str, significance: str, fun_fact: str) -> dict:
    return {
        "id": f"map_{idx:03d}",
        "name": name,
        "origin": origin,
        "period": period,
        "museum": museum,
        "category": "map",
        "description": description,
        "significance": significance,
        "fun_fact": fun_fact,
        "related_subjects": ["World History", "Geography"],
        "links": {
            "wikipedia": wiki_url(wiki_title),
            "image_search": commons_search(name),
            "video": yt(f"{name} history cartography documentary"),
            "explanation_video": yt(f"{name} explained history"),
            "smarthistory": smarthistory(name),
        },
        "wiki_title": wiki_title,
    }


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    objects = [build_map_object(i + 1, *entry) for i, entry in enumerate(MAPS)]

    data["galleries"]["famous_historical_maps"] = {
        "label": "Famous Historical Maps",
        "emoji": "🗺️",
        "description": (
            f"A virtual tour of {len(objects)} real, individually named historical maps — from the oldest surviving "
            f"world map to the first fully surveyed map of a modern nation — spanning ancient Mesopotamia to the "
            f"Age of Exploration and beyond. Pairs well with the World History Atlas in Countries Explorer."
        ),
        "objects": objects,
    }

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} famous historical maps. Museum now has {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
