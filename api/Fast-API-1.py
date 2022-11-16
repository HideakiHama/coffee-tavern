from fastapi import FastAPI
from models import User

user_db = [
    User(
        id = 1,
        username = 'curtis_the_user',
        password = 'e=mc^2',
        email = 'curtis_thd_user@gmail.com')
        ]


class UserQueries:
    def get_all_users(self):
        return user_db


app = FastAPI()

# @app.get('/users') ## this is the path sending get request to the /user --> this will invoke a function
# def get_users():
#     user_list = list(user_db.values()) ## grabs all user information data
#     return user_list

# @app.get('/users/{username}') ## {username} is placeholder. This is for looking for specific user
# def get_user_path(username: str): # str is telling python this parameter is a string
#     return user_db[username]

# ## uvicorn main:app --reload 
# ## hints for fastapi
# ## 1. FastAPI automatically converts data to the required type.
# ## 2. When data is invalid, FastAPI proveds a utomatic errors.
# ## 3. Editors like PyCharm provides support including type checks and autompletion
