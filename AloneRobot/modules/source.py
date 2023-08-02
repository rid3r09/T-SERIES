from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AloneRobot import OWNER_ID, dispatcher
from AloneRobot import pbot as client

Alone = "https://graph.org/file/05a05c75b049e2f4eed9b.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Alone,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𝗧𝗢𝗫𝗜𝗖](https://t.me/NOOBS_ALWAYS_OP)♨️
  
╚═════ஜ۩۞۩ஜ════╝

**[𝗧 - 𝗦𝗘𝗥𝗜𝗘𝗦](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🫣 𝐌σι 𝐏αρα 🫣",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        " 🙃 𝐌εℓα 𝐑ερσ 🙂",
                        url="https://t.me/DOSTO_KI_M3HFIL",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
