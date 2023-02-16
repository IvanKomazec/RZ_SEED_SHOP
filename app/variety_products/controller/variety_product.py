from sqlalchemy.exc import IntegrityError

from app.variety_products.services import VarietyProductService
from app.variety_products.exceptions import *
from datetime import date
from fastapi import HTTPException, Response


class VarietyProductController:

    @staticmethod
    def create_variety_product(name: str, crop: str, price: float, package_size: str, stock: int,
                               added_to_inventory: date = date.today(), on_discount=False):
        try:
            variety_product = VarietyProductService.create_variety_product(name, crop, price, package_size, stock,
                                                                           added_to_inventory, on_discount)
            return variety_product
        except IntegrityError:
            raise HTTPException(status_code=400, detail="variety already in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_product_by_id(variety_id: str):
        try:
            variety_product = VarietyProductService.get_variety_product_by_id(variety_id)
            return variety_product
        except VarietyIdNotFoundException:
            raise HTTPException(400, "Provided variety ID not DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_variety_products():
        try:
            all_varieties = VarietyProductService.get_all_variety_products()
            return all_varieties
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_products_by_name(variety_name: str):
        try:
            variety_products = VarietyProductService.get_variety_products_by_name(variety_name)
            return variety_products
        except VarietyNotFoundException:
            raise HTTPException(400, "Provided name not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_products_by_crop(crop: str):
        try:
            variety_products = VarietyProductService.get_variety_products_by_name(crop)
            return variety_products
        except VarietyNotFoundException:
            raise HTTPException(400, "Provided crop not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_available_products_by_crop(crop):
        try:
            variety_products = VarietyProductService.get_available_variety_products_by_crop(crop)
            return variety_products
        except VarietyNotFoundException:
            raise HTTPException(400, "Varieties with provided crop type not found")
        except VarietyOutOfStockException:
            raise HTTPException(400, "Varieties out of stock")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_new_variety_products():
        try:
            new_varieties = VarietyProductService.get_all_new_variety_products()
            return new_varieties
        except NoNewVarietiesException:
            raise HTTPException(400, "There are no new varieties at this point")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_variety_products_on_discount():
        try:
            discount_varieties = VarietyProductService.get_variety_products_on_discount()
            return discount_varieties
        except NoDiscountVarietiesException:
            raise HTTPException(400, "There are no discount varieties at this point")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_variety_product_by_id(variety_id: str):
        try:
            if VarietyProductService.delete_variety_product_by_id(variety_id):
                return Response(content=f"Variety with provided ID - {variety_id} is deleted", status_code=200)
        except VarietyNotFoundException:
            raise HTTPException(400, "variety with provided id not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_variety_product_by_id(variety_id: str, name: str, crop: str, price: float, package_size: str,
                                     stock: int, added_to_inventory: date, on_discount: bool = False):
        try:
            variety_product = VarietyProductService.update_variety_product_by_id(variety_id, name, crop, price,
                                                                                 package_size, stock, added_to_inventory,
                                                                                 on_discount)
            return variety_product
        except VarietyNotFoundException:
            raise HTTPException(400, "variety with provided id not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))