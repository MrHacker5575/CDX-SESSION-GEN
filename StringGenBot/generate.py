from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)

import config

ask_ques = "» ▷ 𝐂𝐡𝐨𝐨𝐬𝐞 𝐓𝐡𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 ✔️ : :"
buttons_ques = [
    [
        InlineKeyboardButton("🍻𝗣ʏʀᴏɢʀᴀᴍ ᴠ1🍻", callback_data="pyrogram1"),
        InlineKeyboardButton("🦴𝗣ʏʀᴏɢʀᴀᴍ V2🦴", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🍷𝗧єʟєτнοиє🍷", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("🍒𝗣ʏʀᴏɢʀᴀᴍ 𝗕០Ƭ🍒", callback_data="pyrogram_bot"),
        InlineKeyboardButton("💞𝗧єʟєτнοиє 𝗕០Ƭ💞", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="💎𝗦τяιиց 𝗚єи💎", callback_data="generate")
    ]
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    # (Your existing code here...)
    if telethon:
        string_session = "Your Telethon String Session"
    else:
        string_session = "Your Pyrogram String Session"
    
    text = f"𝐓𝐡𝐢𝐬 𝐈𝐬 𝐘𝐨𝐮𝐫 {ty} 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 \n\n{string_session} \n\n🍒 𝐍𝐎𝐓𝐄 : 𝐃𝐨𝐧𝐭 𝐒𝐡𝐚𝐫𝐞 𝐖𝐢𝐭𝐡 𝐀𝐧𝐲𝐨𝐧𝐞 𝐀𝐧𝐝 𝐃𝐨𝐧𝐭 𝐅𝐨𝐫𝐠𝐞𝐭 𝐓𝐨 𝐉𝐨𝐢𝐧 @TEAM_CDX"
    
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass

    await client.disconnect()
    await bot.send_message(msg.chat.id, "» 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐆𝐫𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐘𝐨𝐮 {} 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧.\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐞𝐜𝐤 𝐘𝐨𝐮𝐫 𝐒𝐚𝐯𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐆𝐞𝐭 𝐈𝐭 💨".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))