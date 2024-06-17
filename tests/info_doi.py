import requests
from pprint import pprint


def get_item_from_doi(doi_str: str):
    url = f"https://api.crossref.org/works/{doi_str}"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        info = data["message"]
        pprint(info)
    else:
        raise Exception(
            f"DOI '{doi_str}' の情報取得に失敗しました: {response.status_code}"
        )


doi = "10.1088/1742-5468/aceb4f"
doi = "10.1371/journal.pcbi.1009739"
doi = "10.1103/PhysRevX.14.021001"
doi = "https://doi.org/10.1103/PhysRevLett.61.259"
get_item_from_doi(doi)
