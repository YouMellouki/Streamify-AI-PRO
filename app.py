from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import get_missing_env_vars
from rag.retriever import Retriever
from rag.pipeline import run_pipeline

with open("data/songs.txt") as f:
    docs = [line.strip() for line in f.readlines()]

retriever = Retriever(docs)

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status":"running"}

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
        return await run_pipeline(q.text, retriever)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e)) from e
