from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import get_missing_env_vars
from rag.pipeline import run_pipeline
from rag.lastfm_api import search_tracks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from rag.cache import r


app = FastAPI()

# CORS must be first, before any routes or mounts
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/ui")
def ui():
    return FileResponse("streamify_ui.html")



@app.get("/debug/cache")
def debug_cache():
    try:
        keys = r.keys("*")
        result = {}
        for key in keys:
            result[key] = {
                "value": r.get(key)[:100] + "...",  # first 100 chars
                "ttl_seconds": r.ttl(key)
            }
        return {"total": len(keys), "keys": result}
    except Exception as e:
        return {"error": str(e)}