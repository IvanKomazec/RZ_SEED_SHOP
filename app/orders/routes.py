from fastapi import APIRouter

from app.orders.controller import CartController, ProductOrderController
from app.orders.schemas import CartSchema, CartSchemaIn, ProductOrderSchema, ProductOrderSchemaIn

order_router = APIRouter(prefix="/api/orders", tags=["Orders"])


@order_router.post("/create-cart", response_model=CartSchema)
def create_cart(cart: CartSchemaIn):
    return CartController.create_cart(created_at=cart.created_at, status=cart.status, customer_id=cart.customer_id)

@order_router.get("/get-all-carts", response_model=list[CartSchema])
def get_all_carts():
    return CartController.get_all_carts()

@order_router.get("/get-cart-by-id", response_model=CartSchema)
def get_cart_by_id(cart_id):
    return CartController.get_cart_by_id(cart_id)

@order_router.put("/update-cart-status-by-id", response_model=CartSchema)
def update_cart_status_by_id(cart_id: str):
    return CartController.update_cart_status_by_id(cart_id)

@order_router.delete("/delete-cart-by-id")
def delete_cart_by_id(cart_id: str):
    return CartController.delete_cart_by_id(cart_id)

@order_router.post("/create-product-order", response_model=ProductOrderSchema)
def create_product_order(quantity: int, variety_id: str, cart_id: str):
    return ProductOrderController.create_product_order(quantity, variety_id, cart_id)
