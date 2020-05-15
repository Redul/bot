import config
import telebot
from telebot import types
import random

bot = telebot.TeleBot(config.token)


# Обычный режим
@bot.message_handler(content_types=["text"])
def any_msg(message):
    answer_list = ["Естесна", "Конечно", "Само собой", "Да"]
    random.shuffle(answer_list)
    keyboard = types.InlineKeyboardMarkup()
    if answer_list[0] == "Да":
        callback_button = types.InlineKeyboardButton(text=answer_list[0], callback_data="yes")
    else:
        callback_button = types.InlineKeyboardButton(text=answer_list[0], callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Хочешь узнать своё скрытое желание?", reply_markup=keyboard)


# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    answer_list = ["Естесна", "Конечно", "Само собой", "Да"]
    random.shuffle(answer_list)
    kb = types.InlineKeyboardMarkup()
    if answer_list[0] == "Да":
        kb.add(types.InlineKeyboardButton(text=answer_list[0], callback_data="yes"))
    else:
        kb.add(types.InlineKeyboardButton(text=answer_list[0], callback_data="test"))
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Ну давай-давай, нажми",
        input_message_content=types.InputTextMessageContent(message_text="Хочешь узнать своё скрытое желание?"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    wishlist = ["Кикнуть Егора", "Выпить", "Остаться 5.0-щиком"]
    random.shuffle(wishlist)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=wishlist[0])
        elif call.data == "yes":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пизда")

    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text=wishlist[0])
        elif call.data == "yes":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Пизда")


if __name__ == '__main__':
    random.seed()
    bot.infinity_polling()
