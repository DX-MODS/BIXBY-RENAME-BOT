# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN"

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed
from config import FORCE_SUB

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**πΏπ»π΄π°ππ΄ πΉπΎπΈπ½ πΌπ π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ π **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



