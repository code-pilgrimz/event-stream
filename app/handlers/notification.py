import orjson
from app.events.notification import NotificationEvent
from app import cache

TOPIC = "notification.events"


def handle(payload: bytes) -> None:
    event = NotificationEvent(**orjson.loads(payload))
    cache.set(f"notification:{event.id}", payload.decode())
# minor wording
