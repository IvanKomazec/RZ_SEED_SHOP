from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4


class Admin(Base):
    __tablename__ = "admins"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    last_name = Column(String(100))

    user_id = Column(String(50), ForeignKey("users.id"), unique=True)
    user = relationship("User", lazy='subquery')

    def __init__(self, name: str, last_name: str, user_id: str):
        self.name = name
        self.last_name = last_name
        self.user_id = user_id
