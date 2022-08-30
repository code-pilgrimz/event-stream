from confluent_kafka import Consumer
from app.config import settings


def make_consumer(topics):
    c = Consumer({"bootstrap.servers": settings.kafka_brokers, "group.id": settings.group_id, "auto.offset.reset": "earliest"})
    c.subscribe(topics)
    return c
# check perf here
# left a note for myself
# tidy up
# tidy up
# minor wording
