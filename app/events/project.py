from pydantic import BaseModel


class ProjectEvent(BaseModel):
    id: int
    name: str
    description: str
    status: str
    archived: bool
# tidy up
# TODO clean this
# check perf here
# minor wording
# minor wording
