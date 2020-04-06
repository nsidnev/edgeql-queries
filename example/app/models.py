from dataclasses import dataclass
from typing import Set


@dataclass
class Person:
    first_name: str
    last_name: str


@dataclass
class Movie:
    title: str
    year: str
    director: Person
    actors: Set[Person]
