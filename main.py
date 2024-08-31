import time
import telebot

API_TOKEN = '7517940619:AAFM8sfVjLLcsDIaWwaP81F1rw0kq4CsL78'
CHANNEL_ID = '@ahlsnov1'  # Kanal ID'si
bot = telebot.TeleBot(API_TOKEN)

last_message_id = None

def send_and_delete_message():
    global last_message_id
    # Avvalgi xabarni o'chirish
    if last_message_id:
        bot.delete_message(CHANNEL_ID, last_message_id)
    # Yangi xabarni yuborish
    sent_message = bot.send_message(CHANNEL_ID, "Salom")
    last_message_id = sent_message.message_id

if __name__ == "__main__":
    while True:
        send_and_delete_message()
        time.sleep(60)  # 10 daqiqa kutish (600 soniya)