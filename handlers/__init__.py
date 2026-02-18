from aiogram import Router

router = Router()

# Auto-import
from . import users
from . import errors

# Routerlarni ulash
router.include_router(users.router)
router.include_router(errors.router)