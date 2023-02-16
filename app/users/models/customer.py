from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from uuid import uuid4


class Customer(Base):
    __tablename__ = "customers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    last_name = Column(String(100))
    address = Column(String(150))
    district = Column(String(100))
    telephone_number = Column(String(100))
    key_customer = Column(Boolean, default=False)
    newsletter_subscription = Column(Boolean, default=False)

    user_id = Column(String(50), ForeignKey("users.id"), unique=True)
    user = relationship("User", lazy='subquery')

    def __init__(self, name: str, last_name: str, address: str, district: str, telephone_number: str, user_id: str,
                 key_customer=False, newsletter_subscription=False):
        self.user_id = user_id
        self.newsletter_subscription = newsletter_subscription
        self.key_customer = key_customer
        self.telephone_number = telephone_number
        self.district = district
        self.address = address
        self.last_name = last_name
        self.name = name

