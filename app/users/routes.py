from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.controller.customer_controller import CustomerController
from app.users.controller.admin_controller import AdminController
from app.users.schemas import UserSchema, UserSchemaIn, CustomerSchema, CustomerSchemaIn, AdminSchema, AdminSchemaIn, \
    UserSchemaUpdate, CustomerSchemaUpdate

from app.users.controller.user_auth_controller import JWTBearer

user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_user_by_id():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user: UserSchemaUpdate):
    return UserController.update_user_is_active(user_id=user.id, is_active=user.is_active)


customer_router = APIRouter(prefix="/api/customer", tags=["Customers"])


@customer_router.post("/create-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    return CustomerController.create_customer(customer.name, customer.last_name, customer.address, customer.district,
                                              customer.telephone_number, customer.user_id)


@customer_router.get("/get-all-customers", response_model=list[CustomerSchema])
def get_all_customers():
    return CustomerController.get_all_customers()


@customer_router.get("/get-customer-by-id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    return CustomerController.get_customer_by_id(customer_id)


@customer_router.get("/get-customer-by_partial_last_name", response_model=list[CustomerSchema])
def get_customer_by_partial_last_name(partial_last_name: str):
    return CustomerController.get_customer_by_partial_last_name(partial_last_name)


@customer_router.delete("/delete-user-by-id")
def delete_user_by_id(customer_id: str):
    return CustomerController.delete_customer_by_id(customer_id)


@customer_router.put("/update-customer", response_model=CustomerSchema)
def update_customer(customer: CustomerSchemaUpdate):
    return CustomerController.update_customer(customer_id=customer.id,
                                              name=customer.name,
                                              last_name=customer.last_name,
                                              address=customer.address,
                                              district=customer.district,
                                              telephone_number=customer.telephone_number,
                                              key_customer=customer.key_customer,
                                              newsletter_subscription=customer.newsletter_subscription)


admin_router = APIRouter(prefix="/api/admins", tags=["Admins"])


@admin_router.post("/add-new-admin", response_model=AdminSchema)
def create_admin(admin: AdminSchemaIn):
    return AdminController.create_admin(admin.name, admin.last_name, admin.user_id)


@admin_router.get("/get-user-by-id", response_model=AdminSchema)
def get_admin_by_id(admin_id: str):
    return AdminController.get_admin_by_id(admin_id)


@admin_router.get("/get-all-admins", response_model=list[AdminSchema])
def get_all_admins():
    return AdminController.get_all_admins()


@admin_router.get("/get-admin-by-partial-last-name", response_model=list[AdminSchema])
def get_admin_by_partial_last_name(partial_last_name: str):
    return AdminController.get_admin_by_partial_last_name(partial_last_name)


@admin_router.delete("/delete-admin-by-id")
def delete_admin_by_id(admin_id: str):
    return AdminController.delete_admin_by_id(admin_id)
