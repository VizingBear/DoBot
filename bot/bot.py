from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from .handlers.base import base_router
from config.config import token


bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher()
dp.include_routers(base_router)
