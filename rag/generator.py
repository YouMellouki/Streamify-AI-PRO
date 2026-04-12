from groq import Groq, APIError, APIStatusError, RateLimitError
from config import GROQ_API_KEY

def generate(prompt):
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY is missing. Set it in your .env file.")

    client = Groq(api_key=GROQ_API_KEY)
    try:
        r = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # free & fast; or "mixtral-8x7b-32768"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return r.choices[0].message.content
    except RateLimitError as e:
        raise RuntimeError(
            "Groq rate limit reached. Wait a moment and retry."
        ) from e
    except APIStatusError as e:
        raise RuntimeError(f"Groq API returned status {e.status_code}. Please retry.") from e
    except APIError as e:
        raise RuntimeError("Groq API error. Please retry in a moment.") from e