from sqlalchemy.exc import IntegrityError, DatabaseError, InterfaceError
from sqlalchemy.orm import Session
from app.variety_products.exceptions import VarietyTraitsNotFoundException
from app.variety_products.models import VarietyTraits, VarietyProduct


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

    def get_variety_traits_by_id(self, variety_traits_id: str):
        try:
            variety_traits = self.db.query(VarietyTraits).filter(VarietyTraits.id == variety_traits_id).first()
            return variety_traits
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_variety_traits_by_variety_product_id(self, variety_product_id: str):
        try:
            variety_traits = self.db.query(VarietyTraits).filter(VarietyTraits.product_id == variety_product_id).first()
            return variety_traits
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_variety_traits_by_product_name(self, variety_name: str):
        try:
            variety_traits = self.db.query(VarietyTraits).join(VarietyProduct)\
                .filter(VarietyTraits.product_id == VarietyProduct.id, VarietyProduct.name == variety_name).first()
            return variety_traits
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_variety_traits_by_id(self, variety_traits_id: str, fruit_size_g: int, fruit_size_kg: float,
                                    maturity_days: int, open_field: bool = True, indoor: bool = True,
                                    fresh_market: bool = True, industry: bool = True, spring_production: bool = True,
                                    summer_production: bool = True, autumn_production: bool = True,
                                    winter_production: bool = True):
        try:
            variety_traits = self.db.query(VarietyTraits).filter(VarietyTraits.id == variety_traits_id).first()
            if not variety_traits:
                raise VarietyTraitsNotFoundException("Variety traits with provided ID not found", 400)
            if fruit_size_g is not None:
                variety_traits.fruit_size_g = fruit_size_g
            if fruit_size_kg is not None:
                variety_traits.fruit_size_kg = fruit_size_kg
            if maturity_days is not None:
                variety_traits.maturity_days = maturity_days
            # if open_field is not None:
            variety_traits.open_field = open_field
            # if indoor is not None:
            variety_traits.indoor = indoor
            # if fresh_market is not None:
            variety_traits.fresh_market = fresh_market
            # if industry is not None:
            variety_traits.industry = industry
            # if spring_production is not None:
            variety_traits.spring_production = spring_production
            # if summer_production is not None:
            variety_traits.summer_production = summer_production
            # if autumn_production is not None:
            variety_traits.autumn_production = autumn_production
            # if winter_production is not None:
            variety_traits.winter_production = winter_production
            self.db.add(variety_traits)
            self.db.commit()
            self.db.refresh(variety_traits)
            return variety_traits
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_variety_traits_by_id(self, variety_traits_id: str):
        try:
            variety_traits = self.db.query(VarietyTraits).filter(VarietyTraits.id == variety_traits_id).first()
            if variety_traits is None:
                raise VarietyTraitsNotFoundException(f"Variety traits with provided id not found.", 400)
            self.db.delete(variety_traits)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee
