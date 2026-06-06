from fastapi import FastAPI,APIRouter
from backend.models.models import Images



app = FastAPI()
router = APIRouter()

#@app.post("/upload/")
