from datetime import date

from app.db import SessionLocal
from app.orders.exceptions import CartNotFoundException
from app.users.user_exceptions import IdNotFoundException
from app.orders.repositories import CompletedOrderRepository, CartRepository, ProductOrderRepository
from app.users.repository import CustomerRepository
from app.variety_products.repositories import VarietyProductRepository


class CompletedOrderService:

    @staticmethod
    def create_completed_order(cart_id: str, customer_id: str, order_date: date.today(), order_value: float,
                               discount: bool = False, status: str = "pending"):
        with SessionLocal() as db:
            try:
                cart_repository = CartRepository(db)
                if cart_repository.get_cart_by_id(cart_id) is None:
                    raise CartNotFoundException("cart with provided id not found", 400)
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id) is None:
                    raise IdNotFoundException("customer with provided id not found", 400)
                completed_order_repository = CompletedOrderRepository(db)
                completed_order = completed_order_repository.create_completed_order(cart_id, customer_id, order_date,
                                                                                    order_value, discount, status)
                product_order_repository = ProductOrderRepository(db)
                variety_product_repository = VarietyProductRepository(db)
                cart_products = product_order_repository.get_all_product_orders_by_cart_id(cart_id)
                value = []
                for product in cart_products:
                    value.append(product.quantity*(variety_product_repository.get_product_price_by_id(product.variety_id)))
                completed_order.order_value = sum(value)
                if completed_order.order_value > 10000:
                    completed_order.discount = True
                if completed_order.discount is True:
                    completed_order.order_value *= 0.9
                return completed_order
            except Exception as e:
                raise e
