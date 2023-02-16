from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.variety_products.exceptions import VarietyNotFoundException, VarietyTraitsNotFoundException
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

    @staticmethod
    def get_variety_traits_by_id(variety_traits_id):
        try:
            variety_traits = VarietyTraitsService.get_variety_traits_by_id(variety_traits_id)
            return variety_traits
        except VarietyTraitsNotFoundException:
            raise HTTPException(status_code=400, detail="Variety traits with provided ID not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_traits_by_product_id(product_id: str):
        try:
            variety_traits = VarietyTraitsService.get_variety_traits_by_product_id(product_id)
            return variety_traits
        except VarietyTraitsNotFoundException:
            raise HTTPException(status_code=400, detail="Variety traits with provided product ID not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_traits_by_product_name(product_name: str):
        try:
            variety_traits = VarietyTraitsService.get_variety_traits_by_product_name(product_name)
            return variety_traits
        except VarietyTraitsNotFoundException:
            raise HTTPException(status_code=400, detail="Variety traits with provided product name not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_variety_traits_by_id(variety_traits_id: str, fruit_size_g: int, fruit_size_kg: float,
                                    maturity_days: int, open_field: bool = True, indoor: bool = True,
                                    fresh_market: bool = True, industry: bool = True, spring_production: bool = True,
                                    summer_production: bool = True, autumn_production: bool = True,
                                    winter_production: bool = True):
        try:
            variety_traits = VarietyTraitsService.update_variety_traits_by_id\
                (variety_traits_id, fruit_size_g, fruit_size_kg, maturity_days, open_field, indoor, fresh_market,
                 industry, spring_production, summer_production, autumn_production, winter_production)
            return variety_traits
        except VarietyTraitsNotFoundException:
            raise HTTPException(status_code=400, detail="Variety traits with provided ID not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_variety_traits_by_id(variety_traits_id: str):
        try:
            if VarietyTraitsService.delete_variety_traits_by_id(variety_traits_id):
                return Response(content=f"Variety traits with provided ID - {variety_traits_id} is deleted",
                                status_code=200)
        except VarietyTraitsNotFoundException:
            raise HTTPException(400, "variety traits with provided id not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))