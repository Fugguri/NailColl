import os
import telebot
from telebot import types
from func import save_user_data, get_random_v2

SECRET_KEY = os.getenv('KEY')
'''Импортирование секретного кода для бота. Код получен от BOT_FATHER. 
Секретный код лежит в отдельном .env файле,
для обеспечения безопасного доступа к боту, в случае размещения на открытых ресурсах.
'''

bot = telebot.TeleBot(SECRET_KEY)


@bot.message_handler(commands=['start'])
def start(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    go = types.KeyboardButton('/go')
    help_button = types.KeyboardButton('/help')
    introduction = f'Привет, <b> {massage.from_user.first_name} !</b>'
    markup.add(go, help_button)
    bot.send_message(massage.chat.id, introduction, reply_markup=markup, parse_mode='html')
    save_user_data(command=massage.from_user)


@bot.message_handler(commands=['help'])  # help button. Let it be
def get_user_link(message):
    help_massage = f'Бот создан - чтобы помочь тебе выбрать ноготочки!'
    bot.send_message(message.chat.id, help_massage, parse_mode='html')


@bot.message_handler(commands=['go'])
def get_random_answer(massage):
    markup = types.InlineKeyboardMarkup()  # add button in keyboard

    markup.add(types.InlineKeyboardButton('Посмотреть цвет в интернете',
                                          url=f"https://get-color.ru/#!{get_random_v2('color', 'code')[1:]}"))

    bot.send_message(massage.chat.id,
                     f" <b>Цвет:</b> <u>{get_random_v2('color', 'name')}</u> "
                     f"\n<b>Покрытие:</b> <u>{get_random_v2('mat')}</u> "
                     f"\n<b>Дизайн:</b> <u>{get_random_v2('design')}</u>",
                     parse_mode='html', reply_markup=markup, )


bot.polling(none_stop=True)
