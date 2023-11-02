from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    username = Column(String(256))
    role = Column(String(256))

    products = relationship(
        "Product", cascade="delete", uselist=True, back_populates="user"
    )

    __tablename__ = "users"
