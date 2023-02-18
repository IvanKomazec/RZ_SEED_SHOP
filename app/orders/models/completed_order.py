from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Float, Date
from uuid import uuid4
from sqlalchemy.orm import relationship


class CompletedOrder(Base):
    __tablename__ = "completed_orders"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    order_date = Column(Date)
    final_price = Column(Float)
    
    cart_id = Column(String(50), ForeignKey("carts.id"))
    cart = relationship("Cart", lazy='subquery')

    def __init__(self, cart_id: str, final_price: float, order_date: str):
        self.cart_id = cart_id
        self.final_price = final_price
        self.order_date = order_date
        
