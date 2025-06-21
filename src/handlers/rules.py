from main import bot


@bot.message_handler(commands=['rules'])
async def send_rules(message):
    text = 'Bot rules'
    await bot.reply_to(message, text)
