from app.db.database import SessionLocal
from app.users.repository.customer_repository import CustomerRepository
from app.users.user_exceptions import *

class CustomerService:
    @staticmethod
    def create_customer(name: str, last_name: str, address: str, district: str, telephone_number: str, user_id):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create_customer(name, last_name, address, district, telephone_number,
                                                           user_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_customer_by_id(customer_id: str):
        with SessionLocal() as db:
            try:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_customer_by_id(customer_id=customer_id)
            except Exception as e:
                raise e

    # @staticmethod
    # def get_customer_by_user_id(user_id: str):
    #     with SessionLocal() as db:
    #         try:
    #             customer_repository = CustomerRepository(db)
    #             return customer_repository.get_customer_by_user_id(user_id=user_id)
    #         except Exception as e:
    #             raise e

    @staticmethod
    def get_all_customers():
        with SessionLocal() as db:
            customer_repository = CustomerRepository(db)
            return customer_repository.get_all_customers()

    @staticmethod
    def get_customer_by_partial_last_name(partial_last_name: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_customer_by_partial_last_name(partial_last_name)
        except Exception as e:
            raise Exception

    @staticmethod
    def delete_customer_by_id(customer_id):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                if customer_repository.delete_customer_by_id(customer_id):
                    return True
                raise IdNotFoundException("provided customer ID not found", 400)
        except Exception as e:
            raise e

    @staticmethod
    def update_customer(customer_id: str, name: str, last_name: str, address: str, district: str,
                        telephone_number: str, key_customer: bool, newsletter_subscription: bool):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.update_customer(customer_id, name, last_name, address, district,
                                                           telephone_number, key_customer, newsletter_subscription)
        except Exception as e:
            raise e

