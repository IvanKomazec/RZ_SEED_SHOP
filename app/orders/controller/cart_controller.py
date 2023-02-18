from datetime import date
from app.orders.exceptions import *
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.users.user_exceptions import IdNotFoundException

from app.orders.services import CartService


class CartController:

    @staticmethod
    def create_cart(created_at: date.today(), customer_id: str, status: str = "pending"):
        try:
            cart = CartService.create_cart(created_at, customer_id, status)
            return cart
        except IdNotFoundException:
            raise HTTPException(400, "Customer with provided ID not in DB")
        except CartCreationDateInvalidException:
            raise HTTPException(400, "Cart 'created_at' date not valid")
        # except IntegrityError:
        #     raise HTTPException(400, "provided cart id with 'pending' status already in DB")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_carts():
        try:
            carts = CartService.get_all_carts()
            return carts
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_cart_by_id(cart_id):
        try:
            cart = CartService.get_cart_by_id(cart_id)
            return cart
        except CartNotFoundException:
            raise HTTPException(400, "Cart with provided ID not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def update_cart_status_by_id(cart_id: str):
        try:
            cart = CartService.update_cart_status_by_id(cart_id)
            return cart
        except CartNotFoundException:
            raise HTTPException(400, "Cart with provided ID not found")
        except AttributeError:
            raise HTTPException(400, "Cart with provided ID NOT found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def delete_cart_by_id(cart_id: str):
        try:
            if CartService.delete_cart_by_id(cart_id):
                return Response("Cart with provided id is deleted", 200)
        except CartNotFoundException:
            raise HTTPException(400, "Cart with provided ID not found")
        except AttributeError:
            raise HTTPException(400, "Cart with provided ID NOT found")
        except Exception as e:
            raise HTTPException(500, str(e))

