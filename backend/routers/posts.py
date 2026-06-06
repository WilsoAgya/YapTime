from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.posts_schema import PostSchema, PostUpdateSchema
from backend.models.models import Post, Users
from backend.models.database import get_db
from typing import List

import uvicorn


router = APIRouter()

@router.post("/post_article/",response_model=PostSchema)
async def create_post(post: PostSchema, db: Session = Depends(get_db)):
    db_post = Post(title = post.title, body= post.body, slug = post.slug, tags = post.tags, created_at = post.created_at, sub_header = post.sub_header, author_id = post.author_id)
    db.add(db_post)
    db.flush()
    db.refresh(db_post)
    db.commit()

    return db_post

#endpoint for deleting posts
@router.delete("/delete_article/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.post_id == post_id).first()

    if not post:
        raise HTTPException(status_code = 404, detail = f"Post {post_id} not found")

    db.delete(post)
    db.commit()

    return {"msg":f"Post {post_id} was deleted"}


@router.get("/", response_model=List[PostSchema])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()

    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")

    return posts


@router.patch("/update_article/{post_id}")
async def update_post(post_id:int, post:PostUpdateSchema,  db:Session = Depends(get_db)):
    selected_post = db.query(Post).filter(Post.post_id == post_id).first()
    if not selected_post:
        raise HTTPException(status_code=404, detail="No posts found")

    update_data = post.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(selected_post, key, value)

    db.commit()
    db.refresh(selected_post)
    return selected_post



