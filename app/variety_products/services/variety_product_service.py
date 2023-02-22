from sqlalchemy.exc import IntegrityError
from app.db import SessionLocal
from app.variety_products.exceptions.variety_product_exceptions import InvalidDateInputException, MatchNotFoundException
from app.variety_products.repositories import VarietyProductRepository
from app.variety_products.exceptions import *
from datetime import date


class VarietyProductService:

    @staticmethod
    def create_variety_product(name: str, crop: str, price: float, package_size: str, stock: int,
                               added_to_inventory: date = date.today(), on_discount=False):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_product = variety_product_repository.create_product(name, crop, price, package_size, stock,
                                                                            added_to_inventory, on_discount)
                if variety_product.added_to_inventory > date.today():
                    raise InvalidDateInputException("Invalid date for 'added to inventory' input", 400)
                return variety_product
        except IntegrityError:
            raise VarietyAlreadyInDatabaseException("Variety with provided ID already in DB", 400)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_variety_products():
        with SessionLocal() as db:
            variety_product_repository = VarietyProductRepository(db)
            all_variety_products = variety_product_repository.get_all_variety_products()
            return all_variety_products

    @staticmethod
    def get_variety_product_by_id(variety_id: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_product = variety_product_repository.get_variety_product_by_id(variety_id)
                if variety_product is None:
                    raise VarietyIdNotFoundException("Variety with provided ID not in DB", 400)
                return variety_product
        except Exception as e:
            raise e

    @staticmethod
    def get_variety_products_by_name(variety_name: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_products = variety_product_repository.get_variety_products_by_name(variety_name)
                if not variety_products:
                    raise VarietyNotFoundException("Variety with provided name not in DB", 400)
                return variety_products
        except Exception as e:
            raise e

    @staticmethod
    def get_variety_products_by_crop(crop: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_products = variety_product_repository.get_variety_products_by_name(crop)
                if not variety_products:
                    raise VarietyNotFoundException("Provided crop not in DB", 400)
                return variety_products
        except Exception as e:
            raise e

    @staticmethod
    def get_available_variety_products_by_crop(crop: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_products = variety_product_repository.get_variety_products_by_crop(crop)
                if not variety_products:
                    raise VarietyNotFoundException("Varieties with provided crop type not found", 400)
                variety_products_in_stock = variety_product_repository.get_available_variety_products_by_crop(crop)
                if not variety_products_in_stock:
                    raise VarietyOutOfStockException("Variety out of stock", 400)
                return variety_products_in_stock
        except Exception as ee:
            raise ee

    @staticmethod
    def get_all_new_variety_products():
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                new_varieties = variety_product_repository.get_all_new_variety_products()
                if not new_varieties:
                    raise NoNewVarietiesException("No new varieties at this point", 400)
                return new_varieties
        except Exception as e:
            raise e

    @staticmethod
    def get_variety_products_on_discount():
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                discount_varieties = variety_product_repository.get_variety_products_on_discount()
                if not discount_varieties:
                    raise NoDiscountVarietiesException("No discount varieties at this point", 400)
                return discount_varieties
        except Exception as e:
            raise e

    @staticmethod
    def delete_variety_product_by_id(variety_id: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                if variety_product_repository.delete_variety_product_by_id(variety_id):
                    return True
                else:
                    raise VarietyNotFoundException("variety with provided ID not in DB", 400)
        except Exception as e:
            raise e

    @staticmethod
    def update_variety_product_by_id(variety_id: str, name: str, crop: str, price: float, package_size: str,
                                     stock: int, added_to_inventory: date, on_discount: bool = False):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_product = variety_product_repository.update_variety_product_by_id(variety_id, name, crop, price,
                                                                                          package_size, stock,
                                                                                          added_to_inventory,
                                                                                          on_discount)
                return variety_product
        except VarietyNotFoundException as e:
            raise e
        except Exception as ee:
            raise ee

    @staticmethod
    def filter_by_variety_traits(fruit_size_g: int, maturity_days: int, open_field: bool,
                                 indoor: bool, fresh_market: bool, industry: bool, spring_production: bool,
                                 summer_production: bool, autumn_production: bool, winter_production: bool):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                filtered_varieties = variety_product_repository.filter_by_variety_traits(fruit_size_g, maturity_days,
                                                                                         open_field, indoor,
                                                                                         fresh_market, industry,
                                                                                         spring_production,
                                                                                         summer_production,
                                                                                         autumn_production,
                                                                                         winter_production)
                if len(filtered_varieties) == 0:
                    raise MatchNotFoundException("No varieties match the criteria", 400)
                return filtered_varieties
        except Exception as e:
            raise e
