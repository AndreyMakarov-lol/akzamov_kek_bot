from aiogram import Bot, Dispatcher
#Импортируем инструменты для работы с переменными окружения
import os
from dotenv import load_dotenv
#Загружаем переменные окружения
load_dotenv()
#Берем из переменной окружения токен
BOT_TOKEN = os.getenv("BOT_TOKEN")
#Инициализация бота
bot = Bot(token=BOT_TOKEN)
#Инициализация диспетчера
dp = Dispatcher()

