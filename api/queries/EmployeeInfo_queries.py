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
                        RETURNING id;
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            account_id
                        ],
                    )
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Create did not work"}
        
    
    def update(self, info: EmployeeInfoIn, account_id: int) -> Union[List[EmployeeInfoOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE employee_info
                        SET 
                            career_title = %s, 
                            location = %s, 
                            education = %s, 
                            about = %s
                        WHERE account_id = (%s);
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            account_id
                        ]
                    )
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Update did not work"}
