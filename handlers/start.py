from typing import Optional
from aiogram import Router , types , Bot , F
from aiogram.filters import CommandStart , CommandObject
from database import user as db
from aiogram.enums import ParseMode
from keyboards.regular import start_keyboard , menu_keyboards

start_router = Router()

msg = """
<b> 👋 Hey there! </b>

If you read this, you are as much a business as I who wants to make money!
This bot has a very simple system: sponsor channels pay the bot for advertising, and the bot pays you for subscribing to these channels!

You can withdraw money from the bot to: PayTM, UPI, Mobikwik Visa/Mastercard, other.
"""




@start_router.message(CommandStart())
async def command_start_handler(message:types.Message, command:CommandObject, bot:Bot) -> None:
    ref: Optional[str] = command.args
    try:    
        user = await db.select_user(message.from_user.id)
        if not  user:
            if ref:
                if ref.isdigit()==True:
                    await db.update_bonus_count(int(ref))
                    try: 
                        await  bot.send_message(ref , "Someone joined from your link. You got 200.")
                    except Exception :
                        pass

       
            await db.add_user(message.from_user.id)
        await message.reply(msg , parse_mode=ParseMode.HTML , reply_markup=start_keyboard())

    except Exception as e:
        await message.answer(str(e))
        


@start_router.message(F.text.contains('Start Make Money 💷'))
async def command_start_handler(message:types.Message, bot:Bot) -> None:
    try:    
        user = await db.select_user(message.from_user.id)
        if user:
            await message.answer("Menu !", reply_markup=menu_keyboards())
        else:
            await  message.answer("Press /start to start.")


    except Exception as e:
        await message.answer(str(e))
        