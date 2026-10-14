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
    ("world_visual_arts", "wc_0826", "Alejandro_Ciccarelli_-_Vista_de_Santiago_desde_Peñalolén.jpg", "Chile traditional painting"),
    ("world_visual_arts", "wc_0832", "Tribunales_de_Santiago_de_Chile-1900.jpg", "Chile historic photograph Santiago"),
    ("world_visual_arts", "wc_0846", "Chile_Airmail_stamp_50p_1935_issue.jpg", "Chile postage stamp art"),
    ("world_visual_arts", "wc_0851", "Along_the_River_During_the_Qingming_Festival_(Qing_Court_Version).jpg", "China traditional painting Ming Qing dynasty"),
    ("world_visual_arts", "wc_0871", "Li_Shizhen_Stamp_of_China.JPG", "China postage stamp art painting"),
    ("world_visual_arts", "wc_0876", "Serrania_de_la_Lindosa_rock_paintings_-_giant_ground_sloth_-_Iriarte_et_al_2022.jpg", "Colombia traditional painting"),
    ("world_visual_arts", "wc_0882", "Bogotazo.jpg", "Colombia historic photograph Bogota"),
    ("world_visual_arts", "wc_0932", "Museo_Nacional_de_Costa_Rica,_San_Jose_2008.jpg", "Costa Rica historic photograph San Jose"),
    ("world_visual_arts", "wc_0946", "First_postal_stamp_CR_4_Reales_1863.jpg", "Costa Rica postage stamp"),
    ("world_visual_arts", "wc_0976", "Victor_Patricio_-_Corte_de_Cana,_1874.jpg", "Cuba traditional painting"),
    ("world_visual_arts", "wc_0982", "Havana_Harbor,_Cuba_-_1898.jpg", "Cuba historic photograph Havana"),
    ("world_visual_arts", "wc_0996", "1899-Cuba-1-Centavo-Stamp.jpg", "Cuba postage stamp art"),
    ("world_visual_arts", "wc_0201", "Ferdinand_Georg_Waldmüller_-_Niederösterreichische_Bauernhochzeit_-_1122_-_Österreichische_Galerie_Belvedere.jpg", "Austria Biedermeier painting Waldmüller"),
    ("world_visual_arts", "wc_0376", "Saint_Barbara_of_Nicodemia_-_Jan_van_Eyck_-_1437.jpg", "Jan van Eyck Saint Barbara painting Belgium"),
    ("world_visual_arts", "wc_0557", "Pedro_II_of_Brazil_in_imperial_uniform_1865.jpg", "Brazil historic photograph Pedro II 19th century"),
    ("world_visual_arts", "wc_0857", "Amoy,_China;_a_husband_and_wife_by_John_Thomson,_1870-1871._Wellcome_L0056177.jpg", "John Thomson China photograph 1870s"),
    ("world_sculpture_ritual", "wc_0002", "Afghanistan,_Gandhara,_Hadda,_late_Kushan_Period_-_Seated_Buddha_-_1967.39_-_Cleveland_Museum_of_Art.jpg", "Afghanistan sculpture Gandhara Buddhist"),
    ("world_sculpture_ritual", "wc_0017", "Afghanistan,_Standing_Buddha,_Ghorband_Valley,_Fondukistan_Monastery,_7th_century.jpg", "Afghanistan religious object Buddhist Islamic"),
    ("world_sculpture_ritual", "wc_0027", "Metal_statue_from_Albanian_tourism_expo_\"Exhibit_of_Illyrian_Kings\"_depicting_Glaucias.jpg", "Albania sculpture statue"),
    ("world_sculpture_ritual", "wc_0102", "Chibinda_Ilunga_figure,_Angola,_Chokwe,_19th_century_AD,_wood,_hair,_plant_materials,_glass_beads_-_Ethnological_Museum,_Berlin_-_DSC02219.JPG", "Angola sculpture figure museum"),
    ("world_sculpture_ritual", "wc_0113", "Pwo_mask,_Angola,_Chokwe_people,_view_1,_mid_20th_century,_wood,_raffia,_twine_-_Chazen_Museum_of_Art_-_DSC01739.JPG", "Angola Chokwe mask ritual"),
    ("world_sculpture_ritual", "wc_0127", "Museo_de_Arte_Decorativo_Esculturas_del_Jardin.jpg", "Argentina sculpture statue museum"),
    ("world_sculpture_ritual", "wc_0152", "Armenian_Khatchkar.jpg", "Armenia khachkar cross stone sculpture"),
    ("world_sculpture_ritual", "wc_0177", "Aboriginal_hollow_log_tombs02.jpg", "Australia Aboriginal sculpture carving"),
    ("world_sculpture_ritual", "wc_0202", "Winged_Nike_bronze_statue_near_Kunsthistorisches_Museum_(Museum_of_Art_History)_Vienna._Austria,_Western_Europe.jpg", "Austria sculpture statue museum Vienna"),
    ("world_sculpture_ritual", "wc_0252", "WoodesRogersStatueNassau.jpg", "Bahamas sculpture statue"),
    ("world_sculpture_ritual", "wc_0292", "Barbar_temple,_Dilmun_culture,_ca._3000-2000_BCE;_Bahrain_(11).jpg", "Bahrain archaeology artifact ancient Dilmun"),
    ("world_sculpture_ritual", "wc_0302", "Kantajew_Temple-Terracotta.jpg", "Bangladesh terracotta sculpture temple"),
    ("world_sculpture_ritual", "wc_0317", "Buddha_Dhatu_Jadi_-_Bandarban_Golden_Temple.jpg", "Bangladesh religious object Buddhist Hindu"),
    ("world_sculpture_ritual", "wc_0327", "Bussa_statue.png", "Barbados sculpture statue Emancipation"),
    ("world_sculpture_ritual", "wc_0377", "Bruxelles_Manneken_Pis_cropped.jpg", "Belgium sculpture Manneken Pis Rodin"),
    ("world_sculpture_ritual", "wc_0402", "Stone_Stela,_Caana,_Caracol,_Belize.jpg", "Belize Maya sculpture stela"),
    ("world_sculpture_ritual", "wc_0427", "Royal_statues_of_Abomey_in_Quai_Branly_museum_May_2021.jpg", "Benin Dahomey royal palace Abomey sculpture"),
    ("world_sculpture_ritual", "wc_0452", "Buddha_Dordenma_Statue_and_around_–_Thimphu_during_LGFC_-_Bhutan_2019_(81).jpg", "Bhutan sculpture statue Buddha"),
    ("world_sculpture_ritual", "wc_0477", "Bolivia_-_Gate_of_the_Sun_detail_-_Tiwanaku_or_Tiahuanaco_04.jpg", "Bolivia Tiwanaku sculpture statue"),
    ("world_sculpture_ritual", "wc_0502", "Bosniangraves_bosniska_gravar_februari_2007_stecak_stecci5.jpg", "Bosnia Herzegovina stecci medieval tombstone sculpture"),
    ("world_sculpture_ritual", "wc_0552", "Aleijadinho_-_A_última_ceia_-_Santuário_do_Bom_Jesus_de_Matosinhos_-_Congonhas.jpg", "Brazil sculpture statue Aleijadinho baroque"),
    ("world_sculpture_ritual", "wc_0577", "Billionth_Barrel_Monument_-_Brunei.jpg", "Brunei sculpture monument"),
    ("world_sculpture_ritual", "wc_0602", "National_Archaeological_Museum_Sofia_-_Bronze_Head_from_the_Golyama_Kosmatka_Tumulus_near_Shipka.jpg", "Bulgaria sculpture Thracian treasure ritual"),
    ("world_sculpture_ritual", "wc_0638", "Mask_(Nyanga)_Bobo_Burkina_Faso_early_19th_century.jpg", "Burkina Faso mask museum Bwa Mossi"),
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
