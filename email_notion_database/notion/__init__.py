from typing import Optional
import os
from notion_client import Client
from . import databases

client = None

def init_client(token:Optional[str]=None, env_var:Optional[str]=None)-> Client:
    global client
    _token = token or os.environ[env_var]
    client = Client(auth=_token)

__all__= [
    'databases'
]