from datetime import date

from sqlalchemy.exc import IntegrityError, InterfaceError, DatabaseError
from sqlalchemy.orm import Session

from app.orders.exceptions import CompletedOrderNotFoundException
from app.orders.models.completed_order import CompletedOrder


class CompletedOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_completed_order(
        self,
        cart_id: str,
        customer_id: str,
        order_date: date.today(),
        order_value: float,
        discount: bool = False,
        status: str = "pending",
    ):
        try:
            completed_order = CompletedOrder(
                cart_id, customer_id, order_date, order_value, discount, status
            )
            self.db.add(completed_order)
            self.db.commit()
            self.db.refresh(completed_order)
            return completed_order
        except IntegrityError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_all_completed_orders(self):
        completed_orders = self.db.query(CompletedOrder).all()
        return completed_orders

    def get_all_completed_orders_by_status(self, status: str):
        completed_orders = (
            self.db.query(CompletedOrder).filter(CompletedOrder.status == status).all()
        )
        return completed_orders

    def get_all_completed_orders_in_specified_period_by_status(
        self, status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int
    ):
        try:
            finalized_orders_in_specific_period = (
                self.db.query(CompletedOrder)
                .filter(
                    CompletedOrder.order_date.between(
                        date(sy, sm, sd), date(ey, em, ed)
                    ),
                    CompletedOrder.status == status,
                )
                .all()
            )
            return finalized_orders_in_specific_period
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_completed_order_by_id(self, completed_order_id: str):
        try:
            completed_order = (
                self.db.query(CompletedOrder)
                .filter(CompletedOrder.id == completed_order_id)
                .first()
            )
            return completed_order
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_completed_orders_by_customer_id(self, customer_id: str):
        try:
            completed_orders = (
                self.db.query(CompletedOrder)
                .filter(CompletedOrder.customer_id == customer_id)
                .all()
            )
            return completed_orders
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_completed_order_status_by_id(
        self,
        completed_order_id: str,
        status: str = "pending",
        discount: bool = "false",
        order_date: date = date.today(),
    ):
        try:
            completed_order = (
                self.db.query(CompletedOrder)
                .filter(CompletedOrder.id == completed_order_id)
                .first()
            )
            if completed_order is None:
                raise CompletedOrderNotFoundException("completed order not found", 400)
            completed_order.status = status
            completed_order.discount = discount
            completed_order.order_date = order_date
            self.db.commit()
            self.db.refresh(completed_order)
            return completed_order
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_completed_order_by_id(self, completed_order_id):
        try:
            completed_order = self.db.query(CompletedOrder).filter(CompletedOrder.id == completed_order_id).first()
            self.db.delete(completed_order)
            self.db.commit()
            return True
        except AttributeError as e:
            raise e
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee
