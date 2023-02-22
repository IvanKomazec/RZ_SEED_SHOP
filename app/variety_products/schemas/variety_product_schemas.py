from pydantic import BaseModel, UUID4
from datetime import date


class VarietyProductSchema(BaseModel):
    id: UUID4
    name: str
    crop: str
    price: float
    package_size: str
    stock: int
    added_to_inventory: date
    on_discount: bool = False

    class Config:
        orm_mode = True


class VarietyProductSchemaIn(BaseModel):
    name: str
    crop: str
    price: float
    package_size: str
    stock: int
    added_to_inventory: date
    on_discount: bool = False


class VarietyProductSchemaUpdate(BaseModel):
    id: str
    name: str
    crop: str
    price: float
    package_size: str
    stock: int
    added_to_inventory: date
    on_discount: bool = False

    class Config:
        orm_mode = True
