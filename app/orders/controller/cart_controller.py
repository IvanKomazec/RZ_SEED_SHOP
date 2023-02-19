from datetime import date
from app.orders.exceptions import *
from fastapi import HTTPException, Response

from app.orders.services import CartService, ProductOrderService


class CartController:

    @staticmethod
    def create_cart(created_at: date.today(), status: str = "pending"):
        try:
            cart = CartService.create_cart(created_at, status)
            return cart
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

    @staticmethod
    def get_cart_with_list_of_product_orders(cart_id: str):
        try:
            cart = CartService.get_cart_by_id(cart_id)
        except Exception:
            raise HTTPException(400, "Cart with provided ID NOT found")
        try:
            product_orders = ProductOrderService.get_all_product_orders_by_cart_id(cart_id)
            product_orders_list = []
            for product in product_orders:
                product_orders_list.append(ProductOrderService.get_product_order_by_id(product.id))
            cart.product_orders = product_orders_list
            return cart
        except Exception as e:
            raise HTTPException(500, str(e))
