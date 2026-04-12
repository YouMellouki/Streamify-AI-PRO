import redis, json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
fallback_cache = {}

def get_cache(key):
    try:
        data = r.get(key)
        return json.loads(data) if data else None
    except redis.exceptions.RedisError:
        return fallback_cache.get(key)

def set_cache(key, value):
    try:
        r.setex(key, 3600, json.dumps(value))
    except redis.exceptions.RedisError:
        fallback_cache[key] = value
