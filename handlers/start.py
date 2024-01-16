from typing import Optional
from aiogram import Router , types , Bot
from aiogram.filters import CommandStart , CommandObject
from database import user as db
start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message:types.Message, command:CommandObject, bot:Bot) -> None:
    ref: Optional[str] = command.args
    try:    
        user = await db.select_user(message.from_user.id)
        if user:
            await  message.answer("This is example Bot.\nPress /help for commands")
        else:
            if ref:
                if ref.isdigit()==True:
                    await db.update_bonus_count(int(ref))

            await db.add_user(message.from_user.id)
            await message.reply("Welcome to Bot.\nPress /help for commands")

    except Exception as e:
        await message.answer(str(e))
        