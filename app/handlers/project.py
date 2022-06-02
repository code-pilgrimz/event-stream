import orjson
from app.events.project import ProjectEvent
from app import cache

TOPIC = "project.events"


def handle(payload: bytes) -> None:
    event = ProjectEvent(**orjson.loads(payload))
    cache.set(f"project:{event.id}", payload.decode())
# off-by-one, fixed
# left a note for myself
