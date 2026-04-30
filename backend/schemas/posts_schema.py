from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Posts(BaseModel):
    id: int
    title: str
    body: str
    slug :str
    created_at: datetime
    sub_header: str
    author_id : int

    class Config:
        from_attributes = True

