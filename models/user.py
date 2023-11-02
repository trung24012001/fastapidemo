from sqlalchemy import Column, Integer, String
from .base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    username = Column(String(256))
    role = Column(String(256))

    __tablename__ = "users"
