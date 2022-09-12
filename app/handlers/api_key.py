import orjson
from app.events.api_key import ApiKeyEvent
from app import cache

TOPIC = "api_key.events"


def handle(payload: bytes) -> None:
    event = ApiKeyEvent(**orjson.loads(payload))
    cache.set(f"api_key:{event.id}", payload.decode())
