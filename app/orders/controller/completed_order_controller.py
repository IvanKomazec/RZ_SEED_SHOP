from datetime import date

from fastapi import HTTPException, Response

from app.orders.exceptions import CartNotFoundException, InvalidDateException, CompletedOrderNotFoundException
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

    @staticmethod
    def get_top5_bestselling_products(status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int):
        product_dict = CompletedOrderService.get_product_orders_for_specified_period_by_status(status, sy, sm,
                                                                                                      sd, ey, em, ed)
        sorted_product_dict = dict(sorted(product_dict.items(), key=lambda item: item[1], reverse=True))
        top5list = []
        for item in sorted_product_dict.items():
            top5list.append(item)
        return top5list[0:5]


    @staticmethod
    def get_completed_order_by_id(completed_order_id: str):
        try:
            completed_order = CompletedOrderService.get_completed_order_by_id(completed_order_id)
            return completed_order
        except CompletedOrderNotFoundException:
            raise HTTPException(400, "Order with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_completed_orders_by_customer_id(customer_id: str):
        try:
            completed_orders = CompletedOrderService.get_completed_orders_by_customer_id(customer_id)
            return completed_orders
        except IdNotFoundException:
            raise HTTPException(400, "Customer with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def update_completed_order_status_by_id(
        completed_order_id: str,
        status: str = "pending",
        discount: bool = "false",
        order_date: date = date.today(),
    ):
        try:
            completed_order = CompletedOrderService.update_completed_order_status_by_id(completed_order_id, status,
                                                                                        discount, order_date)
            return completed_order
        except CompletedOrderNotFoundException:
            raise HTTPException(400, "Order with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def delete_completed_order_by_id(completed_order_id):
        try:
            if CompletedOrderService.delete_completed_order_by_id(completed_order_id):
                return Response("delete successful", 200)
        except CompletedOrderNotFoundException:
            raise HTTPException(400, "Order with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

