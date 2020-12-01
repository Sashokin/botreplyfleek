# -*- coding: utf-8 -*-
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import bot_token

# todo:


bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# обработчик всех сообщений и команд в чате с ботом - если бот работает, он отвечает
@dp.message_handler()
async def process_bot_check(message: types.Message):
    await message.reply("bruh im working")


if __name__ == '__main__':
    executor.start_polling(dp)

