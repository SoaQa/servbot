#!/usr/bin/python
import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from src import handlers # NoQa


bot = AsyncTeleBot(os.environ["SERVBOT_TELEGRAM_TOKEN"])


if __name__ == '__main__':
    asyncio.run(bot.polling())
