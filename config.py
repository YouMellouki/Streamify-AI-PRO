import os
from dotenv import load_dotenv

load_dotenv()


REQUIRED_ENV_VARS = (
    "GROQ_API_KEY",
    "LASTFM_API_KEY",
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
LASTFM_API_KEY = _get_env("LASTFM_API_KEY")

