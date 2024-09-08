from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
api = '****************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup( resize_keyboard = True)
button_info = KeyboardButton(text='Информация')
button_calc = KeyboardButton(text='Рассчитать')
kb.row(button_info, button_calc)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=["start"])
async def start_kb(message):
    await message.answer('Используйте клавиатуру', reply_markup= kb)


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer('Рассчет колорий для мужчины по возрасту, весу и росту')


@dp.message_handler(text="Рассчитать")
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
async def send_caloriez(message, state):
    await state.update_data(our_weight=message.text)
    data = await state.get_data()
    rez = 10 * float(data['our_weight']) + 6.25 * float(data['our_growth']) - 5 * float(data['our_age']) + 5
    await message.answer(f' Ваша норма калорий {rez}')
    state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
