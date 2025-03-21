import request
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id
    }
    response = request.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
    return response
