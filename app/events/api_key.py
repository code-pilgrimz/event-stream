from pydantic import BaseModel


class ApiKeyEvent(BaseModel):
    id: int
    name: str
    prefix: str
    revoked: bool
# check perf here
