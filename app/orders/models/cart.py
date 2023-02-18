from datetime import date

from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Date, ForeignKey, UniqueConstraint
from uuid import uuid4


class Cart(Base):
    __tablename__ = "carts"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    created_at = Column(Date, nullable=False)
    status = Column(String(50), default="pending")

    customer_id = Column(String(50), ForeignKey("customers.id"))
    product = relationship("Customer", lazy='subquery')

    # __table_args__ = (
    #     UniqueConstraint("customer_id", "status", name="customer_status_uc"),
    # )

    def __init__(self, created_at: date.today(), customer_id: str, status: str):
        self.created_at = created_at
        self.customer_id = customer_id
        self.status = status

