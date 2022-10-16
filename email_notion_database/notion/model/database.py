from dataclasses import dataclass
from typing import List, Any, Optional
from email_notion_database.notion.property import DataBaseProperty
from email_notion_database.utils import retrieve_url_preview
from email_notion_database.notion.pages import get_page, get_page_content


@dataclass
class DataBase:
    """Local class for Notion db"""
    properties: List[DataBaseProperty]

    @classmethod
    def from_dict(cls: type, notion_dict: dict):
        properties = []
        if notion_dict.get("properties"):
            properties = DataBaseProperty.from_dict(notion_dict.get("properties"))
        return cls(properties=properties)
