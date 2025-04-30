from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phoneNumber = Column(String(10))


class UserInformation(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    address = Column(String(255))
    zip_code = Column(String(10))
    first_name = Column(String(255))
    last_name = Column(String(255))
    middle_name = Column(String(255))
    business_name = Column(String(255))
    gstn = Column(String(255))


