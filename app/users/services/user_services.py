from app.users.repository.user_repository import UserRepository
from app.db.database import SessionLocal


class UserServices:

    @staticmethod
    def create_user(email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.create_user(email, password)
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception as e:
                raise e
