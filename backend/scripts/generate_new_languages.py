#!/usr/bin/env python3
"""Add Bangla (bn), Hindi (hi), Urdu (ur), and Swahili (sw) to the Language
Academy: registers them in languages.json and writes vocab_<code>.json /
sentences_<code>.json, each including a "slang" category of everyday
informal expressions (clean, non-offensive) alongside the standard
greetings/numbers/family/food/common-phrases categories.

Note: Hindi already has a full grammar_hi.json; Bangla, Urdu, and Swahili
grammar files are added separately by generate_new_grammars.py.

Re-run after editing:
    python3 backend/scripts/generate_new_languages.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LANG_DIR = BASE_DIR / "data" / "language_academy"

LANGUAGE_META = [
    {
        "code": "bn", "name": "Bangla", "native": "বাংলা", "flag": "🇧🇩", "family": "Indo-Aryan",
        "speakers": "270+ million", "countries": ["Bangladesh", "India (West Bengal)"],
        "alphabet": "Bengali script (an abugida with 11 vowels and 39 consonants)",
        "description": "Bangla (Bengali) is the official language of Bangladesh and one of India's 22 scheduled languages, with a rich literary tradition including Nobel laureate Rabindranath Tagore.",
        "greeting": "নমস্কার (Nomoshkar) / আসসালামু আলাইকুম (Assalamu Alaikum)",
        "fun_fact": "Bangla has its own Language Movement Day (21 February), now recognized by UNESCO as International Mother Language Day.",
    },
    {
        "code": "hi", "name": "Hindi", "native": "हिन्दी", "flag": "🇮🇳", "family": "Indo-Aryan",
        "speakers": "600+ million", "countries": ["India", "Fiji", "Mauritius"],
        "alphabet": "Devanagari script (an abugida written left to right)",
        "description": "Hindi is one of India's official languages and, together with Urdu, forms the Hindustani language continuum spoken across South Asia.",
        "greeting": "नमस्ते (Namaste)",
        "fun_fact": "Hindi cinema (Bollywood) is one of the largest film industries in the world by number of films produced each year.",
    },
    {
        "code": "ur", "name": "Urdu", "native": "اردو", "flag": "🇵🇰", "family": "Indo-Aryan",
        "speakers": "230+ million", "countries": ["Pakistan", "India"],
        "alphabet": "Perso-Arabic script, written right to left (Nasta'liq style)",
        "description": "Urdu is the national language of Pakistan and an official language in parts of India, closely related to Hindi in everyday speech but written in Perso-Arabic script and rich in Persian and Arabic vocabulary.",
        "greeting": "السلام علیکم (Assalamu Alaikum)",
        "fun_fact": "Urdu poetry (shayari and ghazals) is a major literary art form, with poets like Mirza Ghalib still widely quoted today.",
    },
    {
        "code": "sd", "name": "Sindhi", "native": "سنڌي", "flag": "🇵🇰", "family": "Indo-Aryan",
        "speakers": "30+ million", "countries": ["Pakistan", "India"],
        "alphabet": "Perso-Arabic script in Pakistan (extended with extra letters for implosive sounds); Devanagari also used in India",
        "description": "Sindhi is spoken mainly in the Sindh province of Pakistan and by Sindhi communities in India, with a literary tradition going back over a thousand years, including the mystic poetry of Shah Abdul Latif Bhittai.",
        "greeting": "سلام (Salaam) / السلام عليڪم (Assalamu Alaikum)",
        "fun_fact": "Sindhi's script includes extra letters not found in Arabic or Urdu, created to represent implosive consonants unique to the language.",
    },
    {
        "code": "sw", "name": "Swahili", "native": "Kiswahili", "flag": "🇰🇪", "family": "Bantu",
        "speakers": "200 million", "countries": ["Tanzania", "Kenya", "Uganda", "DR Congo", "Rwanda"],
        "alphabet": "Latin script (no diacritics needed)",
        "description": "Swahili (Kiswahili) is a Bantu language and the lingua franca of East Africa, an official language of the African Union, and widely used in trade, media, and education.",
        "greeting": "Jambo / Habari?",
        "fun_fact": "Swahili has borrowed extensively from Arabic due to centuries of Indian Ocean trade, including words like 'safari' (journey) and 'chai' (tea).",
    },
]

# category -> list of (word, translation, pronunciation, example)
VOCAB = {
    "bn": {
        "greetings": [
            ("হ্যালো", "Hello", "HAY-lo", "হ্যালো, কেমন আছো?"),
            ("নমস্কার", "Greetings (formal)", "no-MOSH-kar", "নমস্কার, আপনার সাথে দেখা হয়ে ভালো লাগলো।"),
            ("আসসালামু আলাইকুম", "Peace be upon you (greeting)", "ah-sa-LAH-mu ah-LAI-kum", "আসসালামু আলাইকুম, ভাই।"),
            ("কেমন আছেন?", "How are you? (formal)", "KAY-mon AH-chen", "কেমন আছেন? আশা করি ভালো আছেন।"),
            ("কেমন আছো?", "How are you? (informal)", "KAY-mon AH-cho", "কেমন আছো, বন্ধু?"),
            ("ধন্যবাদ", "Thank you", "DHON-no-bad", "সাহায্যের জন্য ধন্যবাদ।"),
            ("দুঃখিত", "Sorry", "DUK-khi-to", "দুঃখিত, আমি দেরি করে ফেলেছি।"),
            ("বিদায়", "Goodbye", "bi-DAY", "বিদায়, আবার দেখা হবে।"),
            ("হ্যাঁ", "Yes", "hyan", "হ্যাঁ, আমি রাজি।"),
            ("না", "No", "na", "না, আমি জানি না।"),
        ],
        "numbers": [
            ("এক", "One", "ek", "আমার একটা বই আছে।"),
            ("দুই", "Two", "dui", "দুইটা আপেল দাও।"),
            ("তিন", "Three", "tin", "তিন জন ছাত্র এসেছে।"),
            ("চার", "Four", "char", "চারটা কলম আছে।"),
            ("পাঁচ", "Five", "panch", "পাঁচ মিনিট অপেক্ষা করো।"),
            ("ছয়", "Six", "chhoy", "ছয়টা বাজে।"),
            ("সাত", "Seven", "shat", "সপ্তাহে সাত দিন।"),
            ("আট", "Eight", "aat", "আটটা বাজে এখন।"),
            ("নয়", "Nine", "noy", "নয়টা কমলা কিনলাম।"),
            ("দশ", "Ten", "dosh", "দশ টাকা দাও।"),
        ],
        "family": [
            ("মা", "Mother", "ma", "আমার মা রান্না করছেন।"),
            ("বাবা", "Father", "ba-ba", "আমার বাবা অফিসে গেছেন।"),
            ("ভাই", "Brother", "bhai", "আমার ভাই স্কুলে যায়।"),
            ("বোন", "Sister", "bon", "আমার বোন গান গায়।"),
            ("দাদি", "Grandmother (paternal)", "da-di", "দাদি গল্প বলছেন।"),
            ("নানা", "Grandfather (maternal)", "na-na", "নানা বাগানে হাঁটছেন।"),
            ("ছেলে", "Son", "chhe-le", "আমার ছেলে পড়াশোনা করছে।"),
            ("মেয়ে", "Daughter", "me-ye", "আমার মেয়ে ছবি আঁকছে।"),
        ],
        "food": [
            ("ভাত", "Rice", "bhat", "আমি ভাত খাই।"),
            ("মাছ", "Fish", "mach", "মাছ ভাজা সুস্বাদু।"),
            ("ডাল", "Lentils", "dal", "ডাল ভাত খুব পুষ্টিকর।"),
            ("রুটি", "Bread/flatbread", "ru-ti", "সকালে রুটি খাই।"),
            ("পানি", "Water", "pa-ni", "এক গ্লাস পানি দাও।"),
            ("চা", "Tea", "cha", "বিকেলে চা খাই।"),
            ("মিষ্টি", "Sweets", "mish-ti", "বাংলাদেশের মিষ্টি বিখ্যাত।"),
        ],
        "common_phrases": [
            ("আপনার নাম কি?", "What is your name?", "AP-nar naam ki", "আপনার নাম কি, ভাই?"),
            ("আমি ভালো আছি", "I am fine", "A-mi bha-lo a-chi", "ধন্যবাদ, আমি ভালো আছি।"),
            ("আমি বাংলা শিখছি", "I am learning Bangla", "A-mi bang-la shik-chi", "আমি বাংলা শিখছি, এটা সুন্দর ভাষা।"),
            ("আমি বুঝতে পারছি না", "I don't understand", "A-mi bujh-te par-chi na", "দুঃখিত, আমি বুঝতে পারছি না।"),
        ],
        "slang": [
            ("দোস্ত", "Buddy/friend (informal)", "dost", "কি খবর, দোস্ত?"),
            ("মামা", "Dude/mate (informal address)", "ma-ma", "এই মামা, চল বের হই।"),
            ("জোস", "Awesome/cool (slang)", "jos", "গানটা একদম জোস হয়েছে!"),
            ("টেনশন নিস না", "Don't stress out (informal)", "TEN-shun nish na", "আরে টেনশন নিস না, সব ঠিক হয়ে যাবে।"),
        ],
    },
    "hi": {
        "greetings": [
            ("नमस्ते", "Hello / greetings", "nuh-mus-TAY", "नमस्ते, आप कैसे हैं?"),
            ("नमस्कार", "Greetings (formal)", "nuh-mus-KAAR", "नमस्कार, आपसे मिलकर खुशी हुई।"),
            ("आप कैसे हैं?", "How are you? (formal)", "aap KAI-say hain", "नमस्ते, आप कैसे हैं?"),
            ("तुम कैसे हो?", "How are you? (informal)", "toom KAI-say ho", "अरे, तुम कैसे हो?"),
            ("धन्यवाद", "Thank you", "dhun-yuh-VAAD", "मदद के लिए धन्यवाद।"),
            ("शुक्रिया", "Thanks (casual)", "shuk-ri-YAA", "शुक्रिया, बहुत अच्छा लगा।"),
            ("माफ़ करना", "Sorry / excuse me", "maaf KAR-na", "माफ़ करना, मुझे देर हो गई।"),
            ("अलविदा", "Goodbye", "al-vi-DAA", "अलविदा, फिर मिलेंगे।"),
            ("हाँ", "Yes", "haan", "हाँ, मैं तैयार हूँ।"),
            ("नहीं", "No", "nuh-HEEN", "नहीं, मुझे नहीं पता।"),
        ],
        "numbers": [
            ("एक", "One", "ek", "मेरे पास एक किताब है।"),
            ("दो", "Two", "do", "दो सेब दो।"),
            ("तीन", "Three", "teen", "तीन बजे मिलते हैं।"),
            ("चार", "Four", "chaar", "चार कुर्सियाँ हैं।"),
            ("पाँच", "Five", "paanch", "पाँच मिनट रुको।"),
            ("छह", "Six", "chhah", "छह बज गए हैं।"),
            ("सात", "Seven", "saat", "हफ्ते में सात दिन होते हैं।"),
            ("आठ", "Eight", "aath", "आठ बजे स्कूल जाता हूँ।"),
            ("नौ", "Nine", "nau", "नौ बजे सो जाओ।"),
            ("दस", "Ten", "das", "दस रुपये दो।"),
        ],
        "family": [
            ("माँ", "Mother", "maa", "मेरी माँ खाना बना रही हैं।"),
            ("पिता", "Father", "pi-TAA", "मेरे पिता दफ्तर गए हैं।"),
            ("भाई", "Brother", "bhai", "मेरा भाई स्कूल जाता है।"),
            ("बहन", "Sister", "beh-en", "मेरी बहन गाना गाती है।"),
            ("दादी", "Grandmother (paternal)", "daa-dee", "दादी कहानी सुना रही हैं।"),
            ("नाना", "Grandfather (maternal)", "naa-naa", "नाना बगीचे में टहल रहे हैं।"),
            ("बेटा", "Son", "BAY-taa", "मेरा बेटा पढ़ाई कर रहा है।"),
            ("बेटी", "Daughter", "BAY-tee", "मेरी बेटी चित्र बना रही है।"),
        ],
        "food": [
            ("चावल", "Rice", "CHAA-wal", "मुझे चावल पसंद है।"),
            ("रोटी", "Bread/flatbread", "RO-tee", "सुबह रोटी खाता हूँ।"),
            ("दाल", "Lentils", "daal", "दाल चावल बहुत स्वादिष्ट है।"),
            ("सब्ज़ी", "Vegetables", "SUB-zee", "आज कौन सी सब्ज़ी बनी है?"),
            ("पानी", "Water", "PAA-nee", "एक गिलास पानी दो।"),
            ("चाय", "Tea", "chai", "शाम को चाय पीता हूँ।"),
            ("मिठाई", "Sweets", "mi-THAI", "दिवाली पर मिठाई बाँटते हैं।"),
        ],
        "common_phrases": [
            ("आपका नाम क्या है?", "What is your name?", "AAP-ka naam kya hai", "आपका नाम क्या है, भाई?"),
            ("मैं ठीक हूँ", "I am fine", "main theek hoon", "शुक्रिया, मैं ठीक हूँ।"),
            ("मुझे हिंदी आती है", "I know Hindi", "MUJH-ay HIN-dee AA-tee hai", "मुझे थोड़ी हिंदी आती है।"),
            ("मुझे भूख लगी है", "I am hungry", "MUJH-ay bhookh LAG-ee hai", "मुझे बहुत भूख लगी है।"),
        ],
        "slang": [
            ("यार", "Buddy/dude (very common informal)", "yaar", "क्या हाल है, यार?"),
            ("बिंदास", "Carefree / totally cool", "bin-DAAS", "वो बिंदास लड़का है।"),
            ("जुगाड़", "A clever improvised fix", "joo-GAAR", "थोड़ा जुगाड़ लगाओ, काम बन जाएगा।"),
            ("मस्त", "Awesome/great (slang)", "must", "यह गाना बिल्कुल मस्त है!"),
        ],
    },
    "ur": {
        "greetings": [
            ("السلام علیکم", "Peace be upon you (greeting)", "ah-sa-LAA-mu ah-LAI-kum", "السلام علیکم، آپ کیسے ہیں؟"),
            ("وعلیکم السلام", "And peace be upon you (reply)", "wa-AY-lai-kum ah-SA-laam", "وعلیکم السلام، میں ٹھیک ہوں۔"),
            ("آداب", "A respectful greeting", "aa-DAAB", "آداب، آپ سے مل کر خوشی ہوئی۔"),
            ("آپ کیسے ہیں؟", "How are you? (formal)", "aap KAI-say hain", "آپ کیسے ہیں؟ امید ہے ٹھیک ہوں گے۔"),
            ("شکریہ", "Thank you", "shuk-ri-YAA", "آپ کی مدد کا شکریہ۔"),
            ("معاف کیجیے", "Excuse me / sorry", "ma-AAF kee-jee-ay", "معاف کیجیے، مجھے دیر ہو گئی۔"),
            ("خدا حافظ", "Goodbye", "khu-DAA HAA-fiz", "خدا حافظ، پھر ملیں گے۔"),
            ("جی ہاں", "Yes (polite)", "jee haan", "جی ہاں، میں تیار ہوں۔"),
            ("نہیں", "No", "na-HEEN", "نہیں، مجھے معلوم نہیں۔"),
        ],
        "numbers": [
            ("ایک", "One", "ek", "میرے پاس ایک کتاب ہے۔"),
            ("دو", "Two", "do", "دو سیب دو۔"),
            ("تین", "Three", "teen", "تین بجے ملتے ہیں۔"),
            ("چار", "Four", "chaar", "چار کرسیاں ہیں۔"),
            ("پانچ", "Five", "paanch", "پانچ منٹ انتظار کرو۔"),
            ("چھ", "Six", "chhay", "چھ بج گئے ہیں۔"),
            ("سات", "Seven", "saat", "ہفتے میں سات دن ہوتے ہیں۔"),
            ("آٹھ", "Eight", "aath", "آٹھ بجے اسکول جاتا ہوں۔"),
            ("نو", "Nine", "nau", "نو بجے سو جاؤ۔"),
            ("دس", "Ten", "das", "دس روپے دو۔"),
        ],
        "family": [
            ("ماں", "Mother", "maan", "میری ماں کھانا بنا رہی ہیں۔"),
            ("ابو", "Father", "AA-bu", "میرے ابو دفتر گئے ہیں۔"),
            ("بھائی", "Brother", "bhai", "میرا بھائی اسکول جاتا ہے۔"),
            ("بہن", "Sister", "beh-en", "میری بہن گانا گاتی ہے۔"),
            ("دادی", "Grandmother (paternal)", "daa-dee", "دادی کہانی سنا رہی ہیں۔"),
            ("نانا", "Grandfather (maternal)", "naa-naa", "نانا باغ میں ٹہل رہے ہیں۔"),
            ("بیٹا", "Son", "BAY-taa", "میرا بیٹا پڑھائی کر رہا ہے۔"),
            ("بیٹی", "Daughter", "BAY-tee", "میری بیٹی تصویر بنا رہی ہے۔"),
        ],
        "food": [
            ("چاول", "Rice", "CHAA-wal", "مجھے چاول پسند ہیں۔"),
            ("روٹی", "Bread/flatbread", "RO-tee", "صبح روٹی کھاتا ہوں۔"),
            ("دال", "Lentils", "daal", "دال چاول بہت مزیدار ہیں۔"),
            ("سبزی", "Vegetables", "SUB-zee", "آج کون سی سبزی بنی ہے؟"),
            ("پانی", "Water", "PAA-nee", "ایک گلاس پانی دو۔"),
            ("چائے", "Tea", "chai", "شام کو چائے پیتا ہوں۔"),
            ("مٹھائی", "Sweets", "mi-THAI", "عید پر مٹھائی بانٹتے ہیں۔"),
        ],
        "common_phrases": [
            ("آپ کا نام کیا ہے؟", "What is your name?", "AAP kaa naam kyaa hai", "آپ کا نام کیا ہے، بھائی؟"),
            ("میں ٹھیک ہوں", "I am fine", "main theek hoon", "شکریہ، میں ٹھیک ہوں۔"),
            ("مجھے اردو آتی ہے", "I know Urdu", "MUJH-ay UR-du AA-tee hai", "مجھے تھوڑی اردو آتی ہے۔"),
            ("مجھے بھوک لگی ہے", "I am hungry", "MUJH-ay bhookh LAG-ee hai", "مجھے بہت بھوک لگی ہے۔"),
        ],
        "slang": [
            ("یار", "Buddy/dude (very common informal)", "yaar", "کیا حال ہے، یار؟"),
            ("زبردست", "Awesome/excellent (informal praise)", "za-bar-DAST", "یہ فلم زبردست تھی!"),
            ("چل یار", "Come on, buddy (informal)", "chal yaar", "چل یار، دیر ہو رہی ہے۔"),
            ("مزے کی بات", "A fun/interesting thing (informal)", "MA-zay kee baat", "یہ تو مزے کی بات ہے۔"),
        ],
    },
    "sd": {
        "greetings": [
            ("سلام", "Hello", "sa-LAAM", "سلام، توهان ڪيئن آهيو؟"),
            ("السلام عليڪم", "Peace be upon you (greeting)", "ah-sa-LAA-mu ah-LAI-kum", "السلام عليڪم، مهرباني."),
            ("توهان ڪيئن آهيو؟", "How are you? (formal)", "toh-AAN KAY-yan AAH-yo", "سلام، توهان ڪيئن آهيو؟"),
            ("مهرباني", "Thank you", "meh-r-BAA-nee", "مدد لاءِ مهرباني."),
            ("معاف ڪجو", "Sorry / excuse me", "ma-AAF ka-jo", "معاف ڪجو، دير ٿي وئي."),
            ("خدا حافظ", "Goodbye", "khu-DAA HAA-fiz", "خدا حافظ، وريملنداسين."),
            ("ها", "Yes", "haa", "ها، مان تيار آهيان."),
            ("نه", "No", "na", "نه، مون کي خبر ناهي."),
        ],
        "numbers": [
            ("هڪ", "One", "hik", "مون وٽ هڪ ڪتاب آهي."),
            ("ٻه", "Two", "bay", "مون کي ٻه آم ڏي."),
            ("ٽي", "Three", "trey", "ٽي وڳي ملنداسين."),
            ("چار", "Four", "chaar", "چار ڪرسيون آهن."),
            ("پنج", "Five", "panj", "پنج منٽ ترسو."),
            ("ڇهه", "Six", "chhah", "ڇهه وڳي ٿي ويا آهن."),
            ("ست", "Seven", "sat", "هفتي ۾ ست ڏينهن هوندا آهن."),
            ("اٺ", "Eight", "ath", "اٺ وڳي اسڪول ويندو آهيان."),
            ("نو", "Nine", "nau", "نو وڳي سمهي پئو."),
            ("ڏهه", "Ten", "daha", "ڏهه رپيا ڏي."),
        ],
        "family": [
            ("امڙ", "Mother", "am-mar", "منهنجي امڙ رڌپچاءُ ڪري رهي آهي."),
            ("ابو", "Father", "AA-boo", "منهنجو ابو آفيس ويو آهي."),
            ("ڀاءُ", "Brother", "bhaa-oo", "منهنجو ڀاءُ اسڪول ويندو آهي."),
            ("ڀيڻ", "Sister", "bhen", "منهنجي ڀيڻ ڳائيندي آهي."),
            ("ڏاڏي", "Grandmother (paternal)", "daa-dee", "ڏاڏي ڪهاڻي ٻڌائي رهي آهي."),
            ("نانا", "Grandfather (maternal)", "naa-naa", "نانا باغ ۾ گھمي رهيو آهي."),
            ("پٽ", "Son", "putt", "منهنجو پٽ پڙهي رهيو آهي."),
            ("ڌيءَ", "Daughter", "dhee", "منهنجي ڌيءَ تصوير ٺاهي رهي آهي."),
        ],
        "food": [
            ("ماني", "Bread/food", "MAA-nee", "مون کي ماني کپي."),
            ("ڀت", "Rice", "bhatt", "مون کي ڀت پسند آهي."),
            ("پاڻي", "Water", "PAA-nee", "هڪ گلاس پاڻي ڏي."),
            ("چانھ", "Tea", "chaanh", "شام جو چانھ پيئندو آهيان."),
            ("ڀاڄي", "Vegetable", "BHAA-jee", "اڄ ڪهڙي ڀاڄي پچي آهي؟"),
            ("مڇي", "Fish", "MA-chhee", "مڇي مزيدار آهي."),
            ("مٺائي", "Sweets", "mi-THAA-ee", "عيد تي مٺائي ونڊيندا آهيون."),
        ],
        "common_phrases": [
            ("توهان جو نالو ڇا آهي؟", "What is your name?", "toh-AAN jo NAA-lo chhaa AAH-e", "توهان جو نالو ڇا آهي؟"),
            ("مان ٺيڪ آهيان", "I am fine", "maa-n THEEK aah-yaan", "مهرباني، مان ٺيڪ آهيان."),
            ("مون کي بک لڳي آهي", "I am hungry", "moon khe bhukh LAG-ee aah-e", "مون کي تمام بک لڳي آهي."),
            ("مون کي سنڌي اچي ٿي", "I know Sindhi", "moon khe SIN-dhee AH-che thee", "مون کي ٿوري سنڌي اچي ٿي."),
        ],
        "slang": [
            ("يار", "Buddy/dude (very common informal)", "yaar", "ڪهڙو حال آهي، يار؟"),
            ("بلڪل", "Absolutely / totally (informal emphasis)", "bil-KUL", "بلڪل صحيح چيو اٿئي!"),
            ("چڱو", "Good / nice / okay (colloquial)", "CHAN-gho", "چڱو، پوءِ ملنداسين."),
        ],
    },
    "sw": {
        "greetings": [
            ("Jambo", "Hello", "JAM-bo", "Jambo! Habari yako?"),
            ("Habari?", "How are you? / What's the news?", "ha-BA-ree", "Habari? Nzuri, asante."),
            ("Habari za asubuhi", "Good morning", "ha-BA-ree za a-su-BU-hee", "Habari za asubuhi, mwalimu."),
            ("Sijambo", "I'm fine (reply to Jambo)", "see-JAM-bo", "Sijambo, na wewe je?"),
            ("Asante", "Thank you", "a-SAN-tay", "Asante kwa msaada wako."),
            ("Asante sana", "Thank you very much", "a-SAN-tay SA-na", "Asante sana kwa chakula."),
            ("Karibu", "Welcome / you're welcome", "ka-REE-boo", "Karibu nyumbani!"),
            ("Samahani", "Sorry / excuse me", "sa-ma-HA-nee", "Samahani, nimechelewa."),
            ("Kwaheri", "Goodbye", "kwa-HEH-ree", "Kwaheri, tutaonana kesho."),
            ("Ndiyo", "Yes", "n-DEE-yo", "Ndiyo, niko tayari."),
            ("Hapana", "No", "ha-PA-na", "Hapana, sijui."),
        ],
        "numbers": [
            ("moja", "One", "MO-ja", "Nina kitabu kimoja."),
            ("mbili", "Two", "m-BEE-lee", "Nipe machungwa mawili."),
            ("tatu", "Three", "TA-too", "Tutaonana saa tatu."),
            ("nne", "Four", "N-nay", "Kuna viti vinne."),
            ("tano", "Five", "TA-no", "Ngoja dakika tano."),
            ("sita", "Six", "SEE-ta", "Ni saa sita sasa."),
            ("saba", "Seven", "SA-ba", "Wiki ina siku saba."),
            ("nane", "Eight", "NA-nay", "Naenda shule saa nane."),
            ("tisa", "Nine", "TEE-sa", "Lala saa tisa."),
            ("kumi", "Ten", "KOO-mee", "Nipe shilingi kumi."),
        ],
        "family": [
            ("mama", "Mother", "MA-ma", "Mama anapika chakula."),
            ("baba", "Father", "BA-ba", "Baba ameenda kazini."),
            ("kaka", "Brother", "KA-ka", "Kaka yangu anaenda shule."),
            ("dada", "Sister", "DA-da", "Dada yangu anaimba."),
            ("babu", "Grandfather", "BA-boo", "Babu anatembea bustanini."),
            ("bibi", "Grandmother", "BEE-bee", "Bibi anasimulia hadithi."),
            ("mtoto", "Child", "m-TO-to", "Mtoto anacheza nje."),
            ("mwana", "Son/child", "MWA-na", "Mwana wangu anasoma."),
        ],
        "food": [
            ("wali", "Rice", "WA-lee", "Ninapenda wali na samaki."),
            ("ugali", "Maize porridge (staple food)", "oo-GA-lee", "Ugali ni chakula kikuu Afrika Mashariki."),
            ("samaki", "Fish", "sa-MA-kee", "Samaki wa kukaanga ni mtamu."),
            ("nyama", "Meat", "N-ya-ma", "Ninapenda nyama choma."),
            ("maji", "Water", "MA-jee", "Nipe glasi ya maji."),
            ("chai", "Tea", "chai", "Ninakunywa chai jioni."),
            ("maziwa", "Milk", "ma-ZEE-wa", "Mtoto ananywa maziwa."),
            ("matunda", "Fruit", "ma-TOON-da", "Matunda ni mazuri kwa afya."),
        ],
        "common_phrases": [
            ("Jina lako nani?", "What is your name?", "JEE-na LA-ko NA-nee", "Jina lako nani, rafiki?"),
            ("Jina langu ni...", "My name is...", "JEE-na LAN-goo nee", "Jina langu ni Amina."),
            ("Ninatoka...", "I come from...", "nee-na-TO-ka", "Ninatoka Kenya."),
            ("Ninapenda...", "I like...", "nee-na-PEN-da", "Ninapenda muziki wa Kiswahili."),
        ],
        "slang": [
            ("Poa", "Cool / fine (very common informal reply)", "PO-a", "Habari? Poa sana!"),
            ("Mambo", "What's up (informal greeting)", "MAM-bo", "Mambo vipi, rafiki?"),
            ("Vipi", "How's it going (informal)", "VEE-pee", "Vipi, umeshindaje?"),
            ("Sawa sawa", "Okay okay / alright (informal)", "SA-wa SA-wa", "Sawa sawa, tutaonana kesho."),
            ("Bomba", "Awesome/cool (slang)", "BOM-ba", "Sherehe ilikuwa bomba!"),
        ],
    },
}

# code -> list of (target, english, category)
SENTENCES = {
    "bn": [
        ("তোমার নাম কি?", "What is your name?", "greetings"),
        ("আমার নাম রহিম।", "My name is Rahim.", "greetings"),
        ("আমি বাংলাদেশ থেকে এসেছি।", "I come from Bangladesh.", "geography"),
        ("এখন কয়টা বাজে?", "What time is it now?", "time"),
        ("আমি ক্ষুধার্ত।", "I am hungry.", "food"),
        ("এটার দাম কত?", "How much does this cost?", "shopping"),
        ("আমি তোমাকে ভালোবাসি।", "I love you.", "emotions"),
        ("দয়া করে সাহায্য করুন।", "Please help me.", "common_phrases"),
        ("আজ আবহাওয়া সুন্দর।", "The weather is nice today.", "weather"),
        ("আমি স্কুলে যাচ্ছি।", "I am going to school.", "school"),
        ("তুমি কোথায় থাকো?", "Where do you live?", "common_phrases"),
        ("এই বইটা আমার।", "This book is mine.", "school"),
    ],
    "hi": [
        ("तुम्हारा नाम क्या है?", "What is your name?", "greetings"),
        ("मेरा नाम राहुल है।", "My name is Rahul.", "greetings"),
        ("मैं भारत से हूँ।", "I am from India.", "geography"),
        ("अभी क्या समय हुआ है?", "What time is it now?", "time"),
        ("मुझे भूख लगी है।", "I am hungry.", "food"),
        ("इसकी कीमत क्या है?", "How much does this cost?", "shopping"),
        ("मैं तुमसे प्यार करता हूँ।", "I love you.", "emotions"),
        ("कृपया मेरी मदद करें।", "Please help me.", "common_phrases"),
        ("आज मौसम अच्छा है।", "The weather is nice today.", "weather"),
        ("मैं स्कूल जा रहा हूँ।", "I am going to school.", "school"),
        ("तुम कहाँ रहते हो?", "Where do you live?", "common_phrases"),
        ("यह किताब मेरी है।", "This book is mine.", "school"),
    ],
    "ur": [
        ("آپ کا نام کیا ہے؟", "What is your name?", "greetings"),
        ("میرا نام علی ہے۔", "My name is Ali.", "greetings"),
        ("میں پاکستان سے ہوں۔", "I am from Pakistan.", "geography"),
        ("ابھی کیا وقت ہوا ہے؟", "What time is it now?", "time"),
        ("مجھے بھوک لگی ہے۔", "I am hungry.", "food"),
        ("اس کی قیمت کیا ہے؟", "How much does this cost?", "shopping"),
        ("میں تم سے محبت کرتا ہوں۔", "I love you.", "emotions"),
        ("براہ کرم میری مدد کریں۔", "Please help me.", "common_phrases"),
        ("آج موسم اچھا ہے۔", "The weather is nice today.", "weather"),
        ("میں اسکول جا رہا ہوں۔", "I am going to school.", "school"),
        ("آپ کہاں رہتے ہیں؟", "Where do you live?", "common_phrases"),
        ("یہ کتاب میری ہے۔", "This book is mine.", "school"),
    ],
    "sd": [
        ("توهان جو نالو ڇا آهي؟", "What is your name?", "greetings"),
        ("منهنجو نالو علي آهي.", "My name is Ali.", "greetings"),
        ("مان پاڪستان مان آهيان.", "I am from Pakistan.", "geography"),
        ("هاڻي ڪهڙو وقت آهي؟", "What time is it now?", "time"),
        ("مون کي بک لڳي آهي.", "I am hungry.", "food"),
        ("هن جي قيمت ڪيتري آهي؟", "How much does this cost?", "shopping"),
        ("مان توهان سان پيار ڪريان ٿو.", "I love you.", "emotions"),
        ("مهرباني ڪري منهنجي مدد ڪريو.", "Please help me.", "common_phrases"),
        ("اڄ موسم سٺي آهي.", "The weather is nice today.", "weather"),
        ("مان اسڪول وڃي رهيو آهيان.", "I am going to school.", "school"),
        ("توهان ڪٿي رهو ٿا؟", "Where do you live?", "common_phrases"),
        ("هي ڪتاب منهنجو آهي.", "This book is mine.", "school"),
    ],
    "sw": [
        ("Jina lako nani?", "What is your name?", "greetings"),
        ("Jina langu ni Juma.", "My name is Juma.", "greetings"),
        ("Ninatoka Kenya.", "I come from Kenya.", "geography"),
        ("Ni saa ngapi sasa?", "What time is it now?", "time"),
        ("Nina njaa.", "I am hungry.", "food"),
        ("Hii inagharimu shilingi ngapi?", "How much does this cost?", "shopping"),
        ("Ninakupenda.", "I love you.", "emotions"),
        ("Tafadhali nisaidie.", "Please help me.", "common_phrases"),
        ("Hali ya hewa ni nzuri leo.", "The weather is nice today.", "weather"),
        ("Ninaenda shuleni.", "I am going to school.", "school"),
        ("Unaishi wapi?", "Where do you live?", "common_phrases"),
        ("Kitabu hiki ni changu.", "This book is mine.", "school"),
    ],
}


def build_vocab(code: str, language_name: str) -> dict:
    vocabulary = []
    for category, words in VOCAB[code].items():
        for word, translation, pronunciation, example in words:
            vocabulary.append({
                "word": word,
                "translation": translation,
                "pronunciation": pronunciation,
                "category": category,
                "example": example,
            })
    return {"language": language_name, "code": code, "vocabulary": vocabulary}


def build_sentences(code: str, language_name: str) -> dict:
    sentences = [{"target": t, "english": e, "category": c} for t, e, c in SENTENCES[code]]
    return {"language": language_name, "code": code, "sentences": sentences}


def main() -> None:
    lang_path = LANG_DIR / "languages.json"
    with open(lang_path, encoding="utf-8") as f:
        data = json.load(f)

    existing_codes = {l["code"] for l in data["languages"]}
    added = []
    for meta in LANGUAGE_META:
        if meta["code"] not in existing_codes:
            data["languages"].append(meta)
            added.append(meta["code"])

    with open(lang_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    for meta in LANGUAGE_META:
        code = meta["code"]
        vocab_path = LANG_DIR / f"vocab_{code}.json"
        with open(vocab_path, "w", encoding="utf-8") as f:
            json.dump(build_vocab(code, meta["name"]), f, indent=2, ensure_ascii=False)

        sentences_path = LANG_DIR / f"sentences_{code}.json"
        with open(sentences_path, "w", encoding="utf-8") as f:
            json.dump(build_sentences(code, meta["name"]), f, indent=2, ensure_ascii=False)

    print(f"Registered languages: {added or 'none new'} (all 4 vocab/sentence files (re)written).")
    print(f"Total languages in academy: {len(data['languages'])}")


if __name__ == "__main__":
    main()
