from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool


class Error(BaseModel):
    message: str

class EmployeeInfoIn(BaseModel):
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]

class EmployeeInfoOut(BaseModel):
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]
    account_id: int
    
class EmployeeInfoRepo:
    def create(self, info: EmployeeInfoIn, account_id: int) -> Union[List[EmployeeInfoOut], Error]:
        print("::::::", info)
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO employee_info
                            (career_title, location, education, about, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s);
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            account_id
                        ],
                    )
                    # get current user id
                    return EmployeeInfoOut(**info.dict())
        except Exception:
            return {"message": "Create did not work"}