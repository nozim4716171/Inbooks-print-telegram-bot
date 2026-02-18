from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("about"))
async def about_command(message: Message):
    """
    /about buyrug'ini qayta ishlovchi handler.
    Bot haqida umumiy ma'lumot beradi.
    """
    about_text = (
        "<b>Mukammal telegram bot</b>\n\n"
        "Versiya: 1.0.0\n"
        "Ishlab chiquvchi: @nozimjon_hamdamov\n\n"
        "Bu bot foydalanuvchilarga qulay va samarali xizmat ko'rsatish uchun yaratilgan."
    )
    await message.answer(about_text)
