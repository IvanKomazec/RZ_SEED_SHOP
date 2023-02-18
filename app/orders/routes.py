from fastapi import APIRouter

from app.orders.controller import CartController, ProductOrderController, CompletedOrderController
from app.orders.schemas.cart_schemas import CartSchema, CartSchemaIn, CartWithProductsSchema
from app.orders.schemas.product_order_schemas import ProductOrderSchemaIn, ProductOrderSchema
from app.orders.schemas.completed_order_schemas import *

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
def create_product_order(product_order: ProductOrderSchemaIn):
    return ProductOrderController.create_product_order(product_order.quantity, product_order.variety_id,
                                                       product_order.cart_id)


@order_router.get("/get-all-product-orders", response_model=list[ProductOrderSchema])
def get_all_product_orders():
    return ProductOrderController.get_all_product_orders()


@order_router.get("/get-all-product-orders-by-cart-id", response_model=list[ProductOrderSchema])
def get_all_product_orders_by_cart_id(cart_id: str):
    return ProductOrderController.get_all_product_orders_by_cart_id(cart_id)


@order_router.get("/get-product-order-by-id", response_model=ProductOrderSchema)
def get_product_order_by_id(product_order_id: str):
    return ProductOrderController.get_product_order_by_id(product_order_id)


@order_router.put("/update-product-order-quantity-by-id", response_model=ProductOrderSchema)
def update_product_order_quantity_by_id(product_order_id: str, quantity: int, variety_id: str):
    return ProductOrderController.update_product_order_quantity_by_id(product_order_id, quantity, variety_id)


@order_router.delete("/delete-product-order-by-id")
def delete_product_order_by_id(product_order_id: str):
    return ProductOrderController.delete_product_order_by_id(product_order_id)


@order_router.get("/get-cart-with-product-order-list", response_model=CartWithProductsSchema)
def get_cart_with_list_of_product_orders(cart_id: str):
    return CartController.get_cart_with_list_of_product_orders(cart_id)


@order_router.post("/create-completed-order", response_model=CompletedOrderSchema)
def create_completed_order(completed_order: CompletedOrderSchemaIn):
    return CompletedOrderController.create_completed_order(cart_id=completed_order.cart_id,
                                                           customer_id=completed_order.customer_id,
                                                           order_date=completed_order.order_date,
                                                           order_value=completed_order.order_value,
                                                           discount=completed_order.discount,
                                                           status=completed_order.status)
