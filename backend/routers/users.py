from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.users_schema import CreateUserSchema, UserUpdateSchema
from backend.models.models import Users
from backend.models.database import get_db
from typing import List

router = APIRouter()

@router.post("/create_user/", response_model=CreateUserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    db_post = Users(
        name=user.name,
        username=user.username,
        password = user.password,
        admin=user.admin
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

#endpoint for deleting users
@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    post = db.query(Users).filter(Users.user_id == user_id).first()

    if not post:
        raise HTTPException(status_code = 404, detail = f"Post {user_id} not found")

    db.delete(post)
    db.commit()

    return {"msg":f"User {Users.username} was deleted"}


@router.get("/")
async def get_posts(db: Session = Depends(get_db)):
    users = db.query(Users).all()

    if not users:
        raise HTTPException(status_code=404, detail="No posts found")

    return users


@router.patch("/update_user/{post_id}")
async def update_user(user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    selected_post = db.query(Users).filter(Users.user_id == user_id).first()
    if not selected_post:
        raise HTTPException(status_code=404, detail="No posts found")

    update_data = user.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(selected_post, key, value)

    db.commit()
    db.refresh(selected_post)
    return selected_post
