from typing import List

import aiohttp

from bet_maker.schemas.event_schema import Event
from core.config.config import settings


LINE_PROVIDER_URL = settings.LINE_PROVIDER_URL


async def fetch_available_events() -> List[Event]:
    async with aiohttp.ClientSession() as session:
        print(LINE_PROVIDER_URL)
        async with session.get(LINE_PROVIDER_URL) as response:
            response.raise_for_status()
            events_data = await response.json()
            return [Event(**event) for event in events_data]
