from database.sqlite_connections import create_db,engine
from sqlalchemy import insert,delete,select,Column,String,Integer
from sqlalchemy.orm import declarative_base

Base=declarative_base()
class users(Base):
    __tablename__='USERS'

    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)

    def __repr__(self):
        f"<users(id={self.id},name='{self.name}',email='{self.email}')>"
Base.metadata.create_all(engine)

async def create_user(name,email):
    try:
        session=await create_db()
        query=insert(users).values(name=name,email=email)
        session.execute(query)
        session.commit()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"the error is {e}")
    finally:
        session.close()



