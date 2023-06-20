from db import Base
from sqlalchemy import create_engine, Column, String, JSON, DateTime
from datetime import datetime

class Node(Base):
    __tablename__ = "nodes"
    certname = Column(String, primary_key=True, index=True)
    environment = Column(String)
    classes = Column(JSON)
    parameters = Column(JSON)
    date_creation = Column(DateTime, default=datetime.now)
    date_modify = Column(DateTime, default=datetime.now, onupdate=datetime.now)