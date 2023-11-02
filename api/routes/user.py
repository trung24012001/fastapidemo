from typing import List
from fastapi import APIRouter, HTTPException, status, File, Form, UploadFile
from schemas import UserSchema, UserCreate, UserUpdate


router = APIRouter()

id = 1
users = [UserSchema(id=id, username="trungvd", name="Trung", role="admin", products=[])]


@router.get("/", response_model=List[UserSchema])
def get_users():
    return users


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/", response_model=UserSchema, status_code=201)
def create_user(user_in: UserCreate):
    global id
    for user in users:
        if user.username == user_in.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User existed"
            )
    id += 1
    user = UserSchema(id=id, **user_in.model_dump())
    users.append(user)
    return user


@router.post("/file", status_code=201)
async def send_file(file: UploadFile):
    with open("test.txt", "wb") as f:
        content = await file.read()
        f.write(content)
    return "ok"


@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user_in: UserUpdate):
    for user in users:
        if user.id == user_id:
            return UserSchema(id=user.id, **user_in.model_dump())

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/{user_id}", response_model=int)
def remove_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user_id

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
