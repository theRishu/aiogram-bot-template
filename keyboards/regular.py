from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

def regular_button():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="+1"), KeyboardButton(text="-1")],
            [KeyboardButton(text="close")],
        ],
        resize_keyboard=True
    )
    return kb