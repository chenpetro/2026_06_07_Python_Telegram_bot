from aiogram.filters import Command, CommandStart
from aiogram.types.bot_command import BotCommand

HELP = "help"
START = "start"
FILMS = "films"
ADD_FILM = "add_film"


commands = [START, HELP, FILMS, ADD_FILM]

COMMAND_START = Command(START)
COMMAND_HELP = Command(HELP)
COMMAND_MULTIPLY = Command("multiply")
COMMAND_ABOUT = Command("about")
COMMAND_FILMS = Command(FILMS)
COMMAND_ADD_FILM = Command(ADD_FILM)
BOT_COMMAND_START = BotCommand(command=START, description="Start the bot")
BOT_COMMAND_HELP = BotCommand(command=HELP, description="List all available commands")
BOT_COMMAND_MULTIPLY = BotCommand(command="multiply", description="Multiply numbers. Usage: /multiply 2 3")
BOT_COMMAND_ABOUT = BotCommand(command="about", description="Information about this bot")
BOT_COMMAND_FILMS = BotCommand(command=FILMS, description="List all available films")
BOT_COMMAND_ADD_FILM = BotCommand(command=ADD_FILM, description="Add a new film")


bot_commands = [BOT_COMMAND_START, BOT_COMMAND_HELP, BOT_COMMAND_MULTIPLY, BOT_COMMAND_ABOUT, BOT_COMMAND_FILMS, BOT_COMMAND_ADD_FILM]