# Copyright (C) 2021 By Attitudeking

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from modules.callsmusic.callsmusic import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Stɑɤtɩŋʛ Ɓɤøɑɗƈɑst ...`")
        if not message.reply_to_message:
            await wtf.edit("**__🔥🥂ᴩʟᴇᴀꜱᴇ ʀᴇᴩʟy ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴀᴛʀᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.................🔥__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ.....................` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`🔥🥂ɢᴄᴀꜱᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} Ƈɦɑts")
