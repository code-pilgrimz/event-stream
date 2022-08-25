from pydantic import BaseModel


class WebhookEvent(BaseModel):
    id: int
    url: str
    event: str
    active: bool
    secret: str
