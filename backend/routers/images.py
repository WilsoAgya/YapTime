from fastapi import FastAPI
from backend.models.models import Images



app = FastAPI()

@app.post("/upload/")
