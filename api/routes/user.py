from typing import List
from fastapi import APIRouter, HTTPException, status, UploadFile, Depends
from sqlalchemy.orm import Session
from schemas import UserSchema, UserCreate, UserUpdate
from api.deps import get_db, get_token
import crud

router = APIRouter()


@router.get("/", response_model=List[UserSchema])
def get_users(token: str = Depends(get_token), db: Session = Depends(get_db)):
    print(token)
    return crud.user.get_all(db)


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found",
        )
    return user


@router.post("/", response_model=UserSchema, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return crud.user.create(db, obj_in=user_in)


@router.post("/upload", status_code=201)
async def send_file(file: UploadFile):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)
    return "ok"


@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found",
        )
    return crud.product.update(db, db_obj=user, obj_in=user_in)


@router.delete("/{user_id}", response_model=int)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.product.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found",
        )

    return crud.user.remove(db, obj=user)
