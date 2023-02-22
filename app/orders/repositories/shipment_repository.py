from sqlalchemy.exc import IntegrityError, InterfaceError, DatabaseError
from sqlalchemy.orm import Session

from app.orders.exceptions import ShipmentNotFoundException
from app.orders.models import Shipment


class ShipmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_shipment(self, completed_order_id: str, customer_id: str, status: str, shipment_name: str,
                        shipment_last_name: str, shipment_address: str, shipment_district: str,
                        shipment_telephone_number: str):
        try:
            shipment = Shipment(completed_order_id, customer_id, status, shipment_name, shipment_last_name,
                                shipment_address, shipment_district, shipment_telephone_number)
            self.db.add(shipment)
            self.db.commit()
            self.db.refresh(shipment)
            return shipment
        except IntegrityError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_all_shipments_by_status(self, shipment_status: str):
        try:
            shipments_by_status = self.db.query(Shipment).filter(Shipment.status == shipment_status).all()
            return shipments_by_status
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

    def get_all_shipments_by_district(self, shipment_district: str):
        try:
            shipments_by_district = self.db.query(Shipment).filter(Shipment.shipment_district.like(shipment_district + "%")).all()
            print(shipments_by_district)
            return shipments_by_district
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

    def get_shipment_by_id(self, shipment_id: str):
        try:
            shipment = self.db.query(Shipment).filter(Shipment.id == shipment_id).first()
            return shipment
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

    def get_shipments_by_customer_id(self, customer_id: str):
        try:
            shipments = self.db.query(Shipment).filter(Shipment.customer_id == customer_id).all()
            return shipments
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

    def update_shipment(self, shipment_id, status: str, shipment_name: str,
                        shipment_last_name: str, shipment_address: str, shipment_district: str,
                        shipment_telephone_number: str):
        try:
            shipment = self.db.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment is None:
                raise ShipmentNotFoundException("Shipment with provided id not found", 400)
            shipment.status = status
            shipment.shipment_name = shipment_name
            shipment.shipment_last_name = shipment_last_name
            shipment.shipment_address = shipment_address
            shipment.shipment_district = shipment_district
            shipment.shipment_telephone_number = shipment_telephone_number
            self.db.add(shipment)
            self.db.commit()
            self.db.refresh(shipment)
            return shipment
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

    def delete_shipment_by_id(self, shipment_id: str):
        try:
            shipment = self.db.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment is None:
                raise ShipmentNotFoundException("Shipment with provided id not found", 400)
            self.db.delete(shipment)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as e:
            raise e

