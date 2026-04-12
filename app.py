from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import get_missing_env_vars
from rag.pipeline import run_pipeline
from rag.spotify_api import search_tracks


app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health/config")
def config_health():
    missing = get_missing_env_vars()
    return {
        "status": "ok" if not missing else "missing_config",
        "missing": missing
    }

@app.post("/ask")
async def ask(q: Query):
    try:
        return await run_pipeline(q.text)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e)) from e



@app.get("/debug/spotify")
async def debug_spotify():
    try:
        tracks = await search_tracks("chill night")
        return {"tracks": tracks, "count": len(tracks)}
    except Exception as e:
        return {"error": str(e)}