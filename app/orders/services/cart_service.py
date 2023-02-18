from datetime import date
from app.orders.repositories import CartRepository, ProductOrderRepository
from app.db import SessionLocal
from app.orders.exceptions import *
from app.users.repository import CustomerRepository
from app.users.user_exceptions import IdNotFoundException


class CartService:

    @staticmethod
    def create_cart(created_at: date.today(), customer_id: str, status: str = "pending"):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer = customer_repository.get_customer_by_id(customer_id)
                if customer is None:
                    raise IdNotFoundException("Customer with provided ID not in DB", 400)
                cart_repository = CartRepository(db)
                cart = cart_repository.create_cart(created_at, customer_id, status)
                if cart.created_at > date.today():
                    raise CartCreationDateInvalidException("Cart 'created_at' date not valid", 400)
                return cart

        except Exception as e:
            raise e

    @staticmethod
    def get_all_carts():
        with SessionLocal() as db:
            cart_repository = CartRepository(db)
            all_carts = cart_repository.get_all_carts()
            return all_carts

    @staticmethod
    def get_cart_by_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_repository = CartRepository(db)
                cart = cart_repository.get_cart_by_id(cart_id)
                if cart is None:
                    raise CartNotFoundException("Cart with provided id not found", 400)
                return cart
        except Exception as e:
            raise e

    @staticmethod
    def update_cart_status_by_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_repository = CartRepository(db)
                cart = cart_repository.update_cart_status_by_id(cart_id)
                if cart is None:
                    raise CartNotFoundException("Cart with provided id not found", 400)
                return cart
        except Exception as e:
            raise e

    @staticmethod
    def delete_cart_by_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_repository = CartRepository(db)
                if cart_repository.get_cart_by_id(cart_id) is None:
                    raise CartNotFoundException("Cart with provided id not found", 400)
                if cart_repository.delete_cart_by_id(cart_id):
                    return True
        except Exception as e:
            raise e


