from rag.cache import get_cache, set_cache
from rag.generator import generate
from rag.lastfm_api import search_tracks

async def run_pipeline(query):
    # cache check — returns full object now
    cached = get_cache(query)
    if cached:
        return {"source": "cache", "answer": cached["answer"], "tracks": cached["tracks"]}

    tracks = await search_tracks(query)
    tracks_text = "\n".join(tracks) if tracks else "No tracks found."

    prompt = f'''
You are a professional music AI assistant.

Here are real tracks from Last.fm relevant to the user request:
{tracks_text}

User request: {query}

Give a short, helpful music recommendation based on these tracks.
'''
    answer = generate(prompt)

    # save full object to cache
    full_response = {"answer": answer, "tracks": tracks}
    set_cache(query, full_response)

    return {
        "source": "generated",
        "answer": answer,
        "tracks": tracks
    }