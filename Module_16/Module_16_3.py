from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Вася, возраст: 18'}


@app.get('/users')
async def all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str , age: int) -> str:
    users[f'{len(users)+1}'] = f'Имя: {username:}, возраст: {age}'
    return f'User {len(users)} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id:str, username: str, age:int) -> str:
    if user_id in users.keys():
        users[user_id] = f'Имя: {username:}, возраст: {age}'
        return f"The user {user_id} is registered"
    else:
        return f"The user {user_id} is not registered"


@app.delete('/user/{user_id}')
async def delete_user_id(user_id:str):
    users.pop(user_id)


