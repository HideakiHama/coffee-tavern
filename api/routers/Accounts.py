from fastapi import FastAPI, Form, APIRouter

router = APIRouter()


@router.post("/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}

# @router.post('/createUser')
# def create_user():

@router.post('/jobPost')
def create_job_post():
    pass


user_db = {
    'curtis': {'username': 'curtis', 'location': ' Alameda', 'age': '28' }
}

@router.get('/users') ## this is the path sending get request to the /user --> this will invoke a function
def get_users():
    user_list = list(user_db.values()) ## grabs all user information data
    return user_list

@router.get('/users/{username}') ## {username} is placeholder. This is for looking for specific user
def get_user_path(username: str): # str is telling python this parameter is a string
    return user_db[username]

# uvicorn main:app --reload
## hints for fastapi
## 1. FastAPI automatically converts data to the required type.
## 2. When data is invalid, FastAPI proveds a utomatic errors.
## 3. Editors like PyCharm provides support including type checks and autompletion
