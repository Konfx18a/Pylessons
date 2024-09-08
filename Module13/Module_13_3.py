from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
api = '**********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
   await message.answer('Введите команду /start, чтобы начать общение')
