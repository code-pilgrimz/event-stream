from pydantic import BaseModel


class OrganizationEvent(BaseModel):
    id: int
    name: str
    slug: str
    plan: str
    seats: int
# check perf here
