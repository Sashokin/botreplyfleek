# -*- coding: utf-8 -*-
import configparser
import json
from telethon.sync import TelegramClient
from telethon import connection

# todo: {как передавать id канала, чтоб работать с ним}, {реализовать получение новых сообщений},
#  {реализовать постинг уведомления о сообщении в канал}, {залить на сервер}, {реализовать постинг сообщений текстовых},
#  {реализовать скан edit собщения}, {реализовать постинг сообщений с картинкой/файлом}

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

from config import username_aslan, api_id_aslan, api_hash_aslan, id_aslan, api_id_alex, api_hash_alex, api_hash_main, api_id_main, id_main, id_alex, username_main, username_alex
from config import url_testchannel, id_testchannel, peer_id_testchannel


client = TelegramClient(username_main, api_id_main, api_hash_main)
# client = TelegramClient(username_alex, api_id_alex, api_hash_alex)
# client = TelegramClient(username_aslan, api_id_aslan, api_hash_aslan)
client.start()


# Записывает json-файл с информацией о всех сообщениях канала
async def dump_all_messages(channel):
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 1   # максимальное число записей, передаваемых за один раз
    all_messages = []   # список всех сообщений
    total_messages = 0
    total_count_limit = 1  # поменяйте это значение, если вам нужны не все сообщения

    class DateTimeEncoder(json.JSONEncoder):
        # Класс для записи дат в JSON
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        history = await client(GetHistoryRequest(peer=channel, offset_id=offset_msg, offset_date=None, add_offset=0, limit=limit_msg, max_id=0, min_id=0, hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
            json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


async def main():
    channel = await client.get_entity(url_testchannel)  # как делать с id, а не url :/
    # await dump_all_messages(channel)


# выключение, пока не закончится процесс в main
# with client:
    # client.loop.run_until_complete(main())


# выключение по завершению процесса в пичарме
with client:
    client.run_until_disconnected()

# не решил, что нам лучше, поэтому оставил 2 варианта
