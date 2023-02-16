from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.variety_products.models.variety_traits import VarietyTraits


class VarietyTraitsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_variety_traits(self, product_id: str, fruit_size_g: int, fruit_size_kg: float, maturity_days: int,
                              open_field: bool = True, indoor: bool = True, fresh_market: bool = True,
                              industry: bool = True, spring_production: bool = True, summer_production: bool = True,
                              autumn_production: bool = True, winter_production: bool = True):
        try:
            variety_traits = VarietyTraits(product_id, fruit_size_g, fruit_size_kg, maturity_days, open_field, indoor,
                                           fresh_market, industry, spring_production, summer_production,
                                           autumn_production, winter_production)
            self.db.add(variety_traits)
            self.db.commit()
            self.db.refresh(variety_traits)
            return variety_traits
        except IntegrityError as e:
            raise e
        except Exception as ee:
            raise ee
