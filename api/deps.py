from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas import UserSchema
import crud


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(user_id: int, db: Session = Depends(get_db)) -> UserSchema:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found",
        )
    return user


oauth2 = OAuth2()


def get_token(token: str = Depends(oauth2)) -> str:
    return token
