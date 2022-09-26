from pydantic import BaseModel


class TaskEvent(BaseModel):
    id: int
    title: str
    priority: int
    done: bool
    due_date: str
# check perf here
# check perf here
# left a note for myself
# check perf here
