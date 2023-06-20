from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from schemas import NodeCreate, NodeUpdate
from db import Base, engine, Node, get_db, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(
  tags=['node'],
)

@router.post("/")
def create_node(node: NodeCreate, db: SessionLocal = Depends(get_db)):
    db_node = Node(
        certname=node.certname,
        environment=node.environment,
        classes=node.classes,
        parameters=node.parameters,
    )
    print(db_node)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return {"message": "Node created"}

@router.get("/")
@router.get("/{certname}")
def read_node(db: Session = Depends(get_db), certname: str = None):
    if certname:
        node = db.query(Node).filter(Node.certname == certname).first()
        if not node:
            return {"message": "Node not found"}
        return node
    else:
        nodes = db.query(Node).all()
    return nodes


@router.put("/{certname}")
def update_node(certname: str, node: NodeUpdate, db: Session = Depends(get_db)):
    db_node = db.query(Node).filter(Node.certname == certname).first()
    if not db_node:
        return {"message": "Node not found"}
    if node.environment:
        db_node.environment = node.environment
    if node.classes:
        db_node.classes = node.classes
    if node.parameters:
        db_node.parameters = node.parameters
    db.commit()
    return db.refresh(db_node)

@router.delete("/{certname}")
def delete_node(certname: str, db: Session = Depends(get_db)):
    db_node = db.query(Node).filter(Node.certname == certname).first()
    if not db_node:
        return {"message": "Node not found"}
    db.delete(db_node)
    return db.commit()

