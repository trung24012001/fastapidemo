from typing import Generator
from fastapi import Depends
from fastapi.security import OAuth2
from db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2 = OAuth2()


def get_token(token: str = Depends(oauth2)) -> str:
    return token
