from app.db.database import SessionLocal
from app.users.repository.admin_repository import AdminRepository
from app.users.repository.user_repository import UserRepository
from app.users.user_exceptions import *


class AdminService:
    @staticmethod
    def create_admin(name: str, last_name: str, user_id):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                if user_repository.get_user_by_id(user_id) is None:
                    raise IdNotFoundException("Provided user id not in DB")
                admin_repository = AdminRepository(db)
                return admin_repository.create_admin(name, last_name, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_admins():
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_all_admins()
        except Exception as e:
            raise e

    @staticmethod
    def get_admin_by_id(admin_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_admin_by_id(admin_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_admin_by_partial_last_name(partial_last_name: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_admin_by_partial_last_name(partial_last_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_admin_by_id(admin_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                if admin_repository.delete_admin_by_id(admin_id):
                    return True
                raise IdNotFoundException("Provided id not in DB", 400)
        except Exception as e:
            raise e
