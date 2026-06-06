from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column
from .database import Base


class Post(Base):
    __tablename__ = "Posts"

    post_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str]
    slug: Mapped[str] = mapped_column(String(255))
    tags: Mapped[str] = mapped_column(String(255))
    created_at:Mapped[datetime]
    sub_header: Mapped[str] = mapped_column(String(255))
    author_id = mapped_column(ForeignKey("users.user_id"))


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(50))
    admin: Mapped[bool] = mapped_column(Boolean, default=False)

class Images(Base):

    __tablename__ = "Images"

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    filename:Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(510))
    alt_text: Mapped[str]
    



