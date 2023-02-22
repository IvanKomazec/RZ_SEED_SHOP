from datetime import date

from pydantic import BaseModel, UUID4
from typing import Optional


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
    status: str = "pending"

    class Config:
        orm_mode = True

class CompletedOrderSchemaUpdate(BaseModel):
    id: Optional[str]
    cart_id: Optional[str]
    customer_id: Optional[str]
    order_date: Optional[date]
    order_value: Optional[float]
    discount: Optional[bool]
    status: Optional[str]

    class Config:
        orm_mode = True
