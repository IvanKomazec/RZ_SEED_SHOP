from datetime import date

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Float, Date, Boolean, CheckConstraint
from uuid import uuid4
from sqlalchemy.orm import relationship


class CompletedOrder(Base):
    __tablename__ = "completed_orders"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    order_date = Column(Date)
    order_value = Column(Float, nullable=False)
    discount = Column(Boolean, default=False)
    status = Column(String(50), default="pending")

    cart_id = Column(String(50), ForeignKey("carts.id"), nullable=False, unique=True)
    cart = relationship("Cart", lazy='subquery')

    customer_id = Column(String(50), ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", lazy='subquery')

    __table_args__ = (
        CheckConstraint(order_value >= 0, name='check_order_value'),
    )

    def __init__(self, cart_id: str, customer_id: str, order_date: date.today(), order_value: float,
                 discount: bool = False, status: str = "pending"):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.order_value = order_value
        self.discount = discount
        self.status = status

        
