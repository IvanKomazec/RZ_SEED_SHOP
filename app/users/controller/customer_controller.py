from app.users.services import CustomerService, UserServices
from fastapi import HTTPException, Response, status
from app.users.user_exceptions import UserIdAlreadyInUseException, IdNotFoundException, LastNameNotFoundException
from sqlalchemy.exc import IntegrityError


class CustomerController:

    @staticmethod
    def create_customer(name: str, last_name: str, address: str, district: str, telephone_number: str, user_id):
        try:
            UserServices.get_user_by_id(user_id)
            customer = CustomerService.create_customer(name, last_name, address, district, telephone_number, user_id)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Provided user ID already in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_customers():
        all_customers = CustomerService.get_all_customers()
        all_customers_list = [customer for customer in all_customers]
        return all_customers_list

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            customer = CustomerService.get_customer_by_id(customer_id)
            return customer
        except IdNotFoundException:
            raise HTTPException(status_code=400, detail="Provided user ID not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_partial_last_name(partial_last_name: str):
        try:
            customer = CustomerService.get_customer_by_partial_last_name(partial_last_name)
            return customer
        except LastNameNotFoundException:
            raise HTTPException(status_code=400, detail=f"Provided last name {partial_last_name} not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_customer_by_id(customer_id):
        try:
            if CustomerService.delete_customer_by_id(customer_id):
                return Response(content=f"Customer with provided ID - {customer_id} is deleted", status_code=200)
        except IdNotFoundException:
            raise HTTPException(status_code=400, detail="Provided customer ID not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_customer(customer_id: str, name: str, last_name: str, address: str, district: str,
                        telephone_number: str, key_customer: bool, newsletter_subscription: bool):
        try:
            customer = CustomerService.update_customer(customer_id, name, last_name, address, district,
                                                       telephone_number, key_customer, newsletter_subscription)
            return customer
        except Exception as e:
            raise HTTPException(status_code=400, detail="str(e)")
