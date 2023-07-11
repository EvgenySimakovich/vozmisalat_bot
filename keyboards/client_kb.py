from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

client_menu_buttons = [
    [
        KeyboardButton(text='Адрес'),
        KeyboardButton(text='Время работы'),
    ],
    [
        KeyboardButton(text='Копить бонусы'),
        KeyboardButton(text='Меню'),
        KeyboardButton(text='Доставка'),
    ],
]

client_keyboard = ReplyKeyboardMarkup(
    keyboard=client_menu_buttons,
    resize_keyboard=True,
)
