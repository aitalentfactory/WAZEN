
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# الاتصال بقاعدة بيانات PostgreSQL بدلًا من SQLite
DATABASE_URL = "postgresql://postgres:goldkey424@localhost:5432/wazen"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    merchant = Column(String, index=True)
    description = Column(String)
    amount = Column(Float)
    date = Column(String)
    category = Column(String)
