#import os
import telebot
from telebot import types

'''


with open("token.txt") as f:
    TOKEN = f.read().strip()
'''

#TOKEN = ''
# os.environ[TOKEN]
#bot = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot('5400061015:AAFONAnfRMWtE0sGvcs1HAKopTbJFuBE0tw')
'''
@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    Btn_1 = types.KeyboardButton('кнопка 1')
    Btn_2 = types.KeyboardButton('кнопка 2')
    markup.add(Btn_1, Btn_2)
    bot.send_message(message.chat.id, 'test', reply_markup=markup)
'''
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Старт":
        bot.send_message(message.from_user.id, "Окей, погнали")
    elif message.text == "Стоп":
        bot.send_message(message.from_user.id, "Окей, закругляемся")
    else:
        bot.send_message(message.from_user.id, "не пиши херню!")


bot.infinity_polling()
