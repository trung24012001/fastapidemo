from sqlalchemy import Column, Integer, String
from .base import Base


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

    __tablename__ = "products"
