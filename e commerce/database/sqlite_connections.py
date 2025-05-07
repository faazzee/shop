from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Base=declarative_base()

engine=create_engine('sqlite:///commerce.db',echo=False)
Base.metadata.create_all(engine)

async def create_db():
    Session=sessionmaker(bind=engine)
    session=Session()
    return session

