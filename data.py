import logging

logger = logging.getLogger(__name__)

import json
from decor import sync_log_function_call
from models import Film

@sync_log_function_call
def get_all_films(file_path: str = "films.json") -> list[dict]:
    """
    Function returns a list of all films from the JSON file.
    """


    with open(file_path, 'r', encoding='utf-8') as file:
        films = json.load(file)
    return films["films"]

@sync_log_function_call
def add_film(film_model: Film, file_path: str = "films.json") -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        films = json.load(file)


    films["films"].append(film_model.model_dump())

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(films, file, ensure_ascii=False, indent=4)