from fastapi import APIRouter

from app.variety_products.controller import VarietyProductController
from app.variety_products.schemas import VarietyProductSchema, VarietyProductSchemaIn

variety_products_router = APIRouter(prefix="/api/variety-products", tags=["Variety-products"])


@variety_products_router.post("/create-variety-product", response_model=VarietyProductSchema)
def create_variety_product(variety_product: VarietyProductSchemaIn):
    return VarietyProductController.create_variety_product(name=variety_product.name,
                                                           crop=variety_product.crop,
                                                           price=variety_product.price,
                                                           package_size=variety_product.package_size,
                                                           stock=variety_product.stock,
                                                           added_to_inventory=variety_product.added_to_inventory,
                                                           on_discount=variety_product.on_discount)


@variety_products_router.get("/get-variety-product-by-id", response_model=VarietyProductSchema)
def get_variety_product_by_id(variety_id: str):
    return VarietyProductController.get_variety_product_by_id(variety_id)


@variety_products_router.get("/get-all-variety-products", response_model=list[VarietyProductSchema])
def get_all_variety_products():
    return VarietyProductController.get_all_variety_products()


@variety_products_router.get("/get-variety-product-by-name", response_model=list[VarietyProductSchema])
def get_variety_product_by_name(variety_name: str):
    return VarietyProductController.get_variety_products_by_name(variety_name)


@variety_products_router.get("/get-variety-product-by-crop", response_model=list[VarietyProductSchema])
def get_variety_product_by_crop(variety_crop: str):
    return VarietyProductController.get_variety_products_by_name(variety_crop)

@variety_products_router.get("/get-available-variety-products-by-crop", response_model=list[VarietyProductSchema])
def get_available_variety_products_by_crop(crop: str):
    return VarietyProductController.get_available_products_by_crop(crop)

@variety_products_router.get("/get-all-new-varieties", response_model=list[VarietyProductSchema])
def get_all_new_variety_products():
    return VarietyProductController.get_all_new_variety_products()

@variety_products_router.get("/get-all-discount-varieties", response_model=list[VarietyProductSchema])
def get_variety_products_on_discount():
    return VarietyProductController.get_variety_products_on_discount()

@variety_products_router.delete("/delete-variety-by-id")
def delete_variety_by_id(variety_id: str):
    return VarietyProductController.delete_variety_product_by_id(variety_id)


# @course_router.get("/get-all-courses", response_model=list[CourseSchema])
# def get_all_courses():
#     courses = CourseController.get_all_courses()
#     return courses
#
#
# @course_router.get("/get-course-by-id", response_model=CourseSchema)
# def get_course_by_id(course_id: str):
#     return CourseController.get_course_by_id(course_id)
#
#
# @course_router.delete("/delete-course")
# def delete_course_by_id(course_id: str):
#     return CourseController.delete_course_by_id(course_id)
