from sqlalchemy.exc import IntegrityError, DatabaseError, InterfaceError
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
        except InterfaceError as ee:
            raise ee

    def get_user_by_id(self, user_id: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise IdNotFoundException(f"Provided ID: {user_id} not found.", 400)
            return user
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id:str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise IdNotFoundException("User with provided id not found", 400)
            self.db.delete(user)
            self.db.commit()
            return True
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_user_is_active(self, user_id: str, is_active: bool):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise IdNotFoundException("User with provided id not found", 400)
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def update_user_is_superuser(self, user_id: str, is_superuser: bool):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise IdNotFoundException("User with provided id not found", 400)
            user.is_superuser = is_superuser
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except DatabaseError as e:
            raise e
        except InterfaceError as ee:
            raise ee

    def read_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        return user
    