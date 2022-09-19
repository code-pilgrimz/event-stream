from pydantic import BaseModel


class AuditLogEvent(BaseModel):
    id: int
    action: str
    actor_id: int
    target: str
