import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Send Message
def send_signal_message(message):
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    
    res = requests.get(url)
    if res.status_code == 200:
        return "sent"
    else:
        return "failed"