import json
import os
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from database.orm import get_one
from models.user import User


class I18nMiddleware(BaseMiddleware):
    def __init__(self, locales_dir: str = 'locales', default_lang: str = 'uz'):
        self.locales_dir = locales_dir
        self.default_lang = default_lang
        self.translations: Dict[str, Dict[str, str]] = {}
        self._load_translations()


    def _load_translations(self):
        """ Barch JSON tarjima fayllarni yuklash """
        for filename in os.listdir(self.locales_dir):
            if filename.endswith('.json'):
                lang = filename.replace('.json', '')
                filepath = os.path.join(self.locales_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    self.translations[lang] = json.load(file)

    
    def get_text(self, lang: str, key: str, **kwargs) -> str:
        """ Kalitga mos matnni qaytaradi """
        return self.translations.get(lang, {}).get(
            key, self.translations.get(self.default_lang, {}).get(key, key)
        )
    
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user = await get_one(User, telegram_id=event.from_user.id)
        lang = user.language if user and user.language else self.default_lang
        data['i18n'] = lambda key: self.get_text(lang, key)
        return await handler(event, data)