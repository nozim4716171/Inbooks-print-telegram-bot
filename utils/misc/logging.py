import logging
import sys


def setup_logger(level: int = logging.INFO):
    """Oddiy logging sozlash"""
    
    logging.basicConfig(
        level=level,
        format="%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Aiogram noise ni kamaytirish
    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)

    return logging.getLogger(__name__)