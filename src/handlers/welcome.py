from src.common import bot


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, я ServBot.\nПросто напишите мне что-нибудь, и я повторю это!'
    await bot.reply_to(message, text)
