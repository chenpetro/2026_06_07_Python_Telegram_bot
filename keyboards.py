from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from commands import commands

def create_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    for com in commands:
        builder.add(KeyboardButton(text=f"/{com}"))
    return builder.as_markup()