from pydantic import BaseModel
from typing import Optional,List

class CreateUserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    username: str
    password: str
    admin: Optional[bool] = None

    class Config:
        from_attributes = True

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    username: Optional[List[str]] = None
    password: Optional[List[str]] = None
    admin: Optional[bool] = None
