from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


def indexing_id():
    for uid in range(0, len(users)):
        users[uid].id = uid+1


def find_to_id(uid):
    for u in users:
        if u.id == uid:
            return u


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_users(username: str, age: int) -> User:
    indexing_id()
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
def delete_message(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        indexing_id()
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


