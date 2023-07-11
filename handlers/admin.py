# from aiogram import Router, types
# from aiogram.filters import Command
# from aiogram.types import Message
# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# from keyboards import admin_keyboard
# from services import client
# from bot import bot
#
# router = Router()
# ID = 309338412
#
#
# @router.message(Command('moderator'))
# async def command_moderator(message: Message):
#     if message.from_user.id == ID:
#         await message.answer(text='Вы авторизованы\n')
#     else:
#         await message.answer(text='Доступ ограничен')
#     await message.delete()
#
#
# @router.message(Command('send_post'))
# async def send_post(message: Message):
#     users = await client.get_users()
#     for user in users:
#         try:
#             await bot.send_message(chat_id=user.telegram_id, text='Text PROMO')
#         except:
#             print(f'Пользователю {user.telegram_id} сообщение не отправлено')
#
#     await message.reply(text='PROMO отправлено пользователям')
#
