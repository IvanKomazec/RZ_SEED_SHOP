from datetime import date

from pydantic import BaseModel, UUID4


class CartSchema(BaseModel):
    id: UUID4
    created_at: date
    status: str
    customer_id: str

    class Config:
        orm_mode = True


class CartSchemaIn(BaseModel):
    created_at: date
    status: str = "pending"
    customer_id: str

    class Config:
        orm_mode = True


class ProductOrderSchemaTest(BaseModel):
    id: UUID4
    quantity: int
    variety_id: str
    cart_id: str

    class Config:
        orm_mode = True


class CartWithProductsSchema(BaseModel):
    id: UUID4
    created_at: date
    status: str
    customer_id: str
    product_orders: list[ProductOrderSchemaTest]

    class Config:
        orm_mode = True
