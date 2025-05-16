from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemCategory(Base):
   __tablename__ = "item_category"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(JSON)
   status = Column(JSON)
   created_at = Column(DateTime)
   updated_at = Column(DateTime)
   deleted_at = Column(DateTime)
