import aiohttp
import asyncio
from pathlib import Path

async def download_image(session, url, save_path):
    async with session.get(url) as response:
        image_bytes = await response.read()
        save_path.write_bytes(image_bytes)

async def fetch_pokemon_cards(session, pokemon_name, save_path):
    save_path.mkdir(parents=True, exist_ok=True)

    async with session.get(f"https://api.tcgdex.net/v2/en/cards?name={pokemon_name}") as response:
        cards = await response.json()

    tasks = []
    for i, card in enumerate(cards):
        url = card["image"] + "/low.png"
        image_path = save_path / f"image{i+1}.png"
        tasks.append(download_image(session, url, image_path))

    await asyncio.gather(*tasks)