import asyncio
import logging
import sys

from handlers import router
from middlewares.throttling import ThrottlingMiddleware
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.create_database import on_startup_db, on_shutdown_db
from utils.set_bot_commands import set_default_commands
from utils.misc.logging import setup_logger

from loader import bot, dp



async def main():
    # Logger sozlash
    logger = setup_logger(level=logging.INFO)
    
    logger.info("Bot ishga tushmoqda...")
    
    
    # Middlewarelar
    dp.message.middleware(ThrottlingMiddleware())
    
    # Routerlar
    dp.include_router(router)
    
    # Startup
    await set_default_commands(bot)
    await on_startup_notify(bot)
    await on_startup_db()
    
    # Polling
    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types()
        )
    except Exception as e:
        logger.exception(f"Bot ishida xatolik: {e}")
    finally:
        # Shutdown
        await on_shutdown_notify(bot)
        await on_shutdown_db()
        await bot.session.close()
        logger.info("Bot to'xtatildi")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot KeyboardInterrupt bilan to'xtatildi")