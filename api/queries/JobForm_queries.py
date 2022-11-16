from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool

class JobPostForm(BaseModel):
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: Optional[str]

#response shape
class JobPostFormIn(BaseModel):
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: Optional[str]

class Tags(BaseModel):
    tag: str
