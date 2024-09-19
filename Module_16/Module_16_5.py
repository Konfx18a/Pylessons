from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []

def find_to_id(uid):
    for u in users:
        if u.id == uid:
            return u

class User(BaseModel):
    id: int = None
    age: int
    username: str



@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/users/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
def create_users(username: str, age: int) -> User:
    # indexing_id()
    ur = User(id=len(users)+1, username=username, age=age)
    users.append(ur)
    return ur

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int) -> User:
    try:
        ur = find_to_id(user_id)
        ur.username = username
        ur.age = age
        return ur
    except IndexError:
        raise HTTPException(status_code=404, detail=f"User with id # {user_id} was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    try:
        users.remove(find_to_id(user_id))
        # indexing_id()
        return f"User ID={user_id} deleted!"
    except ValueError:
        raise HTTPException(status_code=404, detail="User was not found")













