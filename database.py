from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .session import CustomSession

# PostgreSQL connection URL (adjust accordingly)
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"  # Change to your DB info

# Set up engine and session for PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=CustomSession)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
