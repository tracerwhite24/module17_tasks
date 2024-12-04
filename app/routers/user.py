from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/user", tags=["user"])

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

@router.get("/")
async def all_users():
    pass

@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass

@router.post("/create", response_model=User)
async def create_user(user: UserCreate):
    pass

@router.put("/update/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    pass

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    pass
