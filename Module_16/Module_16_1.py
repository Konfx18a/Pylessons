from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def triam() -> dict:
    return {'message': 'Главная страница!!!!'}

@app.get('/user')
async def user_info(username: str, age: int) -> dict:
     return {'message': f'Информация о пользователе {username} возраст {age}'}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как админ'}

@app.get('/user/{user_id}')
async def user_id(user_id: int = Path(ge=1, le=100, description='Введите id пользователя', example='34') ) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}