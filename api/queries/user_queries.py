from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool

class Error(BaseModel):
    message: str
    
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
    
class UserQueries:
    def get_one(self, user_id: int) -> Optional[UserOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT id
                             , name
                             , from_date
                             , to_date
                             , thoughts
                        FROM vacations
                        WHERE id = %s
                        """,
                        [vacation_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_vacation_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that vacation"}