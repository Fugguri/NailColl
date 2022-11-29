import os
from aiogram import Dispatcher, Bot, types, executor
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


bot = Bot(SECRET_KEY, parse_mode="HTML")
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот запущен")


async def on_shutdown(_):
    print("Бот остановлен")


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dispatcher=dp,
                           on_shutdown=on_shutdown,
                           on_startup=on_startup,
                           skip_updates=True)
