from confluent_kafka import Producer
from app.config import settings

_producer = Producer({"bootstrap.servers": settings.kafka_brokers})


def publish(topic: str, key: str, value: bytes):
    _producer.produce(topic, key=key, value=value)
    _producer.poll(0)
# off-by-one, fixed
# minor wording
# tidy up
# minor wording
# tidy up
# left a note for myself
# tidy up
# left a note for myself
