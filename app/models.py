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

from sqlalchemy import Column, Integer, String, Boolean.

class ImageModel(Base):
    """
    This Model only for change the watermakr column if this image had process by server!
    By default the `watermark` column is set `0` and after process by server its being `1`!
    """
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    watermark = Column(Integer)  # 0 is no watermark ,1 is mean watermark


class ExtractModel(Base):
    __tablename__ = 'extract'
    id = Column(Integer, primary_key=True)
    watermark = Column(String)  # store the extract context of watermark
