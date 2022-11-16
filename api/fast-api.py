/api/main.py
from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)

/api/routers/users.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from db import UserQueries

router = APIRouter()

# CREATE TABLE users (
# id INTEGER NOT NULL UNIQUE,
# first TEXT NOT NULL,
# last TEXT NOT NULL,
# avatar TEXT NOT NULL,
# email TEXT NOT NULL,
# username TEXT NOT NULL,
# referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE,=
#);

class UserOut(BaseModel):
    id: int
    first: str
    last: str
    avatar: str
    email: str
    username: str
    #referrer_id: int

class UsersOut(BaseModel):
    users: list[UserOut]

@router.get("/api/users", response_model=UsersOut)
def users_list(
    queries: UserQueries = Depends()
):
    return UsersOut(users = queries.get_all_users())

/api/db.py
import psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class UserQueries:
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(

                )
                results = list()

                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                    results.append(record)
                return results
