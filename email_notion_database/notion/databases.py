from typing import List, Dict, Any
import random
from unittest import result

import email_notion_database.notion
from email_notion_database.notion.model.database import DataBase
from email_notion_database.notion.model.rows import DataBaseRow


def get_list()-> List:
    """ Using the Search endpoint, collect all the databases available for this integration token """
    response = email_notion_database.notion.client.search()
    database_list = []
    for notion_object in response['results']:
        if notion_object['object'] == "database":
            database_list.append(notion_object)
    return database_list

def get(database_id: str)-> Any:
    return DataBase.from_dict(email_notion_database.notion.client.databases.retrieve(database_id))

def get_elements(database_id: str, max_elements: int = None, shuffle: bool=False, filter: Dict = None)-> List[DataBaseRow]:
    response = email_notion_database.notion.client.databases.query(
        database_id=database_id,
        filter=filter
    )
    results = response.get("results")
    if shuffle:
        random.shuffle(results)
    element_list = []
    for element_dict in results:
        element_list.append(DataBaseRow.from_dict(element_dict))
        if max_elements is not None and len(element_list) >= max_elements:
            break
    return element_list
