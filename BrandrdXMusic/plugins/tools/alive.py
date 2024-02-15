import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph//file/5374701ae0678848e9631.mp4",
        caption=f"❤️ හෙලෝ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ මම වේගවත් Music bot කෙනෙක්. ඔයාලගෙ group වලටත් මාව Add කරගන්න. සුපිරි වැඩ කෑලි තියෙනව මගේ.\n\n💫 ඔයාලට ප්‍රශ්න තියෙනවනම් අපේ group එකට ඇවිත් අහන්න✨...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ Ishini, The Owner ", url=f"https://t.me/ishini_qr"
            ),
            InlineKeyboardButton(
                text="☆ ꜱᴜᴘᴘᴏʀᴛ 💗", url=f"https://t.me/illumnati1"
            ),
        ],
                [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ💗", url=f"https://t.me/illumnati1"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
