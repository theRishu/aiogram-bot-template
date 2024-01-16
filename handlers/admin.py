from aiogram import Router ,types
from aiogram.filters import Command
from filters.admin import AdminFilter
from database import user as db
from aiogram import Bot

admin_router = Router()

admin_router.message.filter(AdminFilter())


@admin_router.message(Command("stats"))
async def stats(message: types.Message) -> None:
    all_count  = await db.get_all_count()
    stats_message = (
        f"User Statistics 📊\n\n"
        f"Total Users: {all_count}\n"
    )
    await message.answer(stats_message)


@admin_router.message(Command("broadcast"))
async def broadcast(message: types.Message, command: Command, bot: Bot):
    # Check if the command has arguments
    args = command.args
    if not args:
        await message.answer("No message text. Use like this /broadcast message ")
        return
    users = await db.get_all_user_ids()
    for user_id in users:
        try:
            await bot.send_message(user_id,  f"{args}\nThis message is from admin" ,disable_web_page_preview=True) 
        except Exception:
            pass