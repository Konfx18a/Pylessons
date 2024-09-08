from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging
import texts
from keyboards import *
from config import *
from crud_functions import *

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start_(message):
    await message.answer(texts.start + f' {message.from_user.username}', reply_markup= start_kb)

@dp.message_handler(text='О нас')
async def about_(message):
    await message.answer(texts.about, reply_markup= start_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    all_products_ = get_all_products()
    len_ = get_db_lenght()
    for i in range(0, len_):
        with open(f'img/img{i+1}.jpg', 'rb') as photo:
            await message.answer(f'Название: {all_products_[i][1]} | Описание: {all_products_[i][2]} '
                                 f'| Цена: {all_products_[i][3]}')
            await message.answer_photo(photo)
    # await message.answer('Выберите продукт для покупки', reply_markup=photo_catalog_kb)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Стоимость')
async def price_(message):
    await message.answer('Выберите интересующий товар', reply_markup=catalog_kb)

@dp.callback_query_handler(text = 'baby')
async def buy_baby(call):
    await call.message.answer(texts.baby_bicycle, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'hardtail')
async def buy_hard(call):
    await call.message.answer(texts.hardTail_bicycle, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'BMX')
async def buy_bmx(call):
    await call.message.answer(texts.BMX_bicycle, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'MTB')
async def buy_MTB(call):
    await call.message.answer(texts.MTB_bicycle, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='back_to_catalog')
async def back_to_catalog(call):
    await call.message.answer('Что вам интересно?', replay_markup=catalog_kb)
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




