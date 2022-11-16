from pydantic import BaseModel
from fastapi import APIRouter, Depends
from queries.user_queries import UserQueries
# from typing import Optional

class User(BaseModel):
    id : int
    username : str
    password : str
    email : str


class UserIn(BaseModel):
    id : int
    username : str
    password : str
    email : str


class UserOut(BaseModel):
    user: list[User]

router = APIRouter()

# user = {
#     'id' : 1,
#     'username' : 'curtis',
#     'password' : 'password',
#     'email' : 'curtis@gmail.com',
# }

@router.get('/users',response_model=UserOut)

@router.get('/users{id}', response_model=User)
def get_user_by_id(id: int = 0):
    return User #idk if this should be user or User


# creating new user
@router.post('/users', response_model=User) 
def create_user(
    new_user: UserIn,
    queries: UserQueries = Depends()
):
    return queries.create(new_user)

# @router.get('/hello_world')
# def hello_world():
#     return 'hello world'

# @router.get_absolute_url(self):
#     return reverse("model_detail", kwargs={"pk": self.pk})
