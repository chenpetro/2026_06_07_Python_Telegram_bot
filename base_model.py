import json

def get_film_info(file_path="films.json"):
    with open(file_path, 'r', encoding='utf-8') as file:
        films = json.load(file)
    return films["films"]

def add_film(film_model, file_path="films.json"):
    with open(file_path, 'r', encoding='utf-8') as file:
        films = json.load(file)

    films["films"].append(film_model.model_dump())
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(films, file, ensure_ascii=False, indent=4)