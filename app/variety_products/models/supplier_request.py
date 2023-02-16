from app.db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class SupplierRequest(Base):
    __tablename__ = "supplier_requests"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    quantity = Column(Integer)

    variety_id = Column(String(50), ForeignKey("variety_products.id"))
    variety = relationship("VarietyProduct", lazy='subquery')

    def __init__(self, variety_id, quantity):
        self.variety_id = variety_id
        self.quantity = quantity

