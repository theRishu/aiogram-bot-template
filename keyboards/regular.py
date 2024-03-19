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


def start_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=
           [ [KeyboardButton(text="Start Make Money 💷")]] ,
        resize_keyboard=True
    )
    return kb
    
def menu_keyboards():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 Earn "), KeyboardButton(text="👥 Partners")],
            [KeyboardButton(text="⚖️ Balance"), KeyboardButton(text="❓ Help")],
        ],
        resize_keyboard=True
    )
    return kb