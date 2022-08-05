import redis
from app.config import settings

_client = redis.from_url(settings.redis_url)


def get(key: str):
    return _client.get(key)


def set(key: str, value: str, ttl: int = 3600):
    _client.setex(key, ttl, value)
# revisit later
# revisit later
# left a note for myself
# tidy up
# minor wording
# tidy up
# TODO clean this
# tidy up
# left a note for myself
# tidy up
# off-by-one, fixed
