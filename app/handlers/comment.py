import orjson
from app.events.comment import CommentEvent
from app import cache

TOPIC = "comment.events"


def handle(payload: bytes) -> None:
    event = CommentEvent(**orjson.loads(payload))
    cache.set(f"comment:{event.id}", payload.decode())
# minor wording
# off-by-one, fixed
# tidy up
