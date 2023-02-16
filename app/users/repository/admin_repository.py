from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import Admin
from app.users.user_exceptions import IdNotFoundException, LastNameNotFoundException


class AdminRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_admin(self, name: str, last_name: str, user_id: str):
        try:
            admin = Admin(name, last_name, user_id)
            self.db.add(admin)
            self.db.commit()
            self.db.refresh(admin)
            return admin
        except IntegrityError as e:
            raise e

    def get_all_admins(self):
        all_admins = self.db.query(Admin).all()
        return all_admins

    def get_admin_by_id(self, admin_id: str):
        admin = self.db.query(Admin).filter(Admin.id == admin_id).first()
        return admin

    def get_admin_by_partial_last_name(self, partial_last_name: str):
        try:
            admin = self.db.query(Admin).filter(Admin.last_name.like(partial_last_name + "%")).all()
            if admin is None:
                raise LastNameNotFoundException("provided last name not in DB", 400)
            return admin
        except Exception as e:
            raise e

    def delete_admin_by_id(self, admin_id):
        try:
            admin = self.db.query(Admin).filter(Admin.id == admin_id).first()
            if admin is None:
                raise IdNotFoundException("provided ID not in DB", 400)
            self.db.delete(admin)
            self.db.commit()
            return True
        except Exception as e:
            raise e
        