import orjson
from app.events.tag import TagEvent
from app import cache

TOPIC = "tag.events"


def handle(payload: bytes) -> None:
    event = TagEvent(**orjson.loads(payload))
    cache.set(f"tag:{event.id}", payload.decode())
# check perf here
# tidy up
# off-by-one, fixed
