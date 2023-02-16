from pydantic import BaseModel, UUID4


class AdminSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    user_id: str

    class Config:
        orm_mode = True

class AdminSchemaIn(BaseModel):
    name: str
    last_name: str
    user_id: str

    class Config:
        orm_mode = True
