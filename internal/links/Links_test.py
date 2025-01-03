from pydantic import BaseModel
from typing import List, Dict, Tuple


class BaseParametersLinks(BaseModel):
    parameters: Dict[str, str] = {'key': 'value'}


class Links(BaseModel):
    links_scrape_test: List[str] = ['https://synapsenet.ru/organizacii/1217700195020-ooo-si-mobajl']
    links_search_test: Tuple[str, Dict[str, str]]

