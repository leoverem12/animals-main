from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тваринок на лікуванні")
    builder.button(text="Додати тваринку на лікування")
    builder.button(text="Показати список вилікуваних тваринок")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати відгук")
    builder.adjust(1)
    return builder.as_markup()
