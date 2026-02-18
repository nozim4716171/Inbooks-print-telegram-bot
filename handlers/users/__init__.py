from aiogram import Router

router = Router()

# Bu papkadagi barcha handlerlarni import qilish
from . import start
from . import help
from . import about

router.include_router(start.router)
router.include_router(help.router)
router.include_router(about.router)