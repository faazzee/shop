from fastapi import FastAPI
from controller.orders_router import orders_routers
from controller.products_router import products_router
from controller.user_router import user_router

app=FastAPI()
app.include_router(orders_routers,prefix='/api',tags=['hello'])
app.include_router(products_router,prefix='/api',tags=['users'])
app.include_router(user_router,prefix='/api',tags=['users'])
print("hai")