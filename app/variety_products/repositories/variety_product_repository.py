from app.variety_products.exceptions.variety_product_exceptions import InvalidDateInputException
from app.variety_products.models import VarietyProduct, VarietyTraits
from app.variety_products.exceptions import *
from sqlalchemy.exc import IntegrityError, DatabaseError, InterfaceError
from sqlalchemy.orm import Session
from datetime import date, timedelta


class VarietyProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, crop: str, price: float, package_size: str, stock: int,
                       added_to_inventory: date = date.today(), on_discount=False):
        try:
            variety_product = VarietyProduct(name, crop, price, package_size, stock, added_to_inventory, on_discount)
            if variety_product.added_to_inventory > date.today():
                raise InvalidDateInputException("Invalid date for 'added to inventory' input", 400)
            self.db.add(variety_product)
            self.db.commit()
            self.db.refresh(variety_product)
            return variety_product
        except IntegrityError as e:
            raise e
        except Exception as ee:
            raise ee

    def get_all_variety_products(self):
        variety_products = self.db.query(VarietyProduct).all()
        return variety_products

    def get_variety_product_by_id(self, variety_id: str):
        try:
            variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_id).first()
            return variety_product
        except DatabaseError as e:
            raise e

    def get_variety_products_by_name(self, variety_name: str):
        try:
            variety_products = self.db.query(VarietyProduct).filter(VarietyProduct.name.like(variety_name + "%")).all()
            return variety_products
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_variety_products_by_crop(self, crop: str):
        try:
            variety_products = self.db.query(VarietyProduct).filter(VarietyProduct.crop.like(crop + "%")).all()
            return variety_products
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_available_variety_products_by_crop(self, crop: str):
        try:
            variety_product_in_stock = self.db.query(VarietyProduct).filter(VarietyProduct.crop.like(crop + "%"),
                                                                            VarietyProduct.stock > 0).all()
            return variety_product_in_stock
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_all_new_variety_products(self):
        try:
            date_point = date.today() - timedelta(100)
            new_products = self.db.query(VarietyProduct).filter(VarietyProduct.added_to_inventory > date_point).all()
            return new_products
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_variety_products_on_discount(self):
        try:
            discount_products = self.db.query(VarietyProduct).filter(VarietyProduct.on_discount == True).all()
            return discount_products
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_variety_product_by_id(self, variety_id: str):
        try:
            variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_id).first()
            if variety_product is None:
                raise VarietyNotFoundException(f"Variety with provided id: {variety_id} not found.", 400)
            self.db.delete(variety_product)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_variety_product_by_id(self, variety_id: str, name: str, crop: str, price: float, package_size: str,
                                     stock: int, added_to_inventory: date, on_discount: bool = False):
        try:
            variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_id).first()
            if variety_product is None:
                raise VarietyNotFoundException(f"Variety with provided id: {variety_id} not found.", 400)
            if name is not None:
                variety_product.name = name
            if crop is not None:
                variety_product.crop = crop
            if price is not None:
                variety_product.price = price
            if package_size is not None:
                variety_product.package_size = package_size
            if stock is not None:
                variety_product.stock = stock
            variety_product.added_to_inventory = added_to_inventory
            variety_product.on_discount = on_discount
            self.db.add(variety_product)
            self.db.commit()
            self.db.refresh(variety_product)
            return variety_product
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_product_price_by_id(self, variety_product_id):
        variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_product_id).first()
        return variety_product.price

    def get_variety_name_by_id(self, variety_id):
        try:
            variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_id).first()
            return variety_product.name
        except DatabaseError as e:
            raise e

    def update_stock(self, variety_id: str, quantity: int):
        variety_product = self.db.query(VarietyProduct).filter(VarietyProduct.id == variety_id).first()
        variety_product.stock = variety_product.stock - quantity
        return variety_product

    def filter_by_variety_traits(self, fruit_size_g: int, maturity_days: int, open_field: bool,
                                 indoor: bool, fresh_market: bool, industry: bool, spring_production: bool,
                                 summer_production: bool, autumn_production: bool, winter_production: bool):
        try:
            varieties = self.db.query(VarietyProduct).join(VarietyTraits).\
                filter(VarietyProduct.id == VarietyTraits.product_id).\
                filter(VarietyTraits.fruit_size_g.between(fruit_size_g-25, fruit_size_g+25)).\
                filter(VarietyTraits.maturity_days.between(maturity_days-5, maturity_days+5)).\
                filter(VarietyTraits.open_field == open_field).\
                filter(VarietyTraits.indoor == indoor).\
                filter(VarietyTraits.fresh_market == fresh_market).\
                filter(VarietyTraits.industry == industry).\
                filter(VarietyTraits.spring_production == spring_production).\
                filter(VarietyTraits.summer_production == summer_production).\
                filter(VarietyTraits.autumn_production == autumn_production).\
                filter(VarietyTraits.winter_production == winter_production).all()
            return varieties
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee