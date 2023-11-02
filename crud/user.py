from typing import Type
from crud.base import CRUDBase
from schemas import UserSchema, UserCreate, UserUpdate
from models import User


class CRUDUser(CRUDBase[UserSchema, UserCreate, UserUpdate]):
    pass


user = CRUDUser(User)
