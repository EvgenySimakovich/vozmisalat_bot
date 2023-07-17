from aiogram import Router, F
from aiogram.filters import CommandStart, Text
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services import client
from keyboards import client_keyboard

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    if await client.get_user(telegram_id=user_id):
        await message.answer(text=f'{username}, рады вновь видеть Вас!\n'
                                  f'Мы по-прежнему одни из немногих готовим полезную еду вкусно ☺️',
                             reply_markup=client_keyboard)
        await message.delete()
    else:
        await message.answer(text=f'{username}, спасибо, что подписались на наш канал!\n\n'
                                  f'Мы всегда рады новым гостям, ведь мы одни из немногих готовим полезную еду вкусно ☺️\n'
                                  f'Ну и, конечно, подарочки!\n'
                                  f'При <a href="https://sabyget.ru/delivery/vozmisalat_lad">заказе наших блюд на доставку</a> укажите в специальном поле промо НОВЫЙ и получите скидку 15% на весь заказ!',
                             parse_mode='HTML',
                             reply_markup=client_keyboard,
                             disable_web_page_preview=True)
        await client.add_user(telegram_id=user_id, username=username)
        await message.delete()


@router.message(Text('Адрес'))
async def about_handler(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Яндекс Карта', url='https://yandex.ru/maps/org/vozmi_salat_/216691454177/?ll=30.437644%2C59.933028&z=16'),
    )
    try:
        await message.answer(text='Заневский просп., д.67, корп.2\n(на выходе с эскалатора, 4 этаж)',
                             reply_markup=builder.as_markup())
        await message.delete()
    except Exception as e:
        print(e)


@router.message(Text('Время работы'))
async def about_handler(message: Message):
    try:
        await message.answer(text='Рады видеть Вас 10.00-22.00 ежедневно, без выходных')
        await message.delete()
    except Exception as e:
        print(e)


@router.message(Text('Копить бонусы'))
async def about_handler(message: Message):
    try:
        await message.answer(text='Программа лояльности <a href="https://sabyget.ru/go/FmJT7M">Возьми Салат</a>',
                             parse_mode='HTML')
        await message.delete()
    except Exception as e:
        print(e)


@router.message(Text('Меню'))
async def about_handler(message: Message):
    try:
        await message.answer(text='<a href="https://sabyget.ru/delivery/vozmisalat_lad">Вот здесь</a> можно посмотреть меню и сделать заказ',
                             parse_mode='HTML')
        await message.delete()
    except Exception as e:
        print(e)


@router.message(Text('Доставка'))
async def about_handler(message: Message):
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text='Яндекс Еда', url='https://eda.yandex.ru/r/voz_mi_salat?placeSlug=vozmi_salat'))
    builder.add(InlineKeyboardButton(text='Деливери Маркет', url='https://market-delivery.yandex.ru/r/voz_mi_salat?placeSlug=vozmi_lvado&shippingType=delivery',))
    builder.add(InlineKeyboardButton(text='Сбер Маркет', url='https://sbermarket.ru/Vozmisalat?sid=59343'))
    try:
        await message.answer(text='Если вдруг мы не можем доставить на нужный адрес, вы можете заказать наши блюда через сервисы партнеров',
                             reply_markup=builder.as_markup())
        await message.delete()
    except Exception as e:
        print(e)