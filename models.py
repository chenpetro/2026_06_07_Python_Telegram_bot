import logging

logger = logging.getLogger(__name__)

from pydantic import BaseModel

class Film(BaseModel):
    name: str
    description: str
    rating: float
    genre: str | None = None
    actors: list[str] | None = None
    poster: str | None = None


   # "name": "Harry Potter and the Philosopher's Stone",
            # "description": "Harry Potter and the Philosopher's Stone (also known as Harry Potter and the Sorcerer's Stone in the United States) is a 2001 fantasy film directed by Chris Columbus and produced by David Heyman, from a screenplay by Steve Kloves, based on the 1997 novel of the same name by J. K. Rowling. It is the first instalment in the Harry Potter film series. The film stars Daniel Radcliffe as Harry Potter, with Rupert Grint as Ron Weasley, and Emma Watson as Hermione Granger. Its story follows Harry's first year at Hogwarts School of Witchcraft and Wizardry as he discovers that he is a famous wizard and begins his formal wizarding education.",
            # "rating": 7.1,
            # "genre": "Fantasy",
            # "actors": [
            #     "Daniel Radcliffe",
            #     "Rupert Grint",
            #     "Emma Watson",
            #     "John Cleese",
            #     "Robbie Coltrane",
            #     "Warwick Davis",
            #     "Richard Griffiths",
            #     "Richard Harris",
            #     "Ian Hart",
            #     "John Hurt",
            #     "Alan Rickman",
            #     "Fiona Shaw",
            #     "Maggie Smith",
            #     "Julie Walters"
            # ],
            # "poster": "https://upload.wikimedia.org/wikipedia/en/7/7a/Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg"