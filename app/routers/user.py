from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.create_tables import *
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This user is not found.'
        )
    return user


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_users: CreateUser):
    try:
        db.execute(insert(User).values(username=create_users.username,
                                       firstname=create_users.firstname,
                                       lastname=create_users.lastname,
                                       age=create_users.age,
                                       slug=slugify(create_users.username)))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }
    except IntegrityError as er:
        db.rollback()
        if 'unique constraint' in str(er).lower() and 'username' in str(er).lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this username already exists."
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database error: {er}"
            )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}"
        )


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is not user found"
        )
    else:
        db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                                 lastname=update_user.lastname,
                                                                 age=update_user.age))
        db.commit()
        return {
            "status_code": status.HTTP_200_OK,
            "detail": "User update is successful"
        }


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is not user found"
        )
    else:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {
            "status_code": status.HTTP_200_OK,
            "detail": "User delete is successful."
        }
