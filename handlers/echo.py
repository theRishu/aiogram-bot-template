from aiogram import F, types, Router

echo_router = Router()

@echo_router.message(F.text)
async def bot_echo(message: types.Message):
    await message.answer(message.text)