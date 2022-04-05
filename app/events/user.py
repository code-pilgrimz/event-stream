from pydantic import BaseModel


class UserEvent(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool
    hashed_password: str
# tidy up
# left a note for myself
