# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient
from telethon import events

# todo: {реализовать скан edit собщения}

from config import api_id_anton, api_hash_anton, username_anton
from config import id_fleek, id_leakchannel, id_testchannel, id_tesla

client = TelegramClient(username_anton, api_id_anton, api_hash_anton)  # аккаунт Антона
client.start()


# Обработчик новых сообщений
@client.on(events.NewMessage(chats=id_fleek))
async def handler_new_message(event):
    try:
        await client.forward_messages(id_leakchannel, event.message)
    except Exception as e:
        print(e)


@client.on(events.NewMessage(chats=id_tesla))
async def handler_new_message(event):
    try:
        await client.forward_messages(id_leakchannel, event.message)
    except Exception as e:
        print(e)


@client.on(events.NewMessage(chats=id_testchannel))
async def handler_new_message(event):
    try:
        await client.forward_messages(id_leakchannel, event.message)
    except Exception as e:
        print(e)


async def send_message_to_channel(channel, message):
    await client.send_message(channel, message)


# выключение по завершению процесса в пичарме
with client:
    client.run_until_disconnected()
