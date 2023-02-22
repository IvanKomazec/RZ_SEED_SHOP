from app.db import SessionLocal
from app.orders.exceptions import CompletedOrderNotFoundException, ShipmentNotFoundException
from app.orders.repositories import ShipmentRepository, CompletedOrderRepository, ProductOrderRepository
from app.users.repository import CustomerRepository
from app.users.user_exceptions import IdNotFoundException, InvalidCustomerIdException
from app.variety_products.repositories import VarietyProductRepository


class ShipmentService:

    @staticmethod
    def create_shipment(completed_order_id, customer_id, status, shipment_name, shipment_last_name,
                        shipment_address, shipment_district, shipment_telephone_number):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id) is None:
                    raise IdNotFoundException("customer with provided id not found", 400)
                completed_order_repository = CompletedOrderRepository(db)
                completed_order = completed_order_repository.get_completed_order_by_id(completed_order_id)
                if completed_order is None:
                    raise CompletedOrderNotFoundException("Completed order with provided id not found", 400)
                if completed_order.customer_id != customer_id:
                    raise InvalidCustomerIdException("Customer id doesn't match order-customer_id", 400)
                shipment_repository = ShipmentRepository(db)
                shipment = shipment_repository.create_shipment(completed_order_id, customer_id, status, shipment_name,
                                                               shipment_last_name, shipment_address, shipment_district,
                                                               shipment_telephone_number)
                completed_order = completed_order_repository.get_completed_order_by_id(completed_order_id)
                completed_order.status = "finalized"
                customer = customer_repository.get_customer_by_id(customer_id)
                shipment.shipment_name = customer.name
                shipment.shipment_last_name = customer.last_name
                shipment.shipment_address = customer.address
                shipment.shipment_district = customer.district
                shipment.shipment_telephone_number = customer.telephone_number

                product_order_repository = ProductOrderRepository(db)
                product_orders = product_order_repository.get_all_product_orders_by_cart_id(completed_order.cart_id)
                varieties_ids = [product.variety_id for product in product_orders]
                variety_product_repository = VarietyProductRepository(db)
                variety_products = []
                for variety_id in varieties_ids:
                    variety_products.append(variety_product_repository.get_variety_product_by_id(variety_id))
                for variety_product in variety_products:
                    for product_order in product_orders:
                        variety_product_repository.update_stock(variety_product.id, product_order.quantity)
                return shipment
        except Exception as e:
            raise e

    @staticmethod
    def get_all_shipments_by_status(shipment_status: str):
        try:
            with SessionLocal() as db:
                shipment_repository = ShipmentRepository(db)
                shipments = shipment_repository.get_all_shipments_by_status(shipment_status)
                if len(shipments) == 0:
                    raise ShipmentNotFoundException("No shipments with provided status", 400)
                return shipments
        except Exception as e:
            raise e

    @staticmethod
    def get_all_shipments_by_district(shipment_district: str):
        try:
            with SessionLocal() as db:
                shipment_repository = ShipmentRepository(db)
                shipments = shipment_repository.get_all_shipments_by_district(shipment_district)
                if len(shipments) == 0:
                    raise ShipmentNotFoundException("No shipments within provided district", 400)
                return shipments
        except Exception as e:
            raise e

    @staticmethod
    def get_shipment_by_id(shipment_id: str):
        try:
            with SessionLocal() as db:
                shipment_repository = ShipmentRepository(db)
                shipment = shipment_repository.get_shipment_by_id(shipment_id)
                if shipment is None:
                    raise ShipmentNotFoundException("Shipment with provided id not found", 400)
                return shipment
        except Exception as e:
            raise e

    @staticmethod
    def get_shipments_by_customer_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id) is None:
                    raise IdNotFoundException("customer with provided id not found", 400)
                shipment_repository = ShipmentRepository(db)
                shipments = shipment_repository.get_shipments_by_customer_id(customer_id)
                return shipments
        except Exception as e:
            raise e

    @staticmethod
    def update_shipment(shipment_id, status: str, shipment_name: str,
                        shipment_last_name: str, shipment_address: str, shipment_district: str,
                        shipment_telephone_number: str):
        try:
            with SessionLocal() as db:
                shipment_repository = ShipmentRepository(db)
                shipment = shipment_repository.get_shipment_by_id(shipment_id)
                if shipment is None:
                    raise ShipmentNotFoundException("Shipment with provided id not found", 400)
                return shipment_repository.update_shipment(shipment_id, status,
                                                           shipment_name, shipment_last_name, shipment_address,
                                                           shipment_district, shipment_telephone_number)
        except Exception as e:
            raise e

    @staticmethod
    def delete_shipment_by_id(shipment_id: str):
        try:
            with SessionLocal() as db:
                shipment_repository = ShipmentRepository(db)
                if shipment_repository.get_shipment_by_id(shipment_id) is None:
                    raise ShipmentNotFoundException("Shipment with provided id not found", 400)
                if shipment_repository.delete_shipment_by_id(shipment_id):
                    return True
        except Exception as e:
            raise e