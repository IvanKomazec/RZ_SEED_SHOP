
from app.db import SessionLocal
from app.orders.repositories import ProductOrderRepository
from app.variety_products.repositories import VarietyProductRepository
from app.variety_products.exceptions import VarietyIdNotFoundException, VarietyOutOfStockException
from app.orders.repositories import CartRepository
from app.orders.exceptions import CartNotFoundException, ProductOrderNotFoundException



class ProductOrderService:

    @staticmethod
    def create_product_order(quantity: int, variety_id: str, cart_id: str):
        try:
            with SessionLocal() as db:
                variety_product_depository = VarietyProductRepository(db)
                variety_product = variety_product_depository.get_variety_product_by_id(variety_id)
                if variety_product is None:
                    raise VarietyIdNotFoundException("Variety with provided id not found", 400)
                if variety_product.stock < quantity:
                    raise VarietyOutOfStockException(f"only {variety_product.stock} {variety_product.name} with the "
                                                     f"package size of {variety_product.package_size} available", 400)
                cart_repository = CartRepository(db)
                if cart_repository.get_cart_by_id(cart_id) is None:
                    raise CartNotFoundException("Cart with provided id not found", 400)
                product_order_repository = ProductOrderRepository(db)
                product_order = product_order_repository.create_product_order(quantity, variety_id, cart_id)
                return product_order
        except Exception as e:
            raise e

    @staticmethod
    def get_all_product_orders():
        with SessionLocal() as db:
            product_order_repository = ProductOrderRepository(db)
            product_orders = product_order_repository.get_all_product_orders()
            return product_orders

    @staticmethod
    def get_all_product_orders_by_cart_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_repository = CartRepository(db)
                if cart_repository.get_cart_by_id(cart_id) is None:
                    raise CartNotFoundException("provided cart_id not found", 400)
                product_order_repository = ProductOrderRepository(db)
                product_orders = product_order_repository.get_all_product_orders_by_cart_id(cart_id)
                return product_orders
        except Exception as e:
            raise e

    @staticmethod
    def get_product_order_by_id(product_order_id: str):
        try:
            with SessionLocal() as db:
                product_order_repository = ProductOrderRepository(db)
                product_order = product_order_repository.get_product_order_by_id(product_order_id)
                if product_order is None:
                    raise ProductOrderNotFoundException("provided id not found", 400)
                return product_order
        except Exception as e:
            raise e

    @staticmethod
    def update_product_order_quantity_by_id(product_order_id: str, quantity: int, variety_id: str):
        try:
            with SessionLocal() as db:
                variety_product_repository = VarietyProductRepository(db)
                variety_product = variety_product_repository.get_variety_product_by_id(variety_id)
                product_order_repository = ProductOrderRepository(db)
                product_order = product_order_repository.update_product_order_quantity_by_id(product_order_id, quantity)
                if product_order.quantity > variety_product.stock:
                    raise VarietyOutOfStockException(f"only {variety_product.stock} {variety_product.name} with the "
                                                     f"package size of {variety_product.package_size} available", 400)
                if product_order is None:
                    raise ProductOrderNotFoundException("provided id not found", 400)
                return product_order
        except Exception as e:
            raise e

    @staticmethod
    def delete_product_order_by_id(product_order_id: str):
        try:
            with SessionLocal() as db:
                product_order_repository = ProductOrderRepository(db)
                if product_order_repository.get_product_order_by_id(product_order_id) is None:
                    raise ProductOrderNotFoundException("product order with provided id not found", 400)
                if product_order_repository.delete_product_order_by_id(product_order_id):
                    return True
        except Exception as e:
            raise e


