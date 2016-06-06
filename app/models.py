from config import DATABASE_PORT, DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER, DATABASE_NAME, DATABASE_TYPE
from sqlalchemy import create_engine

# create a engine to connect to db
DATABASE_CONF = DATABASE_TYPE + '://' + DATABASE_USER + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + ':' + str(
        DATABASE_PORT) + '/' + DATABASE_NAME
engine = create_engine(DATABASE_CONF, echo=False)
# echo is for show the SQL language if you set it True

# Declare a map file
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean


# class WatermarkORM(Base):
#     __tablename__ = 'watermarked'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     result = Column(Integer)
#     path = Column(String(32))
#
#
# class ImageName(Base):
#     __tablename__ = 'watermark'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer)
#     category_id = Column(Integer)
#     image_name = Column(String(128))
#     path = Column(String(128))
#     suffix = Column(String(128))
#     data = Column(String(128))
#     password = Column(String(128))
#
#
# ImageName.metadata.create_all(engine)

# Run this script to create a table ..

class Image(Base):
    """
    This Model only for change the watermakr column if this image had process by server!
    By default the `watermark` column is set `0` and after process by server its being `1`!
    """
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    watermark = Column(Boolean)
