from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Стоимость'),
        KeyboardButton(text='О нас'),
        KeyboardButton(text='Купить'),
        KeyboardButton(text='Регистрация')
         ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Детский велосипед', callback_data='baby')],
    [InlineKeyboardButton(text='Гравийный велосипед', callback_data='hardtaile')],
    [InlineKeyboardButton(text='Велосипед BMX', callback_data='BMX')],
    [InlineKeyboardButton(text='Велосипед MTB', callback_data='MTB')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url='https://pro-bike.ru/product/velosipedy/')]
                     ]
)

# photo_catalog_kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Продукт1', callback_data='product_buying')],
#         [InlineKeyboardButton(text='Продукт2', callback_data='product_buying')],
#         [InlineKeyboardButton(text='Продукт3', callback_data='product_buying')],
#         [InlineKeyboardButton(text='Продукт4', callback_data='product_buying')]
#          ],
# )
photo_catalog_kb = InlineKeyboardMarkup()
photo_catalog_kb.row_width=4
photo_catalog_kb.add(InlineKeyboardButton(text='Продукт1', callback_data='product_buying'),
                           InlineKeyboardButton(text='Продукт2', callback_data='product_buying'),
                           InlineKeyboardButton(text='Продукт3', callback_data='product_buying'),
                           InlineKeyboardButton(text='Продукт4', callback_data='product_buying'),
                    )