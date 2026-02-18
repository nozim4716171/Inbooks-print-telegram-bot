from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_limit: int = 1):
        self.caches: Dict[int, TTLCache] = {}
        self.default_limit = default_limit
    
    def _get_cache(self, limit: int) -> TTLCache:
        if limit not in self.caches:
            self.caches[limit] = TTLCache(maxsize=10_000, ttl=limit)
        return self.caches[limit]
    
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        
        # Handler funksiyasidan throttling limitni olish
        handler_func = data.get("handler").callback  # aiogram 3 da handler objekti
        limit = getattr(handler_func, "__throttling_limit__", self.default_limit)
        
        cache = self._get_cache(limit)
        
        if user_id in cache:
            return await event.answer(f"⏳ Iltimos {limit} soniya kuting!")
        
        cache[user_id] = None
        return await handler(event, data)