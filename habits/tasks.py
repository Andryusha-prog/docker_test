import requests
from celery import shared_task

from config.settings import TELEGRAM_URL, TELEGRAM_BOT_TOKEN


@shared_task
def send_tg_message(chat_id, message):
    params = {"chat_id": chat_id, "text": message}

    requests.get(
        f"{TELEGRAM_URL}{TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
