import json

def get_all_films():
    with open('films.json', 'r', encoding='utf-8') as file:
        films = json.load(file)
    return films["films"]