import telebot
from telebot import types
import urllib.request

# соединяемся с апи
TOKEN = '1113660723:AAGYPXwH7_y4uJuEFk3LC9LpwnS3G3KWn1w' # токен бота
bot = telebot.TeleBot(TOKEN)
#                python C:\telebot\bot.py

# слушаем событие ввода команды старт и выводим приветсвие
@bot.message_handler(commands=['start', 'go'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\n Я <b>{1.first_name}</b>🤖,\nВоспользуйся коммандой /help, чтобы узнать о всех существующих коммандах бота'.format(message.from_user, bot.get_me()), parse_mode='html')

# получаем информацию и выбираем нужный жанр
@bot.message_handler(commands=['info'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton(text='комедии', callback_data='num0')
    button1 = types.InlineKeyboardButton(text='ужасы', callback_data='num1')
    button2 = types.InlineKeyboardButton(text='триллеры', callback_data='num2')
    button3 = types.InlineKeyboardButton(text='боевик', callback_data='num3')
    button4 = types.InlineKeyboardButton(text='детектив', callback_data='num4')
    markup.add(button0, button1, button2,button3, button4)
    bot.send_message(message.chat.id, 'Выберите что вам нужно:', reply_markup = markup)

# чтобы получить помощь ,используем данную команду
@bot.message_handler(commands=['help', 'helper'])
def help(message):
    bot.send_message(message.chat.id, 'Комманды которые пока доступны:\n1) /go & /start - начало работы бота.\n2) /info - информация.\n3) /help - помощь')

# помощь бота в выборе фильма
@bot.message_handler(content_types=['text'])
def Notext(message):
    text = message.text.lower()
    if text == 'привет':
        bot.send_message(message.chat.id, 'Привет, рад видеть тебя!)')
    else:
        bot.send_message(message.chat.id, 'Не знаю что ответить :(\nПопробуй /help')

# предоставление нескольких вариантов на выбор
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    chat_id = c.message.chat.id
    if c.data == 'num1':
        bot.send_message(chat_id, 'Чужой\nХэллоуин\nСияние', parse_mode='html')
    elif c.data == 'num0':
        bot.send_message(chat_id, '1+1\nОдин дома\nЗверополис')
    elif c.data == 'num2':
        bot.send_message(chat_id, 'Леон\nПрестиж\nУбить билла', parse_mode='html')
    elif c.data == 'num3':
        bot.send_message(chat_id, 'Начало\nГладиатор\nМатрица', parse_mode='html')
    elif c.data == 'num4':
        bot.send_message(chat_id, 'Ликвидация\nИгра\nПсихо', parse_mode='html')

bot.polling()
