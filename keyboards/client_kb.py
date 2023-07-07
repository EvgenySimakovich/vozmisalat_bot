from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

mainmenu_buttons = [
    [
        KeyboardButton(text='О нас'),
        KeyboardButton(text='Адрес')
    ]
]

client_keyboard = ReplyKeyboardMarkup(
    keyboard=mainmenu_buttons,
    resize_keyboard=True
)
