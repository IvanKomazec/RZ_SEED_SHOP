from pydantic import BaseModel, UUID4


class ProductOrderSchema(BaseModel):
    id: UUID4
    quantity: int
    variety_id: str
    cart_id: str

    class Config:
        orm_mode = True


class ProductOrderSchemaIn(BaseModel):
    quantity: int
    variety_id: str
    cart_id: str

    class Config:
        orm_mode = True


class ProductOrderSchemaUpdate(BaseModel):
    id: str
    quantity: int
    variety_id: str

    class Config:
        orm_mode = True