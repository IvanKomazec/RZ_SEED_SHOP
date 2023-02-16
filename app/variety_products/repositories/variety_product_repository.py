from app.variety_products.models import VarietyProduct
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
            self.db.add(variety_product)
            self.db.commit()
            self.db.refresh(variety_product)
            return variety_product
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

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
                raise VarietyNotFoundException(f"Variety with provided name: {variety_id} not found.", 400)
            self.db.delete(variety_product)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee