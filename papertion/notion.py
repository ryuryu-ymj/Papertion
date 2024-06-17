from pprint import pprint
import tomllib
import notion_client as nc

from papertion.item import Item, ntprop_type


def get_config() -> (nc.Client, int, dict):
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    token = config["notion"]["token_key"]
    client = nc.Client(auth=token)

    db_id = config["notion"]["database_id"]

    prop_name = config["properties"]

    return client, db_id, prop_name


def set_properties():
    client, db_id, prop_name = get_config()

    ret = client.databases.retrieve(database_id=db_id)
    prop_old = ret["properties"]

    prop_add = {}
    prop_rename = {}
    for name, field in prop_name.items():
        if name not in prop_old:
            if field == "name":
                prop_rename["title"] = {"name": name}
            else:
                prop_add[name] = ntprop_type[field]

    if len(prop_add) == 0 and len(prop_rename) == 0:
        print("No updates on the database properties.")
    else:
        print("Updating the database properties...")
        client.databases.update(
            database_id=db_id,
            **{
                "properties": prop_add | prop_rename,
            },
        )
        if len(prop_add) != 0:
            print("Add new properties to the database: " + ", ".join(prop_add))
        if len(prop_rename) != 0:
            rename = [it["name"] for it in prop_rename.values()]
            print(
                "Rename properties of the database: " + ", ".join(rename),
            )


def insert_item(item: Item):
    client, db_id, prop_name = get_config()

    prop_field = item.to_ntprop()
    prop = {}
    for name, field in prop_name.items():
        prop[name] = prop_field[field]

    pprint(prop)
    client.pages.create(
        **{
            "parent": {"database_id": db_id},
            "properties": prop,
        },
    )
