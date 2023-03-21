import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

TOKEN = os.getenv("TOKEN")
DEFAULT_COMMAND = (
    ("start", "запусти бота"),
    ("help", "вывести справку")
)
