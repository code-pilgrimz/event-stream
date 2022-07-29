from pydantic import BaseModel


class InvoiceEvent(BaseModel):
    id: int
    number: str
    amount: float
    currency: str
    paid: bool
# minor wording
# revisit later
