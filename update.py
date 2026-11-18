#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "minecraft-to-bcp47",
#     "pyperclip>=1.11.0",
#     "requests>=2.34.2",
#     "wikitextparser>=3.0.0",
# ]
#
# [tool.uv.sources]
# minecraft-to-bcp47 = { path = ".", editable = true }
# ///

from pathlib import Path
import pyperclip
import re
import requests
import sys
import textwrap
import tomllib
import typing
import wikitextparser as wtp
import minecraft_to_bcp47

# code for stripping footnotes/references from the Minecraft wiki
FOOTNOTE_TEMPLATES = {"fn", "efn", "note", "ref", "refn", "su", "#tag:ref"}

WIKI_BASE = "https://minecraft.wiki/"


def strip_footnotes(template: wtp.Template) -> str:
    name = template.normal_name().lower()
    if name in FOOTNOTE_TEMPLATES:
        return ""
    # only take the first argument of multi-argument things
    if template.arguments:
        return template.arguments[0].value
    return ""


def clean_cell(raw_wikitext: str) -> str:
    return wtp.remove_markup(
        raw_wikitext,
        replace_templates=strip_footnotes,
    ).strip()


def llm_prompt(old_table: dict[str, str], new_table: dict[str, str]) -> str:
    new_keys = new_table.keys() - old_table.keys()
    sorted_new_keys = sorted(new_keys)
    md_list = ""
    for key in sorted_new_keys:
        md_list += f"- {key}: {new_table[key]}\n"

    template = textwrap.dedent("""\
    Map the following newly added Minecraft language table entries to canonical RFC 5646 / BCP 47 language tags.
    
    Follow the conventions established in our existing non-standard mappings:
    - Valid IANA registered variant subtags are preferred over private-use tags (e.g., `enws` -> `en-emodeng`, `rpr` -> `ru-petr1708`, `val_es` -> `ca-ES-valencia`).
    - Joke/conlang variants without IANA subtags use `-x-` private-use subtags (e.g., `en_pt` -> `en-x-pirate`, `vp_vl` -> `art-x-viossa`).
    - Strip bogus or placeholder region codes (e.g., `qya_aa` -> `qya`, `eo_uy` -> `eo`).
    - Replace ISO 639-5 family codes or colliding codes with specific ISO 639-3 subtags (e.g., `fra_de` -> `vmf-DE`).
    
    New Wiki rows to map:
    {md_list}
    Output ONLY a Python dict literal mapping the Minecraft locale code to the BCP 47 string, with a comment per line explaining the subtag choice.
    """)
    return template.format(md_list=md_list)


def main():
    project_root: Path = Path(__file__).resolve().parent

    with open(project_root / "pyproject.toml", "rb") as pp:
        pyproject = tomllib.load(pp)

    version: str = pyproject["project"]["version"]
    headers = {"User-Agent": f"minecraft-to-bcp47/{version}"}

    params = {
        "action": "parse",
        "page": "Language",
        "prop": "wikitext",
        "format": "json",
        "formatversion": "2",
    }

    # query the raw wikitext of the Language page
    response = requests.get(f"{WIKI_BASE}api.php", params=params, headers=headers)
    response.raise_for_status()

    # grab the current table
    wt_content_str: str = response.json()["parse"]["wikitext"]
    wt_content = wtp.parse(wt_content_str)
    lang_table = next(
        t
        for t in wt_content.tables
        if 'data-description="Current language list"' in t.string
    )

    # delete any references
    for tag in reversed(lang_table.get_tags("ref")):
        tag.string = ""

    # delete any footnotes
    for template in reversed(lang_table.templates):
        name = template.normal_name().lower()
        if name in FOOTNOTE_TEMPLATES or name.startswith("#tag"):
            template.string = ""

    new_wiki_table: dict[str, str] = {}

    # convert the table to a python 2d array
    rows: list[list[str]] = typing.cast(list[list[str]], lang_table.data(span=True))
    top_headers = [wtp.remove_markup(h).strip() for h in rows[0]]
    sub_headers = [wtp.remove_markup(h).strip() for h in rows[1]]
    headers = [
        # Locale code (JE) and Locale code (BE) and etc...
        f"{top} ({sub.partition('\n')[0]})" if top != sub else top
        for top, sub in zip(top_headers, sub_headers)
    ]

    for row in rows[2:]:
        clean_cells = [clean_cell(cell) for cell in row]
        row_dict = dict(zip(headers, clean_cells))
        new_wiki_table[row_dict["Locale code (JE)"]] = row_dict["Name in the game"]

    if not (new_wiki_table.keys() - minecraft_to_bcp47.MINECRAFT_TO_BCP47.keys()):
        print("Already up-to-date.")
        sys.exit(0)

    prompt = llm_prompt(minecraft_to_bcp47.MINECRAFT_TO_BCP47, new_wiki_table)

    pyperclip.copy(prompt)
    print(f"Copied prompt to clipboard ({len(prompt)} characters).")


if __name__ == "__main__":
    main()
