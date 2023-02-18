from datetime import date

from fastapi import HTTPException

from app.orders.exceptions import CartNotFoundException
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
