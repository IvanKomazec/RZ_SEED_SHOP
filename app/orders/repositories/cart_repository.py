from datetime import date

from sqlalchemy.exc import IntegrityError, InterfaceError, DatabaseError

from app.orders.models import Cart
from sqlalchemy.orm import Session


class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_cart(self, created_at: date.today(), customer_id: str, status: str = "pending"):
        try:
            cart = Cart(created_at, customer_id, status)
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
            return cart
        except IntegrityError as e:
            raise e
        except InterfaceError as e:
            raise e

    def get_all_carts(self):
        all_carts = self.db.query(Cart).all()
        return all_carts

    def get_cart_by_id(self, cart_id: str):
        try:
            cart = self.db.query(Cart).filter(Cart.id == cart_id).first()
            return cart
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_cart_status_by_id(self, cart_id: str):
        try:
            cart = self.db.query(Cart).filter(Cart.id == cart_id).first()
            cart.status = "processed"
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
            return cart
        except AttributeError as e:
            raise e
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_cart_by_id(self, cart_id: str):
        try:
            cart = self.db.query(Cart).filter(Cart.id == cart_id).first()
            self.db.delete(cart)
            self.db.commit()
            return True
        except AttributeError as e:
            raise e
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee



