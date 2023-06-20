from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from schemas import NodeCreate, NodeUpdate
from db import Base, engine, Node, get_db, SessionLocal
from sqlalchemy.orm import Session
import yaml

router = APIRouter(
  tags=['enc'],
)

@router.get("/{certname}")
def show_records(certname: str, db: Session = Depends(get_db)):
    node = db.query(Node).filter(Node.certname == certname).first()
    if not node:
        return {"message": "Node not found"}
    return node