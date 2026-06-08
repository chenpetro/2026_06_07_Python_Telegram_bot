import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import TOKEN


# Bot token can be obtained via https://t.me/BotFather

# TOKEN = getenv("8728056325:AAFdbnBx-15jsCwb6DVvVhZJanf-GGnXHG4")
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(Command("help"))  
async def command_help(message):
#list all available commands
    await message.answer("/help - list all available commands\n/about - information about this bot")

@dp.message(Command("about"))  
async def command_about(message):
    await message.answer("This bot is created using aiogram library. It is a simple echo bot that responds to /help and /about commands.")

@dp.message(Command("multiply"))
async def command_multiply(message):
    # Extract numbers from the message text
    numbers = [int(num) for num in message.text.split()[1:]]
    if len(numbers) < 2:
        await message.answer("Please provide at least two numbers to multiply. Usage: /multiply 2 3")
        return
    result = 1
    for num in numbers:
        result *= num
    await message.answer(f"The result of multiplying {', '.join(map(str, numbers))} is {result}")

# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with /start command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use message.answer(...) alias
#     # and the target chat will be passed to :ref:aiogram.methods.send_message.SendMessage
#     # method automatically or call API method directly via
#     # Bot instance: bot.send_message(chat_id=message.chat.id, ...)
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())