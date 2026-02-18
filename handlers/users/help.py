from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandHelp

router = Router()

@router.message(CommandHelp())
async def help_command(message: Message):
    """
    /help buyrug'ini qayta ishlovchi handler. Foydalanuvchilarga botning imkoniyatlari va buyruqlari haqida ma'lumot beradi.
    """
    help_text = (
        "/start - Botni ishga tushirish\n"
        "/help - Botning imkoniyatlari va buyruqlari haqida ma'lumot\n"
        "/help <buyruq> - Buyruq haqida ma'lumot\n"
    )
    await message.answer(help_text)