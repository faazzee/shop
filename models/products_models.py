from database.sqlite_connections import create_db,engine
from sqlalchemy import insert,delete,select,Column,Integer,String
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class products(Base):
    __tablename__='PRODUCTS'

    id=Column(Integer,primary_key=True)
    name=Column(String)
    price=Column(Integer)

    def __repr__(self):
       return f"<products(id={self.id},name='{self.name}',price={self.price})"
Base.metadata.create_all(engine)

async def create_product(name,price):
    try:
        session=await create_db()
        query=insert(products).values(name=name,price=price)
        session.execute(query)
        session.commit()
        return True
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)
    finally:
        session.close()
        