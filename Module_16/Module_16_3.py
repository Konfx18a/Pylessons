from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Вася, возраст: 18'}


@app.get('/users')
async def all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(max_length=20, min_length=5, description='Введите имя пользователя',
                                                  example='Василий')], age: int = Path(ge=18, le=120,
                                                  description='Введите возраст пользователя', example='34')) -> str:
    users[f'{len(users)+1}'] = f'Имя: {username:}, возраст: {age}'
    return f'User {len(users)} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: Annotated[int, Path(ge=1, le=100, description='Введите id пользователя', example='34')],
                                username: str = Path(max_length=20, min_length=5, description='Введите имя пользователя',
                                                  example='Василий'),
                                age: int = Path(ge=18, le=120, description='Введите возраст пользователя',
                                                  example='34')) -> str:
    if f'{user_id}' in users.keys():
        users[f'{user_id}'] = f'Имя: {username:}, возраст: {age}'
        return f"User {user_id} has been updated"
    else:
        return f"The user {user_id} is not registered"


@app.delete('/user/{user_id}')
async def delete_user_id(user_id: int = Path(ge=1, le=100, description='Введите id пользователя', example='34')):
    users.pop(f'{user_id}')
    return f'User {user_id} has been deleted'

