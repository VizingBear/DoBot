from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_base = [
    [KeyboardButton(text='Приветственная кнопка')],
]

base_keyboard = ReplyKeyboardMarkup(
        keyboard=kb_base,
        resize_keyboard=True
    )