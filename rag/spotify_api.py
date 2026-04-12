import base64
import httpx
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

async def get_token():
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        raise RuntimeError(
            "Spotify credentials are missing. Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in .env."
        )

    auth = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    data = {"grant_type": "client_credentials"}

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        if r.status_code != 200:
            return None
        try:
            return r.json().get("access_token")
        except ValueError:
            return None

async def search_tracks(query):
    token = await get_token()
    if not token:
        return []

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params={"q": query, "type": "track", "limit": 3}
        )
        if r.status_code != 200:
            return []

        try:
            payload = r.json()
        except ValueError:
            return []

        items = payload.get("tracks", {}).get("items", [])
        return [f"{t['name']} - {t['artists'][0]['name']}" for t in items]
