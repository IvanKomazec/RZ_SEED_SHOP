from sqlalchemy.exc import IntegrityError

from app.db import SessionLocal
from app.variety_products.repositories import VarietyTraitsRepository, VarietyProductRepository
from app.variety_products.exceptions import VarietyTraitsAlreadyExistException, VarietyNotFoundException


class VarietyTraitsService:
    @staticmethod
    def create_variety_traits(product_id: str, fruit_size_g: int, fruit_size_kg: float, maturity_days: int,
                              open_field: bool = True, indoor: bool = True, fresh_market: bool = True,
                              industry: bool = True, spring_production: bool = True, summer_production: bool = True,
                              autumn_production: bool = True, winter_production: bool = True):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                if variety_product_repository.get_variety_product_by_id(product_id):
                    variety_traits_repository = VarietyTraitsRepository(db)
                    variety_traits = variety_traits_repository.create_variety_traits(product_id, fruit_size_g,
                                                                                     fruit_size_kg, maturity_days,
                                                                                     open_field, indoor, fresh_market,
                                                                                     industry, spring_production,
                                                                                     summer_production, autumn_production,
                                                                                     winter_production)
                    return variety_traits
                raise VarietyNotFoundException("Variety with provided product ID not found", 400)
        except IntegrityError:
            raise VarietyTraitsAlreadyExistException("Variety traits with provided product ID already in DB", 400)
        except Exception as e:
            raise e
