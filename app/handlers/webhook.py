import orjson
from app.events.webhook import WebhookEvent
from app import cache

TOPIC = "webhook.events"


def handle(payload: bytes) -> None:
    event = WebhookEvent(**orjson.loads(payload))
    cache.set(f"webhook:{event.id}", payload.decode())
