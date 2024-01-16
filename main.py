import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from database.setup import initialize_database
from handlers import routers_list
from config import BOT_TOKEN

logger = logging.getLogger(__name__)

async def main():
    storage = MemoryStorage()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=storage)
    dp.include_routers(*routers_list)
    await initialize_database(reset_db=False)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.info("Bot Started")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot Stopped")
