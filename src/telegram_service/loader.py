from aiogram import Bot, Dispatcher
from telegram_service.config import settings
from loguru import logger


log = logger
bot: Bot = Bot(settings.bot_token)
dp: Dispatcher = Dispatcher(bot)

