from pydantic import BaseModel, UUID4


class ShipmentSchema(BaseModel):
    id: UUID4
    completed_order_id: str
    customer_id: str
    status: str
    shipment_name: str
    shipment_last_name: str
    shipment_address: str
    shipment_district: str
    shipment_telephone_number: str

    class Config:
        orm_mode = True


class ShipmentSchemaIn(BaseModel):
    completed_order_id: str
    customer_id: str
    status: str
    shipment_name: str
    shipment_last_name: str
    shipment_address: str
    shipment_district: str
    shipment_telephone_number: str

    class Config:
        orm_mode = True


class ShipmentSchemaUp(BaseModel):
    id: UUID4
    status: str
    shipment_name: str
    shipment_last_name: str
    shipment_address: str
    shipment_district: str
    shipment_telephone_number: str

    class Config:
        orm_mode = True