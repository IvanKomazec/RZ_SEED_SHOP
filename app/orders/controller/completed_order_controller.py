from datetime import date

from fastapi import HTTPException

from app.orders.exceptions import CartNotFoundException, InvalidDateException
from app.orders.services import CompletedOrderService
from app.users.user_exceptions import IdNotFoundException


class CompletedOrderController:

    @staticmethod
    def create_completed_order(cart_id: str, customer_id: str, order_date: date.today(), order_value: float,
                               discount: bool = False, status: str = "pending"):
        try:
            completed_order = CompletedOrderService.create_completed_order(cart_id, customer_id, order_date,
                                                                           order_value, discount, status)
            return completed_order
        except CartNotFoundException:
            raise HTTPException(400, "cart with provided id not found")
        except IdNotFoundException:
            raise HTTPException(400, "provided customer id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_completed_orders():
        try:
            completed_orders = CompletedOrderService.get_all_completed_orders()
            return completed_orders
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_completed_orders_by_status(status: str):
        try:
            completed_orders = CompletedOrderService.get_all_completed_orders_by_status(status)
            return completed_orders
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_completed_orders_in_specified_period_by_status(status: str, sy: int, sm: int, sd: int, ey: int,
                                                               em: int, ed: int):
        try:
            orders_in_specific_period = CompletedOrderService.\
                get_all_completed_orders_in_specified_period_by_status(status, sy, sm, sd, ey, em, ed)
            return orders_in_specific_period
        except InvalidDateException:
            raise HTTPException(400, "Provided start date is not valid")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_total_sales_amount_for_specified_period_by_status(status: str, sy: int, sm: int, sd: int, ey: int, em: int,
                                                              ed: int):
        try:
            all_orders_value = CompletedOrderService.\
                get_total_sales_amount_for_specified_period_by_status(status, sy, sm, sd, ey, em, ed)
            return all_orders_value
        except InvalidDateException:
            raise HTTPException(400, "Provided start date is not valid")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_product_orders_for_specified_period(status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int):
        try:
            product_orders_for_specified_period = CompletedOrderService.\
                get_product_orders_for_specified_period_by_status(status, sy, sm, sd, ey, em, ed)
            return product_orders_for_specified_period
        except InvalidDateException:
            raise HTTPException(400, "Provided start date is not valid")
        except Exception as e:
            raise HTTPException(500, str(e))
