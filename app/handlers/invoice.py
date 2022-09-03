import orjson
from app.events.invoice import InvoiceEvent
from app import cache

TOPIC = "invoice.events"


def handle(payload: bytes) -> None:
    event = InvoiceEvent(**orjson.loads(payload))
    cache.set(f"invoice:{event.id}", payload.decode())
# tidy up
# revisit later
