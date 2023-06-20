from pydantic import BaseModel
from typing import Dict

class NodeCreate(BaseModel):
    certname: str
    environment: str
    classes: dict
    parameters: dict
    
    class Config:
        orm_mode = True

class NodeUpdate(BaseModel):
    environment: str = None
    classes: dict = None
    parameters: dict = None

    class Config:
        orm_mode = True