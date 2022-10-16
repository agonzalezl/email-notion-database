
from pathlib import Path
from typing import List, Optional

from email_notion_database.notion.model.rows import DataBaseRow
from email_notion_database.model import Email

def compose_content(database_rows: List[DataBaseRow], email_data: Email):
    email_html = load_email_template()
    email_html, _ = populate_email(email_html, email_data)
    figure_list = ""
    plain_list = ""
    for row in database_rows:
        figure = load_figure_template(row.get_template_path())
        figure_html, plain = populate_figure_fields(figure, row)
        figure_list += figure_html
        plain_list += "\n" + plain

    email_html = email_html.replace("{{email_content}}", figure_list)
    return email_html, plain_list

def load_figure_template(path: Optional[Path] = None):
    _path = path or Path(__file__).parent / "./templates/figure.html"
    return _path.open().read()

def load_email_template():
    path = Path(__file__).parent / "./templates/email.html"
    return path.open().read()

def populate_email(email_string: str, email_data: Email):
    email_string = email_string.replace("{{page_title}}", email_data.title).replace("{{page_header}}", email_data.header)
    email_string = email_string.replace("{{page_footer}}", email_data.page_footer)
    return email_string, "plain"

def populate_figure_fields(figure_string: str, row: DataBaseRow):
    figure_string = figure_string.replace("{{title}}", row.title).replace("{{content}}", row.description).replace("{{site_url}}", row.url)
    figure_string = figure_string.replace("{{site_title}}", row.url_title).replace("{{site_description}}", row.url_description)
    figure_string = figure_string.replace("{{site_image}}", row.url_image).replace("{{url_favicon}}", row.url_favicon)  
    return figure_string, row.title+": "+row.url
