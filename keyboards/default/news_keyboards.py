from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Екомонічні новини")],
        [KeyboardButton(text="Політичні новини")],
    ]
)