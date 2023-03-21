from telebot.types import Message
from config_data.config import DEFAULT_COMMAND
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message):
    text = [f"/{command} - {desc}" for command, desc in DEFAULT_COMMAND]
    bot.send_message(message.from_user.id, "hello world")





