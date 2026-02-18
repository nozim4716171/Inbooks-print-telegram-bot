from aiogram.types import ErrorEvent
from aiogram import Router
import logging
from aiogram.exceptions import (
    TelegramAPIError, TelegramNetworkError, TelegramRetryAfter, TelegramMigrateToChat,
    TelegramBadRequest, TelegramNotFound, TelegramConflictError, TelegramUnauthorizedError,
    TelegramForbiddenError, TelegramServerError, RestartingTelegram, TelegramEntityTooLarge,
    ClientDecodeError, UnsupportedKeywordArgument, CallbackAnswerException, SceneException,
    AiogramError, DetailedAiogramError
)

router = Router()
logger = logging.getLogger(__name__)


@router.errors()
async def error_handler(event: ErrorEvent):
    """
    Botdagi barcha xatoliklarni ushlash va ularni qayta ishlash uchun umumiy xatolik ushlagich.
    """
    
    # MUHIM: Aniq exceptionlarni birinchi tekshirish kerak, keyin umumiylarni
    
    # Flood control - Telegram ko'p so'rov yuborishni blokladi
    if isinstance(event.exception, TelegramRetryAfter):
        logger.warning(
            f"Flood control: {event.exception.retry_after} sekund kutish kerak\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Chat supergroup ga migrate qilindi
    if isinstance(event.exception, TelegramMigrateToChat):
        logger.info(
            f"Chat migrate: yangi chat_id {event.exception.migrate_to_chat_id}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Yuborilayotgan media hajmi juda katta
    if isinstance(event.exception, TelegramEntityTooLarge):
        logger.error(
            f"Media hajmi juda katta: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Telegram serverida xato yuz berdi (5xx xatolari)
    if isinstance(event.exception, TelegramServerError):
        logger.error(
            f"Telegram server xatosi: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Telegram qayta ishga tushirilmoqda
    if isinstance(event.exception, RestartingTelegram):
        logger.warning(
            f"Telegram qayta ishga tushirilmoqda: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Bot bloklangan yoki guruhdan chiqarilgan
    if isinstance(event.exception, TelegramForbiddenError):
        logger.warning(
            f"Bot bloklangan: {event.exception.message}\n"
            f"Update: {event.update.model_dump_json(indent=2, exclude_none=True)}"
        )
        return True
    
    # Token noto'g'ri yoki bot API tomonidan ban qilingan
    if isinstance(event.exception, TelegramUnauthorizedError):
        logger.critical(
            f"Token noto'g'ri: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Webhook va polling bir vaqtda ishga tushirilgan
    if isinstance(event.exception, TelegramConflictError):
        logger.error(
            f"Konflikt (webhook/polling): {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Telegramda topilmadi (masalan, noto'g'ri message_id)
    if isinstance(event.exception, TelegramNotFound):
        logger.warning(
            f"Topilmadi: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # Noto'g'ri so'rov (message not modified, can't parse entities va h.k.)
    if isinstance(event.exception, TelegramBadRequest):
        logger.error(
            f"Noto'g'ri so'rov: {event.exception.message}\n"
            f"Method: {event.exception.method}\n"
            f"Update: {event.update.model_dump_json(indent=2, exclude_none=True)}"
        )
        return True
    
    # Tarmoq xatosi (connection timeout, DNS error va h.k.)
    if isinstance(event.exception, TelegramNetworkError):
        logger.error(
            f"Tarmoq xatosi: {event.exception.message}\n"
            f"Method: {event.exception.method}"
        )
        return True
    
    # JSON javobini dekodlashda xato
    if isinstance(event.exception, ClientDecodeError):
        logger.error(
            f"JSON decode xatosi: {event.exception.message}\n"
            f"Original error: {event.exception.original}"
        )
        return True
    
    # Noto'g'ri kalit so'z argumenti (filter xatosi)
    if isinstance(event.exception, UnsupportedKeywordArgument):
        logger.error(f"Noto'g'ri filter argumenti: {event.exception.message}")
        return True
    
    # Callback query javobida xato
    if isinstance(event.exception, CallbackAnswerException):
        logger.error(f"Callback answer xatosi: {str(event.exception)}")
        return True
    
    # FSM sahnasida xato
    if isinstance(event.exception, SceneException):
        logger.error(f"FSM sahna xatosi: {str(event.exception)}")
        return True
    
    # Aiogramning batafsil xatolari (DetailedAiogramError AiogramError dan meros oladi)
    if isinstance(event.exception, DetailedAiogramError):
        logger.error(f"Aiogram batafsil xatosi: {event.exception.message}")
        return True
    
    # Aiogramning umumiy xatolari
    if isinstance(event.exception, AiogramError):
        logger.error(f"Aiogram xatosi: {str(event.exception)}")
        return True
    
    # Umumiy Telegram API xatolari (oxirgi navbatda tekshirish kerak!)
    if isinstance(event.exception, TelegramAPIError):
        logger.error(
            f"Telegram API xato: {event.exception.message}\n"
            f"Method: {event.exception.method}\n"
            f"Update: {event.update.model_dump_json(indent=2, exclude_none=True)}"
        )
        return True
    
    # Boshqa barcha noma'lum xatolar
    logger.exception(
        f"Kutilmagan xato: {event.exception}\n"
        f"Update: {event.update.model_dump_json(indent=2, exclude_none=True)}"
    )
    return True