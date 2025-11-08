#8414023618:AAGA3yO08KG7gTg-Qw0CLbJpjMveg1q1HsI
import telebot
import random
import time
from bot import gen_pass
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8414023618:AAGA3yO08KG7gTg-Qw0CLbJpjMveg1q1HsI")

@bot.message_handler(commands=['start', 'hi'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['гойда'])
def send_coins(message):
    x1 = 0
    x = random.randint(100, 1000)
    bot.reply_to(message, 'Твой мешок пополнен:')
    x1 += x
    bot.reply_to(message, str(x1))

@bot.message_handler(commands=['timer'])
def send_time(message):
    bot.reply_to(message, 'Введите время (в секундах)')
    t = int(message.text.split()[1]) if len(message.text.split()) > 1 else 3
    time.sleep(t)
    bot.reply_to(message, 'Время истекло')

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()