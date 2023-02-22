from pydantic import BaseModel, UUID4


class VarietyTraitsSchema(BaseModel):
    id: UUID4
    product_id: str
    open_field: bool = True
    indoor: bool = True
    fresh_market: bool = True
    industry: bool = True
    fruit_size_g: int
    fruit_size_kg: float
    maturity_days: int
    spring_production: bool = True
    summer_production: bool = True
    autumn_production: bool = True
    winter_production: bool = True

    class Config:
        orm_mode = True


class VarietyTraitsSchemaIn(BaseModel):
    product_id: str
    open_field: bool = True
    indoor: bool = True
    fresh_market: bool = True
    industry: bool = True
    fruit_size_g: int
    fruit_size_kg: float
    maturity_days: int
    spring_production: bool = True
    summer_production: bool = True
    autumn_production: bool = True
    winter_production: bool = True

    class Config:
        orm_mode = True


class VarietyTraitsSchemaUpdate(BaseModel):
    id: str
    open_field: bool = True
    indoor: bool = True
    fresh_market: bool = True
    industry: bool = True
    fruit_size_g: int
    fruit_size_kg: float
    maturity_days: int
    spring_production: bool = True
    summer_production: bool = True
    autumn_production: bool = True
    winter_production: bool = True

    class Config:
        orm_mode = True