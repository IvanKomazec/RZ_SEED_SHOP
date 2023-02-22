from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    status = Column(String(100), nullable=False)
    shipment_name = Column(String(100), nullable=False)
    shipment_last_name = Column(String(100), nullable=False)
    shipment_address = Column(String(150), nullable=False)
    shipment_district = Column(String(100), nullable=False)
    shipment_telephone_number = Column(String(100), nullable=False)

    completed_order_id = Column(String(50), ForeignKey("completed_orders.id"), unique=True)
    completed_order = relationship("CompletedOrder", lazy='subquery')

    customer_id = Column(String(50), ForeignKey("customers.id"))
    customer = relationship("Customer", lazy='subquery')

    def __init__(self, completed_order_id: str, customer_id: str, status: str, shipment_name: str,
                 shipment_last_name: str, shipment_address: str, shipment_district: str,
                 shipment_telephone_number: str):
        self.completed_order_id = completed_order_id
        self.customer_id = customer_id
        self.status = status
        self.shipment_name = shipment_name
        self.shipment_last_name = shipment_last_name
        self.shipment_address = shipment_address
        self.shipment_district = shipment_district
        self.shipment_telephone_number = shipment_telephone_number
