from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from commands import commands

# def create_menu_keyboard():
    # builder = ReplyKeyboardBuilder()
    # for com in commands:
    #     builder.add(KeyboardButton(text=f"/{com}"))
    # return builder.as_markup()

def create_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    commands = ["start", "help", "settings"]  # Example commands
    for com in commands:
        builder.add(KeyboardButton(text=f"{com}"))
    return builder.as_markup()

def create_inline_keyboard():
    builder = InlineKeyboardBuilder()
    button = "Send secret"
    builder.button(text=button, callback_data="secret_button")
    
    return builder.as_markup()