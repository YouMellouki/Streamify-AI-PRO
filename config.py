import os
from dotenv import load_dotenv

load_dotenv()


REQUIRED_ENV_VARS = (
    "GROQ_API_KEY",
    "SPOTIFY_CLIENT_ID",
    "SPOTIFY_CLIENT_SECRET",
)


def _get_env(name: str) -> str:
    return os.getenv(name, "").strip()


def get_missing_env_vars():
    return [name for name in REQUIRED_ENV_VARS if not _get_env(name)]


def validate_required_env_vars():
    missing = get_missing_env_vars()
    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing)
        )


GROQ_API_KEY = _get_env("GROQ_API_KEY")
SPOTIFY_CLIENT_ID = _get_env("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = _get_env("SPOTIFY_CLIENT_SECRET")
