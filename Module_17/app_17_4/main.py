from fastapi import FastAPI
from app.routers.user import user_router
from app.routers.task import task_router

app = FastAPI()

app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
