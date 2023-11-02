from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductDBBase(ProductBase):
    id: int

    class Config:
        from_attributes = True


class ProductSchema(ProductBase):
    pass
