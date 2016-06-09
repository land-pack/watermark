from sqlalchemy import create_engine
import os

# create a engine to connect to db
# DATABASE_CONF = os.environ.get('DATABASE_URL')
DATABASE_CONF = 'mysql://root:openos@127.0.0.1/watermark_site'
engine = create_engine(DATABASE_CONF)
# echo is for show the SQL language if you set it True

# Declare a map file
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String


class CategoryModel(Base):
    """
    Only for counter the watermark image counter!!
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    watermark_count = Column(Integer)


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
