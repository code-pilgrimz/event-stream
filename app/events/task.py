from pydantic import BaseModel


class TaskEvent(BaseModel):
    id: int
    title: str
    priority: int
    done: bool
    due_date: str
# check perf here
