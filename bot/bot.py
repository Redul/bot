import config
import utils
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = utils.create_markup("hello")
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def check_answer(message):
    keyboard_hider = types.ReplyKeyboardRemove()
    if message.text == "Привет👋":
        markup = utils.create_markup("answer")
        bot.send_message(message.chat.id, "Чё ты мне пишешь?\nИди ботай", reply_markup=markup)
    if message.text == "Ок":
        bot.send_message(message.chat.id, "😎", reply_markup=keyboard_hider)
    elif message.text == "Слыш, ты ебало то завали":
        bot.send_message(message.chat.id, "(((", reply_markup=keyboard_hider)


if __name__ == '__main__':
    bot.infinity_polling()
