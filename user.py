# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient
from telethon import events

# todo: {реализовать скан edit собщения}

from config import username_aslan, api_id_aslan, api_hash_aslan, id_aslan, api_id_alex, api_hash_alex, api_hash_main, \
    api_id_main, id_main, id_alex, username_main, username_alex, api_id_anton, id_anton, api_hash_anton, username_anton
from config import id_fleek, id_leakchannel, id_testchannel, id_tesla

client = TelegramClient(username_anton, api_id_anton, api_hash_anton)  # аккаунт Антона
# client = TelegramClient(username_main, api_id_main, api_hash_main)  # Саша основной ак
# client = TelegramClient(username_alex, api_id_alex, api_hash_alex)  # Саша второй ак
# client = TelegramClient(username_aslan, api_id_aslan, api_hash_aslan)  # Аслан
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


# Обработчик отредактированных сообщений
# @client.on(events.MessageEdited(chats=id_testchannel))
# async def handler_edit_message(event):
    # try:
        # попытаемся найти в базе данных сообщение-клон
        # message_to_edit = database.find_by_id(event.message.id)
        # if message_to_edit is None:
            # return
        # если такое нашлось -- отредактируем его
        # id_message_to_edit = message_to_edit['mirror_message_id']
        # await client.edit_message(id_leakchannel, event.message.id, event.message.message)
    # except Exception as e:
        # print(e)


async def send_message_to_channel(channel, message):
    await client.send_message(channel, message)


async def main():
    last_message_id = 0
    channel = await client.get_entity(id_leakchannel)  # для id - int, для ссылок - str
    # await send_message_to_channel(channel, 'test message')


# выключение по завершению процесса в пичарме
with client:
    client.run_until_disconnected()
