from dataclasses import dataclass
from typing import List
from enum import Enum


class PropertyType(Enum):
    SELECT = 1
    CHECKBOX = 2
    URL = 3
    TITLE = 4

@dataclass
class DataBaseProperty:
    """Local class for Notion db property"""
    name: str
    id: str
    type: PropertyType

    @classmethod
    def list_from_dict(cls: type, notion_dict: dict)->List:
        for key in notion_dict:
            print(key, '->', )
            cls.from_dict(notion_dict[key])
        return[cls.from_dict(notion_dict[key])for key in notion_dict]  

    @classmethod
    def from_dict(cls: type, notion_dict: dict):
        notion_dict.get('name')
        _type = PropertyType[notion_dict.get("type")] if notion_dict.get("type") in PropertyType._value2member_map_ else None
        return cls(name=notion_dict.get('name'), id=notion_dict.get('id'), type=_type)
