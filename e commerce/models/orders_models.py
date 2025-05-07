from sqlalchemy import insert,delete,Column,select,String,Integer
from sqlalchemy.orm import declarative_base
from database.sqlite_connections import create_db,engine
from models.users_models import users
from models.products_models import products

Base=declarative_base()

class orders(Base):
    __tablename__= 'orders'

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    order_date=Column(Integer)
    product_id=Column(Integer)

    def __repr__(self):
      return f"<orders(id={self.id},user_id={self.user_id},order_date={self.order_date},product_id={self.product_id})>"
Base.metadata.create_all(engine)
async def inserting_orders(user_id,order_date,product_id):
    try:
        sesion=await create_db()
        query=insert(orders).values(user_id=user_id,order_date=order_date,product_id=product_id)
        sesion.execute(query)
        sesion.commit()
    except Exception as e:
        print(e)
        import traceback
        traceback.print_exc()
    finally:
        sesion.close()
async def placing_order(product_id):
    try:
        userlist=[]
        sesion=await create_db()
        stmt=(select(orders,users,products)
            .select_from(users,products)
            .join(products,orders.product_id==products.id))
        result=sesion.execute(stmt).scalars().all()
        for user in result:
            userlist.append({"id":user.id,"order_date":user.order_date})
        return userlist
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)
    finally:
        sesion.close()
    