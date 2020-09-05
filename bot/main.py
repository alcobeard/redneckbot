import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token="1378253464:AAE6fDSGuhNNrGGrlxlBPXOZbQdCAiCZjP4")
dp = Dispatcher(bot)


# @bot.message_handler(content_types=["text"])
# # Название функции не играет никакой роли, в принципе
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)
#     print(message)
@dp.message_handler(content_types=['text'])
async def echo(message):
    await message.reply(message.text)


@dp.message_handler(content_types=['new_chat_members'])
async def greeting(message):
    await message.reply(text='hello')
    print(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)