import logging

logger = logging.getLogger(__name__)


from aiogram.fsm.state import State, StatesGroup

class FilmStates(StatesGroup):
    name_state = State()
    desc_state = State()
    rate_state = State()