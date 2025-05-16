from sqlalchemy import Column, Integer, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemSubCategory(Base):
   __tablename__ = "item_sub_category"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(JSON)
   status = Column(JSON)
   item_category_id = Column(Integer, ForeignKey('item_category.id'))
   created_at = Column(DateTime)
   updated_at = Column(DateTime)
   deleted_at = Column(DateTime)
