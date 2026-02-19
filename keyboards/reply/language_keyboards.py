from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def language_keyboard() -> ReplyKeyboardMarkup:
    keyboards = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 O'zbek tili"),
                KeyboardButton(text="🇷🇺 Русский язык")
            ]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )

    return keyboards