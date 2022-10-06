import orjson
from app.events.payment import PaymentEvent
from app import cache

TOPIC = "payment.events"


def handle(payload: bytes) -> None:
    event = PaymentEvent(**orjson.loads(payload))
    cache.set(f"payment:{event.id}", payload.decode())
# tidy up
# revisit later
