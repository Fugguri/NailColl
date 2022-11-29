from aiogram import types
from aiogram.dispatcher.filters import Text
from main import dp, bot
from scripts.save import save_user_data
from scripts.connection import *
from keyboards.keyboards import markup


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.delete()
    await message.answer(f'Привет, <b> {message.from_user.first_name} !</b>', reply_markup=markup)
    save_user_data(command=message.from_user)


@dp.message_handler(commands=['help'])  # help button. Let it be
async def get_user_link(message: types.Message):
    help_massage = f'Бот создан - чтобы помочь тебе выбрать ноготочки!'
    await message.answer(help_massage)


@dp.message_handler(commands=['go'])
async def get_random_answer(message: types.Message):
    name, code, rgb = get_random_color('color', 'all')
    from scripts.create_img import create
    img = create(rgb)
    await bot.send_photo(message.chat.id,
                         photo=img,
                         caption=f"<b>Цвет:</b> <u>{name}</u> "
                         f"\n<b>HEX код :</b> <u>{code}</u> "
                         f"\n<b>RGB код :</b> <u>{rgb}</u> \n"
                         f"\n<b>Покрытие:</b> <u>{get_random_mat()}</u> "
                         f"\n<b>Дизайн:</b> <u>{get_random_design()}</u>"
                         )
