import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import client, other, admin
from database import database
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
logging.basicConfig(level=logging.INFO)


async def on_startup():
    print('Bot started')
    database.create_db()


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.include_router(client.router)
    dp.include_router(other.router)
    dp.include_router(admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
