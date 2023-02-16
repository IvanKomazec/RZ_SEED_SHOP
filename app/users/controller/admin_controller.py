from app.users.services import AdminService
from fastapi import HTTPException, Response, status
from app.users.user_exceptions import UserIdAlreadyInUseException, IdNotFoundException, LastNameNotFoundException
from sqlalchemy.exc import IntegrityError


class AdminController:

    @staticmethod
    def create_admin(name: str, last_name: str, user_id: str):
        try:
            admin = AdminService.create_admin(name, last_name, user_id)
            return admin
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Provided user ID already in DB")
        except IdNotFoundException:
            raise HTTPException(status_code=400, detail="Provided user ID not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_admins():
        all_admins = AdminService.get_all_admins()
        return all_admins

    @staticmethod
    def get_admin_by_id(admin_id: str):
        try:
            admin = AdminService.get_admin_by_id(admin_id)
            if admin is None:
                raise IdNotFoundException("Provided id not in DB", 400)
            return admin
        except IdNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_admin_by_partial_last_name(partial_last_name: str):
        try:
            admin = AdminService.get_admin_by_partial_last_name(partial_last_name)
            if admin is None:
                raise LastNameNotFoundException("Provided last name not in DB", 400)
            return admin
        except LastNameNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_admin_by_id(admin_id):
        try:
            if AdminService.delete_admin_by_id(admin_id):
                return Response(content=f"Customer with provided ID - {admin_id} is deleted", status_code=200)
        except IdNotFoundException:
            raise HTTPException(status_code=400, detail="Provided customer ID not in DB")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
