from aiogram import Router

router = Router()

# Bu papkadagi barcha handlerlarni import qilish
from . import error_handler

router.include_router(error_handler.router)