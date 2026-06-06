from typing import Optional
from pydantic import BaseModel

class ImageSchema(BaseModel):
    user_id: int
    post_id: int
    filename: str
    url :str
    alt_text: str

