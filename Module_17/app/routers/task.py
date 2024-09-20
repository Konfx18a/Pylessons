from app.models.task import Task
from app.models.user import User
from app.shemas import CreateTask, UpdateTask
from app.backend.db_depends import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify

task_router = APIRouter(prefix="/task", tags=['task'])


@task_router.get("/all_tasks")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    return db.query(Task).all()

@task_router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    our_task = db.scalar(select(Task).where(Task.id == task_id))
    if our_task:
        return our_task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Пользователь с id # {task_id} не найден')

@task_router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], created_task: CreateTask, user_id: int):
    usr = db.scalar(select(User).where(User.id == user_id))
    if usr:
        db.execute(insert(Task).values(
                                      title=created_task.title,
                                      content=created_task.content,
                                      priority=created_task.priority,
                                      completed=False,
                                      user_id=user_id,
                                      slug=created_task.title.lower()
                                        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Пользователь  с ID :{user_id} не найден')

@task_router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], upd_task: UpdateTask, task_id: int = -1):
    our_user = db.scalar(select(Task).where(Task.id == task_id))
    if our_user:
        db.execute(update(Task).where(Task.id == task_id).values(id=task_id,
                                                            title=upd_task.title,
                                                            content=upd_task.content,
                                                            priority=upd_task.priority))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Задача {task_id} не найдена')

@task_router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    our_user = db.scalar(select(Task).where(Task.id == task_id))
    if our_user:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Задача с id # {task_id} не найдена')

