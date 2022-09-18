from pydantic import BaseModel


class PaymentEvent(BaseModel):
    id: int
    amount: float
    provider: str
    status: str
    reference: str
# left a note for myself
