from pydantic import BaseModel
from typing import Optional, List
from .product import ProductSchema


class UserBase(BaseModel):
    name: Optional[str]
    username: Optional[str]
    role: Optional[str]


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserSchema(UserBase):
    products: List[ProductSchema]
