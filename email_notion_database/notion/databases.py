from typing import List
import random

import email_notion_database.notion
from email_notion_database.notion.row import DataBaseRow


def get_list()-> List:
    """ Using the Search endpoint, collect all the databases available for this integration token """
    response = email_notion_database.notion.client.search()
    database_list = []
    for notion_object in response['results']:
        if notion_object['object'] == "database":
            database_list.append(notion_object)
    return database_list

def get_elements(database_id: str, max_elements: int = None, shuffle: bool=False)-> List[DataBaseRow]:
    response = email_notion_database.notion.client.databases.query(
        database_id=database_id,

    )
    results = response.get("results")
    if shuffle:
        random.shuffle(results)
    element_list = []
    for element_dict in results:
        element_list.append(DataBaseRow.from_dict(element_dict))
        if max_elements is not None and max_elements >= len(element_list):
            break
    return element_list
