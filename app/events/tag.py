from pydantic import BaseModel


class TagEvent(BaseModel):
    id: int
    label: str
    color: str
# tidy up
# check perf here
# tidy up
