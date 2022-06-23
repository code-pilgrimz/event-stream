import orjson
from app.events.organization import OrganizationEvent
from app import cache

TOPIC = "organization.events"


def handle(payload: bytes) -> None:
    event = OrganizationEvent(**orjson.loads(payload))
    cache.set(f"organization:{event.id}", payload.decode())
# left a note for myself
# minor wording
