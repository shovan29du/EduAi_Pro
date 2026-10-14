#!/usr/bin/env python3
"""Record manually-verified Wikimedia Commons images for Virtual Museum
objects that had no image mechanism at all (see
add_museum_images_from_alternate_sources.py for the automated version of
this, blocked from running in this session by network policy).

Each entry here was found via a live WebSearch restricted to
commons.wikimedia.org, reading the exact file title directly from the
result's URL (not guessed), for the specific country+category object it's
attached to. Matches that weren't confidently on-topic were skipped rather
than attached -- see the skip notes in the batch's run log.

MATCHES: list of (gallery_id, object_id, exact_commons_filename, source_query)

Re-run after adding more entries to MATCHES:
    python3 backend/scripts/record_museum_commons_images.py
"""
from __future__ import annotations

import json
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"

MATCHES: list[tuple[str, str, str, str]] = [
    ("world_visual_arts", "wc_0001", "Portrait_of_Ahmad_Shah_Durrani.jpg", "Afghanistan traditional painting"),
    ("world_visual_arts", "wc_0007", "Old_men_of_Herat,_Afghanistan.jpg", "Afghanistan historic photograph"),
    ("world_visual_arts", "wc_0021", "Stamp_of_Afghanistan_-_1964_-_Colnect_354797_-_Snow_Leopard_Panthera_uncia.jpeg", "Afghanistan print art"),
    ("world_visual_arts", "wc_0026", "The_Albanian_Girl_(1831_painting).jpg", "Albania traditional painting"),
    ("world_visual_arts", "wc_0032", "Albania_in_1912.jpg", "Albania historic photograph"),
    ("world_visual_arts", "wc_0051", "Pierre-Auguste_Renoir_-_Algerian_Girl_-_Google_Art_Project.jpg", "Algeria traditional painting"),
    ("world_visual_arts", "wc_0057", "Indépendance_day-Algeria.jpg", "Algeria historic photograph"),
    ("world_visual_arts", "wc_0046", "Stamp_of_Albania_-_1973_-_Colnect_354082_-_Narcissus_by_Caravaggio.jpeg", "Albania postage stamp art"),
    ("world_visual_arts", "wc_0071", "Stamp_of_Algeria_-_1965_-_Colnect_325136_-_Algerian_princess_and_antelope.jpeg", "Algeria postage stamp art"),
    ("world_visual_arts", "wc_0082", "Vista_de_Andorra_la_Vieja,_Andorra,_2013-12-30,_DD_01.JPG", "Andorra historic photograph"),
    ("world_visual_arts", "wc_0101", "Pedro_Alvares_de_Andrade_-_Capitão-General_do_Reino_de_Angola.png", "Angola traditional painting"),
    ("world_visual_arts", "wc_0107", "António_Agostinho_Neto.jpg", "Angola historic photograph"),
    ("world_visual_arts", "wc_0126", "Paintings-Handprint-Cueva-de-las-Manos-Argentina.webp", "Argentina traditional painting"),
    ("world_visual_arts", "wc_0132", "Buenos_Aires_1915.jpg", "Argentina historic photograph"),
    ("world_visual_arts", "wc_0146", "1888_50C_Argentina_Mitre_Mi62_Yv71.jpg", "Argentina postage stamp art"),
    ("world_visual_arts", "wc_0151", "ArmenianWomen-Hagop_Hovnatanian.jpg", "Armenia traditional painting"),
    ("world_visual_arts", "wc_0157", "Armenian_Genocide_Memorial_-_Yerevan_(2903021240).jpg", "Armenia historic photograph"),
    ("world_visual_arts", "wc_0171", "Martiros_Saryan_painting_2005_Armenian_stamp.jpg", "Armenia postage stamp art"),
    ("world_visual_arts", "wc_0176", "Australie_Aborigene_ancetre_totemique_kangourou.jpg", "Australia Aboriginal painting"),
    ("world_visual_arts", "wc_0196", "Australia_1974_4_Dollar_Stamp_Shearing_the_Rams,_by_Tom_Roberts_AU_566b.jpg", "Australia postage stamp art"),
    ("world_visual_arts", "wc_0207", "1906-History-Austria-Classic-Hotel-Wien-Vienna.jpg", "Austria historic photograph Vienna"),
    ("world_visual_arts", "wc_0221", "Austria_specimen_telegraph_stamps.JPG", "Austria postage stamp art painting"),
    ("world_visual_arts", "wc_0232", "Members_of_the_Parliament_of_the_Azerbaijan_Democratic_Republic_(1920).jpg", "Azerbaijan historic photograph"),
    ("world_visual_arts", "wc_0246", "The_Soviet_Union_1990_CPA_6249_stamp_(Azerbaijani_balaban,_nagara,_tar,_saz_and_zurna)_small_resolution.jpg", "Azerbaijan postage stamp art"),
    ("world_visual_arts", "wc_0251", "Winslow_Homer_-_After_the_Hurricane,_Bahamas.jpg", "Bahamas painting"),
    ("world_visual_arts", "wc_0257", "Grand_bahama.jpg", "Bahamas historic photograph"),
    ("world_visual_arts", "wc_0282", "Manama_(40513813472).jpg", "Bahrain historic photograph Manama"),
    ("world_visual_arts", "wc_0301", "Woman_painting_traditional_Bengali_art_,_Patachitra.jpg", "Bangladesh traditional painting"),
    ("world_visual_arts", "wc_0307", "Archeological_picture_of_Ahsan_Manzil,_Dhaka,_Bangladesh.jpg", "Bangladesh historic photograph"),
    ("world_visual_arts", "wc_0321", "Bangladesh_stamp_type_BB6.jpg", "Bangladesh postage stamp art"),
    ("world_visual_arts", "wc_0326", "Isaac_Sailmaker_-_The_Island_of_Barbados_-_Google_Art_Project.jpg", "Barbados painting"),
    ("world_visual_arts", "wc_0332", "Holetown_Monument_plaque,_Saint_James,_Barbados-1.jpg", "Barbados historic photograph"),
    ("world_visual_arts", "wc_0346", "Barbados_Postcard.JPG", "Barbados postage stamp"),
]


def commons_file_path_url(filename: str) -> str:
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(filename)


def main() -> None:
    data = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    galleries = data["galleries"]

    updated = 0
    for gid, oid, filename, query in MATCHES:
        objs = galleries[gid]["objects"]
        match = next((o for o in objs if o["id"] == oid), None)
        if match is None:
            print(f"WARNING: {gid}/{oid} not found, skipping")
            continue
        match["thumbnail_local"] = commons_file_path_url(filename)
        match["image_source"] = "wikimedia_commons"
        match["image_source_url"] = f"https://commons.wikimedia.org/wiki/File:{urllib.parse.quote(filename)}"
        match["image_found_via_query"] = query
        updated += 1

    MUSEUM_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {updated} object(s) with real Wikimedia Commons images.")


if __name__ == "__main__":
    main()
