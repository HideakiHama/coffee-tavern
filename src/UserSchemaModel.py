import pydantic as _pydantic
import datetime as _dt
from typing import List

class _PostBase(_pydantic.BaseModel):
    title : str
    content : str

# Some example
# {
#     "id": 1,
#     "owner_id": 23,
#     "title" : "this is th title",
#     "content" : "some content for the post"
# }

class PostCreate(_PostBase):
    pass 

class Post(_PostBase):
    id : int
    owner_id : int
    date_created: _dt.datetime
    date_last_updated : _dt.datetime

    class Config:
        orm_mode = True #orm set to True because default is False. This is to make sure we are getting the post from the User Model
    

class _UserBase(_pydantic.BaseModel):
    email : str

class UserCreates(_UserBase):
    password : str

class User(_UserBase): ## do not want to return password here (this is to list the user)
    id : int
    posts : List[Post] = [] ## [] for if no post

    class Config:
        orm_mode = True


