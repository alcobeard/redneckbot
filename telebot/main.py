import telebot
import config
import parser

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
# Название функции не играет никакой роли, в принципе
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    print(message)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='hello')


if __name__ == '__main__':
    bot.polling(none_stop=True)
