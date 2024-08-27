import telebot

# Telegram bot tokenini bu yerga kiriting
TOKEN = "7345533909:AAG9iYq9nLMXv0NjYoCgCH7leOT1yaR1kwU"

bot = telebot.TeleBot(TOKEN)

# Salom desa javob beradigan funksiyani yozamiz
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Qanday yordam bera olaman?")

@bot.message_handler(func=lambda message: message.text.lower() == 'salom')
def greet(message):
    bot.reply_to(message, "Salom!")

# Botni ishga tushiramiz
bot.polling()
