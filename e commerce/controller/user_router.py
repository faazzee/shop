from models.users_models import create_user
from sqlalchemy.orm import declarative_base
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
user_router=APIRouter()

class orders(BaseModel):
    name:str
    email:str

@user_router.post("/users/")
async def add_users(request:orders):
    sesion=await create_user(name=request.name,email=request.email)
    if not sesion:
        return JSONResponse(status_code=500,content={"message":"error"})
    return JSONResponse(status_code=200,content={"message":"added successfully"})

