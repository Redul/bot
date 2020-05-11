from telebot import types


def create_markup(answer_type):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_items = []
    if answer_type == "hello":
        list_items = ["Привет👋"]
    else:
        list_items = ["Ок", "Слыш, ты ебало то завали"]
    for item in list_items:
        markup.add(item)
    return markup
