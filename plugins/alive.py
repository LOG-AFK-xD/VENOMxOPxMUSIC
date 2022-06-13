import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/49b5112926e556cb64c9e.jpg",
        caption=f"""**➖➖➖➖➖➖➖➖➖➖➖➖➖➖
♻️ Hello, I Am Khushi Music Bot Telegram Groups.
🦋 I'm a telegram streaming bot with some useful features.

✦ Powered By - [⇆ㅤ◁ㅤㅤ❚❚ㅤㅤ▷ㅤ↻](t.me/Official_Afk_xD) .
➖➖➖➖➖➖➖➖➖➖➖➖➖➖**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Owner", url=f"t.me/Official_Pro_xD"),
                        InlineKeyboardButton(text="Channel", url=f"https://t.me/ITZZ_OFFICIAL"),
                      InlineKeyboardButton(text="Group", url=f"https://t.me/LOVE_X_POISONS"),
                  ],[
                      InlineKeyboardButton(
                        "✦ Support", url=f"https://t.me/UNIQUE_SOCIETY"
                    ),
                    InlineKeyboardButton(
                        "Updates ✦", url=f"https://t.me/BLAZE_SUPPORT"                  
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "✦ Add Me To Group ✦", url="t.me/khushirobot?startgroup=true"),

                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "venomop"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4efa4c558c98393f24c61.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=
                        "Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )

