from aiogram import Router
from aiogram.types import Message
from aiogram import F

import json
import string

router = Router()


@router.message(F.text)
async def echo_send(message: Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()
