from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}, botimizga xush kelibsiz!")