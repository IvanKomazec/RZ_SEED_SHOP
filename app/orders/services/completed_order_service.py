from datetime import date

from app.db import SessionLocal
from app.orders.exceptions import CartNotFoundException, InvalidDateException, CompletedOrderNotFoundException
from app.users.user_exceptions import IdNotFoundException
from app.orders.repositories import (
    CompletedOrderRepository,
    CartRepository,
    ProductOrderRepository,
)
from app.users.repository import CustomerRepository
from app.variety_products.repositories import VarietyProductRepository


class CompletedOrderService:
    @staticmethod
    def create_completed_order(
        cart_id: str,
        customer_id: str,
        order_date: date.today(),
        order_value: float,
        discount: bool = False,
        status: str = "pending",
    ):
        with SessionLocal() as db:
            try:
                cart_repository = CartRepository(db)
                if cart_repository.get_cart_by_id(cart_id) is None:
                    raise CartNotFoundException("cart with provided id not found", 400)
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id) is None:
                    raise IdNotFoundException(
                        "customer with provided id not found", 400
                    )
                completed_order_repository = CompletedOrderRepository(db)
                completed_order = completed_order_repository.create_completed_order(
                    cart_id, customer_id, order_date, order_value, discount, status
                )
                cart_repository.update_cart_status_by_id(completed_order.cart_id)
                product_order_repository = ProductOrderRepository(db)
                variety_product_repository = VarietyProductRepository(db)
                cart_products = (
                    product_order_repository.get_all_product_orders_by_cart_id(cart_id)
                )
                value = []
                for product in cart_products:
                    value.append(
                        product.quantity
                        * (
                            variety_product_repository.get_product_price_by_id(
                                product.variety_id
                            )
                        )
                    )
                completed_order.order_value = sum(value)
                if completed_order.order_value > 10000:
                    completed_order.discount = True
                if completed_order.discount is True:
                    completed_order.order_value *= 0.9
                customer = customer_repository.get_customer_by_id(customer_id)
                if customer.key_customer is True:
                    completed_order.order_value *= 0.9
                return completed_order
            except Exception as e:
                raise e

    @staticmethod
    def get_all_completed_orders():
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                completed_orders = completed_order_repository.get_all_completed_orders()
                return completed_orders
        except Exception as e:
            raise e

    @staticmethod
    def get_all_completed_orders_by_status(status: str):
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                completed_orders = (
                    completed_order_repository.get_all_completed_orders_by_status(
                        status
                    )
                )
                return completed_orders
        except Exception as e:
            raise e

    @staticmethod
    def get_all_completed_orders_in_specified_period_by_status(
        status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int
    ):
        try:
            with SessionLocal() as db:
                if date(sy, sm, sd) > date.today():
                    raise InvalidDateException("Provided start date is not valid", 400)
                completed_order_repository = CompletedOrderRepository(db)
                orders_in_specific_period = \
                    completed_order_repository.get_all_completed_orders_in_specified_period_by_status(
                        status, sy, sm, sd, ey, em, ed)
                return orders_in_specific_period
        except Exception as e:
            raise e

    @staticmethod
    def get_total_sales_amount_for_specified_period_by_status(
        status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int
    ):
        try:
            with SessionLocal() as db:
                if date(sy, sm, sd) > date.today():
                    raise InvalidDateException("Provided start date is not valid", 400)
                completed_order_repository = CompletedOrderRepository(db)
                completed_orders_in_specified_period = \
                    completed_order_repository.get_all_completed_orders_in_specified_period_by_status(
                        status, sy, sm, sd, ey, em, ed)
                order_value_list = []
                for order in completed_orders_in_specified_period:
                    order_value_list.append(order.order_value)
                return sum(order_value_list)
        except Exception as e:
            raise e

    @staticmethod
    def get_product_orders_for_specified_period_by_status(
        status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int
    ):
        try:
            with SessionLocal() as db:
                if date(sy, sm, sd) > date.today():
                    raise InvalidDateException("Provided start date is not valid", 400)
                completed_order_repository = CompletedOrderRepository(db)
                completed_orders_in_specific_period = \
                    completed_order_repository.get_all_completed_orders_in_specified_period_by_status(
                        status, sy, sm, sd, ey, em, ed)
                cart_ids = [
                    order.cart_id for order in completed_orders_in_specific_period
                ]
                product_order_repository = ProductOrderRepository(db)
                product_orders = []
                for cart_id in cart_ids:
                    product_orders.append(
                        product_order_repository.get_all_product_orders_by_cart_id(
                            cart_id
                        )
                    )
                all_product_orders = []
                for product_ord in product_orders:
                    all_product_orders += product_ord
                # print("all_product_orders", all_product_orders)
                variety_product_repository = VarietyProductRepository(db)
                sorted_product_orders = []
                for product in all_product_orders:
                    sorted_product_orders.append(
                        {
                            variety_product_repository.get_variety_name_by_id(
                                product.variety_id
                            ): product.quantity
                        }
                    )
                sorted_product_dict = {}
                for prod_order in sorted_product_orders:
                    for key in prod_order.keys():
                        sorted_product_dict[key] = sorted_product_dict.get(key, 0) + prod_order[key]

                return sorted_product_dict
        except Exception as e:
            raise e

    # @staticmethod
    # def get_top5_bestselling_products(status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int):
    #     sorted_product_dict = CompletedOrderService.get_product_orders_for_specified_period_by_status(status, sy, sm,
    #                                                                                                   sd, ey, em, ed)
    #     top5_bestselling_products = []
    #     for item in sorted_product_dict.items():
    #         top5_bestselling_products.append(item)
    #     return sorted(top5_bestselling_products[0:4], reverse=True)

    @staticmethod
    def get_completed_order_by_id(completed_order_id: str):
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                completed_order = completed_order_repository.get_completed_order_by_id(completed_order_id)
                if completed_order is None:
                    raise CompletedOrderNotFoundException("completed order with provided id not found", 400)
                return completed_order
        except Exception as e:
            raise e

    @staticmethod
    def get_completed_orders_by_customer_id(customer_id: str):
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id) is None:
                    raise IdNotFoundException("Customer with provided id not found", 400)
                completed_orders = completed_order_repository.get_completed_orders_by_customer_id(customer_id)
                return completed_orders
        except Exception as e:
            raise e

    @staticmethod
    def update_completed_order_status_by_id(
        completed_order_id: str,
        status: str = "pending",
        discount: bool = "false",
        order_date: date = date.today(),
    ):
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                completed_order = completed_order_repository.\
                    update_completed_order_status_by_id(completed_order_id, status, discount, order_date)
                if completed_order is None:
                    raise CompletedOrderNotFoundException("completed order with provided id not found", 400)
                return completed_order
        except Exception as e:
            raise e

    @staticmethod
    def delete_completed_order_by_id(completed_order_id):
        try:
            with SessionLocal() as db:
                completed_order_repository = CompletedOrderRepository(db)
                if completed_order_repository.get_completed_order_by_id(completed_order_id) is None:
                    raise CompletedOrderNotFoundException("Completed order with provided id not found", 400)
                if completed_order_repository.delete_completed_order_by_id(completed_order_id):
                    return True
        except Exception as e:
            raise e


