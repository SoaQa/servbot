import os

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.environ["SERVBOT_TELEGRAM_TOKEN"])
