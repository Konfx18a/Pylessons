from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Integer, String, Column

# engine = create_engine("sqlite:///ecommerce.db", echo= True)
engine = create_engine('sqlite:///taskmanager.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


