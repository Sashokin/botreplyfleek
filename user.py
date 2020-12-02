# -*- coding: utf-8 -*-
import configparser
import json
from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

from config import username_aslan, api_id_aslan, api_hash_aslan, api_id_alex, api_hash_alex, api_hash_main, api_id_main, id_main, id_alex, username_main, username_alex


#client = TelegramClient(username_main, api_id_main, api_hash_main)
#client = TelegramClient(username_alex, api_id_alex, api_hash_alex)
client = TelegramClient(username_aslan, api_id_aslan, api_hash_aslan)
client.start()


