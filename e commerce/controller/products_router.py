from fastapi import APIRouter
from pydantic import BaseModel
from models.products_models import create_product
from fastapi.responses import JSONResponse

products_router=APIRouter()

class products(BaseModel):
    name:str
    price:int

@products_router.post("/add_products/")
async def add_product(request:products):
    result=await create_product(name=request.name,price=request.price)
    if not result:
        return JSONResponse(status_code=500,content={"message":"cannot add"})
    return JSONResponse(status_code=200,content={"message":" can add succesful"})
    r