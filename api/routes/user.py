from fastapi import APIRouter, HTTPException, status
from schemas import UserSchema, UserPostSchema, UserPutSchema
from typing import List


router = APIRouter()

id = 1
users = [UserSchema(id=id, username="trungvd", name="Trung", role="Admin")]


@router.get("/", response_model=List[UserSchema])
def get_users():
    return users


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/", response_model=UserSchema)
def post_user(user_in: UserPostSchema):
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


@router.put("/{user_id}", response_model=UserSchema)
def put_user(user_id: int, user_in: UserPutSchema):
    for user in users:
        if user.id == user_id:
            # user = user.model_dump()
            # user_in = user_in.model_dump(exclude_none=True)
            # for k in user_in:
            #     user[k] = user_in[k]
            # return UserSchema(**user)
            return UserSchema(id=user.id, **user_in.model_dump())

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/{user_id}", response_model=int)
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user_id

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
