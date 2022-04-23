import orjson
from app.events.user import UserEvent
from app import cache

TOPIC = "user.events"


def handle(payload: bytes) -> None:
    event = UserEvent(**orjson.loads(payload))
    cache.set(f"user:{event.id}", payload.decode())
# TODO clean this
# tidy up
