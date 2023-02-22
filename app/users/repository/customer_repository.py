from sqlalchemy.exc import IntegrityError, DatabaseError, InterfaceError
from sqlalchemy.orm import Session

from app.users.models import Customer
from app.users.user_exceptions import IdNotFoundException, LastNameNotFoundException


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, name: str, last_name: str, address: str, district: str, telephone_number: str, user_id):
        try:
            customer = Customer(name, last_name, address, district, telephone_number, user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_customer_by_id(self, customer_id: str):
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if customer is None:
            raise IdNotFoundException(f"Provided ID: {customer_id} not found.", 400)
        return customer

    # def get_customer_by_user_id(self, user_id: str):
    #     customer = self.db.query(Customer).filter(Customer.user_id == user_id).first()
    #     if customer is not None:
    #         raise UserIdAlreadyInUseException(f"Provided user ID: {user_id} not found.", 400)
    #     return customer

    def get_customer_by_partial_last_name(self, partial_last_name: str):
        customer = self.db.query(Customer).filter(Customer.name.like(partial_last_name + "%")).all()
        if customer is None:
            raise LastNameNotFoundException(f"Provided partial last name: {partial_last_name} not found.", 400)
        return customer

    def get_all_customers(self):
        all_customers = self.db.query(Customer).all()
        return all_customers

    def update_customer(self, customer_id: str, name: str, last_name: str, address: str, district: str,
                        telephone_number: str, key_customer: bool, newsletter_subscription: bool):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            # if customer is None:
            #     raise IdNotFoundException(f"provided ID: {customer_id} not found.", 400)
        # if name is not None:
            customer.name = name
        # if last_name is not None:
            customer.last_name = last_name
        # if address is not None:
            customer.address = address
        # if district is not None:
            customer.district = district
        # if telephone_number is not None:
            customer.telephone_number = telephone_number
        # if key_customer is not None:
            customer.key_customer = key_customer
        # if newsletter_subscription is not None:
            customer.newsletter_subscription = newsletter_subscription
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def delete_customer_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            if customer is None:
                raise IdNotFoundException(f"provided ID: {customer_id} not found.", 400)
            self.db.delete(customer)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee
