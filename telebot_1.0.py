import telebot
from telebot import types

bot = telebot.TeleBot('5400061015:AAFONAnfRMWtE0sGvcs1HAKopTbJFuBE0tw')

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    Btn_1 = types.KeyboardButton('кнопка 1')
    Btn_2 = types.KeyboardButton('кнопка 2')
    markup.add(Btn_1, Btn_2)
    bot.send_message(message.chat.id, 'test', reply_markup=markup)


bot.infinity_polling()

