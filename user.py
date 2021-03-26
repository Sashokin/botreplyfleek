# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient
from telethon import events

# todo: {залить на сервер}, {реализовать скан edit собщения}
# todo сервер: зарегистрировался, установил пип, установил requirements. Осталось: загрузить конфиг, запустить бота

from config import username_aslan, api_id_aslan, api_hash_aslan, id_aslan, api_id_alex, api_hash_alex, api_hash_main, \
    api_id_main, id_main, id_alex, username_main, username_alex, api_id_anton, id_anton, api_hash_anton, username_anton

client = TelegramClient(username_anton, api_id_anton, api_hash_anton)  # аккаунт Антона
# client = TelegramClient(username_main, api_id_main, api_hash_main)  # Саша основной ак
# client = TelegramClient(username_alex, api_id_alex, api_hash_alex)  # Саша второй ак
# client = TelegramClient(username_aslan, api_id_aslan, api_hash_aslan)  # Аслан
client.start()


# Обработчик новых сообщений
@client.on(events.NewMessage(chats=id_fleek))
async def handler_new_message(event):
    try:
        await client.send_message(id_leakchannel, event.message)
        # либо репост
        # await client.forward_messages(id_leakchannel, event.message)
    except Exception as e:
        print(e)


async def send_message_to_channel(channel, message):
    await client.send_message(channel, message)


async def main():
    # await send_message_to_channel(channel, 'test message')


# выключение по завершению процесса в пичарме
with client:
    client.run_until_disconnected()
