from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: Optional[str]
    username: Optional[str]
    role: Optional[str]


class UserSchema(UserBase):
    id: int


class UserPostSchema(UserBase):
    pass


class UserPutSchema(UserBase):
    pass
