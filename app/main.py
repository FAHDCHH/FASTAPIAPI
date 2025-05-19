from fastapi import FastAPI
from routes import authRoutes
from models import Base
from db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authRoutes.router)
