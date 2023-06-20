from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, JSON, DateTime
from sqlalchemy.orm import sessionmaker
from routes import router as api_router
from celery import Celery
from schemas import NodeCreate, NodeUpdate
from db import Base, engine
import uvicorn

app = FastAPI()
app.include_router(api_router)

redis_server = "redis"
celery = Celery("tasks", broker='redis://'+ redis_server,
                         backend='redis://'+ redis_server,
                         broker_connection_retry_on_startup=True)


#@app.on_event("startup")
#async def startup_event():
#  await database.execute('VACUUM')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
