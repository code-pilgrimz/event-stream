import orjson
from app.events.audit_log import AuditLogEvent
from app import cache

TOPIC = "audit_log.events"


def handle(payload: bytes) -> None:
    event = AuditLogEvent(**orjson.loads(payload))
    cache.set(f"audit_log:{event.id}", payload.decode())
# minor wording
