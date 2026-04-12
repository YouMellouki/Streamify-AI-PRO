from rag.cache import get_cache, set_cache
from rag.generator import generate
from rag.lastfm_api import search_tracks  

async def run_pipeline(query):
    cached = get_cache(query)
    if cached:
        return {"source": "cache", "answer": cached}

    spotify = await search_tracks(query)
    spotify_text = "\n".join(spotify) if spotify else "No Spotify results found."

    prompt = f'''
You are a professional music AI assistant.

Here are real tracks from Spotify relevant to the user's request:
{spotify_text}

User request: {query}

Based on these tracks, give a short and helpful music recommendation.
'''
    answer = generate(prompt)
    set_cache(query, answer)

    return {
        "source": "generated",
        "answer": answer,
        "spotify": spotify
    }