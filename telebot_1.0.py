import os
import telebot
from telebot import types

token = os.getenv(TOKEN)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    Btn_1 = types.KeyboardButton('кнопка 1')
    Btn_2 = types.KeyboardButton('кнопка 2')
    markup.add(Btn_1, Btn_2)
    bot.send_message(message.chat.id, 'test', reply_markup=markup)


bot.infinity_polling()

