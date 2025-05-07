from sqlalchemy import insert,delete,select,Column,String,Integer,join
from sqlalchemy.orm import declarative_base
from database.sqlite_connections import engine,create_db
from models.products_models import products
from models.users_models import users
from models.orders_models import orders
Base=declarative_base()

class order_items(Base):
    __tablename__="order_items"

    id=Column(Integer,primary_key=True)
    order_id=Column(Integer)
    product_id=Column(Integer)
    quantity=Column(Integer)

    def __repr__(self):
        return f"<order_items(id={self.id},order_id={self.order_id},product_id={self.product_id},quantity={self.quantity})>"

Base.metadata.create_all(engine)

async def getting_orderdetails():
    try:
        stmt=(select(order_items,products,users)
        .select_from(orders)
        .join(products,orders.id==order_items.order_id)
        .join(users,orders))
        session=await create_db()
        userlist=[]
        session.execute(stmt).scalars().all()
        for user in userlist:
            userlist.append({"id":user.id,"order_id":user.order_id,"product":user.product_id,"quantity":user.quantity})
            return userlist
    except Exception as e:
        print(e)
        import traceback
        traceback.print_exc()
    finally:
        session.close