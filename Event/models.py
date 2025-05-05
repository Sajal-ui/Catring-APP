from sqlalchemy import Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
   id = Column(Integer, primary_key=True, index=True)
   display_name = Column(JSON)
   status = Column(JSON)
   created_at = Column(DateTime)
   updated_at = Column(DateTime)
   deleted_at = Column(DateTime)
