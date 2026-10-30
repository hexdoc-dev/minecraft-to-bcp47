MINECRAFT_TO_BCP47: dict[str, str] = {
    "af_za": "af-ZA",  # Standard Afrikaans (South Africa)
    "ar_sa": "ar",  # Strip specific region SA as label specifies Arab World (العالم العربي) broadly
    "ast_es": "ast-ES",  # Asturian (Spain)
    "az_az": "az-Latn-AZ",  # Azerbaijani in Latin script (Azerbaijan)
    "ba_ru": "ba-RU",  # Bashkir (Russia)
    "bar": "bar",  # Bavarian (ISO 639-3 macrolanguage/individual subtag)
    "be_by": "be-BY",  # Belarusian (Belarus)
    "be_latn": "be-Latn-BY",  # Belarusian in Latin script (Łacinka)
    "bg_bg": "bg-BG",  # Bulgarian (Bulgaria)
    "br_fr": "br-FR",  # Breton (France)
    "brb": "nl-x-brabants",  # Brabantian; ISO 639-3 'brb' collides with Brao (Lave), mapped to Dutch variant
    "bs_ba": "bs-Latn-BA",  # Bosnian in Latin script (Bosnia and Herzegovina)
    "ca_es": "ca-ES",  # Catalan (Spain)
    "cs_cz": "cs-CZ",  # Czech (Czechia)
    "cv_cu": "cv-RU",  # Chuvash; replace invalid 'CU' (Cuba) placeholder for Chuvashia with 'RU'
    "cy_gb": "cy-GB",  # Welsh (United Kingdom)
    "da_dk": "da-DK",  # Danish (Denmark)
    "de_at": "de-AT",  # German (Austria)
    "de_ch": "gsw-CH",  # Swiss German (Schwiizerdutsch) uses ISO 639-3 'gsw' rather than Standard Swiss High German
    "de_de": "de-DE",  # German (Germany)
    "el_gr": "el-GR",  # Greek (Greece)
    "en_au": "en-AU",  # English (Australia)
    "en_ca": "en-CA",  # English (Canada)
    "en_gb": "en-GB",  # English (United Kingdom)
    "en_nz": "en-NZ",  # English (New Zealand)
    "en_pt": "en-x-pirate",  # Pirate Speak; replace bogus 'PT' region with private-use subtag
    "en_ud": "en-x-upsidedn",  # Upside-down English; replace bogus 'UD' region with private-use subtag
    "en_us": "en-US",  # English (United States)
    "enp": "en-x-anglish",  # Anglish; ISO 639-3 'enp' collides with Enga, use private-use subtag
    "enws": "en-emodeng",  # Shakespearean / Early Modern English via IANA registered variant 'emodeng'
    "eo_uy": "eo",  # Esperanto; strip bogus 'UY' (Uruguay / Esperantujo) region code
    "es_ar": "es-AR",  # Spanish (Argentina)
    "es_cl": "es-CL",  # Spanish (Chile)
    "es_ec": "es-EC",  # Spanish (Ecuador)
    "es_es": "es-ES",  # Spanish (Spain)
    "es_mx": "es-MX",  # Spanish (Mexico)
    "es_uy": "es-UY",  # Spanish (Uruguay)
    "es_ve": "es-VE",  # Spanish (Venezuela)
    "esan": "es-ES-x-andaluh",  # Andalusian Spanish in Andalûh orthography (non-ISO 'esan' code)
    "et_ee": "et-EE",  # Estonian (Estonia)
    "eu_es": "eu-ES",  # Basque (Spain)
    "fa_ir": "fa-IR",  # Persian (Iran)
    "fi_fi": "fi-FI",  # Finnish (Finland)
    "fil_ph": "fil-PH",  # Filipino (Philippines)
    "fo_fo": "fo-FO",  # Faroese (Faroe Islands)
    "fr_ca": "fr-CA",  # French (Canada)
    "fr_ch": "fr-CH",  # French (Switzerland)
    "fr_fr": "fr-FR",  # French (France)
    "fra_de": "vmf-DE",  # East Franconian (Fränggisch); replace colliding 'fra' (French) with ISO 639-3 'vmf'
    "fur_it": "fur-IT",  # Friulian (Italy)
    "fy_nl": "fy-NL",  # Western Frisian (Netherlands)
    "ga_ie": "ga-IE",  # Irish (Ireland)
    "gd_gb": "gd-GB",  # Scottish Gaelic (United Kingdom)
    "gl_es": "gl-ES",  # Galician (Spain)
    "go_fr": "fr-FR-gallo",  # Gallo; use IANA registered variant 'gallo' (prefix 'fr') instead of invalid 'go'
    "got_de": "got-Goth",  # Gothic in Gothic script; strip anachronistic 'DE' region
    "hal_ua": "uk-UA-x-halych",  # Halychian/Galician dialect of Ukrainian; 'hal' collides with Halang
    "haw_us": "haw-US",  # Hawaiian (United States)
    "he_il": "he-IL",  # Hebrew (Israel)
    "hi_in": "hi-IN",  # Hindi (India)
    "hn_no": "nn-NO-hognorsk",  # Høgnorsk; use IANA registered variant 'hognorsk' under Norwegian Nynorsk ('nn')
    "hr_hr": "hr-HR",  # Croatian (Croatia)
    "hu_hu": "hu-HU",  # Hungarian (Hungary)
    "hy_am": "hy-AM",  # Armenian (Armenia)
    "id_id": "id-ID",  # Indonesian (Indonesia)
    "ig_ng": "ig-NG",  # Igbo (Nigeria)
    "io_en": "io",  # Ido; strip invalid 'EN' region code
    "is_is": "is-IS",  # Icelandic (Iceland)
    "isv": "art-x-isv",  # Interslavic; pending ISO 639-3 code 'isv', use 'art' + private-use subtag
    "it_it": "it-IT",  # Italian (Italy)
    "ja_jp": "ja-JP",  # Japanese (Japan)
    "jbo_en": "jbo",  # Lojban; strip invalid 'EN' region code
    "ka_ge": "ka-GE",  # Georgian (Georgia)
    "kk_kz": "kk-KZ",  # Kazakh (Kazakhstan)
    "kn_in": "kn-IN",  # Kannada (India)
    "ko_kr": "ko-KR",  # Korean (South Korea)
    "ksh": "ksh-DE",  # Colognian / Ripuarian (Germany)
    "kw_gb": "kw-GB",  # Cornish (United Kingdom)
    "ky_kg": "ky-KG",  # Kyrgyz (Kyrgyzstan)
    "la_la": "la-VA",  # Latin; replace bogus 'LA' (Laos) region for Latium with 'VA' (or strip region)
    "lb_lu": "lb-LU",  # Luxembourgish (Luxembourg)
    "li_li": "li-NL",  # Limburgish; replace bogus 'LI' (Liechtenstein) region for Limburg with 'NL'
    "lmo": "lmo-IT",  # Lombard (Italy)
    "lo_la": "lo-LA",  # Lao (Laos)
    "lol_us": "en-x-lolcat",  # LOLCAT; replace colliding ISO 639-3 'lol' (Mongo) with English private-use variant
    "lt_lt": "lt-LT",  # Lithuanian (Lithuania)
    "lv_lv": "lv-LV",  # Latvian (Latvia)
    "lzh": "lzh-Hant",  # Literary / Classical Chinese in Traditional script
    "mk_mk": "mk-MK",  # Macedonian (North Macedonia)
    "mn_mn": "mn-Cyrl-MN",  # Mongolian in Cyrillic script (Mongolia)
    "ms_my": "ms-Latn-MY",  # Malay in Latin script (Malaysia)
    "mt_mt": "mt-MT",  # Maltese (Malta)
    "nah": "nhe-MX",  # Nahuatl; replace ISO 639-5 collective code 'nah' with primary Classical/Modern ISO 639-3 or 'ncj'/'nhn-MX'
    "nds_de": "nds-DE",  # Low German (Germany)
    "nl_be": "nl-BE",  # Dutch / Flemish (Belgium)
    "nl_nl": "nl-NL",  # Dutch (Netherlands)
    "nn_no": "nn-NO",  # Norwegian Nynorsk (Norway)
    "no_no": "nb-NO",  # Norwegian Bokmål; prefer explicit 'nb' subtag over macrolanguage 'no' per label
    "oc_fr": "oc-FR",  # Occitan (France)
    "ovd": "ovd-SE",  # Elfdalian / Övdalska (Sweden)
    "pl_pl": "pl-PL",  # Polish (Poland)
    "pls": "pls-MX",  # San Marcos Tlacoyalco Popoloca (Mexico)
    "pt_br": "pt-BR",  # Portuguese (Brazil)
    "pt_pt": "pt-PT",  # Portuguese (Portugal)
    "qcb_es": "es-ES-x-cantabru",  # Cantabrian; replace private-use ISO 639-3 'qcb' with BCP 47 private-use variant
    "qid": "id-ID-x-edjaan",  # Indonesian in Van Ophuijsen / Republikan old orthography; replace private-use 'qid'
    "qya_aa": "qya",  # Quenya; strip user-assigned placeholder region 'AA'
    "ro_ro": "ro-RO",  # Romanian (Romania)
    "rpr": "ru-petr1708",  # Pre-reform Russian via IANA registered variant 'petr1708'
    "ru_ru": "ru-RU",  # Russian (Russia)
    "ry_ua": "rue-UA",  # Rusyn (Ukraine); replace invalid 2-letter 'ry' with ISO 639-3 'rue'
    "sah_sah": "sah-RU",  # Sakha / Yakut; replace invalid 'SAH' region with 'RU'
    "se_no": "se-NO",  # Northern Sami (Norway)
    "sk_sk": "sk-SK",  # Slovak (Slovakia)
    "sl_si": "sl-SI",  # Slovenian (Slovenia)
    "so_so": "so-SO",  # Somali (Somalia)
    "sq_al": "sq-AL",  # Albanian (Albania)
    "sr_cs": "sr-Latn-RS",  # Serbian in Latin script; replace deprecated 'CS' (Serbia and Montenegro) with 'RS'
    "sr_sp": "sr-Cyrl-RS",  # Serbian in Cyrillic script; replace non-standard 'SP' region with 'RS'
    "sv_se": "sv-SE",  # Swedish (Sweden)
    "sxu": "sxu-DE",  # Upper Saxon (Germany)
    "szl": "szl-PL",  # Silesian (Poland)
    "ta_in": "ta-IN",  # Tamil (India)
    "th_th": "th-TH",  # Thai (Thailand)
    "tl_ph": "tl-PH",  # Tagalog (Philippines)
    "tlh_aa": "tlh",  # Klingon; strip user-assigned placeholder region 'AA'
    "tok": "tok",  # Toki Pona (registered ISO 639-3 code as of 2022)
    "tr_tr": "tr-TR",  # Turkish (Türkiye)
    "tt_ru": "tt-RU",  # Tatar (Russia)
    "tzo_mx": "tzo-MX",  # Tzotzil (Mexico)
    "uk_ua": "uk-UA",  # Ukrainian (Ukraine)
    "uz_uz": "uz-Latn-UZ",  # Uzbek in Latin script (Uzbekistan)
    "val_es": "ca-ES-valencia",  # Valencian via IANA registered variant 'valencia' under Catalan ('ca')
    "vec_it": "vec-IT",  # Venetian (Italy)
    "vi_vn": "vi-VN",  # Vietnamese (Vietnam)
    "vp_vl": "art-x-viossa",  # Viossa constructed pidgin; replace non-standard 'vp_vl' with 'art' + private-use subtag
    "vro": "vro-EE",  # Võro (Estonia)
    "yi_de": "yi",  # Yiddish; strip 'DE' as label specifies Ashkenazi Jews broadly rather than Germany
    "yo_ng": "yo-NG",  # Yoruba (Nigeria)
    "zh_cn": "zh-Hans-CN",  # Simplified Chinese (Mainland China)
    "zh_hk": "zh-Hant-HK",  # Traditional Chinese (Hong Kong SAR)
    "zh_tw": "zh-Hant-TW",  # Traditional Chinese (Taiwan)
    "zlm_arab": "ms-Arab-MY",  # Malay in Jawi (Arabic) script; prefer macrolanguage 'ms' per BCP 47 over 'zlm'
}
