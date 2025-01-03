from pydantic import BaseModel
from typing import List


class Links(BaseModel):
    links_scrape: List[str]
    links_search: List[str]
