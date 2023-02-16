from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer, Float
from uuid import uuid4


class VarietyTraits(Base):
    __tablename__ = "variety_traits"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    open_field = Column(Boolean, default=False)
    indoor = Column(Boolean, default=False)
    fresh_market = Column(Boolean, default=False)
    industry = Column(Boolean, default=False)
    fruit_size_g = Column(Integer)
    fruit_size_kg = Column(Float)
    maturity_days = Column(Integer)
    spring_production = Column(Boolean, default=False)
    summer_production = Column(Boolean, default=False)
    autumn_production = Column(Boolean, default=False)
    winter_production = Column(Boolean, default=False)

    product_id = Column(String(50), ForeignKey("variety_products.id"), unique=True)
    product = relationship("VarietyProduct", lazy='subquery')

    def __init__(self, product_id, fruit_size_g, fruit_size_kg, maturity_days, open_field=False, indoor=False,
                 fresh_market=False, industry=False, spring_production=False, summer_production=False,
                 autumn_production=False, winter_production=False):
        self.product_id = product_id
        self.fruit_size_g = fruit_size_g
        self.fruit_size_kg = fruit_size_kg
        self.maturity_days = maturity_days
        self.open_field = open_field
        self.indoor = indoor
        self.fresh_market = fresh_market
        self.industry = industry
        self.spring_production = spring_production
        self.summer_production = summer_production
        self.autumn_production = autumn_production
        self.winter_production = winter_production
