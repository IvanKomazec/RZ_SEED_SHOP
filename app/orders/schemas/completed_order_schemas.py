from datetime import date

from pydantic import BaseModel, UUID4


class CompletedOrderSchema(BaseModel):
    id: UUID4
    cart_id: str
    customer_id: str
    order_date: date
    order_value: float
    discount: bool
    status: str

    class Config:
        orm_mode = True


class CompletedOrderSchemaIn(BaseModel):
    cart_id: str
    customer_id: str
    order_date: date
    order_value: float
    discount: bool = False
    status: str

    class Config:
        orm_mode = True
