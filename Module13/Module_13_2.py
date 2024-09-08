from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
api = '********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
def all_massages(message):
    print('Привет! Я бот помогающий твоему здоровью.')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

