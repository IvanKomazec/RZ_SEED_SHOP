from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User
from app.users.user_exceptions import IdNotFoundException


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password):
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise IdNotFoundException(f"Provided ID: {user_id} not found.", 400)
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id:str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_user_is_active(self, user_id: str, is_active: bool):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def read_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        return user
    