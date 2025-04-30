from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
   id = Column(Integer, primary_key=True, index=True)
   display_name = Column(String(255), index=True)
