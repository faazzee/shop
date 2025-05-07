from models.orders_models import placing_order,inserting_orders
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

orders_routers=APIRouter()

class orders(BaseModel):

    product_id:int
    order_date:int
    user_id:int

class mulitple_orders(BaseModel):
    data:List[orders]

@orders_routers.post("/insert_products")
async def inserting(request:orders):
    result=await inserting_orders(product_id=request.product_id,order_date=request.order_date,user_id=request.user_id)
    if not result:
         return JSONResponse(status_code=500,content={"message":"error adding products"})
    return JSONResponse(status_code=200,content={"message":"successfully"})


@orders_routers.post("/products/{user_id}")
async def placing_orders(product_id:int):
    result=await placing_order(product_id)
    if not result:
        return JSONResponse(status_code=500,content={"message":"error adding products"})
    return JSONResponse(status_code=200,content={"message":result})