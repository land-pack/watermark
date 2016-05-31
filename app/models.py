from sqlalchemy import create_engine

# create a engine to connect to db
engine = create_engine('mysql://root:openos@127.0.0.1:3306/sqlalchemy', echo=False)
# echo is for show the SQL language if you set it True

# Declare a map file
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean


class ImageORM(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    embed = Column(Integer)
    path = Column(String(32))


ImageORM.metadata.create_all(engine)
