from aiogram import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
go = types.KeyboardButton('/go')
help_button = types.KeyboardButton('/help')
markup.add(go, help_button)
