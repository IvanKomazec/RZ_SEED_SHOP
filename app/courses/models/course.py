from sqlalchemy import Column, String
from uuid import uuid4

from app.db import Base


class Course(Base):
    __tablename__ = "courses"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    code = Column(String(100), unique=True)
    name = Column(String(100))
    description = Column(String(500))

    def __init__(self, code: str, name: str, description: str):
        self.code = code
        self.name = name
        self.description = description
