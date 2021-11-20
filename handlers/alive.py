# https://t.me/Alone_shaurya_king

from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(command(["start", f"start@Attitude_Player_Bot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/be59d5c0d55a63ba62193.jpg",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂ᴊᴏɪɴ ᴏᴜʀ ꜱᴜᴩᴩᴏʀᴛ🥂🔥", url=f"https://t.me/sweetkingdom1")
                ]
            ]
        ),
    )


@Client.on_message(command(["help", f"help@Attitude_Player_Bot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/be59d5c0d55a63ba62193.jpg",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂ᴄʟɪᴄᴋ ʜᴇʀᴇ ꜰᴏʀ ʜᴇʟᴩ🥂🔥", url=f"https://t.me/sweetkingdom1")
                ]
            ]
        ),
    )
