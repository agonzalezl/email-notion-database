from typing import List
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

def get_elements(database_id)-> List[DataBaseRow]:
    response = email_notion_database.notion.client.databases.query(
        database_id=database_id,

    )
    element_list = []
    for element_dict in response.get("results"):
        element_list.append(DataBaseRow.from_dict(element_dict))
    return element_list
