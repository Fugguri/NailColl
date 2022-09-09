import os
import telebot
from telebot import types
from func import save_user_data, get_random_color, get_random_design, get_random_mat

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
    from PIL import Image
    name, code, rgb = get_random_color('color', 'all')
    rgb_code = tuple(map(int, rgb.split(' ')))
    img = Image.new('RGB', (250, 250), rgb_code)
    bot.send_photo(massage.chat.id,
                   photo=img,
                   caption=f"<b>Цвет:</b> <u>{name}</u> "
                   f"\n<b>HEX код :</b> <u>{code}</u> "
                   f"\n<b>RGB код :</b> <u>{rgb}</u> \n"
                   f"\n<b>Покрытие:</b> <u>{get_random_mat()}</u> "
                   f"\n<b>Дизайн:</b> <u>{get_random_design()}</u>",
                   parse_mode='html'
                   )
    img = Image.open("nail.jpg")
    img = img.convert("RGB")

    datas = img.getdata()

    new_image_data = []
    for item in datas:
        # change all white (also shades of whites) pixels to yellow
        if item[0] in list(range(1, 256)) and item[1] in range(1, 80) and item[2] in range(1,80):
            new_image_data.append(rgb_code)
        else:
            new_image_data.append(item)

    # update image data
    img.putdata(new_image_data)
    bot.send_photo(massage.chat.id,
                   photo=img)
    print('done')


bot.polling(none_stop=True)
