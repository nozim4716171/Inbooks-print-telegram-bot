from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    """
    Bot komandalarini o'rnatish
    """
    commands = [
        BotCommand(command="start", description="Botni ishga tushurish"),
        BotCommand(command="help", description="Yordam"),
        BotCommand(command="about", description="Bot haqida ma'lumot"),
    ]
    
    await bot.set_my_commands(commands)