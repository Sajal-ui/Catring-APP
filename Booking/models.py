from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    customer_name = Column(String, index=True)
    contact_no = Column(String(10))
    email = Column(String)
    address = Column(String(255))
    event_identifier = Column(Integer, ForeignKey('event.id'))
    event_venue = Column(String(255))
    amount = Column(Float)
    advance = Column(Float)
