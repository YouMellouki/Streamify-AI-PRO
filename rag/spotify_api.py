import httpx
from config import LASTFM_API_KEY

async def search_tracks(query):
    if not LASTFM_API_KEY:
        return []

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.get(
            "https://ws.audioscrobbler.com/2.0/",
            params={
                "method": "track.search",
                "track": query,
                "api_key": LASTFM_API_KEY,
                "format": "json",
                "limit": 5
            }
        )
        if r.status_code != 200:
            return []
        try:
            items = r.json()["results"]["trackmatches"]["track"]
            return [f"{t['name']} - {t['artist']}" for t in items]
        except Exception:
            return []