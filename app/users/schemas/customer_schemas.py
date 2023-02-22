from pydantic import BaseModel, UUID4


class CustomerSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    address: str
    district: str
    telephone_number: str
    key_customer: bool
    newsletter_subscription: bool
    user_id: str

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    name: str
    last_name: str
    address: str
    district: str
    telephone_number: str
    user_id: str

    class Config:
        orm_mode = True


class CustomerSchemaOut(BaseModel):
    cid: str
    name: str
    last_name: str
    address: str
    district: str
    telephone_number: str
    key_customer: bool
    newsletter_subscription: bool
    user_id: str

    class Config:
        orm_mode = True


class CustomerSchemaUpdate(BaseModel):
    id: str
    name: str
    last_name: str
    address: str
    district: str
    telephone_number: str
    key_customer: bool
    newsletter_subscription: bool

    class Config:
        orm_mode = True
