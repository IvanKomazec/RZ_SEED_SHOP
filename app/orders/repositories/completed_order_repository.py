from datetime import date

from sqlalchemy.exc import IntegrityError, InterfaceError
from sqlalchemy.orm import Session

from app.orders.models.completed_order import CompletedOrder


class CompletedOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_completed_order(self, cart_id: str, customer_id: str, order_date: date.today(), order_value: float,
                               discount: bool = False, status: str = "pending"):
        try:
            completed_order = CompletedOrder(cart_id, customer_id, order_date, order_value, discount, status)
            self.db.add(completed_order)
            self.db.commit()
            self.db.refresh(completed_order)
            return completed_order
        except IntegrityError as e:
            raise e
        except InterfaceError as ee:
            raise ee


