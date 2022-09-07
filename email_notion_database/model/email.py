
from dataclasses import dataclass
from typing import List, Any, Optional
from email_notion_database.utils import retrieve_url_preview
from email_notion_database.notion.pages import get_page, get_page_content

@dataclass
class Email:
    """ Model for storing email information"""
    title: str = ""
    header: str = ""
    page_footer: str = ""
