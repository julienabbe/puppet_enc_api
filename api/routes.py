from fastapi import APIRouter

router = APIRouter()
from v1.endpoints import node
router.include_router(node.router, prefix='/node')
from v1.endpoints import enc
router.include_router(enc.router, prefix='/enc')