from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.orders.exceptions import CompletedOrderNotFoundException, ShipmentNotFoundException
from app.orders.services import ShipmentService
from app.users.user_exceptions import IdNotFoundException, InvalidCustomerIdException


class ShipmentController:

    @staticmethod
    def create_shipment(completed_order_id, customer_id, status, shipment_name, shipment_last_name,
                        shipment_address, shipment_district, shipment_telephone_number):
        try:
            shipment = ShipmentService.create_shipment(completed_order_id, customer_id, status, shipment_name,
                                                       shipment_last_name, shipment_address, shipment_district,
                                                       shipment_telephone_number)
            return shipment
        except IntegrityError as e:
            raise HTTPException(400, str(e))
        except IdNotFoundException:
            raise HTTPException(400, "Customer with provided id not found")
        except InvalidCustomerIdException:
            raise HTTPException(400, "Customer id doesn't match order-customer_id")
        except CompletedOrderNotFoundException:
            raise HTTPException(400, "completed order with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_shipments_by_status(shipment_status: str):
        try:
            shipments = ShipmentService.get_all_shipments_by_status(shipment_status)
            return shipments
        except ShipmentNotFoundException:
            raise HTTPException(400, "No shipments with provided status")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_all_shipments_by_district(shipment_district: str):
        try:
            shipments = ShipmentService.get_all_shipments_by_district(shipment_district)
            return shipments
        except ShipmentNotFoundException:
            raise HTTPException(400, "No shipments within provided district")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_shipment_by_id(shipment_id: str):
        try:
            shipment = ShipmentService.get_shipment_by_id(shipment_id)
            return shipment
        except ShipmentNotFoundException:
            raise HTTPException(400, "Shipment with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def get_shipments_by_customer_id(customer_id: str):
        try:
            shipments = ShipmentService.get_shipments_by_customer_id(customer_id)
            return shipments
        except IdNotFoundException:
            raise HTTPException(400, "customer with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def update_shipment(shipment_id, status: str, shipment_name: str,
                        shipment_last_name: str, shipment_address: str, shipment_district: str,
                        shipment_telephone_number: str):
        try:
            shipment = ShipmentService.update_shipment(shipment_id, status,
                                                       shipment_name, shipment_last_name, shipment_address,
                                                       shipment_district, shipment_telephone_number)
            return shipment
        except ShipmentNotFoundException:
            raise HTTPException(400, "Shipment with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))

    @staticmethod
    def delete_shipment_by_id(shipment_id: str):
        try:
            if ShipmentService.delete_shipment_by_id(shipment_id):
                return Response("shipment with provided id is deleted", 200)
        except ShipmentNotFoundException:
            raise HTTPException(400, "Shipment with provided id not found")
        except Exception as e:
            raise HTTPException(500, str(e))
