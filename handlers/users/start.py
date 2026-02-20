from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.reply.language_keyboards import language_keyboard
from keyboards.reply.menu_keyboards import main_menu_keyboard, phone_request_keyboard
from data.config import CHANNEL_USERNAME
from database.orm import add_one, get_one, update_by_filter
from models.user import User
from states.registration import RegistrationState
from utils.i18n import I18nMiddleware

router = Router()

i18n_middleware = I18nMiddleware()


def get_text(lang: str, key: str, **kwargs) -> str:
    """Berilgan til va kalit bo'yicha tarjima matnini qaytaradi"""
    text = i18n_middleware.get_text(lang, key)
    if kwargs:
        text = text.format(**kwargs)
    return text


async def show_main_menu(message: Message, lang: str):
    """Asosiy menyuni ko'rsatish"""
    i18n = lambda key: get_text(lang, key)
    await message.answer(
        get_text(lang, "main_menu"),
        reply_markup=main_menu_keyboard(i18n),
    )


async def ask_phone_number(message: Message, lang: str, state: FSMContext):
    """Telefon raqam so'rash"""
    i18n = lambda key: get_text(lang, key)
    await message.answer(
        get_text(lang, "send_phone_number_text"),
        reply_markup=phone_request_keyboard(i18n),
    )
    await state.set_state(RegistrationState.phone)


@router.message(CommandStart())
async def start_command(message: Message, bot: Bot, state: FSMContext):
    user_id = message.from_user.id
    user = await get_one(User, telegram_id=user_id)

    if not user:
        # Yangi user - DB ga qo'shish
        await add_one(
            User,
            telegram_id=user_id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )

    if user and user.language:
        # Til mavjud - telefon raqamni tekshirish
        lang = user.language
        if user.phone_number:
            # Telefon raqam bor - asosiy menyuga
            await state.clear()
            await message.answer(
                get_text(lang, "welcome_back", first_name=message.from_user.first_name),
                reply_markup=main_menu_keyboard(lambda key: get_text(lang, key)),
                disable_web_page_preview=True,
            )
        else:
            # Telefon raqam yo'q - so'rash
            await ask_phone_number(message, lang, state)
    else:
        # Til yo'q - til tanlashni ko'rsatish
        await state.set_state(RegistrationState.language)
        await message.answer(
            get_text(
                "uz",
                "welcome",
                first_name=message.from_user.first_name,
                channel=CHANNEL_USERNAME,
            ),
            reply_markup=await language_keyboard(),
            disable_web_page_preview=True,
        )


@router.message(RegistrationState.language, F.text == "🇺🇿 O'zbek tili")
async def select_uzbek(message: Message, state: FSMContext):
    lang = "uz"
    user_id = message.from_user.id

    await update_by_filter(User, {"telegram_id": user_id}, language=lang)
    await state.update_data(language=lang)

    user = await get_one(User, telegram_id=user_id)
    if user and user.phone_number:
        await state.clear()
        await show_main_menu(message, lang)
    else:
        await ask_phone_number(message, lang, state)


@router.message(RegistrationState.language, F.text == "🇷🇺 Русский язык")
async def select_russian(message: Message, state: FSMContext):
    lang = "ru"
    user_id = message.from_user.id

    await update_by_filter(User, {"telegram_id": user_id}, language=lang)
    await state.update_data(language=lang)

    user = await get_one(User, telegram_id=user_id)
    if user and user.phone_number:
        await state.clear()
        await show_main_menu(message, lang)
    else:
        await ask_phone_number(message, lang, state)


@router.message(RegistrationState.phone, F.contact)
async def receive_phone_number(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone = message.contact.phone_number

    await update_by_filter(User, {"telegram_id": user_id}, phone_number=phone)

    user = await get_one(User, telegram_id=user_id)
    lang = user.language if user else "uz"

    await message.answer(get_text(lang, "phone_saved"))
    await state.clear()
    await show_main_menu(message, lang)
