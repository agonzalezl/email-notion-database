from typing import Dict, List
import email_notion_database.notion


def get_page(page_id)-> List:
    """ Using the Search endpoint, collect all the databases available for this integration token """
    response = email_notion_database.notion.client.blocks.children.list(page_id)
    return response

def get_page_content(page_dict: Dict)->str:
    n_paragraphs = 0
    final_content = ""
    for result in page_dict.get("results"):
        paragraph = result.get("paragraph")
        if paragraph == None:
            continue
        if rich_text:=paragraph.get("rich_text"):
            if len(rich_text) != 0:
                final_content += rich_text[0].get("text").get("content") + "\n"
                n_paragraphs += 1
        if n_paragraphs > 2:
            break
    return final_content
