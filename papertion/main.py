import click

import papertion.doi as doi_mod
import papertion.notion as notion


@click.group()
def main():
    pass


@main.command("prop")
def update_db_properties():
    """Add necessary properties to the database."""
    notion.update_db_properties()


@main.command("doi")
@click.argument("doi")
def new_item_from_doi(doi: str):
    """Insert a new paper identified by given DOI into the database."""
    item = doi_mod.get_item_from_doi(doi)
    notion.insert_item(item)
