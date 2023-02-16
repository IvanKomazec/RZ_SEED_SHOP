from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.variety_products.exceptions import VarietyNotFoundException
from app.variety_products.services import VarietyTraitsService


class VarietyTraitsController:

    @staticmethod
    def create_variety_traits(product_id: str, fruit_size_g: int, fruit_size_kg: float, maturity_days: int,
                              open_field: bool = True, indoor: bool = True, fresh_market: bool = True,
                              industry: bool = True, spring_production: bool = True, summer_production: bool = True,
                              autumn_production: bool = True, winter_production: bool = True):
        try:
            variety_traits = VarietyTraitsService.create_variety_traits(product_id, fruit_size_g,
                                                                        fruit_size_kg, maturity_days,
                                                                        open_field, indoor, fresh_market,
                                                                        industry, spring_production,
                                                                        summer_production, autumn_production,
                                                                        winter_production)
            return variety_traits
        except VarietyNotFoundException:
            raise HTTPException(status_code=400, detail="Variety with provided product ID not found")
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Variety traits with provided product ID already in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))