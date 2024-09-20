from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from app.backend.db_depends import get_db
from app.models.user import User
from app.shemas import CreateUser, UpdateUser

user_router = APIRouter(prefix="/user", tags=['user'])

@user_router.get("/all_users")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    return db.query(User).all()

@user_router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    our_user = db.scalar(select(User).where(User.id == user_id))
    if our_user:
        return our_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Пользователь с id # {user_id} не найден')


@user_router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], created_user: CreateUser, user_id: int):
    test_username = db.scalar(select(User).where(User.username == created_user.username))
    test_id = db.scalar(select(User).where(User.id == user_id))
    if not test_username and not test_id:
        db.execute(insert(User).values(firstname=created_user.firstname,
                                      lastname=created_user.lastname,
                                      age=created_user.age,
                                      username=created_user.username))
                                      # id=user_id))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Не возможно создать пользователя. Такой пользователь существует!!!')


@user_router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], upd_user: UpdateUser, user_id: int):
    our_user = db.scalar(select(User).where(User.id == user_id))
    if our_user:
        db.execute(update(User).where(User.id == user_id).values(firstname=upd_user.firstname,
                                                                 lastname=upd_user.lastname,
                                                                 age=upd_user.age
                                                                 ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Пользователь с id # {user_id} не найден')



@user_router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    our_user = db.scalar(select(User).where(User.id == user_id))
    if our_user:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Пользователь с id # {user_id} не найден')


@user_router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    usr = db.scalar(select(User).where(User.id == user_id))
    if usr:
        return usr.tasks
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Пользователь с id # {user_id} не найден')
