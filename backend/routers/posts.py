from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from backend.schemas.posts_schema import Posts
from backend.models.models import Post
from backend.models.database import get_db
import uvicorn



app = FastAPI()

router = APIRouter()

@router.post("/post_article/",response_model=Posts)
async def create_post(post: Posts, db: Session = Depends(get_db)):
    db_post = Post(title = post.title, body= post.body, slug = post.slug, created_at = post.created_at, sub_header = post.sub_header, author_id = post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post
