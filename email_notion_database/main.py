#!/usr/bin/env python3
import sys
import argparse
import random
from typing import Any, List

import email_notion_database.notion
import email_notion_database.email_client
from email_notion_database.notion.row import DataBaseRow
from email_notion_database.model.email import Email

from . import composer


parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-to','--token', help="Integration token", type=str)
parser.add_argument('-ev', '--env-var', help="Environment variable that contains integration token", type=str)
parser.add_argument('-ser', '--email-server', help="Email server", type=str)
parser.add_argument('-po', '--email-port', help="Email port", type=int)
parser.add_argument('-sa', '--sender-address', help="Sender address", type=str)
parser.add_argument('-sn', '--sender-name', help="Sender name", type=str)
parser.add_argument('-sp', '--sender-password', help="Sender password", type=str)
parser.add_argument('-su', '--subject', help="Email subject", type=str)
parser.add_argument('-ta', '--target-address', help="Target address", type=str)
parser.add_argument('-et', '--email-title', help="Email title", type=str)
parser.add_argument('-eh', '--email-header', help="Email header", type=str)
parser.add_argument('-nr', '--number-rows', help="Number or rows to send", type=str)
parser.add_argument('-nd', '--notion-db-id', help="Number or rows to send", type=str)

def get_database_rows(token: str, notion_database_id: str, number_of_rows: int) -> List[DataBaseRow]:
    email_notion_database.notion.init_client(token)
    if notion_database_id:
        database_list = [{'id': notion_database_id}]
    else:
        database_list = email_notion_database.notion.databases.get_list()
    elements = []
    for db in database_list:
        db_elements = email_notion_database.notion.databases.get_elements(db.get('id'), number_of_rows, shuffle=True)
        elements = elements + db_elements
        if len(elements) > number_of_rows:
            break
    return elements[0:min(len(elements)-1,number_of_rows-1)]

def send_email(elements: List[DataBaseRow], email_server: str, email_address: str, sender_name: str, sender_password: str, email_port: int, target_address: str, subject: str, title:str, header: str) -> None:
    
    email_notion_database.email_client.init_client(server_address=email_server, user_email=email_address, user_name=sender_name, password=sender_password, port=email_port)
    html, plain = composer.compose_content(elements, Email(title=title, header=header))
    email_notion_database.email_client.send_email(target_address, html, plain, subject=subject)

def get_database_send_email(notion_token: str,
        notion_database_id: str,
        email_server: str,
        email_address: str,
        sender_name: str,
        sender_password: str,
        email_port: int,
        target_address: str,
        subject: str,
        title:str,
        header: str,
        number_of_rows: int=5):
    elements = get_database_rows(notion_token, notion_database_id, number_of_rows)
    send_email(elements, email_server, email_address, sender_name, sender_password, email_port, target_address, subject, title, header )

def main(arguments):

    args = parser.parse_args(arguments)
    # Notion parameters
    token = mandatory(args.token)
    notion_database_id = args.notion_db_id or None
    # Email parameters
    email_server = mandatory(args.email_server)
    email_port = args.email_port or 465
    email_address = mandatory(args.sender_address)
    sender_name = mandatory(args.sender_name)
    sender_password  = mandatory(args.sender_password)
    subject = mandatory(args.subject)
    target_address = mandatory(args.target_address)
    # Html parameters
    title = mandatory(args.email_title)
    header = mandatory(args.email_header)
    number_rows = int(args.number_rows) or 5

    get_database_send_email(token, notion_database_id, email_server, email_address, sender_name, sender_password, email_port, target_address, subject, title, header, number_rows)


class MissingParameterError(Exception):
    pass

def mandatory(field: Any):
    if field is None:
        raise MissingParameterError()
    return field

if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except MissingParameterError:
        parser.print_help()
