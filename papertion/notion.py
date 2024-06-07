from pprint import pprint
import tomllib
import notion_client as nc

from papertion.item import Item

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

token = config["notion"]["token_key"]
client = nc.Client(auth=token)

db_id = config["notion"]["database_id"]


def update_db_properties():
    client.databases.update(
        database_id=db_id,
        **{
            "properties": {
                "Name": {
                    "title": {},
                },
                "Title": {
                    "rich_text": {},
                },
                "Retrieved": {
                    "date": {},
                },
                "First": {
                    "select": {},
                },
                "Year": {
                    "number": {},
                },
                "Journal": {
                    "select": {},
                },
            },
        },
    )


def _rich_text(text: str) -> dict:
    return {"rich_text": [{"type": "text", "text": {"content": text}}]}


def _select(name: str) -> dict:
    return {"select": {"name": name}}


def insert_item(item: Item):
    client.pages.create(
        **{
            "parent": {"database_id": db_id},
            "properties": {
                "Name": {"title": [{"text": {"content": item.name}}]},
                "Title": _rich_text(item.title),
                "Retrieved": {
                    "date": {
                        "start": item.retrieved.strftime("%Y-%m-%d"),
                    },
                },
                "First": _select(item.first),
                "Year": {
                    "number": item.year,
                },
                "Journal": _select(item.journal),
            },
        },
    )
