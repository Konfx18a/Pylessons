from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
api = '********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
keyb = InlineKeyboardMarkup(resize_keyboard=True)
inline_button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton('Формула рассчета', callback_data='formulas')
keyb.row(inline_button1, inline_button2)
kb = ReplyKeyboardMarkup(resize_keyboard = True)
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
    await message.answer('Рассчет калорий для мужчины по возрасту, весу и росту')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=keyb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

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
    await UserState.weight.set()
    data = await state.get_data()
    rez = 10 * float(data['our_weight']) + 6.25 * float(data['our_growth']) - 5 * float(data['our_age']) + 5
    await message.answer(f' Ваша норма калорий {rez}')
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
