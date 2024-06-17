from datetime import date
from dataclasses import dataclass


def _ntobj_title(title: str) -> dict:
    return {"title": [{"text": {"content": title}}]}


def _ntobj_rich_text(text: str) -> dict:
    return {"rich_text": [{"type": "text", "text": {"content": text}}]}


def _ntobj_select(option: str) -> dict:
    return {"select": {"name": option}}


def _ntobj_multi_select(option_list: list[str]) -> dict:
    return {"multi_select": [{"name": n} for n in option_list]}


def _ntobj_url(url: str) -> dict:
    return {"url": url}


def _ntobj_number(num: int) -> dict:
    return {"number": num}


def _ntobj_date(date: date) -> dict:
    return {"date": {"start": date.strftime("%Y-%m-%d")}}


ntprop_type = {
    "name": {"title": {}},
    "title": {"rich_text": {}},
    "first": {"select": {}},
    "year": {"number": {}},
    "journal": {"select": {}},
    "authors": {"multi_select": {}},
    "url": {"url": {}},
    "retrieved": {"date": {}},
}


@dataclass
class Item:
    name: str
    title: str
    first: str
    year: int
    journal: str
    authors: list[str]
    url: str
    retrieved: date = date.today()

    def to_ntprop(self) -> dict:
        return {
            "name": _ntobj_title(self.name),
            "title": _ntobj_rich_text(self.title),
            "first": _ntobj_select(self.first),
            "year": _ntobj_number(self.year),
            "journal": _ntobj_select(self.journal),
            "authors": _ntobj_multi_select(self.authors),
            "url": _ntobj_url(self.url),
            "retrieved": _ntobj_date(self.retrieved),
        }
