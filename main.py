import telebot
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7459499876:AAE-ph1h4V6xDu4A10Ag_4JNVl7OeajSY2s"
bot = telebot.TeleBot(TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_DOMAIN/' + TOKEN)
    return "Webhook set!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))