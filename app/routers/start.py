from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from app.keyboards.start import build_global_menu_keyboard


start_router = Router()


# Обробник для команди /start
@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = build_global_menu_keyboard()
    text = (
        f"Вітаю, {hbold(message.from_user.full_name)}, в інформаційній системі ветеринарної клініки!\n"
        "\nВиберіть дію"
    )
    await message.answer(
        text=text,
        reply_markup=keyboard
    )
