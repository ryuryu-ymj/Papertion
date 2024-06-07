from datetime import date
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    title: str
    first: str
    year: int
    journal: str
    authors: list[str]
    retrieved: date = date.today()
