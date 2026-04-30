from fastapi import FastAPI
from backend.models.database import Base, engine
from backend.models.models import Post, Users
from backend.routers import posts  # ← import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(posts.router)  # ← register router