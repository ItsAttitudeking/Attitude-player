from pyrogram import Client as Bot
from pyrogram import idle
from modules.callsmusic import run
from modules.config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
