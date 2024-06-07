import requests
import re

from papertion.item import Item


re_space = re.compile(r"(?u:\s)")


def get_item_from_doi(doi_str: str) -> Item:
    """
    Crossref API を使用して DOI から論文情報を得る

    Args:
      doi (str): DOI

    Returns:
      dict: 論文情報を含む辞書
    """
    url = f"https://api.crossref.org/works/{doi_str}"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        info = data["message"]

        authors = _author_list(info["author"])
        year = info["published"]["date-parts"][0][0]
        name = info["author"][0]["family"] + str(year)
        title = "".join(info["title"])
        first = authors[0]
        journal = info["container-title"][0]

        return Item(
            name=name,
            title=title,
            first=first,
            year=year,
            journal=journal,
            authors=authors,
        )
    else:
        raise Exception(
            f"DOI '{doi_str}' の情報取得に失敗しました: {response.status_code}",
        )


def _author_list(authors: list) -> list[str]:
    author_list = []
    for a in authors:
        given = a["given"]
        given = re_space.sub(" ", given)
        family = a["family"]
        family = re_space.sub(" ", family)
        author_list.append(given + " " + family)
    return author_list
