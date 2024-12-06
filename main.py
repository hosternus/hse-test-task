from asyncio import run

import logging
logging.basicConfig(level=logging.INFO)

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import admin, user

async def main():

    dp = Dispatcher()

    dp.include_router(admin.router)
    dp.include_router(user.router)

    bot = Bot(BOT_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())