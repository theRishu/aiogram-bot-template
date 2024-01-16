from aiogram.filters import Command
from aiogram import F, types, Router
from database import user as db
from keyboards.inline import inline_button
from keyboards.regular import regular_button

other_router = Router()



@other_router.message(Command("inline_keyboard"))
async def inline_keyboard(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await message.answer("Example of Inline Button.",reply_markup= inline_button())
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   

@other_router.callback_query(F.data =="alert")
async def alert(call: types.CallbackQuery):
    await call.answer("Example alert", show_alert = True)


@other_router.message(Command("regular_keyboard"))
async def regular_keyboard(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await message.answer("Example of Regular Button.",reply_markup= regular_button())
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   


@other_router.message(F.text.contains("+1"))
async def plus_1(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await db.plus_user_rating(user.user_id)
        await message.answer("Rating increased by plus one.")
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   

@other_router.message(F.text.contains("-1"))
async def plus_1(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await db.minus_user_rating(user.user_id)
        await message.answer("Rating decreased by minus one.")
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   
  
 

@other_router.message(F.text.contains("close"))
async def plus_1(message: types.Message ) -> None:
    user = await db.select_user(message.from_user.id)
    if user:
        await message.answer("Keyboard Removed" , reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   
  

@other_router.message(Command("info"))
async def inline_keyboard(message: types.Message) -> None:
    
    user = await db.select_user(message.from_user.id)
    if user:
        info_text = f"User ID: {user.user_id}\nUse Count: {user.use_count}\nRating: {user.rating}\nBio: {user.bio}"
        await message.answer(info_text)
    else:
        await message.reply("You are not a registered user.\nPress /start to register.")
   