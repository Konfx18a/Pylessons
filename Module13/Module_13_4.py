from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
api = '***************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(our_age=message.text)
    await message.answer('Введите свой вес')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(our_growth=message.text)
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(our_weight=message.text)
    await UserState.weight.set()
    data = await state.get_data()
    rez = 10 * float(data['our_weight']) + 6.25 * float(data['our_growth']) - 5 * float(data['our_age']) + 5
    await message.answer(f' Ваша норма калорий {rez}')
    state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
