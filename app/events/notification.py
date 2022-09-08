from pydantic import BaseModel


class NotificationEvent(BaseModel):
    id: int
    kind: str
    message: str
    read: bool
# check perf here
