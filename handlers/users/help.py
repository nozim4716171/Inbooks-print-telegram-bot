from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    """
    /help buyrug'ini qayta ishlovchi handler. Foydalanuvchilarga botning imkoniyatlari va buyruqlari haqida ma'lumot beradi.
    """
    help_text = (
        "/start - Botni ishga tushirish\n"
        "/help - Botning imkoniyatlari va buyruqlari haqida ma'lumot\n"
    )
    await message.answer(help_text)