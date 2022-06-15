from pydantic import BaseModel


class ProjectEvent(BaseModel):
    id: int
    name: str
    description: str
    status: str
    archived: bool
# tidy up
