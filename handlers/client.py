from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.types import Message

from services import client
from keyboards import client_keyboard

router = Router()

array_users = []


@router.message(Command('start'))
async def command_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    if await client.get_user(telegram_id=user_id):
        await message.answer(text=f'{username}, рады вновь видеть Вас в Салат Бар!',
                             reply_markup=client_keyboard)
        await message.delete()
    else:
        await message.answer(text=f'{username}, добро пожаловать в Салат Бар!\nДарим Вам промокод на первый заказ.',
                             reply_markup=client_keyboard)
        await client.add_user(telegram_id=user_id, username=username)


@router.message(Text('О нас'))
async def about_handler(message: Message):
    try:
        await message.answer(text='Салатбар Варвары Яковлевой')
        await message.delete()
    except Exception as e:
        print(e)


@router.message(Text('Адрес'))
async def about_handler(message: Message):
    try:
        await message.answer(text="Заневский просп., д.67, корп.2\n(на выходе с эскалатора, 4 этаж)")
        await message.delete()
    except Exception as e:
        print(e)

# async def help_handler(message: types.Message):
#     try:
#         await message.reply('https://www.google.com/')
#         await message.delete()
#     except Exception as e:
#         print(e)
#

