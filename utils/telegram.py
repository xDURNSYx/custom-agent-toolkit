
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def send_telegram_message(chat_id, message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    res = requests.post(url, json=payload)
    return res.json()
