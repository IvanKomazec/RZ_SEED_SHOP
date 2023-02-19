from datetime import date

from app.db.database import Base
from sqlalchemy import Column, String, Date
from uuid import uuid4


class Cart(Base):
    __tablename__ = "carts"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    created_at = Column(Date, nullable=False)
    status = Column(String(50), default="pending")

    def __init__(self, created_at: date.today(), status: str):
        self.created_at = created_at
        self.status = status
