import logging
from aiogram import Bot

from data.config import ADMINS

logger = logging.getLogger(__name__)


async def on_startup_notify(bot: Bot):
    """
    Bot ishga tushganda adminlarga xabar yuborish
    """
    for admin_id in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text="✅ Bot ishga tushdi!"
            )
        except Exception as err:
            logger.exception(f"Admin {admin_id} ga xabar yuborib bo'lmadi: {err}")

async def on_shutdown_notify(bot: Bot):
    """
    Bot to'xtaganda adminlarga xabar yuborish
    """
    for admin_id in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text="⚠️ Bot to'xtatildi!"
            )
        except Exception as err:
            logger.exception(f"Admin {admin_id} ga xabar yuborib bo'lmadi: {err}")


async def notify_admins(bot: Bot, message: str):
    """
    Adminlarga istalgan xabar yuborish
    
    :param bot: Bot instance
    :param message: Yuborilishi kerak bo'lgan xabar
    """
    for admin_id in ADMINS:
        try:
            await bot.send_message(chat_id=admin_id, text=message)
        except Exception as err:
            logger.exception(f"Admin {admin_id} ga xabar yuborib bo'lmadi: {err}")