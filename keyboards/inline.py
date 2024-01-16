from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_button():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="alert", callback_data="alert")],
            [InlineKeyboardButton(text="open website ", url="https://example.com")],
        ]
    )
    return kb