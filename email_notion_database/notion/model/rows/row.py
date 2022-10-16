from dataclasses import dataclass
from pathlib import Path
from typing import List, Any, Optional
from email_notion_database.utils import retrieve_url_preview
from email_notion_database.notion.pages import get_page, get_page_content


@dataclass
class DataBaseRow:
    """Local class for Notion db row"""
    title: str
    description: str
    url: str
    url_title: str
    url_description: str
    url_image: str
    url_favicon: str

    __template_path: str = Path(__file__).parent.parent.parent.parent / "./templates/figure.html"

    def get_template_path(self)->str:
        return self.__template_path

    @classmethod
    def from_dict(cls: type, notion_dict: dict):
        title_dict = cls.__get_dict_property(dict_list=notion_dict, property_type="title")
        _title = ""
        if title_dict is not None and title_dict.get('title') is not None and len(title_dict.get('title')) > 0:
           _title = title_dict.get('title')[0].get("plain_text") 

        _url = ""
        _url_title = ""
        _url_description = ""
        _url_image = ""
        _url_favicon = ""
        url_dict = cls.__get_dict_property(dict_list=notion_dict, property_type="url")
        if url_dict is not None:
            url = url_dict.get("url")
            if url is not None:
                _url = url
                url_title, url_description, url_image, _url_favicon = retrieve_url_preview(_url)
                _url_description = url_description or ""
                _url_title = url_title or ""
                _url_image = url_image or ""
        content = get_page_content(get_page(notion_dict.get("id"))) or ""
        return cls(title=_title, description=content, url=_url, url_title=_url_title, url_description=_url_description, url_image=_url_image, url_favicon=_url_favicon)
    
    @classmethod
    def __get_dict_property(cls: type, dict_list: List, property_name: Optional[str]= None, property_type: Optional[str]= None)-> Any:
        properties = dict_list.get('properties')
        for key in properties.keys():
            property_object = properties.get(key)
            if not property_type == property_object.get("type"):
                continue 
            if not property_name ==  property_object.get("name"):
                continue
            return property_object
        return None
