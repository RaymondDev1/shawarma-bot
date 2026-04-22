import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import load_config
from database import init_db
from handlers.menu import router as menu_router
from handlers.order import router as order_router


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    config = load_config()
    init_db()

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_router(menu_router)
    dp.include_router(order_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
