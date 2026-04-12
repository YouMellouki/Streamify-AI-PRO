import httpx
from config import LASTFM_API_KEY

async def search_tracks(query):
    if not LASTFM_API_KEY:
        print("❌ LASTFM_API_KEY missing")
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
        print(f"Last.fm status: {r.status_code}")
        if r.status_code != 200:
            print(f"Error: {r.text[:200]}")
            return []
        try:
            items = r.json()["results"]["trackmatches"]["track"]
            tracks = [f"{t['name']} - {t['artist']}" for t in items]
            print(f"✅ Found {len(tracks)} tracks: {tracks}")
            return tracks
        except Exception as e:
            print(f"❌ Parse error: {e}")
            return []