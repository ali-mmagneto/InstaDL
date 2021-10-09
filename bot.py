import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import import_conf
from telebot import types
from parse_insta import main, delete_file

bot = telebot.TeleBot(import_conf("BOT", "token"))

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    channel_button = types.InlineKeyboardButton(text="Канал", url="https://t.me/SJa_bots")
    admin_button = types.InlineKeyboardButton(text="Автор", url="https://t.me/SJ_Lynx")
    keyboard.add(channel_button, admin_button)
    chat_id = message.chat.id
    bot.send_message(chat_id, "Здравствуйте, пришлите мне ссылку на пост в instagram для скачивания", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_downloaded_file(message: types.Message):
    chat_id = message.chat.id
    if message.text.startswith('http'):
        bot.send_message(chat_id, "Подожди секунду...")
        file_name = main(link=message.text)
        if message.text.endswith('.jpg'):
            bot.send_photo(chat_id, open(file_name, 'rb'))
            delete_file(file_name)
        else:
            bot.send_video(chat_id, open(file_name, 'rb'))
            delete_file(file_name)
    else:
        bot.send_message(chat_id, "Я могу читать только ссылки😔")


bot.polling()
