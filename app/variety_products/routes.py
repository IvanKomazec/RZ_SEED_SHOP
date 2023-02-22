from fastapi import APIRouter

from app.variety_products.controller import VarietyProductController, VarietyTraitsController
from app.variety_products.schemas import VarietyProductSchema, VarietyProductSchemaIn, VarietyTraitsSchema, \
    VarietyTraitsSchemaIn, VarietyProductSchemaUpdate, VarietyTraitsSchemaUpdate

variety_products_router = APIRouter(prefix="/api/variety-products", tags=["Variety-products"])
variety_traits_router = APIRouter(prefix="/api/variety-traits", tags=["Variety-traits"])


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


@variety_products_router.put("/update-variety-by-id", response_model=VarietyProductSchema)
def update_variety_product_by_id(variety_product: VarietyProductSchemaUpdate):
    return VarietyProductController.update_variety_product_by_id(variety_id=variety_product.id,
                                                                 name=variety_product.name,
                                                                 crop=variety_product.crop,
                                                                 price=variety_product.price,
                                                                 package_size=variety_product.package_size,
                                                                 stock=variety_product.stock,
                                                                 added_to_inventory=variety_product.added_to_inventory,
                                                                 on_discount=variety_product.on_discount)


@variety_traits_router.post("/create-variety-traits", response_model=VarietyTraitsSchema)
def create_variety_traits(variety_traits: VarietyTraitsSchemaIn):
    return VarietyTraitsController.create_variety_traits(product_id=variety_traits.product_id,
                                                         open_field=variety_traits.open_field,
                                                         indoor=variety_traits.indoor,
                                                         fresh_market=variety_traits.fresh_market,
                                                         industry=variety_traits.industry,
                                                         fruit_size_g=variety_traits.fruit_size_g,
                                                         fruit_size_kg=variety_traits.fruit_size_kg,
                                                         maturity_days=variety_traits.maturity_days,
                                                         spring_production=variety_traits.spring_production,
                                                         summer_production=variety_traits.summer_production,
                                                         autumn_production=variety_traits.autumn_production,
                                                         winter_production=variety_traits.winter_production)


@variety_traits_router.get("/get-variety-traits-by-id", response_model=VarietyTraitsSchema)
def get_variety_traits_by_id(variety_traits_id: str):
    return VarietyTraitsController.get_variety_traits_by_id(variety_traits_id)


@variety_traits_router.get("/get-variety-traits-by-product-id", response_model=VarietyTraitsSchema)
def get_variety_traits_by_product_id(variety_product_id: str):
    return VarietyTraitsController.get_variety_traits_by_product_id(variety_product_id)


@variety_traits_router.get("/get-variety-traits-by-product-name", response_model=VarietyTraitsSchema)
def get_variety_traits_by_product_name(variety_product_name: str):
    return VarietyTraitsController.get_variety_traits_by_product_name(variety_product_name)


@variety_traits_router.put("/update-variety-traits-by-id", response_model=VarietyTraitsSchema)
def update_variety_traits_by_id(variety_traits: VarietyTraitsSchemaUpdate):
    return VarietyTraitsController.update_variety_traits_by_id(variety_traits_id=variety_traits.id,
                                                               fruit_size_g=variety_traits.fruit_size_g,
                                                               fruit_size_kg=variety_traits.fruit_size_kg,
                                                               maturity_days=variety_traits.maturity_days,
                                                               open_field=variety_traits.open_field,
                                                               indoor=variety_traits.indoor,
                                                               fresh_market=variety_traits.fresh_market,
                                                               industry=variety_traits.industry,
                                                               spring_production=variety_traits.spring_production,
                                                               summer_production=variety_traits.summer_production,
                                                               autumn_production=variety_traits.autumn_production,
                                                               winter_production=variety_traits.winter_production)


@variety_traits_router.delete("/delete-variety-traits-by-id")
def delete_variety_traits_by_id(variety_traits_id: str):
    return VarietyTraitsController.delete_variety_traits_by_id(variety_traits_id)


@variety_products_router.get("get-varieties-by-filter", response_model=list[VarietyProductSchema])
def filter_by_variety_traits(fruit_size_g: int, maturity_days: int, open_field: bool,
                             indoor: bool, fresh_market: bool, industry: bool, spring_production: bool,
                             summer_production: bool, autumn_production: bool, winter_production: bool):
    return VarietyProductController.filter_by_variety_traits(fruit_size_g, maturity_days, open_field, indoor,
                                                             fresh_market, industry, spring_production,
                                                             summer_production, autumn_production, winter_production)
