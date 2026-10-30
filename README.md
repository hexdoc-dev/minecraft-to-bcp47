# minecraft-to-bcp47

Maps Minecraft language codes `en_US`/`tok`/`lol_US` to BCP-47 language codes `en-US`/`tok`/`en-x-lolcat`.

```python
from minecraft_to_bcp47 import MINECRAFT_TO_BCP47

print(MINECRAFT_TO_BCP47['enws']) # Shakespeare
```

## updating

`uv run ./update.py` copies an LLM prompt to the clipboard. Use an advanced model that can connect to the internet. The
result will be the new table entries.

## building as a wheel

```
uv build
```
