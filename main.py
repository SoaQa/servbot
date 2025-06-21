#!/usr/bin/python
import asyncio
from src import handlers # NoQa
from src.common import bot

if __name__ == '__main__':
    asyncio.run(bot.polling())
