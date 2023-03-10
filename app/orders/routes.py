from fastapi import APIRouter

from app.orders.controller import CartController, ProductOrderController, CompletedOrderController, ShipmentController
from app.orders.schemas.cart_schemas import CartSchema, CartSchemaIn, CartWithProductsSchema, CartSchemaUpdate
from app.orders.schemas.product_order_schemas import ProductOrderSchemaIn, ProductOrderSchema, ProductOrderSchemaUpdate
from app.orders.schemas.completed_order_schemas import *
from app.orders.schemas import ShipmentSchema, ShipmentSchemaIn, ShipmentSchemaUp

order_router = APIRouter(prefix="/api/orders", tags=["Orders"])


@order_router.post("/create-cart", response_model=CartSchema)
def create_cart(cart: CartSchemaIn):
    return CartController.create_cart(created_at=cart.created_at, status=cart.status)


@order_router.get("/get-all-carts", response_model=list[CartSchema])
def get_all_carts():
    return CartController.get_all_carts()


@order_router.get("/get-cart-by-id", response_model=CartSchema)
def get_cart_by_id(cart_id):
    return CartController.get_cart_by_id(cart_id)


@order_router.put("/update-cart-status-by-id", response_model=CartSchema)
def update_cart_status_by_id(cart: CartSchemaUpdate):
    return CartController.update_cart_status_by_id(cart_id=cart.id)


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
def update_product_order_quantity_by_id(product_order: ProductOrderSchemaUpdate):
    return ProductOrderController.update_product_order_quantity_by_id(product_order_id=product_order.id,
                                                                      quantity=product_order.quantity,
                                                                      variety_id=product_order.variety_id)


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


@order_router.get("/get-all-completed-orders", response_model=list[CompletedOrderSchema])
def get_all_completed_orders():
    return CompletedOrderController.get_all_completed_orders()


@order_router.get("/get-all-completed-orders-by-status", response_model=list[CompletedOrderSchema])
def get_all_completed_orders_by_status(status: str):
    return CompletedOrderController.get_all_completed_orders_by_status(status)


@order_router.get("/get-all-completed-orders-in-specified-period-by-status", response_model=list[CompletedOrderSchema])
def get_all_completed_orders_in_specified_period_by_status(status: str, sy: int, sm: int, sd: int, ey: int,
                                                           em: int, ed: int):
    return CompletedOrderController.get_all_completed_orders_in_specified_period_by_status(status, sy, sm, sd, ey, em,
                                                                                           ed)


@order_router.get("/get-total-sales-for-specified-period")
def get_total_sales_amount_for_specified_period_by_status(status: str, sy: int, sm: int, sd: int, ey: int, em: int,
                                                          ed: int):
    return CompletedOrderController.get_total_sales_amount_for_specified_period_by_status(status, sy, sm, sd, ey, em,
                                                                                          ed)


@order_router.get("/get-product-orders-for-specified-period")
def get_product_orders_for_specified_period(status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int):
    return CompletedOrderController.get_product_orders_for_specified_period(status, sy, sm, sd, ey, em, ed)

@order_router.get("/get-top5-bestselling-products")
def get_top5_bestselling_products(status: str, sy: int, sm: int, sd: int, ey: int, em: int, ed: int):
    return CompletedOrderController.get_top5_bestselling_products(status, sy, sm, sd, ey, em, ed)


@order_router.get("/get-completed-order-by-id", response_model=CompletedOrderSchema)
def get_completed_order_by_id(completed_order_id: str):
    return CompletedOrderController.get_completed_order_by_id(completed_order_id)


@order_router.get("/get-all-orders-by-customer-id", response_model=list[CompletedOrderSchema])
def get_completed_orders_by_customer_id(customer_id: str):
    return CompletedOrderController.get_completed_orders_by_customer_id(customer_id)


@order_router.put("/update-completed-order", response_model=CompletedOrderSchema)
def update_completed_order_by_id(completed_order: CompletedOrderSchemaUpdate):
    return CompletedOrderController.update_completed_order_status_by_id(completed_order.id, completed_order.status,
                                                                        completed_order.discount,
                                                                        completed_order.order_date)


@order_router.delete("/delete-completed-order")
def delete_completed_order(completed_order_id: str):
    return CompletedOrderController.delete_completed_order_by_id(completed_order_id)


@order_router.post("/create-shipment", response_model=ShipmentSchema)
def create_shipment(shipment: ShipmentSchemaIn):
    return ShipmentController.create_shipment(completed_order_id=shipment.completed_order_id,
                                              customer_id=shipment.customer_id, status=shipment.status,
                                              shipment_name=shipment.shipment_name,
                                              shipment_last_name=shipment.shipment_last_name,
                                              shipment_address=shipment.shipment_address,
                                              shipment_district=shipment.shipment_district,
                                              shipment_telephone_number=shipment.shipment_telephone_number)


@order_router.get("/get-all-shipments-by-status", response_model=list[ShipmentSchema])
def get_all_shipments_by_status(shipment_status: str):
    return ShipmentController.get_all_shipments_by_status(shipment_status)


@order_router.get("/get-all-shipments-by-district", response_model=list[ShipmentSchema])
def get_all_shipments_by_district(shipment_district: str):
    return ShipmentController.get_all_shipments_by_district(shipment_district)

@order_router.get("/get-shipment-by-id", response_model=ShipmentSchema)
def get_shipment_by_id(shipment_id: str):
    return ShipmentController.get_shipment_by_id(shipment_id)

@order_router.get("/get-shipments-by-customer-id", response_model=list[ShipmentSchema])
def get_shipments_by_customer_id(customer_id: str):
    return ShipmentController.get_shipments_by_customer_id(customer_id)


@order_router.put("/update-shipment", response_model=ShipmentSchema)
def update_shipment(shipment: ShipmentSchemaUp):
    return ShipmentController.update_shipment(shipment_id=shipment.id, status=shipment.status,
                                              shipment_name=shipment.shipment_name,
                                              shipment_last_name=shipment.shipment_last_name,
                                              shipment_address=shipment.shipment_address,
                                              shipment_district=shipment.shipment_district,
                                              shipment_telephone_number=shipment.shipment_telephone_number)


@order_router.delete("/delete-shipment")
def delete_shipment(shipment_id: str):
    return ShipmentController.delete_shipment_by_id(shipment_id)