from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.reply.language_keyboards import language_keyboard
from data.config import CHANNEL_USERNAME

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    await message.answer(
        f"Assalomu alaykum <b>{message.from_user.first_name} 👋</b>.\n\n"
        f"<b>Inbooks print</b> 🖨 — professional kitob chop etish xizmati.\n\n"
        f"📢 Kanalimizga qo'shiling: https://t.me/{CHANNEL_USERNAME}\n\n"
        f"Tilni tanlang 🌐👇:",
        reply_markup=await language_keyboard(),
        disable_web_page_preview=True
    )
    