from os import getenv
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.log.log import get_log
from app.routers.start import start_router
from app.routers.animals import animal_router
from app.routers.reviews import review_router


load_dotenv()


root_router = Router()
root_router.include_routers(start_router, animal_router, review_router)


async def main() -> None:
    TOKEN = getenv("BOT_API")

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())