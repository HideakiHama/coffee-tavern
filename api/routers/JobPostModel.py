from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool


class JobPostForm(BaseModel):
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: Optional[str]

class Tags(BaseModel):
    tag: str
