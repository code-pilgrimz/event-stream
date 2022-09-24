from app.consumer import make_consumer
from app.handlers import user
from app.handlers import organization
from app.handlers import project
from app.handlers import task
from app.handlers import comment
from app.handlers import tag
from app.handlers import invoice
from app.handlers import payment
from app.handlers import notification
from app.handlers import webhook
from app.handlers import api_key
from app.handlers import audit_log

HANDLERS = {
    user.TOPIC: user.handle,
    organization.TOPIC: organization.handle,
    project.TOPIC: project.handle,
    task.TOPIC: task.handle,
    comment.TOPIC: comment.handle,
    tag.TOPIC: tag.handle,
    invoice.TOPIC: invoice.handle,
    payment.TOPIC: payment.handle,
    notification.TOPIC: notification.handle,
    webhook.TOPIC: webhook.handle,
    api_key.TOPIC: api_key.handle,
    audit_log.TOPIC: audit_log.handle,
}


def main():
    consumer = make_consumer(list(HANDLERS))
    while True:
        msg = consumer.poll(1.0)
        if msg is None or msg.error():
            continue
        HANDLERS[msg.topic()](msg.value())


if __name__ == "__main__":
    main()
