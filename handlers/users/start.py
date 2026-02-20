from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.reply.language_keyboards import language_keyboard
from data.config import CHANNEL_USERNAME
from database.orm import add_one, get_one
from models.user import User

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    user_id = message.from_user.id
    user = await get_one(User, telegram_id=user_id)
    if not user:
        await add_one(User, telegram_id=user_id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, username=message.from_user.username)
    await message.answer(
        f"Assalomu alaykum <b>{message.from_user.first_name} 👋</b>.\n\n"
        f"<b>Inbooks print</b> 🖨 — professional kitob chop etish xizmati.\n\n"
        f"📢 Kanalimizga qo'shiling: https://t.me/{CHANNEL_USERNAME}\n\n"
        f"Tilni tanlang 🌐👇:",
        reply_markup=await language_keyboard(),
        disable_web_page_preview=True
    )
    