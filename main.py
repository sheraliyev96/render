import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime
import csv

TOKEN = '7545685077:AAFHFeWTIdgr41Uv1RoxHltoBovNFCwFJvs'
bot = telebot.TeleBot(TOKEN)

CHANNEL_ID = '@snovpyton2'  

# Ishchilar ro'yxati
ishchilar = {
    "ID 1": "Hamidillo",
    "ID 2": "Nematillo",
    "ID 3": "Shopr Bogishamol",
    "ID 6": "Dilmurod",
    "ID 7": "Muhammadali",
    "ID 10": "Iroda Abdurahimova Kichik",
    "ID 11": "Minojat opa",
    "ID 12": "Mavludaxon",
    "ID 13": "Moxira Mominova",
    "ID 14": "Iroda Obidova",
    "ID 15": "Diyora Yusupova",
    "ID 16": "Mastura",
    "ID 17": "Zebo",
    "ID 18": "Ogilloy",
    "ID 19": "Gulshoda",
    "ID 20": "Komola",
    "ID 21": "Guli Tillaboyeva",
    "ID 22": "Gulshanoy Tillaboyeva",
    "ID 23": "Zamira",
    "ID 27": "Durdona",
    "ID 28": "Mohlaroy Tolanboyeva",
    "ID 29": "Shaxodatoy",
    "ID 30": "Odinaxon Jorayeva",
    "ID 31": "Mahliyo Abdurahimova",
    "ID 32": "Shaxnoza Otajonova",
    "ID 33": "Gulsora Mamajonova",
    "ID 37": "Nasiba Ganieva",
    "ID 38": "Lolaxon",
    "ID 39": "Dilafruz Tojiboyeva",
    "ID 40": "Mohidil Rasulova",
    "ID 41": "Ogilloy Halimova",
    "ID 42": "Oyshaxon Jorayeva",
    "ID 43": "Gavxary Dehqonova",
    "ID 44": "Shirinoy Baxodirova",
    "ID 46": "Saidaxon Sirojiddinova",
    "ID 47": "Dilfuza Jabaraliyeva",
    "ID 48": "Shaxnoza Tavakkalova",
    "ID 49": "Xurshida Turgunova",
    "ID 52": "Mahliyo Tillaboyeva",
    "ID 53": "Mubina Abdujalilova Anjan",
    "ID 54": "Gulshanoy Ahmadjonova",
    "ID 56": "Umida Umarova",
    "ID 57": "Ziyoda Mirzayeva",
    "ID 58": "Gulnora Tojiboyeva",
    "ID 59": "Maxliyoxon Mirzayeva",
    "ID 60": "Gulchexra Soqova",
    "ID 61": "Muhayyo Mahliyo Qizi",
    "ID 62": "Dilfuza Daaz",
    "ID 63": "Muhayyo Yusupova",
    "ID 64": "Xayitoy Nabijonova",
    "ID 65": "Nargiza Abubakirova",
    "ID 66": "Nigora Mamajonova",
    "ID 67": "Dilafruz Rahmanova",
    "ID 68": "Matluba Teshaboyeva",
    "ID 69": "Zulfiya Ismailova",
    "ID 70": "Nargiza Qoqonboyeva",
    "ID 71": "Jumagul Tojiboyeva",
    "ID 73": "Mastura Jalabek Daz",
    "ID 75": "Shaxnoza Parlov",
    "ID 78": "Dilfuza Mallayeva",
    "ID 81": "Mubina Segaza",
    "ID 83": "Gulnora Gulomova",
    "ID 85": "Gulnora Eski Parlov",
    "ID 98": "Muhayyo Saidalimova",
    "ID 99": "Mastura Nishonboyeva",
    # Qo'shimcha ishchilar...
}

# Ishlar ro'yxati
ish_nomi = [
    "AVANS",
    "PAYPOQ",
    "JARIMA",
    "Operator",
    "Averlo",
    "Dazmol",
    "Dazmol solish",
    "Dazmol olish",
    "Etiket",
    "Parlov",
    "Paket",
    "Tosh",
    "Toshkaropka",
    "Jemchuk7",
    "Vishilka",
    "Sim",
    "Karopka",
    "Kar dazmol",
    "Paxta",
    "Buklab ot",
    "Belbog",
    "Povurlik",
    "Bantik",
    "Selikon",
    "Jemchuk24",
    "Jemchuk16",
    "MING SOM",
    # Qo'shimcha ishlar...
]

# Parol
PASSWORD = "9196"

