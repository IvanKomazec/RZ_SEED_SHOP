from sqlalchemy.exc import IntegrityError

from app.orders.services import ProductOrderService
from app.orders.exceptions import CartNotFoundException, ProductOrderNotFoundException
from app.variety_products.exceptions import VarietyIdNotFoundException, VarietyOutOfStockException

from fastapi import HTTPException, Response


class ProductOrderController:

    @staticmethod
    def create_product_order(quantity: int, variety_id: str, cart_id: str):
        try:
            product_order = ProductOrderService.create_product_order(quantity, variety_id, cart_id)
            return product_order
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except VarietyIdNotFoundException:
            raise HTTPException(status_code=400, detail="variety with provided id not found")
        except VarietyOutOfStockException:
            raise HTTPException(status_code=400, detail="not enough variety on stock at this point")
        except CartNotFoundException:
            raise HTTPException(status_code=400, detail="cart with provided id not found")

    @staticmethod
    def get_all_product_orders():
        try:
            all_product_orders = ProductOrderService.get_all_product_orders()
            return all_product_orders
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_product_orders_by_cart_id(cart_id: str):
        try:
            all_product_orders = ProductOrderService.get_all_product_orders_by_cart_id(cart_id)
            return all_product_orders
        except CartNotFoundException:
            raise HTTPException(400, "provided cart id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_product_order_by_id(product_order_id: str):
        try:
            product_order = ProductOrderService.get_product_order_by_id(product_order_id)
            return product_order
        except ProductOrderNotFoundException:
            raise HTTPException(400, "provided product order id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def update_product_order_quantity_by_id(product_order_id: str, quantity: int, variety_id: str):
        try:
            product_order = ProductOrderService.update_product_order_quantity_by_id(product_order_id, quantity,
                                                                                    variety_id)
            return product_order
        except VarietyOutOfStockException:
            raise HTTPException(status_code=400, detail="not enough variety on stock at this moment")
        except AttributeError:
            raise HTTPException(400, "product_order with provided id not found")
        except ProductOrderNotFoundException:
            raise HTTPException(400, "product_order with provided id not found")
        except VarietyIdNotFoundException:
            raise HTTPException(400, "Variety id with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def delete_product_order_by_id(product_order_id: str):
        try:
            if ProductOrderService.delete_product_order_by_id(product_order_id):
                return Response("product order with provided id deleted", 200)
        except AttributeError:
            raise HTTPException(400, "product_order with provided id not found")
        except ProductOrderNotFoundException:
            raise HTTPException(400, "product_order with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))
