from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", uselist=False, back_populates="products")

    __tablename__ = "products"
