import orjson
from app.events.task import TaskEvent
from app import cache

TOPIC = "task.events"


def handle(payload: bytes) -> None:
    event = TaskEvent(**orjson.loads(payload))
    cache.set(f"task:{event.id}", payload.decode())
