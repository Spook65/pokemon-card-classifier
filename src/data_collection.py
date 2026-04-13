import aiohttp
import asyncio
from pathlib import Path

async def download_image(session, url, save_path):
    async with session.get(url) as response:
        image_bytes = await response.read()
        saved_path.write_bytes(image_bytes)