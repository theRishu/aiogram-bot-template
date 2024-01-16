from aiogram.filters import Command
from aiogram import types, Router

help_router = Router()

@help_router.message(Command("help"))
async def help_command(message: types.Message) -> None:
    help_text = (
        "Here are the available commands:\n\n"
        "/start - Register or restart\n"
        "/inline_keyboard - Show an example of Inline Keyboard with two buttons\n"
        "/regular_keyboard - Show an example of Regular Keyboard with buttons +1, -1, and Close\n"
        "+1  - Increase rating by +1\n"
        "-1 - Decrease rating by -1\n"
        "close - Remove keyboard\n"
        "/info - Get user information"
    )

    await message.answer(help_text)