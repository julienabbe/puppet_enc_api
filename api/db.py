from sqlalchemy import create_engine, Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from datetime import datetime

database_url = "sqlite:///enc_db.db"
Base = declarative_base()

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Node(Base):
    __tablename__ = "nodes"
    certname = Column(String, primary_key=True, index=True)
    environment = Column(String)
    classes = Column(JSON)
    parameters = Column(JSON)
    date_creation = Column(DateTime, default=datetime.now)
    date_modify = Column(DateTime, default=datetime.now, onupdate=datetime.now)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
