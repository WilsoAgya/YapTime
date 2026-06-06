from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PostSchema(BaseModel):
    post_id: Optional[int] = None
    title: str
    body: str
    slug :str
    tags: str
    created_at: datetime
    sub_header: str
    author_id : int

    class Config:
        from_attributes = True

class PostUpdateSchema(BaseModel):
    post_id: Optional[int] = None,
    title: Optional[str] = None,
    body: Optional[str] = None,
    slug: Optional[str] = None,
    created_at: Optional[datetime]= None,
    sub_header: Optional[str] = None,
    author_id:Optional[int] = None