# Foydalanuvchi parolini saqlash uchun
authorized_users = set()

# Har bir ishchining qilgan ishlar ro'yxati
ishchi_ishlari = {}
user_id = None
user_ishlari = []
ish_tanlangan = None

# Barcha ma'lumotlarni yozish uchun yagona CSV fayli
csv_filename = 'ishchilar_malumotlari.csv'

# CSV faylga sarlavhalar qo'shish (agar fayl yangi yaratilgan bo'lsa)
def initialize_csv():
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')  # delimiter sifatida nuqtali vergul qo'shildi
        # Fayl boshida ustunlarning nomlarini qo'shish
        if file.tell() == 0:  # Fayl bo'sh bo'lsa
            writer.writerow(["Sana", "Soat", "ID", "Ism", "Ish Nomi", "Miqdor"])

initialize_csv()

# /start komandasiga javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Parolni kiriting:")

# Parolni tekshirish
@bot.message_handler(func=lambda message: message.text == PASSWORD)
def password_check(message):
    authorized_users.add(message.chat.id)
    bot.reply_to(message, "Parol tasdiqlandi! Ishchi ID raqamingizni kiriting:", reply_markup=id_klaviaturasi())

@bot.message_handler(func=lambda message: message.chat.id not in authorized_users)
def unauthorized_access(message):
    bot.reply_to(message, "Noto'g'ri parol! Iltimos, qaytadan urinib ko'ring.")

# ID ro'yxatini chiqarish uchun klaviatura
def id_klaviaturasi():
    markup = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
    buttons = [KeyboardButton(id_raqam) for id_raqam in ishchilar.keys()]
    markup.add(*buttons)
    return markup

# ID raqamini qabul qilish
@bot.message_handler(func=lambda message: message.text in ishchilar.keys() and message.chat.id in authorized_users)
def id_qabul(message):
    global user_id, user_ishlari
    user_id = message.text
    user_ishlari = []
    bot.send_message(message.chat.id, f"  {ishchilar[user_id]}! Qilgan ishingizni tanlang:", reply_markup=ishlar_klaviaturasi())

# Ishlar ro'yxatini chiqarish uchun klaviatura
def ishlar_klaviaturasi():
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton(ish) for ish in ish_nomi]
    markup.add(*buttons)
    markup.add(KeyboardButton("ISHLAR TUGADI"))
    return markup

# Ish turini tanlash va miqdorni qabul qilish
@bot.message_handler(func=lambda message: message.text in ish_nomi or message.text == "ISHLAR TUGADI")
def ish_tanlash(message):
    global user_ishlari, ish_tanlangan
    if message.text == "ISHLAR TUGADI":
        if not user_id or user_id not in ishchilar:
            bot.send_message(message.chat.id, "Iltimos, avval ID raqamingizni tanlang.")
        else:
            # CSV faylga yozish
            with open(csv_filename, mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=';')  # delimiter sifatida nuqtali vergul qo'shildi
                for ish in user_ishlari:
                    writer.writerow([
                        datetime.now().strftime("%Y-%m-%d"),  # Sana
                        datetime.now().strftime("%H:%M:%S"),  # Soat
                        user_id,  # ID
                        ishchilar[user_id],  # Ism
                        ish[0],  # Ish nomi
                        ish[1]   # Miqdor
                    ])
            
            # Kanalga yuborish
            for ish in user_ishlari:
                bot.send_message(CHANNEL_ID, f"Ishchi: {ishchilar[user_id]}\nIsh: {ish[0]}\nMiqdor: {ish[1]}")
            
            bot.send_message(message.chat.id, "Ishlar saqlandi va kanalga yuborildi!")
            user_ishlari = []
            bot.send_message(message.chat.id, "Yangi ish uchun ID tanlang:", reply_markup=id_klaviaturasi())
    else:
        ish_tanlangan = message.text
        bot.send_message(message.chat.id, "Miqdorni kiriting:")

# Ish miqdorini qabul qilish
@bot.message_handler(func=lambda message: ish_tanlangan is not None and message.text.isdigit())
def miqdor_qabul(message):
    global user_ishlari, ish_tanlangan
    miqdor = int(message.text)
    user_ishlari.append([ish_tanlangan, miqdor])
    ish_tanlangan = None
    bot.send_message(message.chat.id, "Yana ish tanlang yoki 'ISHLAR TUGADI'ni bosing.", reply_markup=ishlar_klaviaturasi())

bot.polling()
