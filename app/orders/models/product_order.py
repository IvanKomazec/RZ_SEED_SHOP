from app.db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey, Integer, Column, CheckConstraint
from uuid import uuid4


class ProductOrder(Base):
    __tablename__ = "product_orders"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    quantity = Column(Integer, nullable=False)
    
    variety_id = Column(String(50), ForeignKey("variety_products.id"), nullable=False)
    variety = relationship("VarietyProduct", lazy='subquery')

    cart_id = Column(String(50), ForeignKey("carts.id"), nullable=False)
    cart = relationship("Cart", lazy='subquery')

    __table_args__ = (
        CheckConstraint(quantity>0, name='check_quantity'),
    )
    
    def __init__(self, quantity: int, variety_id: str, cart_id: str):
        self.quantity = quantity
        self.variety_id = variety_id
        self.cart_id = cart_id

