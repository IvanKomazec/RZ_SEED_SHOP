import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.users.routes import user_router, customer_router, admin_router
from app.variety_products.routes import variety_products_router, variety_traits_router
from app.orders.routes import order_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(customer_router)
    app.include_router(variety_products_router)
    app.include_router(admin_router)
    app.include_router(variety_traits_router)
    app.include_router(order_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
