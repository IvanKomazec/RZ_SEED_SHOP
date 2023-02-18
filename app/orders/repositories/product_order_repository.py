from app.orders.models import ProductOrder
from sqlalchemy.exc import IntegrityError, DatabaseError, InterfaceError
from sqlalchemy.orm import Session
from app.orders.exceptions import ProductOrderNotFoundException


class ProductOrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_product_order(self, quantity: int, variety_id: str, cart_id: str):
        try:
            product_order = ProductOrder(quantity, variety_id, cart_id)
            self.db.add(product_order)
            self.db.commit()
            self.db.refresh(product_order)
            return product_order
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_product_order_by_id(self, product_order_id: str):
        try:
            product_order = self.db.query(ProductOrder).filter(ProductOrder.id == product_order_id).first()
            return product_order
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_all_product_orders(self):
        all_product_orders = self.db.query(ProductOrder).all()
        return all_product_orders

    def get_all_product_orders_by_cart_id(self, cart_id: str):
        all_product_orders = self.db.query(ProductOrder).filter(ProductOrder.cart_id == cart_id).all()
        return all_product_orders

    def update_product_order_quantity_by_id(self, product_order_id: str, quantity: int):
        try:
            product_order = self.db.query(ProductOrder).filter(ProductOrder.id == product_order_id).first()
            product_order.quantity = quantity
            self.db.commit()
            self.db.refresh(product_order)
            return product_order
        except AttributeError as e:
            raise e
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_product_order_by_id(self, product_order_id: str):
        try:
            product_order = self.db.query(ProductOrder).filter(ProductOrder.id == product_order_id).first()
            self.db.delete(product_order)
            self.db.commit()
            return True
        except AttributeError as e:
            raise e
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee
