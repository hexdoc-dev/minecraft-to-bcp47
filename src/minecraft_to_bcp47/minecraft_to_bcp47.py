MINECRAFT_TO_BCP47: dict[str, str] = {
    "af_za": "af-ZA",  # ISO 639-1 af (Afrikaans) + ISO 3166-1 ZA (South Africa)
    "ar_sa": "ar-SA",  # ISO 639-1 ar (Arabic) + nominal region SA (Saudi Arabia)
    "ast_es": "ast-ES",  # ISO 639-3 ast (Asturian) + ES (Spain)
    "az_az": "az-AZ",  # ISO 639-1 az (Azerbaijani) + AZ (Azerbaijan); Latn suppressed
    "ba_ru": "ba-RU",  # ISO 639-1 ba (Bashkir) + RU (Russia)
    "bar": "bar",  # ISO 639-3 bar (Bavarian)
    "be_by": "be-BY",  # ISO 639-1 be (Belarusian, Cyrillic) + BY (Belarus)
    "be_latn": "be-Latn",  # ISO 639-1 be + ISO 15924 script Latn (Belarusian Lacinka)
    "bg_bg": "bg-BG",  # ISO 639-1 bg (Bulgarian) + BG (Bulgaria)
    "br_fr": "br-FR",  # ISO 639-1 br (Breton) + FR (France)
    "brb": "nl-x-brabant",  # Avoids ISO 639-3 brb (Lave) collision; Dutch + private-use Brabantian
    "bs_ba": "bs-BA",  # ISO 639-1 bs (Bosnian) + BA (Bosnia and Herzegovina)
    "ca_es": "ca-ES",  # ISO 639-1 ca (Catalan) + ES (Spain)
    "cs_cz": "cs-CZ",  # ISO 639-1 cs (Czech) + CZ (Czechia)
    "cv_cu": "cv",  # ISO 639-1 cv (Chuvash); stripped bogus CU (Cuba) region
    "cy_gb": "cy-GB",  # ISO 639-1 cy (Welsh) + GB (United Kingdom)
    "da_dk": "da-DK",  # ISO 639-1 da (Danish) + DK (Denmark)
    "de_at": "de-AT",  # ISO 639-1 de (German) + AT (Austria)
    "de_ch": "gsw-CH",  # ISO 639-3 gsw (Swiss German / Schwiizerdutsch) + CH (Switzerland)
    "de_de": "de-DE",  # ISO 639-1 de (German) + DE (Germany)
    "el_gr": "el-GR",  # ISO 639-1 el (Modern Greek) + GR (Greece)
    "en_au": "en-AU",  # ISO 639-1 en (English) + AU (Australia)
    "en_ca": "en-CA",  # ISO 639-1 en (English) + CA (Canada)
    "en_gb": "en-GB",  # ISO 639-1 en (English) + GB (United Kingdom)
    "en_nz": "en-NZ",  # ISO 639-1 en (English) + NZ (New Zealand)
    "en_pt": "en-x-pirate",  # Joke English variant with private-use subtag; bogus PT stripped
    "en_ud": "en-x-upside",  # Joke upside-down English variant with private-use subtag; invalid UD stripped
    "en_us": "en-US",  # ISO 639-1 en (English) + US (United States)
    "enp": "en-x-anglish",  # Avoids ISO 639-3 enp (Northern Paiute) collision; English + private-use Anglish
    "enws": "en-emodeng",  # ISO 639-1 en + IANA registered variant emodeng (Early Modern English)
    "eo_uy": "eo",  # ISO 639-1 eo (Esperanto); stripped bogus UY (Uruguay) region
    "es_ar": "es-AR",  # ISO 639-1 es (Spanish) + AR (Argentina)
    "es_cl": "es-CL",  # ISO 639-1 es (Spanish) + CL (Chile)
    "es_ec": "es-EC",  # ISO 639-1 es (Spanish) + EC (Ecuador)
    "es_es": "es-ES",  # ISO 639-1 es (Spanish) + ES (Spain)
    "es_mx": "es-MX",  # ISO 639-1 es (Spanish) + MX (Mexico)
    "es_uy": "es-UY",  # ISO 639-1 es (Spanish) + UY (Uruguay)
    "es_ve": "es-VE",  # ISO 639-1 es (Spanish) + VE (Venezuela)
    "esan": "es-ES-x-andaluh",  # Invalid 4-letter primary subtag replaced with es-ES + private-use Andaluh
    "et_ee": "et-EE",  # ISO 639-1 et (Estonian) + EE (Estonia)
    "eu_es": "eu-ES",  # ISO 639-1 eu (Basque) + ES (Spain)
    "fa_ir": "fa-IR",  # ISO 639-1 fa (Persian) + IR (Iran)
    "fi_fi": "fi-FI",  # ISO 639-1 fi (Finnish) + FI (Finland)
    "fil_ph": "fil-PH",  # ISO 639-3 fil (Filipino) + PH (Philippines)
    "fo_fo": "fo-FO",  # ISO 639-1 fo (Faroese) + FO (Faroe Islands)
    "fr_ca": "fr-CA",  # ISO 639-1 fr (French) + CA (Canada)
    "fr_ch": "fr-CH",  # ISO 639-1 fr (French) + CH (Switzerland)
    "fr_fr": "fr-FR",  # ISO 639-1 fr (French) + FR (France)
    "fra_de": "vmf-DE",  # Replaces fra (French) collision with ISO 639-3 vmf (Main-Franconian) + DE
    "fur_it": "fur-IT",  # ISO 639-3 fur (Friulian) + IT (Italy)
    "fy_nl": "fy-NL",  # ISO 639-1 fy (Western Frisian) + NL (Netherlands)
    "ga_ie": "ga-IE",  # ISO 639-1 ga (Irish) + IE (Ireland)
    "gd_gb": "gd-GB",  # ISO 639-1 gd (Scottish Gaelic) + GB (United Kingdom)
    "gl_es": "gl-ES",  # ISO 639-1 gl (Galician) + ES (Spain)
    "go_fr": "fr-FR-x-gallo",  # Invalid primary subtag go replaced with fr-FR + private-use Gallo
    "got_de": "got",  # ISO 639-3 got (Gothic); stripped anachronistic DE region; Goth script suppressed
    "hal_ua": "uk-UA-x-halych",  # Avoids ISO 639-3 hal (Halang) collision; uk-UA + private-use Halychian
    "haw_us": "haw-US",  # ISO 639-3 haw (Hawaiian) + US (United States)
    "he_il": "he-IL",  # ISO 639-1 he (Hebrew) + IL (Israel)
    "hi_in": "hi-IN",  # ISO 639-1 hi (Hindi) + IN (India)
    "hn_no": "nn-NO-hognorsk",  # Invalid hn replaced with nn-NO + IANA registered variant hognorsk
    "hr_hr": "hr-HR",  # ISO 639-1 hr (Croatian) + HR (Croatia)
    "hu_hu": "hu-HU",  # ISO 639-1 hu (Hungarian) + HU (Hungary)
    "hy_am": "hy-AM",  # ISO 639-1 hy (Armenian) + AM (Armenia)
    "id_id": "id-ID",  # ISO 639-1 id (Indonesian) + ID (Indonesia)
    "ig_ng": "ig-NG",  # ISO 639-1 ig (Igbo) + NG (Nigeria)
    "io_en": "io",  # ISO 639-1 io (Ido); stripped invalid EN region code
    "is_is": "is-IS",  # ISO 639-1 is (Icelandic) + IS (Iceland)
    "isv": "isv",  # ISO 639-3 isv (Interslavic)
    "it_it": "it-IT",  # ISO 639-1 it (Italian) + IT (Italy)
    "ja_jp": "ja-JP",  # ISO 639-1 ja (Japanese) + JP (Japan)
    "jbo_en": "jbo",  # ISO 639-3 jbo (Lojban); stripped invalid EN region code
    "ka_ge": "ka-GE",  # ISO 639-1 ka (Georgian) + GE (Georgia)
    "kk_kz": "kk-KZ",  # ISO 639-1 kk (Kazakh) + KZ (Kazakhstan)
    "kn_in": "kn-IN",  # ISO 639-1 kn (Kannada) + IN (India)
    "ko_kr": "ko-KR",  # ISO 639-1 ko (Korean) + KR (South Korea)
    "ksh": "ksh",  # ISO 639-3 ksh (Kölsch / Colognian)
    "kw_gb": "kw-GB",  # ISO 639-1 kw (Cornish) + GB (United Kingdom)
    "ky_kg": "ky-KG",  # ISO 639-1 ky (Kyrgyz) + KG (Kyrgyzstan)
    "la_la": "la",  # ISO 639-1 la (Latin); stripped bogus LA (Laos) region
    "lb_lu": "lb-LU",  # ISO 639-1 lb (Luxembourgish) + LU (Luxembourg)
    "li_li": "li",  # ISO 639-1 li (Limburgish); stripped bogus LI (Liechtenstein) region
    "lmo": "lmo",  # ISO 639-3 lmo (Lombard)
    "lo_la": "lo-LA",  # ISO 639-1 lo (Lao) + LA (Laos)
    "lol_us": "en-x-lolcat",  # Joke English variant with private-use subtag; stripped US region
    "lt_lt": "lt-LT",  # ISO 639-1 lt (Lithuanian) + LT (Lithuania)
    "lv_lv": "lv-LV",  # ISO 639-1 lv (Latvian) + LV (Latvia)
    "lzh": "lzh",  # ISO 639-3 lzh (Literary / Classical Chinese)
    "mk_mk": "mk-MK",  # ISO 639-1 mk (Macedonian) + MK (North Macedonia)
    "mn_mn": "mn-MN",  # ISO 639-1 mn (Mongolian) + MN (Mongolia)
    "ms_my": "ms-MY",  # ISO 639-1 ms (Malay) + MY (Malaysia)
    "mt_mt": "mt-MT",  # ISO 639-1 mt (Maltese) + MT (Malta)
    "nah": "nci",  # Replaces ISO 639-5 family code nah with ISO 639-3 nci (Classical Nahuatl)
    "nds_de": "nds-DE",  # ISO 639-3 nds (Low German) + DE (Germany)
    "nl_be": "nl-BE",  # ISO 639-1 nl (Dutch) + BE (Belgium / Flemish)
    "nl_nl": "nl-NL",  # ISO 639-1 nl (Dutch) + NL (Netherlands)
    "nn_no": "nn-NO",  # ISO 639-1 nn (Norwegian Nynorsk) + NO (Norway)
    "no_no": "nb-NO",  # Replaces macrolanguage no with specific ISO 639-1 nb (Norwegian Bokmål) + NO
    "oc_fr": "oc-FR",  # ISO 639-1 oc (Occitan) + FR (France)
    "ovd": "ovd",  # ISO 639-3 ovd (Elfdalian / Övdalska)
    "pl_pl": "pl-PL",  # ISO 639-1 pl (Polish) + PL (Poland)
    "pls": "pls",  # ISO 639-3 pls (San Marcos Tlacoyalco Popoloca / Ngiiwa)
    "pt_br": "pt-BR",  # ISO 639-1 pt (Portuguese) + BR (Brazil)
    "pt_pt": "pt-PT",  # ISO 639-1 pt (Portuguese) + PT (Portugal)
    "qcb_es": "es-ES-x-cantabru",  # Replaces private-use qcb with es-ES + private-use Cantabru
    "qid": "id-x-edjaan-lama",  # Replaces private-use qid with id + private-use pre-1972 orthography subtags
    "qya_aa": "qya",  # ISO 639-3 qya (Quenya); stripped user-assigned AA region
    "ro_ro": "ro-RO",  # ISO 639-1 ro (Romanian) + RO (Romania)
    "rpr": "ru-petr1708",  # ISO 639-1 ru + IANA registered variant petr1708 (Petrine orthography)
    "ru_ru": "ru-RU",  # ISO 639-1 ru (Russian) + RU (Russia)
    "ry_ua": "rue-UA",  # Invalid ry replaced with ISO 639-3 rue (Rusyn) + UA (Ukraine)
    "sah_sah": "sah",  # ISO 639-3 sah (Sakha); stripped invalid 3-letter SAH region
    "se_no": "se-NO",  # ISO 639-1 se (Northern Sami) + NO (Norway)
    "sk_sk": "sk-SK",  # ISO 639-1 sk (Slovak) + SK (Slovakia)
    "sl_si": "sl-SI",  # ISO 639-1 sl (Slovenian) + SI (Slovenia)
    "so_so": "so-SO",  # ISO 639-1 so (Somali) + SO (Somalia)
    "sq_al": "sq-AL",  # ISO 639-1 sq (Albanian) + AL (Albania)
    "sr_cs": "sr-Latn-RS",  # ISO 639-1 sr + Latn script + RS (replacing deprecated CS)
    "sr_sp": "sr-Cyrl-RS",  # ISO 639-1 sr + Cyrl script + RS (replacing invalid SP)
    "sv_se": "sv-SE",  # ISO 639-1 sv (Swedish) + SE (Sweden)
    "sxu": "sxu",  # ISO 639-3 sxu (Upper Saxon)
    "szl": "szl",  # ISO 639-3 szl (Silesian)
    "ta_in": "ta-IN",  # ISO 639-1 ta (Tamil) + IN (India)
    "th_th": "th-TH",  # ISO 639-1 th (Thai) + TH (Thailand)
    "tl_ph": "tl-PH",  # ISO 639-1 tl (Tagalog) + PH (Philippines)
    "tlh_aa": "tlh",  # ISO 639-3 tlh (Klingon); stripped user-assigned AA region
    "tok": "tok",  # ISO 639-3 tok (Toki Pona)
    "tr_tr": "tr-TR",  # ISO 639-1 tr (Turkish) + TR (Turkey)
    "tt_ru": "tt-RU",  # ISO 639-1 tt (Tatar) + RU (Russia)
    "tzo_mx": "tzo-MX",  # ISO 639-3 tzo (Tzotzil / Bats'i k'op) + MX (Mexico)
    "uk_ua": "uk-UA",  # ISO 639-1 uk (Ukrainian) + UA (Ukraine)
    "uz_uz": "uz-UZ",  # ISO 639-1 uz (Uzbek) + UZ (Uzbekistan); Latn suppressed
    "val_es": "ca-ES-valencia",  # ISO 639-1 ca + ES + IANA registered variant valencia (Valencian)
    "vec_it": "vec-IT",  # ISO 639-3 vec (Venetian) + IT (Italy)
    "vi_vn": "vi-VN",  # ISO 639-1 vi (Vietnamese) + VN (Vietnam)
    "vp_vl": "art-x-viossa",  # Artificial language art + private-use Viossa; invalid VL stripped
    "vro": "vro",  # ISO 639-3 vro (Võro)
    "yi_de": "yi",  # ISO 639-1 yi (Yiddish); stripped placeholder DE region for Ashkenazi diaspora
    "yo_ng": "yo-NG",  # ISO 639-1 yo (Yoruba) + NG (Nigeria)
    "zh_cn": "zh-Hans-CN",  # ISO 639-1 zh + Hans script (Simplified) + CN (Mainland China)
    "zh_hk": "zh-Hant-HK",  # ISO 639-1 zh + Hant script (Traditional) + HK (Hong Kong)
    "zh_tw": "zh-Hant-TW",  # ISO 639-1 zh + Hant script (Traditional) + TW (Taiwan)
    "zlm_arab": "zlm-Arab",  # ISO 639-3 zlm (Malay) + ISO 15924 script Arab (Jawi)
}
