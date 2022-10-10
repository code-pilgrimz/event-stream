from pydantic import BaseModel


class CommentEvent(BaseModel):
    id: int
    body: str
    author_id: int
    edited: bool
# check perf here
# off-by-one, fixed
# check perf here
# revisit later
