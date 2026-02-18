from typing import Callable


def rate_limit(limit: int):
    """
    Handler uchun throttling limit belgilash
    
    :param limit: Soniyalarda limit
    """
    def decorator(func: Callable):
        # Funksiyaga metadata qo'shish
        func.__throttling_limit__ = limit
        return func
    return decorator