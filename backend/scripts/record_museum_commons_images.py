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
    ("world_visual_arts", "wc_0357", "Belarus-Hrodna-New_and_Old_Castles-1.jpg", "Belarus historic photograph"),
    ("world_visual_arts", "wc_0371", "1998._Stamp_of_Belarus_0296.jpg", "Belarus postage stamp art"),
    ("world_visual_arts", "wc_0382", "Belgische_Monarchen.jpg", "Belgium historic photograph"),
    ("world_visual_arts", "wc_0396", "Timbre_Belgique_Leopold2_1905.jpg", "Belgium postage stamp art"),
    ("world_visual_arts", "wc_0407", "BelmopanParliament75.jpg", "Belize historic photograph"),
    ("world_visual_arts", "wc_0432", "Entrée_de_la_Grande_Mosquée_de_Porto-Novo_au_Bénin.jpg", "Cotonou Porto-Novo Benin historic photograph"),
    ("world_visual_arts", "wc_0451", "Bhutanese_painted_thanka_of_the_Jataka_Tales,_18th-19th_Century,_Phajoding_Gonpa,_Thimphu,_Bhutan.jpg", "Bhutan thangka painting"),
    ("world_visual_arts", "wc_0457", "Punakha_Dzong,_1637-38,_Bhutan_(3)_(29317483137).jpg", "Bhutan historic photograph"),
    ("world_visual_arts", "wc_0471", "Stamp_1968_Bhutan_mt_B002a.jpg", "Bhutan postage stamp"),
    ("world_visual_arts", "wc_0476", "The_House_at_Nazareth,_Late_18th_century._Artist_unknown,_Bolivian.jpg", "Bolivia traditional painting"),
    ("world_visual_arts", "wc_0482", "Church_in_Historic_Center_-_Sucre_-_Bolivia.jpg", "Bolivia historic photograph"),
    ("world_visual_arts", "wc_0496", "Stamp_of_Bolivia_-_1925_-_Colnect_226997_-_National_flower_kantuta.jpeg", "Bolivia postage stamp art"),
    ("world_visual_arts", "wc_0501", "Bosnia_&_Herzegovina_Pavilion_by_Alphonse_Mucha,_1900.jpg", "Bosnia and Herzegovina traditional painting"),
    ("world_visual_arts", "wc_0507", "Sarajevo_krajem_XIX_vijeka.jpg", "Bosnia Herzegovina historic photograph Sarajevo"),
    ("world_visual_arts", "wc_0521", "1903_Bosnie_35h_Telsic.jpg", "Bosnia Herzegovina postage stamp art"),
    ("world_visual_arts", "wc_0526", "Giraffe_Rock_Art_Painting_Tsodilo.jpg", "Botswana painting"),
    ("world_visual_arts", "wc_0532", "Royal_Visit_to_Lobatse,_Bechuanaland,_now_Botswana_(1947).jpg", "Botswana historic photograph"),
    ("world_visual_arts", "wc_0546", "Botswana_stamp_type_A11aa.jpg", "Botswana postage stamp"),
    ("world_visual_arts", "wc_0551", "A_Brazilian_family_in_Rio_de_Janeiro_by_Jean-Baptiste_Debret_1839.jpg", "Brazil traditional painting"),
    ("world_visual_arts", "wc_0571", "José_Rodrigues_de_Carvalho_1967_Brazil_stamp.jpg", "Brazil postage stamp art"),
    ("world_visual_arts", "wc_0582", "Brunei_Town_in_1950.jpg", "Brunei historic photograph"),
    ("world_visual_arts", "wc_0601", "Orthodox_Bulgarian_icon_of_St._George_fighting_the_dragon.jpg", "Bulgaria traditional painting icon"),
    ("world_visual_arts", "wc_0607", "Photograph_of_Sofia,_Bulgaria,_c_1881.jpg", "Bulgaria historic photograph Sofia"),
    ("world_visual_arts", "wc_0621", "The_First_Bulgarian_Stamps_May_1,_1879.JPG", "Bulgaria postage stamp art"),
    ("world_visual_arts", "wc_0632", "BF-Ouaga-Entrée_du_Palais_du_Mogho_Naaba_(Roi).jpg", "Burkina Faso historic photograph"),
    ("world_visual_arts", "wc_0657", "View_of_bujumbura.JPG", "Burundi historic photograph"),
    ("world_visual_arts", "wc_0671", "Stamp_1968_BDI_Airmail_MiNr0442A_pm_B002.jpg", "Burundi postage stamp"),
    ("world_visual_arts", "wc_0682", "Nakhon_Thom,_Cambodia._Photograph_by_John_Thomson,_1866._Wellcome_L0056121.jpg", "Cambodia historic photograph"),
    ("world_visual_arts", "wc_0707", "Bundesarchiv_Bild_163-271,_Kamerun,_bei_Duala,_Einheimische_vor_Hütte.jpg", "Cameroon historic photograph"),
    ("world_visual_arts", "wc_0721", "D-Kamerun_1900_12.jpg", "Cameroon postage stamp"),
    ("world_visual_arts", "wc_0726", "The_Jack_Pine,_by_Tom_Thomson.jpg", "Canada Group of Seven painting"),
    ("world_visual_arts", "wc_0732", "Montreal_Lacrosse_Club_1867.jpg", "Canada historic photograph 19th century"),
    ("world_visual_arts", "wc_0746", "3_pence_beaver_stamp.jpg", "Canada postage stamp art"),
    ("world_visual_arts", "wc_0782", "Central_African_Republic_-_Boy_in_Birao.jpg", "Central African Republic historic photograph"),
    ("world_visual_arts", "wc_0801", "Prehistoric_Rock_Paintings_at_Manda_Guéli_Cave_in_the_Ennedi_Mountains_-_northeastern_Chad_2015.jpg", "Chad traditional art historic photograph"),
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
