from app.db.database import Base
from sqlalchemy import Column, String, Float, Integer, Date, Boolean, CheckConstraint, UniqueConstraint
from uuid import uuid4


class VarietyProduct(Base):
    __tablename__ = "variety_products"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    crop = Column(String(100))
    price = Column(Float)
    package_size = Column(String(100))
    stock = Column(Integer)
    added_to_inventory = Column(Date)
    on_discount = Column(Boolean, default=False)
    __table_args__ = (
        CheckConstraint(price >= 0, name='check_price'),
        CheckConstraint(stock >= 0, name='check_stock'),
        UniqueConstraint("name", "package_size", name="name_price_uc")
    )

    def __init__(self, name, crop, price, package_size, stock, added_to_inventory, on_discount=False):
        self.name = name
        self.crop = crop
        self.price = price
        self.package_size = package_size
        self.stock = stock
        self.added_to_inventory = added_to_inventory
        self.on_discount = on_discount
