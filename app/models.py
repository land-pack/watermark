from sqlalchemy import create_engine

# create a engine to connect to db
engine = create_engine('mysql://root:openos@127.0.0.1:3306/sqlalchemy', echo=False)
# echo is for show the SQL language if you set it True

# Declare a map file
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean


class WatermarkORM(Base):
    __tablename__ = 'watermarked'
    id = Column(Integer, primary_key=True, autoincrement=True)
    result = Column(Integer)
    path = Column(String(32))


class ImageName(Base):
    __tablename__ = 'watermark'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    category_id = Column(Integer)
    image_name = Column(String(32))
    path = Column(String(32))
    image_suffix = Column(String(32))
    data = Column(String(32))
    password = Column(String(32))


ImageORM.metadata.create_all(engine)

# Run this script to create a table ..
