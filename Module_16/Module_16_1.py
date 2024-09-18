from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def triam() -> dict:
    return {'message': 'Главная страница!!!!'}