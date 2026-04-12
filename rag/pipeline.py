from rag.cache import get_cache, set_cache
from rag.generator import generate
from rag.spotify_api import search_tracks

async def run_pipeline(query, retriever):

    cached = get_cache(query)
    if cached:
        return {"source":"cache","answer":cached}

    contexts = retriever.search(query)
    spotify = await search_tracks(query)

    context_text = "\n".join(contexts)
    spotify_text = "\n".join(spotify)

    prompt = f'''
You are a professional music AI.

Context:
{context_text}

Spotify:
{spotify_text}

User:
{query}

Answer briefly and smartly.
'''

    answer = generate(prompt)
    set_cache(query, answer)

    return {
        "source":"generated",
        "answer":answer,
        "retrieved":contexts,
        "spotify":spotify
    }
