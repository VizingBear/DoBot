import traceback

from aiogram import types, F, Router
from aiogram.filters import CommandStart

from bot.keyboards import base

base_router = Router()

@base_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')


@base_router.message(F.text == 'Спасибо, помогло!')
async def feeling_panic5(message: types.Message):
    await message.answer('Рады были вам помочь', reply_markup=base.base_keyboard)