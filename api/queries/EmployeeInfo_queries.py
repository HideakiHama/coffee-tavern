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
    # account_id: int       --> current user id
    
class EmployeeInfoRepo:
    def create(self, info: EmployeeInfoIn) -> Union[List[EmployeeInfoOut], Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO employee_info
                            (career_title, location, education, about)
                        VALUES
                            (%s, %s, %s, %s);
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                        ],
                    )
                    # get current user id
                    return EmployeeInfoOut(**info.dict())
        except Exception:
            return {"message": "Create did not work"}